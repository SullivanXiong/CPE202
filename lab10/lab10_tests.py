import unittest
from lab10 import *
from bst_rb import *

class TestCases(unittest.TestCase):

    def test_TreeMap(self):
        tmap = TreeMap()
        self.assertEqual(tmap.size(), 0)
        tmap.put("Smith", Classmate("Smith", "John", "SE", "Freshman"))
        tmap.put("Lincoln", Classmate("Lincoln", "Abraham", "CSC", "Sophomore"))
        tmap.put("Washington", Classmate("Washington", "George", "CPE", "Freshman"))
        self.assertEqual(tree_height(tmap.tree), 1)
        self.assertEqual(tmap.contains("Smith"), True)
        self.assertEqual(tmap.contains("Trump"), False)
        self.assertEqual(tmap.get("Washington").data, Classmate("Washington", "George", "CPE", "Freshman"))
        self.assertEqual(tmap.get("Trump"), None)
        self.assertEqual(tmap.size(), 3)
        tmap.put("Adams", Classmate("Adams", "John", "BUS", "Sophomore"))
        tmap.put("Obama", Classmate("Obama", "Barrack", "ME", "Sophomore"))
        tmap.put("Trump", Classmate("Trump", "Donald", "EE", "Sophomore"))
        tmap.put("Washington2", Classmate("Washington2", "George", "PHYS", "Senior"))
        self.assertEqual(find_min(tmap.tree).data, Classmate("Adams", "John", "BUS", "Sophomore"))
        self.assertEqual(find_max(tmap.tree).data, Classmate("Washington2", "George", "PHYS", "Senior"))
        self.assertEqual(tree_height(tmap.tree), 3)
        self.assertEqual(tmap.size(), 7)
        self.assertEqual(inorder_list(tmap.tree)[-1], "Washington2")
        self.assertEqual(preorder_list(tmap.tree)[-1], "Washington2")
        tmap.delete("Smith")
        self.assertEqual(tmap.contains("Smith"), False)
        self.assertEqual(tmap.size(), 6)
        tmap.delete("Washington")
        self.assertEqual(tmap.contains("Washington"), False)
        self.assertEqual(tmap.size(), 5)
        tmap.delete("Washington2")
        self.assertEqual(tmap.contains("Washington2"), False)
        self.assertEqual(tmap.size(), 4)

    def test_classmate_functions(self):
        tmap = import_classmates("classmates.tsv")
        self.assertEqual(tmap.size(), 33)
        me = search_classmate(tmap, "Xiong")
        self.assertEqual(me.data.first, "Sullivan")

def main():
    # execute unit tests
    unittest.main()

if __name__ == '__main__':
    # execute main() function
    main()
