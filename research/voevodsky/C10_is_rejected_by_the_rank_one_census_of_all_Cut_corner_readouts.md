# C10 is rejected by the rank-one census of all Cut-corner readouts

Stack the projections of

\[
(g_{101},g_{110},g_{111}^{\sim})
\]

at all four sign corners and all three cyclic sectors. This gives 36 columns in the target basis

\[
(e_6,v_{\rm alg}).
\]

Every column is either

\[
(0,0)
\quad\text{or}\quad
(1,0).
\]

The resulting \(2\times36\) matrix has

\[
\operatorname{rank}=1,
\qquad
\operatorname{Smith}=(1).
\]

Its image and cokernel are

\[
\operatorname{im}=\mathbb Z(1,0),
\qquad
\operatorname{coker}\cong\mathbb Z\langle v_{\rm alg}\rangle.
\]

Every \(2\times2\) minor vanishes, so every pair of sourced Cut-corner observables has rank at most one. The unit Smith invariant confirms that the detected \(e_6\) line is primitive after the occurrence-resolved Betti normalization.

Therefore C10 is rejected throughout the frozen total-energy/Cut corner and cyclic orbit: two observables chosen from this family cannot span the full algebraic plane.

A second tomography channel must carry a tail in

\[
\langle e_7,e_8,e_9\rangle
\]

proportional to \(v_{\rm alg}\). The strongest candidate is a logarithmic mixed column or an iterated discontinuity involving a distinct discriminant.

Certificate:

- `research/voevodsky/checkers/reject_C10_all_corner_projection_rank.py`;
- `research/voevodsky/results/C10_all_sourced_corner_projection_rank.json`.
