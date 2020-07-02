# API Doccumentation

## List of APIs

- [User APIs](#User-APIs)  
    * [Register](#Register)
    * [Login](#Login)
    * [Reset](#reset)
- [Workflow APIs](#Workflow-APIs)
    * [Blocks Zip Upload](#blocks-zip-upload)
    * [Tree Initialization](#tree-initialization)
    * [Schedule Job - GET](#schedule-job-get)
    * [Schedule Job - POST](#schedule-job-post)
    * [Job Details](#job-details)



## User APIs

### Register
This is an API to register a new user
```
route: /api/users/register
method: POST
```
Form-data (```application-type: multipart/form-data```) format expected from the client to the server. Check below example:
```
{
    "email": "test@test.com,
    "username": "test",
    "password": "test123"
}
```
Return JSON format (```mimetype: application/json```) from server to client
* < if success >
    ```
    {
        "success": "New Board Created"
    }
    ```
* < if error encountered >
    ```
    {
        "error": "<whatever the error is>"
    }
    ```

### Login
This is an API to login an already exsisting user
```
route: /api/users/login
method: POST
```
Form-data (```application-type: multipart/form-data```) format expected from the client to the server. Check below example:
```
{
    "email": "test@test.com",
    "password": "test123"
}
```
Return JSON format (```mimetype: application/json```) from server to client
* < if success >
    ```
    {
        "reset": false,
        "id": 1, 
        "email": "test@test.com",
        "token": <hashed token>,
        "username": "test"
    }
    ```
* < if error encountered >
    ```
    {
        "error": "<whatever the error is>"
    }
    ```
### Reset
This is an API to login an already exsisting user
```
route: /api/users/reset
method: POST
```
Form-data (```application-type: multipart/form-data```) format expected from the client to the server. Check below example:
```
{
    "currentPassword": "test@test.com",
    "newPassword": "test123"
}
```
Return JSON format (```mimetype: application/json```) from server to client
* < if success >
    ```
    {
        "success": "Password Changed"
    }
    ```
* < if error encountered >
    ```
    {
        "error": "<whatever the error is>"
    }
    ```