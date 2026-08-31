# Irreducible spin-11 pole cell: WP1054

## Question

Can an irreducible representation turn WP1053's twenty-three declared pole
atoms into a degeneracy theorem?

## Explicit finite representation

Use the \(23\)-dimensional irreducible \(sl_2\) module of spin

\[
j=11,
\qquad
\dim V_{11}=2j+1=23.
\]

In the weight basis \(v_0,\ldots,v_{22}\), the exact integral action is

\[
Hv_a=(22-2a)v_a,
\]

\[
Fv_a=(a+1)v_{a+1},
\qquad
Ev_a=(23-a)v_{a-1}.
\]

The checker verifies

\[
[E,F]=H,
\qquad
[H,E]=2E,
\qquad
[H,F]=-2F,
\]

and

\[
EF+FE+\frac{H^2}{2}=264I=2j(j+1)I.
\]

The \(H\)-weights are distinct, and the \(E/F\) action forms one connected
weight chain. This is the finite irreducibility certificate.

## Derived pole data

On this irreducible cell, an invariant mass or residue operator must be
scalar. Taking the common clock \(M^2=1\) gives

\[
C=23,
\qquad
r_i=1,
\qquad
M_i^2=1,
\qquad
\frac{R(1)}{R(0)}=\frac12.
\]

Thus the WP1053 atom list is upgraded from a declaration to an explicit
representation certificate: the spin-11 multiplet supplies the twenty-three
internal pole atoms and their degeneracy.

## Reducible-clock hostile

The split mass operator

\[
D=\operatorname{diag}(1^{\times22},4)
\]

does not commute with the spin-11 \(E/F\) action. It is therefore not a mass
operator on this irreducible cell. Its response remains

\[
\frac{R(1)}{R(0)}=\frac{59}{115},
\]

not \(1/2\).

## Boundary

The representation does not select \(j=11\). It also does not derive the
external two-port arity \(k=2\); this packet treats the ports as an additional
incidence label. The remaining source gates are therefore:

1. derive the spin-\(11\) pole multiplet from the actual source
   representation;
2. derive the two-port arity;
3. derive the common mass scale.

## Classification

Conditional irreducible-multiplet constructor. It converts WP1053's finite
atom provenance into a representation degeneracy theorem and rejects the
\(22+1\) clock as an operator on the irreducible cell.

Checker: `research/flavor/checkers/wp1054_irreducible_spin11_pole_cell.py`

Result: `results/wp1054_irreducible_spin11_pole_cell.json`
