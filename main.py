import random as rand
from clustering import clustering
from point import Point
import csv
import time

start = time.clock()

geo_locs = []
#loc_ = Point(0.0, 0.0)  #tuples for location
#geo_locs.append(loc_)
#read the fountains location from the csv input file and store each fountain location as a Point(latit,longit) object
f = open('data.csv', 'r')
reader = csv.reader(f, delimiter=",")

for line in reader:
    loc_ = Point(line[0], float(line[1]), float(line[2]))  #tuples for name and location
    geo_locs.append(loc_)

#print len(geo_locs)
#for p in geo_locs:
#    print "%f %f" % (p.latit, p.longit)
#let's run k_means clustering. the second parameter is the no of clusters

cluster = clustering(geo_locs, 4 )
flag = cluster.k_means()

end = time.clock()

if flag == -1:
    print "Error in arguments!"
else:	
    print "%.2gs" % (end-start)
    #the clustering results is a list of lists where each list represents one cluster
    print "Clustering results:"
    cluster.print_clusters(cluster.clusters)