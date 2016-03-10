import sys
if sys.version_info[0] == 3:
    from unittest import TestCase
    from unittest.mock import patch
elif sys.version_info[0] == 2:
    from mock import patch
    if sys.version_info[1] < 7:
        from unittest2 import TestCase
    else:
        from unittest import TestCase
