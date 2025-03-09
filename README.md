# AudioPlayer Site

The project allows registered users to add songs or create albums using an intuitive interface. Each registered user has access to create content, listen to music, and like songs.

---

## Description

This application enables you to:
- Register and log in as a user
- Create your own album with songs
- Post your own song on a site
- Like others songs in a site
- Listen to songs with beautiful videos
- Use a simple and intiitive interface

---

## Requirements

To run the project, you will need:
- **Python 3.9** or later.
- **Django 4.2**.
- **PostgreSQL** or **SQLite** (default).

All dependencies are listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```
---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Moriarty-Zero/Audioplayer-Site.git
   cd Audioplayer-Site
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create an admin user:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

Open http://127.0.0.1:8000/ in your browser.

---

## Usage

1. Register or log in to the system.
2. Use the interface to create albums and songs
3. Use the interface to save songs
4. Listen to songs along with the video

---

## Technologies

The project was built with:
- Python 3.9
- Django 4.2

---

## Contribution

Contributions to the project are welcome!

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-your-feature`.
3. Make your changes and commit them: `git commit -m "Description of changes"`.
4. Submit a pull request.

---

## Author

**Oleksiy Klymchuk**  
[GitHub Profile](https://github.com/MoriartyZero)  
[Email](oleksiyklumchuk@gmail.com)

---

## License

This project is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0).

### Terms of use:
- You may share the material in its original form for non-commercial purposes with proper attribution.
- You may not modify, adapt, or create derivative works.
- Commercial use is prohibited.

Full text of the license is available at: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
