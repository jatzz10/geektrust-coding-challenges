package com.example.geektrust;

import java.util.HashMap;

public class StationStats {
    private int totalAmountCollected;
    private int totalDiscountGiven;
    private HashMap<String, Integer> passengerTypeCount;

    /**
    * Initialize a StationStats object.
    * Instance variables:
    *   - total_amount_collected: Total amount collected at the station.
    *   - total_discount_given: Total discount given at the station.
    *   - passenger_type_count: Dictionary of passenger types and their counts.
    * */
    public StationStats() {
        this.totalAmountCollected = 0;
        this.totalDiscountGiven = 0;
        this.passengerTypeCount = new HashMap<String, Integer>();
    }

    public int getTotalAmountCollected() {
        return this.totalAmountCollected;
    }

    public int getTotalDiscountGiven() {
        return this.totalDiscountGiven;
    }

    public HashMap<String, Integer> getPassengerTypeCount() {
        return this.passengerTypeCount;
    }

    public void addToTotalAmountCollected(int amount) {
        this.totalAmountCollected += amount;
    }

    public void addToTotalDiscountGiven(int amount) {
        this.totalDiscountGiven += amount;
    }

    public void updatePassengerTypeCount(PassengerType passengerType) {
        if (this.passengerTypeCount.containsKey(passengerType.name())) {
            this.passengerTypeCount.put(passengerType.name(), this.passengerTypeCount.get(passengerType.name())+1);
        } else {
            this.passengerTypeCount.put(passengerType.name(), 1);
        }
    }

    public void update_stats(PassengerType passengerType, int travelCharge, int discountApplied) {
        /*
        * Update station statistics.
        *  Args:
        *  @param passenger_type Type of passenger.
        *  @param travel_charge Travel charge for the passenger.
        *  @param discount_applied Discount applied to the passenger.
        */
        this.addToTotalAmountCollected(travelCharge);
        this.addToTotalDiscountGiven(discountApplied);
        this.updatePassengerTypeCount(passengerType);
    }
}
