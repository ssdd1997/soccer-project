class Constants:
    KEY_STATS_COLUMNS = ['player_name','club','position','minutes_played','match_played','goals','assists']

    TRUNCATE_CLUBS = """DELETE FROM t_clubs;"""
    TRUNCATE_POSITIONS = """DELETE FROM t_positions;"""
    TRUNCATE_PLAYERS = """DELETE FROM t_players;"""

    QUERY_CLUBS = """CREATE TABLE IF NOT EXISTS t_clubs
                      (
                        id_club   integer 
                        constraint t_clubs_pk
                            primary key,
                        club VARCHAR(150) null
                        
                    );"""

    QUERY_POSITIONS = """ CREATE TABLE IF NOT EXISTS t_positions
                              (
                                id_position   int,
                                position VARCHAR(100) null,
                                constraint t_positions_pk
                                    primary key (id_position)
                            );"""

    QUERY_PLAYERS = """CREATE TABLE IF NOT EXISTS t_players
(
    id_player        integer
        constraint t_players_pk
            primary key,
    player_name      varchar(200),
    minutes_played   integer,
    match_played     integer,
    goals             integer,
    assists          integer,
    saved            integer,
    conceded         integer,
    fk_club          integer
        constraint table_name_t_clubs_id_club_fk
            references t_clubs,
    fk_position      integer
        constraint table_name_t_positions_id_position_fk
            references t_positions
);

"""