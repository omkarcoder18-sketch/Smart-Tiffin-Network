# Smart-Tiffin-Network
Smart Tiffin Network is a multi-role meal subscription and delivery platform connecting customers, home cooks, delivery partners, and administrators through a centralized food subscription ecosystem built with Django and PostgreSQL.



# Smart Tiffin Network

## Overview

Smart Tiffin Network is a multi-role home-cooked meal subscription and delivery platform designed to connect customers, home cooks, delivery partners, and administrators through a unified digital ecosystem.

The platform helps customers discover and subscribe to affordable homemade meal plans while enabling cooks to manage menus, subscriptions, orders, and earnings efficiently. Delivery partners can handle meal deliveries, and administrators can manage operations through a centralized dashboard.

---

## Problem Statement

Many students, working professionals, and migrants struggle to find affordable, hygienic, and reliable home-cooked meals. At the same time, local home cooks often lack a digital platform to showcase their services, manage subscriptions, receive payments, and coordinate deliveries.

Smart Tiffin Network aims to bridge this gap by creating a subscription-based marketplace for homemade meals.

---

## Key Features

### Authentication & Authorization

* Multi-role registration
* Customer onboarding
* Home Cook onboarding
* Delivery Partner onboarding
* Admin access
* Email verification
* Mobile OTP verification
* Login using email or mobile number
* Password reset via OTP

### Customer Features

* Browse nearby cooks
* View menus and pricing
* Subscribe to meal plans
* Daily, weekly, and monthly subscriptions
* Order tracking
* Ratings and feedback
* Complaint management

### Cook Features

* Profile management
* Menu management
* Subscription management
* Daily order tracking
* Earnings dashboard
* Customer feedback monitoring

### Delivery Partner Features

* Assigned delivery management
* Pickup and delivery tracking
* Order status updates
* Delivery confirmation

### Admin Features

* User management
* Cook verification
* Delivery partner management
* Subscription monitoring
* Payment tracking
* Reports and analytics

---

## System Roles

| Role             | Description                                    |
| ---------------- | ---------------------------------------------- |
| Customer         | Subscribes to meal plans and tracks deliveries |
| Home Cook        | Creates menus and fulfills orders              |
| Delivery Partner | Handles meal delivery operations               |
| Admin            | Manages platform operations                    |

---

## Technology Stack

### Backend

* Python 3.x
* Django Framework
* Django REST Framework (DRF)

### Database

* PostgreSQL

### API Testing

* Postman

### Version Control

* Git
* GitHub

### Authentication

* JWT Authentication
* OTP Verification (Mobile & Email)

---

## Proposed Project Structure

```bash
smart-tiffin-network/
│
├── accounts/
│   ├── authentication
│   ├── user management
│   └── role management
│
├── customers/
│
├── cooks/
│
├── delivery/
│
├── subscriptions/
│
├── orders/
│
├── payments/
│
├── notifications/
│
├── feedback/
│
├── dashboard/
│
├── config/
│
├── requirements.txt
│
└── manage.py
```

---

## Authentication Flow

### Registration

1. Select User Role
2. Enter Registration Details
3. Mobile OTP Verification
4. Email Verification
5. Account Activation
6. Login

### Login

* Email + Password
  OR
* Mobile Number + Password

### Forgot Password

1. Enter Registered Mobile Number
2. OTP Verification
3. Reset Password
4. Login Again

---

## Future Enhancements

* Razorpay Payment Integration
* Real-Time Delivery Tracking
* Push Notifications
* AI Meal Recommendations
* Diet-Based Meal Plans
* Referral Program
* Subscription Renewal Automation
* Multi-City Expansion Support

---

## API Documentation

API endpoints will be documented and tested using Postman.

Example Modules:

* Authentication APIs
* User Management APIs
* Cook Management APIs
* Subscription APIs
* Order APIs
* Delivery APIs
* Payment APIs
* Feedback APIs

---

## Development Setup

### Clone Repository

```bash
git clone https://github.com/your-username/smart-tiffin-network.git
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your-secret-key

DEBUG=True

DB_NAME=smart_tiffin

DB_USER=postgres

DB_PASSWORD=your-password

DB_HOST=localhost

DB_PORT=5432
```

### Run Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

---

## Contributors

Developed as a scalable food subscription and delivery platform using Django and PostgreSQL.

---

## License

This project is licensed under the MIT License.

