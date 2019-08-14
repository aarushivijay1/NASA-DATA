#NASA Info will give you information about the asteroids from
#the NASA website. The dates you enter are in YYYY-MM-DD format 
#TRY ENTERING THE DATES IN THE SAME MONTH.
#and the API KEY that you can use is 'dqUjYcrOHWw1Xmlr47YlLCVSAGaQfX4vL9I06eqr'
#you can generate different asteroid informations and also 
#click on a button to open a different window

#BE PATIENT, GO AHEAD AND HAVE FUN! 

# CS 101 FINAL PROJECT


from Asteroid import Asteroid, Asteroid2 #importing the classes from user-defined object
from datetime import datetime 
import requests #importing requests 
import json
from tkinter import * #importing tkinter library 

#FIRST - making functions for different things 

def CheckDate(b): #validating the data format for the API
        try: 
                datetime.strptime(str(b), '%Y-%m-%d')
                return True
        except ValueError:
                return False

def CheckStartEnd(a,b): #function to make sure the start date is before the end date
        try:
                A = datetime.strptime(str(a), '%Y-%m-%d')
                B = datetime.strptime(str(b), '%Y-%m-%d')
                if (A.year - B.year > 0): #nested-if loop to compare year and month of the start date and end date
                        return False
                elif (A.year == B.year):
                        if (A.month - B.month > 0):
                                return False
                        elif (A.month == B.month):
                                if (A.day - B.day > 0):
                                        return False
                                else:
                                        return True
                        else:
                                return True
                else:
                        return True
        except ValueError: 
                return False

def GetData(asteroid2, window):   #function to create the basic GUI window
        AsteroidData = Toplevel(window) 
        AsteroidData.title('NASA INFO')
        AsteroidData.geometry('{}x{}'.format(400,400)) #defining the size of the window
        #creating labels for different operations on the screen
        Label(AsteroidData, text = "Name:").grid(row=0, column=0, sticky='nw')
        Label(AsteroidData, text = "Close_approach_date:").grid(row=1, column=0, sticky='nw')
        Label(AsteroidData, text = "Inital_relative_velocity (miles/h):").grid(row=2, column=0, sticky='nw')
        Label(AsteroidData, text = "Initial_miss_distance (miles):").grid(row=3, column=0, sticky='nw')
        Label(AsteroidData, text = "Latest_relative_velocity (miles/h):").grid(row=4, column=0, sticky='nw')
        Label(AsteroidData, text = "Latest_miss_distance (miles):").grid(row=5, column=0, sticky='nw')
        Label(AsteroidData, text = "First_obeservation_date:").grid(row=6, column=0, sticky='nw')
        Label(AsteroidData, text = "Last_observation_date:").grid(row=7, column=0, sticky='nw')
        Label(AsteroidData, text = asteroid2.name).grid(row=0, column=1, sticky='nw')
        Label(AsteroidData, text = asteroid2.close_approach_date).grid(row=1, column=1, sticky='nw')
        Label(AsteroidData, text = asteroid2.inital_relative_velocity).grid(row=2, column=1, sticky='nw')
        Label(AsteroidData, text = asteroid2.initial_miss_distance).grid(row=3, column=1, sticky='nw')
        Label(AsteroidData, text = asteroid2.latest_relative_velocity).grid(row=4, column=1, sticky='nw')
        Label(AsteroidData, text = asteroid2.latest_miss_distance).grid(row=5, column=1, sticky='nw')
        Label(AsteroidData, text = asteroid2.first_obeservation_date).grid(row=6, column=1, sticky='nw')
        Label(AsteroidData, text = asteroid2.last_observation_date).grid(row=7, column=1, sticky='nw')

def CheckFilter(asteroid, FilterKey): #function to perform simple search for the filter key
        FilterList=asteroid.ToList() 
        for i in FilterList:
                if str(i) == str(FilterKey):
                        return True
                else:
                        return False

