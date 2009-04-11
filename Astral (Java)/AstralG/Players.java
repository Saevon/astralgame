/*
 * Dmitri Amariei (dim3000)
 * Players.java (Part of Astral package)
 * Handles the infromation for both players (i.e money, color, etc...)
 * March 12, 2009
 * (c) Dmitri Amariei and Serghei Fillipov. All Rights Reserved.
 */

package AstralG;


public class Players {
  private int money1 = 0;
  private int money2 = 0;
  private int maxpower1 = 0;
  private int maxpower2 = 0;
  private int power1 = 0;
  private int power2 = 0;
  private String name1 = "";
  private String name2 = "";
  private String clr1;
  private String clr2;
  
  public Players(String name1, String name2, int startmoney, int startpower) {
    this.name1 = name1;
    this.name2 = name2;
    this.money1 = startmoney;
    this.money2 = startmoney;
    this.maxpower1 = startpower;
    this.maxpower2 = startpower;
    this.maxpower1 = this.power1;
    this.maxpower2 = this.power1;
    this.clr1 = "green";
    this.clr2 = "blue";
  }
  
  public void setMoney(int player, int amount) {
    if (player==1) {
      money1 = amount;
    } else {
      money2 = amount;
    }
  }
  
  public void addMoney(int player, int amount) {
    if (player==1) {
      money1 += amount;
    } else {
      money2 += amount;
    }
  }
  
  public int getMoney(int player) {
    if (player==1) {
      return money1;
    } else {
      return money2;
    }
  }
  
  public void setMaxPower(int player, int amount) {
    if (player==1) {
      maxpower1 = amount;
    } else {
      maxpower2 = amount;
    }
  }
  
  public void addPower(int player, int amount) {
    if (player==1) {
      power1 += amount;
    } else {
      power2 += amount;
    }
  }
  
  public int getMaxPower(int player) {
    if (player==1) {
      return maxpower1;
    } else {
      return maxpower2;
    }
  }
  
  public int getPower(int player) {
    if (player==1) {
      return power1;
    } else {
      return power2;
    }
  }
  
  public String getName(int player) {
    if (player==1) {
      return name1;
    } else {
      return name2;
    }
  }
  
  public String getColor(int player) {
    if (player==1) {
      return clr1;
    } else {
      return clr2;
    }
  }
  
}