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
cities_grouped_t = Base.classes.cities_grouped_reset
status_grouped_t = Base.classes.status_grouped


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
        f"/project2/data/cities<br/>"
        f"/project2/data/status<br/>"
    )
@app.route("/project2/data/status")
def status_data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all recovered data"""
    # Query all table
    status_final= session.query(status_grouped_t.identifier,status_grouped_t.confirmed,status_grouped_t.death,status_grouped_t.recovered).all()
 
    session.close()
    
    # Create a dictionary
    
    status_all = []
    for identifier, confirmed, death, recovered in status_final:
        status_d = {}
        status_d["identifier"] = identifier
        status_d["confirmed"]= confirmed
        status_d["death"] = death
        status_d["recovered"] = recovered
        status_all.append(status_d)

    return jsonify(status_all)


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
    all_countries_final= session.query(all_countries_t.rownumber,all_countries_t.fips,all_countries_t.estado, all_countries_t.pais, all_countries_t.status, all_countries_t.Lat, all_countries_t.Long, all_countries_t.January22, all_countries_t.January23, all_countries_t.January24, all_countries_t.January25, all_countries_t.January26, all_countries_t.January27, all_countries_t.January28, all_countries_t.January29, all_countries_t.January30, all_countries_t.January31, all_countries_t.Feburary1, all_countries_t.Feburary2, all_countries_t.Feburary3, all_countries_t.Feburary4, all_countries_t.Feburary5, all_countries_t.Feburary6, all_countries_t.Feburary7, all_countries_t.Feburary8, all_countries_t.Feburary9, all_countries_t.Feburary10, all_countries_t.Feburary11, all_countries_t.Feburary12, all_countries_t.Feburary13, all_countries_t.Feburary14, all_countries_t.Feburary15, all_countries_t.Feburary16, all_countries_t.Feburary17, all_countries_t.Feburary18, all_countries_t.Feburary19, all_countries_t.Feburary20, all_countries_t.Feburary21, all_countries_t.Feburary22, all_countries_t.Feburary23, all_countries_t.Feburary24, all_countries_t.Feburary25, all_countries_t.Feburary26, all_countries_t.Feburary27, all_countries_t.Feburary28, all_countries_t.Feburary29, all_countries_t.March1, all_countries_t.March2, all_countries_t.March3,all_countries_t.March4, all_countries_t.March5, all_countries_t.March6, all_countries_t.March7, all_countries_t.March8, all_countries_t.March9, all_countries_t.March10, all_countries_t.March11, all_countries_t.March12, all_countries_t.March13, all_countries_t.March14, all_countries_t.March15, all_countries_t.March16, all_countries_t.March17, all_countries_t.March18, all_countries_t.March19, all_countries_t.March20, all_countries_t.March21, all_countries_t.March22, all_countries_t.March23, all_countries_t.March24, all_countries_t.March25, all_countries_t.March26, all_countries_t.March27, all_countries_t.March28, all_countries_t.March29, all_countries_t.March30, all_countries_t.March31, all_countries_t.April1, all_countries_t.April2, all_countries_t.April3, all_countries_t.April4, all_countries_t.April5, all_countries_t.April6, all_countries_t.April7, all_countries_t.April8, all_countries_t.April9, all_countries_t.April10, all_countries_t.April11, all_countries_t.April12, all_countries_t.April13, all_countries_t.April14, all_countries_t.April15, all_countries_t.April16, all_countries_t.April17, all_countries_t.April18, all_countries_t.April19, all_countries_t.April20, all_countries_t.April21, all_countries_t.April22).all()
        
    session.close()
            
    # Create a dictionary
            
    all_countries_all = []
    for rownumber, fips, estado, pais, status, Lat, Long, January22, January23, January24, January25, January26, January27, January28, January29, January30, January31, Feburary1, Feburary2, Feburary3, Feburary4, Feburary5, Feburary6, Feburary7, Feburary8, Feburary9, Feburary10, Feburary11, Feburary12, Feburary13, Feburary14, Feburary15, Feburary16, Feburary17, Feburary18, Feburary19, Feburary20, Feburary21, Feburary22, Feburary23, Feburary24, Feburary25, Feburary26, Feburary27, Feburary28, Feburary29, March1, March2, March3, March4, March5, March6, March7, March8, March9, March10, March11, March12, March13, March14, March15, March16, March17, March18, March19, March20, March21, March22, March23, March24, March25, March26, March27, March28, March29, March30, March31, April1, April2, April3, April4, April5, April6, April7, April8, April9, April10, April11, April12, April13, April14, April15, April16, April17, April18, April19, April20, April21, April22 in all_countries_final:
        all_countries_d = {}
        all_countries_d["row_number"] = rownumber
        all_countries_d["fips"] = fips
        all_countries_d["estado"] = estado
        all_countries_d["pais"] = pais
        all_countries_d["status"] = status
        all_countries_d["Lat"] = Lat
        all_countries_d["Long"] = Long
        all_countries_d["January22"]=January22
        all_countries_d["January23"]=January23
        all_countries_d["January24"]=January24
        all_countries_d["January25"]=January25
        all_countries_d["January26"]=January26
        all_countries_d["January27"]=January27
        all_countries_d["January28"]=January28
        all_countries_d["January29"]=January29
        all_countries_d["January30"]=January30
        all_countries_d["January31"]=January31
        all_countries_d["Feburary1"]=Feburary1
        all_countries_d["Feburary2"]=Feburary2
        all_countries_d["Feburary3"]=Feburary3
        all_countries_d["Feburary4"]=Feburary4
        all_countries_d["Feburary5"]=Feburary5
        all_countries_d["Feburary6"]=Feburary6
        all_countries_d["Feburary7"]=Feburary7
        all_countries_d["Feburary8"]=Feburary8
        all_countries_d["Feburary9"]=Feburary9
        all_countries_d["Feburary10"]=Feburary10
        all_countries_d["Feburary11"]=Feburary11
        all_countries_d["Feburary12"]=Feburary12
        all_countries_d["Feburary13"]=Feburary13
        all_countries_d["Feburary14"]=Feburary14
        all_countries_d["Feburary15"]=Feburary15
        all_countries_d["Feburary16"]=Feburary16
        all_countries_d["Feburary17"]=Feburary17
        all_countries_d["Feburary18"]=Feburary18
        all_countries_d["Feburary19"]=Feburary19
        all_countries_d["Feburary20"]=Feburary20
        all_countries_d["Feburary21"]=Feburary21
        all_countries_d["Feburary22"]=Feburary22
        all_countries_d["Feburary23"]=Feburary23
        all_countries_d["Feburary24"]=Feburary24
        all_countries_d["Feburary25"]=Feburary25
        all_countries_d["Feburary26"]=Feburary26
        all_countries_d["Feburary27"]=Feburary27
        all_countries_d["Feburary28"]=Feburary28
        all_countries_d["Feburary29"]=Feburary29
        all_countries_d["March1"]=March1
        all_countries_d["March2"]=March2
        all_countries_d["March3"]=March3
        all_countries_d["March4"]=March4
        all_countries_d["March5"]=March5
        all_countries_d["March6"]=March6
        all_countries_d["March7"]=March7
        all_countries_d["March8"]=March8
        all_countries_d["March9"]=March9
        all_countries_d["March10"]=March10
        all_countries_d["March11"]=March11
        all_countries_d["March12"]=March12
        all_countries_d["March13"]=March13
        all_countries_d["March14"]=March14
        all_countries_d["March15"]=March15
        all_countries_d["March16"]=March16
        all_countries_d["March17"]=March17
        all_countries_d["March18"]=March18
        all_countries_d["March19"]=March19
        all_countries_d["March20"]=March20
        all_countries_d["March21"]=March21
        all_countries_d["March22"]=March22
        all_countries_d["March23"]=March23
        all_countries_d["March24"]=March24
        all_countries_d["March25"]=March25
        all_countries_d["March26"]=March26
        all_countries_d["March27"]=March27
        all_countries_d["March28"]=March28
        all_countries_d["March29"]=March29
        all_countries_d["March30"]=March30
        all_countries_d["March31"]=March31
        all_countries_d["April1"]=April1
        all_countries_d["April2"]=April2
        all_countries_d["April3"]=April3
        all_countries_d["April4"]=April4
        all_countries_d["April5"]=April5
        all_countries_d["April6"]=April6
        all_countries_d["April7"]=April7
        all_countries_d["April8"]=April8
        all_countries_d["April9"]=April9
        all_countries_d["April10"]=April10
        all_countries_d["April11"]=April11
        all_countries_d["April12"]=April12
        all_countries_d["April13"]=April13
        all_countries_d["April14"]=April14
        all_countries_d["April15"]=April15
        all_countries_d["April16"]=April16
        all_countries_d["April17"]=April17
        all_countries_d["April18"]=April18
        all_countries_d["April19"]=April19
        all_countries_d["April20"]=April20
        all_countries_d["April21"]=April21
        all_countries_d["April22"]=April22

        

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

@app.route("/project2/data/cities")
def cities_data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    cities_grouped_final= session.query(cities_grouped_t.rownumber, cities_grouped_t.pais, cities_grouped_t.status, cities_grouped_t.January22, cities_grouped_t.January23, cities_grouped_t.January24, cities_grouped_t.January25, cities_grouped_t.January26, cities_grouped_t.January27, cities_grouped_t.January28, cities_grouped_t.January29, cities_grouped_t.January30, cities_grouped_t.January31, cities_grouped_t.Feburary1, cities_grouped_t.Feburary2, cities_grouped_t.Feburary3, cities_grouped_t.Feburary4, cities_grouped_t.Feburary5, cities_grouped_t.Feburary6, cities_grouped_t.Feburary7, cities_grouped_t.Feburary8, cities_grouped_t.Feburary9, cities_grouped_t.Feburary10, cities_grouped_t.Feburary11, cities_grouped_t.Feburary12, cities_grouped_t.Feburary13, cities_grouped_t.Feburary14, cities_grouped_t.Feburary15, cities_grouped_t.Feburary16, cities_grouped_t.Feburary17, cities_grouped_t.Feburary18, cities_grouped_t.Feburary19, cities_grouped_t.Feburary20, cities_grouped_t.Feburary21, cities_grouped_t.Feburary22, cities_grouped_t.Feburary23, cities_grouped_t.Feburary24, cities_grouped_t.Feburary25, cities_grouped_t.Feburary26, cities_grouped_t.Feburary27, cities_grouped_t.Feburary28, cities_grouped_t.Feburary29, cities_grouped_t.March1, cities_grouped_t.March2, cities_grouped_t.March3,cities_grouped_t.March4, cities_grouped_t.March5, cities_grouped_t.March6, cities_grouped_t.March7, cities_grouped_t.March8, cities_grouped_t.March9, cities_grouped_t.March10, cities_grouped_t.March11, cities_grouped_t.March12, cities_grouped_t.March13, cities_grouped_t.March14, cities_grouped_t.March15, cities_grouped_t.March16, cities_grouped_t.March17, cities_grouped_t.March18, cities_grouped_t.March19, cities_grouped_t.March20, cities_grouped_t.March21, cities_grouped_t.March22, cities_grouped_t.March23, cities_grouped_t.March24, cities_grouped_t.March25, cities_grouped_t.March26, cities_grouped_t.March27, cities_grouped_t.March28, cities_grouped_t.March29, cities_grouped_t.March30, cities_grouped_t.March31, cities_grouped_t.April1, cities_grouped_t.April2, cities_grouped_t.April3, cities_grouped_t.April4, cities_grouped_t.April5, cities_grouped_t.April6, cities_grouped_t.April7, cities_grouped_t.April8, cities_grouped_t.April9, cities_grouped_t.April10, cities_grouped_t.April11, cities_grouped_t.April12, cities_grouped_t.April13, cities_grouped_t.April14, cities_grouped_t.April15, cities_grouped_t.April16, cities_grouped_t.April17, cities_grouped_t.April18, cities_grouped_t.April19, cities_grouped_t.April20, cities_grouped_t.April21, cities_grouped_t.April22).all()
        
    session.close()
            
    # Create a dictionary
            
    cities_grouped_all = []
    for rownumber, pais, status, January22, January23, January24, January25, January26, January27, January28, January29, January30, January31, Feburary1, Feburary2, Feburary3, Feburary4, Feburary5, Feburary6, Feburary7, Feburary8, Feburary9, Feburary10, Feburary11, Feburary12, Feburary13, Feburary14, Feburary15, Feburary16, Feburary17, Feburary18, Feburary19, Feburary20, Feburary21, Feburary22, Feburary23, Feburary24, Feburary25, Feburary26, Feburary27, Feburary28, Feburary29, March1, March2, March3, March4, March5, March6, March7, March8, March9, March10, March11, March12, March13, March14, March15, March16, March17, March18, March19, March20, March21, March22, March23, March24, March25, March26, March27, March28, March29, March30, March31, April1, April2, April3, April4, April5, April6, April7, April8, April9, April10, April11, April12, April13, April14, April15, April16, April17, April18, April19, April20, April21, April22 in cities_grouped_final:
        cities_grouped_d = {}
        cities_grouped_d["row_number"] = rownumber
        cities_grouped_d["pais"] = pais
        cities_grouped_d["status"] = status
        cities_grouped_d["January22"]=January22
        cities_grouped_d["January23"]=January23
        cities_grouped_d["January24"]=January24
        cities_grouped_d["January25"]=January25
        cities_grouped_d["January26"]=January26
        cities_grouped_d["January27"]=January27
        cities_grouped_d["January28"]=January28
        cities_grouped_d["January29"]=January29
        cities_grouped_d["January30"]=January30
        cities_grouped_d["January31"]=January31
        cities_grouped_d["Feburary1"]=Feburary1
        cities_grouped_d["Feburary2"]=Feburary2
        cities_grouped_d["Feburary3"]=Feburary3
        cities_grouped_d["Feburary4"]=Feburary4
        cities_grouped_d["Feburary5"]=Feburary5
        cities_grouped_d["Feburary6"]=Feburary6
        cities_grouped_d["Feburary7"]=Feburary7
        cities_grouped_d["Feburary8"]=Feburary8
        cities_grouped_d["Feburary9"]=Feburary9
        cities_grouped_d["Feburary10"]=Feburary10
        cities_grouped_d["Feburary11"]=Feburary11
        cities_grouped_d["Feburary12"]=Feburary12
        cities_grouped_d["Feburary13"]=Feburary13
        cities_grouped_d["Feburary14"]=Feburary14
        cities_grouped_d["Feburary15"]=Feburary15
        cities_grouped_d["Feburary16"]=Feburary16
        cities_grouped_d["Feburary17"]=Feburary17
        cities_grouped_d["Feburary18"]=Feburary18
        cities_grouped_d["Feburary19"]=Feburary19
        cities_grouped_d["Feburary20"]=Feburary20
        cities_grouped_d["Feburary21"]=Feburary21
        cities_grouped_d["Feburary22"]=Feburary22
        cities_grouped_d["Feburary23"]=Feburary23
        cities_grouped_d["Feburary24"]=Feburary24
        cities_grouped_d["Feburary25"]=Feburary25
        cities_grouped_d["Feburary26"]=Feburary26
        cities_grouped_d["Feburary27"]=Feburary27
        cities_grouped_d["Feburary28"]=Feburary28
        cities_grouped_d["Feburary29"]=Feburary29
        cities_grouped_d["March1"]=March1
        cities_grouped_d["March2"]=March2
        cities_grouped_d["March3"]=March3
        cities_grouped_d["March4"]=March4
        cities_grouped_d["March5"]=March5
        cities_grouped_d["March6"]=March6
        cities_grouped_d["March7"]=March7
        cities_grouped_d["March8"]=March8
        cities_grouped_d["March9"]=March9
        cities_grouped_d["March10"]=March10
        cities_grouped_d["March11"]=March11
        cities_grouped_d["March12"]=March12
        cities_grouped_d["March13"]=March13
        cities_grouped_d["March14"]=March14
        cities_grouped_d["March15"]=March15
        cities_grouped_d["March16"]=March16
        cities_grouped_d["March17"]=March17
        cities_grouped_d["March18"]=March18
        cities_grouped_d["March19"]=March19
        cities_grouped_d["March20"]=March20
        cities_grouped_d["March21"]=March21
        cities_grouped_d["March22"]=March22
        cities_grouped_d["March23"]=March23
        cities_grouped_d["March24"]=March24
        cities_grouped_d["March25"]=March25
        cities_grouped_d["March26"]=March26
        cities_grouped_d["March27"]=March27
        cities_grouped_d["March28"]=March28
        cities_grouped_d["March29"]=March29
        cities_grouped_d["March30"]=March30
        cities_grouped_d["March31"]=March31
        cities_grouped_d["April1"]=April1
        cities_grouped_d["April2"]=April2
        cities_grouped_d["April3"]=April3
        cities_grouped_d["April4"]=April4
        cities_grouped_d["April5"]=April5
        cities_grouped_d["April6"]=April6
        cities_grouped_d["April7"]=April7
        cities_grouped_d["April8"]=April8
        cities_grouped_d["April9"]=April9
        cities_grouped_d["April10"]=April10
        cities_grouped_d["April11"]=April11
        cities_grouped_d["April12"]=April12
        cities_grouped_d["April13"]=April13
        cities_grouped_d["April14"]=April14
        cities_grouped_d["April15"]=April15
        cities_grouped_d["April16"]=April16
        cities_grouped_d["April17"]=April17
        cities_grouped_d["April18"]=April18
        cities_grouped_d["April19"]=April19
        cities_grouped_d["April20"]=April20
        cities_grouped_d["April21"]=April21
        cities_grouped_d["April22"]=April22

        cities_grouped_all.append(cities_grouped_d)
                
    return jsonify(cities_grouped_all)

if __name__ == '__main__':
    app.run()
