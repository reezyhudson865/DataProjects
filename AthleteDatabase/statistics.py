from database import get_connection
from players import view_player_seasons

#view player seasons connection
def view_player_seasons():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""SELECT PLAYER_SEASON.player_season_id,
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
        print(f'ID: {player_season[0]}, {player_season[1]}, {player_season[2]}, {player_season[3]}, {player_season[4]}, {player_season[5]}')

    connection.close()

#time to add stats tables!!!!

#add passing stats
def add_passing_stats():
    view_player_seasons()

    player_season_id = input("Enter Player Season ID: ")
    passing_attempts = input("Enter passing attempts: ")
    completions = input("Enter completions: ")
    passing_yards = input("Enter passing yards: ")
    passing_touchdowns = input("Enter passing touchdowns: ")
    interceptions = input("Enter interceptions: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(f"""INSERT INTO PASSING_STATS
                    (player_season_id, passing_attempts, completions, passing_yards, passing_touchdowns, interceptions)
                    VALUES (?, ?, ?, ?, ?, ?)""",
                   (player_season_id, passing_attempts, completions, passing_yards, passing_touchdowns, interceptions)
                   )

    connection.commit()
    print("Passing stats added")
    connection.close()

#add rushing stats
def add_rushing_stats():
    view_player_seasons()

    player_season_id = input("Enter Player Season ID: ")
    rushing_attempts = input("Enter rushing attempts: ")
    rushing_yards = input("Enter rushing yards: ")
    rushing_touchdowns = input("Enter rushing touchdowns: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""INSERT INTO RUSHING_STATS
                    (player_season_id, rushing_attempts, rushing_yards, rushing_touchdowns)
                    VALUES (?, ?, ?, ?)""",
                   (player_season_id, rushing_attempts, rushing_yards, rushing_touchdowns)
                   )

    connection.commit()
    print("Rushing stats added")
    connection.close()

#add receiving stats
def add_receiving_stats():
    view_player_seasons()

    player_season_id = input("Enter Player Season ID: ")
    receptions = input("Enter receptions: ")
    receiving_yards = input("Enter receiving yards: ")
    receiving_touchdowns = input("Enter receiving touchdowns: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""INSERT INTO RECEIVING_STATS
                    (player_season_id, receptions, receiving_yards, receiving_touchdowns)
                    VALUES (?, ?, ?, ?)""",
                   (player_season_id, receptions, receiving_yards, receiving_touchdowns)
                   )

    connection.commit()
    print("Receiving stats added")
    connection.close()

#updating player stats function
def update_player_stats():
    print('Update Stats:')
    print('1.Passing 2.Rushing 3.Receiving')

    choice = int(input("Enter your choice: "))

    if choice not in [1, 2, 3]:
        print("Invalid choice.")
        return

    view_player_seasons()
    player_season_id = input("Enter Player Season ID: ")

    connection = get_connection()
    cursor = connection.cursor()

    if choice == 1:
        passing_attempts = input("Enter new passing attempts: ")
        completions = input("Enter new completions: ")
        passing_yards = input("Enter new passing yards: ")
        passing_touchdowns = input("Enter new passing touchdowns: ")
        interceptions = input("Enter new passing interceptions: ")

        cursor.execute("""UPDATE PASSING_STATS
                            SET passing_attempts = ?,
                            completions = ?,
                            passing_yards = ?,
                            passing_touchdowns = ?,
                            interceptions = ?
                            WHERE player_season_id = ?""",
                       (passing_attempts, completions, passing_yards,
                        passing_touchdowns, interceptions, player_season_id)
                       )

    elif choice == 2:
        rushing_attempts = input("Enter new rushing attempts: ")
        rushing_yards = input("Enter new rushing yards: ")
        rushing_touchdowns = input("Enter new rushing touchdowns: ")

        cursor.execute("""UPDATE RUSHING_STATS
                        SET rushing_attempts = ?,
                        rushing_yards = ?,
                        rushing_touchdowns = ?
                        WHERE player_season_id = ?""",
                       (rushing_attempts, rushing_yards,
                        rushing_touchdowns, player_season_id)
                       )

    elif choice == 3:
        receptions = input("Enter new receptions: ")
        receiving_yards = input("Enter new receiving yards: ")
        receiving_touchdowns = input("Enter new receiving touchdowns: ")

        cursor.execute("""UPDATE RECEIVING_STATS
                        SET receptions = ?,
                        receiving_yards = ?,
                        receiving_touchdowns = ?
                        WHERE player_season_id = ?""",
                       (receptions, receiving_yards,
                        receiving_touchdowns, player_season_id)
                       )

    connection.commit()
    print("Player stats updated successfully.")
    connection.close()


# view players function
# user friendly
def view_players():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT player_id, first_name, last_name FROM PLAYER")

    players = cursor.fetchall()

    for player in players:
        print(f'ID: {player[0]}, {player[1]}, {player[2]}')

    connection.close()
