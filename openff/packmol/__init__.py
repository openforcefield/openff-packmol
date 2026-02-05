from importlib.metadata import version

from openff.packmol._packmol import (
    RHOMBIC_DODECAHEDRON,
    RHOMBIC_DODECAHEDRON_XYHEX,
    UNIT_CUBE,
    pack_box,
    solvate_topology,
    solvate_topology_nonwater,
)
from openff.packmol.exceptions import PACKMOLRuntimeError, PACKMOLValueError

__all__ = (
    "RHOMBIC_DODECAHEDRON",
    "RHOMBIC_DODECAHEDRON_XYHEX",
    "UNIT_CUBE",
    "PACKMOLRuntimeError",
    "PACKMOLValueError",
    "pack_box",
    "solvate_topology",
    "solvate_topology_nonwater",
)

__version__ = version("openff.packmol")
