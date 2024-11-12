Django Portfolio Website 

This is a personal portfolio website built with Django as the backend server and HTML, CSS, and JavaScript for the frontend design. The unique feature of this portfolio is that it supports dynamic data management through Django's built-in admin panel. This allows you to easily update your profile information, portfolio projects, education details, social links, and other content directly from the database, without modifying the code.

Features
Dynamic Content Management: Update profile details (profile image, name, designation, about, social links) directly from the Django admin panel.
Projects Section: Add, edit, or delete project entries with descriptions, links, and other project-specific details.
Education Section: Manage education-related details like school/college names, degrees, years, and descriptions.
Social Links: Update social media links (LinkedIn, GitHub, etc.) through the admin panel.
Fully Responsive Design: Ensures the website is accessible and visually appealing on all device sizes.
Technologies Used
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Database: SQLite (default) or other Django-supported databases
Admin Panel: Django's built-in admin interface
Setup Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
Create a virtual environment:

bash
Copy code
python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run migrations to set up the database:

bash
Copy code
python manage.py migrate
Create a superuser for admin panel access:

bash
Copy code
python manage.py createsuperuser
Start the development server:

bash
Copy code
python manage.py runserver
Access the website and admin panel:

Portfolio Website: Visit https://amanraja.pythonanywhere.com
Project Structure
core: Contains the main Django settings and configuration files.
portfolio: Django app with views, models, and templates for the portfolio website.
models.py: Defines data models for profile information, projects, education, and social links.
views.py: Handles the logic for fetching data from the database and rendering templates.
templates/: Contains the HTML templates for various pages.
static/: Includes CSS, JavaScript, and images for frontend styling.
Customization
To customize your portfolio:

Admin Panel: Use the admin panel to add or update profile details, projects, education, and social links.
Frontend Design: Modify the HTML/CSS/JavaScript in the templates/ and static/ directories if you want to change the website’s design.
Contributing
Contributions are welcome! Please fork the repository and create a pull request if you want to add new features or make improvements.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Feel free to replace yourusername/yourrepository with the actual GitHub repository link and update any project details. This README file provides an overview of the project and setup instructions for new users or contributors.






