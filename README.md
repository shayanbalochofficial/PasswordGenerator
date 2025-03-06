# Password Generator

This `Password Generator` is a sleek, web-based tool built with Python and Streamlit, designed to create random, secure passwords in seconds. Customize your password length and choose whether to include digits or special characters—all with an easy-to-use interface! No more struggling to come up with strong passwords for your accounts.

## Features

- **Adjustable Length**: Choose a password length between 8 and 24 characters using a handy slider.
- **Customizable Options**:
  - Include digits (0-9) for added complexity.
  - Add special characters (!@#$%^&*) for extra security.
- **Default Characters**: Uses all letters (a-z, A-Z) as the base character set.
- **Interactive Web App**: Powered by Streamlit, runs in your browser with a clean, responsive design.
- **Instant Results**: Generate and view your password with a single click.

## How to Use

1. **Prerequisites**:
   - Ensure you have Python installed (version 3.7 or higher recommended).
   - Install Streamlit using `pip` or `uv` (a faster package manager):
     ```bash
     pip install streamlit
     # OR with uv
     uv pip install streamlit
     ```

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/shayanbalochofficial/PasswordGenerator.git
   cd PasswordGenerator
   ```

3. **Run the App**:
   - Execute the following command in your terminal:
     ```bash
     streamlit run password_generator.py
     ```
   - Your default web browser will open to `http://localhost:8501`, where you can start generating passwords.

4. **Usage**:
   - Adjust the password length with the slider (8-24 characters).
   - Check the boxes to include digits and/or special characters if desired.
   - Click "Generate Password" to see your new password displayed.

## Requirements
- Python 3.7+
- Streamlit (`pip install streamlit` or `uv pip install streamlit`)

## Contributors
- **[Shayan Baloch](https://github.com/shayanbalochofficial)** - Creator and developer of this Password Generator.

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments
- Built as part of my journey learning Python—proof that simple tools can make a big difference!
- Thanks to the Streamlit team for an amazing framework that makes web apps so accessible.

---

Happy password generating! 🚀
