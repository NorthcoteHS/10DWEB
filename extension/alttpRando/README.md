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
| Fighter Sword | ![Fighter Sword][sword] |
| Master Sword | ![Master Sword][sword2] |
| Moon Pearl | ![Moon Pearl][moonpearl] |
| Bow | ![Bow][bow] |
| Silver Arrows | ![Silver Arrows][silver] |
| Hookshot | ![Hookshot][hookshot] |
| Mushroom | ![Mushroom][mushroom] |
| Magic Powder | ![Magic Powder][powder] |
| Fire Rod | ![Fire Rod][firerod] |
| Ice Rod | ![Ice Rod][icerod] |
| Bombos Medallion | ![Bombos Medallion][bombos] |
| Ether Medallion | ![Ether Medallion][ether] |
| Quake Medallion | ![Quake Medallion][quake] |
| Lantern | ![Lantern][lantern] |
| Hammer | ![Hammer][hammer] |
| Shovel | ![Shovel][shovel] |
| Book of Mudora | ![Book of Mudora][book] |
| Bottle | ![Bottle][bottle] |
| Cane of Somaria | ![Cane of Somaria][somaria] |
| Cane of Byrna | ![Cane of Byrna][byrna] |
| Magic Cape | ![Magic Cape][cape] |
| Magic Mirror | ![Magic Mirror][mirror] |
| Pegasus Boots | ![Pegasus Boots][boots] |
| Power Glove | ![Power Glove][glove] |
| Titan's Mitt | ![Titan's Mitt][glove2] |
| Zora's Flippers | ![Zora's Flippers][flippers] |
| Flute | ![Flute][flute] |

#### Areas
| Area | Code | Requirements |
|------|-------|--------------|
| Light World | light |  |
| Death Mountain - Left | mount_left | (glove1 ![lantern][lantern]  or ![flute][flute]) |
| Death Mountain - Top | mount_top | mount_left (![mirror][mirror] or ![hookshot][hookshot] ![hammer][hammer] ) |
| Death Mountain - Right | mount_right | mount_left (![hookshot][hookshot] or ![mirror][mirror] ![hammer][hammer] ) |
| Death Mountain - Dark World | mount_dark | mount_right ![moonpearl][moonpearl] ![glove2][glove2]  |
| Dark World - North | dark_north | ![moonpearl][moonpearl] (![glove2][glove2] or glove1 ![hammer][hammer]  or agahnim ![hookshot][hookshot] (![hammer][hammer] or glove1 or ![flippers][flippers])) |
| Dark World - South | dark_south | ![moonpearl][moonpearl] (dark_north or agahnim ![hammer][hammer] ) |
| Dark World - East | dark_east | ![moonpearl][moonpearl] (agahnim or glove1 ![hammer][hammer]  or ![glove2][glove2] ![flippers][flippers] ) |
| Misery Mire Area | mire_zone | ![flute][flute] ![glove2][glove2]  |

#### Encounters
| Encounter | Code | Requirements |
|-----------|-------|--------------|
| Agahnim | agahnim | ![lantern][lantern] (![sword2][sword2] or sword1 ![cape][cape] ) |

#### Dungeons
| Dungeon | # of Items | Zone | Entry Requirements | Completion Requirements |
|---------|------------|------|--------------------|-------------------------|
| Eastern Palace | 3 | light |  | ![bow][bow] ![lantern][lantern]  |
| Desert Palace | 2 | light | (![book][book] or mire_zone ![mirror][mirror] ) | glove1 ![boots][boots] (![lantern][lantern] or ![firerod][firerod]) |
| Tower of Hera | 2 | mount_top |  | (![lantern][lantern] or ![firerod][firerod]) |
| Palace of Darkness | 5 | dark_east |  | ![bow][bow] ![lantern][lantern] ![hammer][hammer]  |
| Swamp Palace | 6 | dark_south | ![mirror][mirror] ![flippers][flippers]  | ![hammer][hammer] ![hookshot][hookshot]  |
| Skull Woods | 2 | dark_north |  | ![firerod][firerod]  |
| Thieves' Town | 4 | dark_north |  | ![hammer][hammer]  |
| Ice Palace | 3 | dark_east | ![flippers][flippers] ![glove2][glove2] (![firerod][firerod] or ![bombos][bombos] sword1 ) | ![hammer][hammer] (![hookshot][hookshot] or ![somaria][somaria]) |
| Misery Mire | 2 | mire_zone | (![hookshot][hookshot] or ![boots][boots]) | ![somaria][somaria] ![lantern][lantern]  |
| Turtle Rock | 5 | mount_dark | ![glove2][glove2] ![hammer][hammer] ![somaria][somaria]  | ![lantern][lantern] ![firerod][firerod] ![icerod][icerod]  |
| Ganon's Tower | 20 | mount_dark | all_crystals  | ![boots][boots] ![hammer][hammer] ![hookshot][hookshot] ![somaria][somaria] ![firerod][firerod] ![bow][bow] ![silver][silver]  |

