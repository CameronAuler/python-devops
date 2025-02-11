# Scripts Directory (`scripts/`)

## Overview
The `scripts/` directory contains utility scripts for setting up, deploying, and managing the **Example Python Project**. These scripts help automate common tasks like environment setup, deployment, testing, and database management.

## Directory Structure
```
scripts/
├── deploy.sh        # Deployment script for production
├── setup_env.sh     # Initializes the environment variables
├── start_server.sh  # Starts the application server
├── run_tests.sh     # Runs all test cases
├── README.md        # Documentation for scripts directory
```

## Scripts Explained
### `deploy.sh`
- Automates the deployment process, including pulling the latest code, installing dependencies, and restarting services.
- Usage:
  ```bash
  ./scripts/deploy.sh
  ```

### `setup_env.sh`
- Sets up necessary environment variables for local development.
- Usage:
  ```bash
  source scripts/setup_env.sh
  ```

### `start_server.sh`
- Starts the application server (Flask, Django, or FastAPI, depending on the project).
- Usage:
  ```bash
  ./scripts/start_server.sh
  ```

### `run_tests.sh`
- Runs all unit tests using `pytest`.
- Usage:
  ```bash
  ./scripts/run_tests.sh
  ```

## Best Practices
- Ensure all scripts are executable (`chmod +x script_name.sh` on UNIX systems).
- Use descriptive names for any additional scripts.
- Document new scripts within this `README.md`.
