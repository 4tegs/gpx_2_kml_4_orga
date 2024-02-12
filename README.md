# GPX_2_KML_4_Orga
## Version and licence
Version 02/2024<br/>
Written by Hans Strassguetl - https://gravelmaps.de  <br/>
Licenced under [https://creativecommons.org/licenses/by-sa/4.0/](https://creativecommons.org/licenses/by-sa/4.0/)
## About
Convert GPX files exported from Garmin Basecamp in one go into a meaningful KML file that can be imported by Maps.me or Organic.Maps.

## Use:
### Planning: 
Planning is done in Garmin Basecamp. 
- Waypoints shall be named without special characters (ä/ö/ü etc)
- Waypoints may include a description
- Waypoints description may contain links
- Tracks shall be named without special characters (ä/ö/ü etc)
- Routes will not be considered as routes do not have reasonable track values.
- Export data via Basecamp File -> Export function.

### Conversion
GPX_2_KML_4_Orga has no user interface. You just take your exported GPX and drag & drop it onto the exe. As a result you have a converted KML with the same name in the same directory as the GPX.
If there are any errors, you will be informed.

## Attention

There are some errors with the color codes in Organic.Maps (not sure for maps.me). 
It reflects the wrong color to the hex codes. You need to exchange the codes as follows:

* Cyan <-> Yellow (Cyan has hex color code for yellow, yellow for cyan)
* DarkCyan <-> DarkYellow
* Blue <-> Red
* DarkBlue <-> DarkRed


## Translation Table
GPX2KML uses a translation table to convert Garmin GPX points and track-colors into KML icons and colors. You can change the translation according to your needs.

### Structure
    {
        "tracks": {
            "Magenta": "pline0",
            "Cyan": "pline1",
            ...
            "Default": "pline0"
        },
        "trackwidth":
            {
                "pline0": "10",
                "pline1": "10",
                ....
                "pline7": "5"
            }
        ,
        "trackcolor":
            {
                "pline0": "FFFE01FE",
                "pline1": "FFFE01FE",
                ....
                "pline7": "FF606060"
            }
        ,
        "points": {
            "Default": "placemark-blue",
            "Gas Station": "placemark-yellow",
            .....
            "Residence": "placemark-green"
        }
    }
### Routes 
Since routes do not have reasonable track values, they are not observed.

### Tracks (Lines)
**All values: tracks, trackcolor & trackwidth, must have the same number of items**.

The assignment is done via all Garmin color names for tracks known to me. First the standards, then the colored dark "color". The Light "color" and the gray tones are bridged to black - you hardly can see them on the display.  

**Keep in mind Attention section above**

     "tracks": {
        "Magenta":      "pline0",
        "Cyan":         "pline1",
        "Green":        "pline2",
        "Red":          "pline3",
        "Blue":         "pline4",
        "Yellow":       "pline5",
        "DarkMagenta":  "pline6",
        "DarkCyan":     "pline7",
        "DarkGreen":    "pline8",
        "DarkRed":      "pline9",
        "DarkBlue":     "pline10",
        "DarkYellow":   "pline11",
        "LightGrey":    "pline12",
        "LightGray":    "pline12",
        "DarkGrey":     "pline12",
        "DarkGray":     "pline12",
        "Black":        "pline12",
        "White":        "pline12",
        "Default":      "pline0"
    },
     "trackcolor":
        {
            "pline0":   "FFFE01FE",  
            "pline1":   "FFFFFF00",
            "pline2":   "FF00FF00",
            "pline3":   "FF0000FF",
            "pline4":   "FFFF4040",
            "pline5":   "FF00F0F0",
            "pline6":   "FF600060",
            "pline7":   "FF808000",
            "pline8":   "FF006000",  
            "pline9":   "FF000060",
            "pline10":  "FF600000", 
            "pline11":  "FF008080",  
            "pline12":  "FF000000"
        }
    ,

### Points

The Organic.Maps implementation of KML does not use graphics as available in Garmin. The following icons are the ones I know:

Standards from Organic.Maps / Maps.Me:

    placemark-red
    placemark-blue
    placemark-purple
    placemark-yellow
    placemark-pink
    placemark-brown
    placemark-green
    placemark-orange
    placemark-deeppurple
    placemark-lightblue
    placemark-cyan
    placemark-teal
    placemark-lime
    placemark-deeporange
    placemark-gray
    placemark-bluegray

My implementation is based on many of the Garmin icons. The implementation done so far see in the actual json.  
Example:

    "points": {
        "Default"       : "placemark-deeporange",
        "Gas Station"   : "placemark-yellow",
        "Information"   : "placemark-cyan",
        "TracBack Point": "placemark-cyan",
        "Toll Booth"    : "placemark-cyan",
        "Ferry"         : "placemark-cyan",
        "Truck"         : "placemark-cyan",
        "Airport"       : "placemark-cyan",
        "Parking Area"  : "placemark-cyan",
        "Residence"     : "placemark-green",
        "Summit"        : "placemark-brown",
        "Campground"    : "placemark-orange",
        "Lodge"         : "placemark-orange",
        "Lodging"       : "placemark-orange"
    }


## Defaults: In the sections
In the translation table there is a default value for the **tracks**. This is needed to assign undescribed color values that come from BaseCamp or MapSource to a color in the KML.<br/>
Similar is valid for Waypoints.

    "tracks": {
        "Default":      "pline0"

    "points": {    
        "Default"       : "placemark-deeporange"

## ColorTable: Name to Hex
This is not neccessarily the list of colors used by me - but you may give it a try!<br/>
This is a good site to check your colors: https://www.color-hex.com/


    aliceblue = 'fffff8f0'
    antiquewhite = 'ffd7ebfa'
    aqua = 'ff00ffff'
    aquamarine = 'ffd4ff7f'
    azure = 'fffffff0'
    beige = 'ffdcf5f5'
    bisque = 'ffc4e4ff'
    black = 'ff000000'
    blanchedalmond = 'ffcdebff'
    blue = 'ffff0000'
    blueviolet = 'ffe22b8a'
    brown = 'ff2a2aa5'
    burlywood = 'ff87b8de'
    cadetblue = 'ffa09e5f'
    chartreuse = 'ff00ff7f'
    chocolate = 'ff1e69d2'
    coral = 'ff507fff'
    cornflowerblue = 'ffed9564'
    cornsilk = 'ffdcf8ff'
    crimson = 'ff3c14dc'
    cyan = 'ff00ffff'
    darkblue = 'ff8b0000'
    darkcyan = 'ff8b8b00'
    darkgoldenrod = 'ff0b86b8'
    darkgray = 'ffa9a9a9'
    darkgrey = 'ffa9a9a9'
    darkgreen = 'ff006400'
    darkkhaki = 'ff6bb7bd'
    darkmagenta = 'ff8b008b'
    darkolivegreen = 'ff2f6b55'
    darkorange = 'ff008cff'
    darkorchid = 'ffcc3299'
    darkred = 'ff00008b'
    darksalmon = 'ff7a96e9'
    darkseagreen = 'ff8fbc8f'
    darkslateblue = 'ff8b3d48'
    darkslategray = 'ff4f4f2f'
    darkslategrey = 'ff4f4f2f'
    darkturquoise = 'ffd1ce00'
    darkviolet = 'ffd30094'
    deeppink = 'ff9314ff'
    deepskyblue = 'ffffbf00'
    dimgray = 'ff696969'
    dimgrey = 'ff696969'
    dodgerblue = 'ffff901e'
    firebrick = 'ff2222b2'
    floralwhite = 'fff0faff'
    forestgreen = 'ff228b22'
    fuchsia = 'ffff00ff'
    gainsboro = 'ffdcdcdc'
    ghostwhite = 'fffff8f8'
    gold = 'ff00d7ff'
    goldenrod = 'ff20a5da'
    gray = 'ff808080'
    grey = 'ff808080'
    green = 'ff008000'
    greenyellow = 'ff2fffad'
    honeydew = 'fff0fff0'
    hotpink = 'ffb469ff'
    indianred = 'ff5c5ccd'
    indigo = 'ff82004b'
    ivory = 'fff0ffff'
    khaki = 'ff8ce6f0'
    lavender = 'fffae6e6'
    lavenderblush = 'fff5f0ff'
    lawngreen = 'ff00fc7c'
    lemonchiffon = 'ffcdfaff'
    lightblue = 'ffe6d8ad'
    lightcoral = 'ff8080f0'
    lightcyan = 'ffffffe0'
    lightgoldenrodyellow = 'ffd2fafa'
    lightgray = 'ffd3d3d3'
    lightgrey = 'ffd3d3d3'
    lightgreen = 'ff90ee90'
    lightpink = 'ffc1b6ff'
    lightsalmon = 'ff7aa0ff'
    lightseagreen = 'ffaab220'
    lightskyblue = 'ffface87'
    lightslategray = 'ff998877'
    lightslategrey = 'ff998877'
    lightsteelblue = 'ffdec4b0'
    lightyellow = 'ffe0ffff'
    lime = 'ff00ff00'
    limegreen = 'ff32cd32'
    linen = 'ffe6f0fa'
    magenta = 'ffff00ff'
    maroon = 'ff000080'
    mediumaquamarine = 'ffaacd66'
    mediumblue = 'ffcd0000'
    mediumorchid = 'ffd355ba'
    mediumpurple = 'ffd87093'
    mediumseagreen = 'ff71b33c'
    mediumslateblue = 'ffee687b'
    mediumspringgreen = 'ff9afa00'
    mediumturquoise = 'ffccd148'
    mediumvioletred = 'ff8515c7'
    midnightblue = 'ff701919'
    mintcream = 'fffafff5'
    mistyrose = 'ffe1e4ff'
    moccasin = 'ffb5e4ff'
    navajowhite = 'ffaddeff'
    navy = 'ff800000'
    oldlace = 'ffe6f5fd'
    olive = 'ff008080'
    olivedrab = 'ff238e6b'
    orange = 'ff00a5ff'
    orangered = 'ff0045ff'
    orchid = 'ffd670da'
    palegoldenrod = 'ffaae8ee'
    palegreen = 'ff98fb98'
    paleturquoise = 'ffeeeeaf'
    palevioletred = 'ff9370d8'
    papayawhip = 'ffd5efff'
    peachpuff = 'ffb9daff'
    peru = 'ff3f85cd'
    pink = 'ffcbc0ff'
    plum = 'ffdda0dd'
    powderblue = 'ffe6e0b0'
    purple = 'ff800080'
    red = 'ff0000ff'
    rosybrown = 'ff8f8fbc'
    royalblue = 'ffe16941'
    saddlebrown = 'ff13458b'
    salmon = 'ff7280fa'
    sandybrown = 'ff60a4f4'
    seagreen = 'ff578b2e'
    seashell = 'ffeef5ff'
    sienna = 'ff2d52a0'
    silver = 'ffc0c0c0'
    skyblue = 'ffebce87'
    slateblue = 'ffcd5a6a'
    slategray = 'ff908070'
    slategrey = 'ff908070'
    snow = 'fffafaff'
    springgreen = 'ff7fff00'
    steelblue = 'ffb48246'
    tan = 'ff8cb4d2'
    teal = 'ff808000'
    thistle = 'ffd8bfd8'
    tomato = 'ff4763ff'
    turquoise = 'ffd0e040'
    violet = 'ffee82ee'
    wheat = 'ffb3def5'
    white = 'ffffffff'
    whitesmoke = 'fff5f5f5'
    yellow = 'ff00ffff'
    yellowgreen = 'ff32cd9a'

## All Basecamp waypoint definitions I'm aware of
	Airport
	Alert
	Amusement Park
	Anchor
	Animal Tracks
	ATV
	Ball Park
	Bank
	Bar
	Beach
	Bell
	Big Game
	Bike Trail
	Binoculars
	Blind
	Block, Blue
	Block, Green
	Block, Red
	Blood Trail
	Boat Ramp
	Bowling
	Bridge
	Building
	Buoy, White
	Campground
	Camp Fire
	Canoe
	Car
	Car Rental
	Car Repair
	Cemetery
	Church
	Circle with X
	Circle, Blue
	Circle, Green
	Circle, Red
	City (Large)
	City (Medium)
	City (Small)
	Civil
	Contact, Afro
	Contact, Alien
	Contact, Ball Cap
	Contact, Big Ears
	Contact, Biker
	Contact, Bug
	Contact, Cat
	Contact, Dog
	Contact, Dreadlocks
	Contact, Female1
	Contact, Female2
	Contact, Female3
	Contact, Goatee
	Contact, Kung-Fu
	Contact, Pig
	Contact, Pirate
	Contact, Ranger
	Contact, Smiley
	Contact, Spike
	Contact, Sumo
	Contact, Female3
	Controlled Area
	Convenience Store
	Cover
	Covey
	Crossing
	Dam
	Danger Area
	Department Store
	Diver Down Flag
	Drinking Water
	Fast Food
	Fishing Area
	Fishing Hot Spot Facility
	Fitness Center
	Flag, Blue
	Flag, Green
	Flag, Red
	Food Source
	Forest
	Furbearer
	Gas Station
	Glider Area
	Golf Course
	Horse Trail
	Hunting
	Kayak
	Letter A, Red
	Letter B, Red
	Letter C, Red
	Letter D, Red
	Lighthouse
	Marina
	Man Overboard
	Medical Facility
	Mine
	Movie Theater
	Museum
	Navaid, Amber
	Navaid, Black
	Navaid, Blue
	Navaid, Green
	Navaid, Orange
	Navaid, Red
	Navaid, Violet
	Navaid, White
	Number 1, Blue
	Number, Blue
	Number, Blue
	Number 4, Blue
	Oil Field
	Parachute Area
	Park
	Parking Area
	Pharmacy
	Picnic Area
	Pin, Blue
	Pin, Green
	Pin, Red
	Pin, Yellow
	Pizza
	Police Station
	Post Office
	Private Field
	Radio Beacon
	Residence
	Restaurant
	Restricted Area
	Restroom
	RV Park
	Scales
	Scenic Area
	School
	Shelter
	Shipwreck
	Shopping Center
	Short Tower
	Shower
	Ski Resort
	Skiing Area
	Skull and Crossbones
	Small Game
	Snowmobile
	Square, Yellow
	Stadium
	Stop Sign
	Street Intersection
	Summit
	Swimming Area
	Tall Tower
	Telephone
	Toll Booth
	Trail Head
	Tree
	Tree Stand
	Treed Quarry
	Triangle, Blue
	Triangle, Green
	Triangle, Red
	Triangle, Yellow
	Truck
	Truck Stop
	Tunnel
	Ultralight Area
	Upland Game
	Waterfowl
	Water Source
	Wind Turbine
	Wrecker
	XSki
	Zoo
