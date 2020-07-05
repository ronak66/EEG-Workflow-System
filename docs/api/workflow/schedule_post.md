&#8592; [Back to API docs](/EEG-Workflow-System/server-api)

# Schedule Job

This API is to schedule a new job to execute the workflow.

**URL** : `/api/workflow/schedule`

**Method** : `POST`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : 

Authentication token in the cookie header.  
Form-data (```application-type: multipart/form-data```) format expected from the client to the server.

![Workflow Example](https://ronak66.github.io/EEG-Workflow-System/assets/workflow_example.png)  
To schedule the above workflow example, client sends form format:

```json
{
    "workflow": {
        "edges": [
            {
                "id": 1,
                "block1": 1,
                "connector1": [
                    "output",
                    "output"
                ],
                "block2": 3,
                "connector2": [
                    "num1",
                    "input"
                ]
            },
            {
                "id": 2,
                "block1": 2,
                "connector1": [
                    "output",
                    "output"
                ],
                "block2": 3,
                "connector2": [
                    "num2",
                    "input"
                ]
            }
        ],
        "blocks": [
            {
                "id": 1,
                "x": -457.5000061035156,
                "y": -176,
                "type": "Constant",
                "module": "Arithmetic.zip:Arithmetic",
                "values": {
                    "constant value": "40"
                }
            },
            {
                "id": 2,
                "x": -451.5000061035156,
                "y": -38,
                "type": "Constant",
                "module": "Arithmetic.zip:Arithmetic",
                "values": {
                    "constant value": "30"
                }
            },
            {
                "id": 3,
                "x": -97.5000061035156,
                "y": -117,
                "type": "Addition",
                "module": "Arithmetic.zip:Arithmetic",
                "values": {}
            }
        ]
    }
}
```

## Success Response

**Code** : `200 SUCCESS`

**Content** :    
Return JSON format (```mimetype: application/json```) from server to client. Check the API response format for the Arithmetic block as an example.

```json
{
    "job_id": "[job id]"
}
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