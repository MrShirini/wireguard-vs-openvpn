import pandas as pd

# Load the CSV files
wireguard_df = pd.read_csv("results/WireGuard_iperf_results.csv")
openvpn_df = pd.read_csv("results/OpenVPN_iperf_results.csv")

# Calculate summary statistics
wireguard_stats = wireguard_df.describe()
openvpn_stats = openvpn_df.describe()

# Add a column to distinguish VPN type
wireguard_df["VPN"] = "WireGuard"
openvpn_df["VPN"] = "OpenVPN"

# Combine for group analysis
combined_df = pd.concat([wireguard_df, openvpn_df], ignore_index=True)

# Calculate means for each VPN
means = combined_df.groupby("VPN").mean(numeric_only=True)
print(means)
