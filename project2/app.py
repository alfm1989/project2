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
all_countries_t = Base.classes.all_countries
confirmados_t = Base.classes.confirmados
confirmed_t = Base.classes.confirmed
death_t = Base.classes.death
defunciones_t = Base.classes.defunciones
estados_t = Base.classes.estados
nacional_t = Base.classes.nacional
negativos_t = Base.classes.negativos
recovered_t = Base.classes.recovered


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
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/project2/data/all_countries<br/>"
        f"/project2/data/confirmed<br/>"
        f"/project2/data/death<br/>"
        f"/project2/data/recovered<br/>"
        f"/project2/data/negativos<br/>"
        f"/project2/data/confirmados<br/>"
        f"/project2/data/defunciones<br/>"
        f"/project2/data/estados<br/>"
        f"/project2/data/nacional<br/>"        
    )


@app.route("/project2/data/recovered")
def recovered_data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all recovered data"""
    # Query all table
    recovered_final= session.query(recovered_t.row_number,recovered_t.fips,recovered_t.estado, recovered_t.pais, recovered_t.status, recovered_t.Lat, recovered_t.Long, recovered_t.January_22, recovered_t.January_23, recovered_t.January_24, recovered_t.January_25, recovered_t.January_26, recovered_t.January_27, recovered_t.January_28, recovered_t.January_29, recovered_t.January_30, recovered_t.January_31, recovered_t.Feburary_1, recovered_t.Feburary_2, recovered_t.Feburary_3, recovered_t.Feburary_4, recovered_t.Feburary_5, recovered_t.Feburary_6, recovered_t.Feburary_7, recovered_t.Feburary_8, recovered_t.Feburary_9, recovered_t.Feburary_10, recovered_t.Feburary_11, recovered_t.Feburary_12, recovered_t.Feburary_13, recovered_t.Feburary_14, recovered_t.Feburary_15, recovered_t.Feburary_16, recovered_t.Feburary_17, recovered_t.Feburary_18, recovered_t.Feburary_19, recovered_t.Feburary_20, recovered_t.Feburary_21, recovered_t.Feburary_22, recovered_t.Feburary_23, recovered_t.Feburary_24, recovered_t.Feburary_25, recovered_t.Feburary_26, recovered_t.Feburary_27, recovered_t.Feburary_28, recovered_t.Feburary_29, recovered_t.March_1, recovered_t.March_2, recovered_t.March_3,recovered_t.March_4, recovered_t.March_5, recovered_t.March_6, recovered_t.March_7, recovered_t.March_8, recovered_t.March_9, recovered_t.March_10, recovered_t.March_11, recovered_t.March_12, recovered_t.March_13, recovered_t.March_14, recovered_t.March_15, recovered_t.March_16, recovered_t.March_17, recovered_t.March_18, recovered_t.March_19, recovered_t.March_20, recovered_t.March_21, recovered_t.March_22, recovered_t.March_23, recovered_t.March_24, recovered_t.March_25, recovered_t.March_26, recovered_t.March_27, recovered_t.March_28, recovered_t.March_29, recovered_t.March_30, recovered_t.March_31, recovered_t.April_1, recovered_t.April_2, recovered_t.April_3, recovered_t.April_4, recovered_t.April_5, recovered_t.April_6, recovered_t.April_7, recovered_t.April_8, recovered_t.April_9, recovered_t.April_10, recovered_t.April_11, recovered_t.April_12, recovered_t.April_13, recovered_t.April_14, recovered_t.April_15, recovered_t.April_16, recovered_t.April_17, recovered_t.April_18, recovered_t.April_19, recovered_t.April_20, recovered_t.April_21, recovered_t.April_22).all()
 
    session.close()
    
    # Create a dictionary
    
    recovered_all = []
    for row_number, fips, estado, pais, status, Lat, Long, January_22, January_23, January_24, January_25, January_26, January_27, January_28, January_29, January_30, January_31, Feburary_1, Feburary_2, Feburary_3, Feburary_4, Feburary_5, Feburary_6, Feburary_7, Feburary_8, Feburary_9, Feburary_10, Feburary_11, Feburary_12, Feburary_13, Feburary_14, Feburary_15, Feburary_16, Feburary_17, Feburary_18, Feburary_19, Feburary_20, Feburary_21, Feburary_22, Feburary_23, Feburary_24, Feburary_25, Feburary_26, Feburary_27, Feburary_28, Feburary_29, March_1, March_2, March_3, March_4, March_5, March_6, March_7, March_8, March_9, March_10, March_11, March_12, March_13, March_14, March_15, March_16, March_17, March_18, March_19, March_20, March_21, March_22, March_23, March_24, March_25, March_26, March_27, March_28, March_29, March_30, March_31, April_1, April_2, April_3, April_4, April_5, April_6, April_7, April_8, April_9, April_10, April_11, April_12, April_13, April_14, April_15, April_16, April_17, April_18, April_19, April_20, April_21, April_22, in recovered_final:
        recovered_d = {}
        recovered_d["row_number"] = row_number
        recovered_d["fips"] = fips
        recovered_d["estado"] = estado
        recovered_d["pais"] = pais
        recovered_d["status"] = status
        recovered_d["Lat"] = Lat
        recovered_d["Long"] = Long
        recovered_d['January_22']=January_22
        recovered_d['January_23']=January_23
        recovered_d['January_24']=January_24
        recovered_d['January_25']=January_25
        recovered_d['January_26']=January_26
        recovered_d['January_27']=January_27
        recovered_d['January_28']=January_28
        recovered_d['January_29']=January_29
        recovered_d['January_30']=January_30
        recovered_d['January_31']=January_31
        recovered_d['Feburary_1']=Feburary_1
        recovered_d['Feburary_2']=Feburary_2
        recovered_d['Feburary_3']=Feburary_3
        recovered_d['Feburary_4']=Feburary_4
        recovered_d['Feburary_5']=Feburary_5
        recovered_d['Feburary_6']=Feburary_6
        recovered_d['Feburary_7']=Feburary_7
        recovered_d['Feburary_8']=Feburary_8
        recovered_d['Feburary_9']=Feburary_9
        recovered_d['Feburary_10']=Feburary_10
        recovered_d['Feburary_11']=Feburary_11
        recovered_d['Feburary_12']=Feburary_12
        recovered_d['Feburary_13']=Feburary_13
        recovered_d['Feburary_14']=Feburary_14
        recovered_d['Feburary_15']=Feburary_15
        recovered_d['Feburary_16']=Feburary_16
        recovered_d['Feburary_17']=Feburary_17
        recovered_d['Feburary_18']=Feburary_18
        recovered_d['Feburary_19']=Feburary_19
        recovered_d['Feburary_20']=Feburary_20
        recovered_d['Feburary_21']=Feburary_21
        recovered_d['Feburary_22']=Feburary_22
        recovered_d['Feburary_23']=Feburary_23
        recovered_d['Feburary_24']=Feburary_24
        recovered_d['Feburary_25']=Feburary_25
        recovered_d['Feburary_26']=Feburary_26
        recovered_d['Feburary_27']=Feburary_27
        recovered_d['Feburary_28']=Feburary_28
        recovered_d['Feburary_29']=Feburary_29
        recovered_d['March_1']=March_1
        recovered_d['March_2']=March_2
        recovered_d['March_3']=March_3
        recovered_d['March_4']=March_4
        recovered_d['March_5']=March_5
        recovered_d['March_6']=March_6
        recovered_d['March_7']=March_7
        recovered_d['March_8']=March_8
        recovered_d['March_9']=March_9
        recovered_d['March_10']=March_10
        recovered_d['March_11']=March_11
        recovered_d['March_12']=March_12
        recovered_d['March_13']=March_13
        recovered_d['March_14']=March_14
        recovered_d['March_15']=March_15
        recovered_d['March_16']=March_16
        recovered_d['March_17']=March_17
        recovered_d['March_18']=March_18
        recovered_d['March_19']=March_19
        recovered_d['March_20']=March_20
        recovered_d['March_21']=March_21
        recovered_d['March_22']=March_22
        recovered_d['March_23']=March_23
        recovered_d['March_24']=March_24
        recovered_d['March_25']=March_25
        recovered_d['March_26']=March_26
        recovered_d['March_27']=March_27
        recovered_d['March_28']=March_28
        recovered_d['March_29']=March_29
        recovered_d['March_30']=March_30
        recovered_d['March_31']=March_31
        recovered_d['April_1']=April_1
        recovered_d['April_2']=April_2
        recovered_d['April_3']=April_3
        recovered_d['April_4']=April_4
        recovered_d['April_5']=April_5
        recovered_d['April_6']=April_6
        recovered_d['April_7']=April_7
        recovered_d['April_8']=April_8
        recovered_d['April_9']=April_9
        recovered_d['April_10']=April_10
        recovered_d['April_11']=April_11
        recovered_d['April_12']=April_12
        recovered_d['April_13']=April_13
        recovered_d['April_14']=April_14
        recovered_d['April_15']=April_15
        recovered_d['April_16']=April_16
        recovered_d['April_17']=April_17
        recovered_d['April_18']=April_18
        recovered_d['April_19']=April_19
        recovered_d['April_20']=April_20
        recovered_d['April_21']=April_21
        recovered_d['April_22']=April_22

        recovered_all.append(recovered_d)

    return jsonify(recovered_all)

@app.route("/project2/data/all_countries")
def all_countries_data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    all_countries_final= session.query(all_countries_t.row_number,all_countries_t.fips,all_countries_t.estado, all_countries_t.pais, all_countries_t.status, all_countries_t.Lat, all_countries_t.Long, all_countries_t.January_22, all_countries_t.January_23, all_countries_t.January_24, all_countries_t.January_25, all_countries_t.January_26, all_countries_t.January_27, all_countries_t.January_28, all_countries_t.January_29, all_countries_t.January_30, all_countries_t.January_31, all_countries_t.Feburary_1, all_countries_t.Feburary_2, all_countries_t.Feburary_3, all_countries_t.Feburary_4, all_countries_t.Feburary_5, all_countries_t.Feburary_6, all_countries_t.Feburary_7, all_countries_t.Feburary_8, all_countries_t.Feburary_9, all_countries_t.Feburary_10, all_countries_t.Feburary_11, all_countries_t.Feburary_12, all_countries_t.Feburary_13, all_countries_t.Feburary_14, all_countries_t.Feburary_15, all_countries_t.Feburary_16, all_countries_t.Feburary_17, all_countries_t.Feburary_18, all_countries_t.Feburary_19, all_countries_t.Feburary_20, all_countries_t.Feburary_21, all_countries_t.Feburary_22, all_countries_t.Feburary_23, all_countries_t.Feburary_24, all_countries_t.Feburary_25, all_countries_t.Feburary_26, all_countries_t.Feburary_27, all_countries_t.Feburary_28, all_countries_t.Feburary_29, all_countries_t.March_1, all_countries_t.March_2, all_countries_t.March_3,all_countries_t.March_4, all_countries_t.March_5, all_countries_t.March_6, all_countries_t.March_7, all_countries_t.March_8, all_countries_t.March_9, all_countries_t.March_10, all_countries_t.March_11, all_countries_t.March_12, all_countries_t.March_13, all_countries_t.March_14, all_countries_t.March_15, all_countries_t.March_16, all_countries_t.March_17, all_countries_t.March_18, all_countries_t.March_19, all_countries_t.March_20, all_countries_t.March_21, all_countries_t.March_22, all_countries_t.March_23, all_countries_t.March_24, all_countries_t.March_25, all_countries_t.March_26, all_countries_t.March_27, all_countries_t.March_28, all_countries_t.March_29, all_countries_t.March_30, all_countries_t.March_31, all_countries_t.April_1, all_countries_t.April_2, all_countries_t.April_3, all_countries_t.April_4, all_countries_t.April_5, all_countries_t.April_6, all_countries_t.April_7, all_countries_t.April_8, all_countries_t.April_9, all_countries_t.April_10, all_countries_t.April_11, all_countries_t.April_12, all_countries_t.April_13, all_countries_t.April_14, all_countries_t.April_15, all_countries_t.April_16, all_countries_t.April_17, all_countries_t.April_18, all_countries_t.April_19, all_countries_t.April_20, all_countries_t.April_21, all_countries_t.April_22).all()
        
    session.close()
            
    # Create a dictionary
            
    all_countries_all = []
    for row_number, fips, estado, pais, status, Lat, Long, January_22, January_23, January_24, January_25, January_26, January_27, January_28, January_29, January_30, January_31, Feburary_1, Feburary_2, Feburary_3, Feburary_4, Feburary_5, Feburary_6, Feburary_7, Feburary_8, Feburary_9, Feburary_10, Feburary_11, Feburary_12, Feburary_13, Feburary_14, Feburary_15, Feburary_16, Feburary_17, Feburary_18, Feburary_19, Feburary_20, Feburary_21, Feburary_22, Feburary_23, Feburary_24, Feburary_25, Feburary_26, Feburary_27, Feburary_28, Feburary_29, March_1, March_2, March_3, March_4, March_5, March_6, March_7, March_8, March_9, March_10, March_11, March_12, March_13, March_14, March_15, March_16, March_17, March_18, March_19, March_20, March_21, March_22, March_23, March_24, March_25, March_26, March_27, March_28, March_29, March_30, March_31, April_1, April_2, April_3, April_4, April_5, April_6, April_7, April_8, April_9, April_10, April_11, April_12, April_13, April_14, April_15, April_16, April_17, April_18, April_19, April_20, April_21, April_22, in all_countries_final:
        all_countries_d = {}
        all_countries_d["row_number"] = row_number
        all_countries_d["fips"] = fips
        all_countries_d["estado"] = estado
        all_countries_d["pais"] = pais
        all_countries_d["status"] = status
        all_countries_d["Lat"] = Lat
        all_countries_d["Long"] = Long
        all_countries_d['January_22']=January_22
        all_countries_d['January_23']=January_23
        all_countries_d['January_24']=January_24
        all_countries_d['January_25']=January_25
        all_countries_d['January_26']=January_26
        all_countries_d['January_27']=January_27
        all_countries_d['January_28']=January_28
        all_countries_d['January_29']=January_29
        all_countries_d['January_30']=January_30
        all_countries_d['January_31']=January_31
        all_countries_d['Feburary_1']=Feburary_1
        all_countries_d['Feburary_2']=Feburary_2
        all_countries_d['Feburary_3']=Feburary_3
        all_countries_d['Feburary_4']=Feburary_4
        all_countries_d['Feburary_5']=Feburary_5
        all_countries_d['Feburary_6']=Feburary_6
        all_countries_d['Feburary_7']=Feburary_7
        all_countries_d['Feburary_8']=Feburary_8
        all_countries_d['Feburary_9']=Feburary_9
        all_countries_d['Feburary_10']=Feburary_10
        all_countries_d['Feburary_11']=Feburary_11
        all_countries_d['Feburary_12']=Feburary_12
        all_countries_d['Feburary_13']=Feburary_13
        all_countries_d['Feburary_14']=Feburary_14
        all_countries_d['Feburary_15']=Feburary_15
        all_countries_d['Feburary_16']=Feburary_16
        all_countries_d['Feburary_17']=Feburary_17
        all_countries_d['Feburary_18']=Feburary_18
        all_countries_d['Feburary_19']=Feburary_19
        all_countries_d['Feburary_20']=Feburary_20
        all_countries_d['Feburary_21']=Feburary_21
        all_countries_d['Feburary_22']=Feburary_22
        all_countries_d['Feburary_23']=Feburary_23
        all_countries_d['Feburary_24']=Feburary_24
        all_countries_d['Feburary_25']=Feburary_25
        all_countries_d['Feburary_26']=Feburary_26
        all_countries_d['Feburary_27']=Feburary_27
        all_countries_d['Feburary_28']=Feburary_28
        all_countries_d['Feburary_29']=Feburary_29
        all_countries_d['March_1']=March_1
        all_countries_d['March_2']=March_2
        all_countries_d['March_3']=March_3
        all_countries_d['March_4']=March_4
        all_countries_d['March_5']=March_5
        all_countries_d['March_6']=March_6
        all_countries_d['March_7']=March_7
        all_countries_d['March_8']=March_8
        all_countries_d['March_9']=March_9
        all_countries_d['March_10']=March_10
        all_countries_d['March_11']=March_11
        all_countries_d['March_12']=March_12
        all_countries_d['March_13']=March_13
        all_countries_d['March_14']=March_14
        all_countries_d['March_15']=March_15
        all_countries_d['March_16']=March_16
        all_countries_d['March_17']=March_17
        all_countries_d['March_18']=March_18
        all_countries_d['March_19']=March_19
        all_countries_d['March_20']=March_20
        all_countries_d['March_21']=March_21
        all_countries_d['March_22']=March_22
        all_countries_d['March_23']=March_23
        all_countries_d['March_24']=March_24
        all_countries_d['March_25']=March_25
        all_countries_d['March_26']=March_26
        all_countries_d['March_27']=March_27
        all_countries_d['March_28']=March_28
        all_countries_d['March_29']=March_29
        all_countries_d['March_30']=March_30
        all_countries_d['March_31']=March_31
        all_countries_d['April_1']=April_1
        all_countries_d['April_2']=April_2
        all_countries_d['April_3']=April_3
        all_countries_d['April_4']=April_4
        all_countries_d['April_5']=April_5
        all_countries_d['April_6']=April_6
        all_countries_d['April_7']=April_7
        all_countries_d['April_8']=April_8
        all_countries_d['April_9']=April_9
        all_countries_d['April_10']=April_10
        all_countries_d['April_11']=April_11
        all_countries_d['April_12']=April_12
        all_countries_d['April_13']=April_13
        all_countries_d['April_14']=April_14
        all_countries_d['April_15']=April_15
        all_countries_d['April_16']=April_16
        all_countries_d['April_17']=April_17
        all_countries_d['April_18']=April_18
        all_countries_d['April_19']=April_19
        all_countries_d['April_20']=April_20
        all_countries_d['April_21']=April_21
        all_countries_d['April_22']=April_22

        all_countries_all.append(all_countries_d)
                
    return jsonify(all_countries_all)

@app.route("/project2/data/confirmed")
def confirmed_data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    confirmed_final= session.query(confirmed_t.row_number,confirmed_t.fips,confirmed_t.estado, confirmed_t.pais, confirmed_t.status, confirmed_t.Lat, confirmed_t.Long, confirmed_t.January_22, confirmed_t.January_23, confirmed_t.January_24, confirmed_t.January_25, confirmed_t.January_26, confirmed_t.January_27, confirmed_t.January_28, confirmed_t.January_29, confirmed_t.January_30, confirmed_t.January_31, confirmed_t.Feburary_1, confirmed_t.Feburary_2, confirmed_t.Feburary_3, confirmed_t.Feburary_4, confirmed_t.Feburary_5, confirmed_t.Feburary_6, confirmed_t.Feburary_7, confirmed_t.Feburary_8, confirmed_t.Feburary_9, confirmed_t.Feburary_10, confirmed_t.Feburary_11, confirmed_t.Feburary_12, confirmed_t.Feburary_13, confirmed_t.Feburary_14, confirmed_t.Feburary_15, confirmed_t.Feburary_16, confirmed_t.Feburary_17, confirmed_t.Feburary_18, confirmed_t.Feburary_19, confirmed_t.Feburary_20, confirmed_t.Feburary_21, confirmed_t.Feburary_22, confirmed_t.Feburary_23, confirmed_t.Feburary_24, confirmed_t.Feburary_25, confirmed_t.Feburary_26, confirmed_t.Feburary_27, confirmed_t.Feburary_28, confirmed_t.Feburary_29, confirmed_t.March_1, confirmed_t.March_2, confirmed_t.March_3,confirmed_t.March_4, confirmed_t.March_5, confirmed_t.March_6, confirmed_t.March_7, confirmed_t.March_8, confirmed_t.March_9, confirmed_t.March_10, confirmed_t.March_11, confirmed_t.March_12, confirmed_t.March_13, confirmed_t.March_14, confirmed_t.March_15, confirmed_t.March_16, confirmed_t.March_17, confirmed_t.March_18, confirmed_t.March_19, confirmed_t.March_20, confirmed_t.March_21, confirmed_t.March_22, confirmed_t.March_23, confirmed_t.March_24, confirmed_t.March_25, confirmed_t.March_26, confirmed_t.March_27, confirmed_t.March_28, confirmed_t.March_29, confirmed_t.March_30, confirmed_t.March_31, confirmed_t.April_1, confirmed_t.April_2, confirmed_t.April_3, confirmed_t.April_4, confirmed_t.April_5, confirmed_t.April_6, confirmed_t.April_7, confirmed_t.April_8, confirmed_t.April_9, confirmed_t.April_10, confirmed_t.April_11, confirmed_t.April_12, confirmed_t.April_13, confirmed_t.April_14, confirmed_t.April_15, confirmed_t.April_16, confirmed_t.April_17, confirmed_t.April_18, confirmed_t.April_19, confirmed_t.April_20, confirmed_t.April_21, confirmed_t.April_22).all()
        
    session.close()
            
    # Create a dictionary
            
    confirmed_all = []
    for row_number, fips, estado, pais, status, Lat, Long, January_22, January_23, January_24, January_25, January_26, January_27, January_28, January_29, January_30, January_31, Feburary_1, Feburary_2, Feburary_3, Feburary_4, Feburary_5, Feburary_6, Feburary_7, Feburary_8, Feburary_9, Feburary_10, Feburary_11, Feburary_12, Feburary_13, Feburary_14, Feburary_15, Feburary_16, Feburary_17, Feburary_18, Feburary_19, Feburary_20, Feburary_21, Feburary_22, Feburary_23, Feburary_24, Feburary_25, Feburary_26, Feburary_27, Feburary_28, Feburary_29, March_1, March_2, March_3, March_4, March_5, March_6, March_7, March_8, March_9, March_10, March_11, March_12, March_13, March_14, March_15, March_16, March_17, March_18, March_19, March_20, March_21, March_22, March_23, March_24, March_25, March_26, March_27, March_28, March_29, March_30, March_31, April_1, April_2, April_3, April_4, April_5, April_6, April_7, April_8, April_9, April_10, April_11, April_12, April_13, April_14, April_15, April_16, April_17, April_18, April_19, April_20, April_21, April_22, in confirmed_final:
        confirmed_d = {}
        confirmed_d["row_number"] = row_number
        confirmed_d["fips"] = fips
        confirmed_d["estado"] = estado
        confirmed_d["pais"] = pais
        confirmed_d["status"] = status
        confirmed_d["Lat"] = Lat
        confirmed_d["Long"] = Long
        confirmed_d['January_22']=January_22
        confirmed_d['January_23']=January_23
        confirmed_d['January_24']=January_24
        confirmed_d['January_25']=January_25
        confirmed_d['January_26']=January_26
        confirmed_d['January_27']=January_27
        confirmed_d['January_28']=January_28
        confirmed_d['January_29']=January_29
        confirmed_d['January_30']=January_30
        confirmed_d['January_31']=January_31
        confirmed_d['Feburary_1']=Feburary_1
        confirmed_d['Feburary_2']=Feburary_2
        confirmed_d['Feburary_3']=Feburary_3
        confirmed_d['Feburary_4']=Feburary_4
        confirmed_d['Feburary_5']=Feburary_5
        confirmed_d['Feburary_6']=Feburary_6
        confirmed_d['Feburary_7']=Feburary_7
        confirmed_d['Feburary_8']=Feburary_8
        confirmed_d['Feburary_9']=Feburary_9
        confirmed_d['Feburary_10']=Feburary_10
        confirmed_d['Feburary_11']=Feburary_11
        confirmed_d['Feburary_12']=Feburary_12
        confirmed_d['Feburary_13']=Feburary_13
        confirmed_d['Feburary_14']=Feburary_14
        confirmed_d['Feburary_15']=Feburary_15
        confirmed_d['Feburary_16']=Feburary_16
        confirmed_d['Feburary_17']=Feburary_17
        confirmed_d['Feburary_18']=Feburary_18
        confirmed_d['Feburary_19']=Feburary_19
        confirmed_d['Feburary_20']=Feburary_20
        confirmed_d['Feburary_21']=Feburary_21
        confirmed_d['Feburary_22']=Feburary_22
        confirmed_d['Feburary_23']=Feburary_23
        confirmed_d['Feburary_24']=Feburary_24
        confirmed_d['Feburary_25']=Feburary_25
        confirmed_d['Feburary_26']=Feburary_26
        confirmed_d['Feburary_27']=Feburary_27
        confirmed_d['Feburary_28']=Feburary_28
        confirmed_d['Feburary_29']=Feburary_29
        confirmed_d['March_1']=March_1
        confirmed_d['March_2']=March_2
        confirmed_d['March_3']=March_3
        confirmed_d['March_4']=March_4
        confirmed_d['March_5']=March_5
        confirmed_d['March_6']=March_6
        confirmed_d['March_7']=March_7
        confirmed_d['March_8']=March_8
        confirmed_d['March_9']=March_9
        confirmed_d['March_10']=March_10
        confirmed_d['March_11']=March_11
        confirmed_d['March_12']=March_12
        confirmed_d['March_13']=March_13
        confirmed_d['March_14']=March_14
        confirmed_d['March_15']=March_15
        confirmed_d['March_16']=March_16
        confirmed_d['March_17']=March_17
        confirmed_d['March_18']=March_18
        confirmed_d['March_19']=March_19
        confirmed_d['March_20']=March_20
        confirmed_d['March_21']=March_21
        confirmed_d['March_22']=March_22
        confirmed_d['March_23']=March_23
        confirmed_d['March_24']=March_24
        confirmed_d['March_25']=March_25
        confirmed_d['March_26']=March_26
        confirmed_d['March_27']=March_27
        confirmed_d['March_28']=March_28
        confirmed_d['March_29']=March_29
        confirmed_d['March_30']=March_30
        confirmed_d['March_31']=March_31
        confirmed_d['April_1']=April_1
        confirmed_d['April_2']=April_2
        confirmed_d['April_3']=April_3
        confirmed_d['April_4']=April_4
        confirmed_d['April_5']=April_5
        confirmed_d['April_6']=April_6
        confirmed_d['April_7']=April_7
        confirmed_d['April_8']=April_8
        confirmed_d['April_9']=April_9
        confirmed_d['April_10']=April_10
        confirmed_d['April_11']=April_11
        confirmed_d['April_12']=April_12
        confirmed_d['April_13']=April_13
        confirmed_d['April_14']=April_14
        confirmed_d['April_15']=April_15
        confirmed_d['April_16']=April_16
        confirmed_d['April_17']=April_17
        confirmed_d['April_18']=April_18
        confirmed_d['April_19']=April_19
        confirmed_d['April_20']=April_20
        confirmed_d['April_21']=April_21
        confirmed_d['April_22']=April_22

        confirmed_all.append(confirmed_d)
                
    return jsonify(confirmed_all)


@app.route("/project2/data/death")
def death_data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    death_final= session.query(death_t.row_number,death_t.fips,death_t.estado, death_t.pais, death_t.status, death_t.Lat, death_t.Long, death_t.January_22, death_t.January_23, death_t.January_24, death_t.January_25, death_t.January_26, death_t.January_27, death_t.January_28, death_t.January_29, death_t.January_30, death_t.January_31, death_t.Feburary_1, death_t.Feburary_2, death_t.Feburary_3, death_t.Feburary_4, death_t.Feburary_5, death_t.Feburary_6, death_t.Feburary_7, death_t.Feburary_8, death_t.Feburary_9, death_t.Feburary_10, death_t.Feburary_11, death_t.Feburary_12, death_t.Feburary_13, death_t.Feburary_14, death_t.Feburary_15, death_t.Feburary_16, death_t.Feburary_17, death_t.Feburary_18, death_t.Feburary_19, death_t.Feburary_20, death_t.Feburary_21, death_t.Feburary_22, death_t.Feburary_23, death_t.Feburary_24, death_t.Feburary_25, death_t.Feburary_26, death_t.Feburary_27, death_t.Feburary_28, death_t.Feburary_29, death_t.March_1, death_t.March_2, death_t.March_3,death_t.March_4, death_t.March_5, death_t.March_6, death_t.March_7, death_t.March_8, death_t.March_9, death_t.March_10, death_t.March_11, death_t.March_12, death_t.March_13, death_t.March_14, death_t.March_15, death_t.March_16, death_t.March_17, death_t.March_18, death_t.March_19, death_t.March_20, death_t.March_21, death_t.March_22, death_t.March_23, death_t.March_24, death_t.March_25, death_t.March_26, death_t.March_27, death_t.March_28, death_t.March_29, death_t.March_30, death_t.March_31, death_t.April_1, death_t.April_2, death_t.April_3, death_t.April_4, death_t.April_5, death_t.April_6, death_t.April_7, death_t.April_8, death_t.April_9, death_t.April_10, death_t.April_11, death_t.April_12, death_t.April_13, death_t.April_14, death_t.April_15, death_t.April_16, death_t.April_17, death_t.April_18, death_t.April_19, death_t.April_20, death_t.April_21, death_t.April_22).all()
        
    session.close()
            
    # Create a dictionary
            
    death_all = []
    for row_number, fips, estado, pais, status, Lat, Long, January_22, January_23, January_24, January_25, January_26, January_27, January_28, January_29, January_30, January_31, Feburary_1, Feburary_2, Feburary_3, Feburary_4, Feburary_5, Feburary_6, Feburary_7, Feburary_8, Feburary_9, Feburary_10, Feburary_11, Feburary_12, Feburary_13, Feburary_14, Feburary_15, Feburary_16, Feburary_17, Feburary_18, Feburary_19, Feburary_20, Feburary_21, Feburary_22, Feburary_23, Feburary_24, Feburary_25, Feburary_26, Feburary_27, Feburary_28, Feburary_29, March_1, March_2, March_3, March_4, March_5, March_6, March_7, March_8, March_9, March_10, March_11, March_12, March_13, March_14, March_15, March_16, March_17, March_18, March_19, March_20, March_21, March_22, March_23, March_24, March_25, March_26, March_27, March_28, March_29, March_30, March_31, April_1, April_2, April_3, April_4, April_5, April_6, April_7, April_8, April_9, April_10, April_11, April_12, April_13, April_14, April_15, April_16, April_17, April_18, April_19, April_20, April_21, April_22, in death_final:
        death_d = {}
        death_d["row_number"] = row_number
        death_d["fips"] = fips
        death_d["estado"] = estado
        death_d["pais"] = pais
        death_d["status"] = status
        death_d["Lat"] = Lat
        death_d["Long"] = Long
        death_d['January_22']=January_22
        death_d['January_23']=January_23
        death_d['January_24']=January_24
        death_d['January_25']=January_25
        death_d['January_26']=January_26
        death_d['January_27']=January_27
        death_d['January_28']=January_28
        death_d['January_29']=January_29
        death_d['January_30']=January_30
        death_d['January_31']=January_31
        death_d['Feburary_1']=Feburary_1
        death_d['Feburary_2']=Feburary_2
        death_d['Feburary_3']=Feburary_3
        death_d['Feburary_4']=Feburary_4
        death_d['Feburary_5']=Feburary_5
        death_d['Feburary_6']=Feburary_6
        death_d['Feburary_7']=Feburary_7
        death_d['Feburary_8']=Feburary_8
        death_d['Feburary_9']=Feburary_9
        death_d['Feburary_10']=Feburary_10
        death_d['Feburary_11']=Feburary_11
        death_d['Feburary_12']=Feburary_12
        death_d['Feburary_13']=Feburary_13
        death_d['Feburary_14']=Feburary_14
        death_d['Feburary_15']=Feburary_15
        death_d['Feburary_16']=Feburary_16
        death_d['Feburary_17']=Feburary_17
        death_d['Feburary_18']=Feburary_18
        death_d['Feburary_19']=Feburary_19
        death_d['Feburary_20']=Feburary_20
        death_d['Feburary_21']=Feburary_21
        death_d['Feburary_22']=Feburary_22
        death_d['Feburary_23']=Feburary_23
        death_d['Feburary_24']=Feburary_24
        death_d['Feburary_25']=Feburary_25
        death_d['Feburary_26']=Feburary_26
        death_d['Feburary_27']=Feburary_27
        death_d['Feburary_28']=Feburary_28
        death_d['Feburary_29']=Feburary_29
        death_d['March_1']=March_1
        death_d['March_2']=March_2
        death_d['March_3']=March_3
        death_d['March_4']=March_4
        death_d['March_5']=March_5
        death_d['March_6']=March_6
        death_d['March_7']=March_7
        death_d['March_8']=March_8
        death_d['March_9']=March_9
        death_d['March_10']=March_10
        death_d['March_11']=March_11
        death_d['March_12']=March_12
        death_d['March_13']=March_13
        death_d['March_14']=March_14
        death_d['March_15']=March_15
        death_d['March_16']=March_16
        death_d['March_17']=March_17
        death_d['March_18']=March_18
        death_d['March_19']=March_19
        death_d['March_20']=March_20
        death_d['March_21']=March_21
        death_d['March_22']=March_22
        death_d['March_23']=March_23
        death_d['March_24']=March_24
        death_d['March_25']=March_25
        death_d['March_26']=March_26
        death_d['March_27']=March_27
        death_d['March_28']=March_28
        death_d['March_29']=March_29
        death_d['March_30']=March_30
        death_d['March_31']=March_31
        death_d['April_1']=April_1
        death_d['April_2']=April_2
        death_d['April_3']=April_3
        death_d['April_4']=April_4
        death_d['April_5']=April_5
        death_d['April_6']=April_6
        death_d['April_7']=April_7
        death_d['April_8']=April_8
        death_d['April_9']=April_9
        death_d['April_10']=April_10
        death_d['April_11']=April_11
        death_d['April_12']=April_12
        death_d['April_13']=April_13
        death_d['April_14']=April_14
        death_d['April_15']=April_15
        death_d['April_16']=April_16
        death_d['April_17']=April_17
        death_d['April_18']=April_18
        death_d['April_19']=April_19
        death_d['April_20']=April_20
        death_d['April_21']=April_21
        death_d['April_22']=April_22

        death_all.append(death_d)
                
    return jsonify(death_all)


@app.route("/project2/data/defunciones")
def defunciones_data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    defunciones_final= session.query(defunciones_t.row_number,defunciones_t.fips,defunciones_t.estado, defunciones_t.pais, defunciones_t.status, defunciones_t.Lat, defunciones_t.Long, defunciones_t.January_22, defunciones_t.January_23, defunciones_t.January_24, defunciones_t.January_25, defunciones_t.January_26, defunciones_t.January_27, defunciones_t.January_28, defunciones_t.January_29, defunciones_t.January_30, defunciones_t.January_31, defunciones_t.Feburary_1, defunciones_t.Feburary_2, defunciones_t.Feburary_3, defunciones_t.Feburary_4, defunciones_t.Feburary_5, defunciones_t.Feburary_6, defunciones_t.Feburary_7, defunciones_t.Feburary_8, defunciones_t.Feburary_9, defunciones_t.Feburary_10, defunciones_t.Feburary_11, defunciones_t.Feburary_12, defunciones_t.Feburary_13, defunciones_t.Feburary_14, defunciones_t.Feburary_15, defunciones_t.Feburary_16, defunciones_t.Feburary_17, defunciones_t.Feburary_18, defunciones_t.Feburary_19, defunciones_t.Feburary_20, defunciones_t.Feburary_21, defunciones_t.Feburary_22, defunciones_t.Feburary_23, defunciones_t.Feburary_24, defunciones_t.Feburary_25, defunciones_t.Feburary_26, defunciones_t.Feburary_27, defunciones_t.Feburary_28, defunciones_t.Feburary_29, defunciones_t.March_1, defunciones_t.March_2, defunciones_t.March_3,defunciones_t.March_4, defunciones_t.March_5, defunciones_t.March_6, defunciones_t.March_7, defunciones_t.March_8, defunciones_t.March_9, defunciones_t.March_10, defunciones_t.March_11, defunciones_t.March_12, defunciones_t.March_13, defunciones_t.March_14, defunciones_t.March_15, defunciones_t.March_16, defunciones_t.March_17, defunciones_t.March_18, defunciones_t.March_19, defunciones_t.March_20, defunciones_t.March_21, defunciones_t.March_22, defunciones_t.March_23, defunciones_t.March_24, defunciones_t.March_25, defunciones_t.March_26, defunciones_t.March_27, defunciones_t.March_28, defunciones_t.March_29, defunciones_t.March_30, defunciones_t.March_31, defunciones_t.April_1, defunciones_t.April_2, defunciones_t.April_3, defunciones_t.April_4, defunciones_t.April_5, defunciones_t.April_6, defunciones_t.April_7, defunciones_t.April_8, defunciones_t.April_9, defunciones_t.April_10, defunciones_t.April_11, defunciones_t.April_12, defunciones_t.April_13, defunciones_t.April_14, defunciones_t.April_15, defunciones_t.April_16, defunciones_t.April_17, defunciones_t.April_18, defunciones_t.April_19, defunciones_t.April_20, defunciones_t.April_21, defunciones_t.April_22).all()
        
    session.close()
            
    # Create a dictionary
            
    defunciones_all = []
    for row_number, fips, estado, pais, status, Lat, Long, January_22, January_23, January_24, January_25, January_26, January_27, January_28, January_29, January_30, January_31, Feburary_1, Feburary_2, Feburary_3, Feburary_4, Feburary_5, Feburary_6, Feburary_7, Feburary_8, Feburary_9, Feburary_10, Feburary_11, Feburary_12, Feburary_13, Feburary_14, Feburary_15, Feburary_16, Feburary_17, Feburary_18, Feburary_19, Feburary_20, Feburary_21, Feburary_22, Feburary_23, Feburary_24, Feburary_25, Feburary_26, Feburary_27, Feburary_28, Feburary_29, March_1, March_2, March_3, March_4, March_5, March_6, March_7, March_8, March_9, March_10, March_11, March_12, March_13, March_14, March_15, March_16, March_17, March_18, March_19, March_20, March_21, March_22, March_23, March_24, March_25, March_26, March_27, March_28, March_29, March_30, March_31, April_1, April_2, April_3, April_4, April_5, April_6, April_7, April_8, April_9, April_10, April_11, April_12, April_13, April_14, April_15, April_16, April_17, April_18, April_19, April_20, April_21, April_22, in defunciones_final:
        defunciones_d = {}
        defunciones_d["row_number"] = row_number
        defunciones_d["fips"] = fips
        defunciones_d["estado"] = estado
        defunciones_d["pais"] = pais
        defunciones_d["status"] = status
        defunciones_d["Lat"] = Lat
        defunciones_d["Long"] = Long
        defunciones_d['January_22']=January_22
        defunciones_d['January_23']=January_23
        defunciones_d['January_24']=January_24
        defunciones_d['January_25']=January_25
        defunciones_d['January_26']=January_26
        defunciones_d['January_27']=January_27
        defunciones_d['January_28']=January_28
        defunciones_d['January_29']=January_29
        defunciones_d['January_30']=January_30
        defunciones_d['January_31']=January_31
        defunciones_d['Feburary_1']=Feburary_1
        defunciones_d['Feburary_2']=Feburary_2
        defunciones_d['Feburary_3']=Feburary_3
        defunciones_d['Feburary_4']=Feburary_4
        defunciones_d['Feburary_5']=Feburary_5
        defunciones_d['Feburary_6']=Feburary_6
        defunciones_d['Feburary_7']=Feburary_7
        defunciones_d['Feburary_8']=Feburary_8
        defunciones_d['Feburary_9']=Feburary_9
        defunciones_d['Feburary_10']=Feburary_10
        defunciones_d['Feburary_11']=Feburary_11
        defunciones_d['Feburary_12']=Feburary_12
        defunciones_d['Feburary_13']=Feburary_13
        defunciones_d['Feburary_14']=Feburary_14
        defunciones_d['Feburary_15']=Feburary_15
        defunciones_d['Feburary_16']=Feburary_16
        defunciones_d['Feburary_17']=Feburary_17
        defunciones_d['Feburary_18']=Feburary_18
        defunciones_d['Feburary_19']=Feburary_19
        defunciones_d['Feburary_20']=Feburary_20
        defunciones_d['Feburary_21']=Feburary_21
        defunciones_d['Feburary_22']=Feburary_22
        defunciones_d['Feburary_23']=Feburary_23
        defunciones_d['Feburary_24']=Feburary_24
        defunciones_d['Feburary_25']=Feburary_25
        defunciones_d['Feburary_26']=Feburary_26
        defunciones_d['Feburary_27']=Feburary_27
        defunciones_d['Feburary_28']=Feburary_28
        defunciones_d['Feburary_29']=Feburary_29
        defunciones_d['March_1']=March_1
        defunciones_d['March_2']=March_2
        defunciones_d['March_3']=March_3
        defunciones_d['March_4']=March_4
        defunciones_d['March_5']=March_5
        defunciones_d['March_6']=March_6
        defunciones_d['March_7']=March_7
        defunciones_d['March_8']=March_8
        defunciones_d['March_9']=March_9
        defunciones_d['March_10']=March_10
        defunciones_d['March_11']=March_11
        defunciones_d['March_12']=March_12
        defunciones_d['March_13']=March_13
        defunciones_d['March_14']=March_14
        defunciones_d['March_15']=March_15
        defunciones_d['March_16']=March_16
        defunciones_d['March_17']=March_17
        defunciones_d['March_18']=March_18
        defunciones_d['March_19']=March_19
        defunciones_d['March_20']=March_20
        defunciones_d['March_21']=March_21
        defunciones_d['March_22']=March_22
        defunciones_d['March_23']=March_23
        defunciones_d['March_24']=March_24
        defunciones_d['March_25']=March_25
        defunciones_d['March_26']=March_26
        defunciones_d['March_27']=March_27
        defunciones_d['March_28']=March_28
        defunciones_d['March_29']=March_29
        defunciones_d['March_30']=March_30
        defunciones_d['March_31']=March_31
        defunciones_d['April_1']=April_1
        defunciones_d['April_2']=April_2
        defunciones_d['April_3']=April_3
        defunciones_d['April_4']=April_4
        defunciones_d['April_5']=April_5
        defunciones_d['April_6']=April_6
        defunciones_d['April_7']=April_7
        defunciones_d['April_8']=April_8
        defunciones_d['April_9']=April_9
        defunciones_d['April_10']=April_10
        defunciones_d['April_11']=April_11
        defunciones_d['April_12']=April_12
        defunciones_d['April_13']=April_13
        defunciones_d['April_14']=April_14
        defunciones_d['April_15']=April_15
        defunciones_d['April_16']=April_16
        defunciones_d['April_17']=April_17
        defunciones_d['April_18']=April_18
        defunciones_d['April_19']=April_19
        defunciones_d['April_20']=April_20
        defunciones_d['April_21']=April_21
        defunciones_d['April_22']=April_22

        defunciones_all.append(defunciones_d)
                
    return jsonify(defunciones_all)

@app.route("/project2/data/confirmados")
def confirmados_data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    confirmados_final= session.query(confirmados_t.row_number,confirmados_t.fips,confirmados_t.estado, confirmados_t.pais, confirmados_t.status, confirmados_t.Lat, confirmados_t.Long, confirmados_t.January_22, confirmados_t.January_23, confirmados_t.January_24, confirmados_t.January_25, confirmados_t.January_26, confirmados_t.January_27, confirmados_t.January_28, confirmados_t.January_29, confirmados_t.January_30, confirmados_t.January_31, confirmados_t.Feburary_1, confirmados_t.Feburary_2, confirmados_t.Feburary_3, confirmados_t.Feburary_4, confirmados_t.Feburary_5, confirmados_t.Feburary_6, confirmados_t.Feburary_7, confirmados_t.Feburary_8, confirmados_t.Feburary_9, confirmados_t.Feburary_10, confirmados_t.Feburary_11, confirmados_t.Feburary_12, confirmados_t.Feburary_13, confirmados_t.Feburary_14, confirmados_t.Feburary_15, confirmados_t.Feburary_16, confirmados_t.Feburary_17, confirmados_t.Feburary_18, confirmados_t.Feburary_19, confirmados_t.Feburary_20, confirmados_t.Feburary_21, confirmados_t.Feburary_22, confirmados_t.Feburary_23, confirmados_t.Feburary_24, confirmados_t.Feburary_25, confirmados_t.Feburary_26, confirmados_t.Feburary_27, confirmados_t.Feburary_28, confirmados_t.Feburary_29, confirmados_t.March_1, confirmados_t.March_2, confirmados_t.March_3,confirmados_t.March_4, confirmados_t.March_5, confirmados_t.March_6, confirmados_t.March_7, confirmados_t.March_8, confirmados_t.March_9, confirmados_t.March_10, confirmados_t.March_11, confirmados_t.March_12, confirmados_t.March_13, confirmados_t.March_14, confirmados_t.March_15, confirmados_t.March_16, confirmados_t.March_17, confirmados_t.March_18, confirmados_t.March_19, confirmados_t.March_20, confirmados_t.March_21, confirmados_t.March_22, confirmados_t.March_23, confirmados_t.March_24, confirmados_t.March_25, confirmados_t.March_26, confirmados_t.March_27, confirmados_t.March_28, confirmados_t.March_29, confirmados_t.March_30, confirmados_t.March_31, confirmados_t.April_1, confirmados_t.April_2, confirmados_t.April_3, confirmados_t.April_4, confirmados_t.April_5, confirmados_t.April_6, confirmados_t.April_7, confirmados_t.April_8, confirmados_t.April_9, confirmados_t.April_10, confirmados_t.April_11, confirmados_t.April_12, confirmados_t.April_13, confirmados_t.April_14, confirmados_t.April_15, confirmados_t.April_16, confirmados_t.April_17, confirmados_t.April_18, confirmados_t.April_19, confirmados_t.April_20, confirmados_t.April_21, confirmados_t.April_22).all()
        
    session.close()
            
    # Create a dictionary
            
    confirmados_all = []
    for row_number, fips, estado, pais, status, Lat, Long, January_22, January_23, January_24, January_25, January_26, January_27, January_28, January_29, January_30, January_31, Feburary_1, Feburary_2, Feburary_3, Feburary_4, Feburary_5, Feburary_6, Feburary_7, Feburary_8, Feburary_9, Feburary_10, Feburary_11, Feburary_12, Feburary_13, Feburary_14, Feburary_15, Feburary_16, Feburary_17, Feburary_18, Feburary_19, Feburary_20, Feburary_21, Feburary_22, Feburary_23, Feburary_24, Feburary_25, Feburary_26, Feburary_27, Feburary_28, Feburary_29, March_1, March_2, March_3, March_4, March_5, March_6, March_7, March_8, March_9, March_10, March_11, March_12, March_13, March_14, March_15, March_16, March_17, March_18, March_19, March_20, March_21, March_22, March_23, March_24, March_25, March_26, March_27, March_28, March_29, March_30, March_31, April_1, April_2, April_3, April_4, April_5, April_6, April_7, April_8, April_9, April_10, April_11, April_12, April_13, April_14, April_15, April_16, April_17, April_18, April_19, April_20, April_21, April_22, in confirmados_final:
        confirmados_d = {}
        confirmados_d["row_number"] = row_number
        confirmados_d["fips"] = fips
        confirmados_d["estado"] = estado
        confirmados_d["pais"] = pais
        confirmados_d["status"] = status
        confirmados_d["Lat"] = Lat
        confirmados_d["Long"] = Long
        confirmados_d['January_22']=January_22
        confirmados_d['January_23']=January_23
        confirmados_d['January_24']=January_24
        confirmados_d['January_25']=January_25
        confirmados_d['January_26']=January_26
        confirmados_d['January_27']=January_27
        confirmados_d['January_28']=January_28
        confirmados_d['January_29']=January_29
        confirmados_d['January_30']=January_30
        confirmados_d['January_31']=January_31
        confirmados_d['Feburary_1']=Feburary_1
        confirmados_d['Feburary_2']=Feburary_2
        confirmados_d['Feburary_3']=Feburary_3
        confirmados_d['Feburary_4']=Feburary_4
        confirmados_d['Feburary_5']=Feburary_5
        confirmados_d['Feburary_6']=Feburary_6
        confirmados_d['Feburary_7']=Feburary_7
        confirmados_d['Feburary_8']=Feburary_8
        confirmados_d['Feburary_9']=Feburary_9
        confirmados_d['Feburary_10']=Feburary_10
        confirmados_d['Feburary_11']=Feburary_11
        confirmados_d['Feburary_12']=Feburary_12
        confirmados_d['Feburary_13']=Feburary_13
        confirmados_d['Feburary_14']=Feburary_14
        confirmados_d['Feburary_15']=Feburary_15
        confirmados_d['Feburary_16']=Feburary_16
        confirmados_d['Feburary_17']=Feburary_17
        confirmados_d['Feburary_18']=Feburary_18
        confirmados_d['Feburary_19']=Feburary_19
        confirmados_d['Feburary_20']=Feburary_20
        confirmados_d['Feburary_21']=Feburary_21
        confirmados_d['Feburary_22']=Feburary_22
        confirmados_d['Feburary_23']=Feburary_23
        confirmados_d['Feburary_24']=Feburary_24
        confirmados_d['Feburary_25']=Feburary_25
        confirmados_d['Feburary_26']=Feburary_26
        confirmados_d['Feburary_27']=Feburary_27
        confirmados_d['Feburary_28']=Feburary_28
        confirmados_d['Feburary_29']=Feburary_29
        confirmados_d['March_1']=March_1
        confirmados_d['March_2']=March_2
        confirmados_d['March_3']=March_3
        confirmados_d['March_4']=March_4
        confirmados_d['March_5']=March_5
        confirmados_d['March_6']=March_6
        confirmados_d['March_7']=March_7
        confirmados_d['March_8']=March_8
        confirmados_d['March_9']=March_9
        confirmados_d['March_10']=March_10
        confirmados_d['March_11']=March_11
        confirmados_d['March_12']=March_12
        confirmados_d['March_13']=March_13
        confirmados_d['March_14']=March_14
        confirmados_d['March_15']=March_15
        confirmados_d['March_16']=March_16
        confirmados_d['March_17']=March_17
        confirmados_d['March_18']=March_18
        confirmados_d['March_19']=March_19
        confirmados_d['March_20']=March_20
        confirmados_d['March_21']=March_21
        confirmados_d['March_22']=March_22
        confirmados_d['March_23']=March_23
        confirmados_d['March_24']=March_24
        confirmados_d['March_25']=March_25
        confirmados_d['March_26']=March_26
        confirmados_d['March_27']=March_27
        confirmados_d['March_28']=March_28
        confirmados_d['March_29']=March_29
        confirmados_d['March_30']=March_30
        confirmados_d['March_31']=March_31
        confirmados_d['April_1']=April_1
        confirmados_d['April_2']=April_2
        confirmados_d['April_3']=April_3
        confirmados_d['April_4']=April_4
        confirmados_d['April_5']=April_5
        confirmados_d['April_6']=April_6
        confirmados_d['April_7']=April_7
        confirmados_d['April_8']=April_8
        confirmados_d['April_9']=April_9
        confirmados_d['April_10']=April_10
        confirmados_d['April_11']=April_11
        confirmados_d['April_12']=April_12
        confirmados_d['April_13']=April_13
        confirmados_d['April_14']=April_14
        confirmados_d['April_15']=April_15
        confirmados_d['April_16']=April_16
        confirmados_d['April_17']=April_17
        confirmados_d['April_18']=April_18
        confirmados_d['April_19']=April_19
        confirmados_d['April_20']=April_20
        confirmados_d['April_21']=April_21
        confirmados_d['April_22']=April_22

        confirmados_all.append(confirmados_d)
                
    return jsonify(confirmados_all)

@app.route("/project2/data/negativos")
def negativos_data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    negativos_final= session.query(negativos_t.row_number,negativos_t.fips,negativos_t.estado, negativos_t.pais, negativos_t.status, negativos_t.Lat, negativos_t.Long, negativos_t.January_22, negativos_t.January_23, negativos_t.January_24, negativos_t.January_25, negativos_t.January_26, negativos_t.January_27, negativos_t.January_28, negativos_t.January_29, negativos_t.January_30, negativos_t.January_31, negativos_t.Feburary_1, negativos_t.Feburary_2, negativos_t.Feburary_3, negativos_t.Feburary_4, negativos_t.Feburary_5, negativos_t.Feburary_6, negativos_t.Feburary_7, negativos_t.Feburary_8, negativos_t.Feburary_9, negativos_t.Feburary_10, negativos_t.Feburary_11, negativos_t.Feburary_12, negativos_t.Feburary_13, negativos_t.Feburary_14, negativos_t.Feburary_15, negativos_t.Feburary_16, negativos_t.Feburary_17, negativos_t.Feburary_18, negativos_t.Feburary_19, negativos_t.Feburary_20, negativos_t.Feburary_21, negativos_t.Feburary_22, negativos_t.Feburary_23, negativos_t.Feburary_24, negativos_t.Feburary_25, negativos_t.Feburary_26, negativos_t.Feburary_27, negativos_t.Feburary_28, negativos_t.Feburary_29, negativos_t.March_1, negativos_t.March_2, negativos_t.March_3,negativos_t.March_4, negativos_t.March_5, negativos_t.March_6, negativos_t.March_7, negativos_t.March_8, negativos_t.March_9, negativos_t.March_10, negativos_t.March_11, negativos_t.March_12, negativos_t.March_13, negativos_t.March_14, negativos_t.March_15, negativos_t.March_16, negativos_t.March_17, negativos_t.March_18, negativos_t.March_19, negativos_t.March_20, negativos_t.March_21, negativos_t.March_22, negativos_t.March_23, negativos_t.March_24, negativos_t.March_25, negativos_t.March_26, negativos_t.March_27, negativos_t.March_28, negativos_t.March_29, negativos_t.March_30, negativos_t.March_31, negativos_t.April_1, negativos_t.April_2, negativos_t.April_3, negativos_t.April_4, negativos_t.April_5, negativos_t.April_6, negativos_t.April_7, negativos_t.April_8, negativos_t.April_9, negativos_t.April_10, negativos_t.April_11, negativos_t.April_12, negativos_t.April_13, negativos_t.April_14, negativos_t.April_15, negativos_t.April_16, negativos_t.April_17, negativos_t.April_18, negativos_t.April_19, negativos_t.April_20, negativos_t.April_21, negativos_t.April_22).all()
        
    session.close()
            
    # Create a dictionary
            
    negativos_all = []
    for row_number, fips, estado, pais, status, Lat, Long, January_22, January_23, January_24, January_25, January_26, January_27, January_28, January_29, January_30, January_31, Feburary_1, Feburary_2, Feburary_3, Feburary_4, Feburary_5, Feburary_6, Feburary_7, Feburary_8, Feburary_9, Feburary_10, Feburary_11, Feburary_12, Feburary_13, Feburary_14, Feburary_15, Feburary_16, Feburary_17, Feburary_18, Feburary_19, Feburary_20, Feburary_21, Feburary_22, Feburary_23, Feburary_24, Feburary_25, Feburary_26, Feburary_27, Feburary_28, Feburary_29, March_1, March_2, March_3, March_4, March_5, March_6, March_7, March_8, March_9, March_10, March_11, March_12, March_13, March_14, March_15, March_16, March_17, March_18, March_19, March_20, March_21, March_22, March_23, March_24, March_25, March_26, March_27, March_28, March_29, March_30, March_31, April_1, April_2, April_3, April_4, April_5, April_6, April_7, April_8, April_9, April_10, April_11, April_12, April_13, April_14, April_15, April_16, April_17, April_18, April_19, April_20, April_21, April_22, in negativos_final:
        negativos_d = {}
        negativos_d["row_number"] = row_number
        negativos_d["fips"] = fips
        negativos_d["estado"] = estado
        negativos_d["pais"] = pais
        negativos_d["status"] = status
        negativos_d["Lat"] = Lat
        negativos_d["Long"] = Long
        negativos_d['January_22']=January_22
        negativos_d['January_23']=January_23
        negativos_d['January_24']=January_24
        negativos_d['January_25']=January_25
        negativos_d['January_26']=January_26
        negativos_d['January_27']=January_27
        negativos_d['January_28']=January_28
        negativos_d['January_29']=January_29
        negativos_d['January_30']=January_30
        negativos_d['January_31']=January_31
        negativos_d['Feburary_1']=Feburary_1
        negativos_d['Feburary_2']=Feburary_2
        negativos_d['Feburary_3']=Feburary_3
        negativos_d['Feburary_4']=Feburary_4
        negativos_d['Feburary_5']=Feburary_5
        negativos_d['Feburary_6']=Feburary_6
        negativos_d['Feburary_7']=Feburary_7
        negativos_d['Feburary_8']=Feburary_8
        negativos_d['Feburary_9']=Feburary_9
        negativos_d['Feburary_10']=Feburary_10
        negativos_d['Feburary_11']=Feburary_11
        negativos_d['Feburary_12']=Feburary_12
        negativos_d['Feburary_13']=Feburary_13
        negativos_d['Feburary_14']=Feburary_14
        negativos_d['Feburary_15']=Feburary_15
        negativos_d['Feburary_16']=Feburary_16
        negativos_d['Feburary_17']=Feburary_17
        negativos_d['Feburary_18']=Feburary_18
        negativos_d['Feburary_19']=Feburary_19
        negativos_d['Feburary_20']=Feburary_20
        negativos_d['Feburary_21']=Feburary_21
        negativos_d['Feburary_22']=Feburary_22
        negativos_d['Feburary_23']=Feburary_23
        negativos_d['Feburary_24']=Feburary_24
        negativos_d['Feburary_25']=Feburary_25
        negativos_d['Feburary_26']=Feburary_26
        negativos_d['Feburary_27']=Feburary_27
        negativos_d['Feburary_28']=Feburary_28
        negativos_d['Feburary_29']=Feburary_29
        negativos_d['March_1']=March_1
        negativos_d['March_2']=March_2
        negativos_d['March_3']=March_3
        negativos_d['March_4']=March_4
        negativos_d['March_5']=March_5
        negativos_d['March_6']=March_6
        negativos_d['March_7']=March_7
        negativos_d['March_8']=March_8
        negativos_d['March_9']=March_9
        negativos_d['March_10']=March_10
        negativos_d['March_11']=March_11
        negativos_d['March_12']=March_12
        negativos_d['March_13']=March_13
        negativos_d['March_14']=March_14
        negativos_d['March_15']=March_15
        negativos_d['March_16']=March_16
        negativos_d['March_17']=March_17
        negativos_d['March_18']=March_18
        negativos_d['March_19']=March_19
        negativos_d['March_20']=March_20
        negativos_d['March_21']=March_21
        negativos_d['March_22']=March_22
        negativos_d['March_23']=March_23
        negativos_d['March_24']=March_24
        negativos_d['March_25']=March_25
        negativos_d['March_26']=March_26
        negativos_d['March_27']=March_27
        negativos_d['March_28']=March_28
        negativos_d['March_29']=March_29
        negativos_d['March_30']=March_30
        negativos_d['March_31']=March_31
        negativos_d['April_1']=April_1
        negativos_d['April_2']=April_2
        negativos_d['April_3']=April_3
        negativos_d['April_4']=April_4
        negativos_d['April_5']=April_5
        negativos_d['April_6']=April_6
        negativos_d['April_7']=April_7
        negativos_d['April_8']=April_8
        negativos_d['April_9']=April_9
        negativos_d['April_10']=April_10
        negativos_d['April_11']=April_11
        negativos_d['April_12']=April_12
        negativos_d['April_13']=April_13
        negativos_d['April_14']=April_14
        negativos_d['April_15']=April_15
        negativos_d['April_16']=April_16
        negativos_d['April_17']=April_17
        negativos_d['April_18']=April_18
        negativos_d['April_19']=April_19
        negativos_d['April_20']=April_20
        negativos_d['April_21']=April_21
        negativos_d['April_22']=April_22

        negativos_all.append(negativos_d)
                
    return jsonify(negativos_all)  

@app.route("/project2/data/nacional")
def nacional_data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    nacional_final= session.query(nacional_t.row_number,nacional_t.fips,nacional_t.estado, nacional_t.pais, nacional_t.status, nacional_t.Lat, nacional_t.Long, nacional_t.January_22, nacional_t.January_23, nacional_t.January_24, nacional_t.January_25, nacional_t.January_26, nacional_t.January_27, nacional_t.January_28, nacional_t.January_29, nacional_t.January_30, nacional_t.January_31, nacional_t.Feburary_1, nacional_t.Feburary_2, nacional_t.Feburary_3, nacional_t.Feburary_4, nacional_t.Feburary_5, nacional_t.Feburary_6, nacional_t.Feburary_7, nacional_t.Feburary_8, nacional_t.Feburary_9, nacional_t.Feburary_10, nacional_t.Feburary_11, nacional_t.Feburary_12, nacional_t.Feburary_13, nacional_t.Feburary_14, nacional_t.Feburary_15, nacional_t.Feburary_16, nacional_t.Feburary_17, nacional_t.Feburary_18, nacional_t.Feburary_19, nacional_t.Feburary_20, nacional_t.Feburary_21, nacional_t.Feburary_22, nacional_t.Feburary_23, nacional_t.Feburary_24, nacional_t.Feburary_25, nacional_t.Feburary_26, nacional_t.Feburary_27, nacional_t.Feburary_28, nacional_t.Feburary_29, nacional_t.March_1, nacional_t.March_2, nacional_t.March_3,nacional_t.March_4, nacional_t.March_5, nacional_t.March_6, nacional_t.March_7, nacional_t.March_8, nacional_t.March_9, nacional_t.March_10, nacional_t.March_11, nacional_t.March_12, nacional_t.March_13, nacional_t.March_14, nacional_t.March_15, nacional_t.March_16, nacional_t.March_17, nacional_t.March_18, nacional_t.March_19, nacional_t.March_20, nacional_t.March_21, nacional_t.March_22, nacional_t.March_23, nacional_t.March_24, nacional_t.March_25, nacional_t.March_26, nacional_t.March_27, nacional_t.March_28, nacional_t.March_29, nacional_t.March_30, nacional_t.March_31, nacional_t.April_1, nacional_t.April_2, nacional_t.April_3, nacional_t.April_4, nacional_t.April_5, nacional_t.April_6, nacional_t.April_7, nacional_t.April_8, nacional_t.April_9, nacional_t.April_10, nacional_t.April_11, nacional_t.April_12, nacional_t.April_13, nacional_t.April_14, nacional_t.April_15, nacional_t.April_16, nacional_t.April_17, nacional_t.April_18, nacional_t.April_19, nacional_t.April_20, nacional_t.April_21, nacional_t.April_22).all()
        
    session.close()
            
    # Create a dictionary
            
    nacional_all = []
    for row_number, fips, estado, pais, status, Lat, Long, January_22, January_23, January_24, January_25, January_26, January_27, January_28, January_29, January_30, January_31, Feburary_1, Feburary_2, Feburary_3, Feburary_4, Feburary_5, Feburary_6, Feburary_7, Feburary_8, Feburary_9, Feburary_10, Feburary_11, Feburary_12, Feburary_13, Feburary_14, Feburary_15, Feburary_16, Feburary_17, Feburary_18, Feburary_19, Feburary_20, Feburary_21, Feburary_22, Feburary_23, Feburary_24, Feburary_25, Feburary_26, Feburary_27, Feburary_28, Feburary_29, March_1, March_2, March_3, March_4, March_5, March_6, March_7, March_8, March_9, March_10, March_11, March_12, March_13, March_14, March_15, March_16, March_17, March_18, March_19, March_20, March_21, March_22, March_23, March_24, March_25, March_26, March_27, March_28, March_29, March_30, March_31, April_1, April_2, April_3, April_4, April_5, April_6, April_7, April_8, April_9, April_10, April_11, April_12, April_13, April_14, April_15, April_16, April_17, April_18, April_19, April_20, April_21, April_22, in nacional_final:
        nacional_d = {}
        nacional_d["row_number"] = row_number
        nacional_d["fips"] = fips
        nacional_d["estado"] = estado
        nacional_d["pais"] = pais
        nacional_d["status"] = status
        nacional_d["Lat"] = Lat
        nacional_d["Long"] = Long
        nacional_d['January_22']=January_22
        nacional_d['January_23']=January_23
        nacional_d['January_24']=January_24
        nacional_d['January_25']=January_25
        nacional_d['January_26']=January_26
        nacional_d['January_27']=January_27
        nacional_d['January_28']=January_28
        nacional_d['January_29']=January_29
        nacional_d['January_30']=January_30
        nacional_d['January_31']=January_31
        nacional_d['Feburary_1']=Feburary_1
        nacional_d['Feburary_2']=Feburary_2
        nacional_d['Feburary_3']=Feburary_3
        nacional_d['Feburary_4']=Feburary_4
        nacional_d['Feburary_5']=Feburary_5
        nacional_d['Feburary_6']=Feburary_6
        nacional_d['Feburary_7']=Feburary_7
        nacional_d['Feburary_8']=Feburary_8
        nacional_d['Feburary_9']=Feburary_9
        nacional_d['Feburary_10']=Feburary_10
        nacional_d['Feburary_11']=Feburary_11
        nacional_d['Feburary_12']=Feburary_12
        nacional_d['Feburary_13']=Feburary_13
        nacional_d['Feburary_14']=Feburary_14
        nacional_d['Feburary_15']=Feburary_15
        nacional_d['Feburary_16']=Feburary_16
        nacional_d['Feburary_17']=Feburary_17
        nacional_d['Feburary_18']=Feburary_18
        nacional_d['Feburary_19']=Feburary_19
        nacional_d['Feburary_20']=Feburary_20
        nacional_d['Feburary_21']=Feburary_21
        nacional_d['Feburary_22']=Feburary_22
        nacional_d['Feburary_23']=Feburary_23
        nacional_d['Feburary_24']=Feburary_24
        nacional_d['Feburary_25']=Feburary_25
        nacional_d['Feburary_26']=Feburary_26
        nacional_d['Feburary_27']=Feburary_27
        nacional_d['Feburary_28']=Feburary_28
        nacional_d['Feburary_29']=Feburary_29
        nacional_d['March_1']=March_1
        nacional_d['March_2']=March_2
        nacional_d['March_3']=March_3
        nacional_d['March_4']=March_4
        nacional_d['March_5']=March_5
        nacional_d['March_6']=March_6
        nacional_d['March_7']=March_7
        nacional_d['March_8']=March_8
        nacional_d['March_9']=March_9
        nacional_d['March_10']=March_10
        nacional_d['March_11']=March_11
        nacional_d['March_12']=March_12
        nacional_d['March_13']=March_13
        nacional_d['March_14']=March_14
        nacional_d['March_15']=March_15
        nacional_d['March_16']=March_16
        nacional_d['March_17']=March_17
        nacional_d['March_18']=March_18
        nacional_d['March_19']=March_19
        nacional_d['March_20']=March_20
        nacional_d['March_21']=March_21
        nacional_d['March_22']=March_22
        nacional_d['March_23']=March_23
        nacional_d['March_24']=March_24
        nacional_d['March_25']=March_25
        nacional_d['March_26']=March_26
        nacional_d['March_27']=March_27
        nacional_d['March_28']=March_28
        nacional_d['March_29']=March_29
        nacional_d['March_30']=March_30
        nacional_d['March_31']=March_31
        nacional_d['April_1']=April_1
        nacional_d['April_2']=April_2
        nacional_d['April_3']=April_3
        nacional_d['April_4']=April_4
        nacional_d['April_5']=April_5
        nacional_d['April_6']=April_6
        nacional_d['April_7']=April_7
        nacional_d['April_8']=April_8
        nacional_d['April_9']=April_9
        nacional_d['April_10']=April_10
        nacional_d['April_11']=April_11
        nacional_d['April_12']=April_12
        nacional_d['April_13']=April_13
        nacional_d['April_14']=April_14
        nacional_d['April_15']=April_15
        nacional_d['April_16']=April_16
        nacional_d['April_17']=April_17
        nacional_d['April_18']=April_18
        nacional_d['April_19']=April_19
        nacional_d['April_20']=April_20
        nacional_d['April_21']=April_21
        nacional_d['April_22']=April_22

        nacional_all.append(nacional_d)
                
    return jsonify(nacional_all)

@app.route("/project2/data/estados")
def estados_data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    estados_final= session.query(estados_t.row_number,estados_t.fips,estados_t.estado, estados_t.pais, estados_t.status, estados_t.Lat, estados_t.Long, estados_t.January_22, estados_t.January_23, estados_t.January_24, estados_t.January_25, estados_t.January_26, estados_t.January_27, estados_t.January_28, estados_t.January_29, estados_t.January_30, estados_t.January_31, estados_t.Feburary_1, estados_t.Feburary_2, estados_t.Feburary_3, estados_t.Feburary_4, estados_t.Feburary_5, estados_t.Feburary_6, estados_t.Feburary_7, estados_t.Feburary_8, estados_t.Feburary_9, estados_t.Feburary_10, estados_t.Feburary_11, estados_t.Feburary_12, estados_t.Feburary_13, estados_t.Feburary_14, estados_t.Feburary_15, estados_t.Feburary_16, estados_t.Feburary_17, estados_t.Feburary_18, estados_t.Feburary_19, estados_t.Feburary_20, estados_t.Feburary_21, estados_t.Feburary_22, estados_t.Feburary_23, estados_t.Feburary_24, estados_t.Feburary_25, estados_t.Feburary_26, estados_t.Feburary_27, estados_t.Feburary_28, estados_t.Feburary_29, estados_t.March_1, estados_t.March_2, estados_t.March_3,estados_t.March_4, estados_t.March_5, estados_t.March_6, estados_t.March_7, estados_t.March_8, estados_t.March_9, estados_t.March_10, estados_t.March_11, estados_t.March_12, estados_t.March_13, estados_t.March_14, estados_t.March_15, estados_t.March_16, estados_t.March_17, estados_t.March_18, estados_t.March_19, estados_t.March_20, estados_t.March_21, estados_t.March_22, estados_t.March_23, estados_t.March_24, estados_t.March_25, estados_t.March_26, estados_t.March_27, estados_t.March_28, estados_t.March_29, estados_t.March_30, estados_t.March_31, estados_t.April_1, estados_t.April_2, estados_t.April_3, estados_t.April_4, estados_t.April_5, estados_t.April_6, estados_t.April_7, estados_t.April_8, estados_t.April_9, estados_t.April_10, estados_t.April_11, estados_t.April_12, estados_t.April_13, estados_t.April_14, estados_t.April_15, estados_t.April_16, estados_t.April_17, estados_t.April_18, estados_t.April_19, estados_t.April_20, estados_t.April_21, estados_t.April_22).all()
        
    session.close()
            
    # Create a dictionary
            
    estados_all = []
    for row_number, fips, estado, pais, status, Lat, Long, January_22, January_23, January_24, January_25, January_26, January_27, January_28, January_29, January_30, January_31, Feburary_1, Feburary_2, Feburary_3, Feburary_4, Feburary_5, Feburary_6, Feburary_7, Feburary_8, Feburary_9, Feburary_10, Feburary_11, Feburary_12, Feburary_13, Feburary_14, Feburary_15, Feburary_16, Feburary_17, Feburary_18, Feburary_19, Feburary_20, Feburary_21, Feburary_22, Feburary_23, Feburary_24, Feburary_25, Feburary_26, Feburary_27, Feburary_28, Feburary_29, March_1, March_2, March_3, March_4, March_5, March_6, March_7, March_8, March_9, March_10, March_11, March_12, March_13, March_14, March_15, March_16, March_17, March_18, March_19, March_20, March_21, March_22, March_23, March_24, March_25, March_26, March_27, March_28, March_29, March_30, March_31, April_1, April_2, April_3, April_4, April_5, April_6, April_7, April_8, April_9, April_10, April_11, April_12, April_13, April_14, April_15, April_16, April_17, April_18, April_19, April_20, April_21, April_22, in estados_final:
        estados_d = {}
        estados_d["row_number"] = row_number
        estados_d["fips"] = fips
        estados_d["estado"] = estado
        estados_d["pais"] = pais
        estados_d["status"] = status
        estados_d["Lat"] = Lat
        estados_d["Long"] = Long
        estados_d['January_22']=January_22
        estados_d['January_23']=January_23
        estados_d['January_24']=January_24
        estados_d['January_25']=January_25
        estados_d['January_26']=January_26
        estados_d['January_27']=January_27
        estados_d['January_28']=January_28
        estados_d['January_29']=January_29
        estados_d['January_30']=January_30
        estados_d['January_31']=January_31
        estados_d['Feburary_1']=Feburary_1
        estados_d['Feburary_2']=Feburary_2
        estados_d['Feburary_3']=Feburary_3
        estados_d['Feburary_4']=Feburary_4
        estados_d['Feburary_5']=Feburary_5
        estados_d['Feburary_6']=Feburary_6
        estados_d['Feburary_7']=Feburary_7
        estados_d['Feburary_8']=Feburary_8
        estados_d['Feburary_9']=Feburary_9
        estados_d['Feburary_10']=Feburary_10
        estados_d['Feburary_11']=Feburary_11
        estados_d['Feburary_12']=Feburary_12
        estados_d['Feburary_13']=Feburary_13
        estados_d['Feburary_14']=Feburary_14
        estados_d['Feburary_15']=Feburary_15
        estados_d['Feburary_16']=Feburary_16
        estados_d['Feburary_17']=Feburary_17
        estados_d['Feburary_18']=Feburary_18
        estados_d['Feburary_19']=Feburary_19
        estados_d['Feburary_20']=Feburary_20
        estados_d['Feburary_21']=Feburary_21
        estados_d['Feburary_22']=Feburary_22
        estados_d['Feburary_23']=Feburary_23
        estados_d['Feburary_24']=Feburary_24
        estados_d['Feburary_25']=Feburary_25
        estados_d['Feburary_26']=Feburary_26
        estados_d['Feburary_27']=Feburary_27
        estados_d['Feburary_28']=Feburary_28
        estados_d['Feburary_29']=Feburary_29
        estados_d['March_1']=March_1
        estados_d['March_2']=March_2
        estados_d['March_3']=March_3
        estados_d['March_4']=March_4
        estados_d['March_5']=March_5
        estados_d['March_6']=March_6
        estados_d['March_7']=March_7
        estados_d['March_8']=March_8
        estados_d['March_9']=March_9
        estados_d['March_10']=March_10
        estados_d['March_11']=March_11
        estados_d['March_12']=March_12
        estados_d['March_13']=March_13
        estados_d['March_14']=March_14
        estados_d['March_15']=March_15
        estados_d['March_16']=March_16
        estados_d['March_17']=March_17
        estados_d['March_18']=March_18
        estados_d['March_19']=March_19
        estados_d['March_20']=March_20
        estados_d['March_21']=March_21
        estados_d['March_22']=March_22
        estados_d['March_23']=March_23
        estados_d['March_24']=March_24
        estados_d['March_25']=March_25
        estados_d['March_26']=March_26
        estados_d['March_27']=March_27
        estados_d['March_28']=March_28
        estados_d['March_29']=March_29
        estados_d['March_30']=March_30
        estados_d['March_31']=March_31
        estados_d['April_1']=April_1
        estados_d['April_2']=April_2
        estados_d['April_3']=April_3
        estados_d['April_4']=April_4
        estados_d['April_5']=April_5
        estados_d['April_6']=April_6
        estados_d['April_7']=April_7
        estados_d['April_8']=April_8
        estados_d['April_9']=April_9
        estados_d['April_10']=April_10
        estados_d['April_11']=April_11
        estados_d['April_12']=April_12
        estados_d['April_13']=April_13
        estados_d['April_14']=April_14
        estados_d['April_15']=April_15
        estados_d['April_16']=April_16
        estados_d['April_17']=April_17
        estados_d['April_18']=April_18
        estados_d['April_19']=April_19
        estados_d['April_20']=April_20
        estados_d['April_21']=April_21
        estados_d['April_22']=April_22

        estados_all.append(estados_d)
                
    return jsonify(estados_all)  

if __name__ == '__main__':
    app.run()
