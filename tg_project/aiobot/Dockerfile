FROM python:3.9.1
# set work directory
WORKDIR C:\Users\Crond\my-projects\tg_project\aiobot
# copy project
COPY . C:\Users\Crond\my-projects\tg_project\aiobot
# install dependencies
RUN pip install --user aiogram
# run app
CMD ["python", "docbot.py"]