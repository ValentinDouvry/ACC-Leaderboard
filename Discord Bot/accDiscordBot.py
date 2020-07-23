import discord
import psycopg2
import prettytable
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    try:
        global connection
        global cursor
        connection = psycopg2.connect(database="", user="", password="", host="")
        print("Database opened successfully")
        cursor = connection.cursor()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)

@bot.command(description='Liste les 10 meilleurs temps sur le circuit choisi (ex: $temps spa_2019)')
async def temps(ctx, trackName):

    try:
        track = trackName

        sqlStringTime = "SELECT * FROM track WHERE track_name = %s;"
        cursor.execute(sqlStringTime,[track,])
        validTrack = cursor.fetchall()
        if not validTrack:
            trackTable = prettytable.PrettyTable()
            trackTable.title = 'Liste des circuits disponibles'
            trackTable.field_names = ["1", "2", "3", "4",]
            trackTable.header = False            
            trackTable.add_row(["monza","zolder","brands_hatch","silverstone"])
            trackTable.add_row(["paul_ricard","misano","spa","nurburgring"])
            trackTable.add_row(["barcelona","hungaroring","zandvoort","monza_2019"])
            trackTable.add_row(["zolder_2019","brands_hatch_2019","silverstone_2019","paul_ricard_2019"])
            trackTable.add_row(["misano_2019","spa_2019","nurburgring_2019","barcelona_2019"])
            trackTable.add_row(["hungaroring_2019","zandvoort_2019","kyalami_2019","mount_panorama_2019"])
            trackTable.add_row(["suzuka_2019","laguna_seca_2019","",""])

            stringMessage = "```Circuit non reconnu ! Veuillez choisir un circuit existant (ex: $temps monza_2019) :\n"
            stringMessage += trackTable.get_string()
            stringMessage += "```"
            await ctx.send(stringMessage)
        else:
            sqlStringTime = "SELECT * FROM time WHERE track_name = %s ORDER BY lap_time ASC;"
            cursor.execute(sqlStringTime,[track,])
            times = cursor.fetchmany(10)

            timeTable = prettytable.PrettyTable(["", "Nom","Temps","Voiture","Pluie","Session"])
            stringTimeTableTitle = 'Les 10 meilleurs temps sur ' + track
            timeTable.title = stringTimeTableTitle
            i = 0
            for row in times:
                i = i+1
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
                    timeTable.add_row([str(i),row[1],time,row[7],isRain,row[10]]) 

            stringMessage = "```"
            stringMessage += timeTable.get_string()
            stringMessage += "```"
            await ctx.send(stringMessage)                            
                    
    except (Exception, psycopg2.Error) as error:
        print("Failed to get stats from table time", error)

@bot.command(description='Liste les circuits disponibles')
async def circuits(ctx):
    trackTable = prettytable.PrettyTable()
    trackTable.title = 'Liste des circuits disponibles'
    trackTable.field_names = ["1", "2", "3", "4",]
    trackTable.header = False            
    trackTable.add_row(["monza","zolder","brands_hatch","silverstone"])
    trackTable.add_row(["paul_ricard","misano","spa","nurburgring"])
    trackTable.add_row(["barcelona","hungaroring","zandvoort","monza_2019"])
    trackTable.add_row(["zolder_2019","brands_hatch_2019","silverstone_2019","paul_ricard_2019"])
    trackTable.add_row(["misano_2019","spa_2019","nurburgring_2019","barcelona_2019"])
    trackTable.add_row(["hungaroring_2019","zandvoort_2019","kyalami_2019","mount_panorama_2019"])
    trackTable.add_row(["suzuka_2019","laguna_seca_2019","",""])

    stringMessage = "```"
    stringMessage += trackTable.get_string()
    stringMessage += "```"
    await ctx.send(stringMessage)


bot.run('')