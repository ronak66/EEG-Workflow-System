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

```json
{
    "jobId" : "[id of the job you want details of]"
}
```

## Success Response

**Code** : `200 SUCCESS`

**Content** :    
Return JSON format (```mimetype: application/json```) from server to client. Check the API response format for the Arithmetic block as an example.

![Workflow Example](https://ronak66.github.io/EEG-Workflow-System/assets/workflow_example_complete.png)  
For the above job (with job id 16), the API returns:

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
                "x": -420.0000061035156,
                "y": -209,
                "type": "Constant",
                "module": "Arithmetic.zip:Arithmetic",
                "values": {
                    "constant value": "40"
                },
                "output": {
                    "type": "STRING",
                    "value": "{'output': '40'}"
                },
                "completed": true,
                "error": false,
                "stderr": ""
            },
            {
                "id": 2,
                "x": -362.0000061035156,
                "y": -90.00000381469727,
                "type": "Constant",
                "module": "Arithmetic.zip:Arithmetic",
                "values": {
                    "constant value": "30"
                },
                "output": {
                    "type": "STRING",
                    "value": "{'output': '30'}"
                },
                "completed": true,
                "error": false,
                "stderr": ""
            },
            {
                "id": 3,
                "x": -86.0000061035156,
                "y": -179.00000381469727,
                "type": "Addition",
                "module": "Arithmetic.zip:Arithmetic",
                "values": {},
                "output": {
                    "type": "STRING",
                    "value": "{'output': 70}"
                },
                "completed": true,
                "error": false,
                "stderr": ""
            }
        ]
    },
    "executionStatus": [
        {
            "id": 1,
            "x": -420.0000061035156,
            "y": -209,
            "type": "Constant",
            "module": "Arithmetic.zip:Arithmetic",
            "values": {
                "constant value": "40"
            },
            "output": {
                "type": "STRING",
                "value": "{'output': '40'}"
            },
            "completed": true,
            "error": false,
            "stderr": ""
        },
        {
            "id": 2,
            "x": -362.0000061035156,
            "y": -90.00000381469727,
            "type": "Constant",
            "module": "Arithmetic.zip:Arithmetic",
            "values": {
                "constant value": "30"
            },
            "output": {
                "type": "STRING",
                "value": "{'output': '30'}"
            },
            "completed": true,
            "error": false,
            "stderr": ""
        },
        {
            "id": 3,
            "x": -86.0000061035156,
            "y": -179.00000381469727,
            "type": "Addition",
            "module": "Arithmetic.zip:Arithmetic",
            "values": {},
            "output": {
                "type": "STRING",
                "value": "{'output': 70}"
            },
            "completed": true,
            "error": false,
            "stderr": ""
        }
    ],
    "startTime": "Sun Jul  5 10:27:36 2020",
    "id": 16,
    "endTime": "Sun Jul  5 10:27:58 2020",
    "status": "COMPLETED"
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