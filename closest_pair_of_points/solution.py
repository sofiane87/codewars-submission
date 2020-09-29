from sklearn.neighbors import NearestNeighbors
import numpy as np

def closest_pair(points):
    # Your code here!
    knn = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(points)
    distances, indices = knn.kneighbors(points)
    distances, indices = distances[:, -1] , indices[:, -1]
    arg_index = np.argmin(distances)
    return (points[arg_index], points[indices[arg_index]])
