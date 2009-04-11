package AstralG;


import java.awt.*;
import javax.swing.*;

public class Test1 {
  public static void main(String[] args) {
    ColorPane pane = new ColorPane();
    Color cr = new Color(193,151,0);
    //java.awt.Color[r=193,g=151,b=0]
    pane.appendMulti(cr, "1 java.awt.Color[r=255,g=255,b=0]#java.awt.Color[r=193,g=151,b=0]   o   o   o Quick Stats:\n"+
"2               P1 $50\n"+
"\n3 o   o   o   o P2 $50\n"+
"4              \n"+
"5 o   o   o   java.awt.Color[r=193,g=151,b=0]java.awt.Color[r=255,g=175,b=175]#java.awt.Color[r=193,g=151,b=0]\n"+
"  1 2 3 4 5 6 7 \n"+
"(Current Player: 1)");

    JFrame f = new JFrame("ColorPane example");
    f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    f.setContentPane(new JScrollPane(pane));
    f.setSize(600, 400);
    f.setVisible(true);
  }
  
  public static boolean isPrime(int n) {
    if (n < 2)
      return false;
    double max = Math.sqrt(n);
    for (int j = 2; j <= max; j += 1)
      if (n % j == 0)
        return false; // j is a factor
    return true;
  }

  public static boolean isPerfectSquare(int n) {
    int j = 1;
    while (j * j < n && j * j > 0)
      j += 1;
    return (j * j == n);
  }
}