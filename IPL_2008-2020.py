
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import streamlit as st





IPL_byball = pd.read_csv('C:/Users/admin/Downloads/IPL/IPL Ball-by-Ball 2008-2020.csv')
IPL_match= pd.read_csv('C:/Users/admin/Downloads/IPL/IPL Matches 2008-2020.csv')


IPL_match['year'] = pd. DatetimeIndex(IPL_match['date']). year

st.title('IPL Matches 2008-2020 :cricket_bat_and_ball:')

    
col1, col2 , col3 = st.beta_columns(3)

with col1:
   
    team1 = st.selectbox('Enter your first team', IPL_match.team1.unique(),)

with col2:
    
    team2 = st.selectbox('Enter your second team', IPL_match.team2.unique())

with col3:
    
    year = st.selectbox('Enter IPL Season', IPL_match.year.unique())
    
    
if team1 == team2:
    st.write("**Please select two different teams")

matchid1 = IPL_match[(IPL_match.team1== team1) & (IPL_match.team2== team2 ) & (IPL_match.year == year)].id.values
matchid2 = IPL_match[(IPL_match.team1== team2) & (IPL_match.team2== team1 ) & (IPL_match.year == year)].id.values

matchid  = np.hstack((matchid1,matchid2))
matchid = sorted(matchid)

i = 1
for match in matchid:
    
   
    st.write("**Match :**" , i )
    
    col1, col2 , col3 = st.beta_columns(3)
    
    with col1:
        team1 = st.write('**Toss Won : **', IPL_match[IPL_match.id == match].toss_winner.values[0])

    with col2:
        team2 = st.write('**Match Winner :**',IPL_match[IPL_match.id == match].winner.values[0])

    with col3:
        year = st.write('**Man of the Match :**', IPL_match[IPL_match.id == match].player_of_match.values[0])
    
    df_innings1 = IPL_byball[(IPL_byball.id == int(match))& (IPL_byball['inning'] == 1)]
    df_innings1['delivery_number'] = (df_innings1.over) * 6 + df_innings1.ball 
    df_innings1.sort_values(by =['delivery_number'],inplace= True)
    df_innings1['runs_cumulative'] = df_innings1.total_runs.cumsum()
    df_innings1['total_wickets'] = df_innings1.is_wicket.cumsum()
    
    df_innings2 = IPL_byball[(IPL_byball.id == int(match))& (IPL_byball['inning'] == 2)]
    df_innings2['delivery_number'] = (df_innings2.over) * 6 + df_innings2.ball 
    df_innings2.sort_values(by =['delivery_number'],inplace= True)
    df_innings2['runs_cumulative'] = df_innings2.total_runs.cumsum()
    df_innings2['total_wickets'] = df_innings2.is_wicket.cumsum()
    
    innings1_wicket = df_innings1[df_innings1['is_wicket']>0]
    innings2_wicket = df_innings2[df_innings2['is_wicket']>0]
    
   
  
    fig, ax = plt.subplots()
    plt.plot(df_innings2['delivery_number'],df_innings2['runs_cumulative'],color= 'Orange')
    plt.scatter(innings2_wicket['delivery_number'],innings2_wicket['runs_cumulative'],c = 'Red')
    plt.plot(df_innings1['delivery_number'],df_innings1['runs_cumulative'],color= 'Blue')
    plt.scatter(innings1_wicket['delivery_number'],innings1_wicket['runs_cumulative'],c = 'Black')
    plt.xlabel('Deliveries Bowled')
    plt.ylabel('Runs Scored')
    plt.title('Runs and Fall of Wickets')
    plt.legend(labels = [df_innings2.batting_team.values[0],df_innings1.batting_team.values[0]])
    st.pyplot(fig)
    
    
    i += 1
