#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 08:56:15 2019

@author: ananth
"""

import turicreate as tc
import sqlite3  

# Load dataset
conn = sqlite3.connect("msd.sqlite3")
listens = tc.SFrame.from_sql(conn, "SELECT * FROM train")
songs_df = tc.SFrame.from_sql(conn, "SELECT * FROM song")

# Create Training set and test set
train_data, test_data = tc.recommender.util.random_split_by_user(listens, "userID", "songID")

model3 = tc.recommender.factorization_recommender.create(train_data, user_id="userID", item_id="songID", target="plays")

recc = model3.recommend()

song_recommendations = recc.join(songs_df, on="songID", how="inner").sort('rank')

print(song_recommendations)

# Evaluate the model
rmse_m3 = model3.evaluate_rmse(test_data, target="plays")

# Print the results
print(rmse_m3)