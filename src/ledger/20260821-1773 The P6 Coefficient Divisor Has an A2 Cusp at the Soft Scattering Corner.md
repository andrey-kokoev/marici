# 1773 — The \(P_6\) Coefficient Divisor Has an \(A_2\) Cusp at the Soft Scattering Corner

## Question

Entry 1771 identifies the repeated \(u=0\) resultant component with the
existing carrier corner

\[
E_T=0,\qquad X_2=0.
\]

What coefficient singularity does the algebraic Kummer divisor \(P_6=0\)
carry there?

## Exact completed local form

At \((u,v)=(0,2)\), set

\[
z=v-2,
\qquad
Z=z+u(1+2u-2u^2).
\]

Completing the square exactly gives

\[
\boxed{
4P_6=Z^2-4u^3(2-u)(1-u^2).
}
\]

The coefficient \(4(2-u)(1-u^2)\) is a unit with value \(8\) at the
center. In the completed characteristic-zero local ring, a formal coordinate
change absorbs this unit. The divisor germ is therefore

\[
Z^2-U^3=0.
\]

## Milnor algebra

The Jacobian algebra is

\[
\frac{\mathbb Q[[U,Z]]}{(2Z,3U^2)}
=\mathbb Q\langle[1],[U]\rangle.
\]

Hence

\[
\boxed{\mu(P_6;(0,2))=2.}
\]

## Classification

The rank-two \(A_2\) Milnor object is coefficient complexity over the already
frozen total-energy/site-soft carrier incidence. It is not a new carrier
stratum.

Nor may the Milnor rank be identified directly with a physical period or
relative-chain contribution. The next finite comparison must construct the
specialization of the source-defined \(P_6^{-1/2}\) Kummer line into this
\(A_2\) vanishing-cycle object and test it against the existing total-energy
and site-soft nearby-cycle maps.

## Durable evidence

- `research/benincasa/checkers/p6_soft_cusp.py`
- `research/benincasa/results/p6-soft-cusp.json`
- `research/benincasa/p6-soft-cusp.md`
- allocator claim: `seqclaim-9b1dcb775fde6835c2a0541c`

