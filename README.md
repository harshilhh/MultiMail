
# MultiMail

![Visual representation of Project]({image}.webp)
MultiMail is a simple tool that allows you to send bulk emails separately using multiple email IDs. Unlike Google, which offers a similar feature as a paid service, MultiMail enables you to send emails for free by specifying your email ID and app password.

This tool is useful for:
- Working professionals (Ex. Sending reports to multiple clients separately.)
- Marketing and promotions for sanding Bulk Emails.
- Job seekers who need to send their resume to multiple recruitment firms.
- Students 

## Features
- Send bulk emails individually using multiple email IDs
- Simple and user-friendly GUI
- Secure authentication using app passwords
- Saves time by automating email sending process

## Installation

### Step 1.

Please generate an app password from the Manage your Google profile section.

Please refer [Google App Password.pdf]() file from ripository to generate password.

### Step 2.

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/MultiMail.git
    cd MultiMail
    ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Update .env file
   ```sh
   UserEmail='Your Email Address'
   AppPassword='Your App Password'

   ```
4. Run the application:
   ```sh
   python MultiMail.py
   ```


## Usage
1. Add your email ID and app password in .env file.
2. Downlode Dependences and Run the application.
3. Specify the Multiple recipient email addresses saperated by Comma ",".
4. Compose your email.
5. Click the "Send" button to send emails separately.


## Requirements
- Python 3.x
- Required Python libraries (listed in `requirements.txt`)
- App password enabled for email sending

## Contributing
Feel free to contribute by submitting issues or pull requests.

## License
This project is open-source under the MIT License.