from ansible import errors


#
# Additionnal Jinja2 filter to convert boolean values to vsftpd format
#

def vsftpd_boolean_render(arg):
    """
        Convert boolean value from boolean or string type to VSFTPD format

        :param arg: the brute value to be translated
        :type arg: str
        :type arg: bool
        :return: The translated value
        :rtype: str
    """

    TRUE_CHOICES = [ 'true', 'yes' ]
    FALSE_CHOICES = [ 'false', 'no' ]
    VALID_CHOICES = TRUE_CHOICES + FALSE_CHOICES
    VALID_TYPES = [ str, bool ]

    arg_type = type(arg)
    arg_lower = str(arg).lower()

    # Check if arg is a string with managed content or boolean
    if arg_type not in VALID_TYPES:
        raise errors.AnsibleFilterError(
            'Invalid value type "%s" for "%s" should be String or Boolean' %
            (arg_type, arg_lower))

    elif arg_lower not in VALID_CHOICES :
        raise errors.AnsibleFilterError(
            'Invalid value: %s not in %s' % (arg_lower, VALID_CHOICES))

    # VSFTPD configuration boolean values should be 'YES' or 'NO'
    if arg_lower in TRUE_CHOICES:
        return 'YES'

    return 'NO'


class FilterModule(object):
    """ Filters to manage vsftpd configuration values"""

    filter_map = {
        'vsftpd_boolean_render': vsftpd_boolean_render
    }
    def filters(self):
        return self.filter_map
