from facenet_pytorch import MTCNN
from PIL import Image

# Initialize MTCNN for face detection
mtcnn = MTCNN()

def detect_faces(image_path):
    img = Image.open(image_path)
    boxes, _ = mtcnn.detect(img)
    return boxes

def crop_face(img, box):
    return img.crop(box)
