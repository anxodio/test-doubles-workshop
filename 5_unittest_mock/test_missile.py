import shelve
from unittest.mock import Mock
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
        self.text = code

    def _check_code(self, code, password):
        if password != self._PASSWORD:
            self._unsigned = True
        elif code not in self._VALID_CODES:
            self._invalid = True

    def is_unsigned(self):
        return self._unsigned

    def is_invalid(self):
        return self._invalid


class UsedLaunchCodes(object):
    def __init__(self):
        self.db = shelve.open('database')

    def add(self, code):
        try:
            codes = self.db['codes']
        except KeyError:
            codes = []
        self.db['codes'] = codes+[code]

    def contains(self, code):
        try:
            codes = self.db['codes']
        except KeyError:
            return False
        return code in codes

    def close(self):
        self.db.close()


def launch_missile(missile, code, used):
    if used.contains(code.text) or code.is_unsigned() or code.is_invalid():
        # CODE RED ABORT
        missile.disable()
    else:
        used.add(code.text)
        missile.fire()


#############
# TEST CODE #
#############

# Now manual doubles are forbidden D:

def test_launch_missile():
    missileMock = Mock(Missile)

    codeStub = Mock(Code)
    # set expected return values

    usedStub = Mock(UsedLaunchCodes)
    # set expected return values

    launch_missile(missileMock, codeStub, usedStub)
    # make assertions about called methods


def test_launch_missile_with_repeated_code():
    missileMock = Mock(Missile)

    codeStub = Mock(Code)
    # set expected return values

    usedStub = Mock(UsedLaunchCodes)
    # make contains return first false, then true

    launch_missile(missileMock, codeStub, usedStub)
    launch_missile(missileMock, codeStub, usedStub)
    # make assertions about called methods
