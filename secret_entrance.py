def calculate_safe_password(rotations_input):
    """
    Calculates the number of times the safe dial points to 0 after a sequence of rotations.

    The dial has 100 positions (0 through 99).
    The starting position is 50.
    """
    # 1. Initialize variables
    current_position = 50
    zero_count = 0
    DIAL_SIZE = 100

    # The rotations input as a multiline string (your attached document)
    # R2
    # R40
    # ...
    rotations = rotations_input.strip().split('\n')

    # 3. Process each rotation
    for rotation in rotations:
        # Parse the rotation: 'L' or 'R' direction, and distance
        direction = rotation[0]
        try:
            distance = int(rotation[1:])
        except ValueError:
            print(f"Skipping invalid rotation format: {rotation}")
            continue

        # 4. Update the current position
        if direction == 'R':
            # Right turn (positive distance).
            # We use the modulo operator (%) to handle wrapping (e.g., 99 + 1 = 100, 100 % 100 = 0)
            current_position = (current_position + distance) % DIAL_SIZE
        elif direction == 'L':
            # Left turn (negative distance).
            # To handle negative results of subtraction correctly in Python's modulo,
            # we add DIAL_SIZE before the modulo operation.
            signed_distance = -distance
            current_position = (current_position + signed_distance) % DIAL_SIZE
        else:
            # Should not happen based on the puzzle description
            print(f"Skipping unknown direction: {direction}")
            continue

        # 5. Check if the new position is 0
        if current_position == 0:
            zero_count += 1

    # 6. Return the final count
    return zero_count