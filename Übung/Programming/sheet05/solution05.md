# 05
## Frage 1
```python
import matplotlib.pyplot as plt
import numpy
import scipy.io

def initialize(K, population):
    P = population / numpy.sum(population)

    indices = numpy.random.choice(
        population.size,
        size=K,
        replace=False,
        p=P.ravel()
    )

    return locations[indices]

# Load data from data.mat

data = scipy.io.loadmat('data.mat')
population = data['population']
countries  = data['countries']

x,y = numpy.indices(population.shape)
locations = numpy.array([x.flatten(),y.flatten()]).T

# Assert shapes of population and countries are equal

assert(population.shape[0]==countries.shape[0])
assert(population.shape[1]==countries.shape[1])

# Choose random "geographical" locations

centroids_init = initialize(200, population)

# Plotting

plot(centroids_init[:,0], centroids_init[:,1], population, countries)
```

## Frage 2

All population values must be non-negative.


## Frage 3
```python
import matplotlib.pyplot as plt
import numpy
import pandas as pd
import scipy.io

# Implement initialization function
def initialize(K, population):
    population = numpy.asarray(population, dtype=float)
    probabilities = population.ravel() / population.sum()
    
    indices = numpy.random.choice(population.size, size=K, p=probabilities)
    centroids = numpy.column_stack(numpy.unravel_index(indices, population.shape))
    return centroids + numpy.random.normal(0, 0.01, size=centroids.shape)

# Run initialization 

centroids_init = initialize(200, population)

# Plotting

plot(centroids_init[:,0], centroids_init[:,1], population, countries)
```

## Frage 4

All geographical locations assigned to the cluster have zero weight.
The cluster contains no geographical locations.

## Frage 5 ???
```python
def wkmeans(centroids, points, weights, verbose=False, n_iter=50):
    centroids = numpy.array(centroids, dtype=float, copy=True)
    points = numpy.asarray(points, dtype=float)
    weights = numpy.asarray(weights, dtype=float).ravel()

    total_weight = weights.sum()
    if numpy.any(weights < 0) or total_weight <= 0:
        raise ValueError("Weights must be nonnegative with a positive sum.")

    def squared_distances():
        return numpy.sum(
            (points[:, None, :] - centroids[None, :, :]) ** 2,
            axis=2,
        )

    def objective():
        nearest_distances_sq = numpy.min(squared_distances(), axis=1)
        return float(
            numpy.sum(weights * nearest_distances_sq) / total_weight
        )

    for iteration in range(n_iter):
        labels = numpy.argmin(squared_distances(), axis=1)

        for k in range(len(centroids)):
            mask = labels == k
            cluster_weights = weights[mask]

            if cluster_weights.sum() > 0:
                centroids[k] = numpy.average(
                    points[mask],
                    axis=0,
                    weights=cluster_weights,
                )

        if verbose:
            print(f"Iteration {iteration + 1}: J = {objective():.6f}")

    return centroids, objective()
```

## Frage 6

If the objective function stops decreasing, Weighted K-Means has found the globally optimal centroid locations.