# API Doccumentation

## Open Endpoints

Open endpoints require no Authentication.

* [Login](api/login.md) : `POST /api/users/login/`
* [Register](api/register.md) : `POST /api/users/register/`

## Endpoints that require Authentication

Closed endpoints require a valid Token to be included in the header of the
request. A Token can be acquired from the Login view above.

### Current User related

Each endpoint manipulates or displays information related to the User whose
Token is provided with the request:

* [Get User Details](api/user/user_details.md) : `GET /api/user/details`
* [Reset Password](api/user/reset.md) : `PUT /api/users/reset`

### Workflow related

Endpoints for performing Workflow related requests that the Authenticated User
has permissions to access.

* [Blocks Zip Upload](api/workflow/get.md) : `GET /api/workflow/upload`
* [Tree Initialization](api/workflow/tree_initialise.md) : `POST /api/workflow/initialises`
* [Schedule Job - GET](api/workflow/schedule_get.md) : `GET /api/workflow/schedule`
* [Schedule Job - POST](api/workflow/schedule_post.md) : `POST /api/workflow/schedule`
* [Job Details](api/workflow/pk/job_details.md) : `POST /api/workflow/jobs`


<!-- # List of APIs

- [User APIs](#User-APIs)  
    * [Register](#Register)
    * [Login](#Login)
    * [Reset](#reset)
- [Workflow APIs](#Workflow-APIs)
    * [Blocks Zip Upload](#blocks-zip-upload)
    * [Tree Initialization](#tree-initialization)
    * [Schedule Job - GET](#schedule-job-get)
    * [Schedule Job - POST](#schedule-job-post)
    * [Job Details](#job-details) -->



<!-- # User APIs

## 1. Register
<hr style="width:50%;text-align:left;margin-left:0">
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

## Login
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
## Reset
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
    ``` -->