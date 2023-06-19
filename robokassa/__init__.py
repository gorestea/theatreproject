import sys


VERSION = (1, 3, 3)


def get_version():
    return '.'.join(map(str, VERSION))


PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3


def to_unicode(value):
    try:
        return unicode(value)
    except NameError:
        return str(value)


def python_2_unicode_compatible(klass):
    if PY2:
        if '__str__' not in klass.__dict__:
            raise ValueError("@python_2_unicode_compatible cannot be applied "
                             "to %s because it doesn't define __str__()." %
                             klass.__name__)
        klass.__unicode__ = klass.__str__
        klass.__str__ = lambda self: self.__unicode__().encode('utf-8')
    return klass
