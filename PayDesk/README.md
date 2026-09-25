# PayDesk

PayDesk is a simple customer and payment tracking dashboard for managing PayPal payments.

## Features

- **Dashboard**: Overview of total customers, amounts due, paid amounts, and payment status
- **Customers**: Manage customer information and view payment history
- **Payments**: Track payment status and history
- **PayPal Settings**: Configure PayPal integration settings

## Project Structure

```
PayDesk/
├── Apps/
│   ├── dashboard/      # Dashboard app
│   ├── customers/      # Customer management app
│   ├── payments/       # Payment tracking app
│   └── paypal/         # PayPal settings app
├── templates/          # HTML templates
├── static/            # CSS, JavaScript, and images
├── staticfiles/       # Collected static files (generated)
├── media/             # User uploaded files
├── manage.py          # Django management script
├── requirements.txt   # Python dependencies
├── .env              # Environment variables (not in git)
└── example.env       # Example environment variables
```

## Setup Instructions

### 1. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv myenv

# Activate virtual environment (Windows)
myenv\Scripts\activate

# Activate virtual environment (Mac/Linux)
source myenv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy the example environment file and configure it:

```bash
cp example.env .env
```

Edit `.env` with your configuration:

```env
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# PayPal Configuration
PAYPAL_ENVIRONMENT=sandbox
PAYPAL_CLIENT_ID=your-paypal-client-id
PAYPAL_CLIENT_SECRET=your-paypal-client-secret
PAYPAL_WEBHOOK_ID=your-paypal-webhook-id
PAYPAL_CURRENCY=USD
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

### 7. Collect Static Files (for production)

```bash
python manage.py collectstatic
```

## Usage

### Accessing the Application

- **Dashboard**: `http://localhost:8000/`
- **Customers**: `http://localhost:8000/customers/`
- **Payments**: `http://localhost:8000/payments/`
- **PayPal Settings**: `http://localhost:8000/paypal/settings/`
- **Admin Panel**: `http://localhost:8000/admin/`

### Managing Customers

1. Navigate to the Customers page
2. Add customers through the Django admin panel
3. View customer details and payment history

### Managing Payments

1. Payments are created automatically through the admin panel
2. Track payment status (Pending, Paid, Failed, etc.)
3. View complete payment history

### Configuring PayPal

1. Navigate to PayPal Settings page
2. Enter your PayPal API credentials
3. Choose environment (Sandbox or Live)
4. Save settings

## Development

### Running Django Checks

```bash
python manage.py check
```

### Creating Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Running Tests

```bash
python manage.py test
```

## Security Notes

- Never commit `.env` file to version control
- Use strong secret keys in production
- Keep PayPal credentials secure
- Set `DEBUG=False` in production
- Use proper `ALLOWED_HOSTS` in production

## Future Enhancements

This is the MVP foundation. Future enhancements may include:

- PayPal checkout integration
- Webhook handling
- Email notifications
- Advanced reporting
- Import/export functionality
- User authentication and permissions

## License

This project is provided as-is for demonstration purposes.