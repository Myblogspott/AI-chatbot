```markdown
# Chatbot AI Project

Welcome to the Chatbot AI project! This chatbot application is built with Flask and allows interactive conversations. You can run the chatbot locally or access it remotely through ngrok. Follow the steps below to set up and run the project.

---

## Project Overview

This project provides an interactive chatbot interface powered by Flask. Users can type messages to interact with the chatbot, which responds with automated replies based on the backend logic.

---

## Prerequisites

1. **Python 3.x**: Ensure Python is installed. If it’s not installed, download it from [here](https://www.python.org/downloads/).

   - To check if Python is installed, open a terminal and run:
     ```bash
     python --version
     ```
   - If this returns a version number, you’re good to go. If not, install Python from the link above.

2. **ngrok** (optional, for remote access): [Download ngrok](https://ngrok.com/)

---

## Setup Instructions

### 1. Download and Extract the Project Files

Download the project files from the provided link and extract them to a location on your computer.

### 2. Create a Virtual Environment

Creating a virtual environment is recommended to manage dependencies.

   ```bash
   python -m venv chatbot_env
   ```

   This will create a virtual environment named `chatbot_env` in your project directory.

### 3. Activate the Virtual Environment

   - On **macOS/Linux**:

     ```bash
     source chatbot_env/bin/activate
     ```

   - On **Windows**:

     ```bash
     chatbot_env\Scripts\activate
     ```

   You should see `(chatbot_env)` at the beginning of your terminal prompt, indicating that the virtual environment is active.

### 4. Install Required Python Packages

While the virtual environment is active, install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Running the Chatbot Application

### Option 1: Local Access

#### Start the Flask Application

To start the Flask app locally, run the following command in the project directory:

```bash
python app.py
```

#### Access the Chatbot

Open a web browser and navigate to `http://127.0.0.1:5000`. You should see the chatbot interface, where you can start typing messages to interact with the bot.

### Handling API Key Error

If you encounter an error message similar to:

```plaintext
Traceback (most recent call last):
  File "/Users/username/Chatbot AI/app.py", line 6, in <module>
    client = Groq(api_key=os.getenv('GROQ_API_KEY'))
  File "/path/to/python3.x/site-packages/groq/_client.py", line 89, in __init__
    raise GroqError(
        "The api_key client option must be set either by passing api_key to the client or by setting the GROQ_API_KEY environment variable"
    )
groq.GroqError: The api_key client option must be set either by passing api_key to the client or by setting the GROQ_API_KEY environment variable
```

This error indicates that the **GROQ_API_KEY** environment variable is not set.

#### Solution:

Run the following command in your terminal to set the `GROQ_API_KEY` environment variable:

```bash
export GROQ_API_KEY="your_api_key_here"
```

**Note**: You need to replace `"your_api_key_here"` with your actual API key. You can obtain an API key from the [Groq Console](https://console.groq.com/keys?_gl=1*1qhk3qa*_gcl_au*MTA5NzYxNzEuMTczMDUzOTU1Nw..*_ga*MTA1NDY0ODYwNy4xNzMwNTM5NTU3*_ga_4TD0X2GEZG*MTczMDU2MDM2Mi4zLjAuMTczMDU2MDM2Mi42MC4wLjA.).

---

### Option 2: Remote Access Using ngrok

To make the chatbot accessible remotely, use ngrok to expose the Flask application.

1. **Start ngrok**:

   In a new terminal window, run ngrok with the following command:

   ```bash
   ngrok http 5000
   ```

2. **Get the Public URL**:

   ngrok will provide a public URL (e.g., `https://your-ngrok-id.ngrok-free.app`). Copy this URL.

3. **Access the Chatbot Remotely**:

   Open a web browser and paste the ngrok URL. You can now access the chatbot from any location using this link.

---

## Folder Structure

- `app.py`: Main application file for running the Flask server.
- `templates/`: Contains HTML templates for the chatbot UI.
- `static/`: Stores static files like CSS and JavaScript.
- `requirements.txt`: List of dependencies required for the project.

---

## Troubleshooting

- **API Key Error**: Ensure the `GROQ_API_KEY` is correctly set in your environment (refer to the [Handling API Key Error](#handling-api-key-error) section).
- **Cannot Access the Chatbot**: Verify that Flask is running with `python app.py` and, if using ngrok, that the ngrok session is active.
- **Port Already in Use**: If port `5000` is occupied, specify another port with `python app.py --port <new_port_number>`.
- **Module Not Found**: Ensure all dependencies are installed with `pip install -r requirements.txt`.

---

## Additional Notes

- **Shutting Down**: To stop the Flask server, press `Ctrl+C` in the terminal where it’s running.
- **ngrok Sessions**: Remember that ngrok sessions are temporary. Each time you restart ngrok, the public URL will change.

---

Thank you for using Chatbot AI! If you have any questions, feel free to reach out for support.
```