import platform
import socket

def get_system_info() -> dict:

    """
    Toma la información básica acerca de
    la máquina que se está usando

    :returns:
         dict: informacion del sistema.
    """

    return{
        "hostname": socket.gethostname(),
        "operating_system": platform.system(),
        "os_version": platform.release(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
    }