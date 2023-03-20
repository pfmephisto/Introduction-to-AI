```{python}

import numpy as np
import matplotlib.pyplot as plt

# Define a function to generate a hill-shaped topography


def hill_topography(x, y):
    return np.exp(-(x**2 + y**2)/10) + 0.1


# Generate data for the plot
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = hill_topography(X, Y)

# Create a 3D plot of the topography
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', computed_zorder=False)
ax.plot_surface(X, Y, Z-0.1)
# ax.set_axis_off()
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Initialize starting point for gradient descent
x0, y0 = 0.2, -0.1
z0 = hill_topography(x0, y0)

# Set learning rate and maximum number of iterations
lr = 1.1
max_iter = 100

# Run gradient descent
for i in range(max_iter):

    gx = (hill_topography(x0 + 0.01, y0) - z0) / 0.01
    gy = (hill_topography(x0, y0 + 0.01) - z0) / 0.01

    # Update point based on gradient and learning rate
    x0 -= lr * gx
    y0 -= lr * gy
    z0 = hill_topography(x0, y0)

    # Plot current point on the surface
    ax.scatter(x0, y0, z0, color='r', marker='o')
    # ax.plot(x0, y0, z0, color='r', marker='o')
    # plt.pause(0.2)

plt.show()

```