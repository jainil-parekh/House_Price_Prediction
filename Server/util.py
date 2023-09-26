import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

#function that reurns estimated price given other values
def get_estimated_price(location,sqft,BHK,bath):
    # we are using try catch block beacuse if don't use it than it will throw error
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1


    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = BHK
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2) #it will take input for instance x and return the estimated price


def get_location_names():
    return __locations

def load_saved_artifacts(): #load saved artifacts columns.json and banglore hous prices
    print("loading saved artifacts...start")
    global __data_columns
    global __locations 
    
    with open("C:\\Users\\jpare\\BHP\\Server\\artifacts\\columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open("C:\\Users\\jpare\\BHP\\Server\\artifacts\\banglore_home_price_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location