from document import *
from trie import *
import csv


class Corpus:
    """A corpus of documents that supports:

    - search: given a query, return a list of contained documents ranked by
      relevance
    - compelte: given a query, return prefix-matched words from the corpus
    """

    def __init__(self, path, index=False, trie=True):
        """ Creates the corpus from *.txt files under path.
        
        Args:
        - self: the corpus to create, mandatory object reference
        - path: the documents to add are under path as *.txt files
        - index: construct index if True. 
        - trie: construct trie if True. 

        Returns:
        nothing.
        """
        # The structures that will support the main functionalities.
        self._trie = Trie() if trie else None
        # Initialize the structures with all *.txt files under path.
        path = pathlib.Path(path)
        L = []
        with open('articles.csv', 'r',encoding='utf8') as file:
            reader = csv.reader(file)
            for row in reader:
                doc = Document(row[5])
                if trie:
                    self._trie.add_doc(doc)
        print(f'Built corpus from {i} documents.')

    def complete(self, query: str) -> [(str, Location)]:
        """Returns a list of words from the corpus that prefix-match the words
        in query.

        Each pair in the retruned list contains a word and a Location where the
        word can be found.

        Args:
        - self: mandatory object reference.
        - query: documents are to be sorted according to relevance to query.

        Returns:
        a list of (word, Location) pairs in arbitrary order.
        """
        # Delegete the search to the trie.
        if self._trie:
            return self._trie.complete(query)
