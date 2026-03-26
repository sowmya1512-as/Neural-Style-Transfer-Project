import torch
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt
from torchvision.models import vgg19

def load_image(path, size=256):
    image = Image.open(path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((size, size)),
        transforms.ToTensor()
    ])
    image = transform(image).unsqueeze(0)
    return image

def imshow(tensor, title=None):
    image = tensor.clone().detach().squeeze(0)
    image = transforms.ToPILImage()(image)
    plt.imshow(image)
    if title:
        plt.title(title)
    plt.axis('off')


content = load_image("content.jpg")
style = load_image("style.jpg")

model = vgg19(pretrained=True).features.eval()

target = content.clone().requires_grad_(True)


optimizer = torch.optim.Adam([target], lr=0.01)

for i in range(100):
    optimizer.zero_grad()

    content_loss = torch.mean((target - content)**2)
    style_loss = torch.mean((target - style)**2)

    loss = content_loss + 0.5 * style_loss
    loss.backward()
    optimizer.step()

    if i % 20 == 0:
        print(f"Step {i}, Loss: {loss.item()}")


imshow(target, "Stylized Image")
plt.show()
