import matplotlib.pyplot as plt

# Handshake times in seconds (from user-provided benchmark)
wireguard_times = [0.127, 0.110, 0.119, 0.111, 0.112]
openvpn_times = [0.036, 0.039, 0.033, 0.033, 0.032]

# Calculate average handshake times
avg_wireguard = sum(wireguard_times) / len(wireguard_times)
avg_openvpn = sum(openvpn_times) / len(openvpn_times)

# Prepare bar chart
protocols = ['WireGuard', 'OpenVPN']
avg_times = [avg_wireguard, avg_openvpn]

plt.figure(figsize=(6, 4))
plt.bar(protocols, avg_times)
plt.ylabel('Average Handshake Time (seconds)')
plt.title('VPN Handshake Time Comparison')
plt.grid(axis='y')
plt.tight_layout()

# Save the figure
chart_path = "results/handshake_time_comparison.png"
plt.savefig(chart_path)


