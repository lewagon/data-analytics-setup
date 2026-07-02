# Setup Day — Student FAQ

Something not working? Try the fix below. If you've tried it and restarted your computer and it still doesn't work, raise your hand.

---

## macOS

### "I see `brew: command not found`" (or `pyenv: command not found`, or `direnv: command not found`)

If you have an M1 or M2 Mac (Apple Silicon), Homebrew installs to a different location that your terminal doesn't know about yet.

Fix — run these two commands:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv 2> /dev/null)"' >> ~/.zprofile
source ~/.zprofile && exec zsh
```

Then try the original command again.

---

### "I see a permissions error about directories not being writable"

```bash
sudo chown -R $(whoami) /usr/local/share/zsh /usr/local/share/zsh/site-functions
```

Then restart your terminal and try again.

---

### "pyenv install failed with BUILD FAILED"

Your Xcode developer tools need reinstalling:

```bash
sudo rm -rf /Library/Developer/CommandLineTools
xcode-select --install
```

Wait for the install to finish (it takes a few minutes), then retry the `pyenv install` command.

---

## Windows / WSL

### "WSL install gave me a 403 Forbidden error"

Your WiFi network is blocking the Microsoft download. Try either:

- Connect to a mobile hotspot and retry
- Run `wsl --install --online` instead
- Install Ubuntu from the Microsoft Store directly

---

### "Ubuntu/WSL is frozen or very slow"

Open **Command Prompt** (not Ubuntu) and run:

```
wsl --shutdown
```

Then close all Ubuntu windows and reopen them. This is the correct way to restart WSL. Restarting Windows also works but takes much longer.

---

### "The `code` command doesn't work in Ubuntu"

Restart your computer. This almost always fixes it.

---

### "I forgot my Ubuntu password"

Ask a teacher — they can reset it for you.

---

### "My CMD commands don't work / I see access errors"

Right-click on Command Prompt and choose **"Run as administrator"**.

---

## GCP

### "I accidentally created an Organization when making my GCP project"

Create a new GCP project:

1. Go to the [Cloud Console](https://console.cloud.google.com/)
2. Click the project dropdown at the top → **New Project**
3. Give it a name (e.g. `Wagon Bootcamp 2`)
4. **Leave the Organization field as "No organization"**
5. Click Create

Then continue from the step where you set your project in the terminal:

```bash
gcloud config set project YOUR_NEW_PROJECT_ID
```

---

### "My gcloud commands return a 403 error"

Run the authentication command again:

```bash
gcloud auth application-default login
```

Make sure you log in with the **same Google account** that owns your GCP project (your personal Gmail, not a work or school account).

Also check your Project ID is set correctly:

```bash
gcloud config list project
```

The Project ID looks like `wagon-bootcamp-123456` — it's different from the project name you chose.

---

### "I don't know my Project ID"

```bash
gcloud config list project
```

Or go to [console.cloud.google.com](https://console.cloud.google.com/) — the Project ID is shown below the project name in the dashboard (format: `your-project-name-123456`).

---

## SSH

### "I set a passphrase but now I've forgotten it"

You'll need to delete your SSH key and create a new one without a passphrase. Ask a teacher for help — they'll walk you through the three commands needed.

---

## General

### "I don't know if a step worked"

Run the command shown in the guide. If you see no error message (just a new prompt `$`), it worked. If you see a line starting with `error:` or `fatal:` or `zsh: command not found`, it didn't.

### "When should I ask for help?"

If you've tried the fix above, restarted your computer, and it still doesn't work — raise your hand. Don't spend more than 5 minutes on the same error.
