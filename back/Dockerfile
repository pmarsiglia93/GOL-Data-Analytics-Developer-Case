# Stage 1
FROM continuumio/miniconda3 AS miniconda3

# Set DEBIAN_FRONTEND to noninteractive
ARG DEBIAN_FRONTEND=noninteractive

# Install ssh
RUN apt-get update -y

RUN apt-get install -y openssh-server

COPY docker/sshd_config /etc/ssh/

RUN echo "root:Docker!" | chpasswd

EXPOSE 2222

# Install packages
RUN apt-get update -y

RUN apt-get install -y cron
RUN apt-get install -y dialog

RUN apt-get install -y curl
RUN apt-get install -y g++
RUN apt-get install -y gnupg2
RUN apt-get install -y unixodbc-dev

# Install ODBC driver for SQL Server
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
RUN curl https://packages.microsoft.com/config/debian/12/prod.list | tee /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update -y

RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18

# Copy environment file
COPY ./environment.yml /

# Create the environment and remove file
RUN conda env create -f environment.yml && rm environment.yml


# Stage 2
FROM miniconda3

# Expose port
EXPOSE 8000

# Copy the project
COPY . /gdadc/

# Set work directory
WORKDIR /gdadc/

# Set scheduled jobs
# RUN chmod 0644 ./cron/* && crontab ./cron/*

# Set enviroment variables
ENV DB_ENGINE="mssql+pyodbc"
ENV DB_HOST="db"
ENV DB_PORT="1433"
ENV DB_NAME="master"
ENV DB_USER="sa"
ENV DB_PASSWORD="DataAnalytics.737!"
ENV DB_DRIVER="ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"

# Set entry point permission
RUN chmod u+x ./entrypoint.sh

# Set entry point
ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
