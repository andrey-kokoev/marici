# Inspection of Cook FCC nuclear-lattice sources

## Sources actually accessed

- N. D. Cook, *The Inherent Geometry of the Nuclear Hamiltonian* (2011),
  https://arxiv.org/abs/1101.4251 . Full PDF downloaded and text inspected.
- N. D. Cook, *Quantum Nucleodynamics* (2013),
  https://arxiv.org/abs/1310.3338 . Full PDF downloaded and text searched.
- V. Dallacasa and N. D. Cook, *The FCC nuclear model. I. Equivalence between
  the FCC lattice and nucleon eigenstates and the correspondence with the
  spin-orbit model*, Il Nuovo Cimento A 97, 157–183 (1987),
  https://doi.org/10.1007/BF02733846 . Publisher abstract inspected; full text
  not obtained. Its abstract explicitly describes an antiferromagnetic FCC
  lattice with alternating isospin layers.
- The 2010 book metadata was confirmed through Crossref:
  https://doi.org/10.1007/978-3-642-14737-1 . Full book not obtained.

## What the accessible primary source specifies

Cook (2011), p. 3, equations (2)–(7), maps lattice coordinates to quantum
labels. In particular:

    n = (|x|+|y|+|z|-3)/2
    j = (|x|+|y|-1)/2
    m = s |x|
    s = (-1)^((x-1)/2)/2
    i = (-1)^((z-1)/2)
    parity = sign(x*y*z)

These are the author's conventions, including his isospin normalization.
No inverse-map implementation or coordinate reconstruction has been verified
here. Do not silently mix the author's conventions with different normalizations.

The author describes n-shells, j-subshells and m-subshells as having spherical,
cylindrical and conical symmetries respectively, with spin and isospin layering
along orthogonal axes (pp. 3–5). The n equation describes L1-distance shells
in these Cartesian coordinates; it is not a constant Euclidean-radius equation.
The lattice is built around a central tetrahedron (p. 4).

Figure 1 explicitly discusses calcium-40. Figure 2 uses a 14-nucleon example
labelled beryllium-14, for geometric illustration rather than stability.
Figure 3 discusses alpha-cluster organization and the closed structures with
4, 16 and 40 nucleons (pp. 6–7).

The caption to Table 1 explicitly says that the j-subshell sequence within
n-shells varies nucleus by nucleus through configuration mixing. Thus the
paper does not specify a universal fixed geometric-layer filling sequence
from H-1 through Pb-208.

## Pb-208 status after inspection

Neither accessible paper yielded a Pb-208 diagram or a 208-site coordinate
list in the inspected/searchable text. This is not proof that none exists in
the book, figures, accompanying visualization software or earlier papers.
A published Pb-208 outer polyhedron and its layer-by-layer 82/126 assignment
have therefore NOT been recovered in this inspection.

The meaningful precedent is a quantum-number-labelled FCC site model, not an
already-established identification with the repository's cell-based marked
P/N/E construction. Strong equivalence claims in these sources are claims of
the authors, not independently verified results of this inspection.

Downloaded working PDFs/text are in tmp/cook2011.pdf, tmp/cook2011.txt,
tmp/cook2013.pdf and tmp/cook2013.txt. No large source PDFs were added to the
research result directory.
