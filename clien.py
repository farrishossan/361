from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import pyfiglet
import zmq


def main():
    welcome = pyfiglet.figlet_format("Algo    CLI", font="basic", width=100)
    print(welcome)
    print("Welcome to Algo CLI - A Data Structures and Algorithms CLI reference.")
    print("Use the arrow keys to choose a menu option, Press Enter to select.")

    while True:
        select_item = select()
        if select_item == "Search":
            search()
        if select_item == "Algorithms":
            algorithms()
        if select_item == "Data Structures":
            data_structures()
        if select_item == None:
            break
    quit()

def select():
    select = inquirer.select(
        message = "Please select an option: \n",
        choices=[
            "Search",
            "Algorithms",
            "Data Structures",
            Choice(value=None, name="Exit")
        ],
        default = "Algorithms",
    ).execute()
    return select

def search():
    search_name = inquirer.text(message="Enter Algorithm or Data Structure name: ").execute()
    if search_name.strip() == "":
        print("Not found, Please try again")
    else:
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555")  # Replace with the address of your ZeroMQ service

        socket.send_string(f"SEARCH_{search_name}")
        code = socket.recv_string()

        if code == "NOT_FOUND":
            print("Not found, Please try again")
        else:
            print(code)

        select = inquirer.select(
            message="What do you want to do next?",
            choices=[
                "Search Again",
                "Go Back",
                "Quit",
            ],
            default="Search Again",
        ).execute()
        if select == "Search Again":
            search()
        if select == "Go Back":
            main()
        if select == "Quit":
            quit()

def algorithms():
    select = inquirer.select(
        message = "Please choose a Algorithm type: \n",
        choices = [
            "Searching",
            "Sorting",
            "Other",
            "\nGo Back",
            "Quit",
        ],
        default = "Searching",
    ).execute()

    if select == "Searching":
        searching()
    if select == "Sorting":
        sorting()
    if select == "Other":
        other()
    if select == "Go Back":
        main() 
    if select == "Quit":
        quit()


def searching():
    select = inquirer.select(
        message = "Please choose a search Algorithm: \n",
        choices = [
            "Binary Search",
            "Linear Search",
            "Depth First Search",
            "Breadth First Search",
            "\nGo Back",
            "Quit",
        ],
        default="Binary Search",
    ).execute()

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")  # Replace with the address of your ZeroMQ service

    if select == "Binary Search":
        socket.send_string("BINARY SEARCH")
        code = socket.recv_string()
        print(code)

    if select == "Linear Search":
        socket.send_string("LINEAR SEARCH")
        code = socket.recv_string()
        print(code)

    if select == "Depth First Search":
        socket.send_string("DEPTH FIRST SEARCH")
        code = socket.recv_string()
        print(code)

    if select == "Breadth First Search":
        socket.send_string("BREADTH FIRST SEARCH")
        code = socket.recv_string()
        print(code)

    if select == "Go Back":
        main()
    if select == "Quit":
        quit()


def sorting():
    select = inquirer.select(
        message = "Please choose a sorting Algorithm: \n",
        choices = [
            "Insertion Sort",
            "Heap Sort",
            "Selection Sort",
            "Merge Sort",
            "Quick Sort",
            "\nGo Back",
            "Quit",
        ],
        default="Insertion Sort",
    ).execute()

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")  # Replace with the address of your ZeroMQ service

    if select == "Insertion Sort":
        socket.send_string("INSERTION SORT")
        code = socket.recv_string()
        print(code)

    if select == "Heap Sort":
        socket.send_string("HEAP SORT")
        code = socket.recv_string()
        print(code)

    if select == "Selection Sort":
        socket.send_string("SELECTION SORT")
        code = socket.recv_string()
        print(code)

    if select == "Merge Sort":
        socket.send_string("MERGE SORT")
        code = socket.recv_string()
        print(code)

    if select == "Quick Sort":
        socket.send_string("QUICK SORT")
        code = socket.recv_string()
        print(code)

    if select == "Go Back":
        main()
    if select == "Quit":
        quit()


def other():
    select = inquirer.select(
        message="Please choose an Algorithm: \n",
        choices=[
            "Huffman Code",
            "\nGo Back",
            "Quit",
        ],
        default="Huffman Code",
    ).execute()

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")  # Replace with the address of your ZeroMQ service

    if select == "Huffman Code":
        socket.send_string("HUFFMAN CODE")
        code = socket.recv_string()
        print(code)

    if select == "Go Back":
        main()
    if select == "Quit":
        quit()


def data_structures():
    select = inquirer.select(
        message = "Please choose a Data Structure: \n",
        choices = [
            "Stack",
            "Queue",
            "Deque",
            "Linked List",
            "Trees",
            "Graphs",
            "\nGo Back",
            "Quit",
        ],
        default = "Stack",
    ).execute()

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")  # Replace with the address of your ZeroMQ service

    if select == "Stack":
        socket.send_string("STACK")
        code = socket.recv_string()
        print(code)
    if select == "Queue":
        socket.send_string("QUEUE")
        code = socket.recv_string()
        print(code)
    if select == "Deque":
        socket.send_string("DEQUE")
        code = socket.recv_string()
        print(code)
    if select == "Linked List":
        socket.send_string("LINKED LIST")
        code = socket.recv_string()
        print(code)
    if select == "Trees":
        trees()
    if select == "Graphs":
        graphs()
    if select == "Go Back":
        main()
    if select == "Quit":
        quit()


def trees():
    select = inquirer.select(
        message = "Please choose a Data Structure: \n",
        choices = [
            "Binary Tree",
            "AVL Tree",
            "\nGo Back",
            "Quit",
        ],
        default = "Binary Tree",
    ).execute()

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")  # Replace with the address of your ZeroMQ service

    if select == "Binary Tree":
        socket.send_string("BINARY TREE")
        code = socket.recv_string()
        print(code)
    if select == "AVL Tree":
        socket.send_string("AVL TREE")
        code = socket.recv_string()
        print(code)
    if select == "Go Back":
        main()
    if select == "Quit":
        quit()


def graphs():
    select = inquirer.select(
        message = "Please choose a Data Structure: \n",
        choices = [
            "Kruskal's Algorithm",
            "Dijkstra's Algorithm",
            "\nGo Back",
            "Quit",
        ],
        default = "Kruskal's Algorithm",
    ).execute()

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")  # Replace with the address of your ZeroMQ service

    if select == "Kruskal's Algorithm":
        socket.send_string("KRUSKAL'S ALGORITHM")
        code = socket.recv_string()
        print(code)
    if select == "Dijkstra's Algorithm":
        socket.send_string("DIJKSTRA'S ALGORITHM")
        code = socket.recv_string()
        print(code)
    if select == "Go Back":
        main()
    if select == "Quit":
        quit()


if __name__ == "__main__":
    main()