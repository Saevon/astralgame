/*
 * Dmitri Amariei (dim3000)
 * Stats.java (Part of Astral package)
 * Retrieves all the info about items from data/stats.db
 * March 11, 2009
 * (c) Dmitri Amariei and Serghei Fillipov. All Rights Reserved.
 */

package Astral;

import java.io.*;


public class Stats {
  /*
   * All stats can be found and edited in data/stats.db
   * Format:
   * @           //start of file
   * %           //start of item separator
   * name=Castle //name of new item
   * symbol=#    //item's symbol on map
   * HP=50       //max hp value of item
   * cost=-1     //price to buy item (below zero is infinite)
   * fixcost=5   //cost to fix one hp of item
   * value=-1    //sell price of item (below zero, can't be sold)
   * max=1       //max amount you may own (Zero, infinite)
   * extra="LOL" //Extra Info
   * %           //end of item separator
   * %
   * ...         //next item
   * %
   * #           //end of file
   */
  
  public static String getName(String symbol) {
    //Gets name of item
    return readStats(symbol,"name");
  }
  
  public static int getMaxHP(String symbol) {
    //Gets max HP of item
    return Integer.parseInt(readStats(symbol,"HP"));
  }
  
  public static int getCost(String symbol) {
    //Gets cost of item
    return Integer.parseInt(readStats(symbol,"cost"));
  }
  
  public static int getFixCost(String symbol) {
    //Gets name of item
    return Integer.parseInt(readStats(symbol,"fixcost"));
  }
  
  public static int getValue(String symbol) {
    //Gets value of item
    return Integer.parseInt(readStats(symbol,"value"));
  }
  
  public static String getExtraInfo(String symbol) {
    //Gets name of item
    return readStats(symbol,"extra");
  }
  
  public static int getMax(String symbol) {
    //Gets max allowed of item
    return Integer.parseInt(readStats(symbol,"max"));
  }
  
  private static String readStats(String symbol, String type) {
    //Reads data/stats.db to get properties
    String spr = System.getProperty("file.separator");
    String dir = System.getProperty("user.dir")+spr+"Astral";
    String str = "";
    try {
        BufferedReader in = new BufferedReader(new FileReader(new File(dir+spr+"data"+spr+"stats.db")));
        while (((str = in.readLine()).indexOf(symbol))==-1) {
        }
        while (((str = in.readLine()).indexOf(type))==-1) {
        }
        in.close();
        return str.substring(str.indexOf("=")+1);
    } catch (Exception e) {
      System.out.println("ERROR READING FILE(Called by:Stats)");
      System.exit(-1);
    }
    return null;
  }
  
}