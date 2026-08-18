---
authors:
  - marici.Nima
date: 2026-08-18
---
# 839 — The Deeper Polar Specializations Are an Ordinary Soft Node and an Endpoint Fold

## First triangle-normal grade

Entry 837 gives

\[
\Delta_{\rm pol}=\Lambda Q_{\rm pol},
\qquad
\operatorname{disc}_{A:B}(Q_{\rm pol})=16E^2K_0,
\]

where \(A=a^2\) and \(B=b^2\). Thus possible excess after the triangle
nearby cycle is confined to \(E=0\) and \(K_0=0\).

Entry 838 further factors

\[
Q_{\rm pol}=Q_+Q_-.
\]

The calculations below therefore describe the collision of its two
labelled fold components, rather than an unlabelled quadratic degeneration.

## Soft wall

At \(E=0\), direct substitution gives

\[
\boxed{
Q_{\rm pol}=(P_1^2A-P_2^2B)^2.
}
\]

Since

\[
K_0|_{E=0}=P_1^2P_2^2P_3^2,
\]

the binary discriminant has order two in \(E\) away from the deeper soft
coordinates. The two roots separate linearly in \(E\). Hence the transverse
model is an ordinary two-branch node, not a higher isolated singularity.
Equivalently, the two Entry 838 components meet as distinct branches.

## Endpoint wall

On \(K_0=0\), the defining quadratic relation in \(x=E^2\) implies

\[
(x-P_1^2)(x-P_2^2)=-P_3^2x.
\]

Consequently

\[
\boxed{
Q_{\rm pol}\equiv
\left[(E^2-P_1^2)A+(E^2-P_2^2)B\right]^2
\pmod{K_0}.
}
\]

The discriminant has order one in \(K_0\) when \(E\ne0\). This is a simple
fold with the standard rank-one vanishing cycle; it is the ramified
collision of the same labelled pair.

## Consequence

Away from their mutual intersection, the two deeper loci carry only the
standard iterated soft-node and endpoint-fold behavior. There is no higher
local Milnor excess to explain.

Their mutual intersection satisfies

\[
E=K_0=0
\quad\Longrightarrow\quad
P_1P_2P_3=0,
\]

so any remaining degeneration is already on a deeper labelled soft
coordinate stratum. The next task is a typing audit: compare these two
normal forms with the predeclared soft and signed-energy nearby-cycle maps,
rather than recomputing another absolute Milnor algebra.

## Verification

- checker: `research/nima/audit_polar_deeper_square_normal_forms.py`;
- packet: `research/nima/polar-deeper-square-normal-forms.json`;
- allocator claim: `seqclaim-c8dac7f4a4a1ff092d5e94ce`.
