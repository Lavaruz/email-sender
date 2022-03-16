# Email Sender

Email Sender is a simple GUI Python code that can be used for sending an email

## Requirement If you want to try it

- Or you can make App Password for more secure methode, [Google Set App Password](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbVZxY3hQN3E4ajNwVDE0dThHa1ZDWEhGNTNIZ3xBQ3Jtc0tsLV9CLW1IU1FWQXVwVkVvZlFEWTczUmFoX2F6c3FTQ1kxYVIxTWItQUs1MmlnWlFVZG8xUzQ2bXpHWUluNFA3WXh0Wlo3SlVlN1RRNDUtRjZFVnV5dVBLSzh3MV84d1BKeEpTWHQ2QVFQYWlQSGtNSQ&q=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords)
  - [How to Create & use App Passwords in Gmail](https://support.google.com/mail/answer/185833?hl=en) 
- Actviate Less secure apps & your Google Account, [Google Less Secure](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbVJwa3M3cmRDeUFsUVA2ZkRjOGxyalp4NnFHQXxBQ3Jtc0trSUgwYjAwMjJwenpiNEx1RkstRGtCQy1XQVdvb3FFeDlxT0tXOGdUQUFkZkFQcEp0U2JOVjRHbTRENFFDQklGS0hFeUM3NFpyM3N2X25YajE3M2dMcHRJZUhpVVlkT3VORVQ2LWpyWjNGb1RpTGt3VQ&q=https%3A%2F%2Fmyaccount.google.com%2Flesssecureapps)

## How to use

- Change EMAIL_USER and EMAIL_PASS in "utils/emails.py" to your Email and Password (or App Password : Read [Requirement](https://github.com/Lavaruz/email-sender/edit/main/README.md#requirement-if-you-want-to-try-it))

```
EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('PYTHON_EMAIL')
```

- After changing EMAIL & PASS, you can run demo.py directly, or from CLI

```
python demo.py
```

## Overview
![App Overview](https://github.com/Lavaruz/email-sender/blob/main/utils/app_overview.gif)
