import json
import pickle
import numpy as np

locations = None
columns = None
model = None

def predict_price(loc, sqft, bhk, bath):
    try:
        loc_index = columns.index(loc.lower())
    except:
        loc_index = -1

    x = np.zeros(len(columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
        
    return round(model.predict([x])[0], 2)

def get_location_names():
    return locations

def load_saved_assets():

    print("Started loading assets...")

    global columns
    global locations
    global model

    with open('assets/columns.json', 'r') as f:
        columns = json.load(f)['data_columns']
        locations = columns[3:]

    with open('assets/final_model.pickle', 'rb') as f:
        model = pickle.load(f)

    print("Assets loaded successfully!")

if __name__ == "__main__":
    load_saved_assets()
    get_location_names()
    print(predict_price('Yelahanka', 1200, 2, 2))
    print(predict_price('HSR Layout', 1200, 2, 2))
    print(predict_price('Indira Nagar', 1200, 2, 2))
    print(predict_price('Kalhalli', 1200, 2, 2))
    print(predict_price('Ejipura', 1200, 2, 2))