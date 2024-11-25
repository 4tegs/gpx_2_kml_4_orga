# ##########################################################################################
# Hans Straßgütl
#       Read Garmin GPX and write Organic.Maps / Maps.Me type of KML
#       
#       Files provided: 
#           GPX_2_KML.exe
#           GPX_2_KML.JSON translation table with the same filename as the program (you rename the EXE, you rename the JSON!)
#           Readme.md
#           
# ------------------------------------------------------------------------------------------
# Stand:
#	2022 12 05		Start Programmierung
#	2022 12 13		Added UTF-8 Support. Character from Balkans states crashed readlines(). 
#   2023 01 29      Added Description (comment) field of waypoints into KML Description
#   2024 02 12      Started to migrate on a common tools set - h_utils.py
#                   Needs to be improved in coding season 24/25
#   2024 05 17      h_utils.py now included and compiled in the right manner.
#                   JSON file included in EXE as a fallback in case its missing in the directory
#
# ##########################################################################################
from datetime import datetime
import os
import sys
from pathlib import Path
import gpxpy
import gpxpy.gpx
import simplekml
import time

# ...................................................
# Where do I find my utils to be imported? Set your path here!
sys.path.append("C:\\SynologyDrive\\Python\\00_import_h_utils")
import h_utils                                                                              # type: ignore
# I wasn't able to find the error in my compile, but as long as I don't add the same 
# imports as in utils, the exe breaks with an import error.
# Duplicate imports from uitls.py:
# from pathlib import Path
# import json
# import gpxpy
# import sys
# from tkinter import *
# from tkinter import ttk
# from ttkthemes import ThemedTk
# import xml.etree.ElementTree as ET
# ...................................................

def make_short_name(in_file_name , in_suffix ):
# ...................................................
# Make Short GPX FileName
# Only Name - no path
# 2022 12 06
# ...................................................
    '''
    Make a valid KML name, only name and suffix, no path

    ### Args: 
    - Input  :  GPX File Name to be analyzed
    - Returns:  KML File Name to be used. May be blank
                KML Temp Name
    '''
    if in_file_name:
        in_name = Path(in_file_name).stem      # Der Name der Datei ohne Suffix
        short_file_name = str(in_name) + in_suffix
        tmp_file_name = str(in_name) + '_tmp' + in_suffix
    else:
        short_file_name = ''
        tmp_file_name = ''
    return short_file_name , tmp_file_name

def make_kml_name(gpx_in_file_name ):
# ...................................................
# Make KML FileName
# 2022 12 06
# ...................................................
    '''
    Make a valid KML name.
    Name, Suffix and Path

    ### Args: 
    - Input  : GPX File Name to be analyzed
    - Returns: KML File Name to be used. May be blank
    '''
    if gpx_in_file_name:
        in_path = Path(gpx_in_file_name).parent    # Der Pfad zur EingabeDatei
        in_name = Path(gpx_in_file_name).stem      # Der Name der Datei ohne Suffix
        in_suffix = '.kml'
        kml_file_name = str(in_path) + '\\' + str(in_name) + in_suffix
    else:
        kml_file_name = ''
    return kml_file_name


# ------------------------------------------------------------------------------------------
#  _   _ _   _ _ _ _   _           
# | | | | |_(_) (_) |_(_) ___  ___ 
# | | | | __| | | | __| |/ _ \/ __|
# | |_| | |_| | | | |_| |  __/\__ \
#  \___/ \__|_|_|_|\__|_|\___||___/
# ------------------------------------------------------------------------------------------

def timestamp():
# ------------------------------------------------------------------------------------------
# Schreibe einen Timestamp
# ------------------------------------------------------------------------------------------
    '''Provide formated timestamp'''
    now_time = datetime.now()
    now_time = str(now_time)[:19]
    # print(now_time)
    return now_time

