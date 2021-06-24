from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    data_content = instance.return_data()
    result = list()
    for file in data_content:
        file_content = txt_importer(file)
        count = list()
        for index, line in enumerate(file_content):
            if word.casefold() in line.casefold():
                count.append({"linha": index + 1})
        if len(count) != 0:
            occur_result = {
                "palavra": word,
                "arquivo": file,
                "ocorrencias": count
            }
            result.append(occur_result)
    return result


def search_by_word(word, instance):
    data_content = instance.return_data()
    result = list()
    for file in data_content:
        file_content = txt_importer(file)
        count = list()
        for index, line in enumerate(file_content):
            if word.casefold() in line.casefold():
                count.append({
                    "linha": index + 1,
                    "conteudo": line
                })
        if len(count) != 0:
            occur_result = {
                "palavra": word,
                "arquivo": file,
                "ocorrencias": count
            }
            result.append(occur_result)
    return result
