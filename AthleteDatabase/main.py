from players import add_player, add_player_season, search_player, remove_player
from teams import add_team, add_team_season, remove_team, add_team_passing_stats, add_team_rushing_stats, add_team_receiving_stats
from statistics import add_passing_stats, add_rushing_stats, add_receiving_stats, update_player_stats
from combine import add_combine_stats, check_combine_participation
from analytics import compare_player_to_team, compare_player_to_conference, view_stats_by_position, rank_players

#-----------------Main-------------------
def menu():
    while True:
        print("\nCollege Football Player Database")
        print("1. Player Options")
        print("2. Team Options")
        print("3. Statistics")
        print("4. Combine")
        print("5. Analytics")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\nPlayer Options")
            print("1. Add Player")
            print("2. Add Player Season")
            print("3. Search Player")
            print("4. Remove Player")

            player_choice = input("Enter choice: ")

            if player_choice == "1":
                add_player()

            elif player_choice == "2":
                add_player_season()

            elif player_choice == "3":
                search_player()

            elif player_choice == "4":
                remove_player()

            else:
                print("Invalid choice.")

        elif choice == "2":
            print("\nTeam Options")
            print("1. Add Team")
            print("2. Add Team Season")
            print("3. Remove Team")

            team_choice = input("Enter choice: ")

            if team_choice == "1":
                add_team()

            elif team_choice == "2":
                add_team_season()

            elif team_choice == "3":
                remove_team()

            else:
                print("Invalid choice.")

        elif choice == "3":
            print("\nStatistics")
            print("1. Add Player Passing Stats")
            print("2. Add Player Rushing Stats")
            print("3. Add Player Receiving Stats")
            print("4. Update Player Stats")
            print("5. Add Team Passing Stats")
            print("6. Add Team Rushing Stats")
            print("7. Add Team Receiving Stats")

            stats_choice = input("Enter choice: ")

            if stats_choice == "1":
                add_passing_stats()

            elif stats_choice == "2":
                add_rushing_stats()

            elif stats_choice == "3":
                add_receiving_stats()

            elif stats_choice == "4":
                update_player_stats()

            elif stats_choice == "5":
                add_team_passing_stats()

            elif stats_choice == "6":
                add_team_rushing_stats()

            elif stats_choice == "7":
                add_team_receiving_stats()

            else:
                print("Invalid choice.")

        elif choice == "4":
            print("\nCombine")
            print("1. Add Combine Stats")
            print("2. Check Combine Participation")

            combine_choice = input("Enter choice: ")

            if combine_choice == "1":
                add_combine_stats()

            elif combine_choice == "2":
                check_combine_participation()

            else:
                print("Invalid choice.")

        elif choice == "5":
            print("\nAnalytics")
            print("1. Compare Player to Team")
            print("2. Compare Player to Conference Average")
            print("3. View Stats by Position")
            print("4. Rank Players")

            analytics_choice = input("Enter choice: ")

            if analytics_choice == "1":
                compare_player_to_team()

            elif analytics_choice == "2":
                compare_player_to_conference()

            elif analytics_choice == "3":
                view_stats_by_position()

            elif analytics_choice == "4":
                rank_players()

            else:
                print("Invalid choice.")

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")


menu()