import pytest
from openff.toolkit import Molecule, Quantity

from openff.packmol._tests import MoleculeWithConformer, _rng


@pytest.fixture(autouse=True)
def _initdir(tmpdir):
    tmpdir.chdir()


@pytest.fixture(scope="session")
def water() -> Molecule:
    return MoleculeWithConformer.from_mapped_smiles("[H:2][O:1][H:3]")


@pytest.fixture
def caffeine():
    return MoleculeWithConformer.from_smiles("Cn1cnc2c1c(=O)n(C)c(=O)n2C")


@pytest.fixture
def ethanol_with_conformer(ethanol):
    ethanol.add_conformer(
        Quantity(
            _rng.random((ethanol.n_atoms, 3)),
            "angstrom",
        ),
    )
    return ethanol


@pytest.fixture
def aspirin() -> Molecule:
    return MoleculeWithConformer.from_smiles("CC(=O)Oc1ccccc1C(=O)O")


@pytest.fixture
def ethanol() -> Molecule:
    ethanol = Molecule()

    ethanol.add_atom(6, 0, False)
    ethanol.add_atom(6, 0, False)
    ethanol.add_atom(8, 0, False)
    ethanol.add_atom(1, 0, False)
    ethanol.add_atom(1, 0, False)
    ethanol.add_atom(1, 0, False)
    ethanol.add_atom(1, 0, False)
    ethanol.add_atom(1, 0, False)
    ethanol.add_atom(1, 0, False)
    ethanol.add_bond(0, 1, 1, False, fractional_bond_order=1.33)
    ethanol.add_bond(1, 2, 1, False, fractional_bond_order=1.23)
    ethanol.add_bond(0, 3, 1, False, fractional_bond_order=1)
    ethanol.add_bond(0, 4, 1, False, fractional_bond_order=1)
    ethanol.add_bond(0, 5, 1, False, fractional_bond_order=1)
    ethanol.add_bond(1, 6, 1, False, fractional_bond_order=1)
    ethanol.add_bond(1, 7, 1, False, fractional_bond_order=1)
    ethanol.add_bond(2, 8, 1, False, fractional_bond_order=1)

    ethanol.partial_charges = Quantity(
        [-0.4, -0.3, -0.2, -0.1, 0.00001, 0.1, 0.2, 0.3, 0.4],
        "elementary_charge",
    )

    return ethanol
