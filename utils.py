import matplotlib.pyplot as plt
import networkx as nx

from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).resolve().parent.absolute()


class PathUtils:
    """
    Utils for file names
    """

    # FOLDERS

    # Input netwroks
    input_networks_folder = get_project_root() / "tntp_networks"
    processed_networks_folder = get_project_root() / "processed_networks"

    # FILES

    # Network files
    anaheim_net_file = input_networks_folder / "Anaheim_net.tntp"
    barcelona_net_file = input_networks_folder / "Barcelona_net.tntp"
    braess_net_file = input_networks_folder / "Braess_net.tntp"
    chicago_net_file = input_networks_folder / "ChicagoSketch_net.tntp"
    eastern_massachusetts_net_file = input_networks_folder / "EMA_net.tntp"
    sioux_falls_net_file = input_networks_folder / "SiouxFalls_net.tntp"
    winnipeg_net_file = input_networks_folder / "Winnipeg_net.tntp"





def graph_od_pair(network):
    for od in network.tripSet:
        G = network.to_networkx()
        for i in network.linkSet:
            G.add_edge(network.linkSet[i].init_node, network.linkSet[i].term_node, weight=round(network.linkSetWithOD[i + od].flow,2))
        edge_labels = nx.get_edge_attributes(G, 'weight')
        # filter out the edges with 0 flow
        edge_labels = {k: v for k, v in edge_labels.items() if v > 0}
        nx.draw(G, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels=edge_labels)
        plt.show()