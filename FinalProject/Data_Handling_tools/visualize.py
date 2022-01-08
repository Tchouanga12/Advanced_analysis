# %% [markdown]
# 
# FOOTBALL DATA MANAGEMENT
# 
# 
# In this file we basically create file which will manage all the api data importation into the discord 
# bot that will later on produce the result on discord.
# 
# 1. Create class
#         
# 2. Associate the commands function
#       
# 3. Connect class with robot file
# 
# 4. Test class and command function in robot.

# %%
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import io

# %%
###Different source references

class football:

    def __init__(self):
        """
        Intializing a football that object. This initialization will call the api used 
        to treat the data used in the treatment to produce the diverse commands.
        """
        self.url_topscorers = "https://elenasport-io1.p.rapidapi.com/v2/seasons/4242/topscorers"
        self.url_leagues = "https://elenasport-io1.p.rapidapi.com/v2/leagues"
        self.url_league_id = "https://elenasport-io1.p.rapidapi.com/v2/leagues/263"
        self.url_season = "https://elenasport-io1.p.rapidapi.com/v2/seasons"
        self.url_players = "https://elenasport-io1.p.rapidapi.com/v2/seasons/4242/players"
        self.url_teams = "https://elenasport-io1.p.rapidapi.com/v2/seasons/4242/teams"
        self.url_fixtures_season = "https://elenasport-io1.p.rapidapi.com/v2/seasons/4242/fixtures"
        self.url_upcoming_fixtures = "https://elenasport-io1.p.rapidapi.com/v2/seasons/4242/upcoming"
        self.url_fixtures_season = "https://elenasport-io1.p.rapidapi.com/v2/seasons/4242/fixtures"
        self.data_finished_fixtures_ligue1 = None
        self.data_finished_homefixtures_lille = None
        self.data_finished_awayfixtures_lille = None
    
    def collect_data(self,url):
        """
        function to collect all the produced from that API
        input: url (The reference to the desired data to be collected)
        output: data table of collected sets of data.
        """
        querystring = {"page":"1"}
        headers = {
        'x-rapidapi-host': "elenasport-io1.p.rapidapi.com",
        'x-rapidapi-key': "19459610edmshb2332b3c82bfe6fp14ff82jsnc9ac45d2c719"
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
        plt.savefig(r'C:\Users\Tchouanga\OneDrive - aivancity\Documents\GitHub\Advanced_analysis\FinalProject\visual\visualize.jpg',bbox_inches="tight", dpi = 80)
        plt.close()
        return r'C:\Users\Tchouanga\OneDrive - aivancity\Documents\GitHub\Advanced_analysis\FinalProject\visual\visualize.jpg'


    def visualize_command(self,command):
        """
        This function permits the visualization of the first command, which produces
        a chart of the 10 best.
        """
        if command == 1:
            data_stream = io.BytesIO()
            data_topscorers = self.collect_data(self.url_topscorers)
            data_10_topscorers = data_topscorers.sort_values(by=['totalGoals'], ascending = False)[1:11]
            data_10_topscorers
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
            ax.set_title('10 top scorers in Ligue 1 in the season 2021 - 2022', loc ='left', fontsize=20)

            blue_patch = mpatches.Patch(color='cornflowerblue', label='Total goals without penalties')
            orange_patch = mpatches.Patch(color='lightsteelblue', label='Penalties scored')
            ax.legend(handles=[blue_patch, orange_patch])

            return self.save()
    
        elif command == 2:
            """
            Do second command
            """
            data_fixtures_season = self.collect_data(self.url_fixtures_season)
            # Present all the finished fixtures with the final result column created above

            data_fixtures_ligue1 = data_fixtures_season[['id', 'seasonName','idHome', 'homeName', 'idAway', 'awayName','halftimeScore', 
            'team_home_90min_goals', 'team_away_90min_goals', 'finalScore','finalResult', 'pts_earned_homeName', 'pts_earned_awayName', 'attendance', 'venueName', 'date', 'status']]
            ### Prepare data for visualize
            data_finished_fixtures_ligue1 = data_fixtures_ligue1[data_fixtures_ligue1['status'] == 'finished']
            # Get the finished home fixtures of team Lille in Ligue 1 season 2021 - 2022
            data_finished_homefixtures_lille = data_finished_fixtures_ligue1[data_finished_fixtures_ligue1['homeName'] == 'Lille']
            # Add finalResultLille column in the dataframe presenting finished home fixtures of team Lille in Ligue 1 season 2021 - 2022
            data_finished_homefixtures_lille['homefinalResultLille'] = np.where(data_finished_homefixtures_lille['pts_earned_homeName']
            == 3, 'Win' , np.where(data_finished_homefixtures_lille['pts_earned_homeName'] == 0, 'Defeat', 'Draw'))

            # Get the finished away fixtures of team Lille in Ligue 1 season 2021 - 2022
            data_finished_awayfixtures_lille = data_finished_fixtures_ligue1[data_finished_fixtures_ligue1['awayName'] == 'Lille']
            # Add finalResultLille column in the dataframe presenting finished away fixtures of team Lille in Ligue 1 season 2021 - 2022
            data_finished_awayfixtures_lille['awayfinalResultLille'] = np.where(data_finished_awayfixtures_lille['pts_earned_awayName']
            == 3, 'Win' , np.where(data_finished_awayfixtures_lille['pts_earned_awayName'] == 0, 'Defeat', 'Draw'))

            # Analyze the performances of Lille at home and away
            fig, ax =plt.subplots(1,2)
            order = ['Win', 'Defeat', 'Draw']
            sns.countplot(data_finished_homefixtures_lille['homefinalResultLille'], ax=ax[0], order=order, palette='Set2').set(title='Performances of Lille - Home')
            sns.countplot(data_finished_awayfixtures_lille['awayfinalResultLille'], ax=ax[1], order=order, palette='Set2').set(title='Performances of Lille - Away')
           
            return  self.save()
        
        elif command == 3:
            """
            Do third command
            """
            # Plot total number of wins per team in Ligue 1 2021 - 2022
            sns.countplot(y="finalResult", data=self.data_finished_fixtures_ligue1, order=self.data_finished_fixtures_ligue1.finalResult.value_counts().iloc[1:].index, palette='Set2')
            plt.title('Total number of wins per team')

            return self.save()

        elif command == 4:

                        # Get all the finished fixtures of team Lille in season 2021 - 2022 by concatening 
            data_all_finished_fixtures_lille = pd.concat([self.data_finished_homefixtures_lille, self.data_finished_awayfixtures_lille], axis=0)
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
            plt.title("Percentage of wins, defeats, draws of Lille in Ligue 1 2021 - 2022", size = 20, color = 'white', weight = 'bold')
           
            return self.save()