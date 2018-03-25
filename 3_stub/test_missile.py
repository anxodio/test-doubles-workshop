from tenx_missile import MissileLauncher


class Missile(object):
    def __init__(self):
        self._launcher = MissileLauncher()
        self._disabled = False

    def fire(self):
        if self._disabled:
            raise Exception('Missile is disabled')
        self._launcher.fire()

    def disable(self):
        self._disabled = True


class Code(object):
    _VALID_CODES = ['RDPC', 'BOOM', 'ACME']
    _PASSWORD = 'JONG'

    def __init__(self, code, password):
        self._unsigned = False
        self._invalid = False
        self._check_code(code, password)

    def _check_code(self, code, password):
        if password != self._PASSWORD:
            self._unsigned = True
        elif code not in self._VALID_CODES:
            self._invalid = True

    def is_unsigned(self):
        return self._unsigned

    def is_invalid(self):
        return self._invalid


def launch_missile(missile, code):
    if code.is_unsigned or code.is_invalid:
        # CODE RED ABORT
        missile.disable()
    else:
        missile.fire()


#############
# TEST CODE #
#############

# Copy here the mock from the last exercice

# And here... Stuby Doo!


def test_launch_missile():
    missile_mock = None  # replace with the mock
    correct_code_stub = None  # replace with the stub
    launch_missile(missile_mock, correct_code_stub)
    # assert that was fired


def test_launch_missile_with_invalid_code():
    missile_mock = None  # replace with the mock
    invalid_code_stub = None  # replace with the stub
    launch_missile(missile_mock, invalid_code_stub)
    # assert code red abort


def test_launch_missile_with_unsigned_code():
    missile_mock = None  # replace with the mock
    unsigned_code_stub = None  # replace with the stub
    launch_missile(missile_mock, unsigned_code_stub)
    # assert code red abort
