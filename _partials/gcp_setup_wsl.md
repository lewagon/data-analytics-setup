Now let's set up Application Default Credentials so your Python code can access GCP:

```bash
gcloud auth application-default login --no-launch-browser
```

Copy the URL shown in the terminal, open it in your Windows browser, and log in with the same Google account you used to create your GCP project. Once you approve access, copy the verification code from the browser and paste it back into the terminal. Your credentials will be saved automatically.
