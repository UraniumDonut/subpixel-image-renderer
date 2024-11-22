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


ISS071-E-463285 ISS Satellite picture (3 high-res renders, 1 low-res render):
| Regular Scaling  | Subpixel Optimized Rendering |
| ------------- | ------------- |
|![image](https://github.com/user-attachments/assets/89c9996a-c51f-4735-9875-a04a37f96e6b)|![image](https://github.com/user-attachments/assets/378c0586-12ff-45ff-9520-22cc93c5f62b)|
|![image](https://github.com/user-attachments/assets/ad788f3e-db91-4d9e-adcf-6f3290d4018b)|![image](https://github.com/user-attachments/assets/b6ae154d-dc7d-491a-bc42-9a70de36a450)|
|![image](https://github.com/user-attachments/assets/503dae36-0666-4b48-9fde-0b157734dbba)|![image](https://github.com/user-attachments/assets/9b9e7637-0936-43d6-a82f-ea7aac370483)|
|![image](https://github.com/user-attachments/assets/fd504a01-a9fa-4a18-86c4-25c1ee552e81)|![image](https://github.com/user-attachments/assets/e5111f35-b1bf-4da2-9fe7-35ea3d2ca5ae)|
