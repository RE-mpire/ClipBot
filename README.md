# App Platform

ClipBot is designed to work for Mac

# Tech Stack

- Python
- Poetry
- Pytest
- Rumps (Python library for creating status bars)

# App Intro

ClipBot, clipboard augmentation.
A a clipboard tool that provides easy access to common tools to make to clipboard more useful.

ClipBot is a powerful clipboard management tool designed to enhance your productivity by providing easy access to a variety of useful features. With ClipBot, you can effortlessly manage your clipboard history, quickly access frequently used items, and utilize a range of tools to make your clipboard more functional and efficient. Whether you're a developer, writer, or just someone who frequently uses copy-paste operations, ClipBot is here to streamline your workflow and save you time.

# Questions

### **Functionality**
ClipBot is a macOS menu bar utility that enhances the system clipboard with text manipulation and analysis tools. It continuously monitors the clipboard and provides various text transformation options through an easily accessible dropdown menu. Key features include:

- Text analysis (word count, reading time estimation)
- Format conversions (case changes, date formats, colour codes)
- Text cleanup (removing duplicates, empty lines)
- Developer utilities (hash generation, CSV conversion, Base64 encode/decode)
- Data format transformations (date, color codes)


### Usefulness

ClipBot streamlines text manipulation by allowing users to transform content directly from their system clipboard, eliminating the need to switch between applications. It boosts productivity by providing quick access to common operations like text formatting, hash generation, and data conversions, making it particularly valuable for developers and content creators. While simple in concept, its integration with the system clipboard makes it a powerful tool for everyday text processing tasks.

# Demo Video

https://github.com/user-attachments/assets/f17f226f-cf46-4f5a-9a2e-5152ae8cd6a2

# Setup

First clone the project locally
```bash
git clone https://github.com/csc301-2024-f/assignment-2-ai-app-RE-mpire.git
cd assignment-2-ai-app-RE-mpire
```

Then setup they python environment and run it.
```bash
python3 -m venv env
source env/bin/activate
pip install poetry
poetry install

# run using python3
python3 src/main.py
```

The tool should now be running in your toolbar in the upper right hand corner :)

# Testing

To run tests simply run `pytest` from the root directory of the repository.

# License
Copyright 2025 Kyle Yang

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
