from app.monitoring.system import get_system_info
from app.monitoring.cpu import get_cpu_metrics
from app.monitoring.memory import get_memory_metrics
from app.monitoring.disk import get_disk_metrics


def collect_metrics() -> dict:
    """
    Collect all system metrics.

    Returns:
        dict: Current system metrics.
    """

    return {
        "system": get_system_info(),
        "cpu": get_cpu_metrics(),
        "memory": get_memory_metrics(),
        "disk": get_disk_metrics(),
    }