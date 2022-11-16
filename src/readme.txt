The smiley faces dataset contains 144 unique images of dimensions 9x9x1 belonging to 2 categories (happy and sad).
The file "smiley_X.npy" contains the images.
The file "smiley_Y.npy" contains the corresponding classes (0 for sad, 1 for happy).
They are serialized with numpy, to load use:
```
X = np.load('path/to/smiley_X.npy')
```
