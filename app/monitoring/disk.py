import psutil


def bytes_to_gb(value: int) -> float:
    """
    Convert bytes to gigabytes.
    """

    return round(value / (1024 ** 3), 2)


def get_disk_metrics() -> dict:
    """
    Get disk usage information.

    Returns:
        dict: Disk metrics.
    """

    disk = psutil.disk_usage("/")

    return {
        "total_gb": bytes_to_gb(disk.total),
        "used_gb": bytes_to_gb(disk.used),
        "free_gb": bytes_to_gb(disk.free),
        "usage_percent": disk.percent,
    }