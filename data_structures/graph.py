class Graph:
    def __init__(self, edges) -> None:
        self.edges = edges
        self.graph_dict = {}
        for origin, destination in edges:
            # print(origin, "->", destination)
            if origin not in self.graph_dict:
                self.graph_dict[origin] = [destination]
            else:
                self.graph_dict[origin].append(destination)
    
    def get_all_paths(self, origin, destination, path=[]):
        path += [origin]

        if origin == destination:
            return [path]

        if origin not in self.graph_dict:
            return []

        paths = []

        for dest in self.graph_dict[origin]:
            if dest not in path:
                new_paths = self.get_all_paths(dest, destination, path)
                for p in new_paths:
                    paths.append(p)
        return paths
    
    ...


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    graph = Graph(routes)
    print(graph.graph_dict)

    origin, destination = "Mumbai", "New York"
    print("Paths:", graph.get_all_paths(origin, destination))
