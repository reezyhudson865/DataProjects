from database import get_connection
from players import view_player_seasons

#---------------player vs team analytics--------------
def compare_player_to_team():
    print("Compare Stats:")
    print("1. Passing")
    print("2. Rushing")
    print("3. Receiving")

    choice = input("Enter choice: ")

    view_player_seasons()
    player_season_id = input("Enter player season ID: ")

    connection = get_connection()
    cursor = connection.cursor()

    # passing stats vs team
    if choice == "1":
        cursor.execute(
            """SELECT PASSING_STATS.passing_attempts,
            PASSING_STATS.completions,
            PASSING_STATS.passing_yards,
            PASSING_STATS.passing_touchdowns,
            PASSING_STATS.interceptions,
            TEAM_PASSING_STATS.passing_attempts,
            TEAM_PASSING_STATS.completions,
            TEAM_PASSING_STATS.passing_yards,
            TEAM_PASSING_STATS.passing_touchdowns,
            TEAM_PASSING_STATS.interceptions
            FROM PLAYER_SEASON
            JOIN PASSING_STATS
            ON PLAYER_SEASON.player_season_id = PASSING_STATS.player_season_id
            JOIN TEAM_PASSING_STATS
            ON PLAYER_SEASON.team_season_id = TEAM_PASSING_STATS.team_season_id
            WHERE PLAYER_SEASON.player_season_id = ?""",
            (player_season_id,)
        )

        result = cursor.fetchone()

        if result:
            print("Player vs. Team Passing Stats")
            print(f"Passing Attempts: Player {result[0]} | Team {result[5]}")
            print(f"Completions: Player {result[1]} | Team {result[6]}")
            print(f"Passing Yards: Player {result[2]} | Team {result[7]}")
            print(f"Passing Touchdowns: Player {result[3]} | Team {result[8]}")
            print(f"Interceptions: Player {result[4]} | Team {result[9]}")
        else:
            print("Passing stats not found.")

    # rushing stats vs team
    elif choice == "2":
        cursor.execute(
            """SELECT RUSHING_STATS.rushing_attempts,
            RUSHING_STATS.rushing_yards,
            RUSHING_STATS.rushing_touchdowns,
            TEAM_RUSHING_STATS.rushing_attempts,
            TEAM_RUSHING_STATS.rushing_yards,
            TEAM_RUSHING_STATS.rushing_touchdowns
            FROM PLAYER_SEASON
            JOIN RUSHING_STATS
            ON PLAYER_SEASON.player_season_id = RUSHING_STATS.player_season_id
            JOIN TEAM_RUSHING_STATS
            ON PLAYER_SEASON.team_season_id = TEAM_RUSHING_STATS.team_season_id
            WHERE PLAYER_SEASON.player_season_id = ?""",
            (player_season_id,)
        )

        result = cursor.fetchone()

        if result:
            print("Player vs. Team Rushing Stats")
            print(f"Rushing Attempts: Player {result[0]} | Team {result[3]}")
            print(f"Rushing Yards: Player {result[1]} | Team {result[4]}")
            print(f"Rushing Touchdowns: Player {result[2]} | Team {result[5]}")
        else:
            print("Rushing stats not found.")

    # receiving stats vs team
    elif choice == "3":
        cursor.execute(
            """SELECT RECEIVING_STATS.receptions,
            RECEIVING_STATS.receiving_yards,
            RECEIVING_STATS.receiving_touchdowns,
            TEAM_RECEIVING_STATS.receptions,
            TEAM_RECEIVING_STATS.receiving_yards,
            TEAM_RECEIVING_STATS.receiving_touchdowns
            FROM PLAYER_SEASON
            JOIN RECEIVING_STATS
            ON PLAYER_SEASON.player_season_id = RECEIVING_STATS.player_season_id
            JOIN TEAM_RECEIVING_STATS
            ON PLAYER_SEASON.team_season_id = TEAM_RECEIVING_STATS.team_season_id
            WHERE PLAYER_SEASON.player_season_id = ?""",
            (player_season_id,)
        )

        result = cursor.fetchone()

        if result:
            print("Player vs. Team Receiving Stats")
            print(f"Receptions: Player {result[0]} | Team {result[3]}")
            print(f"Receiving Yards: Player {result[1]} | Team {result[4]}")
            print(f"Receiving Touchdowns: Player {result[2]} | Team {result[5]}")
        else:
            print("Receiving stats not found.")

    else:
        print("Invalid choice.")

    connection.close()

