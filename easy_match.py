from match.RothPeranson import MatchController

def run_match():
    print("This script uses the files in the easy_match folder.")
    print("You can use them as templates, extending to however many bigs/littles are required.")
    print("\n")
    print("In the big list with twin toggle list all of the bigs in the first column and add how many littles they may be paired with. 1 for one little. 2 for twins. etc.")
    print("In the big preference list. Put the bigs names in the first row and there preferences in the column under their names in the order of their little preferences from first to last. Do not input the no's.")
    print("In the pnm preference list. Put the PNMs names in the first row and their preferences in the column under their names int he order of their little preferences from first to last.")
    print("\n")
    print("The filenames cannot be changed or this script will fail to run.")
    print("If you get a KeyError it's likely due to a misspelled Candidate or Program in a ROL.")
    print("\n")

    program_rol = 'easy_match/big_preferences.csv'
    candidate_rol = 'easy_match/pnm_preferences.csv'
    program_places = 'easy_match/big_list_with_twin_toggle.csv'

    match = MatchController(program_rol, candidate_rol, program_places)
    match.start_match()
    results = match.results_dict()

    print(results)
    match.get_output_csv()

if __name__ == '__main__':
    run_match()
