/*
 * Dmitri Amariei (dim3000)
 * MainGame.java (Part of Astral package)
 * The main class of the game Astral, ported to Java w/ Network Gaming added.
 * March 7, 2009
 * (c) Dmitri Amariei and Serghei Fillipov. All Rights Reserved.
 */

package Astral;

import jpb.*;
import java.io.File;


public class MainGame {
  
  //Shortcut Variables
  final static String nocmd = "Unrecognized Command!";
  final static String cmd = "> ";
  static String red = "";
  static String blue = "";
  static String attclr = "";
  static String gr = "";
  static String prp = "";
  static String cr = "";
  static String yell = "";
  static String pink = "";
  static Players players;
  static Items items;
  /* The array stores numbers corrresponding to items
   * Format:
   * blank = 0
   * + = 1
   * # = 2
   * ^ = 3
   */
  static int height = 9;
  static int length = 9;
  static int[][] array;
  static int curplayer = 1;
  static int turnphase = 4;
  static int startmoney = 150;
  
  public static void main(String[] args) {
    // Sets if colors are enabled (from argument given)
    try {
      if (args[0].equals("color")) {
      System.out.println("COLORS ENABLED!");
      red = AnsiString.RED_ESC;
      blue = AnsiString.BLUE_ESC;
      prp = AnsiString.PURPLE_ESC;
      attclr = "\033[1;46m";
      cr = AnsiString.RESET_ESC;
      yell = AnsiString.YELLOW_ESC;
      gr = AnsiString.GREEN_ESC;
      pink = "\033[1;35m";
      }
    } catch (Exception ex) {}
    // Displays main game menu and options
    int looper = 0;
    System.out.println("\n-A-S-T-R-A-L-");
    while (looper==0) {
    SimpleIO.prompt("\nMAIN MENU\n"+
                    "1) Start a new game\n"+
                    "2) View Help\n"+
                    "3) Set Map Size\n"+
                    "4) Set Money\n"+
                    "5) Quit\n"+
                    cmd);
    try {
     int mainchoice = Integer.parseInt(SimpleIO.readLine());
     String ms;
     switch (mainchoice) {
       case 1: setUpGame(); looper=0; break;
       case 2: System.out.println("(Sorry this is not yet implemented)"); sleep(1); break;
       case 3: SimpleIO.prompt("Map Size(x,y)? "); ms = SimpleIO.readLine(); length = Integer.parseInt(ms.substring(0,ms.indexOf(","))); height = Integer.parseInt(ms.substring(ms.indexOf(",")+1)); break;
       case 4: SimpleIO.prompt("Starting Money? "); startmoney = Integer.parseInt(SimpleIO.readLine()); break;
       case 5: System.out.println("Thanks for playing!"); System.exit(0);
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
    }  catch (Exception ex) { System.out.println(nocmd); }
    }
  }
  
  private static void beginGame(String type) {
    //Begins the game
    if (type.equals("host")) {
      SimpleIO.prompt("Port? ");
      int sport = Integer.parseInt(SimpleIO.readLine());
      ServerNet server = new ServerNet(sport);
      array = new int[length][height];
      newMap();
      players = new Players("Player1", "Player2", startmoney, 0);
      items = new Items();
      String spr = System.getProperty("file.separator");
      String dir = System.getProperty("user.dir")+spr+"Astral";
      try {
      Runtime.getRuntime().exec("chmod 755 " + dir+spr+"data"+spr+"items.db");
      } catch (Exception ex) {
      }
      new File(dir+spr+"data"+spr+"items.db").delete();
      items.create(1,1,"#",1,Stats.getMaxHP("#"));
      items.create(length,height,"#",2,Stats.getMaxHP("#"));
      addItem(1,1,"#");
      addItem(length,height,"#");
      while (true==true) {
        String tosend = localTasks("na");
        server.sendData(tosend);
        localTasks(server.getReply());
      }
      
    } else if (type.equals("join")) {
      SimpleIO.prompt("Server's Name? ");
      String sname = SimpleIO.readLine();
      SimpleIO.prompt("Port? ");
      int sport = Integer.parseInt(SimpleIO.readLine());
      ClientNet client = new ClientNet(sname, sport);
      array = new int[length][height];
      newMap();
      players = new Players("Player1", "Player2", startmoney, 0);
      items = new Items();
      String spr = System.getProperty("file.separator");
      String dir = System.getProperty("user.dir")+spr+"Astral";
      try {
      Runtime.getRuntime().exec("chmod 755 " + dir+spr+"data"+spr+"items.db");
      } catch (Exception ex) {
      }
      new File(dir+spr+"data"+spr+"items.db").delete();
      items.create(1,1,"#",1,Stats.getMaxHP("#"));
      items.create(length,height,"#",2,Stats.getMaxHP("#"));
      addItem(1,1,"#");
      addItem(length,height,"#");
      while (true==true) {
        localTasks(client.getReply());
        String tosend = localTasks("na");
        client.sendData(tosend);
      }
      
    } else {
      array = new int[length][height];
      newMap();
      players = new Players("Player1", "Player2", startmoney, 0);
      items = new Items();
      String spr = System.getProperty("file.separator");
      String dir = System.getProperty("user.dir")+spr+"Astral";
      try {
      Runtime.getRuntime().exec("chmod 755 " + dir+spr+"data"+spr+"items.db");
      } catch (Exception ex) {
      }
      new File(dir+spr+"data"+spr+"items.db").delete();
      items.create(1,1,"#",1,Stats.getMaxHP("#"));
      items.create(length,height,"#",2,Stats.getMaxHP("#"));
      addItem(1,1,"#");
      addItem(length,height,"#");
      while (true==true) {
        localTasks("na");
      }
    }
  }
  
  private static String localTasks(String netcmd) {
    /* Does all the tasks required each turn
     * Format:
     * 1) Draw Map and CMD prompt
     * 2) Checks entered command
     * 3) Executes command
     * 4) Checks to see if won
     * 5) Re-Draws Map and CMD prompt
     */
    String usercmd = "";
    try {
    if (turnphase==4) {
    players.addMoney(curplayer,calcIncome());
    turnphase=1;
    }
    redraw(false,0,0);
    if (netcmd.equals("na")) {
    SimpleIO.prompt("\n"+cmd);
    usercmd = SimpleIO.readLine();
    } else {
      SimpleIO.prompt("\nResponse: "+netcmd);
    SimpleIO.readLine();
    usercmd = netcmd;
    }
    boolean allowed = cmdCheck(usercmd);
    if (allowed) {
      cmdRun(usercmd);
    }
    if (!items.isItem(1,1)) {
      System.out.println(pink+"\n\nPlayer 2 has won!!!"+cr);
      System.exit(0);
    }
    if (!items.isItem(length,height)) {
      System.out.println(yell+"\n\nPlayer 1 has won!!!"+cr);
      System.exit(0);
    }
    } catch (Exception ex) {
      System.out.println(nocmd);
    }
    return usercmd;
  }
  
  
  private static boolean cmdCheck(String uc) {
    //Checks if command is allowed
    boolean result = false;
    String tempsymbol = "";
    if (uc.indexOf("buy")!=-1) {
      if (turnphase == 1) {
        int xcoord = 0;
    int ycoord = 0;
        try {
      tempsymbol = uc.substring(uc.indexOf(",")-1,uc.indexOf(","));
      xcoord = Integer.parseInt(uc.substring(uc.indexOf(",")+1,uc.lastIndexOf(",")));
      ycoord = Integer.parseInt(uc.substring(uc.lastIndexOf(",")+1));
        } catch (Exception ex) {
          tempsymbol = "+";
          xcoord = Integer.parseInt(uc.substring(uc.indexOf(",")-1,uc.indexOf(",")));
          ycoord = Integer.parseInt(uc.substring(uc.lastIndexOf(",")+1));
        }
      int cost = Stats.getCost(tempsymbol);
      if ( (tempsymbol.equals("+")) || ((xcoord%2==1)&&(ycoord%2==1)) ) {
      if ((cost!=-1)&&(cost<=players.getMoney(curplayer))) {
        result = true;
      } else {
        System.out.println(cr+red+"Not enough money!"+cr);
      }
      if (items.isItem(xcoord,ycoord)) {
        System.out.println(cr+red+"Item already there!"+cr);
        result = false;
      }
      } else {
        System.out.println(cr+red+"Cant't be placed there!"+cr);
      }
      } else {
        System.out.println(cr+red+"No building during this phase!"+cr);
      }
    } else if (uc.indexOf("quit")!=-1) {
      result = true;
    } else if (uc.indexOf("exit")!=-1) {
      result = true;
    } else if (uc.indexOf("help")!=-1) {
      result = true;
    } else if (uc.indexOf("sell")!=-1) {
      if (turnphase == 1) {
      int xcoord = Integer.parseInt(uc.substring(uc.indexOf(",")-1,uc.lastIndexOf(",")));
      int ycoord = Integer.parseInt(uc.substring(uc.lastIndexOf(",")+1));
      if (items.isItem(xcoord,ycoord)) {
        int value = Stats.getValue(items.getItem(xcoord,ycoord));
        if (curplayer==items.getPlayer(xcoord,ycoord)) {
        if (value!=-1) {
        result = true;
        } else {
        System.out.println(cr+red+"Can't be sold!"+cr);
        sleep(0.8);
      }
      } else {
        System.out.println(cr+red+"Not your item!"+cr);
      }
      } else {
        System.out.println(cr+red+"No item found!"+cr);
        sleep(0.8);
      }
      } else {
        System.out.println(cr+red+"No selling during this phase!"+cr);
        sleep(0.8);
      }
    } else if (uc.indexOf("status")!=-1) {
      int xc = Integer.parseInt(uc.substring(uc.indexOf(",")-1,uc.lastIndexOf(",")));
      int yc = Integer.parseInt(uc.substring(uc.lastIndexOf(",")+1));
      if (items.isItem(xc,yc)) {
      result = true;
      } else {
        System.out.println(red+"No item found!"+cr);
        sleep(0.8);
      }
    } else if (uc.indexOf("done")!=-1) {
      result = true;
    } else if (uc.indexOf("fix")!=-1) {
      if (turnphase!=2) {
      int xc = Integer.parseInt(uc.substring(uc.indexOf(",")+1,uc.lastIndexOf(",")));
      int yc = Integer.parseInt(uc.substring(uc.lastIndexOf(",")+1));
      int maxhp = Stats.getMaxHP(items.getItem(xc,yc));
      int curhp = items.getHP(xc,yc);
      if (curplayer==items.getPlayer(xc,yc)) {
      if (curhp<maxhp) {
        result = true;
      } else {
        System.out.println(red+"Item's HP is already full!"+cr);
        sleep(0.8);
      }
      } else {
        System.out.println(cr+red+"Not your item!"+cr);
      }
      } else {
        System.out.println(red+"No fixing during this phase!"+cr);
        sleep(0.8);
      }
    } else if (uc.indexOf("done")!=-1) {
      result = true;
    } else if ((uc.indexOf("attack")!=-1)||(uc.indexOf("atk")!=-1)) {
      int xc = Integer.parseInt(uc.substring(uc.indexOf(",")-1,uc.indexOf(",")));
      int yc = Integer.parseInt(uc.substring(uc.indexOf(",")+1,uc.lastIndexOf(",")));
      if (curplayer==items.getPlayer(xc,yc)) {
      if (turnphase!=3) {
      result = true;
      } else {
        System.out.println(red+"You have finished attacking!"+cr);
        sleep(0.8);
      } 
      } else {
        System.out.println(cr+red+"Not your item!"+cr);
      }
    } else {
      System.out.println(nocmd);
      sleep(0.8);
    }
    return result;
  }
  
  private static void cmdRun(String uc) {
    //Executes specified command
    if (uc.indexOf("buy")!=-1) {
      String sym = "";
      int xcoord = 0;
      int ycoord = 0;
      try {
      sym = uc.substring(uc.indexOf(",")-1,uc.indexOf(","));
      xcoord = Integer.parseInt(uc.substring(uc.indexOf(",")+1,uc.lastIndexOf(",")));
      ycoord = Integer.parseInt(uc.substring(uc.lastIndexOf(",")+1));
        } catch (Exception ex) {
          sym = "+";
          xcoord = Integer.parseInt(uc.substring(uc.indexOf(",")-1,uc.indexOf(",")));
          ycoord = Integer.parseInt(uc.substring(uc.lastIndexOf(",")+1));
        }
      int cost = Stats.getCost(sym);
      players.addMoney(curplayer, -cost);
      addItem(xcoord,ycoord,sym);
      items.create(xcoord,ycoord,sym,curplayer,Stats.getMaxHP(sym));
      System.out.println("Bought!");
      sleep(0.8);
    } else if (uc.indexOf("quit")!=-1) {
      System.out.println("Brutally Disconnecting...");
      System.exit(0);
    } else if (uc.indexOf("exit")!=-1) {
      System.out.println("Brutally Disconnecting...");
      System.exit(0);
    } else if (uc.indexOf("help")!=-1) {
      System.out.println("(Sorry, not yet implemented)");
      sleep(0.8);
    } else if (uc.indexOf("sell")!=-1) {
      int xcoord = Integer.parseInt(uc.substring(uc.indexOf(",")-1,uc.lastIndexOf(",")));
      int ycoord = Integer.parseInt(uc.substring(uc.lastIndexOf(",")+1));
      int value = Stats.getValue(items.getItem(xcoord,ycoord));
      String sym = items.getItem(xcoord,ycoord);
      players.addMoney(curplayer, value);
      addItem(xcoord,ycoord,"d");
      items.delete(xcoord,ycoord);
      System.out.println("Sold!");
      sleep(0.8);
    } else if (uc.indexOf("status")!=-1) {
      int xcoord = Integer.parseInt(uc.substring(uc.indexOf(",")-1,uc.indexOf(",")));
      int ycoord = Integer.parseInt(uc.substring(uc.indexOf(",")+1));
      int owner = items.getPlayer(xcoord,ycoord);
      if (owner==1) {
      System.out.println(yell+items.getInfo(xcoord,ycoord)+cr);
      } else {
        System.out.println(pink+items.getInfo(xcoord,ycoord)+cr);
      }
      SimpleIO.prompt("(Press Enter)");
      SimpleIO.readLine();
    } else if (uc.indexOf("done")!=-1) {
      if (uc.indexOf("attack")!=-1) {
        turnphase = 3;
      } else if (uc.indexOf("turn")!=-1) {
        turnphase = 4;
        if (curplayer==1) {
          curplayer = 2;
        } else {
          curplayer = 1;
        }
      }
    } else if (uc.indexOf("fix")!=-1) {
      int xc = Integer.parseInt(uc.substring(uc.indexOf(",")+1,uc.lastIndexOf(",")));
      int yc = Integer.parseInt(uc.substring(uc.lastIndexOf(",")+1));
      int maxhp = Stats.getMaxHP(items.getItem(xc,yc));
      int curhp = items.getHP(xc,yc);
      int fixcost = Stats.getFixCost(items.getItem(xc,yc));
      int curmoney = players.getMoney(curplayer);
      int maxheal = curmoney/fixcost;
        int needheal = maxhp - curhp;
        if (needheal<maxheal) {
          maxheal = needheal;
        }
        SimpleIO.prompt(Stats.getName(items.getItem(xc,yc))+" HP: "+curhp+"/"+maxhp+"\nHeal how much(MAX="+maxheal+")? ");
        int wantheal = Integer.parseInt(SimpleIO.readLine());
        players.addMoney(curplayer,-wantheal*fixcost);
        items.fix(xc,yc,wantheal);
    } else if ((uc.indexOf("attack")!=-1)||(uc.indexOf("atk")!=-1)) {
      int xc = Integer.parseInt(uc.substring(uc.indexOf(",")-1,uc.indexOf(",")));
      int yc = Integer.parseInt(uc.substring(uc.indexOf(",")+1,uc.lastIndexOf(",")));
      String dir = uc.substring(uc.lastIndexOf(",")+1);
      SimpleIO.prompt("Power(MAX="+players.getMoney(curplayer)+")? ");
      int attpower = Integer.parseInt(SimpleIO.readLine());
      if (attpower<=players.getMoney(curplayer)) {
        turnphase = 2;
        players.addMoney(curplayer,-attpower);
        if (dir.equals("s")) {
          if (items.getHP(xc,yc+1)<=attpower) {
            String tmpsym = items.getItem(xc,yc+1);
            items.delete(xc,yc+1);
            items.create(xc,yc+1,tmpsym,curplayer,1);
            System.out.println(red+"Captured Item!"+cr);
          } else {
            items.fix(xc,yc+1,-attpower);
            System.out.println("Target's HP: "+items.getHP(xc,yc+1)+"/"+Stats.getMaxHP(items.getItem(xc,yc+1)));
          }
        } else if (dir.equals("n")) {
          if (items.getHP(xc,yc-1)<=attpower) {
            String tmpsym = items.getItem(xc,yc-1);
            items.delete(xc,yc-1);
            items.create(xc,yc-1,tmpsym,curplayer,1);
            System.out.println(red+"Captured Item!"+cr);
          } else {
            items.fix(xc,yc-1,-attpower);
            System.out.println("Target's HP: "+items.getHP(xc,yc-1)+"/"+Stats.getMaxHP(items.getItem(xc,yc-1)));
          }
        } else if (dir.equals("e")) {
          if (items.getHP(xc+1,yc)<=attpower) {
            String tmpsym = items.getItem(xc+1,yc);
            items.delete(xc+1,yc);
            items.create(xc+1,yc,tmpsym,curplayer,1);
            System.out.println(red+"Captured Item!"+cr);
          } else {
            items.fix(xc+1,yc,-attpower);
            System.out.println("Target's HP: "+items.getHP(xc+1,yc)+"/"+Stats.getMaxHP(items.getItem(xc+1,yc)));
          }
        } else if (dir.equals("w")) {
          if (items.getHP(xc-1,yc)<=attpower) {
            String tmpsym = items.getItem(xc-1,yc);
            items.delete(xc-1,yc);
            items.create(xc-1,yc,tmpsym,curplayer,1);
            System.out.println(red+"Captured Item!"+cr);
          } else {
            items.fix(xc-1,yc,-attpower);
            System.out.println("Target's HP: "+items.getHP(xc-1,yc)+"/"+Stats.getMaxHP(items.getItem(xc-1,yc)));
          }
        }
        SimpleIO.readLine();
      } else {
        System.out.println(red+"Not enough money!"+cr);
        sleep(0.8);
    }
    }
  }
  
  
  private static void newMap() {
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
  
  private static void addItem(int x, int y, String symbol) {
    //Adds an item to array
    int itemtype = 0;
    if (symbol.equals("+")) {
      itemtype = 1;
    } else if (symbol.equals("#")) {
      itemtype = 2;
    } else if (symbol.equals("^")) {
      itemtype = 3;
    }
    array[x-1][y-1] = itemtype;
  }
  
  
  private static void redraw(boolean attack,int x, int y) {
    //Re-draws the map
    //Harder to understand the algorithm,
    //even I get confused :).
    //Just know it works!
    String ac = "";
    int ch = 1;
    int cl = 1;
    String clr;
    int pl1money = players.getMoney(1);
    int pl2money = players.getMoney(2);
    int pl1power = players.getPower(1);
    int pl2power = players.getPower(2);
    String toprint = "\n";
    while (ch<=height) {
      if (ch<10) {
    toprint=toprint+ch;
      } else {
        toprint=toprint+Integer.toString(ch).substring(1,2);
      }
      while (cl<=length) {
        toprint = toprint+" ";
        if ((cl==x)&&(ch==y)&&(attack==true)) {
          ac = attclr;
        } else {
          ac = "";
        }
        if (items.isItem(cl,ch)) {
          int maxhp = Stats.getMaxHP(items.getItem(cl,ch));
          int curhp = items.getHP(cl,ch);
          int snum = (maxhp-(maxhp%3))/3;
          int owner = items.getPlayer(cl,ch);
          if (curhp<=snum) {
            if (owner==1) {
              clr = red;
            } else {
              clr = prp;
            }
          } else if ((curhp>snum)&&(curhp<=(snum*2))) {
            if (owner==1) {
              clr = gr;
            } else {
              clr = blue;
            }
          } else {
            if (owner==1) {
              clr = yell;
            } else {
              clr = pink;
            }
          }
        } else {
        clr = cr;
        }
        switch (array[cl-1][ch-1]) {
          case 1: if(ch%2==0) { toprint=toprint+ac+clr+"|"+cr; } else { toprint=toprint+ac+clr+"-"+cr; } break;
          case 2: toprint=toprint+ac+clr+"#"+cr; break;
          case 3: toprint=toprint+ac+clr+"^"+cr; break;
          default: if((cl%2==1)&&(ch%2==1)) { toprint=toprint+"o"; } else { toprint=toprint+" "; } break;
        }
        cl++;
      }
      if (ch==2) {
        toprint=toprint+" P1 $"+pl1money;
      } else if (ch==3) {
        toprint=toprint+" P2 $"+pl2money;
      //} else if (ch==4) {
      //  System.out.print(" P1(P): "+players.getPower(1)+"/"+players.getMaxPower(1));
      //} else if (ch==5) {
      //  System.out.print(" P2(P): "+players.getPower(2)+"/"+players.getMaxPower(2));
      } else if (ch==1) {
        toprint=toprint+" Quick Stats:";
      }
       cl = 1;
       ch++;
       toprint=toprint+"\n";
    }
    toprint=toprint+"  ";
    for (int lnum = 1; lnum<=length; lnum++) {
      if (lnum<10) {
    toprint=toprint+lnum+" ";
      } else {
        toprint=toprint+Integer.toString(lnum).substring(1,2)+" ";
      }
    }
    toprint=toprint+"\n(Current Player: "+curplayer+")";
    System.out.println(toprint);
  }
  
  private static void sleep(int seconds) {
    //Quick game sleep method
    try { Thread.sleep(seconds*1000); } catch (Exception ex) {}
  }
  private static void sleep(double seconds) {
    //Quick game sleep method
    try { Thread.sleep((int)seconds*1000); } catch (Exception ex) {}
  }
  
  private static int calcIncome() {
    //Calculates a players income
    int cx = 1;
    int cy = 1;
    int income = 0;
    while (cx<=length) {
      while (cy<=height) {
        if (items.isItem(cx,cy)){
          income += Stats.getIncome(items.getItem(cx,cy));
        }
        cy++;
      }
      cy=1;
      cx++;
    }
    return income;
  }
  
}
    