#------------players vs conference analytics---------
def compare_player_to_conference():
    print("Compare Stats:")
    print("1. Passing")
    print("2. Rushing")
    print("3. Receiving")

    choice = input("Enter choice: ")

    view_player_seasons()
    player_season_id = input("Enter player season ID: ")

    connection = get_connection()
    cursor = connection.cursor()

#passing stats vs conference
    if choice == "1":
        cursor.execute(
            """SELECT PASSING_STATS.passing_attempts,
            PASSING_STATS.completions,
            PASSING_STATS.passing_yards,
            PASSING_STATS.passing_touchdowns,
            PASSING_STATS.interceptions,
            COLLEGE_TEAM.conference_id,
            TEAM_SEASON.season
            FROM PLAYER_SEASON
            JOIN PASSING_STATS
            ON PLAYER_SEASON.player_season_id = PASSING_STATS.player_season_id
            JOIN TEAM_SEASON
            ON PLAYER_SEASON.team_season_id = TEAM_SEASON.team_season_id
            JOIN COLLEGE_TEAM
            ON TEAM_SEASON.team_id = COLLEGE_TEAM.team_id
            WHERE PLAYER_SEASON.player_season_id = ?""",
            (player_season_id,)
        )

        player_result = cursor.fetchone()

        if player_result:
            conference_id = player_result[5]
            season = player_result[6]

            cursor.execute(
                """SELECT AVG(TEAM_PASSING_STATS.passing_attempts),
                AVG(TEAM_PASSING_STATS.completions),
                AVG(TEAM_PASSING_STATS.passing_yards),
                AVG(TEAM_PASSING_STATS.passing_touchdowns),
                AVG(TEAM_PASSING_STATS.interceptions)
                FROM TEAM_PASSING_STATS
                JOIN TEAM_SEASON
                ON TEAM_PASSING_STATS.team_season_id = TEAM_SEASON.team_season_id
                JOIN COLLEGE_TEAM
                ON TEAM_SEASON.team_id = COLLEGE_TEAM.team_id
                WHERE COLLEGE_TEAM.conference_id = ?
                AND TEAM_SEASON.season = ?""",
                (conference_id, season)
            )

            conference_result = cursor.fetchone()

            if conference_result[0] is not None:
                print("Player vs. Conference Average Passing Stats")
                print(f"Passing Attempts: Player {player_result[0]} | Conference Average {conference_result[0]}")
                print(f"Completions: Player {player_result[1]} | Conference Average {conference_result[1]}")
                print(f"Passing Yards: Player {player_result[2]} | Conference Average {conference_result[2]}")
                print(f"Passing Touchdowns: Player {player_result[3]} | Conference Average {conference_result[3]}")
                print(f"Interceptions: Player {player_result[4]} | Conference Average {conference_result[4]}")

            else:
                print("No conference statistics available for this season.")
        else:
            print("Passing stats not found.")

