/*
 * Dmitri Amariei (dim3000)
 * Mapping.java (Part of Astral package)
 * Handles drawing of game board and its changes.
 * March 12, 2009
 * (c) Dmitri Amariei and Serghei Fillipov. All Rights Reserved.
 */

package Astral;


// @Dmitri: IGNORE class for now, its a old version (in fact i'll probably delete it)
public class Mapping {
  private int height = 1;
  private int length = 1;
  private int[][] array;
  
  public Mapping() {
    height = 10;
    length = 12;
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
    int c1 = 0;
    int c2 = 0;
    //while (
  }
  
}