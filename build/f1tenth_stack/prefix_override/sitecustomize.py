import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/simseunghwan/simseunghwan_ws/install/f1tenth_stack'
