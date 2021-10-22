"""This will bring the app together"""

from flask import Flask, render_template, request
from os import getenv
from .Spotify import find_song



def create_app():
    app = Flask(__name__)
    
    """Creating and configuring an instance of Flask App"""
    @app.route('/', methods = ['GET', 'POST'])
    
    def root():
        song_list = []
        name = request.form.get('name')
        artist = request.form.get('artist')
        if name and artist:
            song_list = find_song(name, artist)
        return render_template('base.html', title="home", song_list = song_list)
    return app

    