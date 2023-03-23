from cli import CommandLineInterface


def test_run_tests_in_file():
    command = CommandLineInterface()
    assert command.run_tests(
    ) == False, "Can't pass tests before running tests, function must return False"

    test = command.obtain_tests()
    command.run_tests(test)

    assert command.run_tests(test) == True, "Tests should be succesful"


def test_time_elapsed_test_execution():
    command = CommandLineInterface
    assert command.run_tests(
    ) == False, "Can't pass tests before running tests, function must return False"

    time = command.elapsed_time_running()

    assert time == 12, "Time must match elapsed time"


def test_find_flags():
    command = CommandLineInterface
    assert command.obtain_command(
        "pytest.py -v") == "pytest.py -v", "Command returned must match argument"

    flags = command.find_flags()

    assert flags == "-v", "Flags found are incorrect"
