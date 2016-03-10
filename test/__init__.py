import sys, types
sys.modules['pandas'] = types.ModuleType('pandas', 'Fake pandas module')
del sys
del types
