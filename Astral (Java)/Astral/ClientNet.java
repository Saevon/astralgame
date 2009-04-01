/*
 * Dmitri Amariei (dim3000)
 * ServerNet.java (Part of Astral package)
 * Handles the transfer and receivale of data on a client
 * March 11, 2009
 * (c) Dmitri Amariei and Serghei Fillipov. All Rights Reserved.
 */

package Astral;

import java.io.*;
import java.net.*;


public class ClientNet {
  String sname = "localhost";
  int sport = 1357;
  PrintWriter out;
  BufferedReader in;
  Socket cs;
  
  public ClientNet(String name, int port) {
    //Creates a connection
    this.sname = name;
    this.sport = port;
    try {
      cs = new Socket(sname,sport);
      out = new PrintWriter(cs.getOutputStream(),true);
      in = new BufferedReader(new InputStreamReader(cs.getInputStream()));
      //cs.close();
      } catch (Exception ex) {
        if((""+ex).indexOf("Connection refused: connect")!=-1) {
          System.exit(-1);
        } else {
        ex.printStackTrace();
        }
      }
  }
  
  
  public boolean sendData(String data) {
    //Send a string of a command
    try {
    out.println(data);
    return true;
    } catch (Exception ex) {
        ex.printStackTrace();
        return false;
      }
  }
  
  public void exit() {
    try {
    out.close();
    in.close();
    cs.close();
    } catch (Exception ex) {
        ex.printStackTrace();
      }
  }
  
  public String getReply() {
    //Waits to recieve a set commands from server
    System.out.println("Waiting for P1...");
    String str = "";
    try {
    str = in.readLine();
    } catch (Exception ex) {
        ex.printStackTrace();
      }
    return str;
  }
  
}