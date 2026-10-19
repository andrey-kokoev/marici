# Two newly added PDFs: relevance to the force-free tetrahedral program

## Discovery and reading scope

Ran `pnpm pdf:reindex` first:4750 pages in48 PDFs,44 pages more than the prior
index. The new files are:

* `preprints202604.0421.v1.pdf` (28 PDF pages): Ors Marton, *Space as an Ether
  Crystal: A Unified Model of Gravity, Electromagnetism, Light, and Matter*,
  posted7April2026, DOI10.20944/preprints202604.0421.v1. Cover explicitly says
  NOT PEER-REVIEWED. Search alias `preprints202604-0421-v1`.
* Filename ending `72-1_IqFYd1k.pdf` (16 PDF pages): L.V. Migal and V.G. Bondarev,
  *Computer visualization of the spatial structure of the atomic nucleus*,2022,
  DOI10.18413/2518-1092-2022-7-2-0-1. Search alias `72-1-iqfyd1k`.

Read abstracts and the relevant construction, nuclear, parameter and validation
sections, not a complete critical review of every claim in either paper.
Visually inspected Migal PDFpp4,6 and Marton PDFpp6,19. Renderings are under
`temp/strominger/new-nuclear-pdfs/`. Locators below are PDF pages, including
Marton's extra cover, not his printed-page numbering.

## Marton: closely related motifs, substantially different model

Useful mathematical structure (PDFpp5-6): the SAME four tetrahedral directions
we use, assigned to four FCC sublattices. Unit directions u_i satisfy

    sum u_i u_i^T=(4/3)I,
    sum (I-u_i u_i^T)=(8/3)I.

This is a valid isotropic quadratic response identity. It could be reused as a
kinematic common-channel frame without adopting an ether, force law or particle
identification. It is NOT by itself a derivation of fully isotropic wave dynamics.
Our exact check gives fourth directional moments4/9 along a cubic axis versus
28/27 along a body diagonal. A dynamical operator and its dispersion must still
be examined before any propagation claim.

Particle assignments differ fundamentally from ours (PDFpp13-16): electron as
crowdion defect; proton as toroidal vortex dressed by a positron; neutron as the
same proton-like core plus an orbiting electron. This is not tetrahedral P/N
coordination roles. The useful conceptual rival is SAME carrier, DIFFERENT
internal/interface state. The proposed electron identification is not established
by crowdions being known in metals.

There are also TWO different spatial networks (PDFpp18-19): a four-orientation
FCC background, but SIX-coordinate rock-salt ordering for nucleon centers. It
cannot be substituted for our FOUR-coordinate diamond. Grouping four FCC
cosets into two pairs leaves4 same-group and8 opposite-group nearest neighbors,
not6 opposite neighbors. The proposed connection between grouping and rock salt
therefore needs an additional geometric/adjacency construction.

This paper does not satisfy the operator's no-added-forces requirement:
Coulomb energetics selects ordering (p18), screening is force-averaged (p20), and
a Morse pair potential/Frenkel-Kontorova model supplies coupling (p26). A computed
g~0.81 gives inverse alpha~152; tuning toward g~0.998 gives~137. Euler's number
enters the relation with no explanation acknowledged on p26. These are not
parameter-free structural derivations of both electron mass and alpha.

Two conditional checks on literal constituent claims:

* Its rounded masses give mp+me-mn=-0.782MeV, not positive binding of an ordinary
  below-threshold proton-electron bound state. A resonance/excitation mechanism
  would need specification; the mass subtraction itself predicts nothing new.
* Ordinary spin1/2 proton plus spin1/2 electron, with integer orbital angular
  momentum, has integer total spin. Recovering neutron spin1/2 would require
  additional structure and an actual rotation representation. A54.74degree
  lattice angle is not such a representation.

The FCC crowdion calculation is along[110] on p26, while the electron channel is
called[111] on p13. These directions are not equivalent close-packed rows: in
FCC integer coordinates with even coordinate sum, first same-row squared
separations are2 and12. A mode/channel correspondence must be supplied before
transferring one calculation to the other.

## Migal/Bondarev: directly useful representation, not independent magic counts

PDFpp3-5 give a common axis with planes perpendicular to it, cylindrical quantum
number coordinates and structural cells that can hold P, N, or a paired PN
configuration called a deuteron. This is relevant to our question of which
SPACE should carry the pairing. Site position and particle/pair state are not
automatically the same thing.

Potential force-free adaptation: put single-nucleon states on centers and an
explicit paired state on an ACTUAL P-N incidence edge, keeping endpoint identity
and preventing double use of one endpoint. This would be a new typed pairing
constructor to test, not a derived deuteron or imported binding force. Their
larger spherical/cylindrical deuteron cell cannot simply be identified with our
coordination tetrahedron.

The paper's magic numbers are not obtained from bare geometry:

* PDFp5 assumes a modified Pauli principle, minimum-energy filling, previous
  settlement rules and proton-neutron pairing.
* PDFp8 explicitly follows known proton energy-level ordering.
* PDFpp8,11 use experimental quadrupole behavior to select uncertain filling.
* PDFp10 adds a0.25 comparison coefficient for its asymmetry quantity.
* PDFpp12-14 use shell-specific occupancy choices to estimate isotope limits;
  p13 explicitly restricts available cells to obtain values near the known
  isotope diagram. This is not a fixed, independently selected geometric rule.

Thus the diagrams and constraints are useful comparison material. Their claimed
agreement is not an independent prediction of magic numbers or isotope endpoints
under our frozen incidence rule.

## Exact local audit and disposition

    python research/strominger/checkers/check_new_pdf_geometric_claims.py

Five exact checks passed; hashes of both actual PDFs and the checker are recorded
in `results/new-nuclear-pdf-relevance/geometry-audit.json`. This verifies only the
specified tensor/neighbor/distance/mass arithmetic, not either physical theory.
No original source graph, P/N assignment or previous negative result was changed.

Both papers are relevant as SOURCES OF RIVAL CONSTRUCTORS, not confirmation of
our model. Preserve the distinction between:

1. P/N locked to diamond A/B placement (our tested original proposal);
2. P/N as distinguishable INTERNAL interface patterns on a common geometric
   carrier, with pairing on edges or loops (a different candidate).

The second candidate has a useful lead in our already-constructed independent
interface loop modes. It still needs an explicit conserved readout and allowed
state operations, not merely new names for existing amplitudes. Reinterpreting
P/N this way would change the old hypothesis and must be registered as a new
rival rather than used to erase the earlier transfer obstruction.
