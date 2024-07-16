from sklearn.neighbors import NearestNeighbors
import numpy as np

def read_file(file):
    with open(file,encoding='utf-8') as f:
        data = np.loadtxt(f,delimiter=',',skiprows=1,usecols=(5,6))
    array = np.array(data)
    return array

def analyze_interaction(red_array,green_array,blue_array):
    RL = len(red_array)
    GL = len(green_array)
    BL = len(blue_array)
    RR,RG,RB,GR,GG,GB,BR,BG,BB = 0,0,0,0,0,0,0,0,0
    colors_array = np.concatenate((red_array,green_array,blue_array))
    neighbors = NearestNeighbors(radius=,metric='euclidean',algorithm='auto').fit(colors_array)
    #radius should be changed based on your figures.
    dists, neighbs = neighbors.radius_neighbors(colors_array)
    
    n=0
    for i in neighbs:
        if n<RL:
            for j in i:
                if j < RL:
                    RR+=1
                elif j < RL+GL:
                    RG+=1
                elif j < RL+GL+BL:
                    RB+=1
            n+=1
        
        elif n<RL+GL:
            for j in i:
                if j < RL:
                    GR+=1
                elif j < RL+GL:
                    GG+=1
                elif j < RL+GL+BL:
                    GB+=1
            n+=1
        
        elif n<RL+GL+BL:
            for j in i:
                if j < RL:
                    BR+=1
                elif j < RL+GL:
                    BG+=1
                elif j < RL+GL+BL:
                    BB+=1
            n+=1
            
    print(RR/(RR+RG+RB),RG/(RG+RR+RB),RB/(RR+RG+RB))
    print(GR/(GR+GG+GB),GG/(GG+GR+GB),GB/(GR+GG+GB))
    print(BR/(BR+BG+BB),BG/(BR+BG+BB),BB/(BR+BG+BB))

if __name__ == '__main__' :
    red_file = 'red_file.csv'
    green_file = 'green_file.csv'
    blue_file = 'blue_file.csv'
    
    red_array = read_file(red_file)
    green_array = read_file(green_file)
    blue_array = read_file(blue_file)
    
    analyze_interaction(red_array, green_array, blue_array)
