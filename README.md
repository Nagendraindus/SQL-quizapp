
# SQL Quiz Game

This is a simple SQL Quiz Game developed using Python and the Tkinter library. The game provides a graphical interface to test your SQL knowledge by answering multiple-choice questions. The application features a modern UI with customizable color schemes and fonts. It compliles the questions of CodeHelp "Common SQL Queries for Interviews". https://www.youtube.com/watch?v=vIq9zkpGWc8 

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Features
- Questions compiled from CodeHelp SQL video
- Multiple-choice questions related to SQL.
- Modern UI with customizable colors and fonts.
- Displays score after each question and at the end of the quiz.
- Customizable icon and title bar for a personalized look.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Nagendraindus/SQL-quizapp.git
   ```

2. **Ensure you have Python installed (Python 3.6 or later is recommended).**

3. **Install the required dependencies:**

  

   > Note: No additional dependencies are needed beyond the Tkinter library, which is included with most Python installations.

## Usage

1. **Run the application:**

   ```bash
   python up.py
   ```

2. **Play the game:**

   - Read the question displayed on the screen.
   - Select the correct answer from the options provided.
   - Click the "Check Answer" button to submit your answer.
   - The correct answer will be highlighted, and your score will be updated.
   - Continue through the quiz until all questions have been answered.

## Customization

### Color Scheme

The color scheme of the application can be modified by changing the values in the `COLOR_SCHEME` dictionary within the `up.py` file:

```python
COLOR_SCHEME = {
    "sapphire": "#4059ad",
    "blue_gray": "#6b9ac4",
    "tiffany_blue": "#97d8c4",
    "antiflash_white": "#eff2f1",
    "xanthous": "#f4b942",
    "option_bg": "#ffffff",
    "correct": "#28a745",
    "incorrect": "#dc3545",
    "button_hover": "#5a73e5",
    "button_active": "#283e6e"
}
```

### Font Styles

The font styles can be adjusted by modifying the following variables in the `up.py` file:

```python
font_family = "Segoe UI"
question_font = (font_family, 16, "bold")
option_font = (font_family, 14)
button_font = (font_family, 14)
score_font = (font_family, 14, "italic")
```

### Custom Icon

To change the application icon, replace the `icon.ico` file located at the specified path in the `up.py` file:

```python
self.iconbitmap("C:/Users/Public/Desk/py/icon.ico")
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## License

This project is licensed under the APACHE License. See the [LICENSE](LICENSE) file for details.



