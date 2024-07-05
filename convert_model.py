import torch
from facenet_pytorch import InceptionResnetV1

model = InceptionResnetV1(pretrained='vggface2').eval()
dummy_input = torch.randn(1, 3, 160, 160)

# Export the model
torch.onnx.export(model, dummy_input, "inception_resnet_v1.onnx", 
                  input_names=['input'], output_names=['output'])
