# 🪙 Real-Time Bitcoin Price & Volume Tracker 📊

This Python project fetches and visualizes real-time Bitcoin (BTC-USD) price and volume data using the `yfinance` API. It provides a clear visual representation of Bitcoin's 1-minute interval price trends and trading volumes, ideal for analysts, crypto enthusiasts, and developers exploring financial data visualization.

---

## 🔍 Features

- ✅ Fetches **real-time BTC-USD data** (1-minute interval) from Yahoo Finance
- ✅ Displays **current Bitcoin price** with timestamp
- ✅ Prints the latest **Open, High, Low, Close, Volume** data
- ✅ Generates:
  - 📈 Line chart of closing prices
  - 📊 Bar chart of trading volume
- ✅ Auto-cleans data (removes nulls, formats timestamps)
- ✅ Custom matplotlib x-axis formatting (HH:MM view)
- ✅ Ready to run in VS Code or terminal

---

## 🛠️ Technologies Used

- Python 3.7+
- `yfinance` – for fetching BTC-USD data
- `pandas` – for data manipulation
- `matplotlib` – for plotting
- `datetime` – for formatting timestamps
- `warnings` – for suppressing irrelevant warnings

---
Install dependencies
pip install -r requirements.txt
python bitcoin_tracker.py

real-time-bitcoin-tracker/
│
├── bitcoin_tracker.py     # Main Python script
├── README.md              # Project overview (this file)
├── requirements.txt       # Dependencies
├── .gitignore             # Files to ignore
└── LICENSE                # MIT License



📄 License
This project is licensed under the MIT License - free to use and modify.

🤝 Contributing
Contributions are welcome! Open an issue or submit a pull request with improvements or new features.

🙋‍♂️ Author
Akhilesh Yadav
📍 Data Science Student | Python Developer
📫 GitHub: @Akhilesh-yadav680

🌐 Useful Links
Yahoo Finance - https://finance.yahoo.com/quote/BTC-USD/

https://matplotlib.org/stable/index.html




