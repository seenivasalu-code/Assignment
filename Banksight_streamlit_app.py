import streamlit as st      
import mysql.connector as mysql
import pandas as pd
from datetime import datetime
from decimal import Decimal
db=mysql.connect(
    host="localhost",
    user="seenu",
    password="Travel123",
    )
cursor=db.cursor()

#st.write("This is a simple Streamlit application.")
st.sidebar.header("BankSight Navigation")           
selected_page = st.sidebar.radio("Go to:", ("Introduction", "View Tables", "Filter Data", "CRUD Operations", "Credit / Debit Simulation", "Analytical Insights", "About Creator"))
if selected_page == "Introduction":
    st.title("BankSight Dashboard")
    st.header("Project Overview")
    st.write("BankSight is a financial data analysis tool designed to help users visualize and manage their banking data effectively. With BankSight, users can view detailed tables, filter data based on various criteria, perform CRUD operations, and simulate credit/debit transactions. Additionally," \
    " the platform provides analytical insights to help users make informed financial decisions.  ")
    st.subheader("Objectives:")     
    st.write("""1.   Provide a user-friendly interface for viewing financial data.
                2. Enable filtering and sorting of financial records.
                3. Support CRUD operations for managing financial data.
                4. Simulate credit and debit transactions.
                5. Generate analytical insights from financial data.
                """)
    st.subheader("Technologies Used:")
    st.write("""- Streamlit for web application development.
            - Mysql for database management.
            - Python for backend logic.
            """)
elif selected_page == "View Tables":
        st.title("View Financial Tables")
        selected_value=st.selectbox("Select Table to View:", ["Accounts", "Branches","Credit Cards", "Customers",  "Loans", "Support Tickets","Transactions"])  
        if selected_value == "Accounts":
            cursor.execute("USE banksight;")
            cursor.execute("SELECT * FROM accounts;")
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
            st.dataframe(df)      
        elif selected_value == "Branches":
                cursor.execute("USE banksight;")
                cursor.execute("SELECT * FROM branches;")
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                st.dataframe(df)  
        elif selected_value == "Credit Cards":  
                cursor.execute("USE banksight;")
                cursor.execute("SELECT * FROM credit_cards;")
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                st.dataframe(df) 
        elif selected_value == "Customers":
                cursor.execute("USE banksight;")
                cursor.execute("SELECT * FROM customers;")
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                st.dataframe(df) 
        elif selected_value == "Loans":
                cursor.execute("USE banksight;")
                cursor.execute("SELECT * FROM loans;")
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                st.dataframe(df) 
        elif selected_value == "Support Tickets":
                cursor.execute("USE banksight;")
                cursor.execute("SELECT * FROM support_tickets;")
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                st.dataframe(df) 
        elif selected_value == "Transactions":
                cursor.execute("USE banksight;")
                cursor.execute("SELECT * FROM transactions;")
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                st.dataframe(df)        
    # st.write("This is the View Tables page.")
