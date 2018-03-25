from tenx_missile import MissileLauncher

_VALID_CODES = ['RDPC', 'BOOM', 'ACME']
_PASSWORD = 'JONG'


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
    return '{}+{}'.format(code, password)


def unsign(signed_code, password):
    splitted = signed_code.split('+')
    if len(splitted) != 2 or splitted[1] != password:
        raise ValueError('Invalid signature')
    return splitted[0]


#############
# TEST CODE #
#############

# Coooooomooooock?


def test_launch_missile():
    missile_mock = None  # replace with the mock
    launch_missile(missile_mock, sign('RDPC', _PASSWORD))
    # assert that was fired


def test_launch_missile_with_invalid_code():
    missile_mock = None  # replace with the mock
    launch_missile(missile_mock, 'INVALID')
    # assert code red abort


def test_launch_missile_with_unsigned_code():
    missile_mock = None  # replace with the mock
    launch_missile(missile_mock, 'RDPC')
    # assert code red abort
