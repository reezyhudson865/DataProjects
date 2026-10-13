#player table programming

from database import get_connection
from teams import view_team_season

#add fixed data

#player positions
positions = [
    'QB',
    'RB',
    'WR',
    'TE'
]

#class ranks
class_ranks = [
    'Freshman',
    'Sophomore',
    'Junior',
    'Senior',
    'Fifth-Year'
]


#adding a player
def add_player():
    first_name = input("Enter player's first name: ")
    last_name = input("Enter player's last name: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO PLAYER (first_name, last_name) VALUES (?, ?)", (first_name, last_name))

    connection.commit()
    print("Player successfully added.")
    connection.close()


#searching for a player
def search_player():
    print('Search Player By:')
    print('1.Name 2.School 3.Class Rank')

    choice = input("Enter choice: ")

    connection = get_connection()
    cursor = connection.cursor()


    if choice == '1':
        last_name = input("Enter player's last name: ")

        cursor.execute("""SELECT player_id, first_name, Last_name
                       FROM PLAYER
                       WHERE last_name = ?""", (last_name,)
                       )

    elif choice == '2':
        school = input("Enter player's school: ")

        cursor.execute("""SELECT DISTINCT PLAYER.player_id, PLAYER.first_name, PLAYER.Last_name
                            FROM PLAYER
                            JOIN PLAYER_SEASON
                            on PLAYER.player_id = PLAYER_SEASON.player_id
                            JOIN TEAM_SEASON
                            ON PLAYER_SEASON.team_season_ID = TEAM_SEASON.team_season_ID
                            JOIN COLLEGE_TEAM
                            ON TEAM_SEASON.team_id = COLLEGE_TEAM.team_ID
                            WHERE COLLEGE_TEAM.team_name = ?""",
                       (school,)
                       )

    elif choice == '3':
        print('Class ranks: Freshman, Sophomore, Junior, Senior, Fifth-Year')
        class_rank = input("Enter class rank: ")

        cursor.execute("""SELECT DISTINCT player.player_id, PLAYER.first_name, PLAYER.last_name
                            FROM PLAYER
                            JOIN PLAYER_SEASON
                            ON PLAYER.player_id = PLAYER_SEASON.player_id
                            WHERE PLAYER_SEASON.class_rank = ?""",
                       (class_rank,)
                       )
    else:
        print('Invalid choice.')
        connection.close()
        return

    results = cursor.fetchall()

    if results:
        for player in results:
            print(f'ID: {player[0]}, {player[1]}, {player[2]}')
    else:
        print("No players found")

    connection.close()

#removing a player
def remove_player():
    player_id = input("Enter player's ID: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM PLAYER WHERE player_id = ?", (player_id,))

    connection.commit()
    print("Player successfully removed.")
    connection.close()

#adding player season stats
def add_player_season():
    view_players()
    player_id = input("Enter player's ID: ")

    view_team_season()
    team_season_id = input("Enter team season ID: ")

   #class rank choices
    print('Class ranks: Freshman, Sophomore, Junior, Senior, Fifth-Year')
    class_rank = input("Enter class rank: ")

    #positions choices
    print('Positions: QB, RB, WR, TE')
    position = input("Enter position: ")

    #physical
    height = input("Enter height in inches: ")
    weight = input("Enter weight in pounds: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT player_id FROM PLAYER WHERE player_id = ?",
        (player_id,)
    )

    #check if player id exists
    if cursor.fetchone() is None:
        print("Invalid player ID. Player does not exist.")
        connection.close()
        return

    #check if team season exists
    cursor.execute(
        "SELECT team_season_id FROM TEAM_SEASON WHERE team_season_id = ?",
        (team_season_id,)
    )

    if cursor.fetchone() is None:
        print("Invalid Team Season ID. Team season does not exist.")
        connection.close()
        return


    cursor.execute("""INSERT INTO PLAYER_SEASON (player_id, team_season_id, class_rank, position, height, weight) VALUES (?, ?, ?, ?, ?, ?)""",
                   (player_id, team_season_id, class_rank, position, height, weight)
                   )

    connection.commit()
    print("Player season added successfully.")
    connection.close()


#view players
def view_players():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT player_id, first_name, last_name FROM PLAYER"
    )

    players = cursor.fetchall()

    for player in players:
        print(f"ID: {player[0]} | {player[1]} {player[2]}")

    connection.close()

#view player seasons
def view_player_seasons():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """SELECT PLAYER_SEASON.player_season_id,
        PLAYER.first_name,
        PLAYER.last_name,
        COLLEGE_TEAM.team_name,
        TEAM_SEASON.season,
        PLAYER_SEASON.position
        FROM PLAYER_SEASON
        JOIN PLAYER
        ON PLAYER_SEASON.player_id = PLAYER.player_id
        JOIN TEAM_SEASON
        ON PLAYER_SEASON.team_season_id = TEAM_SEASON.team_season_id
        JOIN COLLEGE_TEAM
        ON TEAM_SEASON.team_id = COLLEGE_TEAM.team_id"""
    )

    player_seasons = cursor.fetchall()

    for player_season in player_seasons:
        print(f"ID: {player_season[0]} | {player_season[1]} {player_season[2]} | "
              f"{player_season[3]} | {player_season[4]} | {player_season[5]}")

    connection.close()