#### Locations
| Location | # of Items | Zone | Requirements |
|----------|------------|------|--------------|
| Master Sword Pedestal | 1 | light | pendant0 pendant1 pendant2  |
| Mushroom | 1 | light |  |
| Forest Hideout | 1 | light |  |
| Lumberjack Tree | 1 | light | agahnim ![boots][boots]  |
| Lost Old Man | 1 | mount_left | ![lantern][lantern]  |
| Spectacle Rock Cave | 1 | mount_left |  |
| Spectacle Rock | 1 | mount_left | ![mirror][mirror]  |
| Ether Tablet | 1 | mount_top | ![sword2][sword2] ![book][book]  |
| Paradox Cave | 7 | mount_right |  |
| Spiral Cave | 1 | mount_right |  |
| Floating Island | 1 | mount_dark | ![mirror][mirror]  |
| Mimic Cave | 1 | turtle | ![mirror][mirror]  |
| Pegasus Rocks | 1 | light | ![boots][boots]  |
| Graveyard Ledge Cave | 1 | dark_north | ![mirror][mirror]  |
| King's Tomb | 1 | dark_north | ![boots][boots] (![glove2][glove2] or ![mirror][mirror]) |
| Witch | 1 | light | ![mushroom][mushroom]  |
| Waterfall of Wishing | 2 | light | ![flippers][flippers]  |
| King Zora | 1 | light | (![flippers][flippers] or glove1) |
| Zora River Ledge | 1 | light | ![flippers][flippers]  |
| Kakariko Well | 5 | light |  |
| Blind's Hideout | 5 | light |  |
| Bottle Vendor | 1 | light |  |
| Chicken House | 1 | light |  |
| Sick Kid | 1 | light | ![bottle][bottle]  |
| Tavern | 1 | light |  |
| Blacksmith | 1 | light | ![moonpearl][moonpearl] ![glove2][glove2]  |
| Magic Bat | 1 | light | ![powder][powder] (![hammer][hammer] or ![mirror][mirror] ![glove2][glove2] ![moonpearl][moonpearl] ) |
| Sahasrahla's Hut | 3 | light |  |
| Sahasrahla | 1 | light | pendant0  |
| Race Minigame | 1 | light |  |
| Library | 1 | light | ![boots][boots]  |
| Grove | 1 | light | ![shovel][shovel]  |
| Desert West Ledge | 1 | light | (![book][book] or mire_zone ![mirror][mirror] ) |
| Checkerboard Cave | 1 | mire_zone | ![mirror][mirror]  |
| Aginah's Cave | 1 | light |  |
| Bombos Tablet | 1 | dark_south | ![sword2][sword2] ![book][book] ![mirror][mirror]  |
| Cave 45 | 1 | dark_south | ![mirror][mirror]  |
| Light World Swamp | 2 | light |  |
| Minimoldorm Cave | 5 | light |  |
| Ice Rod Cave | 1 | light |  |
| Lake Hylia Island | 1 | light | ![flippers][flippers] ![mirror][mirror] ![moonpearl][moonpearl] (dark_south or dark_east) |
| Hobo | 1 | light | ![flippers][flippers]  |
| Link's House | 1 | light |  |
| Castle Secret Entrance | 2 | light |  |
| Hyrule Castle Dungeon | 3 | light |  |
| Escape Sewer Dark Room | 1 | light | ![lantern][lantern]  |
| Escape Sewer Side Room | 3 | light | (![lantern][lantern] or glove1) |
| Sanctuary | 1 | light |  |
| Bumper Cave | 1 | dark_north | glove1 ![cape][cape]  |
| Spike Cave | 1 | mount_left | ![moonpearl][moonpearl] ![hammer][hammer] glove1 (![byrna][byrna] or ![cape][cape]) |
| Superbunny Cave | 2 | mount_dark |  |
| Hookshot Cave (Top) | 3 | mount_dark | ![hookshot][hookshot]  |
| Hookshot Cave (Bottom) | 1 | mount_dark | (![hookshot][hookshot] or ![boots][boots]) |
| Catfish | 1 | dark_east | glove1  |
| Treasure Chest Minigame | 1 | dark_north |  |
| C House | 1 | dark_north |  |
| Bombable Hut | 1 | dark_north |  |
| Purple Chest | 1 | dark_north | ![glove2][glove2]  |
| Hammer Pegs | 1 | dark_north | ![glove2][glove2] ![hammer][hammer]  |
| Pyramid Fairy | 2 | dark_south | crystal5 crystal6 (![hammer][hammer] or agahnim ![mirror][mirror] ) |
| Pyramid | 1 | dark_east |  |
| Digging Game | 1 | dark_south |  |
| Stumpy | 1 | dark_south |  |
| Hype Cave | 5 | dark_south |  |
| Mire Shed | 2 | mire_zone |  |

[sword]: ./img/sword.jpg "Fighter Sword"
[sword2]: ./img/sword2.jpg "Master Sword"
[moonpearl]: ./img/moonpearl.jpg "Moon Pearl"
[bow]: ./img/bow.jpg "Bow"
[silver]: ./img/silver.jpg "Silver Arrows"
[hookshot]: ./img/hookshot.jpg "Hookshot"
[mushroom]: ./img/mushroom.jpg "Mushroom"
[powder]: ./img/powder.jpg "Magic Powder"
[firerod]: ./img/firerod.jpg "Fire Rod"
[icerod]: ./img/icerod.jpg "Ice Rod"
[bombos]: ./img/bombos.jpg "Bombos Medallion"
[ether]: ./img/ether.jpg "Ether Medallion"
[quake]: ./img/quake.jpg "Quake Medallion"
[lantern]: ./img/lantern.jpg "Lantern"
[hammer]: ./img/hammer.jpg "Hammer"
[shovel]: ./img/shovel.jpg "Shovel"
[book]: ./img/book.jpg "Book of Mudora"
[bottle]: ./img/bottle.jpg "Bottle"
[somaria]: ./img/somaria.jpg "Cane of Somaria"
[byrna]: ./img/byrna.jpg "Cane of Byrna"
[cape]: ./img/cape.jpg "Magic Cape"
[mirror]: ./img/mirror.jpg "Magic Mirror"
[boots]: ./img/boots.jpg "Pegasus Boots"
[glove]: ./img/glove.jpg "Power Glove"
[glove2]: ./img/glove2.jpg "Titan's Mitt"
[flippers]: ./img/flippers.jpg "Zora's Flippers"
[flute]: ./img/flute.jpg "Flute"
