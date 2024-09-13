import pandas as pd
import matplotlib.pyplot as plt

# Sample portfolio data
portfolio_data = {
    'Date': pd.date_range(start='2023-01-01', periods=5, freq='M'),
    'Portfolio_Value': [100000, 110000, 105000, 115000, 120000],
    'Risk_Level': [0.2, 0.25, 0.22, 0.18, 0.15]
}

df_portfolio = pd.DataFrame(portfolio_data)

def plot_portfolio_risk(df):
    """
    Plot portfolio value and risk level over time.
    """
    fig, ax1 = plt.subplots()

    # Plot Portfolio Value
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Portfolio Value', color='blue')
    ax1.plot(df['Date'], df['Portfolio_Value'], color='blue', label='Portfolio Value')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Create a second y-axis for risk level
    ax2 = ax1.twinx()
    ax2.set_ylabel('Risk Level', color='red')
    ax2.plot(df['Date'], df['Risk_Level'], color='red', label='Risk Level', linestyle='--')
    ax2.tick_params(axis='y', labelcolor='red')

    # Title and layout adjustments
    plt.title('Portfolio Risk Analysis')
    fig.tight_layout()

    plt.show()

# Run the risk analysis plot
plot_portfolio_risk(df_portfolio)
