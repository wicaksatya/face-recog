import onnxruntime as ort
from torchvision import transforms

# Load the ONNX model
ort_session = ort.InferenceSession("inception_resnet_v1.onnx")

def preprocess(image):
    preprocess = transforms.Compose([
        transforms.Resize((160, 160)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
    ])
    return preprocess(image).unsqueeze(0)

def extract_features(face_image):
    face_tensor = preprocess(face_image)
    ort_inputs = {ort_session.get_inputs()[0].name: face_tensor.numpy()}
    ort_outs = ort_session.run(None, ort_inputs)
    features = ort_outs[0]
    return features
