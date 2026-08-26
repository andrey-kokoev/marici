# Dihedral generalized-CP obstruction

Work package: WP596  
Owner: marici.Figueiredo

## Finite-representation census

WP595 finds a coefficient-independent diagonal orientation in the square
representation. The hostile question is whether a single finite doublet
actually breaks physical CP, and whether another equally typed dihedral
representation selects a different ratio.

For a faithful irreducible real doublet of \(D_n\), write
\(z=\sigma+is\). Rotation invariance permits a nonradial monomial only when
its angular charge is divisible by \(n\). The first angular invariant is

\[
\operatorname{Re}(z^n),
\]

of degree \(n\).

At renormalizable degree:

- \(D_3\) admits a cubic anisotropy;
- \(D_4\) admits a quartic anisotropy;
- every \(D_n\) with \(n\ge5\) has accidental \(O(2)\) symmetry in the
  scalar potential.

Thus square symmetry is unique among faithful irreducible dihedral doublets in
supporting a renormalizable quartic orientation selector.

## Generalized-CP theorem

The angular extrema of \(\operatorname{Re}(z^n)\) occur at

\[
\theta={m\pi\over n}.
\]

Every such line is a reflection axis of \(D_n\). Consequently every
single-doublet angular extremum preserves some reflection, which is a
generalized CP transformation when the chosen CP is one member of the
dihedral reflection class.

For WP595 specifically, let \(R\) be the quarter turn and \(C\) the bare
reflection. On the diagonal representative \(v=(1,1)\),

\[
Cv\ne v,
\qquad
RCv=v.
\]

The one-half orientation is exact, but physical spontaneous CP breaking does
not follow.

## Corrected explanatory status

A single finite doublet cannot simultaneously provide:

1. a renormalizable coefficient-independent angular orbit;
2. removal of all generalized CP stabilizers;
3. a physical CP-odd prediction through an invariant portal.

The smallest progressive architecture uses at least two source multiplets
whose residual reflection subgroups are misaligned so that their intersection
contains no generalized CP. Alternatively, a fully declared portal
representation could remove the internal rotation used in the stabilizer, but
then the square symmetry would no longer silently authorize the scalar
potential without an explicit breaking analysis.

An observed nonzero physical CP-odd invariant is an experimental criticism of
the single-doublet architecture only after the portal map is shown to respect
the admitted internal group. The current scalar construction alone has no
such instrument.

## Reproduction

Run:

    uv run --offline python research/flavor/checkers/wp596_dihedral_generalized_cp_obstruction.py

The generated result is
research/flavor/results/wp596_dihedral_generalized_cp_obstruction.json.
