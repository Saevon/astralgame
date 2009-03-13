/*
 * Dmitri Amariei (dim3000)
 * Mapping.java (Part of Astral package)
 * Handles drawing of game board and its changes.
 * March 12, 2009
 * (c) Dmitri Amariei and Serghei Fillipov. All Rights Reserved.
 */

package Astral;


public class Mapping {
  /*
   * The array stores numbers corrresponding to items
   * Format:
   * blank = 0
   * + = 1
   * # = 2
   * ^ = 3
   */
  
  private int height = 1;
  private int length = 1;
  private int[][] array;
  
  public Mapping() {
    height = 15;
    length = 15;
    array = new int[length][height];
    newMap();
  }
  
  public Mapping(int length, int height) {
    this.height = height;
    this.length = length;
    array = new int[length][height];
    newMap();
  }
  
  private void newMap() {
    // Draws out initial map from the array
    int ch = 1;
    int cl = 1;
    while (ch<=height) {
      while (cl<=length) {
        array[cl-1][ch-1] = 0;
        cl++;
      }
      cl = 1;
      ch++;
    }
  }
  
  public void addItem(int x, int y, String symbol) {
    //Adds an item to array
    int itemtype = 0;
    if (symbol.equals("+")) {
      itemtype = 1;
    } else if (symbol.equals("#")) {
      itemtype = 2;
    } else if (symbol.equals("V")) {
      itemtype = 3;
    }
    array[x-1][y-1] = itemtype;
  }
  
  public void redraw() {
    //Re-draw the map
    int ch = 1;
    int cl = 1;
    boolean ci = true;
    System.out.print("\n");
    while (ch<=height) {
      if (ch<10) {
    System.out.print(ch);
      } else {
        System.out.print(Integer.toString(ch).substring(1,2));
      }
      while (cl<=length) {
        System.out.print(" ");
        switch (array[cl-1][ch-1]) {
          case 1: if (ci) { System.out.print("+"); ci = false; } else { System.out.print("+"); ci = true; } break;
          case 2: if (ci) { System.out.print("#"); ci = false; } else { System.out.print("#"); ci = true; } break;
          case 3: if (ci) { System.out.print("^"); ci = false; } else { System.out.print("^"); ci = true; } break;
          default: if (ci) { System.out.print("o"); ci = false; } else { System.out.print(" "); ci = true; } break;
        }
        cl++;
      }
      ci = true;
       cl = 1;
      System.out.println();
      ch++;
    }
    System.out.print("  ");
    for (int lnum = 1; lnum<=length; lnum++) {
      if (lnum<10) {
    System.out.print(lnum+" ");
      } else {
        System.out.print(Integer.toString(lnum).substring(1,2)+" ");
      }
    }
    System.out.println();
  }
  
}