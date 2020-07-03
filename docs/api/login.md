# User Login

Login user by authenticate the existing user.

**URL** : `/api/users/login`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** :  

Form-data (```application-type: multipart/form-data```) format expected from the client to the server.

```json
{
    "email": "[user email]",
    "password": "[user password]"
}
```

## Success Response

**Code** : `200 SUCCESS`

**Content** :    
Return JSON format (```mimetype: application/json```) from server to client

```json
{
    "reset": false,
    "id": "[User's id]", 
    "email": "[User's Email]",
    "token": "[Hashed Token]",
    "username": "[User's Username]"
}
```

## Error Responses

**Codes** :  
- `400 Bad Request` (If python error occurs)  
- `403 Forbidden` (If incorrect credentials)

**Content** :  
```json
{
    "error": "[whatever the error is]"
}
```