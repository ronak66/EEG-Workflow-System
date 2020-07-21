&#8592; [Back to API docs](/EEG-Workflow-System/server-api)

# User Details

Get user detials

**URL** : `/api/users/details`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** :  Authentication token in the cookie header.   


## Success Response

**Code** : `200 SUCCESS`

**Content** :    
Return JSON format (```mimetype: application/json```) from server to client

```json
{
    "id": "[user id]", 
    "email": "[user email]",
    "username": "[user Username]"
}
```

## Error Responses

**Codes** :  
- `400 Bad Request` (If python error occurs)  
- `403 Forbidden` (If no token)

**Content** :  
```json
{
    "error": "[whatever the error is]"
}
```