elif selected_page == "Filter Data":
        st.write("This is the Filter Data page.")
        st.title("Filter Financial Data")
        st.write("select table to filter data")
        selected_value=st.selectbox("Select Table to Filter:", ["Accounts", "Branches","Credit Cards", "Customers",  "Loans", "Support Tickets","Transactions"])  
        if selected_value == "Accounts":
            st.write("Filter Accounts Table")
            cursor.execute("USE banksight;")
            cursor.execute("SELECT * FROM accounts;")   
            data = cursor.fetchall()
            columns = [i[0] for i in cursor.description]
            filter_column = st.selectbox("Select Column to Filter By:", columns) 
            filter_value = st.selectbox("Select Value to Filter For:", pd.DataFrame(data, columns=columns)[filter_column].unique())
            query = f"SELECT * FROM accounts WHERE {filter_column} = %s;"
            cursor.execute(query, (filter_value,))
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
            st.dataframe(df)
        elif selected_value == "Branches":
            st.write("Filter Branches Table")
            cursor.execute("USE banksight;")
            cursor.execute("SELECT * FROM branches;")   
            data = cursor.fetchall()
            columns = [i[0] for i in cursor.description]
            filter_column = st.selectbox("Select Column to Filter By:", columns)  
            filter_value = st.selectbox("Select Value to Filter For:", pd.DataFrame(data, columns=columns)[filter_column].unique())
            query = f"SELECT * FROM branches WHERE {filter_column} = %s;"
            cursor.execute(query, (filter_value,))
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
            st.dataframe(df)   
        elif selected_value == "Credit Cards":
            st.write("Filter Credit Cards Table")
            cursor.execute("USE banksight;")
            cursor.execute("SELECT * FROM credit_cards;")   
            data = cursor.fetchall()
            columns = [i[0] for i in cursor.description]
            filter_column = st.selectbox("Select Column to Filter By:", columns)  # Adjusted to avoid non-filterable columns filter
            filter_value = st.selectbox("Select Value to Filter For:", pd.DataFrame(data, columns=columns)[filter_column].unique())
            query = f"SELECT * FROM credit_cards WHERE {filter_column} = %s;"
            cursor.execute(query, (filter_value,))
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
            st.dataframe(df)
        elif selected_value == "Customers":
            st.write("Filter Customers Table")
            cursor.execute("USE banksight;")
            cursor.execute("SELECT * FROM customers;")   
            data = cursor.fetchall()
            columns = [i[0] for i in cursor.description]
            filter_column = st.selectbox("Select Column to Filter By:", columns)  # Adjusted to avoid non-filterable columns filter
            filter_value = st.selectbox("Select Value to Filter For:", pd.DataFrame(data, columns=columns)[filter_column].unique())
            query = f"SELECT * FROM customers WHERE {filter_column} = %s;"
            cursor.execute(query, (filter_value,))
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
            st.dataframe(df)
        elif selected_value == "Loans":
            st.write("Filter Loans Table")
            cursor.execute("USE banksight;")
            cursor.execute("SELECT * FROM loans;")   
            data = cursor.fetchall()
            columns = [i[0] for i in cursor.description]
            filter_column = st.selectbox("Select Column to Filter By:", columns)  # Adjusted to avoid non-filterable columns filter
            filter_value = st.selectbox("Select Value to Filter For:", pd.DataFrame(data, columns=columns)[filter_column].unique())
            query = f"SELECT * FROM loans WHERE {filter_column} = %s;"
            cursor.execute(query, (filter_value,))
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
            st.dataframe(df)  
        elif selected_value == "Support Tickets":
                st.write("Filter Support Tickets Table")
                cursor.execute("USE banksight;")
                cursor.execute("SELECT * FROM support_tickets;")   
                data = cursor.fetchall()
                columns = [i[0] for i in cursor.description]
                filter_column = st.selectbox("Select Column to Filter By:", columns)  # Adjusted to avoid non-filterable columns filter
                filter_value = st.selectbox("Select Value to Filter For:", pd.DataFrame(data, columns=columns)[filter_column].unique())
                query = f"SELECT * FROM support_tickets WHERE {filter_column} = %s;"
                cursor.execute(query, (filter_value,))
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                st.dataframe(df)
        elif selected_value == "Transactions":
                st.write("Filter Transactions Table")
                cursor.execute("USE banksight;")
                cursor.execute("SELECT * FROM transactions;")   
                data = cursor.fetchall()
                columns = [i[0] for i in cursor.description]
                filter_column = st.selectbox("Select Column to Filter By:", columns)  # Adjusted to avoid non-filterable columns filter
                filter_value = st.selectbox("Select Value to Filter For:", pd.DataFrame(data, columns=columns)[filter_column].unique())
                query = f"SELECT * FROM transactions WHERE {filter_column} = %s;"
                cursor.execute(query, (filter_value,))
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                st.dataframe(df)
        # End of Filter Data Page        
        
