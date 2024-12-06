from intervals import ChargerStatusInterval, get_uptime

def run_tests():
    tests = [
        # Intervals1 from problem statement
        {
            "description": "Intervals1 from problem statement (100% uptime)",
            "intervals": [
                ChargerStatusInterval("1", 0, 200000, True),
                ChargerStatusInterval("2", 0, 100000, True),
                ChargerStatusInterval("2", 100000, 200000, False)
            ],
            "expected": 100.0
        },
        # Intervals2 from problem statement
        {
            "description": "Intervals2 from problem statement (50% uptime)",
            "intervals": [
                ChargerStatusInterval("1", 0, 200000, False),
                ChargerStatusInterval("2", 0, 100000, True),
                ChargerStatusInterval("2", 100000, 200000, False)
            ],
            "expected": 50.0
        },
        # Single Charger Always Available
        {
            "description": "Single charger always available",
            "intervals": [ChargerStatusInterval("1", 0, 100000, True)],
            "expected": 100.0
        },
        # Single Charger Always Unavailable
        {
            "description": "Single charger always unavailable",
            "intervals": [ChargerStatusInterval("1", 0, 100000, False)],
            "expected": 0.0
        },
        # Multiple Chargers, No Overlap
        {
            "description": "Multiple chargers, no overlap",
            "intervals": [
                ChargerStatusInterval("1", 0, 50000, True),
                ChargerStatusInterval("2", 50000, 100000, True)
            ],
            "expected": 100.0
        },
        # Partial Overlap
        {
            "description": "Partial overlap",
            "intervals": [
                ChargerStatusInterval("1", 0, 100000, True),
                ChargerStatusInterval("2", 50000, 150000, True),
                ChargerStatusInterval("3", 100000, 200000, False)
            ],
            "expected": 75.0
        },
        # Edge Case: Extremely Large Inputs
        {
            "description": "Edge case with large input size",
            "intervals": [
                ChargerStatusInterval(f"{i}", i * 1000, (i + 1) * 1000, True) for i in range(1_000_000)
            ],
            "expected": 100.0 
        },
    ]

    for i, test in enumerate(tests):
        result = get_uptime(test["intervals"])
        assert abs(result - test["expected"]) < 1e-6, f"Test {i + 1} failed: {test['description']}. Expected {test['expected']}, got {result:.2f}"
        print(f"Test {i + 1} passed: {test['description']}.")

if __name__ == "__main__":
    run_tests()
