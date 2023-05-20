from chessdotcom import get_leaderboards
import pprint

printer = pprint.PrettyPrinter()

def get_Leaderboard():
    data = get_leaderboards().json
    categories = data['leaderboards']
    daiy_leaderboards = categories ['daily']
    for i in daiy_leaderboards:
        print(f" {i['rank']} Username = {i['username']} Score {i['score']}")

get Leaderboard()
