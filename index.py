import os

tree = os.walk('folder')


def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        # print(root, dirs, files)
        # os.sep - это сепоратор (направление слеша в операционной системе)
        level = root.count(os.sep)
        indent = ' ' * 4 * level
        sub_indent = ' ' * 4 * (level + 1)
        # os.path.basename(root) вернет базовый путь (имя папки в пути)
        print(f'{indent}[{os.path.basename(root)}]')
        for file in files:
            print(f'{sub_indent}{file}')



read_dir('folder')