# ------------------------------------------------------------------------------------------
#   ____ ______  __
#  / ___|  _ \ \/ /
# | |  _| |_) \  / 
# | |_| |  __//  \ 
#  \____|_|  /_/\_\
# ------------------------------------------------------------------------------------------
def gpx_elements(gpx_file_name):   
# ...................................................
# Elements in GPX
# 2022 12 05
# ...................................................
    '''
    Analyzes GPX for Routes - Tracks - Waypoints

    ### Args: 
    - Input gpx_file_name
    - Returns: gpx, tracknames_given, waypoints_given

    ### Methods:
        - 
    '''
    # ...........................................
    # Load GPX
    # ...........................................
    gpx_file = ''
    with open(gpx_file_name, "r", encoding='utf-8') as gpx_file:
        data = gpx_file.readlines()                     # read data line by line 

    # ...........................................
    # Clean GPX 
    # Wenn man die GPX von Basecamp bekommt, dann hat 
    # die an den ersten 4 Stellen irgendwas drin stehen. 
    # Das muss weg!
    # ...........................................
    gpx_tmp = open(gpx_tmp_file_name, "w", encoding='utf-8')                      # Open a Tempfile. Will be deleted later
    # i = 0
    for x in data:
    #     wo = x.find('<')
    #     if wo != -1: 
    #         gpx_tmp.write(x[wo:])
            gpx_tmp.write(x)
    #         # i += 1
    gpx_tmp.close()

    # ...........................................
    # The GPX is cleaned now from strange characters. 
    # Read file from disc and parse it for GPX
    # ...........................................
    gpx_file = open(gpx_tmp_file_name, 'r', encoding='utf-8')   
    gpx = gpxpy.parse(gpx_file)             # Jetzt mache ein GPX/XML
    # ...........................................
    # Ganz wichtig: Lösche nun alle Routen heraus, 
    # die will ich nicht in den KML sehen
    # ...........................................
    gpx.routes = []                     
    
    # ...........................................
    # Create a List for waypoints and another 
    # for Tracknames
    # ...........................................

    waypoints_given = []
    this_waypoint = []
    for waypoint in gpx.waypoints:
        # print(str(waypoint))
        this_waypoint = [waypoint.name, waypoint.symbol, waypoint.longitude , waypoint.latitude , waypoint.comment ]
        # print( this_waypoint[0], this_waypoint[1], this_waypoint[2], this_waypoint[3],  this_waypoint[4], sep='  ', end='\n' )
        waypoints_given.append(this_waypoint)

    tracknames_given = []
    if len(gpx.tracks) > 0:
        for track in gpx.tracks:  
            this_track = []
            coords = []
            # c = ''
            for segment in track.segments:
                 for point in segment.points:
                    if not point.elevation:
                        point.elevation = 0
                    coords.append((point.longitude,point.latitude, point.elevation))

            this_track = [track.name, track.description, 'Magenta' , coords]
            tracknames_given.append(this_track)

    # ...........................................
    # Now all names are stored in a List
    # Close File. 
    # ...........................................
    gpx_file.close()
    # ...........................................
    # Next we need to temporarily store the 
    # reworked gpx.
    # ...........................................
    gpx_tmp = open(gpx_tmp_file_name, "w" , encoding='utf-8')                      # Trash the former Tempfile and open a new. Will be deleted later.
    gpx_tmp.write(gpx.to_xml())                         # Bring it into a readable xml format and write it to disc.
    # ...........................................
    # Return the reworked GPX to caller
    # ...........................................
    return gpx, tracknames_given , waypoints_given

