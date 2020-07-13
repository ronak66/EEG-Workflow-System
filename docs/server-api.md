# API Documentation

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

* [Get User Details](api/users/user_details.md) : `GET /api/user/details`
* [Reset Password](api/users/reset.md) : `PUT /api/users/reset`

### Workflow related

Endpoints for performing Workflow related requests that the Authenticated User
has permissions to access.

* [Blocks Zip Upload](api/workflow/upload_blocks.md) : `GET /api/workflow/upload`
* [Tree Initialization](api/workflow/tree_initialize.md) : `POST /api/workflow/initialize`
* [Schedule Job - GET](api/workflow/schedule_get.md) : `GET /api/workflow/schedule`
* [Schedule Job - POST](api/workflow/schedule_post.md) : `POST /api/workflow/schedule`
* [Job Details](api/workflow/job_details.md) : `POST /api/workflow/jobs`