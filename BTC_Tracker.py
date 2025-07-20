import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import datetime
import matplotlib.dates as mdates
import warnings

# Suppress warnings like the auto_adjust notice
warnings.simplefilter("ignore")

# ✅ Download real-time Bitcoin data (1-minute interval for today)
btc_data = yf.download('BTC-USD', period='1d', interval='1m')

# ✅ Flatten multi-index columns (important for yfinance)
btc_data.columns = btc_data.columns.get_level_values(0)

# ✅ Clean data
btc_data.dropna(inplace=True)  # Remove missing rows
btc_data['Volume'] = pd.to_numeric(btc_data['Volume'], errors='coerce')  # Ensure Volume is numeric
btc_data.dropna(subset=['Volume'], inplace=True)  # Remove rows with NaN Volume

# ✅ Show current timestamp and latest price
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
latest_price = btc_data['Close'].iloc[-1]
print(f"\n📈 Real-Time Bitcoin Data as of {now}")
print(f"🟢 Current BTC Price (USD): ${latest_price:,.2f}\n")

# ✅ Display last 5 rows
print(btc_data[['Open', 'High', 'Low', 'Close', 'Volume']].tail())

# ✅ Convert datetime index to matplotlib numeric date format
btc_data['DateTimeNum'] = mdates.date2num(btc_data.index)

# ✅ Create subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# 📉 Price Line Chart
axs[0].plot(btc_data.index, btc_data['Close'], label='BTC Close Price', color='dodgerblue')
axs[0].set_title('Bitcoin Price (1-Minute Interval)', fontsize=14)
axs[0].set_ylabel('Price (USD)')
axs[0].grid(True)
axs[0].legend()

# 📊 Volume Bar Chart
bar_width = 1 / (24 * 60)  # 1 minute in days
axs[1].bar(btc_data['DateTimeNum'].values, btc_data['Volume'].values,
           width=bar_width, color='orange', label='BTC Volume')
axs[1].set_title('Bitcoin Volume', fontsize=14)
axs[1].set_ylabel('Volume')
axs[1].set_xlabel('Time (HH:MM)')
axs[1].grid(True)
axs[1].legend()

# ✅ Format x-axis to show time
axs[1].xaxis_date()
axs[1].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
axs[1].xaxis.set_major_locator(mdates.MinuteLocator(interval=15))  # tick every 15 min
plt.xticks(rotation=45)
plt.tight_layout()

# ✅ Show plot
plt.show()
