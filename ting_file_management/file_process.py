import sys

from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file: str, instance: Queue):
    for i in range(len(instance)):
        searched_item = instance.search(i)
        if searched_item['nome_do_arquivo'] == path_file:
            return None

    txt_import = txt_importer(path_file)
    new_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_import),
        "linhas_do_arquivo": txt_import
    }

    instance.enqueue(new_dict)
    print(new_dict)
    sys.stdout.write(str(new_dict))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
