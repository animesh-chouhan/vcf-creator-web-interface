FROM python:3

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN chmod a+x view.sh

EXPOSE 8080

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]
ENTRYPOINT [ "gunicorn", "--workers", "2", "-b", "0.0.0.0:8080", "app:app" ]