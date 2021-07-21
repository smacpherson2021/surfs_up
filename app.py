# Import general dependancies
import datetime as dt
import numpy as np
import pandas as pd

# Import SQLAlchemy dependancies
import sqlalchemy
from sqlalchemy.ext import automap
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask dependancies
from flask import Flask, jsonify

# Set Up the Database
# Access the SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")
# Allow query to the database file
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create a session link from Python to the database
session = Session(engine)

# Define the Flask app
app = Flask(__name__)

# Define the welcome route
@app.route("/")

# Create to reference all other routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end<br/>
    ''')

# Define the precipitation route
@app.route("/api/v1.0/precipitation")

def precipitation():
    # calculates the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    # create a dictionary with the date as the key and the precipitation as the value
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Define the stations route
@app.route("/api/v1.0/stations")

def stations():
    # get all of the stations in our database
    results = session.query(Station.station).all()
    # unravel the results into a one-dimensional array and convert that array into a list. 
    stations = list(np.ravel(results))
    # Then jsonify the list and return
    return jsonify(stations=stations)

# Define the temperature route
@app.route("/api/v1.0/tobs")

def temp_monthly():
    # calculate the date one year ago from the last date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # query the primary station for all the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    # unravel the results into a one-dimensional array and convert that array into a list. 
    temps = list(np.ravel(results))
    # Then jsonify the list and return
    return jsonify(temps)

# Define the stats route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    # create a query to select the minimum, average, and maximum temperatures from our SQLite database
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

