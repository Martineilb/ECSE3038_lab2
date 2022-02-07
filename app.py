from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

global now
now = datetime.now()
FAKE_DATABASE = []

profile_object = {}
count = 0
print(now)


#CREATE -- POST FUNCTIONS
@app.route("/profile", methods=["POST"])
def post():

    global u
    global f
    global r

    u = request.json["Username"]
    f = request.json["Colour"]
    r = request.json["Role"]   

    global profile_object
    profile_object = {
        "Last Updated": now,
        "Username": u,
        "Role": r,
        "Colour": f
    }

    #FAKE_DATABASE.append(profile_object)
    #store.append(profile_object)
    return jsonify(profile_object)

#--------------TANK--------------------------

@app.route("/data", methods=["POST"])
def post_data():
    location = request.json["Tank Location"]
    percent = request.json["Percent Full"]
    latitude = request.json["Latitude"]
    longitude = request.json["Longitude"]
    global count
    count += 1

    global data_object
    data_object = {
        "id": count,
        "Tank Location": location,
        "Percent Full": percent,
        "Latitude": latitude,
        "Longitude": longitude
    }

    FAKE_DATABASE.append(data_object)
    return jsonify(data_object)


#READ --GET FUNCTIONS
@app.route("/profile", methods=["GET"])
def get_profile():

    return jsonify(FAKE_DATABASE)

#-----------TANK------------------
@app.route("/data", methods=["GET"])
def get_data():
    global data_object
    return jsonify(data_object)
    

#UPDATE -- PATCH FUNCTIONS
@app.route("/profile/<Username>/<Role>/<Colour>", methods=["PATCH"])
def patch_profile(Username, Role, Colour):
    global profile_object

    profile_object = arr
    arr = []  
    
    for u in arr:
        u["Username"] = request.json["Username"]
        
        for r in arr:
            r["Role"]=request.json["Role"]  
            
            for f in arr:
                f["Colour"] = request.json["Colour"]
            
                return jsonify(u, r, f)
                                

#-----------------TANK_-----------------    

@app.route("/data/<int:id>", methods=["PATCH"])
def patch_data(id):

    for location in FAKE_DATABASE:
        if location["id"] == id:
            location["Tank Location"] = request.json["Tank Location"]

    return jsonify(location)    


#DELETE
@app.route("/data/<int:id>", methods=["DELETE"])
def delete_data(id):
    for location in FAKE_DATABASE:
     if location["id"] == id:
        FAKE_DATABASE.remove(location)

        return f"user with ID {id} deleted"


if __name__ == '__main__':
    app.run(
        debug=True,
        port=3000,
        host="0.0.0.0"
    )