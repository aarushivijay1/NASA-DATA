from tkinter import *

class Asteroid:
    def __init__(self, id, name, size, velocity, distance, jpl_url):
        self.id = id
        self.name = name
        self.size = size
        self.velocity = velocity
        self.distance = distance
        self.jpl_url = jpl_url
    
    def ToList(self):
        return [self.id, self.name, self.size, self.velocity, self.distance, self.jpl_url]

    def __eq__(self, other):        
        try:
            if(isinstance(other, Asteroid) and self.ToList() == other.ToList()):
                return True
        except:
            raise ValueError("Type comparison with non-Asteroid object")
    def __repr__(self):
        raise NotImplementedError
    def __str__(self):
        try:
            return "ID: {}, Name: {}, Size: {} miles, Velocity: {} miles/hour, Close-approach distance: {} miles, nasa_jpl_url: {}".format(self.id, self.name, self.size, self.velocity, self.distance, self.jpl_url)
        except:
            raise ValueError("Type comparison with non-Asteroid object")

class Asteroid2:
    def __init__(self, name, close_approach_date, inital_relative_velocity, initial_miss_distance, latest_relative_velocity, latest_miss_distance, first_obeservation_date, last_observation_date):
        self.name = name
        self.close_approach_date = close_approach_date
        self.inital_relative_velocity = inital_relative_velocity
        self.initial_miss_distance = initial_miss_distance
        self.latest_relative_velocity = latest_relative_velocity
        self.latest_miss_distance = latest_miss_distance
        self.first_obeservation_date = first_obeservation_date
        self.last_observation_date = last_observation_date
    
    def ToList(self):
        return [self.name, self.close_approach_date, self.inital_relative_velocity, self.initial_miss_distance, self.latest_relative_velocity, self.latest_miss_distance, self.first_obeservation_date, self.last_observation_date]

    def __eq__(self, other):        
        try:
            if(isinstance(other, Asteroid2) and self.ToList() == other.ToList()):
                return True
        except:
            raise ValueError("Type comparison with non-Asteroid2 object")
    def __repr__(self):
        try:
            return "Name: {}, Close_approach_date: {}, Inital_relative_velocity: {} miles/hour, Initial_miss_distance: {} miles, Latest_relative_velocity: {} miles/hour, Latest_miss_distance: {} miles, First_obeservation_date: {}, Last_observation_date: {}".format(self.name, self.close_approach_date, self.inital_relative_velocity, self.initial_miss_distance, self.latest_relative_velocity, self.latest_miss_distance, self.first_obeservation_date, self.last_observation_date)
        except:
            raise ValueError("Type comparison with non-Asteroid2 object")
    def __str__(self):
        try:
            return "Name: {}, Close_approach_date: {}, Inital_relative_velocity: {} miles/hour, Initial_miss_distance: {} miles, Latest_relative_velocity: {} miles/hour, Latest_miss_distance: {} miles, First_obeservation_date: {}, Last_observation_date: {}".format(self.name, self.close_approach_date, self.inital_relative_velocity, self.initial_miss_distance, self.latest_relative_velocity, self.latest_miss_distance, self.first_obeservation_date, self.last_observation_date)
        except:
            raise ValueError("Type comparison with non-Asteroid2 object")