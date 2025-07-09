#!/bin/bash

# === CONFIGURATION ===
WIREGUARD_INTERFACE="wg0"
OPENVPN_CONFIG="/etc/openvpn/client.conf"
NUM_RUNS=5

# === OUTPUT FILES ===
WG_LOG="wireguard_handshake_times.txt"
OVPN_LOG="openvpn_handshake_times.txt"

# === FUNCTIONS ===

test_wireguard() {
    echo "Measuring WireGuard handshake..."
    > "$WG_LOG"
    for i in $(seq 1 $NUM_RUNS); do
        echo -n "Run $i: "
        { time sudo wg-quick up $WIREGUARD_INTERFACE; } 2>&1 | grep real | tee -a "$WG_LOG"
        sudo wg-quick down $WIREGUARD_INTERFACE > /dev/null
        sleep 1
    done
}
sudo openvpn --config amir.ovpn

test_openvpn() {
    echo "Measuring OpenVPN handshake..."
    > "$OVPN_LOG"
    for i in $(seq 1 $NUM_RUNS); do
        echo -n "Run $i: "
        { time sudo openvpn --config $OPENVPN_CONFIG --daemon --writepid ovpn.pid; } 2>&1 | grep real | tee -a "$OVPN_LOG"
        sleep 3
        sudo kill $(cat ovpn.pid) 2>/dev/null
        sleep 1
    done
}

calculate_stats() {
    echo -e "\n=== Results Summary ==="

    echo -e "\nWireGuard:"
    awk '{print $2}' "$WG_LOG" | sed 's/m.*s//' | awk -F. '{print $1*60 + $2"."$3}' | \
        awk '{sum+=$1; if(min=="" || $1<min) min=$1; if($1>max) max=$1} END {printf("Avg: %.3fs\nMin: %.3fs\nMax: %.3fs\n", sum/NR, min, max)}'

    echo -e "\nOpenVPN:"
    awk '{print $2}' "$OVPN_LOG" | sed 's/m.*s//' | awk -F. '{print $1*60 + $2"."$3}' | \
        awk '{sum+=$1; if(min=="" || $1<min) min=$1; if($1>max) max=$1} END {printf("Avg: %.3fs\nMin: %.3fs\nMax: %.3fs\n", sum/NR, min, max)}'
}

# === EXECUTION ===

test_wireguard
test_openvpn
calculate_stats
