package com.example.geektrust;

public class MetroCard {
    private final String cardId;
    private int balance;
    private boolean cardSwipedForOneWay;

    public MetroCard(String cardId, int balance) {
        this.cardId = cardId;
        this.balance = balance;
        this.cardSwipedForOneWay = false;
    }

    public int getBalance() {
        return balance;
    }

    public boolean isCardSwipedForOneWay() {
        return cardSwipedForOneWay;
    }

    public void addToBalance(int amount) {
        balance += amount;
    }

    public void deductFromBalance(int amount) {
        balance -= amount;
    }

    public void setCardSwipedForOneWay(boolean value) {
        cardSwipedForOneWay = value;
    }
}
