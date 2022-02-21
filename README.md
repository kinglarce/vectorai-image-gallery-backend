# Vector AI Image Gallery Bank API - Backend

## Overview

This repository returns an API for fetching Bank's data for the frontend Image Gallery.

## Technology Used

- `Starlette` is a lightweight ASGI framework.
- `SQLite` is a lightweight SQL database engine.

## Getting started

To get the Node server running locally:

> It doesn't necessary need Python >= 3.6 but ensure you have Docker & Docker Componse installed, since the version of Python is handle inside the Dockerfile.

- Clone this repo
  - `git clone https://github.com/kinglarce/vectorai-image-gallery-backend.git`
- Start the server
  - `docker-compose up -d --build`
- Visit URL or Postman
  - `http://localhost:8000/`

## Frontend 

The source code for the frontend can be found in the [https://github.com/kinglarce/vectorai-image-gallery-frontend](https://github.com/kinglarce/vectorai-image-gallery-frontend).

### API Expose

- Fetching all bank/data for displaying on Image Gallery
  - [GET bank](#)
- Syncing changes on the Frontend to Backend
  - [POST bank](#)

## Functionality overview

- Web API endpoints.
- Fetching data from sqlite.
- Updated data in sqlite.
- CORS policy.

## Application Structure

- `docker-componse.yml` - This file is the entry point to our application and defines our application configuration.
- `backend/app/main.py` - This file is the entry point to our application and defines our application configuration, endpoint and database interactions.
- `backend/app/main.py` - This file contains the schema and database connection.
- `backend/Dockerfile` - This file contains the blueprint for building the image required to run the backend.
- `backend/init_db.py` - This file will seed data to sqlite.
- `backend/requirements.txt` - This file contains the requirements need to run our Python backend.

<br />