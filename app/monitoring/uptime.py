import time
import psutil


def get_uptime_metrics() -> dict:
    """
    Calculate the time elapsed since system boot.

    Returns:
        dict: System uptime.
    """

    boot_time = psutil.boot_time()
    uptime_seconds = int(time.time() - boot_time)

    days, remainder = divmod(uptime_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    return {
        "uptime_seconds": uptime_seconds,
        "uptime_formatted": (
            f"{days}d {hours}h {minutes}m {seconds}s"
        ),
    }