import re
from ansible import errors
from ansible.parsing.yaml.objects import AnsibleUnicode


#
# Additionnal Jinja2 filter to validate positive_integer values
#

def vsftpd_positive_integer_validate(arg):
    """
        Validate positive integer value from integer or string type

        :param arg: the brute value to be translated
        :type arg: str
        :type arg: int
        :return: The validated value
        :rtype: int
    """

    RE = re.compile('^\s*(?P<numeric_value>\d+)\s*$')
    VALID_TYPES = [ str, int, AnsibleUnicode ]

    arg_type = type(arg)

    # Check if arg is a string with managed content or boolean
    if arg_type not in VALID_TYPES:
        raise errors.AnsibleFilterError(
            'Invalid value type "%s" for "%s" should be String or Integer' %
            (arg_type, arg))

    match = RE.match(str(arg))

    if not match:
        raise errors.AnsibleFilterError(
            'Invalid value: "%s" should contains numeric data' % arg)

    return int(match.group('numeric_value'))


class FilterModule(object):
    """ Filters to manage vsftpd configuration with positive integer values"""

    filter_map = {
        'vsftpd_positive_integer_validate': vsftpd_positive_integer_validate
    }
    def filters(self):
        return self.filter_map

