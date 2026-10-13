from database import get_connection

#adding a conference
def add_conference():
    conference_name = input("Enter your conference name: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO CONFERENCE (conference_name) VALUES (?)", (conference_name,))

    connection.commit()
    print("Conference successfully added.")
    connection.close()

#view our conferences
#user friendly: good for users to display the possible conferences
def view_conference():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT conference_id, conference_name FROM CONFERENCE")

    conferences = cursor.fetchall()

    for conference in conferences:
        print(f"ID: {conference[0]} - {conference[1]}")

    connection.close()

#add teams
def add_team():
    view_conference()

    conference_id = input("Enter conference ID: ")
    team_name = input("Enter team name: ")
    city = input("Enter city: ")
    state = input("Enter state: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO COLLEGE_TEAM
                        (conference_id, team_name, city, state)
                        VALUES (?, ?, ?, ?)''',
                        (conference_id, team_name, city, state))

    connection.commit()
    print("Team successfully added.")
    connection.close()

#view the teams
#user friendly
def view_teams():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT team_id, team_name FROM COLLEGE_TEAM")

    teams = cursor.fetchall()

    for team in teams:
        print(f"ID: {team[0]} - {team[1]}")

    connection.close()

#add a team season
def add_team_season():
    view_teams()

    team_id = input("Enter team ID: ")
    season = input("Enter season year: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''INSERT INTO TEAM_SEASON
                    (team_id, season)
                    VALUES (?, ?)''', (team_id, season))

    connection.commit()
    print("Team season successfully added.")
    connection.close()

#view team seasons
#user friendly
def view_team_season():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''SELECT TEAM_SEASON.team_season_id,
                        COLLEGE_TEAM.team_name,
                        TEAM_SEASON.season,
                        CONFERENCE.conference_name
                        FROM TEAM_SEASON
                        JOIN COLLEGE_TEAM
                        ON TEAM_SEASON.team_id = COLLEGE_TEAM.team_id
                        JOIN CONFERENCE
                        ON COLLEGE_TEAM.conference_id = CONFERENCE.conference_id'''
                   )

    team_seasons = cursor.fetchall()

    for team_season in team_seasons:
        print(f"ID: {team_season[0]} | {team_season[1]} | {team_season[2]} | {team_season[3]}")

    connection.close()

#remove team function
def remove_team():
    view_teams()

    team_id = input("Enter team ID: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''DELETE FROM COLLEGE_TEAM WHERE team_id = ?''', (team_id,))

    connection.commit()
    print("Team removed.")
    connection.close()

#add team passing stats function
def add_team_passing_stats():
    view_team_season()

    team_season_id = input("Enter team season ID: ")
    passing_attempts = input("Enter passing attempts: ")
    completions = input("Enter completions: ")
    passing_yards = input("Enter passing yards: ")
    passing_touchdowns = input("Enter passing touchdowns: ")
    interceptions = input("Enter interceptions: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """INSERT INTO TEAM_PASSING_STATS
        (team_season_id, passing_attempts, completions, passing_yards,
        passing_touchdowns, interceptions)
        VALUES (?, ?, ?, ?, ?, ?)""",
        (team_season_id, passing_attempts, completions, passing_yards,
         passing_touchdowns, interceptions)
    )

    connection.commit()
    print("Team passing stats added.")
    connection.close()

#add teaming rushing stats function
def add_team_rushing_stats():
    view_team_season()

    team_season_id = input("Enter team season ID: ")
    rushing_attempts = input("Enter rushing attempts: ")
    rushing_yards = input("Enter rushing yards: ")
    rushing_touchdowns = input("Enter rushing touchdowns: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """INSERT INTO TEAM_RUSHING_STATS
        (team_season_id, rushing_attempts, rushing_yards, rushing_touchdowns)
        VALUES (?, ?, ?, ?)""",
        (team_season_id, rushing_attempts, rushing_yards, rushing_touchdowns)
    )

    connection.commit()
    print("Team rushing stats added.")
    connection.close()

def add_team_receiving_stats():
    view_team_season()

    team_season_id = input("Enter team season ID: ")
    receptions = input("Enter receptions: ")
    receiving_yards = input("Enter receiving yards: ")
    receiving_touchdowns = input("Enter receiving touchdowns: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """INSERT INTO TEAM_RECEIVING_STATS
        (team_season_id, receptions, receiving_yards, receiving_touchdowns)
        VALUES (?, ?, ?, ?)""",
        (team_season_id, receptions, receiving_yards, receiving_touchdowns)
    )

    connection.commit()
    print("Team receiving stats added.")
    connection.close()