def GetRequest(window, main_frame, Sdate, Edate, API, FilterKey):  #function to make the data from the API show up
        if CheckDate(Sdate) == CheckDate(Edate) == True:  #validating the dates inputted
                if CheckStartEnd(Sdate, Edate) == True:
                    #labels for the data that you need to show
                        Label(main_frame, text='ID', borderwidth=1, bg='Blue', fg= 'White' ,relief='solid').grid(row=0, column=1, sticky='nsew') 
                        Label(main_frame, text='Name', borderwidth=1, bg='Blue', fg= 'White', relief='solid').grid(row=0, column=2, sticky='nsew')
                        Label(main_frame, text='Size', borderwidth=1, bg='Blue', fg= 'White', relief='solid').grid(row=0, column=3, sticky='nsew')
                        Label(main_frame, text='Velocity', borderwidth=1, bg='Blue', fg= 'White', relief='solid').grid(row=0, column=4, sticky='nsew')
                        Label(main_frame, text='Distance', borderwidth=1,bg='Blue', fg= 'White', relief='solid').grid(row=0, column=5, sticky='nsew')
                        Label(main_frame, text='Jpl_url', borderwidth=1, bg='Blue', fg= 'White', relief='solid').grid(row=0, column=6, sticky='nsew')
                        RequestString = "https://api.nasa.gov/neo/rest/v1/feed?start_date=" + Sdate + "&end_date=" + Edate + "&api_key=" + API #creating a manipulative URL
                        response = requests.get(RequestString) #getting response from the api
                        json_data = response.json() 
                        asteroids_data = json_data.get('near_earth_objects')
                        results = [] 
                        for date in asteroids_data:  #appending the data in asteroid 
                                for asteroid in asteroids_data[date]:
                                        results.append(Asteroid(asteroid["id"], asteroid['name'], asteroid['estimated_diameter']['miles']['estimated_diameter_max'], asteroid['close_approach_data'][0]['relative_velocity']["miles_per_hour"], asteroid['close_approach_data'][0]['miss_distance']['miles'], asteroid['nasa_jpl_url']))
                        buttons=[]
                        results2=[]
                        printable_results=[]
                        for asteroid in results:
                                if ((CheckFilter(asteroid, FilterKey) == True) or (FilterKey=="")):
                                        printable_results.append(asteroid)
                                        a = printable_results.index(asteroid)+1
                                        b = asteroid.ToList()
                                        for i in b:
                                                Label(main_frame, text=i).grid(row=a, column=(b.index(i)+1))
                                        RequestString2 = "https://api.nasa.gov/neo/rest/v1/neo/" + asteroid.id + "?api_key=" + API
                                        response2 = requests.get(RequestString2)
                                        json_data2 = response2.json()
                                        try:
                                                asteroid2 = Asteroid2(json_data2["name"], json_data2["close_approach_data"][0]["close_approach_date"], json_data2["close_approach_data"][0]["relative_velocity"]["miles_per_hour"], json_data2["close_approach_data"][0]["miss_distance"]["miles"], json_data2["close_approach_data"][1]["relative_velocity"]["miles_per_hour"], json_data2["close_approach_data"][1]["miss_distance"]["miles"], json_data2["orbital_data"]["first_observation_date"], json_data2["orbital_data"]["last_observation_date"])
                                        except IndexError:
                                                asteroid2 = Asteroid2(json_data2["name"], json_data2["close_approach_data"][0]["close_approach_date"], json_data2["close_approach_data"][0]["relative_velocity"]["miles_per_hour"], json_data2["close_approach_data"][0]["miss_distance"]["miles"], 0, 0, json_data2["orbital_data"]["first_observation_date"], json_data2["orbital_data"]["last_observation_date"])
                                        results2.append(asteroid2)
                                for i in range(len(results2)):
                                        buttons.append(Button(main_frame, text="Click for More information", command=lambda i=i: GetData(results2[i], window)).grid(row=i+1, column=0, sticky='w'))
                else:
                        Label(main_frame, text = "Start date must be before the End date").grid(row=0, column=0, sticky='nsew')
        else:
                Label(main_frame, text="Wrong date format, must be y-m-d").grid(row=0, column=0, sticky='nsew')


window = Tk() #creating the main window for the GUI
window.title("FINAL PROJECT AARUSHI- NASA API") 
window.geometry('{}x{}'.format(800, 800)) #size of the window

window.grid_rowconfigure(4, weight=1)  
window.grid_columnconfigure(0, weight=1)

top_frame = Frame(window, bg='pink', width=800, height=150, pady=3) #creating frames
top_frame_2 = Frame(window, bg='yellow', width=800, height=100, pady=3)
top_frame_3 = Frame(window, bg='purple', width=800, height=100, pady=3)
main_frame = Frame(window, width=800, height=300, pady=3, padx=3)

top_frame.grid(row=0, sticky="ew") #placing the frames using grid
top_frame_2.grid(row=1, sticky="new")
top_frame_3.grid(row=2, sticky="new")
main_frame.grid(row=3, sticky="nsew")

API_label = Label(top_frame, text='Enter your given API key:') #labels to interact with user 
Sdate_label = Label(top_frame_2, text='Enter the start date:')
Edate_label = Label(top_frame_2, text='Enter the end date:')
Filter_label = Label(top_frame_3, text='Enter ID to filter it:')
entry_API = Entry(top_frame) #entry field for user to input data 
entry_Sdate = Entry(top_frame_2)
entry_Edate = Entry(top_frame_2)
entry_Filter = Entry(top_frame_3)
 
#placing the labels and entry field 
API_label.grid(row=0, column=0)
Sdate_label.grid(row=0, column=0)
Edate_label.grid(row=0, column=2)
Filter_label.grid(row=0, column=0)
entry_API.grid(row=0, column=1)
entry_Sdate.grid(row=0, column=1)
entry_Edate.grid(row=0, column=3)
entry_Filter.grid(row=0, column=1)

API_list = []
Sdate_list = []
Edate_list = []
Filter_list = []
Times_searched_list = []

def SubmitRequest(): #making the button work
    API = entry_API.get()
    Sdate = entry_Sdate.get()
    Edate = entry_Edate.get() #getting data inputted 
    FilterKey = entry_Filter.get()
    
    API_list.append(API) #appending all the data into existing one
    Sdate_list.append(Sdate)
    Edate_list.append(Edate)
    Filter_list.append(FilterKey)
    for i in range (len(API_list)-len(Times_searched_list)): 
        Times_searched_list.append(1)

    for e in main_frame.winfo_children():
        e.grid_remove()
    GetRequest(window, main_frame, Sdate, Edate, API, FilterKey)

SubmitButton = Button(top_frame_3, text='Submit', command=SubmitRequest)
SubmitButton.grid(row=0, column=2)

def PrevSearch():
    for e in main_frame.winfo_children():
        e.grid_remove()
    a = len(Times_searched_list)-2
    if a >= 0:
        API = API_list[a]
        Sdate = Sdate_list[a]
        Edate = Edate_list[a]
        FilterKey = Filter_list[a]
        GetRequest(window, main_frame, Sdate, Edate, API, FilterKey)
        Times_searched_list.pop()
    else:
        Label(main_frame, text='No more previous search result').grid(row=0, column=0, sticky='nsew')

PrevSearchButton = Button(top_frame_3, text='Previous Search', command=PrevSearch)
PrevSearchButton.grid(row=0, column=3, sticky='e')

window.mainloop() #finally making the window appear 