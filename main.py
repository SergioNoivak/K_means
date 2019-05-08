import matplotlib.pyplot as plt
import Point
import controller as controller
import const as const
import random


samples = controller.define_samples()
for i in range(0, const.number_samples):
   print("X:",samples[i].x,"Y",samples[i].y)   

centroids = controller.define_centroids(samples)
for centroid in centroids:
    centroid.show()

for i in range(0,100):
   clusters = controller.match_samples(samples,centroids)
   controller.refresh_centroids(samples,centroids, clusters)


# x=0
# for cluster in clusters:
#     print("cluster ",x)
#     for i in range(0,len(cluster)):
#            print(" element: ")
#            cluster[i].show()

#     x=x+1


colors = []
for i in range(0,const.k):
       colors.append( (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)))



for sample in samples:
       print(sample.get_match())
       plt.plot(sample.x, sample.y, marker='o', markersize=6, color=colors[sample.get_match()])


plt.show()