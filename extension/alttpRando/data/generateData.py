""" TODO:
- moonpearl exceptions (just pyramid?)
- medallion logic (mire/turtle)
"""

# --- DATA --- #

items = [
    ["sword1",		"Fighter Sword"],
    ["sword2",		"Master Sword"],
    ["moonpearl",	"Moon Pearl"],
    ["bow",			"Bow"],
    ["silver",		"Silver Arrows"],
    ["hookshot",	"Hookshot"],
    ["mushroom",	"Mushroom"],
    ["powder",		"Magic Powder"],
    ["firerod",		"Fire Rod"],
    ["icerod",		"Ice Rod"],
    ["bombos",		"Bombos Medallion"],
    ["ether",		"Ether Medallion"],
    ["quake",		"Quake Medallion"],
    ["lantern",		"Lantern"],
    ["hammer",		"Hammer"],
    ["shovel",		"Shovel"],
    ["book",		"Book of Mudora"],
    ["bottle",		"Bottle"],
    ["somaria",		"Cane of Somaria"],
    ["byrna",		"Cane of Byrna"],
    ["cape",		"Magic Cape"],
    ["mirror",		"Magic Mirror"],
    ["boots",		"Pegasus Boots"],
    ["glove1",		"Power Glove"],
    ["glove2",		"Titan's Mitt"],
    ["flippers",	"Zora's Flippers"],
    ["flute",		"Flute"],
]

imgInfo = items + [
    ["agahnim",		"Agahnim"],
    ["pendant0",	"Green Pendant (Courage)"],
    ["pendant1",	"Blue Pendant (Power)"],
    ["pendant2",	"Red Pendant (Wisdom)"],
    ["crystal1",	"Crystal 1"],
    ["crystal2",	"Crystal 2"],
    ["crystal3",	"Crystal 3"],
    ["crystal4",	"Crystal 4"],
    ["crystal5",	"Crystal 5"],
    ["crystal6",	"Crystal 6"],
    ["crystal7",	"Crystal 7"],
]

areas = [
    ["light",		"Light World",					[]],
    ["mount_left",	"Death Mountain - Left",		[[['glove1', 'lantern'], 'flute']]],
    ["mount_top",	"Death Mountain - Top",			['mount_left', ['mirror', ['hookshot', 'hammer']]]],
    ["mount_right",	"Death Mountain - Right",		['mount_left', ['hookshot', ['mirror', 'hammer']]]],
    ["mount_dark",	"Death Mountain - Dark World",	['mount_right', 'moonpearl', 'glove2']],
    ["dark_north",	"Dark World - North",			['moonpearl', ['glove2', ['glove1', 'hammer'], ['agahnim', 'hookshot', ['hammer', 'glove1', 'flippers']]]]],
    ["dark_south",	"Dark World - South",			['moonpearl', ['dark_north', ['agahnim', 'hammer']]]],
    ["dark_east",	"Dark World - East",			['moonpearl', ['agahnim', ['glove1', 'hammer'], ['glove2', 'flippers']]]],
    ["mire_zone",	"Misery Mire Area",				['flute', 'glove2']],
]

encounters = [
    ["agahnim",		"Agahnim",	['lantern', ['sword2', ['sword1', 'cape']]]],
]

dungeons = [
    ["eastern",		"Eastern Palace",		3,	'light',		[],	['bow', 'lantern']],
    ["desert",		"Desert Palace",		2,	'light',		[['book', ['mire_zone', 'mirror']]],	['glove1', 'boots', ['lantern', 'firerod']]],
    ["hera",		"Tower of Hera",		2,	'mount_top',	[],	[['lantern', 'firerod']]],
    ["darkness",	"Palace of Darkness",	5,	'dark_east',	[110],	['bow', 'lantern', 'hammer']],
    ["swamp",		"Swamp Palace",			6,	'dark_south',	['mirror', 'flippers'],	['hammer', 'hookshot']],
    ["skull",		"Skull Woods",			2,	'dark_north',	[],	['firerod']],
    ["thieves",		"Thieves' Town",		4,	'dark_north',	[],	['hammer']],
    ["ice",			"Ice Palace",			3,	'dark_east',	['flippers', 'glove2', ['firerod', ['bombos', 'sword1']]],	['hammer', ['hookshot', 'somaria']]],
    ["mire",		"Misery Mire",			2,	'mire_zone',	[['hookshot', 'boots']],	['somaria', 'lantern']],
    ["turtle",		"Turtle Rock",			5,	'mount_dark',	['glove2', 'hammer', 'somaria'],	['lantern', 'firerod', 'icerod']],
    ["gt",			"Ganon's Tower",		20,	'mount_dark',	['crystal1', 'crystal2', 'crystal3', 'crystal4', 'crystal5', 'crystal6', 'crystal7'],	['boots', 'hammer', 'hookshot', 'somaria', 'firerod', 'bow', 'silver']],
]

