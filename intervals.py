class ChargerStatusInterval:
    def __init__(self, charger_id: str, begin_time_nanos: int, end_time_nanos: int, available: bool):
        self.charger_id = charger_id
        self.begin_time_nanos = begin_time_nanos
        self.end_time_nanos = end_time_nanos
        self.available = available

# function that calculates uptime and retuns a % 
def get_uptime(intervals):
    # Step 1: Flatten intervals into events 
    events = []
    for interval in intervals:
        events.append((interval.begin_time_nanos, 1 if interval.available else 0))
        events.append((interval.end_time_nanos, -1 if interval.available else 0))

    # Step 2: Sort events 
    events.sort(key=lambda x: (x[0], -x[1]))

    # Step 3: Process events from the beginning to the end of the time range:
    current_uptime = 0
    active_chargers = 0
    last_time = events[0][0] if events else 0

    for time, change in events:
        if active_chargers > 0:
            current_uptime += time - last_time
        active_chargers += change
        last_time = time

    total_time = events[-1][0] - events[0][0] if events else 0
    return (current_uptime / total_time) * 100 if total_time > 0 else 0.0
