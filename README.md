# Face Recognition System Documentation

## Overview

This face recognition system provides RESTful API endpoints to register and recognize faces using ONNX models for detection and feature extraction. The system includes the following endpoints:

1. **Register Face**: `/api/face/register`
2. **Recognize Face**: `/api/face/recognize`
3. **Get All Registered Faces**: `/api/face`
4. **Delete Registered Face**: `/api/face/<id>`

## API Endpoints

### 1. Register Face

**Endpoint**: `/api/face/register`

**Method**: `POST`

**Description**: Registers a new face by extracting features and storing them in the database.

**Request Body**:
```json
{
    "name": "string",       // Name of the person
    "image_path": "string"  // Path to the image file
}```

**Response**:
```json
{
    "status": "Face has been registered"
}```

**Request Body**:
```json
{
    "name": "string",       // Name of the person
    "image_path": "string"  // Path to the image file
}```
