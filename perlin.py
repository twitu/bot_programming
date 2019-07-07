import numpy as np

def perlin(x,y,seed=0):
    """Implement Perlin Noise"""
    # permutation table
    if seed != 0:
        np.random.seed(seed)
    p = np.arange(256,dtype=int)
    np.random.shuffle(p)
    p = np.stack([p,p]).flatten()
    # coordinates of the top-left
    xi = x.astype(int)
    yi = y.astype(int)
    # internal coordinates
    xf = x - xi
    yf = y - yi
    # fade factors
    u = fade(xf)
    v = fade(yf)
    # noise components
    n00 = gradient(p[p[xi]+yi],xf,yf)
    n01 = gradient(p[p[xi]+yi+1],xf,yf-1)
    n11 = gradient(p[p[xi+1]+yi+1],xf-1,yf-1)
    n10 = gradient(p[p[xi+1]+yi],xf-1,yf)
    # combine noises
    x1 = lerp(n00,n10,u)
    x2 = lerp(n01,n11,u)
    return lerp(x1,x2,v)

def lerp(a,b,x):
    """Linear Interpolation"""
    return a + x * (b-a)

def fade(t):
    """6t^5 - 15t^4 + 10t^3"""
    return 6 * t**5 - 15 * t**4 + 10 * t**3

def gradient(h,x,y):
    """Grad converts h to the right gradient vector and return the dot product with (x,y)"""
    vectors = np.array([[0,1],[0,-1],[1,0],[-1,0]])
    g = vectors[h%4]
    return g[:,:,0] * x + g[:,:,1] * y
