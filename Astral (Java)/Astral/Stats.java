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
  
  public static String getMaxHP(String symbol) {
    //Gets max HP of item
    return readStats(symbol,"HP");
  }
  
  public static String getCost(String symbol) {
    //Gets cost of item
    return readStats(symbol,"cost");
  }
  
  public static String getFixCost(String symbol) {
    //Gets name of item
    return readStats(symbol,"fixcost");
  }
  
  public static String getValue(String symbol) {
    //Gets value of item
    return readStats(symbol,"value");
  }
  
  public static String getExtraInfo(String symbol) {
    //Gets name of item
    return readStats(symbol,"extra");
  }
  
  public static String getMax(String symbol) {
    //Gets max allowed of item
    return readStats(symbol,"max");
  }
  
  private static String readStats(String symbol, String type) {
    //Reads data/stats.db to get properties
    String spr = System.getProperty("path.separator");
    try {
        BufferedReader in = new BufferedReader(new FileReader(spr+"data"+spr+"stats.db"));
        String str;
        while (((str = in.readLine()).indexOf(symbol))==-1) {
        }
        while (((str = in.readLine()).indexOf(type))==-1) {
        }
        in.close();
        return str.substring(str.indexOf("="+1));
    } catch (IOException e) {
      System.out.println("ERROR READING FILE");
      System.exit(-1);
    }
  }
  
}