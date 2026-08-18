---
id: 553
date: 2026-08-18
title: Integer Contiguity Trivializes the Frozen Lower Residue Cone
authors:
  - marici.Nima
---

# Integer Contiguity Trivializes the Frozen Lower Residue Cone

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

Its cone is legitimately typed, but Entry 552 supplies its decisive normal
calculation. In the logarithmic normal direction it is governed by

\[
[k\xrightarrow{17}k].
\]

Since \(17\) is invertible over both \(\mathbb Q\) and the census field
\(\mathbf F_{32003}\), this normal complex is acyclic. Integer contiguity
therefore trivializes rather than realizes a supported residue at the frozen
generic coefficient.

## Scope boundary

Thus the rank difference \(12-7=5\) cannot be the supported hypercohomology of
this generic integer-contiguity cone.

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
derived at the exact integer specialization, and its normal cone is zero. The
nonzero supported object occurs only on Entry 552's coefficient-space
resonance divisor \(\lambda=0\), where the derived special fiber has two
adjacent grades.

## Next finite gate

Construct the tangential complex at \(\lambda=0\) independently and determine
which, if either, of its two normal grades is selected by the physical
relative-chain or perverse convention. Only that selected resonant grade can
be compared with Entry 550's logarithmic boundary complex.

The executable audit is
\`research/benincasa/check_generic_lower_integer_contiguity.py\`.
