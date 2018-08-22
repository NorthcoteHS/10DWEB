<img align="right" height="185px" src="alttpRando.jpg">

# alttpRando

[The Legend of Zelda: A Link to the Past](https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_A_Link_to_the_Past) was one of the most popular games made for the Nintendo SNES. It was released in 1991-92 but is still played in tournaments today.

One of the most creative adaptations of the game is the ["ALttP Randomiser"](https://alttpr.com/), which takes the original game but shuffles the location of every item. In Zelda games, you unlock access to different parts of the world by acquiring new items. If those items are in random locations, it makes each play-through new and unique.

Your task is to program the *logic* behind this randomiser (see Step 2 below). You will be given all the information you need below.

## Steps

1. Do some research! [This tournament match](https://www.youtube.com/watch?v=ITpmGZGeCTo#t=11m31s) is a great entry point - the commentators do a good job of explaining what the game is all about.

    - In the link above, the useful commentary starts at 11:31, the match itself begins at 13:16, and it lasts a bit under 2 hours. You don't need to watch the whole thing!
    - There is also a second match in that clip, and there are thousands of other matches available on YouTube and Twitch (see [SpeedGaming](https://www.youtube.com/channel/UC-lm_blkZ_ujmRSwYcJY2ow) on YouTube)

2. Use the information below to create one of:

    - A "tracker" which lets you indicate what items you've found, and tells you which locations are available to you. [Example here](https://crossproduct42.github.io/alttprandohelper/tracker.html?mode=open&map).
    - A "seed generator" which assigns the location of each item, following the rules below and ensuring it is possible to complete the game (finish Ganon's Tower, which requires completing the 7 crystals). *This is the harder option.*

3. Start simple - for the tracker, try creating:

    - A list of all the **Items**, with a way to enter whether you have found them or not (checkboxes, text inputs, however you want to do it).
    - A list of the **Zones** (ignore individual item locations to start).
    - A **Calculate** button, which computes which zones are available with those items.
    - Then somehow indicate the result (e.g. changing the text colour of the available zones using styles).
    - **Ignore** the Agahnim requirements to begin with (or just treat it as an Item that you can toggle on/off).

4. Build from there - the next step is to add the **Locations** (skip Dungeons for now). You can make a list like the Zones, and modify the Calculate button to also check each individual Location.

5. The trickiest bit will be the dungeons - see the [Information](#information) below. The 3 Pendants and 7 Crystals are randomly shuffled between all 10 dungeons, and all 7 Crystals are required to beat the game. In addition, certain locations require specific crystals or pendants. Finally, there are different requirements for getting *into* each dungeon vs. *completing* the dungeon.

6. As you go, try to develop a creative solution - one of the hardest steps will be *representing* all of the information and requirements. Try to avoid using 100+ if statements - it will become very difficult to manage. There is always a more elegant solution.


## Information

There is a *lot* of information to handle for this project:

- **Items:** There are 27 items that may be required to complete the game, all other items can be considered "junk".
- **Zones:** There are 9 separate zones in the world that have different requirements to access.
- **Encounters:** There is one boss fight you can do that opens up additional routes around the world.
- **Dungeons:** There are 10 dungeons in the game, plus Ganon's Tower. Defeating a dungeon gives you either a Pendant (not required) or a Crystal (required to enter Ganon's Tower). There are 3 Pendants and 7 Crystals, shuffled randomly among the 10 dungeons. The goal of the game is to complete Ganon's Tower and defeat Ganon.
- **Locations:** Every item in the game is either in a dungeon or in the "overworld". All the overworld locations are listed, with the requirements to access.

Note that every location has a zone and requirements - to get the item, you must be able to access that zone *and* have all the other requirements. The logic is often complicated, with ands and ors.

#### Items

| Item | Image |
|------|-------|
| Fighter Sword | <img src="./img/sword1.png" alt="Fighter Sword" title="Fighter Sword" height="20px"> |
| Master Sword | <img src="./img/sword2.png" alt="Master Sword" title="Master Sword" height="20px"> |
| Moon Pearl | <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> |
| Bow | <img src="./img/bow.png" alt="Bow" title="Bow" height="20px"> |
| Silver Arrows | <img src="./img/silver.png" alt="Silver Arrows" title="Silver Arrows" height="20px"> |
| Hookshot | <img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px"> |
| Mushroom | <img src="./img/mushroom.png" alt="Mushroom" title="Mushroom" height="20px"> |
| Magic Powder | <img src="./img/powder.png" alt="Magic Powder" title="Magic Powder" height="20px"> |
| Fire Rod | <img src="./img/firerod.png" alt="Fire Rod" title="Fire Rod" height="20px"> |
| Ice Rod | <img src="./img/icerod.png" alt="Ice Rod" title="Ice Rod" height="20px"> |
| Bombos Medallion | <img src="./img/bombos.png" alt="Bombos Medallion" title="Bombos Medallion" height="20px"> |
| Ether Medallion | <img src="./img/ether.png" alt="Ether Medallion" title="Ether Medallion" height="20px"> |
| Quake Medallion | <img src="./img/quake.png" alt="Quake Medallion" title="Quake Medallion" height="20px"> |
| Lantern | <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px"> |
| Hammer | <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> |
| Shovel | <img src="./img/shovel.png" alt="Shovel" title="Shovel" height="20px"> |
| Book of Mudora | <img src="./img/book.png" alt="Book of Mudora" title="Book of Mudora" height="20px"> |
| Bottle | <img src="./img/bottle.png" alt="Bottle" title="Bottle" height="20px"> |
| Cane of Somaria | <img src="./img/somaria.png" alt="Cane of Somaria" title="Cane of Somaria" height="20px"> |
| Cane of Byrna | <img src="./img/byrna.png" alt="Cane of Byrna" title="Cane of Byrna" height="20px"> |
| Magic Cape | <img src="./img/cape.png" alt="Magic Cape" title="Magic Cape" height="20px"> |
| Magic Mirror | <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> |
| Pegasus Boots | <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px"> |
| Power Glove | <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px"> |
| Titan's Mitt | <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px"> |
| Zora's Flippers | <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px"> |
| Flute | <img src="./img/flute.png" alt="Flute" title="Flute" height="20px"> |

#### Zones

| Zone | Image | Requirements |
|------|-------|--------------|
| Light World | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Death Mountain - Left | <img src="./img/mount_left.png" alt="Death Mountain - Left" title="Death Mountain - Left" height="20px"> | (<img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px"> <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px">  or <img src="./img/flute.png" alt="Flute" title="Flute" height="20px">) |
| Death Mountain - Top | <img src="./img/mount_top.png" alt="Death Mountain - Top" title="Death Mountain - Top" height="20px"> | <img src="./img/mount_left.png" alt="Death Mountain - Left" title="Death Mountain - Left" height="20px"> (<img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> or <img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> ) |
| Death Mountain - Right | <img src="./img/mount_right.png" alt="Death Mountain - Right" title="Death Mountain - Right" height="20px"> | <img src="./img/mount_left.png" alt="Death Mountain - Left" title="Death Mountain - Left" height="20px"> (<img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px"> or <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> ) |
| Death Mountain - Dark World | <img src="./img/mount_dark.png" alt="Death Mountain - Dark World" title="Death Mountain - Dark World" height="20px"> | <img src="./img/mount_right.png" alt="Death Mountain - Right" title="Death Mountain - Right" height="20px"> <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px">  |
| Dark World - North | <img src="./img/dark_north.png" alt="Dark World - North" title="Dark World - North" height="20px"> | <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> (<img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px"> or <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px">  or <img src="./img/agahnim.png" alt="Agahnim" title="Agahnim" height="20px"> <img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px"> (<img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> or <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px"> or <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px">)) |
| Dark World - South | <img src="./img/dark_south.png" alt="Dark World - South" title="Dark World - South" height="20px"> | <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> (<img src="./img/dark_north.png" alt="Dark World - North" title="Dark World - North" height="20px"> or <img src="./img/agahnim.png" alt="Agahnim" title="Agahnim" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> ) |
| Dark World - East | <img src="./img/dark_east.png" alt="Dark World - East" title="Dark World - East" height="20px"> | <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> (<img src="./img/agahnim.png" alt="Agahnim" title="Agahnim" height="20px"> or <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px">  or <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px"> <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px"> ) |
| Misery Mire Area | <img src="./img/mire_zone.png" alt="Misery Mire Area" title="Misery Mire Area" height="20px"> | <img src="./img/flute.png" alt="Flute" title="Flute" height="20px"> <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px">  |

#### Encounters

| Encounter | Image | Requirements |
|-----------|--------|--------------|
| Agahnim | <img src="./img/agahnim.png" alt="Agahnim" title="Agahnim" height="20px"> | <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px"> (<img src="./img/sword2.png" alt="Master Sword" title="Master Sword" height="20px"> or <img src="./img/sword1.png" alt="Fighter Sword" title="Fighter Sword" height="20px"> <img src="./img/cape.png" alt="Magic Cape" title="Magic Cape" height="20px"> ) |

#### Dungeons

| Dungeon | # of Items | Zone | Entry Requirements | Completion Requirements |
|---------|------------|------|--------------------|-------------------------|
| Eastern Palace | 3 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  | <img src="./img/bow.png" alt="Bow" title="Bow" height="20px"> <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px">  |
| Desert Palace | 2 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | (<img src="./img/book.png" alt="Book of Mudora" title="Book of Mudora" height="20px"> or <img src="./img/mire_zone.png" alt="Misery Mire Area" title="Misery Mire Area" height="20px"> <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> ) | <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px"> <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px"> (<img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px"> or <img src="./img/firerod.png" alt="Fire Rod" title="Fire Rod" height="20px">) |
| Tower of Hera | 2 | <img src="./img/mount_top.png" alt="Death Mountain - Top" title="Death Mountain - Top" height="20px"> |  | (<img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px"> or <img src="./img/firerod.png" alt="Fire Rod" title="Fire Rod" height="20px">) |
| Palace of Darkness | 5 | <img src="./img/dark_east.png" alt="Dark World - East" title="Dark World - East" height="20px"> |  | <img src="./img/bow.png" alt="Bow" title="Bow" height="20px"> <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px">  |
| Swamp Palace | 6 | <img src="./img/dark_south.png" alt="Dark World - South" title="Dark World - South" height="20px"> | <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px">  | <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> <img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px">  |
| Skull Woods | 2 | <img src="./img/dark_north.png" alt="Dark World - North" title="Dark World - North" height="20px"> |  | <img src="./img/firerod.png" alt="Fire Rod" title="Fire Rod" height="20px">  |
| Thieves' Town | 4 | <img src="./img/dark_north.png" alt="Dark World - North" title="Dark World - North" height="20px"> |  | <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px">  |
| Ice Palace | 3 | <img src="./img/dark_east.png" alt="Dark World - East" title="Dark World - East" height="20px"> | <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px"> <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px"> (<img src="./img/firerod.png" alt="Fire Rod" title="Fire Rod" height="20px"> or <img src="./img/bombos.png" alt="Bombos Medallion" title="Bombos Medallion" height="20px"> <img src="./img/sword1.png" alt="Fighter Sword" title="Fighter Sword" height="20px"> ) | <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> (<img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px"> or <img src="./img/somaria.png" alt="Cane of Somaria" title="Cane of Somaria" height="20px">) |
| Misery Mire | 2 | <img src="./img/mire_zone.png" alt="Misery Mire Area" title="Misery Mire Area" height="20px"> | (<img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px"> or <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px">) | <img src="./img/somaria.png" alt="Cane of Somaria" title="Cane of Somaria" height="20px"> <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px">  |
| Turtle Rock | 5 | <img src="./img/mount_dark.png" alt="Death Mountain - Dark World" title="Death Mountain - Dark World" height="20px"> | <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> <img src="./img/somaria.png" alt="Cane of Somaria" title="Cane of Somaria" height="20px">  | <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px"> <img src="./img/firerod.png" alt="Fire Rod" title="Fire Rod" height="20px"> <img src="./img/icerod.png" alt="Ice Rod" title="Ice Rod" height="20px">  |
| Ganon's Tower | 20 | <img src="./img/mount_dark.png" alt="Death Mountain - Dark World" title="Death Mountain - Dark World" height="20px"> | <img src="./img/crystal1.png" alt="Crystal 1" title="Crystal 1" height="20px"> <img src="./img/crystal2.png" alt="Crystal 2" title="Crystal 2" height="20px"> <img src="./img/crystal3.png" alt="Crystal 3" title="Crystal 3" height="20px"> <img src="./img/crystal4.png" alt="Crystal 4" title="Crystal 4" height="20px"> <img src="./img/crystal5.png" alt="Crystal 5" title="Crystal 5" height="20px"> <img src="./img/crystal6.png" alt="Crystal 6" title="Crystal 6" height="20px"> <img src="./img/crystal7.png" alt="Crystal 7" title="Crystal 7" height="20px">  | <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> <img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px"> <img src="./img/somaria.png" alt="Cane of Somaria" title="Cane of Somaria" height="20px"> <img src="./img/firerod.png" alt="Fire Rod" title="Fire Rod" height="20px"> <img src="./img/bow.png" alt="Bow" title="Bow" height="20px"> <img src="./img/silver.png" alt="Silver Arrows" title="Silver Arrows" height="20px">  |

#### Locations

| Location | # of Items | Zone | Requirements |
|----------|------------|------|--------------|
| Master Sword Pedestal | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | <img src="./img/pendant0.png" alt="Green Pendant (Courage)" title="Green Pendant (Courage)" height="20px"> <img src="./img/pendant1.png" alt="Blue Pendant (Power)" title="Blue Pendant (Power)" height="20px"> <img src="./img/pendant2.png" alt="Red Pendant (Wisdom)" title="Red Pendant (Wisdom)" height="20px">  |
| Mushroom | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Forest Hideout | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Lumberjack Tree | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | <img src="./img/agahnim.png" alt="Agahnim" title="Agahnim" height="20px"> <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px">  |
| Lost Old Man | 1 | <img src="./img/mount_left.png" alt="Death Mountain - Left" title="Death Mountain - Left" height="20px"> | <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px">  |
| Spectacle Rock Cave | 1 | <img src="./img/mount_left.png" alt="Death Mountain - Left" title="Death Mountain - Left" height="20px"> |  |
| Spectacle Rock | 1 | <img src="./img/mount_left.png" alt="Death Mountain - Left" title="Death Mountain - Left" height="20px"> | <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px">  |
| Ether Tablet | 1 | <img src="./img/mount_top.png" alt="Death Mountain - Top" title="Death Mountain - Top" height="20px"> | <img src="./img/sword2.png" alt="Master Sword" title="Master Sword" height="20px"> <img src="./img/book.png" alt="Book of Mudora" title="Book of Mudora" height="20px">  |
| Paradox Cave | 7 | <img src="./img/mount_right.png" alt="Death Mountain - Right" title="Death Mountain - Right" height="20px"> |  |
| Spiral Cave | 1 | <img src="./img/mount_right.png" alt="Death Mountain - Right" title="Death Mountain - Right" height="20px"> |  |
| Floating Island | 1 | <img src="./img/mount_dark.png" alt="Death Mountain - Dark World" title="Death Mountain - Dark World" height="20px"> | <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px">  |
| Mimic Cave | 1 | turtle | <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px">  |
| Pegasus Rocks | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px">  |
| Graveyard Ledge Cave | 1 | <img src="./img/dark_north.png" alt="Dark World - North" title="Dark World - North" height="20px"> | <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px">  |
| King's Tomb | 1 | <img src="./img/dark_north.png" alt="Dark World - North" title="Dark World - North" height="20px"> | <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px"> (<img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px"> or <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px">) |
| Witch | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | <img src="./img/mushroom.png" alt="Mushroom" title="Mushroom" height="20px">  |
| Waterfall of Wishing | 2 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px">  |
| King Zora | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | (<img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px"> or <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px">) |
| Zora River Ledge | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px">  |
| Kakariko Well | 5 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Blind's Hideout | 5 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Bottle Vendor | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Chicken House | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Sick Kid | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | <img src="./img/bottle.png" alt="Bottle" title="Bottle" height="20px">  |
| Tavern | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Blacksmith | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px">  |
| Magic Bat | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | <img src="./img/powder.png" alt="Magic Powder" title="Magic Powder" height="20px"> (<img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> or <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px"> <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> ) |
| Sahasrahla's Hut | 3 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Sahasrahla | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | <img src="./img/pendant0.png" alt="Green Pendant (Courage)" title="Green Pendant (Courage)" height="20px">  |
| Race Minigame | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Library | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px">  |
| Grove | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | <img src="./img/shovel.png" alt="Shovel" title="Shovel" height="20px">  |
| Desert West Ledge | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | (<img src="./img/book.png" alt="Book of Mudora" title="Book of Mudora" height="20px"> or <img src="./img/mire_zone.png" alt="Misery Mire Area" title="Misery Mire Area" height="20px"> <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> ) |
| Checkerboard Cave | 1 | <img src="./img/mire_zone.png" alt="Misery Mire Area" title="Misery Mire Area" height="20px"> | <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px">  |
| Aginah's Cave | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Bombos Tablet | 1 | <img src="./img/dark_south.png" alt="Dark World - South" title="Dark World - South" height="20px"> | <img src="./img/sword2.png" alt="Master Sword" title="Master Sword" height="20px"> <img src="./img/book.png" alt="Book of Mudora" title="Book of Mudora" height="20px"> <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px">  |
| Cave 45 | 1 | <img src="./img/dark_south.png" alt="Dark World - South" title="Dark World - South" height="20px"> | <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px">  |
| Light World Swamp | 2 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Minimoldorm Cave | 5 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Ice Rod Cave | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Lake Hylia Island | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px"> <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> (<img src="./img/dark_south.png" alt="Dark World - South" title="Dark World - South" height="20px"> or <img src="./img/dark_east.png" alt="Dark World - East" title="Dark World - East" height="20px">) |
| Hobo | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px">  |
| Link's House | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Castle Secret Entrance | 2 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Hyrule Castle Dungeon | 3 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Escape Sewer Dark Room | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px">  |
| Escape Sewer Side Room | 3 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> | (<img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px"> or <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px">) |
| Sanctuary | 1 | <img src="./img/light.png" alt="Light World" title="Light World" height="20px"> |  |
| Bumper Cave | 1 | <img src="./img/dark_north.png" alt="Dark World - North" title="Dark World - North" height="20px"> | <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px"> <img src="./img/cape.png" alt="Magic Cape" title="Magic Cape" height="20px">  |
| Spike Cave | 1 | <img src="./img/mount_left.png" alt="Death Mountain - Left" title="Death Mountain - Left" height="20px"> | <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px"> (<img src="./img/byrna.png" alt="Cane of Byrna" title="Cane of Byrna" height="20px"> or <img src="./img/cape.png" alt="Magic Cape" title="Magic Cape" height="20px">) |
| Superbunny Cave | 2 | <img src="./img/mount_dark.png" alt="Death Mountain - Dark World" title="Death Mountain - Dark World" height="20px"> |  |
| Hookshot Cave (Top) | 3 | <img src="./img/mount_dark.png" alt="Death Mountain - Dark World" title="Death Mountain - Dark World" height="20px"> | <img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px">  |
| Hookshot Cave (Bottom) | 1 | <img src="./img/mount_dark.png" alt="Death Mountain - Dark World" title="Death Mountain - Dark World" height="20px"> | (<img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px"> or <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px">) |
| Catfish | 1 | <img src="./img/dark_east.png" alt="Dark World - East" title="Dark World - East" height="20px"> | <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px">  |
| Treasure Chest Minigame | 1 | <img src="./img/dark_north.png" alt="Dark World - North" title="Dark World - North" height="20px"> |  |
| C House | 1 | <img src="./img/dark_north.png" alt="Dark World - North" title="Dark World - North" height="20px"> |  |
| Bombable Hut | 1 | <img src="./img/dark_north.png" alt="Dark World - North" title="Dark World - North" height="20px"> |  |
| Purple Chest | 1 | <img src="./img/dark_north.png" alt="Dark World - North" title="Dark World - North" height="20px"> | <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px">  |
| Hammer Pegs | 1 | <img src="./img/dark_north.png" alt="Dark World - North" title="Dark World - North" height="20px"> | <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px">  |
| Pyramid Fairy | 2 | <img src="./img/dark_south.png" alt="Dark World - South" title="Dark World - South" height="20px"> | <img src="./img/crystal5.png" alt="Crystal 5" title="Crystal 5" height="20px"> <img src="./img/crystal6.png" alt="Crystal 6" title="Crystal 6" height="20px"> (<img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> or <img src="./img/agahnim.png" alt="Agahnim" title="Agahnim" height="20px"> <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> ) |
| Pyramid | 1 | <img src="./img/dark_east.png" alt="Dark World - East" title="Dark World - East" height="20px"> |  |
| Digging Game | 1 | <img src="./img/dark_south.png" alt="Dark World - South" title="Dark World - South" height="20px"> |  |
| Stumpy | 1 | <img src="./img/dark_south.png" alt="Dark World - South" title="Dark World - South" height="20px"> |  |
| Hype Cave | 5 | <img src="./img/dark_south.png" alt="Dark World - South" title="Dark World - South" height="20px"> |  |
| Mire Shed | 2 | <img src="./img/mire_zone.png" alt="Misery Mire Area" title="Misery Mire Area" height="20px"> |  |

## More resources

- [Overworld items guide](https://maplequeensaku.weebly.com/news/legend-of-zelda-a-link-to-the-past-randomizer-overworld-item-locations-guide)
- [Dungeon items guide](https://maplequeensaku.weebly.com/news/legend-of-zelda-a-link-to-the-past-randomizer-dungeon-item-locations-guide)
- [Dungeon requirements guide](https://maplequeensaku.weebly.com/news/what-items-you-need-to-clear-dungeons-in-a-link-to-the-past-randomizer)
