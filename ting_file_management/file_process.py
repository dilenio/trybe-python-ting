import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if not instance.find_file(path_file):
        content = txt_importer(path_file)
        instance.enqueue(path_file)
        lines = list()
        for line in content:
            lines.append(line)
        lines_count = len(lines)
        result = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": lines_count,
            "linhas_do_arquivo": content
        }

        sys.stdout.write(str(result))


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")
    file = instance.dequeue()
    sys.stdout.write(
        f"Arquivo {file} removido com sucesso\n"
    )


def file_metadata(instance, position):
    if position > instance.__len__() - 1:
        return sys.stderr.write("Posição inválida\n")
