# HTTP Verb Tampering Tool

The HTTP Verb Tampering Tool is a Python script that allows you to test and analyze the behavior of different HTTP verbs (methods) on a target URL. It helps in detecting potential vulnerabilities, verb tampering issues, and sensitive information disclosure in web applications.

## Features

- Supports a wide range of HTTP verbs, including GET, POST, HEAD, TRACE, TRACK, OPTIONS, INDEX, CONNECT, PUT, VERSION-CONTROL, PATCH, DELETE, COPY, and MOVE.
- Provides a simple command-line interface to interactively select and test HTTP verbs.
- Checks for verb tampering issues, such as unintended access or bypassing restrictions.
- Detects sensitive information disclosure in server responses.
- Outputs the server responses in a clean format, excluding HTML garbage.

## Prerequisites

- Python 3.x
- Requests library (`pip install requests`)
- Rich library (`pip install rich`)

## Usage

1. Clone the repository or download the script to your local machine.
2. Install the required dependencies mentioned in the Prerequisites section.
3. Open a terminal or command prompt and navigate to the directory where the script is located.
4. Run the script using the command `python http_verb_tampering.py`.
5. Enter the target URL when prompted.
6. Follow the prompts to select and test different HTTP verbs.
