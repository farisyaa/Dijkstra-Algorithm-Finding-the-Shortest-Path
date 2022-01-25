#==============================================#
#    DIJKSTRA ALGO - 1919614, 1919268, 2012657
#==============================================#
import sys

#Creating the G (bi-directional)
G  = {
    'Merdeka Square': {'Bank Negara':2, 'Chowkit':1.8},
    'Bank Negara': {'Merdeka Square':2, 'Chowkit':1.9, 'Pavilion':3.1},
    'Chowkit': {'Merdeka Square':2.6, 'Bank Negara':1.9, 'Royale Chulan':2.9, 'Pavilion':2.4},
    'Pavilion': {'Bank Negara':3.1, 'Chowkit':2.4, 'Royale Chulan':2, 'KLCC':2.8},
    'Royale Chulan': {'Chowkit':2.9, 'Pavilion':2, 'KLCC':2.7, 'Mandarin Oriental':2.4},
    'KLCC': {'Pavilion':2.8,'Royale Chulan':2.7, 'Mandarin Oriental':1.9},
    'Mandarin Oriental': {'Royale Chulan':2.7,'KLCC':1.9}
    }

def dijkstra(G, source, goal):
    shortest_dist =  {}     #find the cost to reach the node.
    track_pred = {}      #keep track of path 
    unseenNodes = G             #to iterate through the entire graph
    inf = sys.maxsize           #hold infinity number
    track_path = []             #tracking the optimal path

    for node in unseenNodes:
        shortest_dist[node] = inf       #creating infinity val
    shortest_dist[source] = 0

    while unseenNodes:                      #making sure we've seen all the nodes
        min_dist_node = None

        for node in unseenNodes:    
            if min_dist_node is None:
                min_dist_node = node    #be the starting node
            elif shortest_dist[node] < shortest_dist[min_dist_node]:
                min_dist_node = node    #update(swap) the value

        path_options = G[min_dist_node].items()     #find the other possible path can be taken

        for child_node, weight in path_options:
            if weight + shortest_dist[min_dist_node] < shortest_dist[child_node]:
                shortest_dist[child_node] = weight + shortest_dist[min_dist_node]   #establish a more effiecient path
                track_pred[child_node] = min_dist_node                              #update the new path

        unseenNodes.pop(min_dist_node)
    currentNodes = goal

    #Work back through destinations in shortest path
    while currentNodes != source:
        try:                                #insert curr nodes to help move backwards
            track_path.insert(0, currentNodes)
            currentNodes = track_pred[currentNodes]

        except KeyError:                    #if there's no path
            print("Path is not reachable")
            break

    track_path.insert(0, source)             

    if shortest_dist[goal] != inf:      #if infinity means not reached yet, if not infinity we've found the optimal path
        print("The Shortest Cost Calculated is " + str(shortest_dist[goal]))
        print("The Shortest Paths:  " + str(track_path))

dijkstra(G, 'Bank Negara', 'Royale Chulan')
