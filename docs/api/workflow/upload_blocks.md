&#8592; [Back to API docs](/EEG-Workflow-System/server-api)

# Block Zip Upload

This API is to upload custom blocks via Zip file to the application.

**URL** : `/api/workflow/upload`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : 

Authentication token in the cookie header.  
Form-data (```application-type: multipart/form-data```) format expected from the client to the server.
```json
{
    "file": (binary)
}
```
The file (binary), is the zip file containing the modules. For example, zip the [Arithmetic](https://github.com/ronak66/EEG-Workflow-System/tree/master/blocks) folder and send to the API to register the blocks.  
Check [How to create blocks](https://ronak66.github.io/EEG-Workflow-System/blocks.html) to better understand the modules and blocks.

## Success Response

**Code** : `200 SUCCESS`

**Content** :    
Return JSON format (```mimetype: application/json```) from server to client. Check the API response format for the Arithmetic block as an example.

```json
{
    "new_blocks_length": "[number of new blocks]"
}
```

## Error Responses

**Codes** :  
- `400 Bad Request` (If python error occurs)
- `403 Forbidden` (If module already exsists)

**Content** :  
```json
{
    "error": "[whatever the error is]"
}
```