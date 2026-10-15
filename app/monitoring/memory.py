import psutil


def bytes_to_gb(value: int) -> float:
    """
    Convert bytes to gigabytes.
    """

    return round(value / (1024 ** 3), 2)


def get_memory_metrics() -> dict:
    """
    Get current RAM usage information.

    Returns:
        dict: Memory metrics.
    """

    memory = psutil.virtual_memory()

    return {
        "total_gb": bytes_to_gb(memory.total),
        "used_gb": bytes_to_gb(memory.used),
        "available_gb": bytes_to_gb(memory.available),
        "usage_percent": memory.percent,
    }