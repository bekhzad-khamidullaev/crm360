# CRM360 - Django Project

CRM360 is a Django-based Customer Relationship Management (CRM) system that helps businesses manage their interactions with customers and improve overall customer satisfaction.

## Features

- **Customer Management**: Easily add, edit, and delete customer records.
- **Lead Tracking**: Keep track of potential leads and their status in the sales pipeline.
- **Communication History**: Record and view interactions and communication history with customers.
- **Task Management**: Assign tasks, set deadlines, and manage your team's workflow.
- **User Authentication**: Secure user authentication and access control.

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bekhzad-khamidullaev/crm360.git

2. Navigate to the project directory:
   ```bash
   cd crm360

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv

4. Activate the virtual environment:
   ```bash
   source venv/bin/activate

5. Install dependencies:
   ```bash
   pip install -r requirements.txt

6. Apply database migrations:
   ```bash
   python manage.py migrate

7. Create a superuser account:
   ```bash
   python manage.py createsuperuser

8. Run the development server:
   ```bash
   python manage.py runserver 

9. Access the CRM360 admin panel at http://localhost:8000/admin/ and log in with the superuser credentials.
## Usage
### Visit the CRM360 admin panel to manage customers, leads, tasks, and user accounts.
### Customize and extend the functionality according to your business needs.
## Contributing
### Contributions are welcome! Please follow the contribution guidelines.

## License
### This project is licensed under the MIT License.

## Acknowledgments
### Special thanks to the Django community for the amazing web framework.