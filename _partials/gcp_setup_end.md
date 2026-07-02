Let's verify your Application Default Credentials are working:

```bash
gcloud auth application-default print-access-token
```

You should see a long token string. If you see an error, run `gcloud auth application-default login` again.

<details>
  <summary>Troubleshooting</summary>

- `AccessDeniedException: 403 The project to be billed is associated with an absent billing account.`
  - Make sure that billing is enabled for your Google Cloud Platform project [https://cloud.google.com/billing/docs/how-to/modify-project](https://cloud.google.com/billing/docs/how-to/modify-project)
</details>

🏁 You are done with the GCP setup!
