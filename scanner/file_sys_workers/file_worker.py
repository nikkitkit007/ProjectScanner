
class File:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_file_by_lines(self) -> list:
        with open(self.file_path) as f:
            lines = [line.rstrip() for line in f]
        for i, line in enumerate(lines):
            lines[i] = line.split(" ")
        return lines

    def _find_links_py(self, lines_for_analysis: list[str], all_files: list) -> list:
        """
        find 'import' and 'from'
        """
        links = []
        special_words = ["from"]

        for line in lines_for_analysis:
            for word in special_words:
                try:
                    link = line[line.index(word) + 1]
                    link = link.replace(".", "/")

                    if link in all_files:
                        links += link,
                    break
                except:
                    pass

        return links

    def find_links(self, possible_links: list) -> list:
        file_extension = self.file_path[self.file_path.rindex("."):]
        links = []

        match file_extension:
            case ".py":
                lines = self.read_file_by_lines()
                links = self._find_links_py(lines, possible_links)

        return links

    @staticmethod
    def get_dist(file1_path: str, file2_path: str) -> int:
        dist = 0

        f1_path = file1_path.split("/")
        f2_path = file2_path.split("/")

        for i in range(len(f1_path)):
            if f1_path[i] != f2_path[i]:
                break
            dist -= 1 * 2

        dist += len(f1_path) + len(f2_path)

        return dist
