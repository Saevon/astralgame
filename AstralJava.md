### Introduction ###

The Java version has many features and works on the following OS:
  * All UNIX based systems
  * Apple Macs and iPod Touch/iPhone (iPhoneOS)
  * Windows systems



### General Gameplay ###

Astral is turn-based and therefore follows a turn order
and allows the following actions (in order):
  1. Get income and power
  1. Build, fix, or sell
  1. Attack until done
  1. Do additional fixing
  1. End turn, next player goes.



### Game Details ###

Buildings:
  * Astral Lines (Allows buildings to be connected) (**+**)
  * Castle (Main structure, +50P/turn) (**#**)
  * Village (You can use this as an offensive structure, +5P/turn) (**^**)
  * Gem Block (Can block attacks) (**X**) Pre. Gem Mining
  * Mage Tower (Research skills) (**T**)
  * Storehouse (Allows power storage for later use) (**W**) Pre. Solar Power<br>
Note:% Damaged is color-coded for buildings</li></ul>

Skills:<br>
<ul><li>Basic Magics - Allows attacking (<b>BM</b>)<br>
</li><li>Gem Mining - Allows defensive buildings (<b>GM</b>)<br>
</li><li>Solar Power - Allows energy storage (<b>SP</b>)<br>
Console Commands:<br>
<pre><code>&gt; buy ^,1,2<br>
Buys item and places at those coords<br>
<br>
&gt; save 'test1<br>
Saves the current game.<br>
Format:<br>
save '&lt;FILENAME&gt;<br>
<br>
&gt; help<br>
Shows command info and game info and symbols<br>
<br>
&gt; chat<br>
Mainly used for networking to send a message to the other player. <br>
<br>
&gt; info [game/income/&lt;ITEM&gt;]<br>
game - About the game<br>
income - Shows player`'`s income/turn<br>
&lt;ITEM&gt; - Displays stats about that item (ex "info ^")<br>
<br>
&gt; sell ^,4,2<br>
Sells item at those coords<br>
<br>
&gt; status 6,8<br>
Prints out info about item at that location<br>
Format:<br>
# - Castle (6,8) [Player 1]<br>
HP: 40/50<br>
Value: $50<br>
Fix Cost: $4/HP<br>
Extra: Lose game if destroyed.<br>
<br>
&gt; fix 1,1<br>
Prompts for ix of an item<br>
Format:<br>
Castle`'`s HP: 40/50<br>
Amount (MAX=10)? ___<br>
<br>
&gt; attack(atk)  3,1,s<br>
Format:<br>
3,1 - From location at those coords<br>
s - Direction of attack (n,e,s,w)<br>
Output Format:<br>
Power (MAX=15)? ___<br>
ATTACK!!!<br>
<br>
Results:<br>
Target HP: 0/15<br>
Power Left: 12<br>
Next Attack: West<br>
--Press ENTER--<br>
// Countines until stopped<br>
<br>
&gt; quit<br>
Brutally disconnects from game<br>
<br>
&gt; cc player.setMoney(100)<br>
Allows entering of cheat codes or for debugging<br>
Current Codes:<br>
items.fix(x,y,amount)<br>
player.setMoney(1,2000) //(player,amount)<br>
player.setPower(1,20) //(player,amount)<br>
<br>
&gt; learn 3,1,GM<br>
Specifies Mage Tower to learn from<br>
then the skill to learn.<br>
<br>
&gt; done (attack, turn, or game)<br>
turn - Ends player's turn.<br>
attack - Ends the attacking part of the turn.<br>
game - Surrender/Close game (like quit, but more safe)<br>
</code></pre>