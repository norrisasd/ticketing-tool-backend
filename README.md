# Ticketing Tool Backend

The backend for the ticketing tool application

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Author](#author)

## Getting Started

Instructions on how to get a copy of the project up and running on your local machine.

> git clone

### Prerequisites

List any software or dependencies that need to be installed before running the project.

<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/docker-colored.svg" width="25" height="25" alt="JavaScript" /></a>
<a href="https://nodejs.org/en/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="25" height="25" alt="NodeJS" /></a>
<a href="https://www.postgresql.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/postgresql-colored.svg" width="25" height="25" alt="PostgreSQL" /></a>
</a><a href="https://fastapi.tiangolo.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/fastapi-colored.svg" width="25" height="25" alt="Fast API" /></a>

```
 - Docker
 - Docker-compose
 - Python
 - PostgreSQL
```

### Installation

Step-by-step guide on how to install and configure the project.

1. Create a .env file
2. Fill the following

   ```
   API_PORT=
   DB_PORT=
   DB_USER=
   DB_PASSWORD=
   DB_NAME=
   ```

3. Run the following commands
   > docker-compose up
4. Running Migrations (Needed only if first time running, Make sure containers are up)

   ```
   #Better to open another terminal
   docker exec -it backend-fastapi /bin/bash
   poetry shell
   alembic upgrade head
   exit
   ```

5. Restart Containers
   ```
   docker-compose down
   docker-compose up
   ```

## Usage

Instructions on how to use the project, including examples and screenshots if applicable.

> docker-compose up

## Author

👨‍💻 **Norris G. Hipolito Jr.**

- Github: [@norrisasd](https://github.com/norrisasd)
- LinkedIn: [@norrishipolito](https://www.linkedin.com/in/norris-hipolito-jr-a67574209/)

## Show your support

Give a ⭐️ if you like this project!
