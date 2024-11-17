
---

# Investment Calculators 💰📊

This project provides a set of financial calculators to help users make informed decisions regarding their investments. The calculators include SIP (Systematic Investment Plan), Step-up SIP, SWP (Systematic Withdrawal Plan), Goal-based SIP, and FD (Fixed Deposit) Calculators. It also provides options to download the results as an Excel file, and visualizes the data using pie charts for better understanding.

## Features 🌟

- **SIP Calculator**: Calculate the future value of an investment based on a fixed monthly investment. 📈
- **Step-up SIP Calculator**: Calculate SIP with an annual increase in investment amount. 🔼
- **SWP Calculator**: Calculate the monthly withdrawals from an invested amount, along with the remaining balance over time. 💸
- **Goal-based SIP Calculator**: Calculate the required monthly SIP to reach a predefined goal amount in a given time. 🎯
- **FD Calculator**: Calculate the maturity amount of a fixed deposit based on principal, interest rate, and time. 🏦

### Key Features ✨

1. **Interactive Inputs**: All calculators have dynamic inputs such as principal, rate of interest, time (in years), etc. 🔄
2. **Visualization**: Pie charts are generated to represent the distribution of the investment (e.g., Total Investment vs. Earnings). 🍰
3. **Downloadable Data**: The results are available for download in an Excel file format. 📥
4. **User-friendly**: The app is built with Streamlit for an easy-to-use interface that requires minimal effort from the user. 👩‍💻👨‍💻

---

## Requirements 🔧

1. Python 3.x
2. Required libraries:
   - `streamlit` (for creating the web interface)
   - `pandas` (for data handling and Excel file export)
   - `matplotlib` (for generating pie charts)

You can install these libraries using `pip`:
```bash
pip install streamlit pandas matplotlib openpyxl
```

---

## How to Run the Application 🚀

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/investment-calculators.git
    ```

2. Navigate to the project folder:
    ```bash
    cd investment-calculators
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run main.py
    ```

4. Open the provided URL in your browser to interact with the calculators. 🌐

---

## How to Use 🛠️

Once the app is running, follow these steps for each calculator:

1. **SIP Calculator**:  
   - Set the monthly investment amount, interest rate, and investment duration. 💸
   - Click on "Calculate SIP" to get the final maturity amount, earnings, and total investment. 🧮
   - View the data in a table and download it as an Excel file. 📑
   - See the result visualized in a pie chart (Total Investment vs. Earnings). 📊

2. **Step-up SIP Calculator**:  
   - Set the initial monthly SIP, the annual increment, interest rate, and investment duration. 🔼
   - Click on "Calculate Step-up SIP" to see the results. 🎯
   - View the detailed table and download the data as an Excel file. 📥
   - A pie chart will display the distribution of earnings and total investment. 🍰

3. **SWP Calculator**:  
   - Input your principal amount, interest rate, withdrawal amount, and time duration. 💵
   - Calculate the SWP and see the results in a pie chart (Principal vs Earnings). 🥧
   - Download the results as an Excel file, which contains the month-by-month remaining amount. 📑

4. **Goal-based SIP Calculator**:  
   - Input your goal amount, interest rate, and time period. 🎯
   - Calculate the required SIP amount per month. 📈
   - The pie chart will show the goal amount vs total SIP investment. 🍰

5. **FD Calculator**:  
   - Input your principal amount, interest rate, and duration. 🏦
   - The final maturity amount and earnings will be calculated. 📊
   - The pie chart will show the distribution between the principal and earnings. 🥧

---

## Example Output 📊

For each calculator, the app will display the following:

1. **Total Investment**: The sum of all the contributions made during the investment period. 💰
2. **Earnings**: The total earnings generated from the investment. 💸
3. **Final Maturity Amount**: The amount you would have at the end of the investment period. 💵
4. **Excel Download**: Option to download the data in an Excel sheet. 📥
5. **Pie Chart**: A visual representation of how much of the maturity amount comes from the total investment vs earnings. 🥧

---

## Contribution 🤝

Feel free to contribute by creating issues, submitting pull requests, or suggesting new features.

To contribute:
1. Fork the repository 🍴
2. Create a new branch (`git checkout -b feature-branch`) 🌱
3. Make your changes 🖊️
4. Commit your changes (`git commit -am 'Add new feature'`) 💬
5. Push to the branch (`git push origin feature-branch`) 🚀
6. Open a pull request 📥

---

## License 📝

This project is open-source and available under the [MIT License](LICENSE). 💡

---

## Contact 📧

If you have any questions, feel free to reach out at:
- Email: your.email@example.com 📩

---

