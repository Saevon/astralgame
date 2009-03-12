/*
 * Dmitri Amariei (dim3000)
 * MainGame.java (Part of Astral package)
 * The main class of the game Astral, ported to Java w/ Network Gaming added.
 * March 7, 2009
 * (c) Dmitri Amariei and Serghei Fillipov. All Rights Reserved.
 */

package Astral;

import jpb.*;


public class MainGame {
  
  //Shortcut Variables
  final static String nocmd = "Unrecognized Command!";
  final static String cmd = "> ";
  static String red = "";
  static String blue = "";
  static String cyan = "";
  static String gr = "";
  static String prp = "";
  static String cr = "";
  static String yell = "";
  
  public static void main(String[] args) {
    // Sets if colors are enabled (from argument given)
    try {
      if (args[0].equals("color")) {
      System.out.println("COLORS ENABLED!");
      red = AnsiString.RED_ESC;
      blue = AnsiString.BLUE_ESC;
      prp = AnsiString.PURPLE_ESC;
      cyan = AnsiString.CYAN_ESC;
      cr = AnsiString.RESET_ESC;
      yell = AnsiString.YELLOW_ESC;
      gr = AnsiString.GREEN_ESC;
      }
    } catch (Exception ex) {}
    // Displays main game menu and options
    int looper = 0;
    System.out.println(cyan+"\n-A-S-T-R-A-L-"+cr);
    while (looper==0) {
    SimpleIO.prompt(gr+"\nMAIN MENU\n"+
                    "1) Start a new game\n"+
                    "2) View Help\n"+
                    "3) Quit\n"+
                    cmd);
    try {
     int mainchoice = Integer.parseInt(SimpleIO.readLine());
     switch (mainchoice) {
       case 1: setUpGame(); looper=0; break;
       case 2: System.out.println("(Sorry this is not yet implemented)"); sleep(1); break;
       case 3: System.out.println("Thanks for playing!"); System.exit(0);
       default: System.out.println(nocmd); sleep(1); break;
      }
     } catch (Exception ex) { System.out.println(nocmd); sleep(1); }
   }
  }
  
  private static void setUpGame() {
    //Sets up a new game
    int looper = 0;
    while (looper==0) {
    SimpleIO.prompt("\n1) Start a local game\n"+
                    "2) Host a game\n"+
                    "3) Join a game\n"+
                    "4) Go Back\n"+
                    cmd);
    try {
     int typechoice = Integer.parseInt(SimpleIO.readLine());
     switch (typechoice) {
       case 1: System.out.println("Starting A New Game..."); sleep(1); beginGame("local"); looper=1; break;
       case 2: System.out.println("Starting A New Game..."); sleep(1); beginGame("host"); looper=1; break;
       case 3: System.out.println("Joining Game..."); sleep(1); beginGame("join"); looper=1; break;
       case 4: looper=1; break;
       default: System.out.println(nocmd); sleep(1); break;
     }
    }  catch (Exception ex) { System.out.println(nocmd); sleep(1); }
    }
  }
  
  private static void beginGame(String type) {
    //Begins the game
    
    if (type.equals("host")) {
      ServerNet server = new ServerNet();
      server.startHost();
      Mapping map = new Mapping(5,5);
    }
    
    if (type.equals("join")) {
      ClientNet client = new ClientNet();
      client.joinHost();
      Mapping map = new Mapping(5,5);
    } else {
      Mapping map = new Mapping(5,5);
    }
  }
  
  private static void sleep(int seconds) {
    //Quick game sleep method
    try { Thread.sleep(seconds*1000); } catch (Exception ex) {}
  }
}
    