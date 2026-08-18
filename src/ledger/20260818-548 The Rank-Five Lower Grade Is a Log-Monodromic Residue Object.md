---
id: 548
date: 2026-08-18
title: The Rank-Five Lower Grade Is a Log-Monodromic Residue Object
authors:
  - marici.Nima
---

# The Rank-Five Lower Grade Is a Log-Monodromic Residue Object

Entry 547 proves that the complete lower-sector deletion cube has exactly the
support incidence required by Entry 544's Kato kernel calculus.  This entry
types its coefficient objects and connecting maps.

Let

\[
U=\mathbb A^3\setminus V(K),\qquad
D_i=V(q_i)\cap U.
\]

The first deletion triangle for the Cartier divisor \(D_i\hookrightarrow U\)
identifies the proper single-pole object with the shifted twisted residue

\[
\boxed{
\mathcal R_i=
R\Gamma_{\rm dR}
\left(
V(q_i)\setminus V(K|_{q_i}),
\mathcal L_K
\right)[\text{Gysin shift}].
}
\]

Its rank is the deletion increment

\[
12-7=5.
\]

Thus the rank-five grade is an algebraic relative surface coefficient object:
a pole plane with the restricted Cayley--Menger curve removed, carrying the
restricted twist.  It is not a new carrier stratum.

Iterating the same localization triangle gives canonical coefficient kernels:

\[
\mathcal R_i
\longrightarrow
R\Gamma_{\rm dR}(D_i\cap D_j,\mathcal L_K)[1]
\longrightarrow
i_{ijk}^!\mathcal L_K[2].
\]

For the five transverse pair lines, the proper residue rank is one.  For the
unique parallel pair (D_1,D_{23}), the fiber product is empty at generic
kinematics, so the residue is zero geometrically.  Exactly the two transverse
triple points have rank-one costalks; the other triples and the fourfold
support are empty.  The ordered conormal determinant supplies the Boolean
signs proved in Entry 547.  Hence the connecting maps have precisely Entry
544's Cartier localization/Gysin kernel type, without fitted splittings.

## Coefficient-sector refinement

The critical census uses pairwise-distinct generic regulator residues, with
finite-field representatives

\[
(17,19,23,29).
\]

These are additional logarithmic connection data on the four pole divisors.
They are not present in Entry 544's bare trivial-inertia finite coefficient
diagram.  Therefore the cross-sector result is

\[
\boxed{
\text{shared fs/Kato support and mixed-variance kernel calculus}
+
\text{sector-specific logarithmic coefficient objects}.
}
\]

This is evidence for H2 in its refined form, not for universal coefficients.
The cosmology object requires a logarithmic connection with regulator
residues.  It is tempting to identify this with a nontrivial-inertia sector of
the Artin-cone stack, but that identification is not established: analytic or
formal connection residues and algebraic stabilizer characters must not be
equated without a realization functor.

The next exact gate is to construct that coefficient realization, or more
conservatively to compute one explicit residue/Gysin matrix in a
source-defined basis of \(\mathcal R_i\) and verify its compatibility with the
rank-one pair object and the Gauss--Manin connection.

The executable audit is
`research/benincasa/check_generic_lower_residue_kernel_typing.py`.
