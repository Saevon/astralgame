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
   * e.x 0'1;#,1,15
   * 0 - x-coord
   * 1 - y-coord
   * ; - separator (default)
   * # - symbol
   * 1 - Belongs to... (Player 1)
   * 15 - current HP
   * (All other stats are stored in this class itself)
   */
  
  public void create(int x, int y, String symbol, int player, int hp) {
    //Creats a new item
    String text = Integer.toString(x)+"'"+Integer.toString(y)+";"+symbol+
                  ","+Integer.toString(player)+","+Integer.toString(hp);
    write(x, y, text);
  }
  
  public String getItem(int x, int y) {
    //Gets symbol of item at the coords
    return read(x,y,"symbol");
  }
  
  public String getInfo(int x, int y) {
    //Returns a formatted string with info about an item
    String itemname = Stats.getName(getItem(x,y));
    String maxhp = Integer.toString(Stats.getMaxHP(getItem(x,y)));
    String value = Integer.toString(Stats.getValue(getItem(x,y)));
    String fixcost = Integer.toString(Stats.getFixCost(getItem(x,y)));
    String income = Integer.toString(Stats.getIncome(getItem(x,y)));
    String extra = Stats.getExtraInfo(getItem(x,y));
    String text1 =  "\n"+getItem(x,y)+" - "+itemname+" ("+
                    Integer.toString(x)+","+Integer.toString(y)+
                    ") [Player "+getPlayer(x,y)+"]\n";
    String text2 = "HP: "+getHP(x,y)+"/"+maxhp+"\n";
    String text3 = "Value($): "+value;
    String text4 = "\nFix Cost($): "+fixcost+"/HP";
    String text5 = "\nIncome($): "+income;
    String text6 = "\nExtra: "+extra;
    return text1+text2+text3+text4+text5+text6;
  }
  
  public void delete(int x, int y) {
    //Deletes an item at the coords
    write(x,y,"erase");
  }
  
  public void fix(int x, int y, int amount) {
    //Changes the HP of an item. Amount may be negative
    //to decrease HP (i.e got attacked)
    int hp = getHP(x,y) + amount;
    String text = Integer.toString(x)+","+Integer.toString(y)+";"+getItem(x,y)+
                  ","+getPlayer(x,y)+","+Integer.toString(hp);
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
  
  public int getPlayer(int x, int y) {
    //Gets the owner of the item
    return Integer.parseInt(read(x,y,"player"));
  }
  
  private void write(int x, int y, String info) {
    //Writes data about an item to data/items.db
    try {
      String str;
      long tmp = 0;
    String spr = System.getProperty("file.separator");
    String dir = System.getProperty("user.dir")+spr+"Astral";
    RandomAccessFile in = new RandomAccessFile(new File(dir+spr+"data"+spr+"items.db"), "rw");
    try {
    tmp = in.getFilePointer() + 1;
    str = in.readLine();
    while ((str.indexOf(x+"'"+y))==-1) {
      tmp = in.getFilePointer() + 1;
      str = in.readLine();
    }
    } catch (Exception ex) {
        str = "";
      }
    String spaces = "";
    int count1 = 1;
    while (spaces.length()<str.length()) {
      spaces = spaces + " ";
    }
    if (tmp!=0) {
      tmp=tmp-1;
    }
    if (info.equals("erase")) {
      //Erase data from file
      in.seek(tmp);
      in.writeBytes(spaces);
    } else {
      //Replace data in file
      in.seek(tmp);
      in.writeBytes(spaces);
      while (((str = in.readLine()))!=null) {
    }
      in.writeBytes("\n"+info);
    }
      in.close();
    } catch (Exception e) {
      System.out.println("ERROR READING FILE");
      e.printStackTrace();
      System.exit(-1);
    }
  }
  
  private String read(int x, int y, String type) {
    //Reads data about an item from data/items.db
    //Type can be "HP", "player", "symbol", "all"
    //Note: returns "na" if no item is found
    String value = "na";
    String str = "";
    try {
    String spr = System.getProperty("file.separator");
    String dir = System.getProperty("user.dir")+spr+"Astral";
    RandomAccessFile in = new RandomAccessFile(new File(dir+spr+"data"+spr+"items.db"), "rw");
    try {
    while (((str = in.readLine()).indexOf(x+"'"+y))==-1) {
    }
    if (type.equals("HP")) {
      value = str.substring(str.lastIndexOf(",")+1);
    } else if (type.equals("player")) {
      value = str.substring(str.indexOf(";")+3, str.lastIndexOf(";")+4);
    } else if (type.equals("symbol")) {
      value = str.substring(str.lastIndexOf(";")+1,str.lastIndexOf(";")+2);
    } else {
      value = str;
    }
    } catch (NullPointerException nex) {
    }
    in.close();
    } catch (Exception ex) {
      System.out.println("ERROR READING FILE(Called by:Items)");
      ex.printStackTrace();
      System.exit(-1);
    }
    return value;
  }
  
}