# Tools

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Some simple tools. Contents that I use in my daily life.

## General System Requirements

- Python 3.x
- Windows system (Some May be tested on Linux/WSL/Ubuntu)
- [Quicker](https://getquicker.net/)
- Adjust Antivirus Software

## General Usage and Guide

Most tools are used by command line like PowerShell or Quicker(to shell).

### About Log Files and Privacy

This is a concise project, maybe just written with an idea in hand, so I didn't consider specific implementations such as logs and privacy, nor did I check the dependencies and initial files of each program.

The purpose of this project is to share, so I will try to improve it as much as possible to make it more convenient to use.

Feel free to make a pull request or open an issue!

---

## Programs

Simple explanations about programs, and record their concepts and ideas.

### Record Rename By Time

#### Overview

`RecordRenameByTime` is a Python tool designed to automatically rename audio files based on their creation timestamps. This utility is especially useful for managing voice recordings, audio files, and speech data before processing with speech-to-text (STT) or TTS systems. It ensures that your files are systematically organized by their timestamps, making them easier to retrieve and manage.

#### Features

- **Automatic Timestamp Renaming**: Renames audio files using their creation date and time as the filename, ensuring a unique and chronological order.
- **Duplicate Handling**: Detects duplicates and handles them gracefully by either skipping or renaming with an additional suffix.
- **Error Handling**: Identifies files with missing metadata and moves them to a separate error directory for further investigation.
- **Supported Formats**: Works with popular audio formats such as `.m4a`, `.mp3`, `.wav`, and `.flac`.

#### Usage for `Record Rename By Time`

To use `RecordRenameByTime`, simply run the tool in your terminal. There are 2 ways to run the tool:

1. `python3 record_rename_by_time.py`: This command will read the audio files from the `source` directory in the same folder and copy them to the `renamed` directory with the renamed filenames.
2. `python3 record_rename_by_time.py <source_folder> <destination_folder>`: This command will read the audio files from the `source_folder` directory and copy them to the `destination_folder` directory with the renamed filenames.

#### Requirements

- Python 3.x
- FFmpeg (for metadata extraction)

### My Time Aware

Originally named `作息与时差.py` (Schedule and jet lag)

I often experience irregular sleep patterns, which I guess is a common human imperfection.

My approach and belief are not to force myself but to face the reality and facts squarely.

I personally find this essential and necessary. Adjustments might come naturally or could be deliberate actions later.

Regarding health, some people are naturally night owls, while others are morning larks. However, some have irregular patterns, and others have regular patterns that are not their preference.

Regardless, it's worth noting not just when a person wakes up too late or too early, but how long they stay awake.

Assuming a standard 24-hour day (with exceptions), we might further assume a life pattern of waking with the sunrise and sleeping at sunset. In a typical scenario, a "standard person" might be assumed to sleep for 8 hours, waking at 7 AM and sleeping at 11 PM.

This is an overly idealized assumption, but it provides a meaningful hint and reference.

#### Usage for `My Time Aware`

Please configure tools like Quicker or others to call this Python program through a PowerShell script.

If you need to update the time, enter the new time and press Enter.

If not, simply press Enter to close and exit.

Since viewing is more frequent, I have omitted the prompt for updating the time.

### sc2map

I enjoy playing StarCraft II to pass the time, but I dislike certain maps and commanders, so I wrote a simple script to manage this.

### open_clipboard

I studied and practiced [Docstring](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings) with Sphinx, initially practiced with pylint, and performed some simple operations. This script reads file or folder paths from the clipboard and opens them in the file explorer.

### base64_checker

Checks if a base64-encoded string matches the original image. Supports command-line arguments as well as interactive input.

---

## Reminders (Personal Study Notes)

File naming rules for Python scripts: generally use lowercase, but if multiple words are involved, use underscores to separate them, like `my_clock.py`.

### sphinx

- Installation: `pip install sphinx`, then `cd toy`
- Usage: Initialize a documentation directory with `python -m sphinx.cmd.quickstart docs`, which generates Sphinx documentation under the `docs` directory.
- Generate API documentation with `python -m sphinx.ext.apidoc -f -o docs/source .`
- To build the documentation: `python -m sphinx -b html docs mydocs` to generate HTML documents, or use `make html` on Linux.

## License

This project is licensed under the MIT License.
