import re
from ansible import errors
from ansible.parsing.yaml.objects import AnsibleUnicode


#
# Additionnal Jinja2 filter to validate positive_integer values
#

def vsftpd_octal_mode_validate(arg):
    """
        Validate octal mode value from integer or string type

        :param arg: the brute value to be translated
        :type arg: str
        :type arg: int
        :return: The validated value
        :rtype: int
    """

    RE = re.compile('^\s*(?P<octal_mode>0[0-7]{3})\s*$')
    VALID_TYPES = [ str, int, AnsibleUnicode ]

    arg_type = type(arg)
    data = str(arg)

    # Check if arg is a string with managed content or boolean
    if arg_type not in VALID_TYPES:
        raise errors.AnsibleFilterError(
            'Invalid value type "%s" for "%s" should be String or Integer' %
            (arg_type, arg))

    # If argument type is int, convert it to octal base format
    if arg_type is int:
        data = '0' + str(format(arg, 'o'))

    match = RE.match(data)

    if not match:
        raise errors.AnsibleFilterError(
            'Invalid value: "%s" should contains linux octal mode' % arg)

    return match.group('octal_mode')


class FilterModule(object):
    """ Filters to manage vsftpd configuration with octal mode values"""

    filter_map = {
        'vsftpd_octal_mode_validate': vsftpd_octal_mode_validate
    }
    def filters(self):
        return self.filter_map

