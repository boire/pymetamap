# Use an official Python runtime as a parent image
FROM python:3.6

# Set the file requirement
COPY . ./

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y python-pip python-dev \
&& pip install --trusted-host pypi.python.org -r requirements.txt


RUN python setup.py install

WORKDIR /pymetamap/

# Make port 80 available to the world outside this container
EXPOSE 6001

# Run app.py when the container launches
CMD ["python", "rest-api.py"]
