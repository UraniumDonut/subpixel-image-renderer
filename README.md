# subpixel-image-renderer
A image renderer that downsamples high-resolution images onto low-resolution screens while respecting their subpixel layout.
Code is currently only a proof of concept.

# Examples

This image was rendered for a R-G-B bar-type screen:

![image](https://github.com/user-attachments/assets/49333824-797d-458d-8d59-ba6e31ccc5a3)

This method creates a 3x higher horizontal resolution, while creating color artifacts. 

Magnified picture of the display:

| Regular Scaling  | Subpixel Optimized Rendering |
| ------------- | ------------- |
| ![image](https://github.com/user-attachments/assets/b1fb68e7-bb1a-49b6-a792-ea4c5f529794) | ![image](https://github.com/user-attachments/assets/33d99016-2e40-413d-a243-4501d40862de) |

The photos above are the bottom left corner of this image: 

![image](https://github.com/user-attachments/assets/617ebcd0-d01c-40df-a494-47a659c6ce12)

As visible in the images, horizontal resolution is greatly improved resulting in a smoother (less pixelated) edge. 
