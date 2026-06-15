class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def print_adj_list(self):
        print("{")
        for key in self.adj_list:
            print(f"{key}: {self.adj_list[key]}")
        print("}")
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return self.adj_list
        return None
    
def main():
    # Initiate Graph
    my_graph = Graph()

    # Add Vertex
    print()
    node = "A"
    print(f"Adding a new vertex with the value of {node}")
    my_graph.add_vertex(node)

    print()
    print(f"Printing Graph:- ")
    my_graph.print_adj_list()

if __name__ == "__main__":
    main()