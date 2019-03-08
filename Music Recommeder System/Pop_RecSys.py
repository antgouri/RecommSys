#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 08:54:11 2019

@author: ananth
"""

import turicreate as tc
import sqlite3  

# Load dataset
conn = sqlite3.connect("msd.sqlite3")
listens = tc.SFrame.from_sql(conn, "SELECT * FROM train")
songs_df = tc.SFrame.from_sql(conn, "SELECT * FROM song")

train_data, test_data = tc.recommender.util.random_split_by_user(listens, "userID", "songID")

model2 = tc.recommender.popularity_recommender.create(train_data, "userID", "songID", target='plays')

#mod2 = tc.popularity_recommender.create(test_data,"userID", "songID", target='plays')

pop = model2.recommend()

song_recommendations = pop.join(songs_df, on="songID", how="inner").sort("score")

#cannot use sort method based on rank / score - looks like redudant data

print(song_recommendations.unique())

rmse_m2 = model2.evaluate_rmse(test_data, target="plays")

print(rmse_m2)

pr_m2 = model2.evaluate_precision_recall(test_data)

print(pr_m2)
