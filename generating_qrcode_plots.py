import qrcode
import matplotlib.pyplot as plt

# Updated performance data
bandwidth_values = [143.62, 236.17]  # OpenVPN, WireGuard
retransmission_values = [178.8, 139.2]  # OpenVPN, WireGuard

# Create QR code
qr = qrcode.make("https://github.com/MrShirini/wireguard-vs-openvpn")
qr_path = "github_qr_code.png"
qr.save(qr_path)

# Bandwidth comparison plot
fig1, ax1 = plt.subplots()
ax1.bar(["OpenVPN", "WireGuard"], bandwidth_values, color=["blue", "green"])
ax1.set_ylabel("Avg Bandwidth (Mbps)")
ax1.set_title("Average Bandwidth Comparison")
plt.tight_layout()
bw_plot_path = "results/bandwidth_comparison.png"
plt.savefig(bw_plot_path)
plt.close()

# Retransmissions comparison plot
fig2, ax2 = plt.subplots()
ax2.bar(["OpenVPN", "WireGuard"], retransmission_values, color=["blue", "green"])
ax2.set_ylabel("Avg Retransmissions")
ax2.set_title("Average Retransmissions Comparison")
plt.tight_layout()
rtx_plot_path = "results/retransmissions_comparison.png"
plt.savefig(rtx_plot_path)
plt.close()

