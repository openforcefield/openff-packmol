from importlib.metadata import version

from openff.packmol._packmol import pack_box, solvate_topology, solvate_topology_nonwater
from openff.packmol.exceptions import PACKMOLRuntimeError, PACKMOLValueError

__all__ = (
    "PACKMOLRuntimeError",
    "PACKMOLValueError",
    "pack_box",
    "solvate_topology",
    "solvate_topology_nonwater",
)

__version__ = version("openff.packmol")
