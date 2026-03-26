# Neural-Style-Transfer-Project

Company name: CodeTech IT solutions 

Name: Sowmya G S

Domain : Artificial Intelligence 

Duration : 4 weeks

Intern ID : CTIS7569 

Mentor : Neela Santosh 

Descrpition of the task :

Neural Style Transfer (NST) is a deep learning technique used to combine the content of one image with the artistic style of another image to generate a new, visually appealing output. The primary objective of this task is to implement a basic Neural Style Transfer model using pre-trained convolutional neural networks, such as VGG19, to apply artistic styles to photographs.

In this project, two input images are required: a content image and a style image. The content image represents the original photograph whose structure, objects, and layout need to be preserved. The style image, on the other hand, provides the artistic features such as colors, textures, and brush strokes. The goal is to generate a new image that retains the content of the original image while adopting the artistic style of the second image.

The implementation is carried out using Python and deep learning libraries such as PyTorch and Torchvision. A pre-trained VGG19 model is used as the feature extractor. This model, trained on a large dataset, is capable of identifying different levels of features in an image, such as edges, shapes, and complex textures. These features are utilized to compute content loss and style loss, which guide the transformation process.

Content loss measures the difference between the feature representations of the generated image and the original content image. It ensures that the generated image maintains the structure and objects present in the content image. Style loss, on the other hand, measures the difference in style between the generated image and the style image. It is typically computed using Gram matrices, which capture the correlations between different feature maps to represent the texture and style of an image.

The process begins by initializing the generated image as a copy of the content image. Through an iterative optimization process, the pixels of this generated image are adjusted to minimize the combined content and style loss. An optimizer such as Adam is used to update the image in each iteration. As the optimization progresses, the generated image gradually transforms, blending the content with the style.

This task demonstrates the practical application of deep learning in the field of computer vision and digital image processing. It highlights how pre-trained models can be reused for creative tasks beyond classification. Neural Style Transfer has applications in art generation, photo editing, graphic design, and entertainment.

In conclusion, this project successfully implements a basic Neural Style Transfer system capable of applying artistic styles to images. It provides a clear understanding of how convolutional neural networks can be used not only for analytical tasks but also for creative and artistic purposes.


output of the task :

<img width="1806" height="914" alt="Image" src="https://github.com/user-attachments/assets/aa4abec6-c2ee-41f7-959c-a2789ba1330f" />
