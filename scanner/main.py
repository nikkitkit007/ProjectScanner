from scanner.file_sys_workers.file_worker import File
from scanner.file_sys_workers.dir_worker import Directory

from displayer.graph import draw_graph


def data_to_graph(data: list, weight: bool = True) -> list[tuple]:
    nodes = []
    for node in data:
        if weight:
            nd = tuple(node)
            nd += File.get_dist(node[0], node[1]),
            nodes.append(nd)

    return nodes


# a = "p1/p2/p3/p4"
# b = "p1/p2/b1/b2/b3"

def main():
    project_path = input("Input project path: ")

    directory = Directory(project_path)

    files_py = directory.get_files_spec_ext(file_extensions=[".py"])
    rel_files_py = directory.print_files_relatively(files_py, project_path)
    print(files_py)
    print(rel_files_py)

    nodes = []
    for file in files_py:
        f = File(file)
        links_in_file = f.find_links(rel_files_py)

        for link in links_in_file:
            f = file.replace(project_path + "/", "")
            f = f[:f.rfind(".")]
            nodes.append([f, link])

    print("nodes", nodes)

    graph_nodes = data_to_graph(nodes)

    draw_graph(graph_nodes)
