# Simplex cones versus historical closed graph-domain packages

## Admissibility

The simplex-chain realization does define closed cone packages. For a face inclusion

\[
f:N_*\mathbb C[\tau]\widehat\otimes V
\longrightarrow
N_*\mathbb C[\sigma]\widehat\otimes V,
\]

`f` is bounded with closed range. Its graph domain is the whole Hilbert tensor product. The block cone differential

\[
d_{Cone(f)}=
\begin{pmatrix}d_\sigma&f\\0&-d_\tau\end{pmatrix}
\]

is bounded and closed. Reciprocal and Fourier transports act by bounded chain equivalences.

This places the new objects inside the bounded, entire-domain subcategory of the historical category of closed cone packages.

## Homological comparison

A simplex and any nonempty face are contractible, and the face inclusion is a homotopy equivalence. Therefore

\[
H_*\operatorname{Cone}
\bigl(N_*(\tau)\to N_*(\sigma)\bigr)=0.
\]

Tensoring with the channel carrier preserves this contraction. The checker confirms zero relative Betti numbers in dimensions one, two, and three.

The historical degree-four Waldhausen fixture uses explicit rectangular maps such as

\[
\mathbb C^2\longrightarrow\mathbb C^3.
\]

Its first displayed matrix has full column rank and a one-dimensional cokernel. Its cone therefore has a nonzero defect class. An acyclic simplex-face cone cannot be quasi-isomorphic to that package.

## Result

The comparison has two levels:

1. **Target-category comparison:** successful. Simplex cones are legitimate bounded closed graph-domain packages with entire domains and closed ranges.
2. **Objectwise identification:** rejected for the historical nonzero-defect packages. Their kernel/cokernel data differ from the contractible simplex-face cones.

A matching realization must attach the historical edge operator `F_e` to each geometric edge and form

\[
\operatorname{Cone}(F_e),
\]

using simplex chains only as the incidence index. Replacing `F_e` by the simplicial face inclusion erases the analytic defect.

## Correction to the theorem

The full `esd_7` construction currently proves a coherent bounded cone-valued indexing model. Its cone relations and signed symmetries are valid. Its simplex-face quotient cells are homologically trivial. The phrase “nonzero exact realization” applies to the ambient objects, not to nonzero quotient defects.

Recovering the historical realization requires a cellwise assignment from the existing analytical-form registry to actual closed operators, followed by cone formation and shared-face compatibility checks.

`check_simplex_face_cone_graph_package.py` verifies closed-package admissibility and acyclicity.
