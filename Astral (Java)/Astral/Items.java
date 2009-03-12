/*
 * Dmitri Amariei (dim3000)
 * Items.java (Part of Astral package)
 * Handles and stores the data of all the items on the map.
 * March 12, 2009
 * (c) Dmitri Amariei and Serghei Fillipov. All Rights Reserved.
 */

package Astral;

import java.io.*;


public class Items {
  /*
   * Item data is stored in \data\items.db
   * The format is:
   * e.x 0,1;#,1,15
   * 0 - x-coord
   * 1 - y-coord
   * ; - separator (default)
   * # - symbol
   * 1 - Belongs to... (Player 1)
   * 15 - current HP
   * (All other stats are stored in this class itself)
   */
  
  public void new(int x, int y, String symbol, int player, int hp) {
    //Creats a new item
    String text = Convert.toString(x)+","+Convert.toString(y)+";"+symbol+
                  ","+Convert.toString(player)+","+Convert.toString(hp);
    write(x, y, text);
  }
  
  public String getItem(int x, int y) {
    //Gets symbol of item at the coords
    return read(x,y,"symbol");
  }
  
  public String getInfo(x,y) {
    //Returns a formatted string with info about an item
    String itemname = Stats.getName(getItem(x,y));
    String maxhp = Convert.toString(Stats.getMaxHP(getItem(x,y)));
    String value = Convert.toString(Stats.getValue(getItem(x,y)));
    String fixcost = Convert.toString(Stats.getFixCost(getItem(x,y)));
    String extra = Stats.getExtraInfo(getItem(x,y));
    String text1 =  "\n"+getItem(x,y)+" - "+itemname+" ("+
                    Convert.toString(x)+","+Convert.toString(y)+
                    ") [Player "+getPlayer(x,y)+"]\n";
    String text2 = "HP: "+getHP(x,y)+"/"+maxhp+"/n";
    String text3 = "Value: $"+value;
    String text4 = "/nFix Cost: $"+fixcost+"/HP\n";
    String text5 = "Extra: "+extra;
    return text1+text2+text3+text4+text5;
  }
  
  public void delete(int x, int y) {
    //Deletes an item at the coords
    write(x,y,"erase");
  }
  
  public void fix(int x, int y, int amount) {
    //Changes the HP of an item. Amount may be negative
    //to decrease HP (i.e got attacked)
    int hp = getHP(x,y) + amount;
    String text = Convert.toString(x)+","+Convert.toString(y)+";"+getItem(x,y)+
                  ","+getPlayer(x,y)+","+Convert.toString(hp);
    write(x, y, text);
  }
  
  public int getHP(int x, int y) {
    //Returns the HP of the item.
    return Integer.parseInt(read(x,y,"HP"));
  }
  
  public boolean isItem(int x, int y) {
    //Checks whether there is an item at he coords
    String text = getItem(x,y);
    if (text.equals("na")) {
      return false;
    } else {
      return true;
    }
  }
  
  public String getPlayer(int x, int y) {
    //Gets the owner of the item
    return read(x,y,"player");
  }
  
  private void write(int x, int y, String info) {
    //Writes data about an item to data/items.db
    if (info.equals("erase")) {
      //Erase data from file
      
    } else {
      //Replace data in file
      
    }
  }
  
  private String read(int x, int y, String type) {
    //Reads data about an item from data/items.db
    //Type can be "HP", "player", "symbol", "all"
    //Note: returns "na" if no item is found
    return null;
  }
  
}