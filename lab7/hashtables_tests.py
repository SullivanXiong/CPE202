""" Contains the classes for LinkedList implementation of lab 7
Name: Sullivan Xiong
CPE202 Section 03
Spring 2019
"""

from hashtables import *
import unittest


class TestCases(unittest.TestCase):

    def test_hash_string(self):
        self.assertEqual(hash_string("c", 11), 0)
        self.assertEqual(hash_string("a", 11), 9)
        self.assertEqual(hash_string("c", 23), 7)
        self.assertEqual(hash_string("a", 23), 5)
        self.assertEqual(hash_string("d", 23), 8)
        self.assertEqual(hash_string("d", 47), 6)
        
    def test_HashTableSepchain(self):
        hashtable = HashTableSepchain()
        hashtable.put("\\", "\\")
        hashtable.put("a", "a")
        hashtable.put("b", "b")
        hashtable.put("c", "c")
        hashtable.put("d", "d")
        hashtable.put("e", "e")
        hashtable.put("f", "f")
        hashtable.put("g", "g")
        hashtable.put("h", "h")
        hashtable.put("i", "i")
        hashtable.put("j", "j")
        hashtable.put("k", "k")
        hashtable.put("l", "l")
        hashtable.put("cc", "cc")
        hashtable.put("\\\\", "\\\\")
        hashtable.put("\\\\\\", "\\\\\\")
        
    def test_HashTableSepchain_import_stopwords(self):
        hashtable = HashTableSepchain()
        # import_stopwords("stop_words.txt", hashtable)
        
    def test_HashTableLinear(self):
        hashtable = HashTableLinear()
        hashtable.put("\\", "\\")
        hashtable.put("a", "a")        
        hashtable.put("b", "b")        
        hashtable.put("c", "c")        
        hashtable.put("d", "d")        
        hashtable.put("cc", "cc")        
        hashtable.put("e", "e")        
        hashtable.put("f", "f")        
        hashtable.put("g", "g")        
        hashtable.put("h", "h")        
        hashtable.put("i", "i")        
        hashtable.put("j", "j")        
        hashtable.put("k", "k")        
        hashtable.put("l", "l")        
        hashtable.put("\\\\", "\\\\")        
        hashtable.put("\\\\\\", "\\\\\\")
        hashtable.remove("\\\\")
        hashtable.remove("\\")
        
    def test_HashTableLinear_import_stopwords(self):
        hashtable = HashTableLinear()
        # import_stopwords("stop_words.txt", hashtable)
        
    def test_HashTableQuadratic(self):
        hashtable = HashTableQuadratic()
        hashtable.put("\\", "\\")
        hashtable.put("b", "b")        
        hashtable.put("c", "c")        
        hashtable.put("d", "d")        
        hashtable.put("cc", "cc")        
        hashtable.put("e", "e")        
        hashtable.put("f", "f")        
        hashtable.put("g", "g")        
        hashtable.put("h", "h")        
        hashtable.put("i", "i")        
        hashtable.put("j", "j")        
        hashtable.put("k", "k")        
        hashtable.put("l", "l")        
        hashtable.put("\\\\", "\\\\")        
        hashtable.put("\\\\\\", "\\\\\\")
        hashtable.remove("\\\\")
        hashtable.remove("\\")
            
    def test_HashTableQuadratic_import_stopwords(self):
        hashtable = HashTableQuadratic()
        # import_stopwords("stop_words.txt", hashtable)

def main():
    # execute unit tests
    unittest.main()

if __name__ == '__main__':
    # execute main() function
    main()