def gpx_colors_in_tracks(gpx_file_name, tracknames_given):
# ...................................................
# Get colors from GPX Track
# 2022 12 07
# There is a problem I was not able to solve using the standard 
# libraries, as they can't handle Garmin format implementation 
# for GPX. The issue is in the track extension 
#   <extensions>
#       <gpxx:TrackExtension>
#       <gpxx:DisplayColor>DarkGray</gpxx:DisplayColor>
#       </gpxx:TrackExtension>
#   </extensions>
# For that I decided to create a "manual" walk through and set the colors 
# into the "tracknames_given" list.
# ...................................................
    ''' 
    Walks through the GPX Tempfile (the one where routes already have been deleted)
    collects the track colors and sets them into tracknames_given.

    ### Args: 
    - Input  :  file:           gpx_file_name ,
                list:           tracknames_given
    
    - Returns:  reworked list:  tracknames_given

    '''
    # global tracknames_given
    gpx_file = ''
    with open(gpx_file_name, "r", encoding='utf-8') as gpx_file:
        data = gpx_file.readlines()                     # read data line by line 

    # ...........................................
    # Bau die Farbe aus dem GPX Track in den neuen Track ein.
    #
    # hier kommt ein Fehler ins Spiel:
    # Eigentlich hieß das Statement gpxx, die Biblio macht
    # MANCHMAL  
    # beim rausschreiben in die Tempfile ein gpxtrx daraus!
    # Daher nun beide Abfragen um sicher zu gehen, dass 
    # alles klappt.
    # ...........................................
    l_length= len('<gpxtrx:DisplayColor>')              
    r_length= len('</gpxtrx:DisplayColor>')
    track_count = 0 
    for x in data:
        x = x.strip()
        if x == '<trk>':
            track_count += 1
        if x[:l_length] == '<gpxtrx:DisplayColor>':
            # print('gefunden')
            y = x[l_length:]
            y = y[:(r_length*-1)]
            tracknames_given[track_count-1][2] = y

    l_length= len('<gpxx:DisplayColor>')              
    r_length= len('</gpxx:DisplayColor>')
    track_count = 0 
    for x in data:
        x = x.strip()
        if x == '<trk>':
            track_count += 1
        if x[:l_length] == '<gpxx:DisplayColor>':
            # print('gefunden')
            y = x[l_length:]
            y = y[:(r_length*-1)]
            tracknames_given[track_count-1][2] = y

    return tracknames_given

