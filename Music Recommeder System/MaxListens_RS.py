#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 18:14:56 2019

@author: ananth
"""

import turicreate as gl
import turicreate.aggregate as agg
import sqlite3

# Loading the DB
conn = sqlite3.connect("msd.sqlite3")

plays_df = gl.SFrame.from_sql(conn, "SELECT * FROM train")
songs_df = gl.SFrame.from_sql(conn, "SELECT * FROM song")

# Get the most listened songs
songs_total_listens = plays_df.groupby('songID', operations={"plays": agg.SUM("plays")})

# Join songs with data
songs_total_listens = songs_total_listens.join(songs_df, on="songID", how="inner").sort("plays", ascending=False)
print("# Top Songs with most total lisens:")
print(songs_total_listens.print_rows())

