# Temperature thresholds
LOW_TEMP = 18
HIGH_TEMP = 28


class TemperatureController:
    def __init__(self):
        # Remember the previous target mode
        self.previous_mode = None

    def decide_mode(self, temperature, occupied):
        # Occupancy has priority
        if not occupied:
            target_mode = "OFF"

        elif temperature <= LOW_TEMP:
            target_mode = "HEAT"

        elif temperature >= HIGH_TEMP:
            target_mode = "COOL"

        else:
            target_mode = "NORMAL"

        # Avoid sending an identical command
        send_command = target_mode != self.previous_mode

        # Update stored mode
        if send_command:
            self.previous_mode = target_mode

        return target_mode, send_command


def run_tests():
    controller = TemperatureController()

    test_cases = [
        (30, True, "Hot room"),
        (30, True, "Repeated hot-room percept"),
        (28, True, "Exact upper boundary"),
        (22, True, "Normal temperature"),
        (18, True, "Exact lower boundary"),
        (15, True, "Cold room"),
        (15, False, "Empty room"),
        (15, False, "Repeated empty-room percept"),
    ]

    for temperature, occupied, description in test_cases:
        target, send = controller.decide_mode(
            temperature, occupied
        )

        command_status = "SEND" if send else "NO COMMAND"

        print(
            f"{description}: "
            f"Temp={temperature}°C, "
            f"Occupied={occupied}, "
            f"Target={target}, "
            f"Command={command_status}"
        )


if __name__ == "__main__":
    run_tests()