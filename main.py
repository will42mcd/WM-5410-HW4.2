from Graph import *
from CalculateDistance import *

loc1 = get_lat_lon('Gilroy, CA')
loc2 = get_lat_lon('Cheyenne, WY')
loc3 = get_lat_lon('Fargo, ND')
loc4 = get_lat_lon('Zanesville, OH')
loc5 = get_lat_lon('Worcester, MA')
loc6 = get_lat_lon('Tupelo, MS')
loc7 = get_lat_lon('Lubbock, TX')

def path_to_target(start,goal,g):
    dijkstra(g, g.get_vertex(start), g.get_vertex(goal)) 

    target = g.get_vertex(goal)
    path = [target.get_id()]
    shortest(target, path)
    return (path[::-1], target.get_distance())

def reset_visited_and_distances(g):
    for v in g:
        v.set_distance(sys.maxsize)
        v.clear_visited()

def load_graph(g):
    #g = Graph()

    g.add_vertex('Gilroy, CA')
    g.add_vertex('Cheyenne, WY')
    g.add_vertex('Fargo, ND')
    g.add_vertex('Zanesville, OH')
    g.add_vertex('Worcester, MA')
    g.add_vertex('Tupelo, MS')
    g.add_vertex('Lubbock, TX')

    #8 edges
    g.add_edge('Lubbock, TX', 'Gilroy, CA', calculate_distance(loc7, loc1), True)  
    g.add_edge('Lubbock, TX', 'Fargo, ND', calculate_distance(loc7, loc3,), True)
    g.add_edge('Lubbock, TX', 'Zanesville, OH', calculate_distance(loc7, loc4), True)
    g.add_edge('Gilroy, CA', 'Cheyenne, WY', calculate_distance(loc1, loc2), True)
    g.add_edge('Cheyenne, WY', 'Fargo, ND', calculate_distance(loc2, loc3), True)
    g.add_edge('Cheyenne, WY', 'Lubbock, TX', calculate_distance(loc2, loc7), True)
    g.add_edge('Fargo, ND', 'Zanesville, OH', calculate_distance(loc3, loc4), True)
    g.add_edge('Tupelo, MS', 'Lubbock, TX', calculate_distance(loc6, loc7), True)
    g.add_edge('Tupelo, MS', 'Zanesville, OH', calculate_distance(loc6, loc4), True)
    g.add_edge('Zanesville, OH', 'Worcester, MA', calculate_distance(loc4, loc5), True)
    g.add_edge('Worcester, MA', 'Tupelo, MS', calculate_distance(loc5, loc6), True)
# end def load_graph(g):

def main():
    graph = Graph()
    load_graph(graph)
    tp1 , dist1 = path_to_target('Gilroy, CA', 'Lubbock, TX', graph )
    print()
    print(f'The shortest path : {tp1}')
    
    tp2  = path_to_target('Gilroy, CA', 'Zanesville, OH', graph )
    print(f'The shortest path : {tp2}')
    
    print()
    tp3 = path_to_target('Tupelo, MS', 'Fargo, ND', graph )
    print(f'The shortest path : {tp3}')
    
    print()
    tp4 = path_to_target('Worcester, MA', 'Gilroy, CA', graph )
    print(f'The shortest path : {tp4}')



if __name__ == '__main__':
    main()