# Green-removal

This done for the project where I have to detect pests from images of plant leaves.
The green removal algorithm is used to remove the greener pixels in the image. In this method a cluster center of [0 1 0]
is initialized at first and all the pixels are calculated with error values they have with this center and
those which has an error less than a threshold are removed from the images leaving only the part we are interested in.

The files in this repository are-


    k_means2.m and k_means2.py -  These are the matlab and python implementations of the above mentioned algorithm.
    
    
But this algorithm is later replaced with the one in the K-clustering repository with the name k_means_with_connected_components_2 in my project.
In this both the green removal and k-clustering algorithms are combined for removing the greener parts to get the pests.
