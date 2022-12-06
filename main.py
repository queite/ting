from ting_file_management.file_process import process, remove
from ting_file_management.queue import Queue
from ting_word_searches.word_search import exists_word, search_by_word

queue = Queue()

process('./statics/arquivo_teste.txt', queue)
print(exists_word('políticas', queue), end='\n')

process('./statics/nome_pedro.txt', queue)
print(search_by_word('amiga', queue), end='\n')

remove(queue)
