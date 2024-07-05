from flask import Flask, request, jsonify
from face_detection import detect_faces, crop_face
from feature_extraction import extract_features
from database import create_table, add_face, get_all_faces, delete_face
import torch
import torch.nn.functional as F
import numpy as np
from PIL import Image
import time

app = Flask(__name__)

def cosine_similarity(features1, features2):
    return F.cosine_similarity(features1, features2)

@app.route('/api/face', methods=['GET'])
def get_faces():
    faces = get_all_faces()
    faces_serializable = []

    for face in faces:
        face_dict = {
            'id': face[0],
            'name': face[1]
        }
        faces_serializable.append(face_dict)
    return jsonify(faces_serializable)


@app.route('/api/face/register', methods=['POST'])
def register_face():
    data = request.json
    name = data['name']
    image_path = data['image_path']
    img = Image.open(image_path)
    boxes = detect_faces(image_path)
    if boxes is None:
        return jsonify({'error': 'No faces found'})
    face_image = crop_face(img, boxes[0])
    features = extract_features(face_image)
    add_face(name, features)
    return jsonify({'status': 'Face has been registered'})

@app.route('/api/face/recognize', methods=['POST'])
def recognize_face():
    data = request.json
    image_path = data['image_path']
    img = Image.open(image_path)
    boxes = detect_faces(image_path)
    if boxes is None:
        return jsonify({'error': 'No faces found'})
    face_image = crop_face(img, boxes[0])
    features = extract_features(face_image)
    faces = get_all_faces()
    best_match = None
    best_similarity = 0
    for face in faces:
        stored_features = torch.tensor(np.frombuffer(face[2], dtype=np.float32))
        similarity = torch.cosine_similarity(torch.tensor(features), stored_features.unsqueeze(0)).item()
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = face
    if best_match:
        response = {
            'id': best_match[0],
            'name': best_match[1]
        }
        return jsonify({'match': response})
    else:
        return jsonify({'error': 'No match found'})

@app.route('/api/face/<int:id>', methods=['DELETE'])
def delete_face_by_id(id):
    delete_face(id)
    return jsonify({'status': 'Face has been deleted'})

if __name__ == '__main__':
    create_table()
    app.run(debug=True, host='0.0.0.0')
