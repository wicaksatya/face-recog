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
    "name": "string",      
    "image_path": "string" 
}
```

**Response**:
```json
{
    "status": "Face has been registered"
}
```

**Example Request**:
```json
{
    "name": "Obama",     
    "image_path": "/path/to/obama.jpg"
}
```

**Example Response**:
```json
{
    "status": "Face has been registered"
}
```

### 2. Recognize Face

**Endpoint**: `/api/face/recognize`

**Method**: `POST`

**Description**: Recognizes a face from an image by comparing extracted features with registered faces.

**Request Body**:
```json
{     
    "image_path": "string" 
}
```

**Response**:
```json
{
    "match": {
        "id": "integer",   
        "name": "string"    
    },
    "error": "No match found"
}
```

**Example Request**:
```json
{
    "image_path": "/path/to/obama_recog.jpg"
}
```

**Example Response**:
```json
{
    "match": {
        "id": 1,   
        "name": "Obama"    
    }
}
```

### 3. Get All Registered Faces

**Endpoint**: `/api/face`

**Method**: `GET`

**Description**: Retrieves all registered faces.

**Response**:
```json
{
    "id": "integer",   
    "name": "string"
}
```

**Request**:
```http
GET http://localhost:5000/api/face
```

**Example Response**:
```json
[
    {
        "id": 1,   
        "name": "Obama"
    }
]
```

### 4. Delete Registered Faces by ID

**Endpoint**: `/api/face/<id>`

**Method**: `DELETE`

**Description**: Deletes a registered face by ID.

**Response**:
```json
{
    "status": "Face has been deleted"
}
```

**Example Request**:
```http
DELETE http://localhost:5000/api/face/1
```

**Example Response**:
```json
{
    "status": "Face has been deleted"
}
```

## Usage

### Running Docker Images
1. Clone the Repository:
   ```bash
   git clone https://github.com/wicaksatya/face-recog
   ```
2. Navigate to the Project Directory:
   ```bash
   cd face-recog
   ``` 
3. Run Docker Compose:
   ```bash
   docker-compose up
   ```
4. Access the API using Postman to interact with the endpoints.

### Example Use Case
1. **Register a Face**:
   Send a POST request to `/api/face/register` with the name and image path.
2. **Recognize a Face**:
   Send a POST request to `/api/face/recognize` with the image path to recognize and retrieve the name of the person.
3. **Get All Faces**:
   Send a GET request to `/api/face` to retrieve a list of all registered faces.
4. **Delete a Face**:
   Send a DELETE request to `/api/face/<id>` to remove a registered face by its ID.
