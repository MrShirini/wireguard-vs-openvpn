#!/bin/bash

# Configurations
VPN_NAME="$1"                     # "WireGuard" or "OpenVPN"
VPN_SERVER_IP="$2"                # IP to connect via VPN (e.g., 10.8.0.1)
RUNS=5                            # Number of tests
OUTPUT_FILE="${VPN_NAME}_iperf_results.csv"

# Header
echo "Run,Throughput_Mbps,Retries" > "$OUTPUT_FILE"

echo "🔧 Running $RUNS tests for $VPN_NAME..."
echo "Target VPN IP: $VPN_SERVER_IP"
echo "Results saved to: $OUTPUT_FILE"

for i in $(seq 1 $RUNS); do
    echo "⏱️ Test #$i..."
    OUTPUT=$(iperf3 -c "$VPN_SERVER_IP" -J)  # JSON output

    if [ $? -ne 0 ]; then
        echo "$i,ERROR,ERROR" >> "$OUTPUT_FILE"
        echo "⚠️ Test $i failed."
        continue
    fi

    # Parse JSON
    THROUGHPUT=$(echo "$OUTPUT" | jq '.end.sum_sent.bits_per_second' | awk '{ printf "%.2f", $1 / 1000000 }')
    RETRIES=$(echo "$OUTPUT" | jq '.end.sum_sent.retransmits')

    echo "$i,$THROUGHPUT,$RETRIES" >> "$OUTPUT_FILE"
    sleep 2
done

echo "✅ All tests completed."
