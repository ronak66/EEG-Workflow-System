&#8592; [Back to API docs](/EEG-Workflow-System/server-api)

# User Login

Register a new user.

**URL** : `/api/users/register`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data constraints** :  

Form-data (```application-type: multipart/form-data```) format expected from the client to the server.

```json
{
    "email": "[user email]",
    "username": "[user username]",
    "password": "[user password]"
}
```

## Success Response

**Code** : `201 CREATED`

**Content** :    
Return JSON format (```mimetype: application/json```) from server to client

```json
{
    "success": "New User Created"
}
```

## Error Responses

**Codes** :  
- `400 Bad Request` (If python error occurs)  
- `403 Forbidden` (If user email already esists)

**Content** :  
```json
{
    "error": "[whatever the error is]"
}
```