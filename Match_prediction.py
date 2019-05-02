# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:48:48 2019

@author: HP
"""
import pandas as pd

df=pd.read_csv('C:/Users/HP/Desktop/train.csv')
#print(df.head(3))
df['team1 4\'s']=df['Inn 1 Team 1 Total 4s']
df['team1 6\'s']=df['Inn 1 Team 1 Total 6s']
df['team2 4\'s']=df['Inn 2 Team 2 Total 4s']
df['team2 6\'s']=df['Inn 2 Team 2 Total 6s']
df['Avg-boundary']=(df['team1 4\'s']+df['team1 6\'s'])-(df['team2 4\'s']-df['team2 6\'s'])
df['total_run_team1']=(df['team1 4\'s']*4)+(df['team1 6\'s']*6)+df['Inn 1 Team 2 Extras conceded in_wides_No Balls']-(df['team2 4\'s']*4)+(df['team2 6\'s']*6)+df['Inn 2 Team 1 Extras conceded in_wides_No Balls']
df['wicket taken by team2']=(df['Inn 1 Team 2 wickets taken_catches_runout']+df['Inn1 Team 2 wickets taken_ bowled _lbw_caught by keeper_stumping'])
df['wicket taken by team1']=(df['Inn 2 Team 1 wickets taken_catches_runout']+df['Inn2 Team 1 wickets taken_ bowled _lbw_caught by keeper_stumping'])
df['faster2']=df['Inn 1 Team 2 NoP fast bowlers']
df['faster1']=df['Inn 2 Team 1 NoP fast bowlers']
X_train=df.iloc[:,30:]
Y_train=df['Winner (team 1=1, team 2=0)']
df1=pd.read_csv('C:/Users/HP/Desktop/test.csv')
df1['team1 4\'s']=df1['Inn 1 Team 1 Total 4s']
df1['team1 6\'s']=df1['Inn 1 Team 1 Total 6s']
df1['team2 4\'s']=df1['Inn 2 Team 2 Total 4s']
df1['team2 6\'s']=df1['Inn 2 Team 2 Total 6s']
df1['Avg-boundary']=(df1['team1 4\'s']+df1['team1 6\'s'])-(df1['team2 4\'s']-df1['team2 6\'s'])
df1['total_run_team1']=(df1['team1 4\'s']*4)+(df1['team1 6\'s']*6)+df1['Inn 1 Team 2 Extras conceded in_wides_No Balls']-(df1['team2 4\'s']*4)+(df1['team2 6\'s']*6)+df1['Inn 2 Team 1 Extras conceded in_wides_No Balls']
df1['wicket taken by team2']=(df1['Inn 1 Team 2 wickets taken_catches_runout']+df1['Inn1 Team 2 wickets taken_ bowled _lbw_caught by keeper_stumping'])
df1['wicket taken by team1']=(df1['Inn 2 Team 1 wickets taken_catches_runout']+df1['Inn2 Team 1 wickets taken_ bowled _lbw_caught by keeper_stumping'])
df1['faster2']=df1['Inn 1 Team 2 NoP fast bowlers']
df1['faster1']=df1['Inn 2 Team 1 NoP fast bowlers']
X_test=df1.iloc[:,30:]
Y_test=df1['Winner (team 1=1, team 2=0)']
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(penalty='l2',C=10,max_iter=7)
clf.fit(X_train,Y_train)
accuracy=clf.score(X_test,Y_test)
print((accuracy*100))