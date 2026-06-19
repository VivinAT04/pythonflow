import os
import networkx as nx
import matplotlib.pyplot as plt


def generate_dag_graph(dag, output_path="static/dag_graph.png"):
    os.makedirs("static", exist_ok=True)

    graph = nx.DiGraph()

    for task in dag.tasks:
        graph.add_node(task.name)

        for downstream in task.downstream:
            graph.add_edge(task.name, downstream.name)

    plt.figure(figsize=(8, 5))

    pos = nx.spring_layout(graph)

    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_size=2500,
        font_size=10,
        arrows=True
    )

    plt.title(f"DAG: {dag.name}")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    return output_path
