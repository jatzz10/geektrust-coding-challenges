package com.example.geektrust;


public class Passenger {
    private final PassengerType passengerType;

    /**
     * Initialize a Passenger object.
     *
     * @param passengerType Type of passenger.
     */
    public Passenger(PassengerType passengerType) {
        this.passengerType = passengerType;
    }

    public PassengerType getPassengerType() {
        return this.passengerType;
    }

    public static PassengerTravelCharge getPassengerTravelCharge(PassengerType passengerType) {
        return PassengerTravelCharge.valueOf(passengerType.name());
    }
}
