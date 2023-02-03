import operator

class MissionariesAndCannibals:

    def _init_(self):
        initial_state = State.value_of(INITIAL_STATE)
        goal_state = State.value_of(GOAL_STATE)
        super()._init_(initial_state, goal_state)

    def actions(self, state):
        all_actions = self.get_all_actions()
        return self.get_valid_actions(state, all_actions)

    @staticmethod
    def get_all_actions():
        return {
            (1, 0, 1),
            (2, 0, 1),
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1)
        }

    def get_valid_actions(self, state, all_actions):
        is_action_valid_lambda = self.get_is_action_valid_lambda(state)
        return set(filter(is_action_valid_lambda, all_actions))

    def get_is_action_valid_lambda(self, state):
        return lambda action: self.is_action_valid(state, action)

    def is_action_valid(self, state, action):
        operate = self.get_operation(state.boat)
        result = operate(state, action)
        return result.is_valid()

    def result(self, state, action):
        operate = self.get_operation(state.boat)
        return operate(state, action)

    @staticmethod
    def get_operation(boat):
        """Subtract action from state if boat is on initial side of river."""
        return operator.sub if boat == 1 else opeator.add
