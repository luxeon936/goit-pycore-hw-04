from os import path as file_path

def get_cats_info(path: str) -> list[dict]:
    """
    Read file and transform data in it to list of dictionaries

    Returns:
        List of dicts 
    """
    if file_path.exists(path):
        with open(path, 'r', encoding='utf-8') as fh:
            lines = fh.readlines()
        parsed_lines = []
        for line in lines:
            parsed_lines.append(line.strip().split(','))
        dict_keys = ['id', 'name', 'age']
        return [dict(zip(dict_keys,vals)) for vals in parsed_lines]
    return 'File not exist'