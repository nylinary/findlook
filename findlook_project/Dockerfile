# Basic image
FROM python 

# Root dir for project image
WORKDIR /

# Copy files from project folder to some place in image
COPY . .

# Runs a specified command only when compiling image
RUN pip install -r pip_requirements.txt

# Which port serves our application
EXPOSE 8000

# Runs when we start image
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]