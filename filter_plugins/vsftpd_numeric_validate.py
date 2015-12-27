import re
from ansible import errors


#
# Additionnal Jinja2 filter to validate numeric values with vsftpd rules
#

def vsftpd_numeric_validate(arg):
    """
        Validate numeric value from integer or string type to VSFTPD format

        :param arg: the brute value to be translated
        :type arg: str
        :type arg: int
        :return: The validated value
        :rtype: int
    """

    RE = re.compile('^\s*(?P<numeric_value>\d+)\s*$')
    VALID_TYPES = [ str, int ]

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
    """ Filters to manage vsftpd configuration with numeric values"""

    filter_map = {
        'vsftpd_numeric_validate': vsftpd_numeric_validate
    }
    def filters(self):
        return self.filter_map

