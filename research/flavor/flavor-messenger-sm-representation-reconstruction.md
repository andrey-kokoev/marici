# Messenger Standard Model representation reconstruction

## Bounded question

Do the already declared renormalizable messenger vertices uniquely determine
the missing Standard Model representations of both connector messenger stages?

## Source-derived reconstruction

WP435 states that an up- or down-sector messenger has the Standard Model
quantum numbers of the corresponding right-handed quark. WP483 inserts a
Standard Model singlet connector between two vectorlike messenger stages, and
the exit flavon is also a Standard Model singlet. Gauge invariance therefore
transports the same representation through both stages.

In the convention

\[
Q_L\sim(3,2,1/6),\qquad
u_R\sim(3,1,2/3),\qquad
d_R\sim(3,1,-1/3),
\]

the unique assignments are

\[
A^u_{L,R},B^u_{L,R}\sim(3,1,2/3),\qquad
A^d_{L,R},B^d_{L,R}\sim(3,1,-1/3).
\]

The entrance doublets have hypercharge one half. Consequently the up entrance
uses \(\widetilde H^u\), with hypercharge minus one half, while the down
entrance uses \(H^d\). This repairs the previously suppressed conjugation mark
in the gauged entrance packet.

## Exact checks

The checker verifies zero total hypercharge for all six route vertices:

\[
\bar Q_L\widetilde H^u A_R^u,
\quad \bar A_L^u S B_R^u,
\quad \bar B_L^u X u_R,
\]

and their down-sector analogues. It also verifies that every messenger is a
weak singlet and color triplet, that the singlet connector cannot change these
representations, and that each vectorlike pair has zero cubic, mixed, and
gravitational anomaly contribution in a left-handed basis.

Two hostile mutations are rejected exactly. Replacing \(\widetilde H^u\) by
\(H^u\) leaves hypercharge residual one. Assigning the second-stage up
messenger down-type hypercharge leaves connector residual minus one. Either is
the smallest one-field falsifier.

## Disposition

WP626's conservative Standard Model representation gap is closed by composition
of already source-authorized vertices; no fitted flavor coordinate was used.
The result completes one registry column but does not create a numerical
selector. Kinetic normalization, threshold status, complete interaction
closure, one-scheme beta functions, finite matching, and the calibrated
instrument remain open.

## Reproduction

Run:

    python research/flavor/checkers/wp627_messenger_sm_representation_reconstruction.py

The generated result is
`research/flavor/results/wp627_messenger_sm_representation_reconstruction.json`.

