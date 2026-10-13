from multiprocessing import connection

from database import get_connection
from players import view_players

#add combine stats
def add_combine_stats():
    view_players()

    player_id = input("Enter player's ID: ")
    combine_year = input("Enter combine year: ")
    forty_yard_dash = input("Enter forty yard dash time: ")
    bench_press_reps = input("Enter number of bench press reps: ")
    vertical_jump = input("Enter vertical jump height in inches: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """SELECT combine_id FROM COMBINE_STATS
        WHERE player_id = ? AND combine_year = ?""",
        (player_id, combine_year)
    )

    if cursor.fetchone() is not None:
        print("Combine statistics already exist for this player and year.")
        connection.close()
        return

    cursor.execute(
        """INSERT INTO COMBINE_STATS
        (player_id, combine_year, forty_yard_dash, bench_press_reps, vertical_jump)
        VALUES (?, ?, ?, ?, ?)""",
        (player_id, combine_year, forty_yard_dash, bench_press_reps, vertical_jump)
    )

    connection.commit()
    print('Combine stats added.')
    connection.close()

#combine participation
#see if a player participated in the combine
def check_combine_participation():
    view_players()

    player_id = input("Enter player's ID: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""SELECT combine_year, forty_yard_dash, bench_press_reps, vertical_jump
    FROM COMBINE_STATS
    WHERE player_id = ?""",
                   (player_id,)
    )

    result = cursor.fetchone()

    if result:
        print('Player participated in the combine.')
        print(f'Combine year: {result[0]}')
        print(f'40 Yard Dash: {result[1]}')
        print(f'Bench Press Reps: {result[2]}')
        print(f'Vertical Jump: {result[3]}')
    else:
        print('Player did not participate in the combine.')
    connection.close()