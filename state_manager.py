class StateManager:
    """ State Management Module """

    def __init__(self, unit_id, state_id=None):
        """
        Initializes the State Manager with the unit type and initial state

        Args:
            unit_id:    Unit Type of AI
            state_id:   Starting state (optional)
        """

        if state_id is None:
            self.state_id = unit_id
        else:
            self.state_id = state_id
        self.unit_id = unit_id

    def advance(self, *args):
        """
        Perform the current state action and update next state

        Args:
            *args:  any and all external arguments necessary. Avoid usage if possible.
                    Use local variables instead.

        Return:
            Current state output. Also updates the next state.
        """

        self.state_id, output = self.state_table[self.state_id](self, *args)
        return output

    # Test states
    def tank_attack(self, danger=False):
        if danger:
            return 'G1', 'aaaaa!'
        else:
            return 'T0', "BOOM"

    def rifleman_attack(self, danger=False):
        if danger:
            return 'G1', 'aaaaa!'
        else:
            return 'R0', "boom"

    def run(self):
        return 'G1', "aaaaa!"

    # Dictionary of all states
    state_table = {'T0': tank_attack,
                   'R0': rifleman_attack,
                   'G1': run}
