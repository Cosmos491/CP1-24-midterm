import pytest
import numpy as np
from your_module import calculate_direction  # Replace 'your_module' with your actual module name

def test_calculate_direction():
    # Example acceleration data
    acceleration_data = [
        [0.17, 0.15, 0.00],  # Test with real values
        [0.18, 0.16, 0.01],  # Another set
        [0.0, 0.0, 0.0],     # Edge case: no acceleration
    ]
    
    expected_directions = [
        (0.7442084075352504, 0.656646520248929, 0.0),
        (0.7452413140023664, 0.6620357900020919, 0.041402295222354796),
        (0, 0, 0),  # No acceleration
    ]

    directions = calculate_direction(acceleration_data)
    
    for i in range(len(directions)):
        assert directions[i] == pytest.approx(expected_directions[i], rel=1e-6)

    # Test with edge case: acceleration values are all 0
    zero_acceleration = [[0, 0, 0]]
    assert calculate_direction(zero_acceleration) == [(0, 0, 0)]