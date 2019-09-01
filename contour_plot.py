import numpy as np
import matplotlib.pyplot as plot

# List of points in x axis
XPoints     = []

# List of points in y axis
YPoints     = []

# X and Y points are from -6 to +6 varying in steps of 2 
for val in range(-6, 8, 2):
    XPoints.append(val)
    YPoints.append(val)

# Z values as a matrix
ZPoints     = np.ndarray((7,7))

# Populate Z Values (a 7x7 matrix) - For a circle x^2+y^2=z    
for x in range(0, len(XPoints)):
    for y in range(0, len(YPoints)):
        ZPoints[x][y] = (XPoints[x]* XPoints[x]) + (YPoints[y]*YPoints[y])

# Print x,y and z values
print(XPoints)
print(YPoints)
print(ZPoints)

# Provide a title for the contour plot
plot.title('Contour plot')

# Set x axis label for the contour plot
plot.xlabel('X')

# Set y axis label for the contour plot
plot.ylabel('Y')

# Create contour lines or level curves using matplotlib.pyplot module
contours = plot.contour(XPoints, YPoints, ZPoints)

# Display z values on contour lines
plot.clabel(contours, inline=1, fontsize=10)

# Display the contour plot
plot.show()