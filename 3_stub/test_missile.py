from tenx_missile import MissileLauncher


class Missile:
    def __init__(self):
        self._launcher = MissileLauncher()
        self._disabled = False

    def fire(self):
        if self._disabled:
            raise Exception('Missile is disabled')
        self._launcher.fire()

    def disable(self):
        self._disabled = True


class Code:
    _VALID_CODES = ['DPRK', 'BOOM', 'ACME']
    _PASSWORD = 'JONG'

    def __init__(self, code, password):
        self._unsigned = False
        self._invalid = False
        self._check_code(code, password)

    def _check_code(self, code, password):
        if password != self._PASSWORD:
            self._unsigned = True
        if code not in self._VALID_CODES:
            self._invalid = True

    def is_unsigned(self):
        return self._unsigned

    def is_invalid(self):
        return self._invalid


def launch_missile(missile, code):
    if code.is_unsigned() or code.is_invalid():
        # CODE RED ABORT
        missile.disable()
    else:
        missile.fire()


#############
# TEST CODE #
#############

# Copy here the mock from the last exercice
class MissileMock:

    def __init__(self):
        self.launch_was_called = False
        self.disable_was_called = False

    def fire(self):
        self.launch_was_called = True

    def disable(self):
        self.disable_was_called = True

    def verify_code_red_abort(self):
        assert not self.launch_was_called
        assert self.disable_was_called


# And here... Stuby Doo!
class CorrectCodeStub:

    def is_unsigned(self):
        return False

    def is_invalid(self):
        return False


class InvalidCodeStub:

    def is_unsigned(self):
        return False

    def is_invalid(self):
        return True


class UnsignedCodeStub:

    def is_unsigned(self):
        return True

    def is_invalid(self):
        return False


def test_launch_missile():
    missile_mock = MissileMock()  # replace with the mock
    correct_code_stub = CorrectCodeStub()  # replace with the stub
    launch_missile(missile_mock, correct_code_stub)
    # assert that was fired
    assert missile_mock.launch_was_called


def test_launch_missile_with_invalid_code():
    missile_mock = MissileMock()  # replace with the mock
    invalid_code_stub = InvalidCodeStub()  # replace with the stub
    launch_missile(missile_mock, invalid_code_stub)
    # assert code red abort
    missile_mock.verify_code_red_abort()


def test_launch_missile_with_unsigned_code():
    missile_mock = MissileMock()  # replace with the mock
    unsigned_code_stub = UnsignedCodeStub()  # replace with the stub
    launch_missile(missile_mock, unsigned_code_stub)
    # assert code red abort
    missile_mock.verify_code_red_abort()
