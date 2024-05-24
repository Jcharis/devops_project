FROM python:3.9-slim 

WORKDIR /app 

# copy requirments for app
COPY requirements.txt /app

# Update pip
RUN pip3 install --upgrade pip 

# Install Packages
RUN pip3 install -r requirements.txt --no-cache-dir 

# Copy all src for the app
COPY . /app

# Expose the PORT
EXPOSE 8000

# Run the app

CMD [ "python","manage.py", "runserver", "0.0.0.0:8000" ]
