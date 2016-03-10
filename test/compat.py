import six
if six.PY3:
    from unittest import TestCase
    from unittest.mock import patch
else:
    from unittest2 import TestCase
    from mock import patch
