# SparkingFlow

SparkingFlow is a local data engineering project that brings together Apache Airflow and Apache Spark. Airflow provides workflow orchestration, while Spark runs the data processing job defined in the project DAG.

## Project contents

- `dags/spark_airflow.py` — Airflow DAG that coordinates the Spark workflow.
- `Dockerfile` — container image build instructions.
- `airflow.env` — local Airflow configuration, including the web UI address.

## Prerequisites

- Docker Desktop with Docker Compose available
- Git (if cloning the project)

## Getting started

1. Clone this repository and open a terminal in the project directory.
2. Review `airflow.env` and adjust local settings as needed. Do not commit passwords, tokens, or other secrets.
3. Start the project's Docker Compose services:

   ```sh
   docker compose up --build -d
   ```

4. Open the Airflow web interface at [http://localhost:8081](http://localhost:8081), as configured in `airflow.env`.
5. In Airflow, enable the `spark_airflow` DAG if it is paused, then trigger a run or wait for its schedule.
6. Follow the task state and logs in the DAG's Grid or Graph view.

To stop the services, run:

```sh
docker compose down
```

To also remove named volumes and their stored data, run `docker compose down --volumes`.

## Workflow

The `spark_airflow.py` DAG is the entry point for the orchestrated Spark workflow. Its tasks, dependencies, schedule, Spark connection details, and input/output locations are defined in that file and the associated container configuration. Check the DAG and Compose configuration before changing paths or service names.

## Configuration and troubleshooting

- Confirm Docker Desktop is running and the Compose services are healthy if the Airflow UI does not load.
- Check container logs with `docker compose logs -f` and task-specific logs in the Airflow UI.
- If the DAG does not appear, confirm the DAG file is mounted or copied into Airflow's DAG folder and check the scheduler logs for import errors.
- Ensure the Spark service/connection settings used by the DAG match the services available in the Compose configuration.

## Development

Edit the DAG in `dags/spark_airflow.py` and rebuild/restart the relevant containers when image or dependency configuration changes. Keep credentials in an untracked local environment file or a secrets manager, not in source control.
