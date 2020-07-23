import json
import subprocess
import glob
import os
import psycopg2


list_of_files = glob.glob('server/results/*')
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

with open(latest_file, 'rb') as data_file:

    try:
        connection = psycopg2.connect(database="", user="", password="", host="")
        print("Database opened successfully")
        cursor = connection.cursor()
        sqlStringCar = "SELECT * FROM car;"
        cursor.execute(sqlStringCar)
        listCars = cursor.fetchall()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)

    dict = json.loads(data_file.read())

    for item in dict['sessionResult']['leaderBoardLines']:
        pilot_name = item['car']['drivers'][0]['firstName'] + " " + item['car']['drivers'][0]['lastName'] 
        best_time = item['timing']['bestLap']
        best_split_1 = item['timing']['bestSplits'][0]
        best_split_2 = item['timing']['bestSplits'][1]
        best_split_3 = item['timing']['bestSplits'][2]
        car = item['car']['carModel']
        for row in listCars:
            if row[1] == car:
                carId = row[0]
    
        isRaining = dict['sessionResult']['isWetSession']
        sessionType = dict['sessionType']
        track = dict['trackName']
        if best_time < 240000:
            try:
                sqlString = "INSERT INTO time (time_id, pilot_name, lap_time, split_1, split_2, split_3, track_name, car_id, is_wet_session, session_type) VALUES(DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                data = (pilot_name,best_time,best_split_1,best_split_2,best_split_3,track,carId,isRaining,sessionType)
                cursor.execute(sqlString,data)
                connection.commit()
                print ("Successfully inserted into time table")
            except (Exception, psycopg2.Error) as error :
                    print("Failed to insert into time table", error)
        
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
        
