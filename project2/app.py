import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
rds_connection_string = "postgres:postgres@localhost:5432/Project2"
engine = create_engine(f'postgresql://{rds_connection_string}')
# engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
estados = Base.classes.estados
worldwide = Base.classes.worldwide
#Measurement = Base.classes.measurement
#Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
	return (
		f"Welcome to Coronavirus stats<br/>"
	
	)


@app.route("/estados")
def estados():
	"""Call all estados table and jsonify it"""
	# Query for all estados table or for estados table separated by status
	estados = session.query().filter().all()
	return jsonify(estados)
	


@app.route("/worldwide")
def worldwide():
	"""Call all worldwide table and jsonify it"""
	worldwide = session.query().all()
	return jsonify(worldwide)
	



@app.route("/api/v1.0/temp/<start>")

@app.route("/api/v1.0/temp/<start>/<end>")

if __name__ == '__main__':
	app.run()