locations = [
    ["pedestal",       "Master Sword Pedestal",     1, 0,       'light',		['pendant0', 'pendant1', 'pendant2']],
    ["mushroom",       "Mushroom",                  1, 0,       'light',		[]],
    ["hideout",        "Forest Hideout",            1, 0,       'light',		[]],
    ["tree",           "Lumberjack Tree",           1, 0,       'light',		['agahnim', 'boots']],
    ["lost_man",       "Lost Old Man",              1, 0,       'mount_left',	['lantern']],
    ["spectacle_cave", "Spectacle Rock Cave",       1, 0,       'mount_left',	[]],
    ["spectacle_rock", "Spectacle Rock",            1, 0,       'mount_left',	['mirror']],
    ["ether",          "Ether Tablet",              1, 0,       'mount_top',	['sword2', 'book']],
    ["paradox",        "Paradox Cave",              7, 1,       'mount_right',	[]],
    ["spiral",         "Spiral Cave",               1, 0,       'mount_right',	[]],
    ["island_dm",      "Floating Island",           1, 0,       'mount_dark',	['mirror']],
    ["mimic",          "Mimic Cave",                1, 0,       'turtle',		['mirror']],
    ["graveyard_w",    "Pegasus Rocks",             1, 0,       'light',		['boots']],
    ["graveyard_n",    "Graveyard Ledge Cave",      1, 0,       'dark_north',	['mirror']],
    ["graveyard_e",    "King's Tomb",               1, 0,       'dark_north',	['boots', ['glove2', 'mirror']]],
    ["witch",          "Witch",                     1, 0,       'light',		['mushroom']],
    ["fairy_lw",       "Waterfall of Wishing",      2, 0,       'light',		['flippers']],
    ["zora",           "King Zora",                 1, 0,       'light',		[500, ['flippers', 'glove1']]],
    ["river",          "Zora River Ledge",          1, 0,       'light',		['flippers']],
    ["well",           "Kakariko Well",             5, 1,       'light',		[]],
    ["thief_hut",      "Blind's Hideout",           5, 1,       'light',		[]],
    ["bottle",         "Bottle Vendor",             1, 0,       'light',		[100]],
    ["chicken",        "Chicken House",             1, 1,       'light',		[]],
    ["kid",            "Sick Kid",                  1, 0,       'light',		['bottle']],
    ["tavern",         "Tavern",                    1, 0,       'light',		[]],
    ["blacksmith",     "Blacksmith",                1, 0,       'light',		['moonpearl', 'glove2']],
    ["bat",            "Magic Bat",                 1, 0,       'light',		['powder', ['hammer', ['mirror', 'glove2', 'moonpearl']]]],
    ["sahasrahla_hut", "Sahasrahla's Hut",          3, -1,      'light',		[]],
    ["sahasrahla",     "Sahasrahla",                1, 0,       'light',		['pendant0']],
    ["maze",           "Race Minigame",             1, -1,      'light',		[]],
    ["library",        "Library",                   1, 0,       'light',		['boots']],
    ["dig_grove",      "Grove",                     1, 0,       'light',		['shovel']],
    ["desert_w",       "Desert West Ledge",         1, 0,       'light',		[['book', ['mire_zone', 'mirror']]]],
    ["desert_ne",      "Checkerboard Cave",         1, 0,       'mire_zone',	['mirror']],
    ["aginah",         "Aginah's Cave",             1, 1,       'light',		[]],
    ["bombos_tab",     "Bombos Tablet",             1, 0,       'dark_south',	['sword2', 'book', 'mirror']],
    ["grove_s",        "Cave 45",                   1, 0,       'dark_south',	['mirror']],
    ["dam",            "Light World Swamp",         2, 0,       'light',		[]],
    ["lake_sw",        "Minimoldorm Cave",          5, 1,       'light',		[]],
    ["ice_cave",       "Ice Rod Cave",              1, 1,       'light',		[]],
    ["island_lake",    "Lake Hylia Island",         1, 0,       'light',		['flippers', 'mirror', 'moonpearl', ['dark_south', 'dark_east']]],
    ["hobo",           "Hobo",                      1, 0,       'light',		['flippers']],
    ["link_house",     "Link's House",              1, 0,       'light',		[]],
    ["secret",         "Castle Secret Entrance",    2, 0,       'light',		[]],
    ["castle",         "Hyrule Castle Dungeon",     3, 0,       'light',		[]],
    ["escape_dark",    "Escape Sewer Dark Room",    1, 0,       'light',		['lantern']],
    ["escape_side",    "Escape Sewer Side Room",    3, -1,      'light',		[['lantern', 'glove1']]],
    ["sanctuary",      "Sanctuary",                 1, 0,       'light',		[]],
    ["bumper",         "Bumper Cave",               1, 0,       'dark_north',	['glove1', 'cape']],
    ["spike",          "Spike Cave",                1, 0,       'mount_left',	['moonpearl', 'hammer', 'glove1', ['byrna', 'cape']]],
    ["bunny",          "Superbunny Cave",           2, 0,       'mount_dark',	[]],
    ["rock_hook",      "Hookshot Cave (Top)",       3, 0,       'mount_dark',	['hookshot']],
    ["rock_boots",     "Hookshot Cave (Bottom)",    1, 0,       'mount_dark',	[['hookshot', 'boots']]],
    ["catfish",        "Catfish",                   1, 0,       'dark_east',	['glove1']],
    ["chest_game",     "Treasure Chest Minigame",   1, 0,       'dark_north',	[30]],
    ["c_house",        "C House",                   1, 0,       'dark_north',	[]],
    ["bomb_hut",       "Bombable Hut",              1, 1,       'dark_north',	[]],
    ["purple",         "Purple Chest",              1, 0,       'dark_north',	['glove2']],
    ["pegs",           "Hammer Pegs",               1, 0,       'dark_north',	['glove2', 'hammer']],
    ["fairy_dw",       "Pyramid Fairy",             2, 0,       'dark_south',	['crystal5', 'crystal6', ['hammer', ['agahnim', 'mirror']]]],
    ["pyramid",        "Pyramid",                   1, 0,       'dark_east',	[]],
    ["dig_game",       "Digging Game",              1, 0,       'dark_south',	[80]],
    ["stumpy",         "Stumpy",                    1, 0,       'dark_south',	[]],
    ["swamp_ne",       "Hype Cave",                 5, 2,       'dark_south',	[]],
    ["mire_w",         "Mire Shed",                 2, 0,       'mire_zone',	[]],
]


