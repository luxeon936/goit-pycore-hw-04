from os import path as file_path

def total_salary(path: str) -> tuple[int]:
    """
    Calculate total and average salary

    Returns:
        Tuple of ints 
    """
    if file_path.exists(path):
        with open(path, 'r', encoding='utf-8') as fh:
            lines = fh.readlines()
        parsed_lines = []
        for line in lines:
            parsed_lines.append(line.strip().split(','))
        salaries = []
        salaries = [int(i[1]) for i in parsed_lines]
        return sum(salaries), sum(salaries)/len(salaries)
    return 'File not exist'