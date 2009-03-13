/*
 * Dmitri Amariei (dim3000)
 * Mapping.java (Part of Astral package)
 * Handles drawing of game board and its changes.
 * March 12, 2009
 * (c) Dmitri Amariei and Serghei Fillipov. All Rights Reserved.
 */

package Astral;


public class Mapping {
  private int height = 1;
  private int length = 1;
  private int[][] array;
  
  public Mapping() {
    height = 15;
    length = 15;
    array = new int[length][height];
    drawMap();
  }
  
  public Mapping(int height, int length) {
    this.height = height;
    this.length = length;
    array = new int[length][height];
    drawMap();
  }
  
  private void drawMap() {
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
    redraw();
  }
  
  public void redraw() {
    //Re-draw the map
    int ch = 1;
    int cl = 1;
    boolean ci = true;
    System.out.print("\n");
    while (ch<=height) {
      while (cl<=length) {
        switch (array[cl-1][ch-1]) {
          case 0: if (ci) { System.out.print("o"); ci = false; } else { System.out.print(" "); ci = true; } break;
        }
        cl++;
      }
       cl = 1;
      System.out.println();
      ch++;
    }
    for (int lnum = 1; lnum<=length; lnum++) {
    System.out.print(lnum);
    }
    System.out.println();
  }
  
}