elif selected_page == "CRUD Operations":
        st.title("CRUD Operations")
        selected_value=st.selectbox("Select Table for CRUD Operations:", ["Accounts", "Branches","Credit Cards", "Customers",  "Loans", "Support Tickets","Transactions"])
        selected_operation=st.selectbox("Select Operation:", ["Create", "Read", "Update", "Delete"])
        st.write(f"You have selected to perform {selected_operation} operation on {selected_value} table.")
        # Implement CRUD operations here based on selected_value and selected_operation 
        if selected_operation == "Create":
            st.write(f"Here you can create a new record in the {selected_value} table.")
            current_dt = datetime.now()
            if selected_value == "Accounts":
                cursor.execute("USE banksight;")
                cursor.execute(f"SELECT customer_id FROM customers;")
                customer_ids = [row[0] for row in cursor.fetchall()]
                with st.form("create_account_form"):
                    cursor.execute("USE banksight;")
                    cursor.execute(f"SELECT customer_id FROM {selected_value};")
                    customer_ids = [row[0] for row in cursor.fetchall()]
                    customer_id = st.selectbox("Customer ID", customer_ids)
                    last_updated = st.text_input(
                    "Created At",
                    value=current_dt.strftime("%Y-%m-%d %H:%M:%S"),
                    disabled=True)
                    account_balance = st.number_input("Balance", min_value=0.0, step=100.0)
                    submit = st.form_submit_button("Create Account")

                if submit:
                    try:
                        cursor.execute(
                                "SELECT 1 FROM accounts WHERE customer_id = %s",
                                (customer_id,)
                        )
                        if cursor.fetchone():
                            st.error("Account with this Customer ID already exists.")
                        else:  
                            cursor.execute(
                                """
                                INSERT INTO accounts (customer_id, last_updated, account_balance)
                                VALUES (%s, %s, %s)
                                """,
                                (customer_id, last_updated, account_balance)
                            )
                            db.commit()
                            st.success("New account created successfully")
                    except Exception as e:
                        db.rollback()
                        st.error(f"Error creating account: {e}")
                        cursor.close()

            elif selected_value == "Branches":
                with st.form("create_branch_form"):
                    branch_ID = st.text_input("Branch ID")
                    branch_name = st.text_input("Branch Name")
                    branch_city = st.text_input("Branch City")
                    manager_name = st.text_input("Manager Name")
                    total_employees = st.number_input("Total Employees", min_value=0)
                    branch_revenue = st.number_input("Branch Revenue", min_value=0.0)
                    opening_date = st.date_input("Opening Date")
                    performance_rating = st.slider("Performance Rating", 1, 5)
                    submit = st.form_submit_button("Create Branch")

                if submit:
                    try:
                        cursor.execute("USE banksight;")
                        query = """
                        INSERT INTO branches (Branch_ID,Branch_Name,City,Manager_Name,Total_Employees,Branch_Revenue,Opening_Date,Performance_Rating)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s) 
                        """
                        cursor.execute(query, (branch_ID,branch_name,branch_city,manager_name,total_employees,branch_revenue,opening_date,performance_rating))
                        db.commit()
                        st.success("New branch created successfully")
                    except Exception as e:
                        db.rollback()
                        st.error(f"Error creating branch: {e}")
                        cursor.close()

            elif selected_value == "Credit Cards":      
                with st.form("create_credit_card_form"):
                    Card_ID = st.text_input("Card ID")
                    Customer_ID = st.text_input("Customer ID")
                    Account_ID = st.text_input("Account ID")
                    Branch = st.text_input("Branch")
                    Card_Number = st.text_input("Card Number")
                    Card_Type = st.text_input("Card Type")
                    Card_Network = st.text_input("Card Network")
                    Credit_Limit = st.number_input("Credit Limit", min_value=0.0)
                    Current_Balance = st.number_input("Current Balance", min_value=0.0)
                    Issued_Date = st.date_input("Issued Date")
                    Expiry_Date = st.date_input("Expiry Date")
                    Status = st.text_input("Status")
                    opening_date = st.date_input("Opening Date")
                    performance_rating = st.slider("Performance Rating", 1, 5)
                    submit = st.form_submit_button("Create Credit Card")

                if submit:
                    try:
                        cursor.execute("USE banksight;")
                        query = """
                        INSERT INTO credit_cards (Card_ID,Customer_ID,Account_ID,Branch,Card_Number,Card_Type,Card_Network,Credit_Limit,Current_Balance,Issued_Date,Expiry_Date,Status)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)            
                        """
                        cursor.execute(query, (Card_ID,Customer_ID,Account_ID,Branch,Card_Number,Card_Type,Card_Network,Credit_Limit,Current_Balance,Issued_Date,Expiry_Date,Status))
                        db.commit()
                        st.success("New credit card created successfully")
                    except Exception as e:
                        db.rollback()
                        st.error(f"Error creating credit card: {e}")
                        cursor.close()

            elif selected_value == "Customers":      
                with st.form("create_customer_form"):
                    Customer_ID = st.text_input("Customer ID")
                    Customer_Name = st.text_input("Customer Name")
                    options = {
                    "Male": "M",
                        "Female": "F",
                        "Other": "O"
                    }

                    selected_text = st.selectbox("Gender",list(options.keys()))
                    Gender = options[selected_text]
                    Age = st.number_input("Age", min_value=15)
                    City = st.text_input("City")
                    Account_Type = st.selectbox("Account Type", ["Savings", "Checking", "Credit"])
                    Join_Date = st.date_input("Join Date", value=current_dt.date())             
                    submit = st.form_submit_button("Create Customer")

                if submit:
                        try:
                            cursor.execute("USE banksight;")
                            query = """
                            INSERT INTO customers (customer_id,name,gender,age,city,account_type,join_date)
                            VALUES (%s,%s,%s,%s,%s,%s,%s)            
                            """
                            cursor.execute(query,   (Customer_ID,Customer_Name,Gender,Age,City,Account_Type,Join_Date))
                            db.commit()
                            st.success("New customer created successfully")
                        except Exception as e:
                            db.rollback()
                            st.error(f"Error creating customer: {e}")
                            cursor.close()

            elif selected_value == "Loans": 
                cursor.execute("USE banksight;")
                cursor.execute(f"SELECT customer_id FROM loans;")    
                customer_ids = [row[0] for row in cursor.fetchall()]
                cursor.execute(f"SELECT account_id FROM loans;")  
                account_ids = [row[0] for row in cursor.fetchall()]                
                cursor.execute(f"SELECT branch_id, branch_name FROM branches ORDER BY branch_name;")  
                branch_names = [row[1] for row in cursor.fetchall()]

                with st.form("create_Loan_form"):
                    Loan_ID = st.text_input("Loan ID")
                    Customer_ID = st.selectbox("Customer ID", customer_ids)
                    Account_ID = st.selectbox("Account ID", account_ids)
                    Branch = st.selectbox("Branch", branch_names)
                    Loan_Type = st.selectbox("Loan Type", ["Personal", "Home", "Auto", "Business"])
                    Loan_Amount = st.number_input("Loan Amount", min_value=0.0)
                    Interest_Rate = st.number_input("Interest Rate", min_value=0.0)
                    Loan_Term_Months = st.number_input("Loan Term (Months)", min_value=1)
                    Start_Date = st.date_input("Start Date", value=current_dt.date())
                    End_Date = st.date_input("End Date", value=current_dt.date())
                    Loan_Status = st.selectbox("Loan Status", ["Active","Approved", "Closed", "Defaulted"])
                    submit = st.form_submit_button("Create Loan")

                if submit:
                    try:
                        cursor.execute("USE banksight;")
                        query = """
                        INSERT INTO loans (loan_ID,Customer_ID,Account_ID,Branch,Loan_Type,Loan_Amount,Interest_Rate,Loan_Term_Months,Start_Date,End_Date,Loan_Status)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)            
                        """
                        cursor.execute(query, (Loan_ID,Customer_ID,Account_ID,Branch,Loan_Type,Loan_Amount,Interest_Rate,Loan_Term_Months,Start_Date,End_Date,Loan_Status))
                        db.commit()
                        st.success("New loan created successfully")
                    except Exception as e:
                        db.rollback()
                        st.error(f"Error creating loan  : {e}")
                        cursor.close()
            elif selected_value == "Support Tickets":  
                cursor.execute("USE banksight;")
                cursor.execute(f"SELECT customer_id,loan_id FROM loans;")    
                customer_ids = [row[0] for row in cursor.fetchall()]
                cursor.execute(f"SELECT account_id FROM loans;")  
                account_ids = [row[0] for row in cursor.fetchall()] 
                loan_ids = [row[1] for row in cursor.fetchall()]               
                cursor.execute(f"SELECT branch_id, branch_name FROM branches ORDER BY branch_name;")  
                branch_names = [row[1] for row in cursor.fetchall()]     
                with st.form("create_support_tickets_form"):    
                    Ticket_ID = st.text_input("Ticket ID")
                    Customer_ID = st.selectbox("Customer ID", customer_ids)
                    Account_ID = st.selectbox("Account ID", account_ids)
                    Loan_ID = st.text_input("Loan ID",loan_ids)
                    Branch_Name = st.selectbox("Branch Name", branch_names)
                    Issue_Category = st.text_input("Issue Category")
                    Description = st.text_area("Description")
                    Date_Opened = st.date_input("Date Opened", value=current_dt.date())
                    Date_Closed = st.date_input("Date Closed", value=current_dt.date())
                    Priority = st.selectbox("Priority", ["Low", "Medium", "High","Critical"])
                    Status = st.selectbox("Status", ["Open", "In Progress", "Closed"])
                    Resolution_Remarks = st.text_area("Resolution Remarks")
                    Support_agent = st.text_input("Support Agent")
                    Customer_Rating = st.slider("Customer Rating", 1, 5)
                    opening_date = st.date_input("Opening Date")
                    performance_rating = st.slider("Performance Rating", 1, 5)
                    submit = st.form_submit_button("Create support_tickets")

                if submit:
                        try:
                            cursor.execute("USE banksight;")
                            query = """
                            INSERT INTO support_tickets (Ticket_ID,Customer_ID,Account_ID,Loan_ID,Branch_Name,Issue_Category,Description,Date_Opened,Date_Closed,
                            Priority,Status,Resolution_Remarks,Support_agent,Customer_Rating)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                            """
                            cursor.execute(query, (Ticket_ID,Customer_ID,Account_ID,Loan_ID,Branch_Name,Issue_Category,Description,Date_Opened,Date_Closed,
                            Priority,Status,Resolution_Remarks,Support_agent,Customer_Rating))
                            db.commit()
                            st.success("New support_tickets created successfully")
                        except Exception as e:
                            db.rollback()
                            st.error(f"Error creating support_tickets: {e}")
                            cursor.close()

            elif selected_value == "Transactions":  
                cursor.execute("USE banksight;")
                cursor.execute(f"SELECT customer_id FROM customers;")    
                customer_ids = [row[0] for row in cursor.fetchall()]
                current_dt = datetime.now()
                with st.form("create_transaction_form"):
                    Transaction_ID = st.text_input("Transaction ID")
                    Customer_ID = st.selectbox("Customer ID", customer_ids)
                    Transaction_Type = st.selectbox("Transaction Type", ["Deposit", "Withdrawal", "Online Fraud", "Transfer", "Purchase"])
                    Amount = st.number_input("Amount", min_value=0.0)
                    Transaction_DateTime = st.text_input(
                    "Created At", 
                    value=current_dt.strftime("%Y-%m-%d %H:%M:%S"),
                    disabled=True)
                    Status = st.selectbox("Status", ["Success", "Failed"])
                    submit = st.form_submit_button("Create Transaction")

                if submit:
                        try:
                            cursor.execute("USE banksight;")
                            query = """
                            INSERT INTO transactions (txn_id,customer_id,txn_type,amount,txn_time,status)
                            VALUES (%s,%s,%s,%s,%s,%s)            
                            """
                            cursor.execute(query, (Transaction_ID,Customer_ID,Transaction_Type,Amount,Transaction_DateTime,Status))
                            db.commit()
                            st.success("New transaction created successfully")
                        except Exception as e:
                            db.rollback()
                            st.error(f"Error creating transaction: {e}")
                            cursor.close()
                #End of Create Operation
        elif selected_operation == "Read":
                    if selected_value == "Accounts":
                        cursor.execute("USE banksight;")
                        cursor.execute("SELECT * FROM accounts;")
                        data = cursor.fetchall()
                        df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                        st.dataframe(df)      
                    elif selected_value == "Branches":
                        cursor.execute("USE banksight;")
                        cursor.execute("SELECT * FROM branches;")
                        data = cursor.fetchall()
                        df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                        st.dataframe(df)  
                    elif selected_value == "Credit Cards":  
                        cursor.execute("USE banksight;")
                        cursor.execute("SELECT * FROM credit_cards;")
                        data = cursor.fetchall()
                        df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                        st.dataframe(df) 
                    elif selected_value == "Customers":
                        cursor.execute("USE banksight;")
                        cursor.execute("SELECT * FROM customers;")
                        data = cursor.fetchall()
                        df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                        st.dataframe(df) 
                    elif selected_value == "Loans":
                        cursor.execute("USE banksight;")
                        cursor.execute("SELECT * FROM loans;")
                        data = cursor.fetchall()
                        df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                        st.dataframe(df) 
                    elif selected_value == "Support Tickets":
                        cursor.execute("USE banksight;")
                        cursor.execute("SELECT * FROM support_tickets;")
                        data = cursor.fetchall()
                        df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                        st.dataframe(df) 
                    elif selected_value == "Transactions":
                        cursor.execute("USE banksight;")
                        cursor.execute("SELECT * FROM transactions;")
                        data = cursor.fetchall()
                        df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                        st.dataframe(df)  

            #End of Read Operation


        elif selected_operation == "Update":
            st.write(f"Here you can update records in the {selected_value} table.")
            # Implement update functionality here
            if selected_value == "Accounts":
                cursor.execute("USE banksight;")

                # Get full table (needed for cursor.description)
                cursor.execute("SELECT * FROM accounts")
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]

                pk = columns[0]  # row[0] as PK

                # Build record map
                records = [dict(zip(columns, row)) for row in rows]
                record_map = {r[pk]: r for r in records}

                selected_pk = st.selectbox(pk, record_map.keys())
                record = record_map[selected_pk]
                editable_fields = [c for c in columns if c != pk]
                field_to_update = st.selectbox("Select Column to update", editable_fields)
                current_value = record[field_to_update]

                with st.form("update_account_form"):
                    if isinstance(current_value, (int, float)):
                        new_value = st.number_input(
                            field_to_update,
                            value=float(current_value)
                        )
                    else:
                        new_value = st.text_input(
                            field_to_update,
                            value=str(current_value)
                        )

                    submit = st.form_submit_button("Update")
                if submit:
                    try:
                        cursor.execute(
                            f"""
                            UPDATE accounts
                            SET {field_to_update} = %s
                            WHERE {pk} = %s
                            """,
                            (new_value, selected_pk)
                        )
                        db.commit()
                        st.success("Record updated successfully")
                    except Exception as e:
                        db.rollback()
                        st.error(f"Error updating record: {e}")
                        cursor.close()
            elif selected_value == "Branches":
                        cursor.execute("USE banksight;")

                        # Get full table (needed for cursor.description)
                        cursor.execute("SELECT * FROM branches")
                        rows = cursor.fetchall()
                        columns = [col[0] for col in cursor.description]

                        pk = columns[0]  # row[0] as PK

                        # Build record map
                        records = [dict(zip(columns, row)) for row in rows]
                        record_map = {r[pk]: r for r in records}

                        selected_pk = st.selectbox(pk, record_map.keys())
                        record = record_map[selected_pk]
                        editable_fields = [c for c in columns if c != pk]
                        field_to_update = st.selectbox("Select Column to update", editable_fields)
                        current_value = record[field_to_update]

                        with st.form("update_branch_form"):
                            if isinstance(current_value, (int, float)):
                                new_value = st.number_input(
                                    field_to_update,
                                    value=float(current_value)
                                )
                            else:
                                new_value = st.text_input(
                                    field_to_update,
                                    value=str(current_value)
                                )

                            submit = st.form_submit_button("Update")
                        if submit:
                            try:
                                cursor.execute(
                                    f"""
                                    UPDATE branches
                                    SET {field_to_update} = %s
                                    WHERE {pk} = %s
                                    """,
                                    (new_value, selected_pk)
                                )
                                db.commit()
                                st.success("Record updated successfully")
                            except Exception as e:
                                db.rollback()
                                st.error(f"Error updating record: {e}")
                                cursor.close()
            elif selected_value == "Credit Cards":
                        # Implement update functionality for Credit Cards table
                        cursor.execute("USE banksight;")

                        # Get full table (needed for cursor.description)
                        cursor.execute("SELECT * FROM credit_cards")
                        rows = cursor.fetchall()
                        columns = [col[0] for col in cursor.description]

                        pk = columns[0]  # row[0] as PK

                        # Build record map
                        records = [dict(zip(columns, row)) for row in rows]
                        record_map = {r[pk]: r for r in records}

                        selected_pk = st.selectbox(pk, record_map.keys())
                        record = record_map[selected_pk]
                        editable_fields = [c for c in columns if c != pk]
                        field_to_update = st.selectbox("Select Column to update", editable_fields)
                        current_value = record[field_to_update]

                        with st.form("update_branch_form"):
                            if isinstance(current_value, (int, float)):
                                new_value = st.number_input(
                                    field_to_update,
                                    value=float(current_value)
                                )
                            else:
                                new_value = st.text_input(
                                    field_to_update,
                                    value=str(current_value)
                                )

                            submit = st.form_submit_button("Update")
                        if submit:
                            try:
                                cursor.execute(
                                    f"""
                                    UPDATE credit_cards
                                    SET {field_to_update} = %s
                                    WHERE {pk} = %s
                                    """,
                                    (new_value, selected_pk)
                                )
                                db.commit()
                                st.success("Record updated successfully")
                            except Exception as e:
                                db.rollback()
                                st.error(f"Error updating record: {e}")
                                cursor.close()
                    # Add similar blocks for other tables: Customers, Loans, Support Tickets, Transactions
            elif selected_value == "Customers":
                        # Implement update functionality for Customers table
                        cursor.execute("USE banksight;")

                        # Get full table (needed for cursor.description)
                        cursor.execute("SELECT * FROM customers")
                        rows = cursor.fetchall()
                        columns = [col[0] for col in cursor.description]

                        pk = columns[0]  # row[0] as PK

                        # Build record map
                        records = [dict(zip(columns, row)) for row in rows]
                        record_map = {r[pk]: r for r in records}

                        selected_pk = st.selectbox(pk, record_map.keys())
                        record = record_map[selected_pk]
                        editable_fields = [c for c in columns if c != pk]
                        field_to_update = st.selectbox("Select Column to update", editable_fields)
                        current_value = record[field_to_update]

                        with st.form("update_customer_form"):
                            if isinstance(current_value, (int, float)):
                                new_value = st.number_input(
                                    field_to_update,
                                    value=float(current_value)
                                )
                            else:
                                new_value = st.text_input(
                                    field_to_update,
                                    value=str(current_value)
                                )

                            submit = st.form_submit_button("Update")
                        if submit:
                            try:
                                cursor.execute(
                                    f"""
                                    UPDATE customers
                                    SET {field_to_update} = %s
                                    WHERE {pk} = %s
                                    """,
                                    (new_value, selected_pk)
                                )
                                db.commit()
                                st.success("Record updated successfully")
                            except Exception as e:
                                db.rollback()
                                st.error(f"Error updating record: {e}")
                                cursor.close()
            elif selected_value == "Loans":
                        # Implement update functionality for Loans table
                        cursor.execute("USE banksight;")

                        # Get full table (needed for cursor.description)
                        cursor.execute("SELECT * FROM loans")
                        rows = cursor.fetchall()
                        columns = [col[0] for col in cursor.description]

                        pk = columns[0]  # row[0] as PK

                        # Build record map
                        records = [dict(zip(columns, row)) for row in rows]
                        record_map = {r[pk]: r for r in records}

                        selected_pk = st.selectbox(pk, record_map.keys())
                        record = record_map[selected_pk]
                        editable_fields = [c for c in columns if c != pk]
                        field_to_update = st.selectbox("Select Column to update", editable_fields)
                        current_value = record[field_to_update]

                        with st.form("update_loan_form"):
                            if isinstance(current_value, (int, float)):
                                new_value = st.number_input(
                                    field_to_update,
                                    value=float(current_value)
                                )
                            else:
                                new_value = st.text_input(
                                    field_to_update,
                                    value=str(current_value)
                                )

                            submit = st.form_submit_button("Update")
                        if submit:
                            try:
                                cursor.execute(
                                    f"""
                                    UPDATE loans
                                    SET {field_to_update} = %s
                                    WHERE {pk} = %s
                                    """,
                                    (new_value, selected_pk)
                                )
                                db.commit()
                                st.success("Record updated successfully")
                            except Exception as e:
                                db.rollback()
                                st.error(f"Error updating record: {e}")
                                cursor.close()
            elif selected_value == "Support Tickets":
                        # Implement update functionality for Support Tickets table
                        cursor.execute("USE banksight;")

                        # Get full table (needed for cursor.description)
                        cursor.execute("SELECT * FROM support_tickets")
                        rows = cursor.fetchall()
                        columns = [col[0] for col in cursor.description]

                        pk = columns[0]  # row[0] as PK

                        # Build record map
                        records = [dict(zip(columns, row)) for row in rows]
                        record_map = {r[pk]: r for r in records}

                        selected_pk = st.selectbox(pk, record_map.keys())
                        record = record_map[selected_pk]
                        editable_fields = [c for c in columns if c != pk]
                        field_to_update = st.selectbox("Select Column to update", editable_fields)
                        current_value = record[field_to_update]

                        with st.form("update_support_ticket_form"):
                            if isinstance(current_value, (int, float)):
                                new_value = st.number_input(
                                    field_to_update,
                                    value=float(current_value)
                                )
                            else:
                                new_value = st.text_input(
                                    field_to_update,
                                    value=str(current_value)
                                )

                            submit = st.form_submit_button("Update")
                        if submit:
                            try:
                                cursor.execute(
                                    f"""
                                    UPDATE support_tickets
                                    SET {field_to_update} = %s
                                    WHERE {pk} = %s
                                    """,
                                    (new_value, selected_pk)
                                )
                                db.commit()
                                st.success("Record updated successfully")
                            except Exception as e:
                                db.rollback()
                                st.error(f"Error updating record: {e}")
                                cursor.close()
            elif selected_value == "Transactions":
                        # Implement update functionality for Transactions table
                        cursor.execute("USE banksight;")

                        # Get full table (needed for cursor.description)
                        cursor.execute("SELECT * FROM transactions")
                        rows = cursor.fetchall()
                        columns = [col[0] for col in cursor.description]

                        pk = columns[0]  # row[0] as PK

                        # Build record map
                        records = [dict(zip(columns, row)) for row in rows]
                        record_map = {r[pk]: r for r in records}

                        selected_pk = st.selectbox(pk, record_map.keys())
                        record = record_map[selected_pk]
                        editable_fields = [c for c in columns if c != pk]
                        field_to_update = st.selectbox("Select Column to update", editable_fields)
                        current_value = record[field_to_update]

                        with st.form("update_transaction_form"):
                            if isinstance(current_value, (int, float)):
                                new_value = st.number_input(
                                    field_to_update,
                                    value=float(current_value)
                                )
                            else:
                                new_value = st.text_input(
                                    field_to_update,
                                    value=str(current_value)
                                )

                            submit = st.form_submit_button("Update")
                        if submit:
                            try:
                                cursor.execute(
                                    f"""
                                    UPDATE transactions
                                    SET {field_to_update} = %s
                                    WHERE {pk} = %s
                                    """,
                                    (new_value, selected_pk)
                                )
                                db.commit()
                                st.success("Record updated successfully")
                            except Exception as e:
                                db.rollback()
                                st.error(f"Error updating record: {e}")
                                cursor.close()
            #End of Update Operation


        elif selected_operation == "Delete":
            st.write(f"Here you can delete records from the {selected_value} table.")
            if selected_value == "Accounts":
                cursor.execute("USE banksight;")

                # Get full table (needed for cursor.description)
                cursor.execute("SELECT * FROM accounts")
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]

                pk = columns[0]  # row[0] as PK

                # Build record map
                records = [dict(zip(columns, row)) for row in rows]
                record_map = {r[pk]: r for r in records}

                selected_pk = st.selectbox(pk, record_map.keys())

                if st.button("Delete"):
                    try:
                        cursor.execute(
                            f"""
                            DELETE FROM accounts
                            WHERE {pk} = %s
                            """,
                            (selected_pk,)
                        )
                        db.commit()
                        st.success("Record deleted successfully")
                    except Exception as e:
                        db.rollback()
                        st.error(f"Error deleting record: {e}")
                        cursor.close()
            # Add similar blocks for other tables: Branches, Credit Cards, Customers, Loans, Support Tickets, Transactions
            elif selected_value == "Branches":  
                cursor.execute("USE banksight;")

                # Get full table (needed for cursor.description)
                cursor.execute("SELECT * FROM branches")
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]

                pk = columns[0]  # row[0] as PK

                # Build record map
                records = [dict(zip(columns, row)) for row in rows]
                record_map = {r[pk]: r for r in records}

                selected_pk = st.selectbox(pk, record_map.keys())

                if st.button("Delete"):
                    try:
                        cursor.execute(
                            f"""
                            DELETE FROM branches
                            WHERE {pk} = %s
                            """,
                            (selected_pk,)
                        )
                        db.commit()
                        st.success("Record deleted successfully")
                    except Exception as e:
                        db.rollback()
                        st.error(f"Error deleting record: {e}")
                        cursor.close()
            elif selected_value == "Credit Cards":  
                cursor.execute("USE banksight;")

                # Get full table (needed for cursor.description)
                cursor.execute("SELECT * FROM credit_cards")
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]

                pk = columns[0]  # row[0] as PK

                # Build record map
                records = [dict(zip(columns, row)) for row in rows]
                record_map = {r[pk]: r for r in records}

                selected_pk = st.selectbox(pk, record_map.keys())

                if st.button("Delete"):
                    try:
                        cursor.execute(
                            f"""
                            DELETE FROM credit_cards
                            WHERE {pk} = %s
                            """,
                            (selected_pk,)
                        )
                        db.commit()
                        st.success("Record deleted successfully")
                    except Exception as e:
                        db.rollback()
                        st.error(f"Error deleting record: {e}")
                        cursor.close()
            elif selected_value == "Customers":  
                cursor.execute("USE banksight;")

                # Get full table (needed for cursor.description)
                cursor.execute("SELECT * FROM customers")
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]

                pk = columns[0]  # row[0] as PK

                # Build record map
                records = [dict(zip(columns, row)) for row in rows]
                record_map = {r[pk]: r for r in records}

                selected_pk = st.selectbox(pk, record_map.keys())

                if st.button("Delete"):
                    try:
                        cursor.execute(
                            f"""
                            DELETE FROM customers
                            WHERE {pk} = %s
                            """,
                            (selected_pk,)
                        )
                        db.commit()
                        st.success("Record deleted successfully")
                    except Exception as e:
                        db.rollback()
                        st.error(f"Error deleting record: {e}")
                        cursor.close()
            elif selected_value == "Loans":
                cursor.execute("USE banksight;")

                # Get full table (needed for cursor.description)
                cursor.execute("SELECT * FROM loans")
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]

                pk = columns[0]  # row[0] as PK

                # Build record map
                records = [dict(zip(columns, row)) for row in rows]
                record_map = {r[pk]: r for r in records}

                selected_pk = st.selectbox(pk, record_map.keys())

                if st.button("Delete"):
                    try:
                        cursor.execute(
                            f"""
                            DELETE FROM loans
                            WHERE {pk} = %s
                            """,
                            (selected_pk,)
                        )
                        db.commit()
                        st.success("Record deleted successfully")
                    except Exception as e:
                        db.rollback()
                        st.error(f"Error deleting record: {e}")
                        cursor.close()
            elif selected_value == "Support Tickets":  
                cursor.execute("USE banksight;")

                # Get full table (needed for cursor.description)
                cursor.execute("SELECT * FROM support_tickets")
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]

                pk = columns[0]  # row[0] as PK

                # Build record map
                records = [dict(zip(columns, row)) for row in rows]
                record_map = {r[pk]: r for r in records}

                selected_pk = st.selectbox(pk, record_map.keys())

                if st.button("Delete"):
                    try:
                        cursor.execute(
                            f"""
                            DELETE FROM support_tickets
                            WHERE {pk} = %s
                            """,
                            (selected_pk,)
                        )
                        db.commit()
                        st.success("Record deleted successfully")
                    except Exception as e:
                        db.rollback()
                        st.error(f"Error deleting record: {e}")
                        cursor.close()
            elif selected_value == "Transactions":  
                cursor.execute("USE banksight;")

                # Get full table (needed for cursor.description)
                cursor.execute("SELECT * FROM transactions")
                rows = cursor.fetchall()
                columns = [col[0] for col in cursor.description]

                pk = columns[0]  # row[0] as PK

                # Build record map
                records = [dict(zip(columns, row)) for row in rows]
                record_map = {r[pk]: r for r in records}

                selected_pk = st.selectbox(pk, record_map.keys())

                if st.button("Delete"):
                    try:
                        cursor.execute(
                            f"""
                            DELETE FROM transactions
                            WHERE {pk} = %s
                            """,
                            (selected_pk,)
                        )
                        db.commit()
                        st.success("Record deleted successfully")
                    except Exception as e:
                        db.rollback()
                        st.error(f"Error deleting record: {e}")
                        cursor.close()
                        st.stop()