#rushing stats vs conference
    elif choice == "2":
        cursor.execute(
            """SELECT RUSHING_STATS.rushing_attempts,
            RUSHING_STATS.rushing_yards,
            RUSHING_STATS.rushing_touchdowns,
            COLLEGE_TEAM.conference_id,
            TEAM_SEASON.season
            FROM PLAYER_SEASON
            JOIN RUSHING_STATS
            ON PLAYER_SEASON.player_season_id = RUSHING_STATS.player_season_id
            JOIN TEAM_SEASON
            ON PLAYER_SEASON.team_season_id = TEAM_SEASON.team_season_id
            JOIN COLLEGE_TEAM
            ON TEAM_SEASON.team_id = COLLEGE_TEAM.team_id
            WHERE PLAYER_SEASON.player_season_id = ?""",
            (player_season_id,)
        )

        player_result = cursor.fetchone()

        if player_result:
            conference_id = player_result[3]
            season = player_result[4]

            cursor.execute(
                """SELECT AVG(TEAM_RUSHING_STATS.rushing_attempts),
                AVG(TEAM_RUSHING_STATS.rushing_yards),
                AVG(TEAM_RUSHING_STATS.rushing_touchdowns)
                FROM TEAM_RUSHING_STATS
                JOIN TEAM_SEASON
                ON TEAM_RUSHING_STATS.team_season_id = TEAM_SEASON.team_season_id
                JOIN COLLEGE_TEAM
                ON TEAM_SEASON.team_id = COLLEGE_TEAM.team_id
                WHERE COLLEGE_TEAM.conference_id = ?
                AND TEAM_SEASON.season = ?""",
                (conference_id, season)
            )

            conference_result = cursor.fetchone()

            if conference_result[0] is not None:
                print("Player vs. Conference Average Rushing Stats")
                print(f"Rushing Attempts: Player {player_result[0]} | Conference Average {conference_result[0]}")
                print(f"Rushing Yards: Player {player_result[1]} | Conference Average {conference_result[1]}")
                print(f"Rushing Touchdowns: Player {player_result[2]} | Conference Average {conference_result[2]}")

            else:
                print("No conference rushing statistics available for this season.")
        else:
            print("Rushing stats not found.")

#receiving stats vs conference
    elif choice == "3":
        cursor.execute(
            """SELECT RECEIVING_STATS.receptions,
            RECEIVING_STATS.receiving_yards,
            RECEIVING_STATS.receiving_touchdowns,
            COLLEGE_TEAM.conference_id,
            TEAM_SEASON.season
            FROM PLAYER_SEASON
            JOIN RECEIVING_STATS
            ON PLAYER_SEASON.player_season_id = RECEIVING_STATS.player_season_id
            JOIN TEAM_SEASON
            ON PLAYER_SEASON.team_season_id = TEAM_SEASON.team_season_id
            JOIN COLLEGE_TEAM
            ON TEAM_SEASON.team_id = COLLEGE_TEAM.team_id
            WHERE PLAYER_SEASON.player_season_id = ?""",
            (player_season_id,)
        )

        player_result = cursor.fetchone()

        if player_result:
            conference_id = player_result[3]
            season = player_result[4]

            cursor.execute(
                """SELECT AVG(TEAM_RECEIVING_STATS.receptions),
                AVG(TEAM_RECEIVING_STATS.receiving_yards),
                AVG(TEAM_RECEIVING_STATS.receiving_touchdowns)
                FROM TEAM_RECEIVING_STATS
                JOIN TEAM_SEASON
                ON TEAM_RECEIVING_STATS.team_season_id = TEAM_SEASON.team_season_id
                JOIN COLLEGE_TEAM
                ON TEAM_SEASON.team_id = COLLEGE_TEAM.team_id
                WHERE COLLEGE_TEAM.conference_id = ?
                AND TEAM_SEASON.season = ?""",
                (conference_id, season)
            )

            conference_result = cursor.fetchone()

            if conference_result[0] is not None:
                print("Player vs. Conference Average Receiving Stats")
                print(f"Receptions: Player {player_result[0]} | Conference Average {conference_result[0]}")
                print(f"Receiving Yards: Player {player_result[1]} | Conference Average {conference_result[1]}")
                print(f"Receiving Touchdowns: Player {player_result[2]} | Conference Average {conference_result[2]}")

            else:
                print("No conference receiving statistics available for this season.")

    else:
        print("Invalid choice.")

    connection.close()

#---------------stats by position-------------
def view_stats_by_position():
    print("Positions: QB, RB, WR, TE")
    position = input("Enter position: ")

    connection = get_connection()
    cursor = connection.cursor()

#QB stats
    if position == "QB":
        cursor.execute(
            """SELECT PLAYER.first_name,
            PLAYER.last_name,
            TEAM_SEASON.season,
            PASSING_STATS.passing_attempts,
            PASSING_STATS.completions,
            PASSING_STATS.passing_yards,
            PASSING_STATS.passing_touchdowns,
            PASSING_STATS.interceptions
            FROM PLAYER_SEASON
            JOIN PLAYER
            ON PLAYER_SEASON.player_id = PLAYER.player_id
            JOIN TEAM_SEASON
            ON PLAYER_SEASON.team_season_id = TEAM_SEASON.team_season_id
            JOIN PASSING_STATS
            ON PLAYER_SEASON.player_season_id = PASSING_STATS.player_season_id
            WHERE PLAYER_SEASON.position = ?""",
            (position,)
        )

        results = cursor.fetchall()

        for player in results:
            print(f"{player[0]} {player[1]} | Season: {player[2]}")
            print(f"Attempts: {player[3]} | Completions: {player[4]} | "
                  f"Yards: {player[5]} | TDs: {player[6]} | INTs: {player[7]}")

