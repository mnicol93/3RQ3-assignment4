class CommandLineInterface:

    def obtain_command(self, command):
        return command
    # Identify the source of the tests to be run

    def obtain_tests(self):
        return "test.py"

    # Runs tests passed by CLI
    def run_tests(self, src=None):
        return False

    # If any flags are added to the command passed to the CLI, identify them
    def find_flags(self, command=None):
        return None

    # Returns time elapsed from start of the first test until completion of all tests.
    def elapsed_time_running(self, tests):
        return 0