# ------------------------------------------------------------------------------------------
#  _  ____  __ _     
# | |/ /  \/  | |    
# | ' /| |\/| | |    
# | . \| |  | | |___ 
# |_|\_\_|  |_|_____|
# ------------------------------------------------------------------------------------------
def write_kml(tracknames_given , waypoints_given , my_line_color, my_line_width, my_kml_color):
# ...................................................
# Write KML
# 2022 12 07
# Siehe Readme.md
# ...................................................
    global kml_file_name
    global kml_short_file_name
    global kml_tmp_file_name
    global json_file_name
    kml_waypoint_colors = ['placemark-red' ,
        'placemark-blue' ,
        'placemark-purple' ,
        'placemark-yellow' ,
        'placemark-pink' ,
        'placemark-brown' ,
        'placemark-green' ,
        'placemark-orange' ,
        'placemark-deeppurple' ,
        'placemark-lightblue' ,
        'placemark-cyan' ,
        'placemark-teal' ,
        'placemark-lime' ,
        'placemark-deeporange' ,
        'placemark-gray' ,
        'placemark-bluegray' ]
    
    # ...........................................
    # Lade die Json Translate Tabelle. 
    # Hole die Point Symbole
    # Setze default für einen falschen Punkt
    # 
    # Eröffne eine neue KML
    # Nun Loop durch alle WayPoints
    # ...........................................
    translate_table = h_utils.load_json(None)
    my_point_symbol = translate_table.get("points")
    default_point_symbol = my_point_symbol.get("Default")
    
    kml = simplekml.Kml( name=kml_short_file_name)
    fld1 = kml.newfolder(name='Waypoints')
    for i in waypoints_given:
        a =  i[1]
        b = my_point_symbol.get(a)
        if b == None: b = default_point_symbol
        # print(b)
        fld1 = kml.newpoint(name=str(i[0]) , coords = [(str(i[2]) ,str(i[3]))])
        # fld1.coords = [(str(i[2]) ,str(i[3]))]
        fld1.description = str(i[4])                    
        fld1.address = b                    
    # ...........................................
    # Ein kleiner Trick. Da keine Bibliothek in der Lage 
    # war eine KML im Organic.Maps Format zu schreiben, 
    # speichere ich den Wert des PlaceMarks im address 
    # Field 
    #   fld1.description = b
    # zwischen.
    # ...........................................

    # ...........................................
    # Hole die Parameter aus der Translate Tabelle
    # Danach schreibe alle Tracks raus
    # ...........................................
    my_line_width = translate_table.get("trackwidth")
    default_line_width = '10'
    my_line_color = translate_table.get("tracks")
    default_line_color = my_line_color.get("Default")

    fld2 = kml.newfolder(name='Tracks')
    for i in tracknames_given:
        a =  i[2]    
        # print(str(i) + ' \n ' + a)                              
        b = my_line_color.get(a)                                # bekomme die pline für die GPX Farbe
        if b == None: b = default_line_color
        ls = fld2.newlinestring(name=i[0])                      # type: ignore
        ls.coords = (i[3])
        ls.description = b
        
        b = my_line_width.get(a)
        if b == None: b = default_line_width
        ls.atomauthor = b
    # ...........................................
    # Ein kleiner Trick. Da keine Bibliothek in der Lage 
    # war eine KML im Organic.Maps Format zu schreiben, 
    # speichere ich den Wert der pline im Description Field 
    #   fld1.description = b
    # zwischen.
    # ...........................................
    

    kml.save(kml_file_name) # Schreibe die fast fertige File raus.
    # ...........................................
    # Da die KML File so nicht in Organic.Maps gelesen 
    # werden kann, müssen nun manuelle Eingriffe 
    # getätigt werden.
    # ...........................................

    # ...........................................
    # Lösche leading und trailing blanks in der KML
    # ...........................................
    l_length= len('<gpxtrx:DisplayColor>')
    r_length= len('</gpxtrx:DisplayColor>')
    # i = 0

    kml_tmp = open(kml_tmp_file_name, "w", encoding='utf-8')              # Open a Tempfile. Will be deleted later

    with open(kml_file_name, "r", encoding='utf-8') as kml_file:
        data = kml_file.readlines()                     # read data line by line 

    for x in data:
        x = x.strip()
        x = x + '\n'
        kml_tmp.writelines(x)
    kml_tmp.close()
    kml_file.close()

    with open(kml_tmp_file_name, "r", encoding='utf-8') as kml_file:
        data = kml_file.readlines()                     # read data line by line 
    kml_file.close()
    
    kml_tmp = open(kml_file_name, "w", encoding='utf-8')
    i = 0
    for x in data:
        kml_tmp.writelines(x)
        if i == 3:
            for y in kml_waypoint_colors:
                kml_tmp.writelines('<Style id="' + y + '">\n')
                kml_tmp.writelines('<IconStyle>')
                kml_tmp.writelines('<Icon>')
                kml_tmp.writelines('<href>https://omaps.app/placemarks/'  + y + '</href>\n' )
                kml_tmp.writelines('</Icon>\n')
                kml_tmp.writelines('</IconStyle>\n')
                kml_tmp.writelines('</Style>\n')
            for y in my_line_width:
                my_pline_color  = my_kml_color.get(y)
                my_pline_width  = my_line_width.get(y)
                kml_tmp.writelines('<Style id="' + y + '">\n')
                kml_tmp.writelines('<LineStyle>\n')
                kml_tmp.writelines('<color>' + str(my_pline_color) + '</color>\n' )
                kml_tmp.writelines('<width>' + str(my_pline_width) + '</width>\n' )
                kml_tmp.writelines('</LineStyle>\n')
                kml_tmp.writelines('</Style>\n')
        if x.find('<address>placemark') == 0 :
            l_length= len('<address>')
            r_length= len('</address>')
            y = x[l_length:]
            y = y[:(r_length*-1)-1]
            kml_tmp.writelines('<Snippet maxLines="0"/>\n')
            kml_tmp.writelines('<styleUrl>#' + y + '</styleUrl>\n')

        if x.find('<description>pline') == 0 :
            l_length= len('<description>')
            r_length= len('</description>')
            y = x[l_length:]
            y = y[:(r_length*-1)-1]
            kml_tmp.writelines('<styleUrl>#' + y + '</styleUrl>\n')
        i = i+1
    kml_tmp.close()


    return

