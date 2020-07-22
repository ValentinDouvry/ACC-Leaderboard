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
        connection = psycopg2.connect(
            database="", user="", password="", host="")
        print("Database opened successfully")
        cursor = connection.cursor()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)

    dict = json.loads(data_file.read())

    for item in dict['sessionResult']['leaderBoardLines']:
        category = ""
        pilot_name = item['car']['drivers'][0]['firstName'] + " " + item['car']['drivers'][0]['lastName'] 
        best_time = item['timing']['bestLap']
        best_split_1 = item['timing']['bestSplits'][0]
        best_split_2 = item['timing']['bestSplits'][1]
        best_split_3 = item['timing']['bestSplits'][2]
        car = item['car']['carModel']
        if car == 0:
            car = 'Porsche 991 GT3'
            category = "GT3"
        elif car == 1:
            car = 'Mercedes AMG GT3'
            category = "GT3"
        elif car == 2:
            car = 'Ferrari 488 GT3'
            category = "GT3"
        elif car == 3:
            car = 'Audi R8 LMS'
            category = "GT3"
        elif car == 4:
            car = 'Lamborghini Huracan GT3'
            category = "GT3"
        elif car == 5:
            car = 'McLaren 650s GT3'
            category = "GT3"
        elif car == 6:
            car = 'Nissan GT R Nismo GT3 2018'
            category = "GT3"
        elif car == 7:
            car = 'BMW M6 GT3'
            category = "GT3"
        elif car == 8:
            car = 'Bentley Continental GT3 2018'
            category = "GT3"
        elif car == 9:
            car = 'Porsche 991.2 GT3 Cup'
            category = "GT3"
        elif car == 10:
            car = 'Nissan GT-R Nismo GT3 2017'
            category = "GT3"
        elif car == 11:
            car = 'Bentley Continental GT3 2016'
            category = "GT3"
        elif car == 12:
            car = 'Aston Martin Vantage V12 GT3'
            category = "GT3"
        elif car == 13:
            car = 'Lamborghini Gallardo R-EX'
            category = "GT3"
        elif car == 14:
            car = 'Jaguar G3'
            category = "GT3"
        elif car == 15:
            car = 'Lexus RC F GT3'
            category = "GT3"
        elif car == 16:
            car = 'Lamborghini Huracan Evo (2019)'
            category = "GT3"
        elif car == 17:
            car = 'Honda NSX GT3'
            category = "GT3"
        elif car == 18:
            car = 'Lamborghini Huracan SuperTrofeo'
            category = "GT3"
        elif car == 19:
            car = 'Audi R8 LMS Evo (2019)'
            category = "GT3"
        elif car == 20:
            car = 'AMR V8 Vantage (2019)'
            category = "GT3"
        elif car == 21:
            car = 'Honda NSX Evo (2019)'
            category = "GT3"
        elif car == 22:
            car = 'McLaren 720S GT3 (2019)'
            category = "GT3"
        elif car == 23:
            car = 'Porsche 911 II GT3 R (2019)'
            category = "GT3"
        elif car == 50:
            car = 'Alpine A1110 GT4'
            category = "GT4"
        elif car == 51:
            car = 'Aston Martin Vantage GT4'
            category = "GT4"
        elif car == 52:
            car = 'Audi R8 LMS GT4'
            category = "GT4"
        elif car == 53:
            car = 'BMW M4 GT4'
            category = "GT4"
        elif car == 55:
            car = 'Chevrolet Camaro GT4'
            category = "GT4"
        elif car == 56:
            car = 'Ginetta G55 GT4'
            category = "GT4"
        elif car == 57:
            car = 'KTM X-Bow GT4'
            category = "GT4"
        elif car == 58:
            car = 'Maserati MC GT4'
            category = "GT4"
        elif car == 59:
            car = 'McLaren 570S GT4'
            category = "GT4"
        elif car == 60:
            car = 'Mercedes AMG GT4'
            category = "GT4"
        elif car == 61:
            car = 'Porsche 718 Cayman GT4'
            category = "GT4"
    
        isRaining = dict['sessionResult']['isWetSession']
        sessionType = dict['sessionType']
        track = dict['trackName']
        try:
            cursor.execute('INSERT INTO time (time_id, pilot_name, lap_time, split_1, split_2, split_3, track_name, car_name,category, is_wet_session, session_type) VALUES(DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(pilot_name,best_time,best_split_1,best_split_2,best_split_3,track,car,category,isRaining,sessionType))
            connection.commit()
            print ("Successfully inserted into time table")
        except (Exception, psycopg2.Error) as error :
                print("Failed to insert into time table", error)
        
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")
        