elif selected_page == "Credit / Debit Simulation":
        st.title("Credit / Debit Simulation page.")
        customer_id = st.text_input("Enter Customer ID")
        amount = st.number_input("Enter Amount", min_value=0.0)
        transaction_type = st.radio("Select Transaction Type", ["Check Current Balance", "Deposit", "Withdraw"])
        if st.button("Submit"):
            if transaction_type == "Check Current Balance":
                try:
                    cursor.execute("USE banksight;")
                    query = "SELECT account_balance FROM accounts WHERE customer_id = %s"
                    cursor.execute(query, (customer_id,))
                    result = cursor.fetchone()
                    if result:              
                        balance = result[0]
                        st.success(f"Current Balance for Customer ID {customer_id}: ${balance:.2f}")
                    else:
                        st.error("Customer ID not found.")
                except Exception as e:
                    st.error(f"Error fetching balance: {e}")
                    cursor.close()
            elif transaction_type == "Deposit":
                try:
                    cursor.execute("USE banksight;")
                    query = "UPDATE accounts SET account_balance = account_balance + %s WHERE customer_id = %s"
                    cursor.execute(query, (amount, customer_id))
                    db.commit()
                    st.success(f"Successfully deposited ${amount:.2f} to Customer ID {customer_id}.")
                except Exception as e:
                    db.rollback()
                    st.error(f"Error depositing amount: {e}")
                    cursor.close()
            elif transaction_type == "Withdraw":
                try:
                    cursor.execute("USE banksight;")
                    query = "SELECT account_balance FROM accounts WHERE customer_id = %s"
                    cursor.execute(query, (customer_id,))
                    result = cursor.fetchone()
                    if result:
                        current_balance = result[0]
                        if current_balance >= amount:
                            update_query = "UPDATE accounts SET account_balance = account_balance - %s WHERE customer_id = %s"
                            cursor.execute(update_query, (amount, customer_id))
                            db.commit()
                            st.success(f"Successfully withdrew ${amount:.2f} from Customer ID {customer_id}.")
                        else:
                            st.error("Insufficient funds for withdrawal transaction.")
                    else:
                        st.error("Customer ID not found.")
                except Exception as e:
                    db.rollback()
                    st.error(f"Error withdrawing amount: {e}")
                    cursor.close()


elif selected_page == "Analytical Insights":
    st.title("Analytical Insights Dashboard")
    st.subheader("Key Performance Indicators (KPIs)")
    try:
        cursor.execute("USE banksight;")
        cursor.execute("SELECT COUNT(*) FROM customers;")
        total_customers = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM accounts;")
        total_accounts = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM loans;")
        total_loans = cursor.fetchone()[0]

        cursor.execute("SELECT AVG(account_balance) FROM accounts;")
        avg_account_balance = cursor.fetchone()[0]

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Customers", total_customers)
            st.metric("Total Accounts", total_accounts)
        with col2:
            st.metric("Total Loans", total_loans)
            st.metric("Avg. Account Balance", f"${avg_account_balance:,.2f}")
    except Exception as e:
        st.error(f"Error fetching KPIs: {e}")
        cursor.close()
        
         

elif selected_page == "About Creator":
    st.write("""Sri is a seasoned DevOps Engineer with strong expertise in cloud infrastructure, automation, and application support. With hands-on
              experience across Azure infrastructure, CI/CD pipelines, Linux/Windows systems,
              databases, and enterprise applications, Sri focuses on building scalable, reliable, and secure platforms.""")




