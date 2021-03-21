import pytest
import morse


@pytest.mark.parametrize('s,exp', [
    ('... --- ...', 'SOS'),
    ('-.- . -.-', 'KEK'),
    ('-.-- . ...', 'YES'),
    ('-- -.--   ... ..- .--. . .-.   - . ... -',
     'MY SUPER TEST')
])
def test_decode(s, exp):
    assert morse.decode(s) == exp
