/*
 * Dmitri Amariei (dim3000)
 * Stats.java (Part of Astral package)
 * Retrieves all the info about items from data/stats.db
 * March 11, 2009
 * (c) Dmitri Amariei and Serghei Fillipov. All Rights Reserved.
 */

package Astral;

import java.io.*;


public static class Stats {
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
   * max=1       //max amount you may own
   * %           //end of item separator
   * %
   * ...         //next item
   * %
   * #           //end of file
   */
  
}