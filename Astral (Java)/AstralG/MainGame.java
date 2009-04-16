package AstralG;

/*
 * Dmitri Amariei (dim3000)
 * MainGame.java (Part of AstralG package)
 * The main class of the game AstralG, the graphical version of the
 * original Astral.
 * April 9, 2009
 * (c) Dmitri Amariei. All Rights Reserved.
 */


import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.File;
import javax.sound.midi.*;

public class MainGame extends JFrame {
  
  private static void createAndShowGUI() {
        //Create and set up the window.
        MainGame astralg = new MainGame();
        astralg.setVisible(true);
        astralg.addWindowListener(new WindowAdapter() {
      public void windowClosing(WindowEvent e) {
        System.exit(0);
      }
    });
    }
  public static void main(String[] args) {
    createAndShowGUI();
    // Sets the colors
      red = Color.red;
      blue = Color.blue;
      prp = new Color(0,0,128);
      attclr = Color.black;
      cr = new Color(193, 151, 0);
      yell = Color.yellow;
      gr = Color.green;
      pink = Color.pink;
      
    //Starts playing music
      try {
      String spr = System.getProperty("file.separator");
        String dir = System.getProperty("user.dir");
        Sequence sequence = MidiSystem.getSequence(new File(dir+spr+"sound"+spr+"background.mid"));
    
        // Create a sequencer for the sequence
        sequencer = MidiSystem.getSequencer();
        sequencer.open();
        sequencer.setSequence(sequence);
        sequencer.setLoopCount(Sequencer.LOOP_CONTINUOUSLY);
      playBGMusic(true);
      } catch (Exception ex) { }
      
    // Displays main game menu and options
    int looper = 0;
    printOutLn(cr, "\n\t-A-S-T-R-A-L-");
    while (looper==0) {
    printOutLn(cr, "\nMAIN MENU\n"+
                    "1) Start a new game\t2) Load a game\n"+
                    "3) Set Map Size\t4) Set Money\n"+
                    "5) View Help\n"+
                    "6) Quit\n");
    try {
     int mainchoice = Integer.parseInt(readLine());
     String ms;
     switch (mainchoice) {
       case 2: printOutLn(cr, "Save File? "); loadfile = readLine(); setUpGame(); looper=0; break;
       case 1: setUpGame(); looper=0; break;
       case 5: printOutLn(cr, "(Sorry this is not yet implemented)"); break;
       case 3: printOutLn(cr, "Map Size(x,y)? "); ms = readLine(); length = Integer.parseInt(ms.substring(0,ms.indexOf(","))); height = Integer.parseInt(ms.substring(ms.indexOf(",")+1)); break;
       case 4: printOutLn(cr, "Starting Money? "); startmoney = Integer.parseInt(readLine()); break;
       case 6: printOutLn(cr, "Thanks for playing!"); System.exit(0);
       default: printOutLn(cr, nocmd); break;
      }
     } catch (Exception ex) { /*printOutLn(cr, nocmd);*/ }
   }
  }
  
  private static void setUpGame() {
    //Sets up a new game
    int looper = 0;
    while (looper==0) {
    printOutLn(cr, "\n1) Start a local game\n"+
                    "2) Host a game\n"+
                    "3) Join a game\n"+
                    "4) Go Back\n");
    try {
     int typechoice = Integer.parseInt(readLine());
     switch (typechoice) {
       case 1: printOutLn(cr, "Starting A New Game..."); sleep(1); beginGame("local"); looper=1; break;
       case 2: printOutLn(cr, "Starting A New Game..."); sleep(1); beginGame("host"); looper=1; break;
       case 3: printOutLn(cr, "Joining Game..."); sleep(1); beginGame("join"); looper=1; break;
       case 4: looper=1; break;
       default: printOutLn(cr, nocmd); sleep(1); break;
     }
    }  catch (Exception ex) { printOutLn(cr, nocmd); }
    }
  }
  
