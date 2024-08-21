FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#copy pre-trained data
#COPY saved_model_data /code/

#copy single file app
COPY main.py /code/

#
CMD ["fastapi", "run", "main.py", "--port", "80"]