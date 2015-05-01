*summary Details about features in the Python version.*

## Introduction

The Python version has many features and works on the following OS:
  * Windows systems (color support)

Other to be added once Beta is complete for Windows<br>
Beta is complete, and testing is proceeding.

# Details

Features:
  * Color was added to show Damage

| Colour  |   Meaning       |         |
|---------|-----------------|---------|
| Purple  | Slight Damage   | 99-66 % |
| Red     | Mediocre Damage | 65-33 % |
| Whitish | Heavy damage    | 32-0  % |

### Buildings:
  * Empty Building Location (*.*)
  * Astral Lines (Allows buildings to be connected) (* - *) OR (* | *)
  * Wizards Cottage (Main structure) (*W*)
  * Village (Minor Mana generator, and attack building) (*^*)
  * Mining Camp (Better Village, lower HP, Research Gem mining) (*M*)
  * Void Crystal (Can block attacks, destroys connected Astral lines when hit by attack) (*X*) Pre. Gem Mining
  * Wall (Defensive Structure, can be built as an AL or as a Building) (*W*)<br>

### Research:
  * ATTACK: Basic Magics - Allows attacking
  * RESEARCH: Gem Mining - Allows Void Crystals buildings, later allows research of other gem types<br>
  * RESEARCH: Resistance Spell - Allows you to raise the resistance of some items.
  * SPECIAL, there are also some upgrades to buildings that can be done in the stats menu


### Console Commands:
  * () means that this is optional

```
> build (Name)<br>
Goes into build menu, leading you through the building process, also allows viewing of these structure`'`s statistics.<br>
By typing "continue" when choosing where to place it you can keep building by just typing the location, if you have enough mana
<br>

> ally(+ Name)<br>
(*-*) Cancel Alliance with Name<br>
(*+*) Start Alliance with Name,br.
When no optionals are given it goes into a menu to show alliances, and change them.
<br>

> tribute (player amount)<br>
Send Mana to a player
<br>

> fix x,y (amount)<br>
Fixes the building at x,y by the amount, if possible.<br>
'max' may be used as an amount<br>
This can also be done in the stats menu
<br>

> sell x,y<br>
Sells the building at x,y.<br>
This can also be done in the stats menu
<br>

> stats x,y<br>
Shows the building's stats<br>
This menu also allows:<br>
-> Fixing<br>
-> Upgrading the Building<br>
-> Selling
<br>

> income<br>
Shows your income, with all the buildings that give you mana.
<br>

> research (Name)<br>
researches the item if possible
<br>

> attack (Name)<br>
Goes into the attacks menu, and shows possible attacks. Specify the direction and other details for the attack in this menu.
<br>

> save (filename)<br>
lets you save the game, if filename is not specified, it saves on the auto save.
<br>

> load (filename)<br>
lets you load the game, if filename is not specified, it loads the auto save.
<br>

> help (item)<br>
Shows command info and game info and symbols<br>
(Currently not tested and not detailed, will be last part of Beta)
<br>

> surrender<br>
Leave the game, you are considered dead, but can still win in terms of score.
<br>

> quit<br>
> exit<br>
> q<br>
Disconnects from game
<br>

> ~<br>
Goes into console, allows execution of typed data as python script. <br>
This will be removed later, and cheatcodes added instead. (Cheats ?? Maybe)
<br>

> done<br>
> end turn<br>
Ends player's turn.<br><br>
<br>
----
<br>

```

## Ideas for Technology

  * Send any ideas you have to Saevon, they will be viewed and could potentially be added


### NEW ATTACKS:
  * Arrow Hail: choose two points, and all buldings within these points have a chance of being hit, damages allied buildings
  * Poison Magics: Like Basic Magics, but does little damage, makes landscape hit ( only enemy buildings are hit ) poisoned. This last for a while, even if you capture the building.
