&#8592; [Back to API docs](/EEG-Workflow-System/server-api)

# Reset User Password

Reset a new password for user account, i.e change password.

**URL** : `/api/users/reset`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Data constraints** :  

Authentication token in the cookie header.   
Form-data (```application-type: multipart/form-data```) format expected from the client to the server.

```json
{
    "currentPassword": "[old/current password]",
    "newPassword": "[new password]"
}
```

## Success Response

**Code** : `200 SUCCESS`

**Content** :    
Return JSON format (```mimetype: application/json```) from server to client

```json
{
    "success": "Password Changed"
}
```

## Error Responses

**Codes** :  
- `400 Bad Request` (If python error occurs)  
- `403 Forbidden` (If oldpassword does not match)

**Content** :  
```json
{
    "error": "[whatever the error is]"
}
```