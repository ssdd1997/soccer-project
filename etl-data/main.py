import pandas as pd
import sqlite3

from constants import Constants


class Database:

    def __init__(self):
        self.cursor = None
        self.connector = None
        self.db_name = "../soccer_database"

    def connect(self):
        self.connector = sqlite3.connect(self.db_name)
        self.cursor = self.connector.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.connector.commit()

    def close(self):
        self.connector.close()


class Extractor:

    def extract(self):
        df_key_stats = pd.read_csv('key_stats.csv', encoding='utf-8')
        df_goalkeeper_stats = pd.read_csv('goalkeeping.csv', encoding='utf-8', usecols=['player_name', 'saved', 'conceded'])
        df_total = pd.merge(df_key_stats, df_goalkeeper_stats, on='player_name', how='left')
        return df_total


class Loader:

    def __init__(self, df, database):
        self._df = df
        self._database = database

    def _prepare_tables_database(self):
        self._database.execute_query(Constants.QUERY_CLUBS)
        self._database.execute_query(Constants.QUERY_POSITIONS)
        self._database.execute_query(Constants.QUERY_PLAYERS)
        self._database.execute_query(Constants.TRUNCATE_CLUBS)
        self._database.execute_query(Constants.TRUNCATE_POSITIONS)
        self._database.execute_query(Constants.TRUNCATE_PLAYERS)


    def load(self):
        self._database.connect()
        self._prepare_tables_database()
        df_teams = self._df['club'].drop_duplicates().reset_index(drop=True)
        df_positions = self._df['position'].drop_duplicates().reset_index(drop=True)
        df_teams.to_sql('t_clubs', self._database.connector, if_exists='append', index_label='id_club', index=True)
        df_positions.to_sql('t_positions', self._database.connector, if_exists='append', index_label='id_position', index=True)
        df_players = self._df.merge(df_teams.reset_index().rename(columns = {'index':'fk_club'}), on='club', how='left')
        df_players = df_players.merge(df_positions.reset_index().rename(columns = {'index':'fk_position'}), on='position', how='left')
        del df_players['club']
        del df_players['position']
        df_players = df_players.reset_index(drop=True)
        df_players.to_sql('t_players', self._database.connector, if_exists='append', index_label='id_player', index=True)
        self._database.close()

if __name__ == '__main__':
    extractor = Extractor()
    df = extractor.extract()
    database = Database()
    loader = Loader(df, database)
    loader.load()