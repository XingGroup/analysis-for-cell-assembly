from sklearn.neighbors import NearestNeighbors

def double_color(red_array,green_array,blue_array):
    RL = len(red_array)
    GL = len(green_array)
    BL = len(blue_array)
    RR = RG = RB = GR = GG = GB = BR = BG = BB = 0
    colors_array = red_array + green_array + blue_array
    neighbors = NearestNeighbors(radius=10.6,metric='euclidean',algorithm='auto').fit(colors_array)
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