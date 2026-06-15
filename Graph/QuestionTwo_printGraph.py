class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for key in self.adj_list:
            print(f"{key}: {self.adj_list[key]}")

def main():
    # Initiate Graph
    my_graph = Graph()

    # Print Graph
    print()
    my_graph.print_graph()

if __name__ == "__main__":
    main()