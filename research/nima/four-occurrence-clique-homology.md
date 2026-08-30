# Supported Cyclic Memory Is Clique Homology

The four-occurrence amplitude result has a canonical combinatorial form.
Given the support graph \(G\) of nonzero pair coherences, fill every supported
triangle.  Triangle Bargmann ports generate the image of the simplicial
boundary

\[
\partial_2:C_2(\operatorname{Cl}G)\longrightarrow C_1(\operatorname{Cl}G).
\]

The supported cycle carrier that cannot be filled by those ports is

\[
\boxed{
H_1(\operatorname{Cl}G)
=\ker\partial_1/\operatorname{im}\partial_2.
}
\]

The corresponding phase records live in the dual coefficient object

\[
H^1(\operatorname{Cl}G;U(1))
\simeq
\operatorname{Hom}(H_1(\operatorname{Cl}G),U(1)).
\]

Thus \(H_1\) types the surviving port, while \(H^1\) is its phase readout.

An exact census of all \(2^6=64\) labelled support graphs on four vertices
finds:

- the complete support has graph-cycle rank three, but its triangle
  boundaries also have rank three, so the quotient vanishes;
- every support containing a reconstructing triangle has vanishing quotient;
- exactly three supports have nonzero quotient: the three labelled chordless
  Hamiltonian four-cycles;
- each surviving quotient is one-dimensional.

This explains Ledger 2044 without coordinates.  Generically, triangles fill
every cycle.  Deleting both chords removes the filling two-simplices while
leaving their boundary cycle, which becomes a supported record.

It also sharpens the comparison with Benincasa's pure four-mode result.  The
three primitive Gaussian Hamiltonian traces are indexed by the same three
labelled four-cycles.  Generically they are readouts of lower pair data.  The
hostile Gaussian finite-fiber test should therefore be stratified by the three
corresponding chord-deletion supports rather than performed only on the dense
open quotient.

The exact checker passes 7/7 gates.

Artifacts:

- `research/nima/four-occurrence-clique-homology.md`
- `research/nima/checkers/check_four_occurrence_clique_homology.py`
- `research/nima/results/four-occurrence-clique-homology.json`

Sequence claim: `seqclaim-a3dd9472ae28d46dfb164c49`.
