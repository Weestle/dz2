import requests
from graphviz import Digraph

packageName = input("Введите название pip пакета ").capitalize()

dot = Digraph()


def get_info(packageName, j):
    global dot
    if j >= 2:
        return
    try:
        res = requests.get(f"https://pypi.org/pypi/{packageName}/json").json()
        dependencies = res["info"]["requires_dist"]
        for i in range(len(dependencies)):
            dependencies[i] = dependencies[i].split()[0]
        dependencies = set(dependencies)
        for i in dependencies:
            dot.node(i)
            dot.edge(packageName, i)
            get_info(i, j + 1)
    except:
        print("", end="")


get_info(packageName, 0)
print(dot.source)
