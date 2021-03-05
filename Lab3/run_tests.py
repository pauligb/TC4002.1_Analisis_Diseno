import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

loader = unittest.TestLoader()
start_dir = "test/"
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)