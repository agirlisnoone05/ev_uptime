## Run code
intervals.py - 
    The main problem logic and get_uptime function
    
test.py - 
    A few test cases to check 

To run this code -

```bash
    python3 test.py
```

## Problem - 
Calculate the uptime percentage of an electric charging station based on the availability of its chargers over time. 

The station uptime is defined as the percentage of time during which at least one charger is available at the station.

## Inputs

A list of ChargerStatusInterval objects. 
Each object contains:
charger_id: 
A unique identifier for the charger.

begin_time_nanos and end_time_nanos: 
The start and end times (in nanoseconds) of a time interval.

available: 
A boolean indicating whether the charger was available during this interval.

The intervals for each charger are guaranteed to be contiguous (no gaps) and non-overlapping, but intervals for different chargers may overlap in time.

## Outputs

A single number representing the percentage of time during which at least one charger was available across all intervals.

## Requirements

The station is considered "up" during any time when at least one charger is available.
We need to compute the percentage of total time across all intervals where the station was "up."

## Goal
Implement the get_uptime function to calculate the station uptime percentage given the input intervals.

## Key Steps:
### I) Flatten intervals into events:

Each interval is split into two events:
1. A start event indicating when the charger becomes available/unavailable.
2. An end event indicating when the availability/unavailability ends.

This transformation allows us to process all changes to charger availability in a linear, sorted order.

### II) Sort events:

Events are sorted by time, and ties are resolved by processing "end" events before "start" events.
Sorting ensures that we process availability changes chronologically and handle overlapping intervals correctly.


### III) Process events from the beginning to the end of the time range:

- Keep track of the number of active chargers at each time point.
- If at least one charger is active, add the time elapsed since the last event to the total uptime.

### IV) Calculate the uptime percentage:

The uptime percentage is the total duration during which at least one charger was available, divided by the total time span.

Efficiency: Flattening and sorting events reduces the complexity of processing overlapping intervals.

Correctness: By processing events chronologically, the algorithm accounts for overlapping intervals and ensures that the uptime is calculated accurately.

## Complexity
### Time Complexity: 
O(nlogn), where 
n is the number of intervals (due to sorting the events).
### Space Complexity: 
O(n), for storing the flattened events.
