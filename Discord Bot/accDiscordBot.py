import discord
import psycopg2
import prettytable

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    try:
        global connection
        global cursor
        connection = psycopg2.connect(database="", user="", password="", host="")
        print("Database opened successfully")
        cursor = connection.cursor()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ACC'):

        if message.content == '$ACC-monza':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'monza' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Monza : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)
        
        elif message.content == '$ACC-zolder':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'zolder' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Zolder : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-brands_hatch':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'brands_hatch' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Brands Hatch : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-silverstone':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'silverstone' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Silverstone : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-paul_ricard':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'paul_ricard ' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Paul Ricard : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-misano':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'misano' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Misano : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-spa':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'spa' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Spa Francorchamps : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-nurburgring':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'nurburgring' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Nurburgring : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-barcelona':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'barcelona' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Barcelona : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-hungaroring':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'hungaroring' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Hungaroring : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-zandvoort':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'zandvoort' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Zandvoort : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-monza_2019':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'monza_2019' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Monza 2019 : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-zolder_2019':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'zolder_2019' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])                
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Zolder 2019 : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-brands_hatch_2019':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'brands_hatch_2019' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Brands Hatch 2019 : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-paul_ricard_2019':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'paul_ricard_2019' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Paul Ricard 2019 : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-misano_2019':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'misano_2019' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Misano 2019 : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-spa_2019':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'spa_2019' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Spa Francorchamps 2019 : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-nurburgring_2019':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'nurburgring_2019' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Nurburgring 2019 : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-barcelona_2019':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'barcelona_2019' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Barcelona 2019 : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-hungaroring_2019':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'hungaroring_2019' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Hungaroring 2019 : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-zandvoort_2019':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'zandvoort_2019' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Zandvoort 2019 : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-kyalami_2019':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'kyalami_2019' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Kyalami 2019 : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-mount_panorama_2019':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'mount_panorama_2019' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Mount Panorama 2019 : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-suzuka_2019':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'suzuka_2019' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Suzuka 2019 : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        elif message.content == '$ACC-laguna_seca_2019':
            try:
                x = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
                cursor.execute("SELECT * FROM time WHERE track_name = 'laguna_seca_2019' ORDER BY lap_time ASC")
                times = cursor.fetchall()
                i = 0
                for row in times:
                    i = i+1
                    if i == 11:
                        break
                    if row[9] == 0:
                        isRain = "Non"
                    else:
                        isRain = "Oui"
                    if row[2] != 2147483647:
                        time = ""
                        millis= row[2]
                        minutes=(millis/(1000*60))%60
                        minutes=int(minutes)
                        seconds=(millis/(1000.0))%60
                        seconds=round(seconds, 3)
                        time = str(minutes) + ":" + str(seconds)
                        x.add_row([str(i),row[1],time,row[7],isRain,row[10]])             
                            
            except (Exception, psycopg2.Error) as error:
                print("Failed to get stats from table time", error)
            else:
                stingMessage = """```Les 10 meilleurs temps sur Laguna Seca 2019 : \n"""
                stingMessage += x.get_string()
                stingMessage += "```"
                await message.channel.send(stingMessage)

        else:
            x = prettytable.PrettyTable()
            x.title = 'Liste des circuits disponibles'
            x.field_names = ["1", "2", "3", "4"]
            x.header = False            
            x.add_row(["monza","zolder","brands_hatch","silverstone"])
            x.add_row(["paul_ricard","misano","spa","nurburgring"])
            x.add_row(["barcelona","hungaroring","zandvoort","monza_2019"])
            x.add_row(["zolder_2019","brands_hatch_2019","silverstone_2019","paul_ricard_2019"])
            x.add_row(["misano_2019","spa_2019","nurburgring_2019","barcelona_2019"])
            x.add_row(["hungaroring_2019","zandvoort_2019","kyalami_2019","mount_panorama_2019"])
            x.add_row(["suzuka_2019","laguna_seca_2019","",""])

            stingMessage = "```Veuillez choisir un circuit (ex: $ACC-monza_2019) :\n"
            stingMessage += x.get_string()
            stingMessage += "```"
            await message.channel.send(stingMessage)
    


client.run('')
