#from _typeshed import Self
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#import matplotlib.patches as patches
import seaborn as sns
import os 


class football:
    def __init__(self):
        # Get top scorers in Ligue 1 (ID season = 4242)
        self.url_topscorers = "https://elenasport-io1.p.rapidapi.com/v2/seasons/4242/topscorers"

        # Get all the leagues available
        self.url_leagues = "https://elenasport-io1.p.rapidapi.com/v2/leagues"

        # Get data for Ligue 1 (ID = 263)
        self.url_league_id = "https://elenasport-io1.p.rapidapi.com/v2/leagues/263"

        # Get all the seasons available
        self.url_season = "https://elenasport-io1.p.rapidapi.com/v2/seasons"

        # Get the current players in Ligue 1 2021 - 2022
        self.url_players = "https://elenasport-io1.p.rapidapi.com/v2/seasons/4242/players"

        # Get the current teams in Ligue 1 2021 - 2022
        self.url_teams = "https://elenasport-io1.p.rapidapi.com/v2/seasons/4242/teams"

        # Get all the fixtures in Ligue 1 2021 - 2022
        self.url_fixtures_season = "https://elenasport-io1.p.rapidapi.com/v2/seasons/4242/fixtures"

        ###Store of valid endpoints
        #self.maxime = ""
        #self.franck = ""

    def collect_data(self,url):
        """
        function to collect all the produced from that API
        input: url (The reference to the desired data to be collected)
        output: data table of collected sets of data.
        """
        querystring = {"page":"1"}
        headers = {
        'x-rapidapi-host': "elenasport-io1.p.rapidapi.com",
        'x-rapidapi-key': ""
        }
        i = 2
        response = requests.request("GET", url, headers=headers, params=querystring)
        response_list = response.json()["data"]
        response_df = pd.DataFrame(response_list)
        while response.status_code == 200 and response.json()["pagination"]["hasNextPage"] == True:
            querystring = {"page":str(i)}
            response = requests.request("GET", url, headers=headers, params=querystring)
            try:
                response_df = response_df.append(pd.DataFrame(response.json()["data"]), ignore_index=True)
                #print(response.json()["data"])
                print("page:", i)
                i += 1
            except:
                continue
        return response_df


    def save(self):
        """
        Function to save each visualization produced.
        It just takes into consideration, the file
        withs associated extension
        """  
        plt.tight_layout()
        plt.subplots_adjust(top=0.85)
        os.path.join(os.getcwd(),'/FinalProject/visual/visualize.jpg')
        plt.savefig(r'C:\Users\Tchouanga\OneDrive - aivancity\Documents\GitHub\Advanced_analysis\FinalProject\visual\visualize.jpg',bbox_inches="tight", dpi = 80)
        plt.close()
        return r'C:\Users\Tchouanga\OneDrive - aivancity\Documents\GitHub\Advanced_analysis\FinalProject\visual\visualize.jpg'

    def visualize_command(self,command):
        
        #data_leagues = self.collect_data(url_leagues)
        #data_season = collect_data(url_season)
        #data_players = collect_data(url_players)
        #data_teams = collect_data(url_teams)
        #data_upcoming_fixtures = collect_data(url_upcoming_fixtures)

        # %% [markdown]
        # ### LIST OF COMMANDS
        # ##### This represents the list of the different commands to be applied by the bot on discord
        # 
        # 
        # 1. Top 10 top scorers of Ligue 1 2021-2022
        # - Data used: URL Topscorers data
        # - Visualization: Horizontal Bar Chart
        # 
        # 2. % of wins, defeats and draws for Lille in Ligue 1 2021-2022
        # - Visualization: Pie Chart
        #       
        # 3. Total number of homewins versus awaywins in Ligue 1 2021-2022
        # - Visualization: Histogram
        # 
        # 4. Total number of wins per team in Ligue 1 2021-2022
        # 
        # 5. Performances of Lille at home and away in Ligue 1 2021-022
        # 
        # 6. Current ranking Ligue 1 2021-2022

        ### FIRST COMMAND
        if command == 1:
            data_topscorers = self.collect_data(self.url_topscorers)
            ## Get the top 10 topscorers in Ligue 1 season 2021 - 2022
            data_10_topscorers = data_topscorers.sort_values(by=['totalGoals'], ascending = False)[1:11]

            ## Visualize the top 10 topscorers in Ligue 1 season 2021 - 2022 in an horizontal bar charts
            players = data_10_topscorers['playerName']
            total_goals_without_penalties = data_10_topscorers['totalGoals'] - data_10_topscorers['penaltiesScored']
            penalties_scored = data_10_topscorers['penaltiesScored']
            # Figure Size
            fig, ax = plt.subplots(figsize =(16, 9))
            # Horizontal Bar Plot
            b1 = ax.barh(players, total_goals_without_penalties, color = 'cornflowerblue')
            b2 = ax.barh(players, penalties_scored, left = total_goals_without_penalties, color = 'lightsteelblue')
            # Remove axes splines
            for s in ['top', 'bottom', 'left', 'right']:
                ax.spines[s].set_visible(False)
            # Remove x, y Ticks
            ax.xaxis.set_ticks_position('none')
            ax.yaxis.set_ticks_position('none')
            # Add padding between axes and labels
            ax.xaxis.set_tick_params(pad = 5)
            ax.yaxis.set_tick_params(pad = 10)
            # Add x, y gridlines
            ax.grid(b = True, color ='grey', linestyle ='-.', linewidth = 0.5, alpha = 0.2)
            # Show top values
            ax.invert_yaxis()
            # Add annotation to bars
            for p in ax.patches:
                left, bottom, width, height = p.get_bbox().bounds
                ax.annotate(int(width), xy=(left+width/2, bottom+height/2), 
                            ha='center', va='center', color='white', fontweight ='bold')
            # Add Plot Title
            #ax.set_title('10 top scorers in Ligue 1 in the season 2021 - 2022', loc ='left', fontsize=20)
            plt.title("Percentage of wins, defeats, draws of Lille in Ligue 1 2021 - 2022", size = 20, color = 'black', weight = 'bold')

            blue_patch = mpatches.Patch(color='cornflowerblue', label='Total goals without penalties')
            orange_patch = mpatches.Patch(color='lightsteelblue', label='Penalties scored')
            ax.legend(handles=[blue_patch, orange_patch])

            return self.save()

        ### Prepare data for visualize
        if command in [2,3,4,5,6]:
            # Display all the fixtures (=games) in Ligue 1 season 2021 - 2022
            data_fixtures_season = self.collect_data(self.url_fixtures_season)

            # Add final score column in the dataframe representing the fixtures in the Ligue 1 2021-2022
            data_fixtures_season['finalScore'] = data_fixtures_season['team_home_90min_goals'].astype(str) + ['-'] + data_fixtures_season['team_away_90min_goals'].astype(str)

            # Add final result column in the dataframe (winning team, losing team, draw) 
            data_fixtures_season = data_fixtures_season.copy()

            data_fixtures_season['finalResult'] = np.where(data_fixtures_season['team_home_90min_goals']
            == data_fixtures_season['team_away_90min_goals'], 'Draw', np.where(data_fixtures_season['team_home_90min_goals'] > 
            data_fixtures_season['team_away_90min_goals'], data_fixtures_season['homeName'], data_fixtures_season['awayName']))

            # Add halftime_score column in the dataframe
            data_fixtures_season['halftimeScore'] = data_fixtures_season['team_home_1stHalf_goals'].astype(str) + ['-'] + data_fixtures_season['team_away_1stHalf_goals'].astype(str)

            # Add points earned by home team column

            data_fixtures_season['pts_earned_homeName'] = np.where(data_fixtures_season['homeName']
            == data_fixtures_season['finalResult'], 3 , np.where(data_fixtures_season['awayName'] ==
            data_fixtures_season['finalResult'], 0, 1))

            # Add points earned by away team column

            data_fixtures_season['pts_earned_awayName'] = np.where(data_fixtures_season['awayName']
            == data_fixtures_season['finalResult'], 3 , np.where(data_fixtures_season['homeName'] ==
            data_fixtures_season['finalResult'], 0, 1))

            data_fixtures_ligue1 = data_fixtures_season[['id', 'seasonName','idHome', 'homeName', 'idAway', 'awayName','halftimeScore', 
            'team_home_90min_goals', 'team_away_90min_goals', 'finalScore','finalResult', 'pts_earned_homeName', 'pts_earned_awayName', 'attendance', 'venueName', 'date', 'status']]
            data_finished_fixtures_ligue1 = data_fixtures_ligue1[data_fixtures_ligue1['status'] == 'finished']

            # Get the finished home fixtures of team Lille in Ligue 1 season 2021 - 2022
            data_finished_homefixtures_lille = data_finished_fixtures_ligue1[data_finished_fixtures_ligue1['homeName'] == 'Lille']
            # Add finalResultLille column in the dataframe presenting finished home fixtures of team Lille in Ligue 1 season 2021 - 2022
            data_finished_homefixtures_lille['homefinalResultLille'] = np.where(data_finished_homefixtures_lille['pts_earned_homeName']
            == 3, 'Win' , np.where(data_finished_homefixtures_lille['pts_earned_homeName'] == 0, 'Defeat', 'Draw'))

            data_finished_homefixtures_lille

            # Get the finished away fixtures of team Lille in Ligue 1 season 2021 - 2022
            data_finished_awayfixtures_lille = data_finished_fixtures_ligue1[data_finished_fixtures_ligue1['awayName'] == 'Lille']
            # Add finalResultLille column in the dataframe presenting finished away fixtures of team Lille in Ligue 1 season 2021 - 2022
            data_finished_awayfixtures_lille['awayfinalResultLille'] = np.where(data_finished_awayfixtures_lille['pts_earned_awayName']
            == 3, 'Win' , np.where(data_finished_awayfixtures_lille['pts_earned_awayName'] == 0, 'Defeat', 'Draw'))


            ## SECOND COMMAND
            if command == 2:
                            # Get all the finished fixtures of team Lille in season 2021 - 2022 by concatening 
                data_all_finished_fixtures_lille = pd.concat([data_finished_homefixtures_lille, data_finished_awayfixtures_lille], axis=0)
                #data_all_finished_fixtures_lille_by_date = data_all_finished_fixtures_lille.sort_values(by=['date'])

                number_wins_lille = data_all_finished_fixtures_lille.finalResult.value_counts().Lille
                number_draws_lille = data_all_finished_fixtures_lille.finalResult.value_counts().Draw
                number_defeats_lille = len(data_all_finished_fixtures_lille) - (number_wins_lille + number_draws_lille)

                labels = ("Wins", "Defeats", "Draws")
                data = [number_wins_lille, number_defeats_lille, number_draws_lille]
                #explode = (0.1, 0.1, 0.1)

                # Creating color parameters
                colors = ( "cornflowerblue", "lightcoral", "lightslategrey")
                
                # Wedge properties
                wp = { 'linewidth' : 1, 'edgecolor' : "black" }
                
                # Creating autocpt arguments
                def func(pct, allvalues):
                    absolute = int(pct / 100.*np.sum(allvalues))
                    return "{:.1f}%".format(pct, absolute)
                # Creating plot
                fig, ax = plt.subplots(figsize =(10, 7))
                wedges, texts, autotexts = ax.pie(data,
                                                autopct = lambda pct: func(pct, data),
                                                #explode = explode,
                                                labels = labels,
                                                shadow = True,
                                                colors = colors,
                                                startangle = 90,
                                                wedgeprops = wp,
                                                textprops = dict(color ="white"))
                
                # Adding legend
                ax.legend(wedges, labels,
                        title ="Team: Lille",
                        loc ="center left",
                        bbox_to_anchor =(1, 0, 0.5, 1))
                
                plt.setp(autotexts, size = 10, weight ="bold")
                plt.title("Percentage of wins, defeats, draws of Lille in Ligue 1 2021 - 2022", size = 20, color = 'black', weight = 'bold') 
                plt.close()
            
                return self.save()

            ## THIRD COMMAND 

            if command == 3:

                # number of home wins in Ligue 1 - 2021/2022
                number_homeWins = len(data_finished_fixtures_ligue1[data_finished_fixtures_ligue1['homeName'] == data_finished_fixtures_ligue1['finalResult']])

                # number of away wins in Ligue 1 - 2021/2022
                number_awayWins = len(data_finished_fixtures_ligue1[data_finished_fixtures_ligue1['awayName'] == data_finished_fixtures_ligue1['finalResult']])

                # number of draws in Ligue 1 - 2021/2022
                number_draws = len(data_finished_fixtures_ligue1[data_finished_fixtures_ligue1['finalResult'] == 'Draw'])

                # Plot total number of homewins vs awaywins 
                total_nb_homewins_and_awaywins = pd.DataFrame({'Type of wins':['homewins', 'awaywins'], 'val':[number_homeWins, number_awayWins]})
                total_nb_homewins_and_awaywins.plot.bar(x='Type of wins', y='val', rot=0, figsize=(8,4))
                plt.title('Total number of homewins vs awaywins in Ligue 1 2021 - 2022')
                plt.close()

                return self.save()

            ## FOURTH COMMAND

            if command == 4:
                    
                # Plot total number of wins per team in Ligue 1 2021 - 2022
                sns.countplot(y="finalResult", data=data_finished_fixtures_ligue1, order=data_finished_fixtures_ligue1.finalResult.value_counts().iloc[1:].index, palette='Set2')
                plt.title('Total number of wins per team')

                return self.save()
            ## FIFTH COMMAND

            if command == 5:
                # Analyze the performances of Lille at home and away
                fig, ax =plt.subplots(1,2)
                order = ['Win', 'Defeat', 'Draw']
                sns.countplot(data_finished_homefixtures_lille['homefinalResultLille'], ax=ax[0], order=order, palette='Set2').set(title='Performances of Lille - Home')
                sns.countplot(data_finished_awayfixtures_lille['awayfinalResultLille'], ax=ax[1], order=order, palette='Set2').set(title='Performances of Lille - Away')
                plt.close()
                
                return self.save()

            ## SIXTH COMMAND

            if command == 6:
                # Total number of points earned by each team at home in Ligue 1 2021-2022
                total_pts_earned_at_home_per_team = data_finished_fixtures_ligue1.groupby('homeName').sum()
                total_pts_earned_at_home_per_team['pts_earned_homeName']
                # Total number of points earned by each team away in Ligue 1 2021-2022
                total_pts_earned_away_per_team = data_finished_fixtures_ligue1.groupby('awayName').sum()
                total_pts_earned_away_per_team['pts_earned_awayName']
                # Current ranking Ligue 1 2021-2022
                total_pts_earned_each_team = total_pts_earned_at_home_per_team['pts_earned_homeName']+total_pts_earned_away_per_team['pts_earned_awayName']
                ranking_ligue1_current_season = total_pts_earned_each_team.sort_values(ascending=False)

                print(ranking_ligue1_current_season)

                # Plot current ranking Ligue 1 2021-2022
                ax = ranking_ligue1_current_season.plot.bar(x='Teams', 
                                                        rot=60, 
                                                        figsize=(20,8), 
                                                        title='Current ranking Ligue 1 2021 - 2022',
                                                        ylabel='Total number of points',
                                                        color='cornflowerblue',
                                                        fontsize='large')
                for p in ax.patches:
                    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.02))

                return self.save()
