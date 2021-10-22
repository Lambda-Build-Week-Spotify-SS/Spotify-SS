"""Connector for spotipy, getting songs and such from the Spotify DB"""
import pandas as pd
import numpy as np
from scipy.spatial import distance

# preparing dataframe to process function
# df = pd.read_csv('data.csv')
# df['artists'] = df['artists'].str.lstrip('[').str.rstrip(']')
# df['artists'] = df['artists'].str.replace('\'','')

# # create vectorized column with which to compare to other songs
# vector = []
# for i in range(len(df)):
#   vector.append(np.array([df['valence'][i],df['acousticness'][i],df['danceability'][i],
#                 df['energy'][i],df['instrumentalness'][i],df['key'][i],
#                 df['liveness'][i],df['speechiness'][i],df['tempo'][i]]
#                 ))
# df['vector'] = vector
#song_list = np.array([x for x in df['vector']])
#len(song_list)


# function to find and return 5 most similar songs
def find_song(name, artist):
  df = pd.read_csv("data.csv")
  df['artists'] = df['artists'].str.lstrip('[').str.rstrip(']')
  df['artists'] = df['artists'].str.replace('\'','')
  vector = []
  for i in range(len(df)):
    vector.append(np.array([df['valence'][i],df['acousticness'][i],df['danceability'][i],
                df['energy'][i],df['instrumentalness'][i],df['key'][i],
                df['liveness'][i],df['speechiness'][i],df['tempo'][i]]
                ))
  df['vector'] = vector
  search_song = df['vector'].loc[(df['name']== name) & (df['artists'] == artist)]
  search_song = np.array(search_song.explode()).reshape(1,-1)
  song_list = np.array([x for x in df['vector']])
  closest_index = distance.cdist(search_song,song_list,'cosine')
  closest_index = np.argsort(closest_index)
  
  songs = []

  songs.append(df['name'].loc[closest_index[0][1]])
  songs.append(df['name'].loc[closest_index[0][2]])
  songs.append(df['name'].loc[closest_index[0][3]])
  songs.append(df['name'].loc[closest_index[0][4]])
  songs.append(df['name'].loc[closest_index[0][5]])

  return songs

  