# --- FUNCTIONS --- #

# Deal with recursive requirement lists.
def parseReq(reqs):
    out = ''
    for req in reqs:
        if isinstance(req, list):
            orList = [parseReq(x) if isinstance(x, list) else imgRef(x,x) for x in req]
            out += '({})'.format(' or '.join(orList))
        elif isinstance(req, str):
            out += imgRef(req, req) + ' '
    return out

# Create a reference to an image.
def imgRef(code, desc):
    #return '![{1}][{0}]'.format(code, desc) if code in imgCodes else code
    if code in imgCodes:
        desc = imgInfo[imgCodes.index(code)][1]
        return '<img src="./img/{0}.png" alt="{1}" title="{1}" height="20px">'.format(code, desc)
    else:
        return code

# Create an image mapping for the footer.
def imgFoot(code, desc):
    return '[{0}]: ./img/{0}.png "{1}"\n'.format(code, desc)


# --- MAIN --- #

# Pre-allocate.
imgCodes = [x[0] for x in imgInfo]
main = ''
#foot = ''

# Items.
main += '#### Items\n\n| Item | Image |\n|------|-------|\n'
for item in items:
    main += '| {} | {} |\n'.format(item[1], imgRef(item[0], item[1]))
    #foot += imgFoot(item[0], item[1])

# Areas.
#main += '\n| Area | Image | Requirements |\n|------|-------|--------------|\n'
main += '\n#### Areas\n\n| Area | Code | Requirements |\n|------|-------|--------------|\n'
for item in areas:
    req = parseReq(item[2])
    main += '| {} | {} | {} |\n'.format(item[1], item[0], req)
    #main += '| {} | {} | {} |\n'.format(item[1], imgRef(item[0], item[1]), req)
    #foot += imgFoot(item[0], item[1])

# Encounters.
#main += '\n| Encounter | Image | Requirements |\n|-----------|-------|--------------|\n'
main += '\n#### Encounters\n\n| Encounter | Image | Requirements |\n|-----------|--------|--------------|\n'
for item in encounters:
    req = parseReq(item[2])
    #main += '| {} | {} | {} |\n'.format(item[1], item[0], req)
    main += '| {} | {} | {} |\n'.format(item[1], imgRef(item[0], item[1]), req)
    #foot += imgFoot(item[0], item[1])

# Dungeons.
main += '\n#### Dungeons\n\n| Dungeon | # of Items | Zone | Entry Requirements | Completion Requirements |'
main += '\n|---------|------------|------|--------------------|-------------------------|\n'
for item in dungeons:
    req1 = parseReq(item[4])
    req2 = parseReq(item[5])
    main += '| {} | {} | {} | {} | {} |\n'.format(item[1], item[2], item[3], req1, req2)

# Locations.
main += '\n#### Locations\n\n| Location | # of Items | Zone | Requirements |'
main += '\n|----------|------------|------|--------------|\n'
for item in locations:
    req = parseReq(item[5])
    main += '| {} | {} | {} | {} |\n'.format(item[1], item[2], item[4], req)


print(main)
#print(foot)
