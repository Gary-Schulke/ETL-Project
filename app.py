import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from password import pw

#################################################
# Database Setup
#################################################
engine = create_engine(f'postgresql://postgres:{pw}@localhost:5432/city_transit_db')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Cities = Base.classes.cities
Tracks = Base.classes.tracks

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def transit_systems():
    """Return a list of transit system data including the city name, country, and track length"""
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query the joined tables
    sel = [Cities.city_id, Cities.city_name, Cities.country, Tracks.length]
    results = session.query(*sel).join(Tracks, Cities.city_id == Tracks.city_id).order_by(Tracks.length.desc()).all()

    session.close()

    # Create a dictionary from the row data and append to a list of city_tracks
    city_tracks = []

    for city_id, city_name, country, length in results:
        tracks_dict = {}
        tracks_dict["city_id"] = city_id
        tracks_dict["city_name"] = city_name
        tracks_dict["country"] = country
        tracks_dict["track_length"] = length
        city_tracks.append(tracks_dict)

    return jsonify(city_tracks)


if __name__ == '__main__':
    app.run(debug=True)
