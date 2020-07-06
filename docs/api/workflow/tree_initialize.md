&#8592; [Back to API docs](/EEG-Workflow-System/server-api)

# Tree Initilaization

Initialize the tree of blocks which are already uploaded.

**URL** : `/api/workflow/initialize`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : 

Authentication token in the cookie header.

## Success Response

**Code** : `200 SUCCESS`

**Content** :    
Return JSON format (```mimetype: application/json```) from server to client. Check the API response format for the Arithmetic block as an example.

```json
[
    {
        "module": "Arithmetic.zip:Arithmetic",
        "name": "Addition",
        "owner": "guest@guest.com",
        "public": false,
        "description": "",
        "family": "AddSub",
        "fields": [
            {
                "attrs": "input",
                "card": "1-1",
                "name": "num1",
                "type": "NUMBER"
            },
            {
                "attrs": "input",
                "card": "1-1",
                "name": "num2",
                "type": "NUMBER"
            },
            {
                "attrs": "output",
                "card": "1-1",
                "name": "output",
                "type": "NUMBER"
            }
        ]
    },
    {
        "module": "Arithmetic.zip:Arithmetic",
        "name": "Subtraction",
        "owner": "guest@guest.com",
        "public": false,
        "description": "",
        "family": "AddSub",
        "fields": [
            {
                "attrs": "input",
                "card": "1-1",
                "name": "num1",
                "type": "NUMBER"
            },
            {
                "attrs": "input",
                "card": "1-1",
                "name": "num2",
                "type": "NUMBER"
            },
            {
                "attrs": "output",
                "card": "1-1",
                "name": "output",
                "type": "NUMBER"
            }
        ]
    },
    {
        "module": "Arithmetic.zip:Arithmetic",
        "name": "Constant",
        "owner": "guest@guest.com",
        "public": false,
        "description": "",
        "family": "Constant",
        "fields": [
            {
                "attrs": "editable",
                "defaultValue": "10",
                "description": "",
                "name": "constant value",
                "type": "NUMBER"
            },
            {
                "attrs": "output",
                "card": "1-1",
                "name": "output",
                "type": "NUMBER"
            }
        ]
    }
]
```

## Error Responses

**Codes** :  
- `400 Bad Request` (If python error occurs)

**Content** :  
```json
{
    "error": "[whatever the error is]"
}
```