# v91: amplitude gluing and factorization

`rzk/119-amplitude-gluing-factorization.rzk.md` introduces the multiplicative
structure required of supported-residue amplitudes. A glued physical filling is
evaluated through its global Gysin class and residue, while the factorized side
multiplies the two component residues. The factorization theorem is derived
from an explicit geometric/Gysin/residue factorization witness.

The module also formulates unit normalization, binary disjoint factorization,
associative three-filling coherence, and reflection compatibility. These are
properties of an amplitude candidate rather than silently assumed ring laws.

A fresh Rzk check passes all 10 declarations. The symbol closure contains one
file and no `#assume` declarations.

Concrete closure now requires a physical gluing operation together with the
multiplicativity of its supported Gysin and oriented residue maps.
