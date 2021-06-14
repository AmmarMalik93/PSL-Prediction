import pandas as pd
import numpy as np

def extract_match_data(filenames):
    x = 0
    team1_data = list()
    team2_data = list()
    for i in filenames:    

        if (i == '1075986.csv')|(i == '1075994.csv')|(i == '1075995.csv')|(i == '1211660.csv')|(i == '1211661.csv'):
            continue

        with open(i) as f:
            lines = f.readlines()

        for j in range(len(lines)):
            if lines[j].startswith('ball'):
                temp = j
                break

        #print('Processing Match #',x+1, 'filename',i) 

        match = pd.read_table(i, sep=',',skiprows=temp, header=None)

        match.columns = ['temp','InningsNum','BallNum','Team','Striker','NonStriker','Bowler','Runsoffbat','Extras','Wides','Noballs',
                    'Byes','LegByes','Penalty','KindWicket','DismissedPlayer']

        match = match.loc[:,['InningsNum','BallNum','Team','Runsoffbat','Extras','KindWicket']]

        Innings1 = match[match.InningsNum==1]
        Innings2 = match[match.InningsNum==2]

        team1_runs = Innings1.Runsoffbat.sum()+Innings1.Extras.sum()
        team1_wickets = Innings1[~Innings1.KindWicket.isnull()].shape[0]

        if team1_wickets == 10:
            team1_overs = 20
        else:
            team1_overs = np.floor(Innings1.BallNum.iloc[-1])+(int(Innings1.BallNum.iloc[-1]*10)%10)/6

        team1_rr = team1_runs/team1_overs

        team1_pp = Innings1[Innings1.BallNum<6.1]
        team1_pp_rr = (team1_pp.Runsoffbat.sum()+team1_pp.Extras.sum())/6
        team1_pp_wkt = 10 - team1_pp[~team1_pp.KindWicket.isnull()].shape[0]

        team1_mid = Innings1[(Innings1.BallNum<15.1)]
        team1_mid_rr = (team1_mid.Runsoffbat.sum()+team1_mid.Extras.sum())/15
        team1_mid_wkt = 10 - team1_mid[~team1_mid.KindWicket.isnull()].shape[0]


        team2_sit = list()
        a = 1.1
        b = 19.0
        for k in range(20):
            team2_over_num = Innings2[Innings2.BallNum<a]
            team2_runs = team2_over_num.Runsoffbat.sum()+team2_over_num.Extras.sum()

            if team2_runs < team1_runs:
                team2_rrr = (team1_runs + 1 - team2_runs)/b
            else:
                team2_rrr = 0.0

            team2_wkt_rem = 10 - team2_over_num[~team2_over_num.KindWicket.isnull()].shape[0]

            team2_sit.append([team2_rrr, team2_wkt_rem])
            a += 1.0
            b -= 1.0
        team2_data.append(np.asarray(team2_sit).flatten())

        if team1_runs>=team2_runs:
            team1_win = 1
            team2_win = 0
        else:
            team1_win = 0
            team2_win = 1

        team1_data.append(np.asarray([team1_pp_rr, team1_pp_wkt, team1_mid_rr, team1_mid_wkt, team1_rr,team1_win]))



        x += 1

    team1_data = np.asarray(team1_data)
    team2_data = np.asarray(team2_data)
    
    return(team1_data, team2_data)