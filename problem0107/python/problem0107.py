import time
import urllib.request
import os

NETWORK_FILE = "./network.txt"


def download_if_not_present() -> None:
    """
    Downloads the network if it doesn't exist already.
    """
    if not os.path.exists(NETWORK_FILE):
        request = urllib.request.urlopen(
            "https://projecteuler.net/resources/documents/0107_network.txt"
        )
        with open(NETWORK_FILE, "wb") as file:
            file.write(request.read())


def parse_network() -> list[list[int]]:
    """
    Reads the network and returns it as a double array.
    """
    network = []
    with open(NETWORK_FILE) as file:
        for line in file.readlines():
            line = line.strip()
            elements = line.split(",")
            elements = [0 if elem == "-" else int(elem) for elem in elements]
            for elem in elements:
                print(f"{elem:4}", end="")
            network.append(elements)
            print("")
    return network


def network_weight(network: list[list[int]]) -> int:
    """
    Returns the total weight of the network.
    """
    return int(sum([sum(line) for line in network]) / 2)


def do_prim(network: list[list[int]]) -> int:
    """
    Based on pseudocode from https://en.wikipedia.org/wiki/Prim%27s_algorithm

    Parameters:
        network (list[list[int]]): The network weights

    Returns:
        int: The weight of the MST

    """
    infinity = 4096
    size = len(network)
    cheapest_cost = [infinity] * size
    cheapest_edge = [-1] * size
    explored = set()
    unexplored = set(range(size))

    start_vertex = 0
    cheapest_cost[start_vertex] = 0

    while len(unexplored) > 0:
        current_cheapest_cost = infinity
        current_vertex = None
        for vertex in unexplored:
            if cheapest_cost[vertex] < current_cheapest_cost:
                current_cheapest_cost = cheapest_cost[vertex]
                current_vertex = vertex

        unexplored.remove(current_vertex)
        explored.add(current_vertex)

        for node in range(size):
            if (
                node in unexplored
                and network[current_vertex][node] != 0
                and network[current_vertex][node] < cheapest_cost[node]
            ):
                cheapest_cost[node] = network[current_vertex][node]
                cheapest_edge[node] = current_vertex

    return sum(cheapest_cost)


def do_107():
    download_if_not_present()
    network = parse_network()
    total_network_weight = network_weight(network)
    print(f"Total network weight: {total_network_weight}")
    mst_network_weight = do_prim(network)
    print(f"MST network weight: {mst_network_weight}")
    print(f"Difference: {total_network_weight - mst_network_weight}")


if __name__ == "__main__":
    start = time.time_ns()
    do_107()
    end = time.time_ns()
    print(f"Duration {(end - start) / 1e9}s")
