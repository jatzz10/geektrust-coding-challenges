package com.example.geektrust;

public enum PassengerTravelCharge {
    SENIOR_CITIZEN(Constants.SENIOR_CITIZEN_TRAVEL_CHARGE),
    ADULT(Constants.ADULT_TRAVEL_CHARGE),
    KID(Constants.KID_TRAVEL_CHARGE);

    private final int charge;

    PassengerTravelCharge(int charge) {
        this.charge = charge;
    }

    public int getCharge() {
        return charge;
    }
}