#RB stats
    elif position == "RB":
        cursor.execute(
            """SELECT PLAYER.first_name,
            PLAYER.last_name,
            TEAM_SEASON.season,
            RUSHING_STATS.rushing_attempts,
            RUSHING_STATS.rushing_yards,
            RUSHING_STATS.rushing_touchdowns
            FROM PLAYER_SEASON
            JOIN PLAYER
            ON PLAYER_SEASON.player_id = PLAYER.player_id
            JOIN TEAM_SEASON
            ON PLAYER_SEASON.team_season_id = TEAM_SEASON.team_season_id
            JOIN RUSHING_STATS
            ON PLAYER_SEASON.player_season_id = RUSHING_STATS.player_season_id
            WHERE PLAYER_SEASON.position = ?""",
            (position,)
        )

        results = cursor.fetchall()

        for player in results:
            print(f"{player[0]} {player[1]} | Season: {player[2]}")
            print(f"Attempts: {player[3]} | Yards: {player[4]} | TDs: {player[5]}")

#WR stats
    elif position == "WR":
        cursor.execute(
            """SELECT PLAYER.first_name,
            PLAYER.last_name,
            TEAM_SEASON.season,
            RECEIVING_STATS.receptions,
            RECEIVING_STATS.receiving_yards,
            RECEIVING_STATS.receiving_touchdowns
            FROM PLAYER_SEASON
            JOIN PLAYER
            ON PLAYER_SEASON.player_id = PLAYER.player_id
            JOIN TEAM_SEASON
            ON PLAYER_SEASON.team_season_id = TEAM_SEASON.team_season_id
            JOIN RECEIVING_STATS
            ON PLAYER_SEASON.player_season_id = RECEIVING_STATS.player_season_id
            WHERE PLAYER_SEASON.position = ?""",
            (position,)
        )

        results = cursor.fetchall()

        for player in results:
            print(f"{player[0]} {player[1]} | Season: {player[2]}")
            print(f"Receptions: {player[3]} | Yards: {player[4]} | TDs: {player[5]}")

#TE stats
    elif position == "TE":
        cursor.execute(
            """SELECT PLAYER.first_name,
            PLAYER.last_name,
            TEAM_SEASON.season,
            RECEIVING_STATS.receptions,
            RECEIVING_STATS.receiving_yards,
            RECEIVING_STATS.receiving_touchdowns
            FROM PLAYER_SEASON
            JOIN PLAYER
            ON PLAYER_SEASON.player_id = PLAYER.player_id
            JOIN TEAM_SEASON
            ON PLAYER_SEASON.team_season_id = TEAM_SEASON.team_season_id
            JOIN RECEIVING_STATS
            ON PLAYER_SEASON.player_season_id = RECEIVING_STATS.player_season_id
            WHERE PLAYER_SEASON.position = ?""",
            (position,)
        )

        results = cursor.fetchall()

        for player in results:
            print(f"{player[0]} {player[1]} | Season: {player[2]}")
            print(f"Receptions: {player[3]} | Yards: {player[4]} | TDs: {player[5]}")

    else:
        print("Invalid position.")

    connection.close()


