if mode == "passwordchange":
    if not email:
        raise ValueError("Email is required for password verification.")
    
    verification_code = str(secrets.randbelow(900000) + 100000)
    message = EmailMessage()
    message["Subject"] = "Library Password Verification"
    message["From"] = sender_email
    message["To"] = email
    message.set_content(
        f"Your verification code is: {verification_code}\n\n"
        "This is an automatically generated email; please do not reply to it."
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(message)

    for attempt in range(3):
        entered_code = input("Enter verification code: ").strip()

        if entered_code == verification_code:
            print("Verification successful!")
            break

        print("Incorrect verification code.")

    else:
        print("Too many incorrect attempts.")
        return None