# ------------------------------------------------------------------------------------------
#  __  __       _       
# |  \/  | __ _(_)_ __  
# | |\/| |/ _` | | '_ \ 
# | |  | | (_| | | | | |
# |_|  |_|\__,_|_|_| |_|
# ------------------------------------------------------------------------------------------
if __name__ == "__main__":
    global gpx_file_name
    global kml_file_name
    global kml_short_file_name
    global kml_tmp_file_name
    global json_file_name

    # ....................................................
    # Erhalte die Übergabeparameter. Erstelle dazu den 
    # default GPX Entry - sofern übergeben.
    # Ansonsten setze Default Pfad auf den Pfad der Exe
    # ....................................................
    os.system('cls')     
    my_script = h_utils.IchSelbst()

    my_name = sys.argv[0]                       # the first argument is the script itself
    my_stem = Path(my_name).stem                # Das ist der DateiName ohne Suffix
    my_path = Path(my_name).parent              # Das ist der Path ohne trailing \
    my_name = Path(my_name).name                # Der Dateiname
    file_paths = sys.argv[1:]                   # the first argument (0) is the script itself. 1: heisst, wir haben nun in der file_paths alle anderen Argumente
    print("\n\nGPX_2_KML - convert Garmin GPX into KML for Organic.Maps\n Version v2.0 dated 11/2024\nWritten by Hans Strassguetl - https://gravelmaps.de \nLicenced under https://creativecommons.org/licenses/by-sa/4.0/ \n\n")


    # Make sure you have either set a valid GPX / KML name 
    # or make sure its clear
    # ....................................................
    mein_gpx = h_utils.mein_gpx(None)
    gpx_file_name = mein_gpx.gpx_name_with_path

    if gpx_file_name:
        kml_file_name = make_kml_name(gpx_file_name)
        gpx_short_file_name, gpx_tmp_file_name = make_short_name(gpx_file_name, '.gpx')
        kml_short_file_name, kml_tmp_file_name = make_short_name(gpx_file_name, '.kml')
    else:
        gpx_file_name = ''
        gpx_short_file_name = ''
        gpx_tmp_file_name = ''
        kml_file_name = ''
        kml_short_file_name = ''
        kml_tmp_file_name = ''
        h_utils.error_message("gpx_02",True)

    translate_table = h_utils.load_json(None)
    my_line_color = translate_table.get("tracks")
    default_line_color = my_line_color.get("Default")
    my_line_width = translate_table.get("trackwidth")
    my_kml_color = translate_table.get("trackcolor")
    my_point_symbol = translate_table.get("points")
    default_point_symbol = my_point_symbol.get("Default")
    # ....................................................
    # Lese die GPX
    # Schreibe die TrackNamen und die WayPoints in seprate Bereiche
    # ....................................................
    gpx , tracknames_given , waypoints_given  = gpx_elements(gpx_file_name)
    # ....................................................
    # Nachdem die Garmin GPX Tracks im Gegensatz zu Standard 
    # GPX Farben kennen, muss ich diese extra behandeln
    # ....................................................
    tracknames_given = gpx_colors_in_tracks(gpx_tmp_file_name, tracknames_given)
    # ....................................................
    # Jetzt Mache aus dem GPX Gerüst eine KML
    # ....................................................
    write_kml(tracknames_given, waypoints_given , my_line_color, my_line_width, my_kml_color )
    os.remove(gpx_tmp_file_name) # Works only if compiled! 
    os.remove(kml_tmp_file_name) # Works only if compiled! 
    print('\n\nDone!\nYou should now find a KML with the same folder and with the same name as the calling GPX.\nProgram closes.\n\n')
    time.sleep(1) # Seconds
sys.exit(0)

