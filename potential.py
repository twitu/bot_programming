import scipy.ndimage
import numpy as np
import matplotlib.pyplot as plt

def view_potential(potential):
    """View colorplot of potential field
    a) potential:   Potential field
    """
    plt.imshow(potential)
    plt.colorbar()
    plt.show()
    return

def obstacle(map_data, d0=2, nu=800, scale=100):
    """View colorplot of potential field
    a) map_data:    Boolean numpy array. True for passable, False for impassable.
    b) d0:          Parameter 1. Fall off.
    c) nu:          Parameter 2. Potential height.
    d) scale:       Parameter 3. Scale. Similar to fall off.
    """
    d = scipy.ndimage.distance_transform_edt(map_data)
    d2 = d/scale + 1
    potn = nu*np.square(np.divide(1, d2) - 1/d0)
    return potn
