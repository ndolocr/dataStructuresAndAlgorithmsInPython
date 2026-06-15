class Graph:
    def __init__(self):
        self.graph_list = {}

    def print_graph(self):
        for val in self.graph_list:
            print(f"{val}: {self.graph_list[val]}")
    
    def create_node(self, value):
        if value not in self.graph_list.keys():
            self.graph_list[value] = []
            return value
        return None
    

    def add_edge(self, node_1, node_2):
        if node_1 in self.graph_list.keys() and node_2 in self.graph_list.keys():
            self.graph_list[node_1].append(node_2)
            self.graph_list[node_2].append(node_1)
            return True
        return False
    
    def remove_edge(self, node_1, node_2):
        if node_2 in self.graph_list[node_1] and node_1 in self.graph_list[node_2]:
            for val in self.graph_list[node_1]:
                if val == node_2:
                    self.graph_list[node_1].remove(node_2)
            for val_2 in self.graph_list[node_2]:
                if val_2 == node_1:
                    self.graph_list[node_2].remove(node_1)

            return True
        return False
    
def main():
    # Initiate Graph
    my_graph = Graph()

    # Create Vertex/ Node A
    node_a = my_graph.create_node("A")
    print("Graph List after adding Node A :- ")
    my_graph.print_graph()
    print()

    # Create Vertex/ Node B    
    node_b = my_graph.create_node("B")
    print("Graph List after adding Node B :- ")
    my_graph.print_graph()
    print()

    # Creating an aedge between A and B
    my_graph.add_edge(node_a, node_b)
    print("Graph after creating an edge between Node A and B")
    my_graph.print_graph()
    print()

    # Remove edge for node A and node B
    my_graph.remove_edge(node_a, node_b)
    print("Graph after removing edge between Node A and B")
    my_graph.print_graph()
    print()

if __name__ == "__main__":
    main()