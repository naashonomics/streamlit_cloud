import os,calendar  # Core Python Module
from datetime import datetime  # Core Python Module
import plotly.graph_objects as go  # pip install plotly
import streamlit as st  # pip install streamlit
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu
import pages.database as db  # local import
from deta import Deta  # pip install deta
from dotenv import load_dotenv



# -------------- SETTINGS --------------
incomes = ["Base_Salary", "Udemy", "Dividends","Rents","ESPP","RSU"]
expenses = ["Rent", "Utilities", "Groceries", "Transport", "Food", "cash_saving","retirement_401K","SIP","stocks"]
currency = "USD"
page_title = "Income and Expense Tracker"
page_icon = ":dollar:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---
years = [datetime.today().year-1, datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])


# --- DATABASE INTERFACE ---
def get_all_periods():
    items = db.fetch_all_periods()
    periods = [item["key"] for item in items]
    return periods

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Data Entry", "Data Visualization"],
    icons=["text-center", "bar-chart-steps"],  # https://icons.getbootstrap.com/
    orientation="horizontal",
)


# --- INPUT & SAVE PERIODS ---
if selected == "Data Entry":
    st.header(f"Data Entry in {currency}")
    with st.form("entry_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        col1.selectbox("Select Month:", months, key="month")
        col2.selectbox("Select Year:", years, key="year")

        "---"
        with st.expander("Income"):
            for income in incomes:
                st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)
        with st.expander("Expenses"):
            for expense in expenses:
                st.number_input(f"{expense}:", min_value=0, format="%i", step=10, key=expense)
        with st.expander("Comment"):
            comment = st.text_area("", placeholder="Enter a comment here ...")

        "---"
        submitted = st.form_submit_button("Save Data")
        if submitted:
            period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
            incomes = {income: st.session_state[income] for income in incomes}
            expenses = {expense: st.session_state[expense] for expense in expenses}
            db.insert_period(period, incomes, expenses, comment)
            #st.write(f"incomes: {incomes}")
            #st.write(f"expenses: {expenses}")
            st.success("Data saved!")


# --- PLOT PERIODS ---
if selected == "Data Visualization":
    st.header("Data Visualization")
    with st.form("saved_periods"):
        period = st.selectbox("Select Period:", get_all_periods())
        #period = st.selectbox("Select Period:" ,["2022_July"])
        submitted = st.form_submit_button("Plot Period")
        if submitted:
            # Get data from database
            period_data = db.get_period(period)
            comment = period_data.get("comment")
            expenses = period_data.get("expenses")
            incomes = period_data.get("incomes")
            #comment = "Testing"
            #incomes= {'Base_Salary': 7000, 'Udemy': 0, 'Dividends': 2000, 'Rents': 3000, 'ESPP': 1200, 'RSU': 0}
            #expenses= {'Rent': 1500, 'Utilities': 200, 'Groceries': 100, 'Transport': 90, 'Food': 350, 'cash_saving': 3000, 'retirement_401K': 3000, 'SIP': 1000, 'stocks': 0} 
            # Create metrics
            total_income = sum(incomes.values())
            total_expense = sum(expenses.values())
            remaining_budget = total_income - total_expense
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Income", f"{total_income} {currency}")
            col2.metric("Total Expense", f"{total_expense} {currency}")
            col3.metric("Remaining Budget", f"{remaining_budget} {currency}")
            st.text(f"Comment: {comment}")

            # Create sankey chart
            label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
            source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
            target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses.keys()]
            value = list(incomes.values()) + list(expenses.values())

            # Data to dict, dict to sankey
            link = dict(source=source, target=target, value=value)
            node = dict(label=label, pad=20, thickness=30, color="#F4C430")
            data = go.Sankey(link=link, node=node)

            # Plot it!
            fig = go.Figure(data)
            fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
            st.plotly_chart(fig, use_container_width=True)
