package AstralG;

/*
 * Dmitri Amariei (dim3000)
 * ColorPane.java (Part of AstralG package)
 * A colored textbox implementtation for the game.
 * April 10, 2009
 * (c) Dmitri Amariei. All Rights Reserved.
 */


import javax.swing.JTextPane;
import java.awt.Color;
import javax.swing.text.AttributeSet;
import javax.swing.text.SimpleAttributeSet;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyleContext;

public class ColorPane extends JTextPane {
  
  public void append(Color c, String s) { 
    StyleContext sc = StyleContext.getDefaultStyleContext();
    AttributeSet aset = sc.addAttribute(SimpleAttributeSet.EMPTY,
        StyleConstants.Foreground, c);
    int len = getDocument().getLength(); 
    setCaretPosition(len); // place caret at the end (with no selection)
    setCharacterAttributes(aset, false);
    replaceSelection(s); // there is no selection, so inserts at caret
  }
  
  public void appendMulti(Color c, String s) { 
    int indexMark = 0;
    String temp[];
    Color partClr;
    int rValue = 0;
    int gValue = 0;
    int bValue = 0;
    if (s.indexOf("java.awt.Color")==-1) {
      append(c, s);
    } else {
      s = s.replace(c.toString(),"1!1");
      while ((s.indexOf("java.awt.Color")!=-1)&&(s.indexOf("1!1")!=-1)) {
        if ((s.indexOf("java.awt.Color")!=0)&&(s.indexOf("1!1")!=0)) {
          append(c,s.substring(0,s.indexOf("java.awt.Color")));
        }
        temp = s.substring(s.indexOf("java.awt.Color"),s.indexOf("1!1")).split("]");
        rValue = Integer.parseInt(temp[0].substring(temp[0].indexOf("r=")+2,temp[0].indexOf("g=")-1));
        gValue = Integer.parseInt(temp[0].substring(temp[0].indexOf("g=")+2,temp[0].indexOf("b=")-1));
        bValue = Integer.parseInt(temp[0].substring(temp[0].indexOf("b=")+2));
        partClr = new Color(rValue,gValue,bValue);
        append(partClr, temp[1]);
        s = s.substring(s.indexOf("1!1")+3);
      }
      append(c, s);
    }
  }
  
}