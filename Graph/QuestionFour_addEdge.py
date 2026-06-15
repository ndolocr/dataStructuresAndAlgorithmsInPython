class Graph:
    def __init__(self):
        self.graph_list = {}

    def print_graph(self):
        print("{")
        for node in self.graph_list:
            print(f"{node} : {self.graph_list[node]}")
        print("}")

        return True
    
    def add_vertex(self, vertex):
        if vertex not in self.graph_list.keys():
            self.graph_list[vertex] = []
            return vertex
        return None
    
    def add_edge(self, node_1, node_2):
        if node_1 in self.graph_list.keys() and node_2 in self.graph_list.keys():
            self.graph_list[node_1].append(node_2)
            self.graph_list[node_2].append(node_1)
            return True
        return False
    
def main():
    # Initiate Graph
    my_graph = Graph()

    # Create Vertex/ Node A
    node_a = my_graph.add_vertex("A")
    print("Graph List after adding Node A :- ")
    my_graph.print_graph()
    print()

    # Create Vertex/ Node B    
    node_b = my_graph.add_vertex("B")
    print("Graph List after adding Node B :- ")
    my_graph.print_graph()
    print()

    # Creating an aedge between A and B
    my_graph.add_edge(node_a, node_b)
    print("Graph after creating an edge between Node A and B")
    my_graph.print_graph()
    print()

if __name__ == "__main__":
    main()