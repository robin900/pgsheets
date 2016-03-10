import os
if os.environ.get('TRAVIS') or os.environ.get('CI'):
    import sys, types
    sys.modules['pandas'] = types.ModuleType('pandas', 'Fake pandas module')
