import threading

import pytest
from openff.toolkit import Molecule, Quantity

from openff.packmol import pack_box


@pytest.fixture
def water():
    return Molecule.from_smiles("O")


@pytest.mark.filterwarnings("error::pytest.PytestUnhandledThreadExceptionWarning")
def test_thread_safety(water):
    """See https://github.com/openforcefield/openff-packmol/issues/10."""
    threads = []
    for i in range(3):
        t = threading.Thread(
            target=pack_box,
            args=(
                [water],
                [100 + i],
                None,
                Quantity(0.2, "nanometer"),
                None,
                Quantity(0.5, "g/mL"),
            ),
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
