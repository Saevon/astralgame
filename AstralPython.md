### Introduction ###

The Python version has many features and works on the following OS:
  * Windows systems (color support)

Other to be added once Beta is complete for Windows<br>
Beta is complete, and testing is proceeding.<br>
<br>
<h3>Details</h3>

Features:<br>
<ul><li>Color was added to show Damage<br>
<table><thead><th> Purple  </th><th> Slight Damage   </th><th> 99-66 % </th></thead><tbody>
<tr><td> Red     </td><td> Mediocre Damage </td><td> 65-33 % </td></tr>
<tr><td> Whitish </td><td> Heavy damage    </td><td> 32-0  % </td></tr></li></ul></tbody></table>

Buildings:<br>
<ul><li>Empty Building Location (<b>.</b>)<br>
</li><li>Astral Lines (Allows buildings to be connected) (<b>-</b>) OR (<b>|</b>)<br>
</li><li>Wizards Cottage (Main structure) (<b>W</b>)<br>
</li><li>Village (Minor Mana generator, and attack building) (<b>^</b>)<br>
</li><li>Mining Camp (Better Village, lower HP, Research Gem mining) (<b>M</b>)<br>
</li><li>Void Crystal (Can block attacks, destroys connected Astral lines when hit by attack) (<b>X</b>) Pre. Gem Mining<br>
</li><li>Wall (Defensive Structure, can be built as an AL or as a Building) (<b>W</b>)<br>
Research:<br>
</li><li>ATTACK: Basic Magics - Allows attacking<br>
</li><li>RESEARCH: Gem Mining - Allows Void Crystals buildings, later allows research of other gem types<br>
</li><li>RESEARCH: Resistance Spell - Allows you to raise the resistance of some items.<br>
</li><li>SPECIAL, there are also some upgrades to buildings that can be done in the stats menu<br>
Console Commands:<br>
</li><li>() means that this is optional</li></ul>

> build (Name)<br>
Goes into build menu, leading you through the building process, also allows viewing of these structure<code>'</code>s statistics.<br>
By typing "continue" when choosing where to place it you can keep building by just typing the location, if you have enough mana<br>
<br>

> ally(+ Name)<br>
(<b>-</b>) Cancel Alliance with Name<br>
(<b>+</b>) Start Alliance with Name,br.<br>
When no optionals are given it goes into a menu to show alliances, and change them.<br>
<br>

> tribute (player amount)<br>
Send Mana to a player<br>
<br>

> fix x,y (amount)<br>
Fixes the building at x,y by the amount, if possible.<br>
'max' may be used as an amount<br>
This can also be done in the stats menu<br>
<br>

> sell x,y<br>
Sells the building at x,y.<br>
This can also be done in the stats menu<br>
<br>

> stats x,y<br>
Shows the building's stats<br>
This menu also allows:<br>
-> Fixing<br>
-> Upgrading the Building<br>
-> Selling<br>
<br>

> income<br>
Shows your income, with all the buildings that give you mana.<br>
<br>

> research (Name)<br>
researches the item if possible<br>
<br>

> attack (Name)<br>
Goes into the attacks menu, and shows possible attacks. Specify the direction and other details for the attack in this menu.<br>
<br>

> save (filename)<br>
lets you save the game, if filename is not specified, it saves on the auto save.<br>
<br>

> load (filename)<br>
lets you load the game, if filename is not specified, it loads the auto save.<br>
<br>

> help (item)<br>
Shows command info and game info and symbols<br>
(Currently not tested and not detailed, will be last part of Beta)<br>
<br>

> surrender<br>
Leave the game, you are considered dead, but can still win in terms of score.<br>
<br>

> quit<br>
> exit<br>
> q<br>
Disconnects from game<br>
<br>

> ~<br>
Goes into console, allows execution of typed data as python script. <br>
This will be removed later, and cheatcodes added instead. (Cheats ?? Maybe)<br>
<br>

> done<br>
> end turn<br>
Ends player's turn.<br><br>
<br>
<hr />
<br>
<h3>Ideas for Technology</h3>

<ul><li>Send any ideas you have to blastowind@gmail.com, they will be viewed and could potentially be added<br>
<br>
--> NEW ATTACKS:<br>
</li><li>Arrow Hail: choose two points, and all buldings within these points have a chance of being hit, damages allied buildings<br>
</li><li>Poison Magics: Like Basic Magics, but does little damage, makes landscape hit ( only enemy buildings are hit ) poisoned. This last for a while, even if you capture the building.