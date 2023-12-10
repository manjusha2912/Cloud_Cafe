# CLOUD CAFE

## Overview

CLOUD CAFE! is a cafe management system designed to streamline daily operations, manage inventory, and enhance the overall customer experience. The system provides functionalities for staff registration, login, inventory management, customer service, and reporting.

## Features

1. **Staff Management:**
   - Staff can register by providing a unique username and password.
   - Login functionality for staff members with appropriate credentials.
   - Removal of ex-staff from the system.

2. **Inventory Management:**
   - View the current stock available in the pantry.
   - Add new products to the inventory.
   - Update existing product entries, including stock and prices.

3. **Customer Service:**
   - Generate bills for customer orders.
   - Update stock and save invoice details.
   - View month-wise revenue collection.
   - View product demand.

4. **Reports:**
   - Sales report: A month-wise revenue collection report.
   - Product details: View product demand.

5. **File Handling:**
   - Invoices are generated and saved as text files.
   - CSV files are created for sales and product reports.

## Getting Started

1. **Installation:**
   - Clone the repository to your local machine.
   - Ensure you have Python installed on your system.

2. **Database Setup:**
   - Set up a MySQL database with the name "ProjectXII" and configure the connection details in the script.

3. **Dependencies:**
   - Install the required dependencies using `pip install mysql-connector-python`.

4. **Run the Program:**
   - Execute the `cloud_cafe.py` script to launch the application.

## Usage

1. **Staff Registration and Login:**
   - Use the registration feature to create a new staff account.
   - Log in with valid credentials to access the system.

2. **Inventory Management:**
   - Add, view, and update products in the pantry.

3. **Customer Service:**
   - Generate bills for customer orders.
   - View sales reports and product details.

## File Structure

- `cloud_cafe.py`: Main script containing the project code.
- `Cafebill.txt`: Default output file for invoices.
- `revenue.csv`: CSV file for the sales report.
- `products.csv`: CSV file for product details.
