FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#crate dir to save as volume
RUN mkdir /code/save_model_data

#copy single file app
COPY main.py /code/

#
CMD ["fastapi", "run", "main.py", "--port", "80"]