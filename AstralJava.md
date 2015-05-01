*summary Details about features in the Java version.*

## Introduction 

The Java version has many features and works on the following OS:
  * All UNIX based systems
  * Apple Macs and iPod Touch/iPhone (iPhoneOS)
  * Windows systems



## General Gameplay

Astral is turn-based and therefore follows a turn order and allows the following actions (in order):
  # Get income and power
  # Build, fix, or sell
  # Attack until done
  # Do additional fixing
  # End turn, next player goes.



## Game Details

Buildings:
  * Astral Lines (Allows buildings to be connected) (*+*)
  * Castle (Main structure, +50P/turn) (*#*)
  * Village (You can use this as an offensive structure, +5P/turn) (*^*)
  * Gem Block (Can block attacks) (*X*) Pre. Gem Mining
  * Mage Tower (Research skills) (*T*)
  * Storehouse (Allows power storage for later use) (*W*) Pre. Solar Power
 
Note:% Damage is color-coded for buildings

Skills:
  * Basic Magics - Allows attacking (*BM*)
  * Gem Mining - Allows defensive buildings (*GM*)
  * Solar Power - Allows energy storage (*SP*)


### Console Commands:

```
> buy ^,1,2
Buys item and places at those coords

> save 'test1
Saves the current game.
Format:
save '<FILENAME>

> help
Shows command info and game info and symbols

> chat
Mainly used for networking to send a message to the other player. 

> info [game/income/<ITEM>]
game - About the game
income - Shows player`'`s income/turn
<ITEM> - Displays stats about that item (ex "info ^")

> sell ^,4,2
Sells item at those coords

> status 6,8
Prints out info about item at that location
Format:
# - Castle (6,8) [Player 1]
HP: 40/50
Value: $50
Fix Cost: $4/HP
Extra: Lose game if destroyed.

> fix 1,1
Prompts for ix of an item
Format:
Castle`'`s HP: 40/50
Amount (MAX=10)? ___

> attack(atk)  3,1,s
Format:
3,1 - From location at those coords
s - Direction of attack (n,e,s,w)
Output Format:
Power (MAX=15)? ___
ATTACK!!!

Results:
Target HP: 0/15
Power Left: 12
Next Attack: West
--Press ENTER--
// Continues until stopped

> quit
Brutally disconnects from game

> cc player.setMoney(100)
Allows entering of cheat codes or for debugging
Current Codes:
items.fix(x,y,amount)
player.setMoney(1,2000) //(player,amount)
player.setPower(1,20) //(player,amount)

> learn 3,1,GM
Specifies Mage Tower to learn from
then the skill to learn.

> done (attack, turn, or game)
turn - Ends player's turn.
attack - Ends the attacking part of the turn.
game - Surrender/Close game (like quit, but more safe)
```
