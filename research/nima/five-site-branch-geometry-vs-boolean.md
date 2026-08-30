# Five-Site Branch Geometry Is Not the Full Boolean Deck Lattice

Entry 1217 gives

\[
F_i=\det(H)(\ell-r_i)^2
\]

in the physical three-coordinate Gram chart. Therefore \(F_i-F_j\) is
affine-linear in the three loop coordinates. A \(k\)-fold branch intersection
is consequently cut out by one quadric and at most \(k-1\) affine-linear
equations.

On a generic complex three-dimensional base:

- \(k=1\): a quadric divisor;
- \(k=2\): a quadric curve inside one affine plane;
- \(k=3\): finitely many points on an affine line;
- \(k=4\): generically empty, since the unique affine point misses the
  remaining quadric;
- \(k=5\): generically empty already at the linear-equation stage or after
  the final quadric condition.

On the real positive-definite Euclidean chamber the statement is sharper:

\[
F_i=0\iff \ell=r_i.
\]

Hence distinct physical branch divisors have no common real point unless
external points collide.

The exact checker freezes five rational points in \(\mathbb Q^3\), audits all
31 nonempty subsets, solves the affine difference equations exactly, and
tests the restricted quadric. It supplies a concrete generic control of the
dimension argument.

## Consequence for the mod-two deck shadow

The algebra

\[
\mathbb F_2[\epsilon_1,\ldots,\epsilon_5]/(\epsilon_i^2)
\]

and its 31 nonzero square-free monomials are a correct formal deck-group or
Loewy object. Their degree profile

\[
(5,10,10,5,1)
\]

is the Boolean profile of five labelled deck directions. It is not, without
a separate locus calculation, the incidence profile of nonempty physical
branch strata.

Thus Grothendieck's norm, bad-prime, Loewy-degree, and multiplication theorems
remain valid algebraically. The geometric interpretation must be restricted
to those branch subsets actually realized on the complexified or physical
source locus.

Artifacts:

- research/nima/check_five_site_branch_geometry_vs_boolean.py
- research/nima/results/five-site-branch-geometry-vs-boolean.json
