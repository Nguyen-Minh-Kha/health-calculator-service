# Health Calculator Service

This Flask application provides functionalities for calculating common health metrics. It includes endpoints for calculations and is structured for easy local setup, testing, and potential cloud deployment following DevOps best practices.

## Project Structure

The repository is organized as follows:

```plaintext
health-calculator-service/
├── app.py
├── utils.py
├── test.py
├── requirements.txt
├── Makefile
├── templates/
│   └── home.html
├── .env
├── .gitignore
```

### File Descriptions

- **`app.py`**: The main Flask application file. It defines the web routes (e.g., `/`, `/calculate`) and handles incoming requests, calling functions from `utils.py` to perform health calculations and rendering the results using the `home.html` template.

- **`utils.py`**: Contains the core logic for the health calculations (e.g., Body Mass Index (BMI), Basal Metabolic Rate (BMR)). Functions in this module take user inputs and return calculated health metrics.

- **`test.py`**: Includes unit tests for the calculation functions defined in `utils.py`. Running these tests ensures the accuracy and reliability of the core health calculation logic.

- **`requirements.txt`**: Lists the Python dependencies required to run the application (e.g., Flask). This file is used by `pip` to install the necessary packages.

- **`Makefile`**: Provides convenient commands to manage the project:
  - `make init`: Installs project dependencies listed in `requirements.txt`.
  - `make run`: Starts the Flask development server.
  - `make test`: Executes the unit tests using `pytest` or a similar test runner.

- **`templates/home.html`**: The HTML template for the web interface. It likely contains forms for users to input their data (like height, weight, age, gender) and displays the calculated health metrics.

- **`.env`**: A file for storing environment variables, such as configuration settings or secret keys. This file is ignored by Git (as specified in `.gitignore`) to prevent sensitive information from being committed to version control.

- **`.gitignore`**: Specifies intentionally untracked files that Git should ignore, such as `.env`, Python bytecode files (`__pycache__`), and virtual environment directories.

## Getting Started

1.  **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd health-calculator-service
    ```

2.  **Set Up the Environment**:
    *   It's recommended to create and activate a Python virtual environment:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   Install the dependencies:
        ```bash
        make init
        ```

3.  **Run the Application**:
    *   Start the Flask app locally:
        ```bash
        make run
        ```
    *   Access the application in your web browser (usually at `http://127.0.0.1:5000`).

4.  **Run Tests**:
    *   Execute unit tests to verify the calculation logic:
        ```bash
        make test
        ```

## Configuration

-   **Environment Variables**: If the application requires specific configurations (e.g., API keys for external services, although unlikely for a simple calculator), add them to a `.env` file in the project root. Example:
    ```plaintext
    # .env
    SECRET_KEY='your_secret_key_here'
    # Add other environment variables as needed
    ```

## Deployment

This application is configured for continuous deployment to Azure App Service using GitHub Actions.

### CI/CD Pipeline

-   The deployment workflow is defined in `.github/workflows/cicd.yaml`.
-   **Trigger**: The workflow automatically triggers upon pushing changes to the `main` branch.
-   **Process**:
    1.  Builds a Docker image of the application using the `Dockerfile` in the root directory.
    2.  Pushes the built Docker image to the GitHub Container Registry (ghcr.io).
    3.  Deploys the container image to the configured Azure App Service instance (`health-calculator-service`).

### Prerequisites for Deployment

-   An Azure App Service instance must be created and configured.
-   The `AZURE_WEBAPP_PUBLISH_PROFILE` secret must be added to the GitHub repository secrets. This contains the publish profile downloaded from the Azure portal.
-   The Azure App Service requires specific Application Settings for accessing the GitHub Container Registry:
    -   `DOCKER_REGISTRY_SERVER_URL`: `https://ghcr.io`
    -   `DOCKER_REGISTRY_SERVER_USERNAME`: Your GitHub username or organization name.
    -   `DOCKER_REGISTRY_SERVER_PASSWORD`: A GitHub Personal Access Token (PAT) with `repo` and `read:packages` permissions.

Once these prerequisites are met, any push to the `main` branch will automatically build and deploy the latest version of the application to Azure App Service. The deployment URL can be found in the GitHub Actions workflow run summary or the Azure portal.