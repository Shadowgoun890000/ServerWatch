import psutil


def get_cpu_metrics() -> dict:
    """
    Get current CPU usage information.

    Returns:
        dict: CPU metrics.
    """

    frequency = psutil.cpu_freq()

    return {
        "usage_percent": psutil.cpu_percent(interval=1),
        "physical_cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(logical=True),
        "frequency_mhz": (
            round(frequency.current, 2)
            if frequency
            else None
        ),
    }