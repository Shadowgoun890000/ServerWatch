import pytest

from app.monitoring.cpu import get_cpu_metrics
from app.monitoring.memory import get_memory_metrics
from app.monitoring.disk import get_disk_metrics
from app.monitoring.network import get_network_metrics
from app.monitoring.system import get_system_info
from app.monitoring.uptime import get_uptime_metrics
from app.monitoring.processes import get_top_processes


def test_cpu_metrics():
    metrics = get_cpu_metrics()

    assert 0 <= metrics["usage_percent"] <= 100
    assert metrics["logical_cores"] >= 1
    assert metrics["physical_cores"] is None or (
        metrics["physical_cores"] >= 1
    )


def test_memory_metrics():
    metrics = get_memory_metrics()

    assert metrics["total_gb"] > 0
    assert metrics["used_gb"] >= 0
    assert metrics["available_gb"] >= 0
    assert 0 <= metrics["usage_percent"] <= 100


def test_disk_metrics():
    metrics = get_disk_metrics()

    assert metrics["total_gb"] > 0
    assert metrics["used_gb"] >= 0
    assert metrics["free_gb"] >= 0
    assert 0 <= metrics["usage_percent"] <= 100


def test_network_metrics():
    metrics = get_network_metrics()

    assert metrics["bytes_sent_mb"] >= 0
    assert metrics["bytes_received_mb"] >= 0
    assert metrics["packets_sent"] >= 0
    assert metrics["packets_received"] >= 0


def test_system_info():
    metrics = get_system_info()

    assert metrics["hostname"]
    assert metrics["operating_system"]
    assert metrics["architecture"]
    assert metrics["python_version"]


def test_uptime_metrics():
    metrics = get_uptime_metrics()

    assert metrics["uptime_seconds"] >= 0
    assert metrics["uptime_formatted"]


def test_top_processes():
    processes = get_top_processes(limit=5)

    assert isinstance(processes, list)
    assert len(processes) <= 5

    memory_values = [
        process["memory_percent"]
        for process in processes
    ]

    assert memory_values == sorted(
        memory_values,
        reverse=True,
    )


def test_top_processes_limit_zero():
    processes = get_top_processes(limit=0)

    assert processes == []