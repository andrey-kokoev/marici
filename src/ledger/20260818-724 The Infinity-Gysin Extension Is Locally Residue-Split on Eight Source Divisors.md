---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 724 — The Infinity-Gysin Extension Is Locally Residue-Split on Eight Source Divisors

## Question after Entry 722

Entry 722 excludes a global splitting with one declared simple-pole
denominator and numerator degree at most ten.  A stronger possible explanation
would be a local logarithmic extension obstruction on one of the source
divisors.

## Frozen residue equation

In the Gysin-adapted frame write the residue along a smooth divisor (f=0) as

\[
R_f=
\begin{pmatrix}
R_K&0\\
R_E&R_B
\end{pmatrix}.
\]

The logarithmic extension class vanishes at the residue level exactly when

\[
L_0(X):=XR_K-R_BX=-R_E
\]

is solvable.  A pole of order (m>0) can begin only in the kernel of the
indicial operator

\[
L_m(X)=-mX+XR_K-R_BX.
\]

## Parameterized divisors

Take transverse Laurent residues on

\[
u, v, y, 1-y, 1+y, v-u, y-u^2, y+u^2.
\]

For every divisor, evaluate sixteen independent generic points over
\(\mathbf F_{2^{61}-1}\).  Reconstruct every entry of the (4\times4)
residue matrix before testing the extension equation.

## Result

The residue equation is solvable at every tested point on every divisor:

\[
\boxed{
R_E\in\operatorname{im}L_0
\quad\text{on all eight parameterized source divisors.}
}
\]

Thus the global failure in Entries 721--722 is not explained by a local
logarithmic residue class on these divisors.

The indicial census through pole order ten separates two groups:

\[
\begin{array}{c|c}
\text{divisor}&\ker L_m, 1\le m\le10\\
\hline
u,v,y,1-y,1+y&0\text{ for every tested }m\\
v-u,y-u^2,y+u^2&\dim\ker L_1=2,\quad\ker L_m=0\ (2\le m\le10).
\end{array}
\]

Hence the first five divisors cannot support a meromorphic splitting with pole
order at most ten.  The final three admit a local order-one resonant leading
term, but Entry 722 proves that none extends to the tested global polynomial
numerator.

## Narrow interpretation

The obstruction is now constrained to global compatibility, mixed-divisor
gluing, the unparameterized (P_6) or \(\mathcal Q\) divisors, higher-degree
numerators, or genuine differential-module nonsplitting.  No new carrier
stratum is indicated.

In particular, residue solvability must not be promoted to a global splitting,
and the three order-one resonances must not be fitted into a mixed denominator
without deriving their compatibility.

## Evidence

- Entries 207, 721--722;
- `research/benincasa/marici-gm/src/main.rs`;
- `research/benincasa/marici-gm/gysin-local-residue-obstruction-16.json`;
- allocator claim `seqclaim-4e67d8188640f98c24e207e3`.

## Next falsifier

Compute the local residue equations on (P_6=0) and \(\mathcal Q=0\) using
their function fields rather than fitted rational points.  Then compute the
Čech compatibility of the local residue splittings on pairwise intersections
of the three resonant divisors.  A nonzero overlap cocycle would locate the
extension globally without introducing a new carrier component.
