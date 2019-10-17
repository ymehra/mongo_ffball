import requests, json

LEAGUE_ID = '119974'

PREV_URL = 'https://fantasy.espn.com/apis/v3/games/ffl/leagueHistory/'

CURRENT_URL = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/2019/segments/0/leagues/'

# TODO: Fix for prev years
def get_teams(leagueId = LEAGUE_ID, season = 2019):
    if season == 2019:
        url = CURRENT_URL + str(leagueId)
    else:
        url = PREV_URL + str(leagueId) + "?seasonId=" + str(season)
    print(url)

    return requests.get(url).json()

teams = get_teams()


def test_all_season():
    teams = get_teams()
    seasons = [2015, 2016, 2017, 2018, 2019]
    for i in seasons:
        filename = str(i) + '.json'
        with open(filename, 'w') as f:
            team = get_teams(season = i)
            json.dump(team, f)