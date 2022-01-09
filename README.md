# airflow-hello-world

## Project Goals

This repo is to learn to use Airflow. Write some DAGS. Learn how to test it. And then to set up GitHub Actions to automate this project.

## Running Locally

I use Docker to run Airflow Locally

First Step is to Pull the image

`docker pull puckel/docker-airflow`

Once that is done, run it locally

```
docker run -d -p 8080:8080 -v \path\to\dags\airflow\dags:/usr/local/airflow/dags puckel/docker-airflow webserver
```

Then go to http://localhost:8080/admin to view the dashboard

Ensure the DAG has the switch before trying to trigger manually
