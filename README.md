# Pomodoro Timer

A simple command-line Pomodoro Timer tool that helps you manage work and break sessions efficiently. It displays a progress bar for each session and sends desktop notifications to keep you on track.

## Features

- **Configurable Sessions:** Set custom durations for work and break sessions.
- **Multiple Iterations:** Specify the number of work/break cycles.
- **Progress Bar:** Visual feedback during each session using `alive_progress`.
- **Desktop Notifications:** Alerts you when a session starts or ends (requires `terminal-notifier` on macOS).

## Prerequisites

- **Python:** Version 3.7 or higher.
- **terminal-notifier:** Required for desktop notifications on macOS.  
  Install it via Homebrew if you haven't already:
  ```bash
  brew install terminal-notifier
  ```

## Installation
Clone the Repository

```
git clone <repository-url>
cd <repository-directory>
```

### Install the Package
Use the provided Makefile to install the package in editable mode along with its dependencies:

```
make
```
Alternatively, you can install the dependencies manually:

```
pip install -r requirements.txt
```
### Update Dependencies

If you need to update dependencies using pip-compile, run:

```
make deps
```
## Usage
Run the timer by specifying the work time, break time, and the number of iterations. For example:

```
pomodoro --work 1h10m --break 25m --iterations 4
```
### Command-line Arguments
```--work```: Duration of each work session (in time type eg. 1h30m, 20m, 1h).

```--break```: Duration of each break session (in time type eg. 1h30m, 20m, 1h).

```--iterations```: Number of work/break cycles.

Each work session will begin with a notification and a progress bar display for the specified duration. If there are additional iterations, a break session will follow before the next cycle.

## Development
### Code Formatting and Linting
This project uses Ruff for code formatting and linting. To automatically format the code and check for issues, run:

```
make format
```

## Tests 
### Run pytest tests 
This project uses pytest for code testing. To runn all of the tests, run:

```
make test 
```

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please feel free to open an issue or submit a pull request if you have suggestions or improvements.

## Happy timing!
