# Vanness Plus Intern Test - Documentation
### Author: Nachat K
This is documentation for the application used in Vanness Plus Intern test. This docs is intended to be as brief as possible, as it is not strictly required. I recommend you check out the repo `https://github.com/GrapesGoober/vanness-plus-intern-test` for more detailed issues, or if you wish to clone it. This file has 4 parts:
- **_Containers:_** Goes over the 3 containers and how they work
- **_API & Backend:_** Goes over the design of the REST API, for all the interns CRUD operations
- **_Frontend:_** Goes over the implementations & user guide for frontend.

## Containers
As defined in `compose.yaml`, this project has 3 containers, in the following order of creation:
- **_mysql:_** running at port 3306. This keeps all the database inside volume `sqldata`. For convenience, I put the database setup script (tables schemas) into `init.sql` which is host-binded to the container's volume initialization script. The server automatically runs this when initializing volume. 
- **_fastapi-app:_** Python app running at port 8000. I chose fastapi for the auto docs feature via `http://localhost:8000/docs`. I designed this to be RESTful.
- **_svelte-app:_** a node server at port 5173 for frontend Svelte, running using Vite

## API & Backend
I designed this to be RESTful, using just one API endpoint `/api/intern` with dedicate methods. These API endpoints will then connect to the database server then runs their commands.

**_PUT:_** to modify the intern data. Using following schema:
```
{
  "name": "John Doe", // string
  "applied_date": "2024-01-01", // yyyy-mm-dd
  "role": "Web Application Trainee", // string
  "status": "New", // "New""WIP""Wait""Pass""Fail""Hire"
  "id": 0 // integer
}
```
This will return `True` if success, regardless whether intern exists.

**_POST:_** to add a new intern data. Using following schema:
```
{
  "name": "John Doe", // string
  "applied_date": "2024-01-01", // yyyy-mm-dd
  "role": "Web Application Trainee", // string
  "status": "New", // "New""WIP""Wait""Pass""Fail""Hire"
}
```
This will return `True` if success.

**_DELETE:_** to remove an intern using integer `id`, via URL parameter.


**_GET:_** to get a list of intern via the following filter:
```
name_contains:  str = ""
applied_after:  date = date(2024, 1, 1)
applied_before: date = date(2024, 12, 1)
status:         Union[InternStatus, str] = ""
```
This responds with the following schema
```
[ // a list of interns
    {
    "name": "John Doe", // string
    "applied_date": "2024-01-01", // yyyy-mm-dd
    "role": "Web Application Trainee", // string
    "status": "New", // "New""WIP""Wait""Pass""Fail""Hire"
    "id": 0 // integer
    }
]
```

## Frontend
I write this assuming that you (reader) have already seen the frontend app already. The frontend is built with one page app. The code is written using Svelte, with Typescript, located in `frontend/src/routes` and `frontend/src/lib`
- The lib folder contains type definitions and API function definitions
- The routes folder contains svelte script for a single page.
    - It shows a list of interns, showing its info.
    - `+page.svelte` is the entry point. Here it defines the states: interns list and filter. It passes these values to other components
    - `intern_filter_input.svelte` and `intern_add_input.svelte` are the first two components. These two are the filter icon and add icon on top of web page. It mutates the `filter` state. Note that it doesn't mutate the `internsList` state, since that state is periodically updated (although it should mutate, for responsiveness)
    - `intern_list` and `intern_item` periodically calls the API to update the list, and display onto screen.