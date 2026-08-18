---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 660 — The Algebraic Quartic Is the Källén Discriminant of a Two-Sheeted Incidence Cover

## Hard-to-vary claim

The source quartic

\[
\mathcal Q=4AB-(A+B-E^2)^2
\]

is exactly the negative Källén discriminant of \((A,B,E^2)\). Equivalently,
it is the collision discriminant of a natural quadratic algebraic cover
built only from the frozen signed-energy functions. This proves that
\(\mathcal Q=0\) admits a source-compiled coefficient-cover realization
without adding a carrier stratum. It does not establish that this cover is
contained in the physical coefficient system, nor identify it with the
physical integration chain or a subquotient of the rank-twenty residue
system.

## Frozen source functions

Retain

\[
B=E(2s-E),\qquad A=B-4p,
\]

and introduce no new kinematic function. Consider the quadratic incidence
equation

\[
f(z)=Az^2-(A+B-E^2)z+B.
\]

Its discriminant in the fiber coordinate \(z\) is

\[
\operatorname{Disc}_z(f)
=(A+B-E^2)^2-4AB
=-\mathcal Q.
\]

Therefore the two roots

\[
z_\pm=
\frac{A+B-E^2\pm\sqrt{-\mathcal Q}}{2A}
\]

define a generic two-sheeted algebraic coefficient cover, and the sheets
collide precisely on \(\mathcal Q=0\).

Over a square-root extension this is the threshold factorization

\[
\mathcal Q
=
\bigl((\sqrt A+\sqrt B)^2-E^2\bigr)
\bigl(E^2-(\sqrt A-\sqrt B)^2\bigr).
\]

Thus the quartic records a relative alignment/collision of two algebraic
sheets, not the appearance of an additional incidence cell.

## Normal-order audit

Substitution of the frozen homogeneous functions gives

\[
\mathcal Q
=-16p^2-8pE^2+8sE^3-5E^4.
\]

Hence

\[
\operatorname{gr}^{(1)}_E\mathcal Q=0,
\qquad
\operatorname{gr}^{(2)}_E\mathcal Q=-8p.
\]

The quadratic cover therefore reproduces the previously observed fact that
the first ordinary normal jet cannot detect the algebraic deformation.

## Relation to the rank-thirty-five work

Entry 659 studies the extension

\[
0\to M_{15}^{\rm del}\to M_{35}^{\rm phys}
\to M_{20}^{\rm res}\to0.
\]

No part of the present calculation reconstructs its off-diagonal connection
block. The result lives entirely over the post-residue coefficient base and
is compatible with Nima's calculation regardless of the rank-thirty-five
splitting.

## What is established

\[
\boxed{
\mathcal Q=0
\text{ is the collision divisor of a source-compiled candidate algebraic double cover.}
}
\]

Classification:

- existing carrier: the signed-energy/Cayley--Menger base;
- candidate coefficient support: the branch collision of \(f(z)=0\);
- new carrier datum: none.

## What is not established

The quadratic variable \(z\) has not yet been derived as a marked
integration-chain endpoint or as a coordinate on the source's relative
elliptic surface. Consequently this entry does not prove that the
\(\mathcal Q\)-cover is the physical algebraic line, the
elliptic--algebraic extension class, or the regulator local system.

## Next falsifier

Derive the source-defined algebraic endpoint ratio on the
\(q_{\mathcal G_{12}}\)-residue surface and test whether it obeys

\[
Az^2-(A+B-E^2)z+B=0.
\]

If yes, \(\mathcal Q\) is physical-chain/relative-period support. If the
actual endpoint satisfies a different minimal polynomial, this quadratic
cover is only an ambient algebraic compilation and must not be identified
with the physical coefficient system.

## Evidence

- source identity \(\mathcal Q=4AB-(A+B-E^2)^2\);
- Entries 128, 150, 526--528, 658--659;
- research/benincasa/q-kallen-incidence-discriminant.json.
- epistemic event ev-000000000262-ff741e96-77a9-41d6-a8b4-7c4b3bf8b886.

## Outcome contract

~~~json
{
  "claim": "The source quartic has no intrinsic algebraic provenance over the frozen energy carrier.",
  "status": "falsified",
  "provenance": "negative Kallen discriminant of A, B, and E^2",
  "incidence_polynomial": "A*z^2-(A+B-E^2)*z+B",
  "collision_divisor": "Q=0",
  "classification": "source-compiled candidate coefficient support",
  "membership_in_physical_coefficient_system": "open",
  "physical_chain_identification": "open",
  "new_carrier_datum": false,
  "next_experiment": "Derive the physical endpoint ratio and test its minimal polynomial."
}
~~~
