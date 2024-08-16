# Django File Sharing Application

This is a simple Django application that allows registered users to upload and download files. The project includes user registration, login, and logout functionality, along with a feature for displaying a list of uploaded files and allowing users to download them.

## Features

- **User Authentication:**
  - User registration with a basic form.
  - Login and logout functionality.
  - CSRF protection for forms.

- **File Upload and Management:**
  - Users can upload files.
  - Uploaded files are displayed with their descriptions, upload date, and a download button.
  - Only authenticated users can upload files.

- **Download Functionality:**
  - Users can download files they uploaded or others have shared.

## Setup and Installation

### Prerequisites

- Python 3.x
- Django 3.x or higher
- pip (Python package installer)

### Installation

1. **Clone the Repository:**

 
   git clone (https://github.com/abumoaz1/ShareYourFiles.git)
   cd file_share_app


2. **Create a Virtual Environment:**


   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`


3. **Install Dependencies:**


   pip install -r requirements.txt


4. **Run Migrations:**


   python manage.py migrate
 

6. **Run the Development Server:**


   python manage.py runserver
 

   Now you can access the application at `http://127.0.0.1:8000/`.

### Project Structure

- **`file_sharing/`**: Main Django app containing views, models, and URLs.
- **`user/`**: Handles user authentication (register, login, logout).
- **`templates/`**: HTML templates for rendering views.
- **`static/`**: Contains CSS, JavaScript, and images.
- **`media/`**: Directory where uploaded files are stored.

### Usage

- **Home Page:**
  - Displays a list of uploaded files with their descriptions and upload dates.
  - Users can download files using the provided download button.
  
- **File Upload:**
  - Authenticated users can upload files with a description.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request if you'd like to contribute.


## Contact

For any questions or feedback, feel free to reach out:

- **Email:** moazkhan7496@gmail.com
