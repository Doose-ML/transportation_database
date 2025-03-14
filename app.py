import streamlit as st
import mysql.connector

# Database connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="08022732801",
        database="transportation"
    )

# Function to execute SQL queries
def execute_query(query, params=None):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    conn.commit()
    cursor.close()
    conn.close()

# Function to fetch data from the database
def fetch_data(query, params=None):
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params or ())
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# Streamlit app
def main():
    st.title("Transportation Management System")

    menu = ["Select an option","Add Customer", "Add Trip", "Add Payment", "View Customers", "View Trips", "View Payments"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Customer":
        st.subheader("Add New Customer")
        customer_name = st.text_input("Customer Name")
        phone_number = st.text_input("Phone Number")
        next_of_kin = st.text_input("Next of Kin")
        next_of_kin_phone = st.text_input("Next of Kin Phone")

        if st.button("Add Customer"):
            query = """
            INSERT INTO customers (customer_name, phone_number, next_of_kin, next_of_kin_phone)
            VALUES (%s, %s, %s, %s)
            """
            execute_query(query, (customer_name, phone_number, next_of_kin, next_of_kin_phone))
            st.success("Customer Added Successfully!")

    elif choice == "Add Trip":
        st.subheader("Add New Trip")
        customer_id = st.number_input("Customer ID", min_value=1)
        driver_id = st.number_input("Driver ID", min_value=1)
        bus_id = st.number_input("Bus ID", min_value=1)
        location = st.text_input("Location")

        if st.button("Add Trip"):
            query = """
            INSERT INTO trips (customer_id, driver_id, bus_id, location)
            VALUES (%s, %s, %s, %s)
            """
            execute_query(query, (customer_id, driver_id, bus_id, location))
            st.success("Trip Added Successfully!")

    elif choice == "Add Payment":
        st.subheader("Add New Payment")
        trip_id = st.number_input("Trip ID", min_value=1)
        amount_paid = st.number_input("Amount Paid", min_value=0.0)
        payment_method = st.selectbox("Payment Method", ["Cash", "Card"])

        if st.button("Add Payment"):
            query = """
            INSERT INTO payments (trip_id, amount_paid, payment_method)
            VALUES (%s, %s, %s)
            """
            execute_query(query, (trip_id, amount_paid, payment_method))
            st.success("Payment Added Successfully!")

    elif choice == "View Customers":
        st.subheader("View Customers")
        customers = fetch_data("SELECT * FROM customers")
        st.table(customers)

    elif choice == "View Trips":
        st.subheader("View Trips")
        trips = fetch_data("SELECT * FROM trips")
        st.table(trips)

    elif choice == "View Payments":
        st.subheader("View Payments")
        payments = fetch_data("SELECT * FROM payments")
        st.table(payments)

if __name__ == "__main__":
    main()