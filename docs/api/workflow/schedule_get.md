&#8592; [Back to API docs](/EEG-Workflow-System/server-api)

# Schedule Job

This API returns a list of previously scheduled jobs by the user.

**URL** : `/api/workflow/schedule`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : Authentication token in the cookie header.  

## Success Response

**Code** : `200 SUCCESS`

**Content** :    
Return JSON format (```mimetype: application/json```) from server to client. Check the API response format for the Arithmetic block as an example.

```json
[
    {
        "startTime": "Sat Jun 20 05:49:18 2020",
        "id": 1,
        "endTime": "Sat Jun 20 05:49:19 2020",
        "status": "COMPLETED"
    },
    {
        "startTime": "Sun Jun 21 07:37:43 2020",
        "id": 2,
        "endTime": "Sun Jun 21 07:38:59 2020",
        "status": "COMPLETED"
    },
    {
        "startTime": "Sun Jun 21 07:45:58 2020",
        "id": 3,
        "endTime": "Sun Jun 21 07:46:19 2020",
        "status": "COMPLETED"
    },
    {
        "startTime": "Mon Jun 22 03:55:29 2020",
        "id": 4,
        "endTime": "",
        "status": "FAILED"
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