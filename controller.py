import const as const
import Point as Point
import random
# Escolher aleatoriamente k valores para centroides dos clusters

def define_samples():
    samples = []
    for i in range(0, const.number_samples):
        samples.append(Point.Point(const.start,const.end))
    return samples    

def define_centroids(samples):
    centroids = []
    probabilistic_space = []
    for sample in samples:
        probabilistic_space.append(sample)
    for i in range(0,const.k):
        random_index = round(random.uniform(0,len(probabilistic_space)-1))
        centroids.append(probabilistic_space[random_index])
        del probabilistic_space[random_index]
    
    return centroids
    
def match_samples(samples,centroids):
    clusters = []
    for centroid in centroids:
        clusters.append([])
    i=0
    for sample in samples:
            min = const.max_num
            index = -1
            for i in range(0,len(centroids)):
                if sample.distance(centroids[i])<min:
                    index = i
                    min = sample.distance(centroids[i])
            
            clusters[index].append(sample)
            sample.match(index)
    return clusters
         
            
def refresh_centroids(samples,centroids, clusters):
     centroid_has_change = False
     for i in range(0,len(clusters)):
        central_point = Point.Point(const.start,const.end)
        central_point.x = central_point.y = 0
        num=0
        for j in range(0,len(clusters[i])):
             central_point.x+=clusters[i][j].x
             central_point.y+=clusters[i][j].y
             num=num+1

        central_point.x/=num
        central_point.y/=num
        clusters[i] = [central_point]

             
         
                    
    
    
