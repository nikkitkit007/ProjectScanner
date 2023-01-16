import os


class Directory:
    def __init__(self, dir_path: str):
        self.dir_path = dir_path

    def get_files_list(self, dir_path: str, files_list: list, recursive: bool = True) -> list:
        files_in_dir = os.listdir(dir_path)

        for file in files_in_dir:
            file_path = dir_path + "/" + file
            if recursive:
                if os.path.isdir(file_path):  # для каждой директории выполняем поиск
                    self.get_files_list(file_path, files_list),
                else:  # для каждого файла проверяем его расширение
                    files_list += file_path,
            else:
                files_list += file_path,

        return files_list

    def get_files_spec_ext(self, file_extensions: list[str], all_files: list = None, dir_path: str = None) -> list:
        files_spec = []

        if not all_files:
            if not dir_path:
                dir_path = self.dir_path

            all_files = self.get_files_list(dir_path, [])

        for file in all_files:
            if Directory.is_file_have_extension(file_extensions=file_extensions, file_name=file):
                files_spec += file,

        return files_spec

    @staticmethod
    def print_files_relatively(files: list, root: str, extension: bool = False) -> list:
        files_rel = []
        root += '/'

        if extension:
            for file in files:
                files_rel += file.replace(root, ""),
        else:
            for file in files:
                f_rel = file.replace(root, "")
                f_rel = f_rel[:f_rel.rfind(".")]

                files_rel += f_rel,

        return files_rel

    @staticmethod
    def is_file_have_extension(file_name: str, file_extensions: list, ) -> bool:
        for extension in file_extensions:
            if file_name[-len(extension):] == extension:
                return True
        return False
