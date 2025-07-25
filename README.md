
# Deploy Flask ML App with Health Check

This repo contains a tiny Flask ML app and a GitHub Actions workflow that deploys it to an EC2 instance and runs a `/health` check. Flip the health endpoint to return 500 to simulate a failed deploy and trigger the failure step (rollback simulation).

## Structure

```
ml-flask-app/
├── app/
│   ├── app.py
│   └── requirements.txt
└── .github/
    └── workflows/
        └── deploy.yml
```

## Run locally

```bash
pip install -r app/requirements.txt
python app/app.py
curl http://localhost:5000/health
```

## Simulate failure

In `app.py` change the `/health` route to:

```python
return jsonify({'status': 'unhealthy'}), 500
```
