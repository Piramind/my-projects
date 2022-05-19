FROM python:3.9.1
# set work directory
WORKDIR /my-projects/tg_project/aiobot
# copy project
COPY . /aiobot
# install dependencies
RUN pip install --user aiogram
# run app
CMD ["python", "docbot.py"]