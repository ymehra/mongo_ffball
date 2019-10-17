from flask import Flask
from flask import render_template
from ffball import *

app = Flask(__name__)

@app.route('/')
def index():
   df_teams, df_matches, names = get_teams_and_matches_dfs(119974, 2019)
   graphJSON  = margins_plot(df_matches, names)
   return render_template('index.html', graphJSON = graphJSON)

if __name__ == '__main__':
   app.run(debug=True)
