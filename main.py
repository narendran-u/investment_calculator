import streamlit as st
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt

# Format currency
def format_currency(value):
    return f"₹{round(value):,}"

# SIP Calculator
def sip_calculator():
    st.header("SIP Calculator")
    principal = st.slider("Monthly Investment (₹)", min_value=500, max_value=50000, value=1000, step=500)
    rate = st.slider("Annual Rate of Interest (%)", min_value=1.0, max_value=15.0, value=6.0, step=0.1)
    time = st.slider("Investment Period (years)", min_value=1, max_value=30, value=10, step=1)

    if st.button("Calculate SIP"):
        months = time * 12
        monthly_rate = rate / 12 / 100
        amount = principal * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)
        amount = round(amount)
        
        total_investment = principal * months
        earnings = amount - total_investment
        
        st.write(f"### Results:")
        st.write(f"Total Investment: {format_currency(total_investment)}")
        st.write(f"Earnings: {format_currency(earnings)}")
        st.write(f"Final Maturity Amount: {format_currency(amount)}")

        labels = ['Total Investment', 'Earnings']
        sizes = [total_investment, earnings]
        colors = ['#4CAF50', '#FFC107']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.axis('equal')
        st.pyplot(fig)

        df = pd.DataFrame({"Month": range(1, months + 1), "Remaining Amount": [amount] * months})
        st.dataframe(df)

        excel_buffer = BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='SIP Data')

        excel_buffer.seek(0)
        st.download_button(
            label="Download SIP Data as Excel",
            data=excel_buffer,
            file_name="sip_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# Step-up SIP Calculator
def stepup_sip_calculator():
    st.header("Step-up SIP Calculator")
    principal = st.slider("Initial Monthly Investment (₹)", min_value=500, max_value=50000, value=1000, step=500)
    increment = st.slider("Annual Increment (₹)", min_value=0, max_value=10000, value=500, step=100)
    rate = st.slider("Annual Rate of Interest (%)", min_value=1.0, max_value=15.0, value=6.0, step=0.1)
    time = st.slider("Investment Period (years)", min_value=1, max_value=30, value=10, step=1)

    if st.button("Calculate Step-up SIP"):
        months = time * 12
        monthly_rate = rate / 12 / 100
        total_investment = 0
        total_amount = 0

        for i in range(time):
            yearly_investment = principal + (increment * i)
            yearly_amount = yearly_investment * (((1 + monthly_rate) ** 12 - 1) / monthly_rate) * (1 + monthly_rate)
            total_investment += yearly_investment * 12
            total_amount += yearly_amount

        total_amount = round(total_amount)
        earnings = total_amount - total_investment

        st.write(f"### Results:")
        st.write(f"Total Investment: {format_currency(total_investment)}")
        st.write(f"Earnings: {format_currency(earnings)}")
        st.write(f"Final Maturity Amount: {format_currency(total_amount)}")

        labels = ['Total Investment', 'Earnings']
        sizes = [total_investment, earnings]
        colors = ['#2196F3', '#FF5722']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.axis('equal')
        st.pyplot(fig)

        df = pd.DataFrame({"Year": range(1, time + 1), "Investment": [total_investment] * time, "Amount": [total_amount] * time})
        st.dataframe(df)

        excel_buffer = BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Step-up SIP Data')

        excel_buffer.seek(0)
        st.download_button(
            label="Download Step-up SIP Data as Excel",
            data=excel_buffer,
            file_name="stepup_sip_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# SWP Calculator
def swp_calculator():
    st.header("SWP Calculator")
    principal = st.slider("Principal Amount (₹)", min_value=10000, max_value=5000000, value=100000, step=5000)
    rate = st.slider("Annual Rate of Interest (%)", min_value=1.0, max_value=15.0, value=6.0, step=0.1)
    time = st.slider("Investment Period (years)", min_value=1, max_value=30, value=5, step=1)
    monthly_withdrawal = st.slider("Monthly Withdrawal Amount (₹)", min_value=500, max_value=50000, value=5000, step=500)

    if st.button("Calculate SWP"):
        months = time * 12
        monthly_rate = rate / 12 / 100
        maturity_amount = principal * (1 + monthly_rate) ** months
        maturity_amount = round(maturity_amount)

        remaining_amount = maturity_amount
        withdrawals = []
        for month in range(1, months + 1):
            if remaining_amount > 0:
                remaining_amount -= monthly_withdrawal
            else:
                remaining_amount = 0
            withdrawals.append([month, remaining_amount])

        st.write(f"### Results:")
        st.write(f"Principal Amount: {format_currency(principal)}")
        st.write(f"Final Maturity Amount: {format_currency(maturity_amount)}")

        earnings = maturity_amount - principal
        labels = ['Principal Amount', 'Earnings']
        sizes = [principal, earnings]
        colors = ['#FF5722', '#4CAF50']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.axis('equal')
        st.pyplot(fig)

        withdrawal_df = pd.DataFrame(withdrawals, columns=["Month", "Remaining Amount"])
        st.write("### Remaining Amount after each Withdrawal")
        st.dataframe(withdrawal_df)

        excel_buffer = BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
            withdrawal_df.to_excel(writer, index=False, sheet_name='SWP Data')

        excel_buffer.seek(0)
        st.download_button(
            label="Download SWP Data as Excel",
            data=excel_buffer,
            file_name="swp_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

# Goal-based SIP Calculator
def goal_based_sip_calculator():
    st.header("Goal-based SIP Calculator")
    goal_amount = st.slider("Goal Amount (₹)", min_value=10000, max_value=10000000, value=500000, step=5000)
    rate = st.slider("Annual Rate of Interest (%)", min_value=1.0, max_value=15.0, value=6.0, step=0.1)
    time = st.slider("Investment Period (years)", min_value=1, max_value=30, value=10, step=1)

    if st.button("Calculate Goal-based SIP"):
        months = time * 12
        monthly_rate = rate / 12 / 100
        required_sip = goal_amount / (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)
        required_sip = round(required_sip)

        st.write(f"### Results:")
        st.write(f"Required SIP per Month: {format_currency(required_sip)}")
        
        labels = ['Goal Amount', 'SIP Investment']
        sizes = [goal_amount, required_sip * months]
        colors = ['#8BC34A', '#FF9800']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.axis('equal')
        st.pyplot(fig)

# Fixed Deposit Calculator
def fd_calculator():
    st.header("FD Calculator")
    principal = st.slider("Principal Amount (₹)", min_value=10000, max_value=5000000, value=100000, step=5000)
    rate = st.slider("Annual Rate of Interest (%)", min_value=1.0, max_value=15.0, value=6.0, step=0.1)
    time = st.slider("Investment Period (years)", min_value=1, max_value=30, value=5, step=1)

    if st.button("Calculate FD"):
        maturity_amount = principal * (1 + rate / 100) ** time
        maturity_amount = round(maturity_amount)
        
        earnings = maturity_amount - principal

        st.write(f"### Results:")
        st.write(f"Principal Amount: {format_currency(principal)}")
        st.write(f"Final Maturity Amount: {format_currency(maturity_amount)}")
        st.write(f"Earnings: {format_currency(earnings)}")

        labels = ['Principal Amount', 'Earnings']
        sizes = [principal, earnings]
        colors = ['#FF5722', '#4CAF50']

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.axis('equal')
        st.pyplot(fig)

# Main function for Streamlit
def main():
    st.sidebar.title("Investment Calculators")
    choice = st.sidebar.radio("Select Calculator", ["SIP Calculator", "Step-up SIP Calculator", "SWP Calculator", "Goal-based SIP Calculator", "FD Calculator"])

    if choice == "SIP Calculator":
        sip_calculator()
    elif choice == "Step-up SIP Calculator":
        stepup_sip_calculator()
    elif choice == "SWP Calculator":
        swp_calculator()
    elif choice == "Goal-based SIP Calculator":
        goal_based_sip_calculator()
    elif choice == "FD Calculator":
        fd_calculator()

if __name__ == "__main__":
    main()
