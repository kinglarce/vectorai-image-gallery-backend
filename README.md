# vectorai-image-gallery-backend

# Running
virtualenv env
source env/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8080
docker run -d --name mycontainer -p 8000:8000 myimage
