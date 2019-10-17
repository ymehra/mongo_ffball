import requests
import pandas as pd
import numpy as np
import json
import plotly
import plotly.graph_objs as go
from plotly.offline import plot, iplot

def get_data(league_id, year):
   url = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/2019/segments/0/leagues/' + str(league_id)
   teams = requests.get(url).json()
   matches = requests.get(url, params={"view":"mMatchup"}).json()
   return teams, matches

def id_to_names(teams):
   names = {}
   for i in teams['teams']:
      names[i['id']] = i['location'] + ' ' + i['nickname']
   return names

def matches_to_df(matches):
   df = [[
        game['matchupPeriodId'],
        game['home']['teamId'], game['home']['totalPoints'],
        game['away']['teamId'], game['away']['totalPoints']
   ] for game in matches['schedule']]
   df = pd.DataFrame(df, columns=['Week', 'Team1', 'Score1', 'Team2', 'Score2'])
   df['Type'] = ['Regular' if w<=14 else 'Playoff' for w in df['Week']]
   return df

def get_teams_and_matches_dfs(league_id, year):
   teams, matches = get_data(league_id, year)
   df_matches = matches_to_df(matches)
   names = id_to_names(teams)
   df_matches = df_matches.replace({'Team1':names})
   df_matches = df_matches.replace({'Team2':names})

   return teams, df_matches, names

def margins_plot(matches, names):
   margins = matches.assign(Margin1 = matches['Score1'] - matches['Score2'],
                Margin2 = matches['Score2'] - matches['Score1'])
   margins = (margins[['Week', 'Team1', 'Margin1', 'Type']]
      .rename(columns={'Team1': 'Team', 'Margin1': 'Margin'})
      .append(margins[['Week', 'Team2', 'Margin2', 'Type']]
      .rename(columns={'Team2': 'Team', 'Margin2': 'Margin'}))
   )
   margins = margins[margins.Margin != 0]

   traces = []
   for i in margins.Team.unique():
      traces.append(go.Box(
         y=margins[margins.Team == i].Margin
         ,name = i
         ,boxpoints='all'
         ,jitter=0.5
         ,whiskerwidth=0.2
         ,marker=dict(size=2)
         ,line=dict(width=1)
      ))
   graphJSON = json.dumps(traces, cls=plotly.utils.PlotlyJSONEncoder)
   return graphJSON




