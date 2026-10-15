import psutil


def get_top_processes(limit: int = 5) -> list[dict]:
    """
    Return processes sorted by memory consumption.

    Args:
        limit: Maximum number of processes to return.

    Returns:
        list[dict]: Process information.
    """

    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "memory_percent", "status"]
    ):
        try:
            info = process.info

            processes.append({
                "pid": info["pid"],
                "name": info["name"] or "Unknown",
                "memory_percent": round(
                    info["memory_percent"] or 0.0, 2
                ),
                "status": info["status"],
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess,
        ):
            continue

    processes.sort(
        key=lambda process: process["memory_percent"],
        reverse=True,
    )

    return processes[:max(0, limit)]