  private static void beginGame(String type) {
    //Begins the game
    if (type.equals("host")) {
      printOutLn(cr, "Server Password: ");
      String pass = readLine();
      printOutLn(cr, "Port? ");
      int sport = Integer.parseInt(readLine());
      ServerNet server = new ServerNet(sport);
      array = new int[length][height];
      newMap();
      players = new Players("Player1", "Player2", startmoney, 0);
      items = new Items();
      String spr = System.getProperty("file.separator");
      String dir = System.getProperty("user.dir");
      try {
      Runtime.getRuntime().exec("chmod 755 " + dir+spr+"data"+spr+"items.db");
      } catch (Exception ex) {
      }
      new File(dir+spr+"data"+spr+"items.db").delete();
      items.create(1,1,"#",1,Stats.getMaxHP("#"));
      items.create(length,height,"#",2,Stats.getMaxHP("#"));
      addItem(1,1,"#");
      addItem(length,height,"#");
      String tosend = "";
      java.util.ArrayList<String> cmdlist = new java.util.ArrayList<String>(0);
      while (true==true) {
        while (true) {
          cmdlist.clear();
          cmdlist.trimToSize();
        tosend = localTasks("na");
        if (tosend.equals("nosend")==false) {
          if ((tosend.indexOf("done")!=-1)&&(tosend.indexOf("turn")!=-1)) {
            break;
          } else {
            cmdlist.add(tosend+";");
          }
        }
      }
        server.sendData((String[])cmdlist.toArray());
        redraw(false,0,0);
        localTasks(server.getReply());
      }
      
    } else if (type.equals("join")) {
      printOutLn(cr, "Server's Name? ");
      String sname = readLine();
      printOutLn(cr, "Server's Password? ");
      String pass = readLine();
      printOutLn(cr, "Port? ");
      int sport = Integer.parseInt(readLine());
      ClientNet client = new ClientNet(sname, sport);
      array = new int[length][height];
      newMap();
      players = new Players("Player1", "Player2", startmoney, 0);
      items = new Items();
      String spr = System.getProperty("file.separator");
      String dir = System.getProperty("user.dir");
      try {
      Runtime.getRuntime().exec("chmod 755 " + dir+spr+"data"+spr+"items.db");
      } catch (Exception ex) {
      }
      new File(dir+spr+"data"+spr+"items.db").delete();
      items.create(1,1,"#",1,Stats.getMaxHP("#"));
      items.create(length,height,"#",2,Stats.getMaxHP("#"));
      addItem(1,1,"#");
      addItem(length,height,"#");
      String tosend = "";
      java.util.ArrayList<String> cmdlist = new java.util.ArrayList<String>(0);
      while (true==true) {
        redraw(false,0,0);
        localTasks(client.getReply());
        while (true) {
        tosend = localTasks("na");
        if (tosend.equals("nosend")==false) {
          break;
        }
      }
        client.sendData(tosend);
      }
      
    } else {
      if (loadfile.equals("")) {
      array = new int[length][height];
      newMap();
      players = new Players("Player1", "Player2", startmoney, 0);
      items = new Items();
      String spr = System.getProperty("file.separator");
      String dir = System.getProperty("user.dir");
      try {
      Runtime.getRuntime().exec("chmod 755 " + dir+spr+"data"+spr+"items.db");
      } catch (Exception ex) {
      }
      new File(dir+spr+"data"+spr+"items.db").delete();
      items.create(1,1,"#",1,Stats.getMaxHP("#"));
      items.create(length,height,"#",2,Stats.getMaxHP("#"));
      addItem(1,1,"#");
      addItem(length,height,"#");
      } else {
        loadGame(loadfile);
      }
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
    boolean allowed = true;
    try {
    if (turnphase==4) {
    players.addMoney(curplayer,calcIncome());
    turnphase=1;
    }
    redraw(false,0,0);
    if (netcmd.equals("na")) {
    printOutLn(cr, cmd);
    usercmd = readLine();
    } else {
      printOutLn(cr, "\nResponse: "+netcmd);
    readLine();
    usercmd = netcmd;
    }
    allowed = cmdCheck(usercmd);
    if (allowed) {
      cmdRun(usercmd);
    }
    if (!items.isItem(1,1)) {
      printOutLn(cr, pink+"\n\nPlayer 2 has won!!!"+cr);
      System.exit(0);
    }
    if (!items.isItem(length,height)) {
      printOutLn(cr, yell+"\n\nPlayer 1 has won!!!"+cr);
      System.exit(0);
    }
    } catch (Exception ex) {
      printOutLn(cr, nocmd);
    }
    if ((usercmd.indexOf("status")!=-1)||(usercmd.indexOf("help")!=-1)) {
      usercmd = "nosend";
    }
    if (!allowed) {
      usercmd = "nosend";
    }
    return usercmd;
  }
  
  
  private static boolean cmdCheck(String uc) {
    //Checks if command is allowed
    boolean result = false;
    String tempsymbol = "";
    if (uc.indexOf("buy")!=-1) {
      if (turnphase == 1) {
        if (uc.indexOf("more")!=-1) {
          result = true;
        } else {
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
        printOutLn(red, "Not enough money!");
      }
      if (items.isItem(xcoord,ycoord)) {
        printOutLn(red, "Item already there!");
        result = false;
      }
      } else {
        printOutLn(red, "Cant't be placed there!");
      }
        }
      } else {
        printOutLn(red, "No building during this phase!");
      }
    } else if (uc.indexOf("quit")!=-1) {
      result = true;
    } else if (uc.indexOf("exit")!=-1) {
      result = true;
    } else if (uc.indexOf("save")!=-1) {
      if (uc.indexOf("'")!=-1) {
      result = true;
      } else {
        printOutLn(red, "No file specified!");
      }
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
        printOutLn(red, "Can't be sold!");
        sleep(0.8);
      }
      } else {
        printOutLn(red, "Not your item!");
      }
      } else {
        printOutLn(red, "No item found!");
        sleep(0.8);
      }
      } else {
        printOutLn(red, "No selling during this phase!");
        sleep(0.8);
      }
    } else if (uc.indexOf("status")!=-1) {
      int xc = Integer.parseInt(uc.substring(uc.indexOf(",")-1,uc.lastIndexOf(",")));
      int yc = Integer.parseInt(uc.substring(uc.lastIndexOf(",")+1));
      if (items.isItem(xc,yc)) {
      result = true;
      } else {
        printOutLn(red, "No item found!");
        sleep(0.8);
      }
    } else if (uc.indexOf("done")!=-1) {
      result = true;
    } else if (uc.indexOf("fix")!=-1) {
      if (turnphase!=2) {
      int xc = Integer.parseInt(uc.substring(uc.indexOf(",")-1,uc.indexOf(",")));
      int yc = Integer.parseInt(uc.substring(uc.indexOf(",")+1));
      int maxhp = Stats.getMaxHP(items.getItem(xc,yc));
      int curhp = items.getHP(xc,yc);
      if (curplayer==items.getPlayer(xc,yc)) {
      if (curhp<maxhp) {
        result = true;
      } else {
        printOutLn(red, "Item's HP is already full!");
        sleep(0.8);
      }
      } else {
        printOutLn(red, "Not your item!");
      }
      } else {
        printOutLn(red, "No fixing during this phase!");
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
        printOutLn(red, "You have finished attacking!");
        sleep(0.8);
      } 
      } else {
        printOutLn(red, "Not your item!");
      }
    } else {
      printOutLn(cr, nocmd);
      sleep(0.8);
    }
    return result;
  }
  
  private static void cmdRun(String uc) {
    //Executes specified command
    if (uc.indexOf("buy")!=-1) {
      boolean doloop = true;
      boolean tmp = true;
      if (uc.indexOf("more")==-1) {
        tmp = false;
      }
      while (doloop) {
        if (tmp) {
          printOutLn(cr, cmd);
          uc = readLine();
        }
        if (uc.indexOf("stop")!=-1) {
          break;
        }
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
      if (tmp==false) {
        doloop = false;
      }
      }
      printOutLn(cr, "Bought!");
    } else if (uc.indexOf("quit")!=-1) {
      printOutLn(cr, "Brutally Disconnecting...");
      System.exit(0);
    } else if (uc.indexOf("exit")!=-1) {
      printOutLn(cr, "Brutally Disconnecting...");
      System.exit(0);
    } else if (uc.indexOf("help")!=-1) {
      doHelp();
    } else if (uc.indexOf("save")!=-1) {
      saveGame(uc.substring(uc.indexOf("'")+1));
      printOutLn(cr, "Game Saved!");
    } else if (uc.indexOf("sell")!=-1) {
      int xcoord = Integer.parseInt(uc.substring(uc.indexOf(",")-1,uc.lastIndexOf(",")));
      int ycoord = Integer.parseInt(uc.substring(uc.lastIndexOf(",")+1));
      int value = Stats.getValue(items.getItem(xcoord,ycoord));
      String sym = items.getItem(xcoord,ycoord);
      players.addMoney(curplayer, value);
      addItem(xcoord,ycoord,"d");
      items.delete(xcoord,ycoord);
      printOutLn(cr, "Sold!");
      sleep(0.8);
    } else if (uc.indexOf("status")!=-1) {
      int xcoord = Integer.parseInt(uc.substring(uc.indexOf(",")-1,uc.indexOf(",")));
      int ycoord = Integer.parseInt(uc.substring(uc.indexOf(",")+1));
      int owner = items.getPlayer(xcoord,ycoord);
      if (owner==1) {
      printOutLn(cr, yell+items.getInfo(xcoord,ycoord)+cr);
      } else {
        printOutLn(cr, pink+items.getInfo(xcoord,ycoord)+cr);
      }
      printOutLn(cr, "(Press Enter)");
      readLine();
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
      int xc = Integer.parseInt(uc.substring(uc.indexOf(",")-1,uc.indexOf(",")));
      int yc = Integer.parseInt(uc.substring(uc.indexOf(",")+1));
      int maxhp = Stats.getMaxHP(items.getItem(xc,yc));
      int curhp = items.getHP(xc,yc);
      int fixcost = Stats.getFixCost(items.getItem(xc,yc));
      int curmoney = players.getMoney(curplayer);
      int maxheal = curmoney/fixcost;
        int needheal = maxhp - curhp;
        if (needheal<maxheal) {
          maxheal = needheal;
        }
        printOutLn(cr, Stats.getName(items.getItem(xc,yc))+" HP: "+curhp+"/"+maxhp+"\nHeal how much(MAX="+maxheal+")? ");
        int wantheal = Integer.parseInt(readLine());
        players.addMoney(curplayer,-wantheal*fixcost);
        items.fix(xc,yc,wantheal);
    } else if ((uc.indexOf("attack")!=-1)||(uc.indexOf("atk")!=-1)) {
      doAttack(uc);
    }
  }
  
  
  private static void doAttack(String uc) {
    try {
    int xc = Integer.parseInt(uc.substring(uc.indexOf(",")-1,uc.indexOf(",")));
      int yc = Integer.parseInt(uc.substring(uc.indexOf(",")+1,uc.lastIndexOf(",")));
      String dir = uc.substring(uc.lastIndexOf(",")+1);
      printOutLn(cr, "Power(MAX="+players.getMoney(curplayer)+")? ");
      int attpower = Integer.parseInt(readLine());
      int attx = 0;
      int atty = 0;
      int xchange = 0;
      int ychange = 0;
      
      if (attpower<=players.getMoney(curplayer)) {
        if (dir.equals("s")) {
          ychange = 1;
        } else if (dir.equals("n")) {
          ychange = -1;
        } else if (dir.equals("e")) {
          xchange = 1;
        } else if (dir.equals("w")) {
          xchange = -1;
        }
        attx = xc+xchange;
        atty = yc+ychange;
        if (items.getItem(attx,atty).equals("+")) {
          players.addMoney(curplayer,-attpower);
          while (attpower>0) {
            while (items.getPlayer(attx,atty)==curplayer) {
              if (!items.getItem(attx,atty).equals("+")) {
                break;
              }
               attx += xchange;
               atty += ychange;
               if (!items.getItem(attx,atty).equals("+")) {
                 String newdirs = "";
                 if (ychange==1) {
                   if (items.isItem(attx-1,atty)) { newdirs += "w"; }
                   if (items.isItem(attx+1,atty)) { newdirs += "e"; }
                   if (items.isItem(attx,atty+1)) { newdirs += "s"; }
                 } else if (ychange==-1) {
                   if (items.isItem(attx-1,atty)) { newdirs += "w"; }
                   if (items.isItem(attx+1,atty)) { newdirs += "e"; }
                   if (items.isItem(attx,atty-1)) { newdirs += "n"; }
                 } else if (xchange==1) {
                   if (items.isItem(attx+1,atty)) { newdirs += "e"; }
                   if (items.isItem(attx,atty+1)) { newdirs += "s"; }
                   if (items.isItem(attx,atty-1)) { newdirs += "n"; }
                 } else if (xchange==-1) {
                   if (items.isItem(attx,atty+1)) { newdirs += "s"; }
                   if (items.isItem(attx-1,atty)) { newdirs += "w"; }
                   if (items.isItem(attx,atty-1)) { newdirs += "n"; }
                 }
                 if (newdirs.equals("")) {
                   return;
                 }
                 int dirnum = (int) ((Math.random() * newdirs.length() + 1));
                 String resultdir = newdirs.substring(dirnum-1,dirnum);
                 xchange = 0;
                 ychange = 0;
                  if (resultdir.equals("s")) {
                    ychange = 1;
                  } else if (resultdir.equals("n")) {
                    ychange = -1;
                  } else if (resultdir.equals("e")) {
                    xchange = 1;
                  } else if (resultdir.equals("w")) {
                    xchange = -1;
                  }
                  if (!items.isItem(attx,atty)) {
                  attx += xchange;
                  atty += ychange;
                  }
               }
            }
            if (attpower>0) {
          redraw(true,attx,atty);
        }
             turnphase = 2;
        if (items.getHP(attx,atty)<=attpower) {
          attpower -= items.getHP(attx,atty);
            String tmpsym = items.getItem(attx,atty);
            items.delete(attx,atty);
            items.create(attx,atty,tmpsym,curplayer,1);
            printOutLn(red, "Captured Item!");
            if (items.getItem(attx,atty).equals("#")) {
              if (items.getPlayer(attx,atty)==1) {
                printOutLn(cr, "\nPlayer 1 Wins!");
                sleep(1);
                System.exit(0);
              } else {
                printOutLn(cr, "\nPlayer 2 Wins!");
                sleep(1);
                System.exit(0);
              }
            }
          } else {
            int temppower = attpower;
            attpower -= items.getHP(attx,atty);
            items.fix(attx,atty,-temppower);
            printOutLn(cr, "Target's HP: "+items.getHP(attx,atty)+"/"+Stats.getMaxHP(items.getItem(attx,atty)));
          }
        readLine();
        }
        } else {
            printOutLn(red, "No Path!");
          }
      } else {
        printOutLn(red, "Not enough money!");
    }
    } catch (Exception ex) { ex.printStackTrace(); }
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
    Color ac = cr;
    int ch = 1;
    int cl = 1;
    Color clr = cr;
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
        if ((cl==x)&&(ch==y)&&(attack==true)) {
          clr = attclr;
        }
        switch (array[cl-1][ch-1]) {
          case 1: if(ch%2==0) { toprint=toprint+clr+"|"+cr; } else { toprint=toprint+clr+"-"+cr; } break;
          case 2: toprint=toprint+clr+"#"+cr; break;
          case 3: toprint=toprint+clr+"^"+cr; break;
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
    textArea1.appendMulti(cr, toprint+"\n");
    textArea1.setCaretPosition(textArea1.getDocument().getLength());
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
        if (items.isItem(cx,cy)&&items.getPlayer(cx,cy)==curplayer){
          income += Stats.getIncome(items.getItem(cx,cy));
        }
        cy++;
      }
      cy=1;
      cx++;
    }
    return income;
  }
  
  private static void doHelp() {
    //Specifs for HELP command
    //Reads data/help.db to get properties
    String spr = System.getProperty("file.separator");
    String dir = System.getProperty("user.dir");
    String topics = "\nHelp Topics";
    String str = "";
    int tcount = 2;
    String tmpstr = "\n";
    try {
        java.io.BufferedReader in = new java.io.BufferedReader(new java.io.FileReader(new java.io.File(dir+spr+"data"+spr+"help.db")));
        while ((str.indexOf("##"))==-1) {
          str = in.readLine();
          if ((str.indexOf("$"))!=-1) {
            str = "";
          }
        }
        str = in.readLine();
        topics += tmpstr+"1) "+str.substring(str.indexOf("=")+1);
        while (true) {
          while (((str = in.readLine()).indexOf("%"))==-1) {
        }
          str = in.readLine();
          if (str.equals("##")) {
            break;
          }
           if (tcount%2!=1) {
            tmpstr = "\t";
          } else {
            tmpstr = "\n";
          }
        topics += tmpstr+tcount+") "+str.substring(str.indexOf("=")+1);
        tcount++;
        }
        printOutLn(cr, topics);
        printOutLn(cr, cmd);
        topics = topics.replace("\t","\n");
        String linechoice = topics.split("\n")[Integer.parseInt(readLine())+1];
        String topicName = linechoice.substring(linechoice.indexOf(")")+2);
        in.close();
        in = new java.io.BufferedReader(new java.io.FileReader(new java.io.File(dir+spr+"data"+spr+"help.db")));
        topics = "\nItems";
        tcount = 2;
        str = "";
        tmpstr = "\n";
        String[] itemlines = new String[20];
        while ((str.indexOf("%="+topicName))==-1) {
          str = in.readLine();
          if ((str.indexOf("$"))!=-1) {
            str = "";
          }
        }
        str = in.readLine();
        topics += tmpstr+"1) "+str.substring(0,str.indexOf("<")-1);
        itemlines[0] = str;
        while (true) {
          str = in.readLine();
          if ((str.equals("%"))) {
            break;
          }
          if (tcount%2!=1) {
            tmpstr = "\t";
          } else {
            tmpstr = "\n";
          }
        topics += tmpstr+tcount+") "+str.substring(0,str.indexOf("<")-1);
        itemlines[tcount-1] = str;
        tcount++;
        }
        printOutLn(cr, topics);
        printOutLn(cr, cmd);
        int numchoice = Integer.parseInt(readLine());
        String itemText = itemlines[numchoice-1].substring(itemlines[numchoice-1].indexOf("<")+1,itemlines[numchoice-1].indexOf(">"));
        itemText = itemText.replace("RED",red+"RED"+cr);
        itemText = itemText.replace("BLACK",attclr+"BLACK"+cr);
        itemText = itemText.replace("GREEN",gr+"GREEN"+cr);
        itemText = itemText.replace("YELLOW",yell+"YELLOW"+cr);
        itemText = itemText.replace("PINK",pink+"PINK"+cr);
        itemText = itemText.replace("BLUE",blue+"BLUE"+cr);
        itemText = itemText.replace("PURPLE",prp+"PURPLE"+cr);
        itemText = itemText.replaceAll("!","\n");
        textArea1.appendMulti(cr, itemText+"\n");
        textArea1.setCaretPosition(textArea1.getDocument().getLength());
        readLine();
        in.close();
        
    } catch (Exception e) {
      printOutLn(cr, "ERROR READING FILE(Called by:doHelp())");
      e.printStackTrace();
      readLine();
      System.exit(-1);
    }
  }
  
  private static void loadGame(String file) {
    int p1money = 0;
    int p2money = 0;
    try {
    String spr = System.getProperty("file.separator");
    String dir = System.getProperty("user.dir");
    java.io.RandomAccessFile in = new java.io.RandomAccessFile(new File(dir+spr+"save"+spr+file+".sav"), "rw");
    String tmp = in.readLine();
    height = Integer.parseInt(tmp.substring(tmp.indexOf("=")+1));
    tmp = in.readLine();
    length = Integer.parseInt(tmp.substring(tmp.indexOf("=")+1));
    tmp = in.readLine();
    p1money = Integer.parseInt(tmp.substring(tmp.indexOf("=")+1));
    tmp = in.readLine();
    p2money = Integer.parseInt(tmp.substring(tmp.indexOf("=")+1));
    tmp = in.readLine();
    curplayer = Integer.parseInt(tmp.substring(tmp.indexOf("=")+1));
    tmp = in.readLine();
    turnphase = Integer.parseInt(tmp.substring(tmp.indexOf("=")+1));
    array = new int[length][height];
    newMap();
    players = new Players("Player1", "Player2", startmoney, 0);
    players.setMoney(1,p1money);
    players.setMoney(2,p2money);
    items = new Items();
    try {
    Runtime.getRuntime().exec("chmod 755 " + dir+spr+"data"+spr+"items.db");
    } catch (Exception ex) {
    }
    new File(dir+spr+"data"+spr+"items.db").delete();
    int xc = 0;
    int yc = 0;
    String sym = "";
    int curhp = 0;
    int owner = 0;
    try {
      while (true) {
    tmp = in.readLine();
    xc = Integer.parseInt(tmp.substring(0,tmp.indexOf("'")));
    yc = Integer.parseInt(tmp.substring(tmp.indexOf("'")+1,tmp.indexOf(":")));
    sym = tmp.substring(tmp.indexOf(":")+1,tmp.indexOf(","));
    owner = Integer.parseInt(tmp.substring(tmp.indexOf(",")+1,tmp.lastIndexOf(",")));
    curhp = Integer.parseInt(tmp.substring(tmp.lastIndexOf(",")+1));
    items.create(xc,yc,sym,owner,curhp);
    addItem(xc,yc,sym);
      }
    } catch (NullPointerException nex) {
    }
    in.close();
    } catch (Exception ex) {
      printOutLn(cr, "ERROR READING FILE");
      System.exit(-1);
    }
  }
  
  private static void saveGame(String file) {
    try {
    String spr = System.getProperty("file.separator");
    String dir = System.getProperty("user.dir");
    try {
    Runtime.getRuntime().exec("chmod 755 " + dir+spr+"save"+spr+file+".sav");
    } catch (Exception ex) {
    }
    new File(dir+spr+"save"+spr+file+".sav").delete();
    java.io.RandomAccessFile in = new java.io.RandomAccessFile(new File(dir+spr+"save"+spr+file+".sav"), "rw");
    String vars = "height="+height+"\nlength="+length+"\nplayer1="+players.getMoney(1)+"\nplayer2="+
                  players.getMoney(2)+"\ncurplayer="+curplayer+"\nturnphase="+turnphase;
    in.writeBytes(vars);
    int cx = 1;
    int cy = 1;
    String locs = "";
    while (cy<=height) {
      while (cx<=length) {
        if (items.isItem(cx,cy)) {
          locs += "\n"+cx+"'"+cy+":"+items.getItem(cx,cy)+","+items.getPlayer(cx,cy)+","+items.getHP(cx,cy);
        }
        cx++;
      }
      cx = 1;
      cy++;
    }
    in.writeBytes(locs);
    in.close();
    } catch (Exception ex) {
      printOutLn(cr, "ERROR WRITING FILE");
      System.exit(-1);
    }
  }
  
  private static String readLine() {
    textField1.setEnabled(true);
    textField1.requestFocus();
    while (textField1.isEnabled()) {
    }
    String text = textField1.getText();
    textField1.setText("");
    return text;
  }
  
  private static void printOut(Color c, String text) {
    textArea1.append(c, text);
    textArea1.setCaretPosition(textArea1.getDocument().getLength());
  }
  
  private static void printOutLn(Color c, String text) {
    textArea1.append(c, text+"\n");
    textArea1.setCaretPosition(textArea1.getDocument().getLength());
  }
  
  private static void playBGMusic(boolean toPlay) {
    try { 
    if (toPlay) {
        sequencer.start();
    } else {
      sequencer.stop();
    }
    } catch (Exception e) { }
  }
 
  
  
  /*
   * Start of GUI code
   * (Variables are at the end)
   */
  
  
  
 public MainGame() {
  initComponents();
 }

 private void menuItem1ActionPerformed(ActionEvent e) {
   JOptionPane.showMessageDialog(this, "Thanks for playing Astral, Goodbye!", 
                                         "Exit Application", JOptionPane.INFORMATION_MESSAGE);
   System.exit(0);
 }
 
 private void menuItem4ActionPerformed(ActionEvent e) {
   JOptionPane.showMessageDialog(this, "Type \"help\" in game for detailed help.", 
                                         "Game Help", JOptionPane.INFORMATION_MESSAGE);
 }
 
 private void menuItem5ActionPerformed(ActionEvent e) {
   JOptionPane.showMessageDialog(this, "AstralG (GUI Version)\nVersion: v1.1\nAuthor: Dmitri Amariei\nWebsite: astralgame.tk", 
                                         "About Game", JOptionPane.INFORMATION_MESSAGE);
 }
 
 private void checkBoxMenuItem1ActionPerformed(ActionEvent e) {
   if (checkBoxMenuItem1.isSelected()) {
     playBGMusic(true);
   } else {
     playBGMusic(false);
   }
 }

 private void button1ActionPerformed(ActionEvent e) {
   //"Run" button is clicked
   if (textField1.isEnabled()) {
     textField1.setEnabled(false);
   }
 }

 private void initComponents() {
  menuBar1 = new JMenuBar();
  menu1 = new JMenu();
  menuItem2 = new JMenuItem();
  menuItem3 = new JMenuItem();
  menuItem1 = new JMenuItem();
  menu2 = new JMenu();
  menu3 = new JMenu();
  menuItem4 = new JMenuItem();
  menuItem5 = new JMenuItem();
  scrollPane1 = new JScrollPane();
  textArea1 = new ColorPane();
  textField1 = new JTextField();
  label1 = new JLabel();
  label2 = new JLabel();
  button1 = new JButton();
  label3 = new JLabel();
  label4 = new JLabel();
  checkBoxMenuItem1 = new JCheckBoxMenuItem();

  //======== this ========
  setTitle("AstralG (v1.1)");
  setResizable(false);
  Container contentPane = getContentPane();
  contentPane.setLayout(null);

  //======== menuBar1 ========
  {

   //======== menu1 ========
   {
    menu1.setText("File");

    //---- menuItem2 ----
    menuItem2.setText("Open...");
    menuItem2.setEnabled(false);
    menu1.add(menuItem2);

    //---- menuItem3 ----
    menuItem3.setText("Save As...");
    menuItem3.setEnabled(false);
    menu1.add(menuItem3);

    //---- menuItem1 ----
    menuItem1.setText("Exit");
    menuItem1.addActionListener(new ActionListener() {
     public void actionPerformed(ActionEvent e) {
      menuItem1ActionPerformed(e);
     }
    });
    menu1.add(menuItem1);
   }
   menuBar1.add(menu1);

   //======== menu2 ========
   {
    menu2.setText("Options");
    
    //---- checkBoxMenuItem1 ----
    checkBoxMenuItem1.setText("Sound");
    checkBoxMenuItem1.setSelected(true);
    checkBoxMenuItem1.addActionListener(new ActionListener() {
     public void actionPerformed(ActionEvent e) {
      checkBoxMenuItem1ActionPerformed(e);
     }
    });
    menu2.add(checkBoxMenuItem1);
   }
   menuBar1.add(menu2);

   //======== menu3 ========
   {
    menu3.setText("Help");

    //---- menuItem4 ----
    menuItem4.setText("Game Help");
    menuItem4.addActionListener(new ActionListener() {
     public void actionPerformed(ActionEvent e) {
      menuItem4ActionPerformed(e);
     }
    });
    menu3.add(menuItem4);

    //---- menuItem5 ----
    menuItem5.setText("About...");
    menuItem5.addActionListener(new ActionListener() {
     public void actionPerformed(ActionEvent e) {
      menuItem5ActionPerformed(e);
     }
    });
    menu3.add(menuItem5);
   }
   menuBar1.add(menu3);
  }
  setJMenuBar(menuBar1);

  //======== scrollPane1 ========
  {

   //---- textArea1 ----
   textArea1.setFont(new Font("Lucida Console", Font.PLAIN, 12));
   textArea1.setBackground(new Color(0, 56, 56));
   textArea1.setForeground(new Color(193, 151, 0));
   textArea1.setEditable(true);
   scrollPane1.setViewportView(textArea1);
  }
  contentPane.add(scrollPane1);
  scrollPane1.setBounds(10, 40, 430, 235);
  contentPane.add(textField1);
  textField1.setBounds(90, 295, 265, textField1.getPreferredSize().height);
  textField1.setEnabled(false);
  textField1.setText("");

  //---- label1 ----
  label1.setText("Game Window (unsaved)");
  label1.setFont(new Font("Tahoma", Font.BOLD, 12));
  contentPane.add(label1);
  label1.setBounds(10, 15, 290, 25);

  //---- label2 ----
  label2.setText("Command:");
  label2.setFont(new Font("Tahoma", Font.BOLD, 11));
  contentPane.add(label2);
  label2.setBounds(20, 290, 75, 25);

  //---- button1 ----
  button1.setText("RUN");
  button1.setFont(new Font("Tahoma", Font.BOLD, 10));
  getRootPane().setDefaultButton(button1);
  button1.addActionListener(new ActionListener() {
   public void actionPerformed(ActionEvent e) {
    button1ActionPerformed(e);
   }
  });
  contentPane.add(button1);
  button1.setBounds(370, 295, 65, 21);

  //---- label3 ----
  label3.setText("   ");
  contentPane.add(label3);
  label3.setBounds(20, 325, 415, label3.getPreferredSize().height);

  //---- label4 ----
  label4.setText("   ");
  contentPane.add(label4);
  label4.setBounds(445, 50, 15, 210);

  { // compute preferred size
   Dimension preferredSize = new Dimension();
   for(int i = 0; i < contentPane.getComponentCount(); i++) {
    Rectangle bounds = contentPane.getComponent(i).getBounds();
    preferredSize.width = Math.max(bounds.x + bounds.width, preferredSize.width);
    preferredSize.height = Math.max(bounds.y + bounds.height, preferredSize.height);
   }
   Insets insets = contentPane.getInsets();
   preferredSize.width += insets.right;
   preferredSize.height += insets.bottom;
   contentPane.setMinimumSize(preferredSize);
   contentPane.setPreferredSize(preferredSize);
  }
  pack();
  setLocationRelativeTo(getOwner());
 }

 private static JMenuBar menuBar1;
 private static JMenu menu1;
 private static JMenuItem menuItem2;
 private  static JMenuItem menuItem3;
 private  static JMenuItem menuItem1;
 private  static JMenu menu2;
 private  static JMenu menu3;
 private  static JMenuItem menuItem4;
 private  static JMenuItem menuItem5;
 private  static JScrollPane scrollPane1;
 private  static ColorPane textArea1;
 private  static JTextField textField1;
 private  static JLabel label1;
 private  static JLabel label2;
 private  static JButton button1;
 private  static JLabel label3;
 private  static JLabel label4;
 private static  JCheckBoxMenuItem checkBoxMenuItem1;
 
 
 //Shortcut/Game Variables
  final static String nocmd = "Unrecognized Command!";
  final static String cmd = "";
  static Color red;
  static Color blue;
  static Color attclr;
  static Color gr;
  static Color prp;
  static Color cr;
  static Color yell;
  static Color pink;
  static Players players;
  static Items items;
  static String loadfile = "";
  /* The array stores numbers corrresponding to items
   * Format:
   * blank = 0
   * + = 1
   * # = 2
   * ^ = 3
   */
  static int height = 5;
  static int length = 7;
  static int[][] array;
  static int curplayer = 1;
  static int turnphase = 1;
  static int startmoney = 50;
  static Sequencer sequencer;
}
