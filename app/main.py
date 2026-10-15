from app.monitoring.system import get_system_info
from app.monitoring.cpu import get_cpu_metrics
from app.monitoring.memory import get_memory_metrics
from app.monitoring.disk import get_disk_metrics
from app.monitoring.network import get_network_metrics
from app.monitoring.uptime import get_uptime_metrics
from app.monitoring.processes import get_top_processes


def collect_metrics() -> dict:
    """
    Collect all local system metrics.

    Returns:
        dict: Current system metrics.
    """

    return {
        "system": get_system_info(),
        "cpu": get_cpu_metrics(),
        "memory": get_memory_metrics(),
        "disk": get_disk_metrics(),
        "network": get_network_metrics(),
        "uptime": get_uptime_metrics(),
        "top_processes": get_top_processes(limit=5),
    }