#-----------ranking players function------------
def rank_players():
    print("Rank Players:")
    print("1. Quarterbacks")
    print("2. Running Backs")
    print("3. Wide Receivers")
    print("4. Tight Ends")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Rank Quarterbacks By:")
        print("1. Passing Yards")
        print("2. Passing Touchdowns")

        stat_choice = input("Enter choice: ")

        if stat_choice == "1":
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                """SELECT PLAYER.first_name,
                PLAYER.last_name,
                TEAM_SEASON.season,
                PASSING_STATS.passing_yards
                FROM PLAYER_SEASON
                JOIN PLAYER
                ON PLAYER_SEASON.player_id = PLAYER.player_id
                JOIN TEAM_SEASON
                ON PLAYER_SEASON.team_season_id = TEAM_SEASON.team_season_id
                JOIN PASSING_STATS
                ON PLAYER_SEASON.player_season_id = PASSING_STATS.player_season_id
                WHERE PLAYER_SEASON.position = ?
                ORDER BY PASSING_STATS.passing_yards DESC""",
                ("QB",)
            )

            results = cursor.fetchall()

            if not results:
                print("No players found for this position or statistic.")


            for player in results:
                print(f"{player[0]} {player[1]} | "
                      f"Season: {player[2]} | Passing Yards: {player[3]}")

            connection.close()

        elif stat_choice == "2":
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                """SELECT PLAYER.first_name,
                PLAYER.last_name,
                TEAM_SEASON.season,
                PASSING_STATS.passing_touchdowns
                FROM PLAYER_SEASON
                JOIN PLAYER
                ON PLAYER_SEASON.player_id = PLAYER.player_id
                JOIN TEAM_SEASON
                ON PLAYER_SEASON.team_season_id = TEAM_SEASON.team_season_id
                JOIN PASSING_STATS
                ON PLAYER_SEASON.player_season_id = PASSING_STATS.player_season_id
                WHERE PLAYER_SEASON.position = ?
                ORDER BY PASSING_STATS.passing_touchdowns DESC""",
                ("QB",)
            )

            results = cursor.fetchall()

            if not results:
                print("No players found for this position or statistic.")

            for player in results:
                print(f"{player[0]} {player[1]} | "
                      f"Season: {player[2]} | Passing TDs: {player[3]}")

            connection.close()

    elif choice == "2":
        print("Rank Running Backs By:")
        print("1. Rushing Yards")
        print("2. Rushing Touchdowns")

        stat_choice = input("Enter choice: ")

        if stat_choice == "1":
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                """SELECT PLAYER.first_name,
                PLAYER.last_name,
                TEAM_SEASON.season,
                RUSHING_STATS.rushing_yards
                FROM PLAYER_SEASON
                JOIN PLAYER
                ON PLAYER_SEASON.player_id = PLAYER.player_id
                JOIN TEAM_SEASON
                ON PLAYER_SEASON.team_season_id = TEAM_SEASON.team_season_id
                JOIN RUSHING_STATS
                ON PLAYER_SEASON.player_season_id = RUSHING_STATS.player_season_id
                WHERE PLAYER_SEASON.position = ?
                ORDER BY RUSHING_STATS.rushing_yards DESC""",
                ("RB",)
            )

            results = cursor.fetchall()

            if not results:
                print("No players found for this position or statistic.")

            for player in results:
                print(f"{player[0]} {player[1]} | "
                      f"Season: {player[2]} | Rushing Yards: {player[3]}")

            connection.close()

        elif stat_choice == "2":
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                """SELECT PLAYER.first_name,
                PLAYER.last_name,
                TEAM_SEASON.season,
                RUSHING_STATS.rushing_touchdowns
                FROM PLAYER_SEASON
                JOIN PLAYER
                ON PLAYER_SEASON.player_id = PLAYER.player_id
                JOIN TEAM_SEASON
                ON PLAYER_SEASON.team_season_id = TEAM_SEASON.team_season_id
                JOIN RUSHING_STATS
                ON PLAYER_SEASON.player_season_id = RUSHING_STATS.player_season_id
                WHERE PLAYER_SEASON.position = ?
                ORDER BY RUSHING_STATS.rushing_touchdowns DESC""",
                ("RB",)
            )

            results = cursor.fetchall()

            if not results:
                print("No players found for this position or statistic.")

            for player in results:
                print(f"{player[0]} {player[1]} | "
                      f"Season: {player[2]} | Rushing TDs: {player[3]}")

            connection.close()

    elif choice == "3":
        print("Rank Wide Receivers By:")
        print("1. Receiving Yards")
        print("2. Receiving Touchdowns")

        stat_choice = input("Enter choice: ")

        if stat_choice == "1":
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                """SELECT PLAYER.first_name,
                PLAYER.last_name,
                TEAM_SEASON.season,
                RECEIVING_STATS.receiving_yards
                FROM PLAYER_SEASON
                JOIN PLAYER
                ON PLAYER_SEASON.player_id = PLAYER.player_id
                JOIN TEAM_SEASON
                ON PLAYER_SEASON.team_season_id = TEAM_SEASON.team_season_id
                JOIN RECEIVING_STATS
                ON PLAYER_SEASON.player_season_id = RECEIVING_STATS.player_season_id
                WHERE PLAYER_SEASON.position = ?
                ORDER BY RECEIVING_STATS.receiving_yards DESC""",
                ("WR",)
            )

            results = cursor.fetchall()

            if not results:
                print("No players found for this position or statistic.")

            for player in results:
                print(f"{player[0]} {player[1]} | "
                      f"Season: {player[2]} | Receiving Yards: {player[3]}")

            connection.close()

        elif stat_choice == "2":
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                """SELECT PLAYER.first_name,
                PLAYER.last_name,
                TEAM_SEASON.season,
                RECEIVING_STATS.receiving_touchdowns
                FROM PLAYER_SEASON
                JOIN PLAYER
                ON PLAYER_SEASON.player_id = PLAYER.player_id
                JOIN TEAM_SEASON
                ON PLAYER_SEASON.team_season_id = TEAM_SEASON.team_season_id
                JOIN RECEIVING_STATS
                ON PLAYER_SEASON.player_season_id = RECEIVING_STATS.player_season_id
                WHERE PLAYER_SEASON.position = ?
                ORDER BY RECEIVING_STATS.receiving_touchdowns DESC""",
                ("WR",)
            )

            results = cursor.fetchall()

            if not results:
                print("No players found for this position or statistic.")

            for player in results:
                print(f"{player[0]} {player[1]} | "
                      f"Season: {player[2]} | Receiving TDs: {player[3]}")

            connection.close()

    elif choice == "4":
        print("Rank Tight Ends By:")
        print("1. Receiving Yards")
        print("2. Receiving Touchdowns")

        stat_choice = input("Enter choice: ")

        if stat_choice == "1":
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                """SELECT PLAYER.first_name,
                PLAYER.last_name,
                TEAM_SEASON.season,
                RECEIVING_STATS.receiving_yards
                FROM PLAYER_SEASON
                JOIN PLAYER
                ON PLAYER_SEASON.player_id = PLAYER.player_id
                JOIN TEAM_SEASON
                ON PLAYER_SEASON.team_season_id = TEAM_SEASON.team_season_id
                JOIN RECEIVING_STATS
                ON PLAYER_SEASON.player_season_id = RECEIVING_STATS.player_season_id
                WHERE PLAYER_SEASON.position = ?
                ORDER BY RECEIVING_STATS.receiving_yards DESC""",
                ("TE",)
            )

            results = cursor.fetchall()

            if not results:
                print("No players found for this position or statistic.")

            for player in results:
                print(f"{player[0]} {player[1]} | "
                      f"Season: {player[2]} | Receiving Yards: {player[3]}")

            connection.close()

        elif stat_choice == "2":
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                """SELECT PLAYER.first_name,
                PLAYER.last_name,
                TEAM_SEASON.season,
                RECEIVING_STATS.receiving_touchdowns
                FROM PLAYER_SEASON
                JOIN PLAYER
                ON PLAYER_SEASON.player_id = PLAYER.player_id
                JOIN TEAM_SEASON
                ON PLAYER_SEASON.team_season_id = TEAM_SEASON.team_season_id
                JOIN RECEIVING_STATS
                ON PLAYER_SEASON.player_season_id = RECEIVING_STATS.player_season_id
                WHERE PLAYER_SEASON.position = ?
                ORDER BY RECEIVING_STATS.receiving_touchdowns DESC""",
                ("TE",)
            )

            results = cursor.fetchall()

            if not results:
                print("No players found for this position or statistic.")

            for player in results:
                print(f"{player[0]} {player[1]} | "
                      f"Season: {player[2]} | Receiving TDs: {player[3]}")

            connection.close()

    else:
        print("Invalid choice.")
