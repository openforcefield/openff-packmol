import numpy
from openff.toolkit import Molecule

_rng = numpy.random.default_rng(seed=700402014834)


class MoleculeWithConformer(Molecule):
    """Thin wrapper around `Molecule` to produce an instance with a conformer in one call."""

    @classmethod
    def from_smiles(self, smiles, name="", *args, **kwargs):
        """Create from smiles and generate a single conformer."""
        molecule = super().from_smiles(smiles, *args, **kwargs)
        molecule.generate_conformers(n_conformers=1)
        molecule.name = name

        return molecule

    @classmethod
    def from_mapped_smiles(self, smiles, name="", **kwargs):
        """Create from smiles and generate a single conformer."""
        molecule = super().from_mapped_smiles(smiles, **kwargs)
        molecule.generate_conformers(n_conformers=1)
        molecule.name = name

        return molecule
