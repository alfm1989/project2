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
rds_connection_string = "postgres:A1d2r3i4@localhost:5432/Project2"
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

    """Return a list of all passenger names"""
    # Query all passengers
    recovered_final= session.query(recovered_t.row_number,recovered_t.fips,recovered_t.estado, recovered_t.pais,                                recovered_t.status, recovered_t.Lat, recovered_t.Long, recovered_t.January_22, recovered_t.January_23, recovered_t.January_24, recovered_t.January_25, recovered_t.January_26, recovered_t.January_27, recovered_t.January_28, recovered_t.January_29, recovered_t.January_30, recovered_t.January_31, recovered_t.Feburary_1, recovered_t.Feburary_2, recovered_t.Feburary_3, recovered_t.Feburary_4, recovered_t.Feburary_5, recovered_t.Feburary_6, recovered_t.Feburary_7, recovered_t.Feburary_8, recovered_t.Feburary_9, recovered_t.Feburary_10, recovered_t.Feburary_11, recovered_t.Feburary_12, recovered_t.Feburary_13, recovered_t.Feburary_14, recovered_t.Feburary_15, recovered_t.Feburary_16, recovered_t.Feburary_17, recovered_t.Feburary_18, recovered_t.Feburary_19, recovered_t.Feburary_20, recovered_t.Feburary_21, recovered_t.Feburary_22, recovered_t.Feburary_23, recovered_t.Feburary_24, recovered_t.Feburary_25, recovered_t.Feburary_26, recovered_t.Feburary_27, recovered_t.Feburary_28, recovered_t.Feburary_29, recovered_t.March_1, recovered_t.March_2, recovered_t.March_3,recovered_t.March_4, recovered_t.March_5, recovered_t.March_6, recovered_t.March_7, recovered_t.March_8, recovered_t.March_9, recovered_t.March_10, recovered_t.March_11, recovered_t.March_12, recovered_t.March_13, recovered_t.March_14, recovered_t.March_15, recovered_t.March_16, recovered_t.March_17, recovered_t.March_18, recovered_t.March_19, recovered_t.March_20, recovered_t.March_21, recovered_t.March_22, recovered_t.March_23, recovered_t.March_24, recovered_t.March_25, recovered_t.March_26, recovered_t.March_27, recovered_t.March_28, recovered_t.March_29, recovered_t.March_30, recovered_t.March_31, recovered_t.April_1, recovered_t.April_2, recovered_t.April_3, recovered_t.April_4, recovered_t.April_5, recovered_t.April_6, recovered_t.April_7, recovered_t.April_8, recovered_t.April_9, recovered_t.April_10, recovered_t.April_11, recovered_t.April_12, recovered_t.April_13, recovered_t.April_14, recovered_t.April_15, recovered_t.April_16, recovered_t.April_17, recovered_t.April_18, recovered_t.April_19, recovered_t.April_20, recovered_t.April_21, recovered_t.April_22).all()
 
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


if __name__ == '__main__':
    app.run()
