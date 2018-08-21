import re

# Source:   https://github.com/crossproduct42/alttprandohelper/blob/master/js/locations.js
#   (copied code into terminal to get value of `chests`)
locCode = """
altar
mushroom
hideout
tree
lost_man
spectacle_cave
spectacle_rock
ether
paradox
spiral
island_dm
mimic
graveyard_w
graveyard_n
graveyard_e
witch
fairy_lw
zora
river
well
thief_hut
bottle
chicken
kid
tavern
frog
bat
sahasrahla_hut
sahasrahla
maze
library
dig_grove
desert_w
desert_ne
aginah
bombos
grove_s
dam
lake_sw
ice_cave
island_lake
hobo
link_house
secret
castle
escape_dark
escape_side
sanctuary
bumper
spike
bunny
rock_hook
rock_boots
catfish
chest_game
c_house
bomb_hut
purple
pegs
fairy_dw
pyramid
dig_game
stumpy
swamp_ne
mire_w
"""

# Source:   https://github.com/crossproduct42/alttprandohelper/blob/master/js/locations.js
#   (copied code into terminal to get value of `chests`)
locDesc = """
Master Sword Pedestal {pendant0}{pendant1}{pendant2} (can check with {book})
Mushroom
Forest Hideout
Lumberjack Tree {agahnim}{boots}
Lost Old Man {lantern}
Spectacle Rock Cave
Spectacle Rock {mirror}
Ether Tablet {sword2}{book}
Death Mountain East (5 + 2 {bomb})
Spiral Cave
Floating Island {mirror}
Mimic Cave ({mirror} outside of Turtle Rock)(Yellow = {medallion} unknown OR possible w/out {firerod})
West of Sanctuary {boots}
Graveyard Cliff Cave {mirror}
King's Tomb {boots} + {glove2}/{mirror}
Witch: Give her {mushroom}
Waterfall of Wishing (2) {flippers}
King Zora: Pay 500 rupees
Zora River Ledge {flippers}
Kakariko Well (4 + {bomb})
Thieve's Hut (4 + {bomb})
Bottle Vendor: Pay 100 rupees
Chicken House {bomb}
Dying Boy: Distract him with {bottle} so that you can rob his family!
Tavern
Take the frog home {mirror} / Save+Quit
Mad Batter {hammer}/{mirror} + {powder}
Sahasrahla's Hut (3) {bomb}/{boots}
Sahasrahla {pendant0}
Race Minigame {bomb}/{boots}
Library {boots}
Buried Itam {shovel}
Desert West Ledge {book}/{mirror}
Checkerboard Cave {mirror}
Aginah's Cave {bomb}
Bombos Tablet {mirror}{sword2}{book}
South of Grove {mirror}
Light World Swamp (2)
Minimoldorm Cave (NPC + 4) {bomb}
Ice Rod Cave {bomb}
Lake Hylia Island {mirror}
Fugitive under the bridge {flippers}
Stoops Lonk's Hoose
Castle Secret Entrance (Uncle + 1)
Hyrule Castle Dungeon (3)
Escape Sewer Dark Room {lantern}
Escape Sewer Side Room (3) {bomb}/{boots} (yellow = need small key)
Sanctuary
Bumper Cave {cape}
Byrna Spike Cave
Super Bunny Chests (2)
Cave Under Rock (3 top chests) {hookshot}
Cave Under Rock (bottom chest) {hookshot}/{boots}
Catfish
Treasure Chest Minigame: Pay 30 rupees
C House
Bombable Hut {bomb}
Gary's Lunchbox (save the frog first)
Hammer pegs {hammer}{hammer}{hammer}{hammer}{hammer}{hammer}{hammer}{hammer}!!!!!!!!
Fat Fairy: Buy OJ bomb from Dark Link's House after {crystal}5 {crystal}6 (2 items)
Pyramid
Alec Baldwin's Dig-a-Thon: Pay 80 rupees
Ol' Stumpy
Hype Cave! {bomb} (NPC + 4 {bomb})
West of Mire (2)
"""

# Source:   https://github.com/crossproduct42/alttprandohelper/blob/master/js/items.js
#   (copied open_items declaration)
items = """
        tunic: 1,
        sword: 0,
        shield: 0,
        moonpearl: false,

        bow: 0,
        boomerang: 0,
        hookshot: false,
        mushroom: false,
        powder: false,

        firerod: false,
        icerod: false,
        bombos: false,
        ether: false,
        quake: false,

        lantern: false,
        hammer: false,
        shovel: false,
        net: false,
        book: false,

        bottle: 0,
        somaria: false,
        byrna: false,
        cape: false,
        mirror: false,

        boots: false,
        glove: 0,
        flippers: false,
        flute: false,
        agahnim: false
"""

# Create location list from CrossProduct42 variables.
locList = zip(locCode.lstrip().splitlines(), locDesc.lstrip().splitlines())
print('locs = [')
for line in locList:
    desc = re.match(r'^[^\(\{\:]+', line[1])[0].strip()
    out = '    [{:17} {:28} 1, []],'.format('"{}",'.format(line[0]), '"{}",'.format(desc))
    print(out)
print(']')

# Create item list from CrossProduct42 variables.
itemList = items.lstrip().splitlines()
print('items = [')
for line in itemList:
    if not line.strip():
        continue
    item = re.match(r'^[^:]+', line.strip())[0]
    print('    "{}",'.format(item))
print(']')
