
def check_coordinate(coordinate_list):
    for i in range(0,len(coordinate_list)):
        if coordinate_list[i]<0:
            coordinate_list[i]='WEST'

def coordinate_combiner(latitudes, longitudes):
    check_coordinate(latitudes)
    check_coordinate(longitudes)
    merged=list(tuple(zip(latitudes, longitudes)))
    return(merged)

    

