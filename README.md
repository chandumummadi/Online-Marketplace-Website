
# Online Marketplace Website

This project is an online marketplace website built using Django, Django REST framework, and PostgreSQL. It allows users to register as buyers or sellers, manage their profiles, and perform specific activities related to buying and selling products. Admin users have full access to manage all aspects of the platform.

## Features

- User authentication and registration (buyers, sellers, admin)
- Buyers can manage addresses, payment methods, and view order history
- Sellers can manage products, view orders, and update their profiles
- Admin users can manage all users, products, orders, and have full access to all functionalities
- RESTful APIs for all operations

## Project Structure

```
marketplace/
    manage.py
    marketplace/
        __init__.py
        settings.py  
        urls.py
        wsgi.py
    users/
        __init__.py
        admin.py
        apps.py
        forms.py
        models.py
        urls.py
        views.py
    buyers/
        __init__.py
        admin.py
        apps.py
        models.py
        urls.py
        views.py
    sellers/
        __init__.py
        admin.py
        apps.py
        models.py
        urls.py
        views.py
    products/
        __init__.py
        admin.py
        apps.py
        models.py
        urls.py
        views.py
    orders/
        __init__.py
        admin.py
        apps.py
        models.py
        urls.py
        views.py
    admin_user/
        __init__.py
        admin.py
        apps.py
        models.py
        urls.py
        views.py
    templates/
        users/
            register.html
            login.html
            profile.html
        buyers/
            dashboard.html
            order_history.html
            product_list.html
            product_detail.html
        sellers/
            dashboard.html
            product_form.html
            sales_report.html
        products/
            product_detail.html
            product_list.html
        orders/
            cart.html
            checkout.html
            order_confirmation.html
```

## Installation and Setup

### Prerequisites

- Python 3.x
- PostgreSQL
- Virtualenv

### Clone the Repository

```bash
git clone https://github.com/yourusername/marketplace.git
cd marketplace
```

### Create and Activate Virtual Environment

```bash
virtualenv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure PostgreSQL Database

Create a PostgreSQL database and update the `DATABASES` setting in `marketplace/settings.py` with your database credentials.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

### Access the Application

- Admin interface: http://127.0.0.1:8000/admin/
- API endpoints: http://127.0.0.1:8000/

## API Endpoints

### Authentication

- Obtain Token: `POST /api-token-auth/`

### User Endpoints

- Register Buyer: `POST /users/register/buyer/`
- Register Seller: `POST /users/register/seller/`
- Login: `POST /users/login/`

### Buyer Endpoints

- View Dashboard: `GET /buyers/dashboard/`
- Add Address: `POST /buyers/addresses/add/`
- Add Card: `POST /buyers/cards/add/`
- View Order History: `GET /buyers/orders/`
- View Order Detail: `GET /buyers/orders/<order_id>/`

### Seller Endpoints

- View Dashboard: `GET /sellers/dashboard/`
- Update Profile: `POST /sellers/profile/update/`
- View Orders: `GET /sellers/orders/`
- View Order Detail: `GET /sellers/orders/<order_id>/`
- View Products: `GET /sellers/products/`

### Admin Endpoints

- View Dashboard: `GET /admin-user/dashboard/`
- Manage Users: `GET /admin-user/users/`
- Manage Sellers: `GET /admin-user/sellers/`
- Manage Buyers: `GET /admin-user/buyers/`
- Manage Products: `GET /admin-user/products/`
- Manage Orders: `GET /admin-user/orders/`

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

This `README.md` file provides an overview of the project, instructions for setting up the development environment, and details on how to replicate the project. It also includes information about the available API endpoints for different user roles. Adjust the URLs, repository link, and any other project-specific details as necessary.
