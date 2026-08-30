# Two-doublet selector-versus-stability dichotomy

Work package: WP597  
Owner: marici.Figueiredo

## Bounded question

WP596 shows that one dihedral doublet always preserves a generalized CP.
Does the smallest proposed repair, two misaligned square-symmetry doublets,
provide a hard-to-vary physical CP selector?

Let the two ordered doublets be \(\phi\) and \(\psi\). The candidate vacuum
places \(\phi\) on an axis and \(\psi\) on a diagonal,

\[
v_\phi=(1,0),
\qquad
v_\psi={1\over\sqrt2}(1,1).
\]

For the generalized CP family \(R^kC\), where \(R\) is the quarter turn and
\(C\) is the bare reflection, \(v_\phi\) is fixed only at \(k=0\), while
\(v_\psi\) is fixed only at \(k=1\). There is no common generalized CP that
fixes the ordered pair.

## Common-group failure

The absence of a common stabilizer is not sufficient. Under one common
square symmetry, the renormalizable cross-quartic

\[
I_\times=(\phi\mathbin{\cdot}\psi)^2
\]

is invariant under both the common quarter turn and bare CP. At fixed radii,
the angular potential may therefore contain

\[
V_A={\kappa_\phi\over4}\sin^2(2\alpha)
+{\kappa_\psi\over4}\cos^2(2\beta)
+{\eta\over2}\cos^2(\alpha-\beta).
\]

At the proposed point \((\alpha,\beta)=(0,\pi/4)\), its exact gradient is

\[
\nabla V_A=
\begin{pmatrix}\eta/2\\-\eta/2\end{pmatrix}.
\]

Thus every nonzero allowed \(\eta\) moves the candidate. The relative angle
is not hard to vary under the complete renormalizable invariant grammar.
The smallest hostile instance is \(\eta=1\), which gives the nonzero gradient
\((1/2,-1/2)\).

## Independent-group failure

Giving the doublets independent square rotations forbids
\(I_\times\). It also restores independent generalized CP choices: the
axis component is stabilized by \(C\), and the diagonal component by
\(RC\). Their componentwise product stabilizes the full vacuum. Stability of
the orientation is recovered by enlarging the symmetry precisely in a way
that removes physical CP breaking.

## Disposition

The naive two-doublet repair fails as a hard-to-vary physical CP selector:

- one common group removes the generalized-CP stabilizer but permits an
  angle-moving cross invariant;
- independent groups forbid that invariant but preserve componentwise
  generalized CP.

This is not a proof that every multi-multiplet architecture fails. It isolates
the next constructor requirement: a source-derived symmetry or representation
must forbid every angle-moving cross invariant while retaining only one common
generalized-CP family, and the selected full vacuum must have no stabilizer in
that family. Merely deleting \(I_\times\) by hand would fit the desired answer.

## Physical criticism gate

Even a source architecture passing that algebraic gate would not yet have an
experiment. Its complete portal must descend to a calibrated CP-odd coordinate
on `physical16`. A second executable scalar or threshold record must test the
same cross-coupling structure that protects the relative angle. Without that
joined source-to-readout map, a measured CKM phase criticizes only the
low-energy packet, not this constructor.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp597_two_doublet_selector_stability_dichotomy.py

The generated result is
research/flavor/results/wp597_two_doublet_selector_stability_dichotomy.json.
