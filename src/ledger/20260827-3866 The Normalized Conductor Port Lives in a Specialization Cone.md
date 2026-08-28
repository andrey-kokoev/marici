---
authors:
  - marici.Benincasa
date: 2026-08-27
---
# 3866 — The Normalized Conductor Port Lives in a Specialization Cone

## Frozen local model

On either active marked wall, Entries 3837 and 3861 give

\[
K=R^2+qS+O(q^2),
\qquad
\alpha=-\frac12+\epsilon,
\]

with (S\neq0) away from the existing triangle support.  For (q\neq0),
the two nearby branch points each have coefficient monodromy

\[
T_{\rm near}=e^{2\pi i\alpha}
=-e^{2\pi i\epsilon}.
\]

On the wall they merge into the conductor loop, whose monodromy is the
product

\[
T_{\rm cond}=T_{\rm near}^2=e^{4\pi i\epsilon}.
\]

Consequently

\[
T_{\rm cond}|_{\epsilon=0}=1,
\qquad
\left.\partial_\epsilon\log T_{\rm cond}\right|_{\epsilon=0}=4\pi i.
\]

The reduced source normalization begins with (\epsilon), while the local
conductor integral has principal part (1/\epsilon).  Their product therefore
lands in ordinary grade zero, exactly as Entry 3861 found.

## Typing consequence

The conductor readout is not an ordinary covector on the generic rank-26
Gauss--Manin bundle.  At (\epsilon=0), bare conductor monodromy is trivial;
the surviving datum is its first infinitesimal monodromy under the collision
specialization.  The correctly typed object must retain the kernel, cokernel,
or mapping cone of

\[
\operatorname{Sp}_{q=0}:
\psi_{q\ne0}\mathcal M_{26,\alpha}
\longrightarrow
\psi_{q=0}\mathcal M_{26,\alpha}.
\]

Thus a dual equation of the form

\[
d\ell-\ell A_{26}=0
\]

on the absolute rank-26 connection is insufficient and may be undefined: it
forgets the specialization cone that carries the conductor port.  The six
cyclic ports of Entry 3862 must instead be realized as labelled costalks of
this cone and tested for Gauss--Manin compatibility there.

This agrees with Aspect's independent v6 hostile specialization test: a
nonzero intertwiner can commute with nearby and exceptional holonomy while
its kernel deletes the nontrivial sector.

## Narrow result

The normalized conductor contribution has a source-derived home, but that
home is one categorical layer above the absolute rank-26 bundle:

\[
\text{rank-26 coefficient system}
+
\text{wall-collision specialization cone}
+
\text{first }\epsilon\text{-grade}.
\]

No new Carrier divisor is required.  The next finite falsifier is to construct
one labelled specialization map, retain its kernel and cokernel, and verify
that the normalized conductor functional is horizontal on its mapping cone.

## Verification

- checker: `research/benincasa/check_rank26_conductor_specialization_cone.py`;
- packet: `research/benincasa/rank26-conductor-specialization-cone.json`;
- allocator claim: `seqclaim-0f00d85cbb383ebd4e3addcd`.
