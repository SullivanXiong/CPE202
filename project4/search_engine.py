""" Contains the implementation for searchEngine Project
Name: Sullivan Xiong
CPE202 Section 03
Spring 2019
"""
from hashtables import *
import math
import os

class SearchEngine:
    """ A class that represents a search engine.
    Attributes:
        directory (str) : a directory name
        stopwords (HashMap) : a hash table containing stopwords
        doc_length (HashMap) : a hash table containing the total number of words in each
        document
        doc_freqs (HashMap) : a hash table containing the number of documents containing the
        term for each term
        term_freqs (HashMap) : a hash table of hash tables for each term. Each hash table
        contains the frequency of the term in documents (document names are the keys and the
        frequencies are the values)
    """
    def __init__(self, directory, stopwords):
        self.doc_length = HashTableLinear()
        self.doc_freqs = HashTableLinear()
        self.term_freqs = HashTableLinear()
        self.stopwords = stopwords
        self.index_files(directory)

    def __eq__(self, other):
        return isinstance(other, SearchEngine)\
            and self.doc_length == other.doc_length\
            and self.doc_freqs == other.doc_freqs\
            and self.term_freqs == other.term_freqs\
            and self.stopwords == other.stopwords\
            and self.index_files == other.index_files\

    def __repr__(self):
        return "SearchEngine({}, {}, {}, {}, {})".format(self.doc_length and\
            self.doc_freqs, self.term_freqs, self.stopwords, self.index_files)
    
    def read_file(self, infile):
        """A helper function to read a file
        Args:
            infile (str) : the path to a file
        Returns:
            list : a list of str read from a file
        """
        with open(infile, "r") as input_file:
            lines = input_file.readlines()
            return lines
            
    def parse_words(self, lines):
        """split strings into words
        Convert words to lower cases and remove new line chars.
        Exclude stopwords.
        Args:
            lines (list) : a list of strings
        Returns:
            list : a list of words
        """
        non_stopwords_list = []
        for line in lines:
            line = line.replace("/n", "")
            line = line.split()
            for word in line:
                if self.stopwords.contain(word) is False:
                    non_stopwords_list.append(word.lower())
        return non_stopwords_list

    def count_words(self, filename, words):
        """count words in a file and store the frequency of each
        word in the term_freqs hash table. Words should not contain stopwords.
        Also store the total count of words contained in the file
        in the doc_length hash table.
        Args:
            filename (str) : the file name
            words (list) : a list of words
        """
        file_hashtable = HashTableLinear()
        count = 0
        while count < len(words):
            if file_hashtable.contains(words[count]):
                index = file_hashtable.get_index(words[count])
                file_hashtable.hash_table[index][1] += 1
            else:
                file_hashtable.put(words[count], 1)
            count += 1
        self.term_freqs.put("{}".format(filename), file_hashtable)
        self.doc_length.put("{}".format(filename), count)

    def index_files(self, directory):
        """index all text files in a given directory
        Args:
            directory (str) : the path of a directory
        """
        list_of_directories = os.listdir(directory)
        for item in list_of_directories:
            os.path.join(directory, item)
            if os.path.isfile(item):
                parts = os.path.splitext(item)
                if parts[1] == '.txt':
                    non_stopwords_list = self.parse_words(self.read_file(item))
                    self.count_words(item, non_stopwords_list)

    def get_wf(self, tf):
        """comptes the weighted frequency
        Args:
            tf (float) : term frequency
        Returns:
            float : the weighted frequency
        """
        if tf > 0:
            wf = 1 + math.log(tf)
        else:
            wf = 0
        return wf

    def get_scores(self, terms):
        """creates a list of scores for each file in corpus
        The score = weighted frequency / the total word count in the file.
        Compute this score for each term in a query and sum all the scores.
        Args:
            terms (list) : a list of str
        Returns:
            list : a list of tuples, each containing the filename and its relevancy score
        """
        # The code listed below is pseudo code
        # scores = HashMap()
        # For each query term t
            # Fetch a hash table of t from self.term_freqs
            # For each file in the hash table, add wf to scores[file]
        # For each file in scores, do scores[file] /= self.doc_length[file]
        # Return scores
        scores = HashTableLinear()
        for t in terms:
            list_of_files = self.term_freqs.get_all_keys()
            for _file in list_of_files:
                hash_table = self.term_freqs.get(_file)
                if hash_table.contains(t):
                    index = hash_table.get_index(t)
                    item = hash_table.hash_table[index]
                    if scores.contains(_file):
                        index = scores.get_index(_file)
                        scores.hash_table[index][1] += item[1]
                    else:
                        scores.put(_file, self.get_wf(item[1]))
        files_in_scores = scores.get_all_keys()
        for file_in_scores in files_in_scores:
            score = scores.get(file_in_scores)[1]
            doc_length = self.doc_length.get(file_in_scores)[1]
            scores.remove(file_in_scores)
            scores.put(file_in_scores, score/doc_length)
        return scores

    def rank(self, scores):
        """ranks files in the descending order of relevancy
        Args:
            scores: a hashtable of scores.
        Returns:
            list : a list of filenames sorted in descending order of relevancy
        """
        all_files = scores.get_all_keys()
        sorted_list = []
        for _file in all_files:
            item = scores.get(_file)
            sorted_list.append([item[1], item[0]])
        sorted(sorted_list, key=lambda x:x[1], reverse=True)
        return sorted_list

    def search(self, query):
        """ search for the query terms in files
        Args:
            query (str) : query input
        Returns:
            list : list of files in descending order or relevancy
        """
        words = query.split()
        all_words = HashTableLinear()
        for word in words:
            word = word.lower()
            if all_words.contains(word) is False:
                all_words.put(word, word)
        parsed_words_list = all_words.get_all_keys()
        scores = self.get_scores(parsed_words_list)
        return self.rank(scores)
