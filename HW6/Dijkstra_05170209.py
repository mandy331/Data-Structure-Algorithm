from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    
    def Dijkstra(self, s):
        visited_array = [s]
        pointer = 0
        for i in range(len(self.graph[s])):
            if self.graph[s][i] > 0:
                self.graph_matrix[0][i] = self.graph[s][i]
            else:
                self.graph_matrix[0][i] = float('inf')
        self.graph_matrix[0][s] = 0
        pointer += 1
        
        while len(visited_array) < len(g.graph):
            self.graph_matrix[pointer] = self.graph_matrix[pointer - 1]
            v = self.find_min_vertice(visited_array, self.graph_matrix[pointer])
            visited_array.append(v)
            compare_distance = [self.graph[v][i] + self.graph_matrix[pointer][v] for i in range(len(self.graph[v]))]
            for i in range(len(self.graph[v])):
                if i in visited_array:
                    pass
                elif self.graph[v][i] == 0:
                    pass
                else:
                    if compare_distance[i] < self.graph_matrix[pointer][i]:
                        self.graph_matrix[pointer][i] = compare_distance[i]     
            pointer += 1
        return self.create_Dijkstra_dict(self.graph_matrix[len(self.graph)-1])
                   
    def find_min_vertice(self, visited_array ,graph_array):
        min_val = min([graph_array[i] for i in range(len(graph_array)) if graph_array[i] > 0 if i not in visited_array])
        for i in range(len(graph_array)):
            if graph_array[i] == min_val:
                return i
               
    def create_Dijkstra_dict(self, final_array):
        Di_dict = defaultdict(list)
        for i in range(len(final_array)):
            Di_dict[str(i)] = final_array[i]
        Di_dict = dict(Di_dict)
        return Di_dict
        