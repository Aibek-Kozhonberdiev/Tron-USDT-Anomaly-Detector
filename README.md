# Tron Transaction History README

## Overview
This application allows users to obtain and analyze transaction history on the Tron network, with a special focus on the Tether (USDT) currency. Users can enter the Tron network address and the app will provide the validity of the transaction.

## Prerequisites
Before running the application, ensure you have the required dependencies installed. You can install them using the following command:

```bash
python -m venv venv
```

```bash
pip install -r requirements.txt
```

Make sure to set up a `.env` file with the necessary configuration variables, such as `FLASK_DEBUG`, `FLASK_KEY`, `FLASK_HOST`, and `MIXER`.

```.env
FLASK_DEBUG=
FLASK_KEY=
FLASK_HOST=
```

## Docker

Make sure to build the Docker image in the same directory as your Dockerfile:

```bash
docker build -t tron-transaction-app .
```

And then run the container:

```bash
docker run -p 8000:8000 tron-transaction-app
```

This will expose the application on port 8000 on your local machine. Adjust the port mappings according to your requirements.

## Usage

### Running the Application

To run the application, execute the following command:

```bash
python main.py
```

### Input
1. **Tron Network Address:** Users can input a Tron network address via the application's interface.

### Output
1. **Evaluation Score:** The application will provide an evaluation score for the specified wallet, indicating its trustworthiness or risk level.

## Implementation Details

The application utilizes the Tron API or a similar tool functioning as a Block Explorer to fetch and analyze transaction data. It specifically focuses on transactions involving Tether (USDT).

```python
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = eval(os.environ.get('FLASK_DEBUG', 'True'))
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('FLASK_KEY', 'my-secret-key')
    STATIC_FOLDER = 'static'
    TEMPLATE_FOLDER = 'templates'
    HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
    MIXER = os.environ.get('MIXER')
```
