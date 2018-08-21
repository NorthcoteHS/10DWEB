<img align="right" height="185px" src="alttpRando.jpg">

# alttpRando

[The Legend of Zelda: A Link to the Past](https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_A_Link_to_the_Past) was one of the most popular games made for the Nintendo SNES. It was released in 1991-92 but is still played in tournaments today.

One of the most creative adaptations of the game is the ["ALttP Randomiser"](https://alttpr.com/), which takes the original game but shuffles the location of every item. In Zelda games, you unlock access to different parts of the world by acquiring new items. If those items are in random locations, it makes each play-through new and unique.

Your task is to program the *logic* behind this randomiser. You will be given all the information you need below.

## Steps

1. Do some research! [This tournament match](https://www.youtube.com/watch?v=ITpmGZGeCTo#t=11m31s) is a great entry point - the commentators do a good job of explaining what the game is all about.

    - In the link above, the useful commentary starts at 11:31, the match itself begins at 13:16, and it lasts a bit under 2 hours. You don't need to watch the whole thing!
    - There is also a second match in that clip, and there are thousands of other matches available on YouTube and Twitch (see [SpeedGaming](https://www.youtube.com/channel/UC-lm_blkZ_ujmRSwYcJY2ow) on YouTube)

2. Use the information below to create one of:

    - A "tracker" which lets you indicate what items you've found, and tells you which items are available to you. [Example here](https://crossproduct42.github.io/alttprandohelper/tracker.html?mode=open&map).
    - A "seed generator" which assigns the location of each item, following the rules below and ensuring it is possible to complete the game (finish Ganon's Tower, which requires completing the 7 crystals). *This is the harder option.*

3. Start simple - e.g. ignore the zone requirements to begin with.

4. Try to develop a creative solution - one of the hardest steps will be *representing* all of the information and requirements. Try to avoid using 100+ if statements - it will become very difficult to manage. There is always a more elegant solution.


## Information

There is a *lot* of information to handle for this project:

- **Items:** There are 27 items that may be required to complete the game, all other items can be considered "junk".
- **Areas:** There are 9 separate areas in the world that have different requirements to access.
- **Encounters:** There is one boss fight you can do that opens up additional routes around the world.
- **Dungeons:** There are 11 dungeons in the game. To beat the game, you must complete Ganon's Tower. To access Ganon's Tower, you must complete all 7 "Crystal" dungeons, which are randomly chosen from the other 10 dungeons each game. Each dungeon has a different number of item locations inside.
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

#### Areas
| Area | Code | Requirements |
|------|-------|--------------|
| Light World | light |  |
| Death Mountain - Left | mount_left | (<img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px"> <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px">  or <img src="./img/flute.png" alt="Flute" title="Flute" height="20px">) |
| Death Mountain - Top | mount_top | mount_left (<img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> or <img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> ) |
| Death Mountain - Right | mount_right | mount_left (<img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px"> or <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> ) |
| Death Mountain - Dark World | mount_dark | mount_right <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px">  |
| Dark World - North | dark_north | <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> (<img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px"> or <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px">  or agahnim <img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px"> (<img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> or <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px"> or <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px">)) |
| Dark World - South | dark_south | <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> (dark_north or agahnim <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> ) |
| Dark World - East | dark_east | <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> (agahnim or <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px">  or <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px"> <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px"> ) |
| Misery Mire Area | mire_zone | <img src="./img/flute.png" alt="Flute" title="Flute" height="20px"> <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px">  |

#### Encounters
| Encounter | Code | Requirements |
|-----------|-------|--------------|
| Agahnim | agahnim | <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px"> (<img src="./img/sword2.png" alt="Master Sword" title="Master Sword" height="20px"> or <img src="./img/sword1.png" alt="Fighter Sword" title="Fighter Sword" height="20px"> <img src="./img/cape.png" alt="Magic Cape" title="Magic Cape" height="20px"> ) |

#### Dungeons
| Dungeon | # of Items | Zone | Entry Requirements | Completion Requirements |
|---------|------------|------|--------------------|-------------------------|
| Eastern Palace | 3 | light |  | <img src="./img/bow.png" alt="Bow" title="Bow" height="20px"> <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px">  |
| Desert Palace | 2 | light | (<img src="./img/book.png" alt="Book of Mudora" title="Book of Mudora" height="20px"> or mire_zone <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> ) | <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px"> <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px"> (<img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px"> or <img src="./img/firerod.png" alt="Fire Rod" title="Fire Rod" height="20px">) |
| Tower of Hera | 2 | mount_top |  | (<img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px"> or <img src="./img/firerod.png" alt="Fire Rod" title="Fire Rod" height="20px">) |
| Palace of Darkness | 5 | dark_east |  | <img src="./img/bow.png" alt="Bow" title="Bow" height="20px"> <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px">  |
| Swamp Palace | 6 | dark_south | <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px">  | <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> <img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px">  |
| Skull Woods | 2 | dark_north |  | <img src="./img/firerod.png" alt="Fire Rod" title="Fire Rod" height="20px">  |
| Thieves' Town | 4 | dark_north |  | <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px">  |
| Ice Palace | 3 | dark_east | <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px"> <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px"> (<img src="./img/firerod.png" alt="Fire Rod" title="Fire Rod" height="20px"> or <img src="./img/bombos.png" alt="Bombos Medallion" title="Bombos Medallion" height="20px"> <img src="./img/sword1.png" alt="Fighter Sword" title="Fighter Sword" height="20px"> ) | <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> (<img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px"> or <img src="./img/somaria.png" alt="Cane of Somaria" title="Cane of Somaria" height="20px">) |
| Misery Mire | 2 | mire_zone | (<img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px"> or <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px">) | <img src="./img/somaria.png" alt="Cane of Somaria" title="Cane of Somaria" height="20px"> <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px">  |
| Turtle Rock | 5 | mount_dark | <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> <img src="./img/somaria.png" alt="Cane of Somaria" title="Cane of Somaria" height="20px">  | <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px"> <img src="./img/firerod.png" alt="Fire Rod" title="Fire Rod" height="20px"> <img src="./img/icerod.png" alt="Ice Rod" title="Ice Rod" height="20px">  |
| Ganon's Tower | 20 | mount_dark | all_crystals  | <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> <img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px"> <img src="./img/somaria.png" alt="Cane of Somaria" title="Cane of Somaria" height="20px"> <img src="./img/firerod.png" alt="Fire Rod" title="Fire Rod" height="20px"> <img src="./img/bow.png" alt="Bow" title="Bow" height="20px"> <img src="./img/silver.png" alt="Silver Arrows" title="Silver Arrows" height="20px">  |

#### Locations
| Location | # of Items | Zone | Requirements |
|----------|------------|------|--------------|
| Master Sword Pedestal | 1 | light | pendant0 pendant1 pendant2  |
| Mushroom | 1 | light |  |
| Forest Hideout | 1 | light |  |
| Lumberjack Tree | 1 | light | agahnim <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px">  |
| Lost Old Man | 1 | mount_left | <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px">  |
| Spectacle Rock Cave | 1 | mount_left |  |
| Spectacle Rock | 1 | mount_left | <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px">  |
| Ether Tablet | 1 | mount_top | <img src="./img/sword2.png" alt="Master Sword" title="Master Sword" height="20px"> <img src="./img/book.png" alt="Book of Mudora" title="Book of Mudora" height="20px">  |
| Paradox Cave | 7 | mount_right |  |
| Spiral Cave | 1 | mount_right |  |
| Floating Island | 1 | mount_dark | <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px">  |
| Mimic Cave | 1 | turtle | <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px">  |
| Pegasus Rocks | 1 | light | <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px">  |
| Graveyard Ledge Cave | 1 | dark_north | <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px">  |
| King's Tomb | 1 | dark_north | <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px"> (<img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px"> or <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px">) |
| Witch | 1 | light | <img src="./img/mushroom.png" alt="Mushroom" title="Mushroom" height="20px">  |
| Waterfall of Wishing | 2 | light | <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px">  |
| King Zora | 1 | light | (<img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px"> or <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px">) |
| Zora River Ledge | 1 | light | <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px">  |
| Kakariko Well | 5 | light |  |
| Blind's Hideout | 5 | light |  |
| Bottle Vendor | 1 | light |  |
| Chicken House | 1 | light |  |
| Sick Kid | 1 | light | <img src="./img/bottle.png" alt="Bottle" title="Bottle" height="20px">  |
| Tavern | 1 | light |  |
| Blacksmith | 1 | light | <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px">  |
| Magic Bat | 1 | light | <img src="./img/powder.png" alt="Magic Powder" title="Magic Powder" height="20px"> (<img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> or <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px"> <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> ) |
| Sahasrahla's Hut | 3 | light |  |
| Sahasrahla | 1 | light | pendant0  |
| Race Minigame | 1 | light |  |
| Library | 1 | light | <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px">  |
| Grove | 1 | light | <img src="./img/shovel.png" alt="Shovel" title="Shovel" height="20px">  |
| Desert West Ledge | 1 | light | (<img src="./img/book.png" alt="Book of Mudora" title="Book of Mudora" height="20px"> or mire_zone <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> ) |
| Checkerboard Cave | 1 | mire_zone | <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px">  |
| Aginah's Cave | 1 | light |  |
| Bombos Tablet | 1 | dark_south | <img src="./img/sword2.png" alt="Master Sword" title="Master Sword" height="20px"> <img src="./img/book.png" alt="Book of Mudora" title="Book of Mudora" height="20px"> <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px">  |
| Cave 45 | 1 | dark_south | <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px">  |
| Light World Swamp | 2 | light |  |
| Minimoldorm Cave | 5 | light |  |
| Ice Rod Cave | 1 | light |  |
| Lake Hylia Island | 1 | light | <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px"> <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> (dark_south or dark_east) |
| Hobo | 1 | light | <img src="./img/flippers.png" alt="Zora's Flippers" title="Zora's Flippers" height="20px">  |
| Link's House | 1 | light |  |
| Castle Secret Entrance | 2 | light |  |
| Hyrule Castle Dungeon | 3 | light |  |
| Escape Sewer Dark Room | 1 | light | <img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px">  |
| Escape Sewer Side Room | 3 | light | (<img src="./img/lantern.png" alt="Lantern" title="Lantern" height="20px"> or <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px">) |
| Sanctuary | 1 | light |  |
| Bumper Cave | 1 | dark_north | <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px"> <img src="./img/cape.png" alt="Magic Cape" title="Magic Cape" height="20px">  |
| Spike Cave | 1 | mount_left | <img src="./img/moonpearl.png" alt="Moon Pearl" title="Moon Pearl" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px"> (<img src="./img/byrna.png" alt="Cane of Byrna" title="Cane of Byrna" height="20px"> or <img src="./img/cape.png" alt="Magic Cape" title="Magic Cape" height="20px">) |
| Superbunny Cave | 2 | mount_dark |  |
| Hookshot Cave (Top) | 3 | mount_dark | <img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px">  |
| Hookshot Cave (Bottom) | 1 | mount_dark | (<img src="./img/hookshot.png" alt="Hookshot" title="Hookshot" height="20px"> or <img src="./img/boots.png" alt="Pegasus Boots" title="Pegasus Boots" height="20px">) |
| Catfish | 1 | dark_east | <img src="./img/glove1.png" alt="Power Glove" title="Power Glove" height="20px">  |
| Treasure Chest Minigame | 1 | dark_north |  |
| C House | 1 | dark_north |  |
| Bombable Hut | 1 | dark_north |  |
| Purple Chest | 1 | dark_north | <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px">  |
| Hammer Pegs | 1 | dark_north | <img src="./img/glove2.png" alt="Titan's Mitt" title="Titan's Mitt" height="20px"> <img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px">  |
| Pyramid Fairy | 2 | dark_south | crystal5 crystal6 (<img src="./img/hammer.png" alt="Hammer" title="Hammer" height="20px"> or agahnim <img src="./img/mirror.png" alt="Magic Mirror" title="Magic Mirror" height="20px"> ) |
| Pyramid | 1 | dark_east |  |
| Digging Game | 1 | dark_south |  |
| Stumpy | 1 | dark_south |  |
| Hype Cave | 5 | dark_south |  |
| Mire Shed | 2 | mire_zone |  |

## More resources

- [Overworld items guide](https://maplequeensaku.weebly.com/news/legend-of-zelda-a-link-to-the-past-randomizer-overworld-item-locations-guide)
- [Dungeon items guide](https://maplequeensaku.weebly.com/news/legend-of-zelda-a-link-to-the-past-randomizer-dungeon-item-locations-guide)
- [Dungeon requirements guide](https://maplequeensaku.weebly.com/news/what-items-you-need-to-clear-dungeons-in-a-link-to-the-past-randomizer)
