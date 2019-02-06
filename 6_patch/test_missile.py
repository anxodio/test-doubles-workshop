import urllib.request
from urllib.error import URLError
from http.client import HTTPException
from unittest.mock import patch
import tenx_missile


class Missile:
    _CODES_URL = 'http://www.korea-dpr.com/katallonian-codes.php'

    def __init__(self):
        self._launcher = tenx_missile.MissileLauncher()
        self._codes = self._get_actual_codes()

    def _get_actual_codes(self):
        try:
            contents = urllib.request.urlopen(self._CODES_URL).read()
            # Ocasionally some br tags come with an space before the slash
            contents = contents.replace('<br />', '<br/>')
            codes = contents.split('<br/>')
        except (URLError, HTTPException):
            codes = []
        finally:
            return codes

    def fire(self, code):
        if code in self._codes:
            self._launcher.fire()


#############
# TEST CODE #
#############

# a patchy server :3

@patch('tenx_missile.MissileLauncher')
@patch.object(Missile, '_get_actual_codes')
def test_fire_missile(get_codes_mock, launcher_mock):
    # make _get_actual_codes return ['valid_code']
    get_codes_mock.return_value = ['valid_code']
    missile = Missile()
    missile.fire('valid_code')
    # assert that MissileLauncher was fired
    launcher_mock().fire.assert_called_once()


@patch('tenx_missile.MissileLauncher')
@patch.object(Missile, '_get_actual_codes')
def test_fire_missile_fails_invalid_code(get_codes_mock, launcher_mock):
    # make _get_actual_codes return ['valid_code']
    get_codes_mock.return_value = ['valid_code']
    missile = Missile()
    missile.fire('invalid_code')
    # assert that MissileLauncher was NOT fired
    launcher_mock().fire.assert_not_called()


@patch('tenx_missile.MissileLauncher')
@patch('urllib.request')
def test_get_actual_codes(request_mock, launcher_mock):
    # make urllib.request...read return 'DPRK<br/>BOOM<br />ACME'
    request_mock.urlopen.return_value.read.return_value = (
        'DPRK<br/>BOOM<br />ACME')
    missile = Missile()
    assert missile._codes == ['DPRK', 'BOOM', 'ACME']


@patch('tenx_missile.MissileLauncher')
@patch('urllib.request')
def test_get_actual_codes_fails(request_mock, launcher_mock):
    # make urllib.request...read raise a HTTPException'
    request_mock.urlopen.return_value.read.side_effect = HTTPException
    missile = Missile()
    assert missile._codes == []
