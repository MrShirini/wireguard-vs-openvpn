import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set visual style
sns.set(style="whitegrid")

# Load data
wireguard_df = pd.read_csv("results/WireGuard_iperf_results.csv")
openvpn_df = pd.read_csv("results/OpenVPN_iperf_results.csv")

# Label VPN type
wireguard_df['VPN'] = 'WireGuard'
openvpn_df['VPN'] = 'OpenVPN'

# Combine data
combined_df = pd.concat([wireguard_df, openvpn_df], ignore_index=True)

# Plot 1: Throughput Comparison
plt.figure(figsize=(10, 6))
sns.boxplot(x="VPN", y="Throughput_Mbps", hue="VPN", data=combined_df, palette="Set2", dodge=False, legend=False)
plt.title("Throughput Comparison between WireGuard and OpenVPN")
plt.ylabel("Throughput (Mbps)")
plt.xlabel("VPN Protocol")
plt.tight_layout()
plt.savefig("throughput_comparison.png")  # Save figure instead of showing

# Plot 2: Retransmission Comparison
plt.figure(figsize=(10, 6))
sns.boxplot(x="VPN", y="Retries", hue="VPN", data=combined_df, palette="Set1", dodge=False, legend=False)
plt.title("Retransmissions Comparison between WireGuard and OpenVPN")
plt.ylabel("Number of Retransmissions")
plt.xlabel("VPN Protocol")
plt.tight_layout()
plt.savefig("retransmission_comparison.png")  # Save figure instead of showing
