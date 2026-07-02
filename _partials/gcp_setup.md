### Configure Cloud sdk

- Authenticate the `gcloud` CLI with the google account you used for GCP

{% if os == "macos" %}
```bash
gcloud auth login
```
{% elsif os == "linux" %}
```bash
gcloud auth login
```
{% elsif os == "windows" %}
```bash
gcloud auth login --no-launch-browser
```
{% endif %}

- Login to your Google account on the new tab opened in your web browser
- List your active account and check your email address you used for GCP is present

```bash
gcloud auth list
```

- Set your current project (replace `PROJECT_ID` with the `ID` of your project, e.g. `wagon-bootcamp-123456`)

```bash
gcloud config set project PROJECT_ID
```

- List your active account and current project and check your project is present

```bash
gcloud config list
```
