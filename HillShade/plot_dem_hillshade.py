"""
Create A Hillshade From a Digital Elevation Model Using EarthPy
===============================================================

Learn how to create a hillshade from a DEM using the EarthPy
es.hillshade() function.
"""

###############################################################################
# Create A Hillshade Layer Using EarthPy
# pip install earthpy
###############################################################################
# Create a Hillshade from a Digital Elevation Model (DEM)
# -------------------------------------------------------
# A hillshade is a 3D representation of a surface. Hillshades are generally
# rendered in greyscale. The darker and lighter colors represent the shadows
# and highlights that you would visually expect to see in a terrain model.
# Hillshades are often used as an underlay in a map, to make the data appear
# more 3-Dimensional and thus visually interesting. This vignette will show
# you how to create a hillshade from a DEM using EarthPy. It will highlight
# how to adjust the sun's azimuth, altitude and other settings that will impact
# how the hillshade shadows are modeled in the data.
#
# The hillshade function is a part of the spatial module in EarthPy.

###############################################################################
# Import Packages

import os
import numpy as np
import matplotlib.pyplot as plt
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import rasterio as rio

####################################################################################
# Open up the DEM

dtm = "Harz_DGM5_32_ProjectRaster_C1.tif"

# Open the DEM with Rasterio
with rio.open(dtm) as src:
    elevation = src.read(1)
    # Set masked values to np.nan
    elevation[elevation < 0] = np.nan

# Plot the data
ep.plot_bands(
    elevation,
    cmap="gist_earth",
    title="DTM Without Hillshade",
    figsize=(10, 6),
)
plt.show()

####################################################################################
# Create the Hillshade
# Create and plot the hillshade with earthpy
hillshade = es.hillshade(elevation)

ep.plot_bands(
    hillshade,
    cbar=False,
    title="Hillshade made from DTM",
    figsize=(10, 6),
)
plt.show()

####################################################################################
# Change the Azimuth of the Sun
# -------------------------------
# The angle that sun light hits the landscape, impacts the shadows and highlights
# created on the landscape. You can adjust the azimuth values to adjust angle of the
# highlights and shadows that are created in your output hillshade. Azimuth numbers can
# range from 0 to 360 degrees, where 0 is due North. The default value for azimuth
# in ``es.hillshade()`` is 30 degrees.


Azimuth = 270
# Change the azimuth of the hillshade layer
hillshade_azimuth_210 = es.hillshade(elevation, azimuth= Azimuth)

# Plot the hillshade layer with the modified azimuth
ep.plot_bands(
    hillshade_azimuth_210,
    cbar=False,
    title="Hillshade with Azimuth set to 270 Degrees",
    figsize=(10, 6),
)
plt.show()

####################################################################################
# Change the Angle Altitude of the Sun
# -------------------------------------
# Another variable you can adjust for hillshade is what angle of the sun.
# The ``angle_altitude`` parameter values range from 0 to 90. 90 represents the sun
# shining from directly above the scene. The default value for ``angle_altitude`` in
# ``es.hillshade()`` is 30 degrees.


Altitude = 20
# Adjust the azimuth value
hillshade_angle_10 = es.hillshade(elevation, altitude= Altitude)

# Plot the hillshade layer with the modified angle altitude
ep.plot_bands(
    hillshade_angle_10,
    cbar=False,
    title="Hillshade with Angle Altitude set to 20 Degrees",
    figsize=(10, 6),
)
plt.show()

####################################################################################
# Overlay a DEM on top of the Hillshade
# -------------------------------------
# A hillshade can be used to visually enhance a DEM.
# To overlay the data, use the ``ep.plot_bands()`` function in EarthPy combined with
# ``ax.imshow()``. The alpha setting sets the tranparency value for the hillshade layer.

# Plot the DEM and hillshade at the same time
# sphinx_gallery_thumbnail_number = 5
fig, ax = plt.subplots(figsize=(200, 120) , labelsize=20.)
ep.plot_bands(
    elevation,
    ax=ax,
    cmap="terrain",
    title=" hillshade",
)
ax.imshow(hillshade, cmap="Greys", alpha=0.5)
plt.show()
