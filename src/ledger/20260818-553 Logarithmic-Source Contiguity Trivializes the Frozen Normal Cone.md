---
id: 553
date: 2026-08-18
title: Logarithmic-Source Contiguity Trivializes the Frozen Normal Cone
authors:
  - marici.Nima
---

# Logarithmic-Source Contiguity Trivializes the Frozen Normal Cone

Entry 551 showed that the deletion census itself contains no morphism between
its rank-seven and rank-twelve critical quotients. This entry asks whether the
frozen coefficient \(17\) nevertheless permits a source-derived chain map.

Let

\[
U=\mathbb A^3\setminus V(K),\qquad
j:U\setminus V(q_{g1})\hookrightarrow U,
\]

and write

\[
\nabla_0=d+5\,d\log K,\qquad
\nabla_{17}=\nabla_0+17\,d\log q_{g1}.
\]

## Exact contiguity identity

On \(U\setminus V(q_{g1})\), multiplication by \(q_{g1}^{-17}\) satisfies

\[
\boxed{
\nabla_{17}\!\left(q_{g1}^{-17}\omega\right)
=q_{g1}^{-17}\nabla_0\omega.
}
\]

The underlying localization map is also explicit. If the source and target
inverse variables obey

\[
uK=1,\qquad vKq_{g1}=1,
\]

then

\[
\boxed{u\longmapsto vq_{g1}}
\]

preserves the source relation. Thus the frozen integer specialization has a
genuine chain-level morphism

\[
(\Omega_U^\bullet,\nabla_0)
\longrightarrow
j_*(\Omega_{U\setminus V(q_{g1})}^\bullet,\nabla_{17}),
\qquad
\omega\longmapsto q_{g1}^{-17}\omega.
\]

Its cone is legitimately typed. If the source lattice is enlarged to
logarithmic normal forms, its normal calculation is governed by

\[
[k\xrightarrow{17}k].
\]

Since \(17\) is invertible over both \(\mathbb Q\) and the census field
\(\mathbf F_{32003}\), this logarithmic-source normal complex is acyclic.

## Ordinary-source correction

Entry 558 identifies the lattice distinction omitted in the original version
of this entry. The actual source on the space containing the wall has ordinary
one-forms. Its image does not contain

\[
q^{-17}\frac{dq}{q},
\]

so the ordinary-to-meromorphic cone has one-dimensional normal cohomology.
The acyclicity theorem here applies only to the logarithmic-source control.

## Scope boundary

Thus logarithmic-source contiguity cannot produce the supported class. The
ordinary-source cone of Entry 558 can, after tensoring with the independently
computed unmarked tangential rank-five object.

Nor does integer contiguity construct the desired generic regulator family.
For a formal or nonintegral exponent \(\alpha\), \(q_{g1}^{-\alpha}\) is not an
algebraic function on the complement. One must retain a Kummer local system or
root-stack coefficient object. Therefore:

\[
\boxed{
\text{integer frozen cone: typed}
\quad\neq\quad
\text{generic Kummer realization: constructed}.
}
\]

This refines Entry 551 rather than reversing it: the missing morphism can be
derived at the exact integer specialization, but its cone depends essentially
on the chosen ordinary or logarithmic source lattice. Entry 552's formal
coefficient-space resonance remains a distinct construction.

## Next finite gate

Compare Entry 558's ordinary-source rank-five cone with Entry 549's resolved
boundary packet, retaining the regulator connection and marked pair residues.

The executable audit is
\`research/benincasa/check_generic_lower_integer_contiguity.py\`.
