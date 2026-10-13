# Database file
import sqlite3


# db connection
def get_connection():
    connection = sqlite3.connect('college_football.db')
    connection.execute('PRAGMA foreign_keys = ON')
    return connection


# schema
# create tables
def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    #Conference Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS CONFERENCE (
                    conference_id INTEGER PRIMARY KEY,
                    conference_name TEXT UNIQUE
                    )
                ''')
    #add conferences
    conferences = [
        'ACC',
        'AAC',
        'Big 12',
        'Big Ten',
        'Conference USA',
        'Mid-American',
        'Mountain West',
        'Pac-12',
        'SEC',
        'Sun Belt',
        'FBS Independents'
    ]
    for conference in conferences:
        cursor.execute('INSERT OR IGNORE INTO CONFERENCE (conference_name) VALUES (?)', (conference,))

    #College Team Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS COLLEGE_TEAM (
                    team_id INTEGER PRIMARY KEY,
                    conference_id INTEGER,
                    team_name TEXT,
                    city TEXT,
                    state TEXT,

                    FOREIGN KEY(conference_id) REFERENCES CONFERENCE(conference_id)
                )
                ''')

    #Team Season Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS TEAM_SEASON (
                    team_season_id INTEGER PRIMARY KEY,
                    team_id INTEGER,
                    season INTEGER,

                    UNIQUE(team_id, season),

                    FOREIGN KEY(team_id) REFERENCES COLLEGE_TEAM(team_id)
                    ON DELETE CASCADE)
                ''')

    #Player table
    cursor.execute('''CREATE TABLE IF NOT EXISTS PLAYER (
                    player_id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT
                    )
                   ''')

    #Player Season Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS PLAYER_SEASON (
                    player_season_id INTEGER PRIMARY KEY,
                    player_id INTEGER,
                    team_season_id INTEGER,
                    class_rank TEXT,
                    position TEXT,
                    height INTEGER,
                    weight INTEGER,

                    UNIQUE(player_id, team_season_id),

                    FOREIGN KEY(player_id) REFERENCES PLAYER(player_id)
                        ON DELETE CASCADE,
                    FOREIGN KEY(team_season_id) REFERENCES TEAM_SEASON(team_season_id)
                    ON DELETE CASCADE)
                ''')

    #Passing Stats Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS PASSING_STATS (
                    player_season_id INTEGER PRIMARY KEY,
                    passing_attempts INTEGER,
                    completions INTEGER,
                    passing_yards INTEGER,
                    passing_touchdowns INTEGER,
                    interceptions INTEGER,

                    FOREIGN KEY (player_season_id) REFERENCES PLAYER_SEASON(player_season_id)
                    ON DELETE CASCADE
                    )
                ''')

    #Rushing Stats Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS RUSHING_STATS (
                    player_season_id INTEGER PRIMARY KEY,
                    rushing_attempts INTEGER,
                    rushing_yards INTEGER,
                    rushing_touchdowns INTEGER,

                    FOREIGN KEY (player_season_id) REFERENCES PLAYER_SEASON(player_season_id)
                    ON DELETE CASCADE
                    )
                ''')

    #Receiving Stats Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS RECEIVING_STATS (
                    player_season_id INTEGER PRIMARY KEY,
                    receptions INTEGER,
                    receiving_yards INTEGER,
                    receiving_touchdowns INTEGER,

                    FOREIGN KEY (player_season_id) REFERENCES PLAYER_SEASON(player_season_id)
                    ON DELETE CASCADE
                    )
                ''')

    #Combine Stats Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS COMBINE_STATS (
                    combine_id INTEGER PRIMARY KEY,
                    player_id INTEGER,
                    combine_year INTEGER,
                    forty_yard_dash REAL,
                    bench_press_reps INTEGER,
                    vertical_jump REAL,

                    UNIQUE(player_id, combine_year),

                    FOREIGN KEY(player_id) REFERENCES PLAYER(player_id)
                    ON DELETE CASCADE
                    )
                ''')

    #Team Passing Stats table
    cursor.execute('''CREATE TABLE IF NOT EXISTS TEAM_PASSING_STATS (
                        team_season_id INTEGER PRIMARY KEY,
                        passing_attempts INTEGER,
                        completions INTEGER,
                        passing_yards INTEGER,
                        passing_touchdowns INTEGER,
                        interceptions INTEGER,
                        
                        FOREIGN KEY (team_season_id) REFERENCES TEAM_SEASON(team_season_id)
                        ON DELETE CASCADE
                        )
                    ''')

    #Team Rushing Stats table
    cursor.execute('''CREATE TABLE IF NOT EXISTS TEAM_RUSHING_STATS (
                        team_season_id INTEGER PRIMARY KEY,
                        rushing_attempts INTEGER,
                        rushing_yards INTEGER,
                        rushing_touchdowns INTEGER,
    
                        FOREIGN KEY (team_season_id) REFERENCES TEAM_SEASON(team_season_id)
                        ON DELETE CASCADE
                        )
                    ''')

    #Team Receiving Stats table

    cursor.execute("""CREATE TABLE IF NOT EXISTS TEAM_RECEIVING_STATS (
                        team_season_id INTEGER PRIMARY KEY,
                        receptions INTEGER,
                        receiving_yards INTEGER,
                        receiving_touchdowns INTEGER,
                        
                        FOREIGN KEY (team_season_id) REFERENCES TEAM_SEASON(team_season_id)
                        ON DELETE CASCADE
                        )
                    """)

    connection.commit()
    connection.close()




create_table()