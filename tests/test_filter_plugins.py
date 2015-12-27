import pytest
from ansible import errors
from filter_plugins.vsftpd_boolean_render import vsftpd_boolean_render


#==============================================================================
# Tests
#==============================================================================

@pytest.mark.parametrize('arg', [
    ('yes'),
    ('YES'),
    ('Yes'),
    ('true'),
    ('True'),
    ('true'),
    (True)
])
def test_true_vsftpd_boolean_render(arg):
    assert vsftpd_boolean_render(arg) == 'YES'

@pytest.mark.parametrize('arg', [
    ('no'),
    ('NO'),
    ('No'),
    ('false'),
    ('False'),
    ('false'),
    (False)
])
def test_false_vsftpd_boolean_render(arg):
    assert vsftpd_boolean_render(arg) == 'NO'

@pytest.mark.parametrize('arg', [
    (),
    ([]),
    ({}),
    (1)
])
def test_bad_type_vsftpd_boolean_render(arg):
    with pytest.raises(errors.AnsibleFilterError) as errorInfo:
        vsftpd_boolean_render(arg)

    assert 'Invalid value type' in str(errorInfo.value)

@pytest.mark.parametrize('arg', [
    ('foo'),
    (''),
    ('bar')
])
def test_bad_string_vsftpd_boolean_render(arg):
    with pytest.raises(errors.AnsibleFilterError) as errorInfo:
        vsftpd_boolean_render(arg)

    assert 'Invalid value: ' in str(errorInfo.value)

