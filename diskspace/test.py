import unittest

from diskspace import *

class DiskspaceTest(unittest.TestCase):
    
    def set_file_tree(self):
        self.file_tree = {'/home/teste': {'print_size': '2.00Kb', 'children': [], 'size': 4}}
        self.file_tree_node = {'print_size': '2.00Kb',
                               'children': [], 'size': 4}
        self.path = '/home/teste'
        self.largest_size = 6
        self.total_size = 4
