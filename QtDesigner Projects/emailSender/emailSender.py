import smtplib
import csv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# Fill in the details for your email account
sender_email = "mshayanalwaha@gmail.com"
app_password = "uluaskwkgccmjgxr"

# List of email addresses
recipients = []


# Read the email addresses from the CSV file
# with open('nonames.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         recipients.append(row[0])

# Connect to the email server using SSL
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(sender_email, app_password)

count = 0
# Import the required library
for recipient in recipients:
    # Compose the message as a MIME message
    message = MIMEMultipart()

    # Add the body of the email to the MIME message
    message.attach(MIMEText("""\
    <html>
    <body>
        <p style="font-size:18px; font-family:Trebuchet ms; color:#073763;">
            Hello there,👋
            <br>I am a <strong>Computer Engineering student at Bilkent University</strong> and would like to explore summer internship opportunities at your company, specifically to join your <strong>frontend or software dev teams</strong>. Apart from the rigorous curriculum at Bilkent, I have also taken additional courses and have gained several skills, such as frontend development and game development (using Unity and C#). In my frontend courses, I have learnt how to use HTML5, CSS and Javascript to make interactive websites that users will engage with. You can find an example of one I made <a href = "https://scorpia2004.github.io/Brainnest-Frontend/Assignment%202%20-%20CSS/index.html">here</a>. 
            <br><br>Moreover, I have been learning <strong>React.js</strong> since last summer for building web applications and also REST with Spring for the backend. Here's a frontend web app Restaurant Menu I made using React.js: <a href = "https://github.com/SCORPIA2004/Urokodaki">link</a>. In my Unity courses, I have learnt how to make 3D games using C# and the Unity Game development engine. You can check out the 3D Martian racer game 🎮 I made a while back when learning Unity (I took inspiration from a similar game I used to play as a kid). It is published on <a href = "https://scorpia2004.itch.io">itch.io</a>.
            <br>I also have strong foundations in C++, Java and OOP, thanks to CS102 and CS201 courses at Bilkent. You can check out the CS102 project I made using Java and the Vaadin Framework <a href = "https://github.com/SCORPIA2004/CS-102-Project-ATLA-g1I">here</a>.
            <br><br>Above all, I would like to work and gain further experience by working on real-life projects with your frontend or software dev teams. I have attached my resume for you to look over, and here is the link to my <a href = "https://github.com/SCORPIA2004">GitHub</a> so you can check out more of my personal projects. I would love the opportunity to discuss how my skills and experience can contribute to your teams.
            <br><br>I hope to hear from you soon.🙌
            <br><br>P.S. I also write as a hobby; you can check it out at <a href = "https://medium.com/@mshayanalwaha">Medium</a>, and here is my <a href = "https://www.linkedin.com/in/muhammed-shayan-usman/">LinkedIn</a>.
            <br><br>Thank you,
            <br>Muhammad Shayan Usman

        </p>
    </body>
    </html>
    """, "html"))

    # Add the attachment to the MIME message
    with open("Muhammad Shayan Usman Resume.pdf", "rb") as f:
        attach = MIMEApplication(f.read(), _subtype = "pdf")
        attach.add_header("Content-Disposition", "attachment", filename = "Muhammad Shayan Usman Resume.pdf")
        message.attach(attach)

    # Set the headers for the email
    message["Subject"] = "Inquiry for Summer Internship Opportunities"
    message["From"] = sender_email
    message["To"] = recipient

    # Send the email
    server.sendmail(sender_email, recipient, message.as_string())
    print(f"Sent email to {recipient}")

# Close the connection to the email server
server.quit()
