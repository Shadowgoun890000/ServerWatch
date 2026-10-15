import psutil


def bytes_to_mb(value: int) -> float:
    """Convert bytes to megabytes."""
    return round(value / (1024 ** 2), 2)


def get_network_metrics() -> dict:
    """
    Collect network traffic counters.

    Returns:
        dict: Network statistics.
    """

    network = psutil.net_io_counters()

    return {
        "bytes_sent_mb": bytes_to_mb(network.bytes_sent),
        "bytes_received_mb": bytes_to_mb(network.bytes_recv),
        "packets_sent": network.packets_sent,
        "packets_received": network.packets_recv,
        "errors_in": network.errin,
        "errors_out": network.errout,
        "dropped_in": network.dropin,
        "dropped_out": network.dropout,
    }