# Vanness Plus Intern Test
### Nachat K
A repository for my Vanness Plus internship application, to implement a intern tracking webapp.

## Requirements
The minimum requirements are as follows.
  1. Dashboard page to show the internship applicants status who apply in different
  roles i.e., Web Application Trainee, UI/UX Designer Trainee, Sales/Marketing
  Trainee. The statuses are `New`, `WIP`, `Wait`, `Pass`, `Fail`, `Hire`.
  2. Internship List page to show all internship applicants with filter to search from
  name, application date, status.
  3. Add/Remove Internship applicants to add each internship applicant or remove.

## Running The Webapp
  1. Start the Docker engine.
  2. Run `docker compose up`
    - This sets up 2 containers: `mysql` for port 3306 and `my-fastapi-app` for port 8000
    - You can visit FastAPI's auto docs via `localhost:8000/docs`
