""" class HumanPlayer:
EXIT_CODE = "q"
ALLOWED_STEP_KEYS = ['a', 's', 'd']

    def get_input(self) -> str:
         """"""Gets a step from the human player. """"""
        message = f"Choose your step {ALLOWED_STEP_KEYS} ({EXIT_CODE} to quit): "
        step = input(message)
        if step == EXIT_CODE:
            exit("Bye!")
        return step

    def validate_step(self, step) -> bool:
        if step not in ALLOWED_STEP_KEYS:
            print(
                f"Error: Unrecognised step: {step}. "
                f"Please choose from {ALLOWED_STEP_KEYS}.")
            return False
        return True

    def get_step(self) -> int:
         """"""Get the pot to move from the user. """"""
        have_valid_input = False
        while not have_valid_input:
            step = self.get_input()
            if self.validate_step(step):
                return ALLOWED_STEP_KEYS.index(step) """

"""Reformated get_input and validate_step is merged"""
class HumanPlayer:
    EXIT_CODE = "q"
    ALLOWED_STEP_KEYS = { 'a': 0, 's': 1, 'd': 2 }

    def get_valid_input(self) -> int:
        while True:
            message = f"Choose your step {list(self.ALLOWED_STEP_KEYS.keys())} ({self.EXIT_CODE} to quit):"
            step = input(message)
            if step == self.EXIT_CODE:
                exit("Game terminated")
            if step in self.ALLOWED_STEP_KEYS:
                return self.ALLOWED_STEP_KEYS[step]
            print(f"Error: Unrecognised step: {step}. Please choose from {list(self.ALLOWED_STEP_KEYS.keys())}.")


    def get_step(self) -> int:
        return self.get_valid_input()


