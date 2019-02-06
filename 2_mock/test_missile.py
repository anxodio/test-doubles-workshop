from tenx_missile import MissileLauncher

_VALID_CODES = ['DPRK', 'BOOM', 'ACME']
_PASSWORD = 'JONG'


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


def launch_missile(missile, code):
    try:
        check_code(code)
        missile.fire()
    except ValueError:
        # CODE RED ABORT
        missile.disable()


def check_code(code):
    unsigned_code = unsign(code, _PASSWORD)
    if unsigned_code not in _VALID_CODES:
        raise ValueError('Invalid code')


def sign(code, password):
    return f'{code}+{password}'


def unsign(signed_code, password):
    splitted = signed_code.split('+')
    if len(splitted) != 2 or splitted[1] != password:
        raise ValueError('Invalid signature')
    return splitted[0]


#############
# TEST CODE #
#############

# Coooooomooooock?
class MissileSpy:

    def __init__(self):
        self.launch_was_called = False
        self.disable_was_called = False

    def fire(self):
        self.launch_was_called = True

    def disable(self):
        self.disable_was_called = True


def assert_code_red_abort(missile_spy):
    assert not missile_spy.launch_was_called
    assert missile_spy.disable_was_called


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


def test_launch_missile():
    missile_mock = MissileMock()  # replace with the mock
    launch_missile(missile_mock, sign('DPRK', _PASSWORD))
    # assert that was fired
    assert missile_mock.launch_was_called


def test_launch_missile_with_invalid_code():
    missile_mock = MissileMock()  # replace with the mock
    launch_missile(missile_mock, 'INVALID')
    # assert code red abort
    # assert not missile_mock.launch_was_called
    # assert missile_mock.disable_was_called
    # assert_code_red_abort(missile_mock)
    missile_mock.verify_code_red_abort()


def test_launch_missile_with_unsigned_code():
    missile_mock = MissileMock()  # replace with the mock
    launch_missile(missile_mock, 'DPRK')
    # assert code red abort
    # assert not missile_mock.launch_was_called
    # assert missile_mock.disable_was_called
    # assert_code_red_abort(missile_mock)
    missile_mock.verify_code_red_abort()
