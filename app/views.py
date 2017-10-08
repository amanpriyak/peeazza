
# from flask import Flask
# from flask import jsonify
# from flask import request
# from flask import render_template
from flask import render_template, request
from app import app


bathrooms = [   {  "Title": "Cory Floor 1 Female",
                   "Building": "Cory",
                   "Floor": 1,
                   "Description": "Near room x",
                   "Coordinates": (37.875075, -122.257729),
                   "Type": "Female",
                   "Number of Stalls": 1,
                   "Number of Sinks": 1,
                   "Urinal": False,
                   "Tampon/Pad Dispenser": False,
                   "Water Fountain":False,
                   "Additional Tags": ["Spacious", "Large Mirror"],
                   "Comments": []},
               {   "Title": "Cory Floor 1 Male",
                   "Building": "Cory",
                   "Floor": 1,
                   "Description": "Near room x",
                    "Coordinates": (37.874961, -122.257693),
                    "Type": "Male",
                    "Number of Stalls": 8,
                    "Number of Sinks": 8,
                    "Urinal": True,
                    "Tampon/Pad Dispenser": False,
                    "Water Fountain":False,
                    "Additional Tags": ["Spacious"]},
                {   "Title": "MLK Floor 1",
                    "Building": "MLK",
                    "Floor": 1,
                    "Description": "Near Amazon Locker and Equator Coffee",
                     "Coordinates": (37.869129, -122.259598),
                     "Type": "Male",
                     "Number of Stalls": 5,
                     "Number of Sinks": 2,
                     "Urinal": True,
                     "Tampon/Pad Dispenser": False,
                     "Water Fountain":True,
                     "Additional Tags": ["Clean"]
                    },
                {   "Title": "MLK Floor 1",
                    "Building": "MLK",
                    "Floor": 1,
                    "Description": "Near Amazon Locker and Equator Coffee",
                     "Coordinates": (37.869129, -122.259598),
                     "Type": "Female",
                     "Number of Stalls": 4,
                     "Number of Sinks": 3,
                     "Urinal": False,
                     "Tampon/Pad Dispenser": False,
                     "Water Fountain":True,
                     "Additional Tags": []
                    },
                {   "Title": "MLK Basement",
                    "Building": "MLK",
                    "Floor": 0,
                    "Description": "By Cal Student Store and Bank of West",
                     "Coordinates": (37.869129, -122.259598),
                     "Type": "Female",
                     "Number of Stalls": 4,
                     "Number of Sinks": 3,
                     "Urinal": False,
                     "Tampon/Pad Dispenser": False,
                     "Water Fountain":False,
                     "Additional Tags": []
                    },
                {   "Title": "MLK Basement",
                    "Building": "MLK",
                    "Floor": 0,
                    "Description": "By Cal Student Store and Bank of West",
                     "Coordinates": (37.869129, -122.259598),
                     "Type": "Male",
                     "Number of Stalls": 4,
                     "Number of Sinks": 3,
                     "Urinal": True,
                     "Tampon/Pad Dispenser": False,
                     "Water Fountain":False,
                     "Additional Tags": []
                    },
                {   "Title": "Wheeler Basement",
                    "Building": "Wheeler",
                    "Floor": 0,
                    "Description": "On the left when you walk downstairs",
                     "Coordinates": (37.871159, -122.259284),
                     "Type": "Female",
                     "Number of Stalls": 5,
                     "Number of Sinks": 3,
                     "Urinal": True,
                     "Tampon/Pad Dispenser": False,
                     "Water Fountain":False,
                     "Additional Tags": ["large mirror", "spacious"]
                    },   
                {   "Title": "Wheeler Basement",
                    "Building": "Wheeler",
                    "Floor": 0,
                    "Description": "On the left when you walk downstairs",
                     "Coordinates": (37.871159, -122.259284),
                     "Type": "Male",
                     "Number of Stalls": 5,
                     "Number of Sinks": 3,
                     "Urinal": True,
                     "Tampon/Pad Dispenser": False,
                     "Water Fountain":False,
                     "Additional Tags": []
                    }
               ]





@app.route('/')
def index():
    print('hello')
    return render_template('index.html')

@app.route('/send', methods=["POST"])
def send():
    # if request.method == "POST":
    print('hi')
    gender = request.form['gender']
    water_f = request.form['water fountain']
    bathroom_match = []
    for item in bathrooms:
        if item["Type"] == gender:
            bathroom_match.append(item)
    matches = ""
    return render_template('map.html', matches = JSON.stringify(bathroom_match) )

#return render_template('index.html')
        #building = request.form['Building']
       # return jsonify("Hello World")
