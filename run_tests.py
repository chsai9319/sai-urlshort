import sys
import os
import nose
import test

def main() -> object:
    sys.path.insert(0, os.path.dirname(__file__))
    nose.main()
    sys.exit(0)

if __name__ == '__main__':
    main()
    os.system('python test.py' )
