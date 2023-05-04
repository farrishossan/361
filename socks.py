#   ZeroMQ Microservice server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#
# Codes - contains Algorithm functions
# Codes2 - contains Data structure functions

import zmq
import codes
import codes2


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    print("Connected to Socket- tcp://*:5555, Microservice Running!")

    # Dictionary store of all data to be retrieved
    algorithms = {
        "BINARY SEARCH": codes.binary_search_code(),
        "LINEAR SEARCH": codes.linear_search_code(),
        "DEPTH FIRST SEARCH": codes.depth_first_search_code(),
        "BREADTH FIRST SEARCH": codes.breadth_first_search_code(),

        "INSERTION SORT": codes.insertion_sort_code(),
        "HEAP SORT": codes.heap_sort_code(),
        "SELECTION SORT": codes.selection_sort_code(),
        "MERGE SORT": codes.merge_sort_code(),
        "QUICK SORT": codes.quick_sort_code(),

        "HUFFMAN CODE": codes.huffman_code(),

        "STACK": codes2.stack_code(),
        "QUEUE": codes2.queue_code(),
        "DEQUE": codes2.deque_code(),
        "LINKED LIST": codes2.linked_list_code(),
        "HASH TABLE": codes2.hash_table_code(),

        "KRUSKAL'S ALGORITHM": codes2.kruskals_algorithm_code(),
        "DIJKSTRA'S ALGORITHM": codes2.dijkstras_algorithm_code(),

        "BINARY TREE": codes2.binary_tree_code(),
        "AVL TREE": codes2.avl_tree_code(),
    }

    data_structures = {
        "STACK": codes2.stack_code(),
        "QUEUE": codes2.queue_code(),
        "DEQUE": codes2.deque_code(),
        "LINKED LIST": codes2.linked_list_code(),
        "HASH TABLE": codes2.hash_table_code(),

        "KRUSKAL'S ALGORITHM": codes2.kruskals_algorithm_code(),
        "DIJKSTRA'S ALGORITHM": codes2.dijkstras_algorithm_code(),

        "BINARY TREE": codes2.binary_tree_code(),
        "AVL TREE": codes2.avl_tree_code(),
    }

    # Search Function
    while True:
        message = socket.recv_string()
        if message.startswith("SEARCH_"):
            search_term = message[7:].upper()
            if search_term in algorithms:
                socket.send_string(algorithms[search_term])
            else:
                socket.send_string("NOT_FOUND")
        elif message in algorithms:
            socket.send_string(algorithms[message])


if __name__ == "__main__":
    main()
