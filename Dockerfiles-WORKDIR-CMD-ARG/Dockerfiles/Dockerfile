# use python:3.12-alpine image as base image
FROM python:3.12-alpine

#OCI LABELS
LABEL org.opencontainers.image.title="Python 3.12 alpine image"
LABEL org.opencontainers.image.description="Python 3.12 alpine image"
LABEL org.opencontainers.image.authors="Sudhanshu Bhagat"


# define build time argument for environment
ARG ENVIRONMENT=dev

# set the environment variable using ARG value
ENV APP_ENVIRONMENT=${ENVIRONMENT}

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt ./requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY app.py .

# copy the templates directory
COPY templates/ ./templates/


# PRINT the ENVIRONMENT VARIABLE for demo purpose
RUN echo "Environment is set to: ${APP_ENVIRONMENT}"

#Expose the port
EXPOSE 80

# start the flask app
CMD ["python", "app.py"]
