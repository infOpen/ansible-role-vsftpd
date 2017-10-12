"""
Tests about role custom filters
"""

import pytest
from ansible import errors
from filter_plugins.vsftpd_boolean_render import vsftpd_boolean_render
from filter_plugins.vsftpd_positive_integer_validate \
    import vsftpd_positive_integer_validate
from filter_plugins.vsftpd_octal_mode_validate \
    import vsftpd_octal_mode_validate


#
# Tests about vsftpd_boolean_render
#
@pytest.mark.parametrize('arg', [
    ('yes'),
    ('YES'),
    ('Yes'),
    ('true'),
    ('TRUE'),
    ('True'),
    (True)
])
def test_true_vsftpd_boolean_render(arg):
    """
    Test boolean with true values
    """

    assert vsftpd_boolean_render(arg) == 'YES'


@pytest.mark.parametrize('arg', [
    ('no'),
    ('NO'),
    ('No'),
    ('false'),
    ('FALSE'),
    ('False'),
    (False)
])
def test_false_vsftpd_boolean_render(arg):
    """
    Test boolean filter with false values
    """

    assert vsftpd_boolean_render(arg) == 'NO'


@pytest.mark.parametrize('arg', [
    (),
    ([]),
    ({}),
    (1)
])
def test_bad_type_vsftpd_boolean_render(arg):
    """
    Test boolean filter with bad value type
    """

    with pytest.raises(errors.AnsibleFilterError) as errorInfo:
        vsftpd_boolean_render(arg)

    assert 'Invalid value type' in str(errorInfo.value)


@pytest.mark.parametrize('arg', [
    ('foo'),
    (''),
    ('bar')
])
def test_bad_string_vsftpd_boolean_render(arg):
    """
    Test boolean filter with bad string values
    """

    with pytest.raises(errors.AnsibleFilterError) as errorInfo:
        vsftpd_boolean_render(arg)

    assert 'Invalid value: ' in str(errorInfo.value)


#
# Tests about vsftpd_positive_integer_validate
#
@pytest.mark.parametrize('arg', [
    ('10'),
    ('   10 '),
    ('10 '),
    (' 10'),
    (10)
])
def test_valid_vsftpd_positive_integer_validate(arg):
    """
    Test integer filter with valid values
    """

    assert vsftpd_positive_integer_validate(arg) == 10


@pytest.mark.parametrize('arg', [
    (),
    ([]),
    ({})
])
def test_bad_type_vsftpd_positive_integer_validate(arg):
    """
    Test integer filter with bad types
    """

    with pytest.raises(errors.AnsibleFilterError) as errorInfo:
        vsftpd_positive_integer_validate(arg)

    assert 'Invalid value type' in str(errorInfo.value)


@pytest.mark.parametrize('arg', [
    (''),
    ('foo')
])
def test_bad_value_vsftpd_positive_integer_validate(arg):
    """
    Test integer filter with bad string values
    """

    with pytest.raises(errors.AnsibleFilterError) as errorInfo:
        vsftpd_positive_integer_validate(arg)

    assert 'Invalid value: ' in str(errorInfo.value)


#
# Tests about vsftpd_octal_mode_validate
#
@pytest.mark.parametrize('arg', [
    ('0754'),
    ('   0754 '),
    ('0754 '),
    (' 0754'),
    (0754)
])
def test_valid_vsftpd_octal_mode_validate(arg):
    """
    Test octal filter with valid values
    """
    assert vsftpd_octal_mode_validate(arg) == '0754'


@pytest.mark.parametrize('arg', [
    (),
    ([]),
    ({})
])
def test_bad_type_vsftpd_octal_mode_validate(arg):
    """
    Test octal filter with bad types
    """

    with pytest.raises(errors.AnsibleFilterError) as errorInfo:
        vsftpd_octal_mode_validate(arg)

    assert 'Invalid value type' in str(errorInfo.value)


@pytest.mark.parametrize('arg', [
    (''),
    ('foo'),
    (1234),
    (755),
    ('07539'),
    (012)
])
def test_bad_value_vsftpd_octal_mode_validate(arg):
    """
    Test octal filter with bad values
    """

    with pytest.raises(errors.AnsibleFilterError) as errorInfo:
        vsftpd_octal_mode_validate(arg)

    assert 'Invalid value: ' in str(errorInfo.value)
