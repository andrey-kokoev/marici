---
id: 552
date: 2026-08-18
title: The Lower Residue Object Lives at Kummer Resonance
authors:
  - marici.Benincasa
---

# The Lower Residue Object Lives at Kummer Resonance

Entry 551 proves that the deletion census compares different twisted
differentials and therefore supplies no residue map by itself. This entry
constructs the minimal coefficient family in which a residue object is
canonically typed.

## Frozen Kummer family

Replace the fixed \(q_{g1}\)-weight by a parameter \(\lambda\):

\[
\nabla_\lambda
=
\nabla_0+\lambda\,d\log q_{g1}.
\]

In a normal coordinate \(q=q_{g1}\), the logarithmic normal complex over
\(R=\mathbb Q[\lambda]\) is

\[
\boxed{
N_\lambda=[R\xrightarrow{\lambda}R].
}
\]

Its Smith factor is \(\lambda\), so

\[
H(N_\lambda)=R/(\lambda)
\]

in one cohomological degree. The supported normal object therefore lives on
the resonant coefficient divisor

\[
\boxed{\lambda=0.}
\]

At the generic census value \(\lambda=17\), multiplication by \(17\) is
invertible over the tested field and the normal complex is acyclic. Thus the
generic rank increment \(12-7=5\) cannot be interpreted as a supported
residue fiber at \(\lambda=17\).

## Special fiber and the doubled grade

Derived specialization to \(\lambda=0\) gives

\[
N_\lambda\otimes_R^L R/(\lambda)
=
[\mathbb Q\xrightarrow{0}\mathbb Q].
\]

There are two adjacent normal grades. If the tangential wall object has rank
five, the complete derived special fiber has total rank ten, while either
ordinary residue grade has rank five:

\[
\boxed{
5\oplus5.
}
\]

No canonical truncation selecting one copy has yet been constructed. Such a
selection must come from the physical extension, integration-chain boundary,
or a declared perverse/nearby-cycle convention; choosing it merely to match
the census would be post hoc.

## Consequence

The corrected architecture is

\[
\text{generic deletion rank difference}
\quad\leadsto\quad
\text{candidate tangential rank},
\]

but

\[
\text{actual supported residue object}
=
\text{Kummer nearby object at }\lambda=0.
\]

This is a coefficient-space nearby-cycle mechanism over the unchanged
energy/Cut carrier. It supports H2's shared-calculus thesis while withdrawing
the stronger claim that the generic deletion cube already realizes the
Gysin map.

The next falsifier is to construct the tangential rank-five complex
independently at \(\lambda=0\), then determine whether the physical relative
chain canonically selects one of the two normal grades and intertwines it with
the resolved boundary packet of Entry 549.

The executable audit is
`research/benincasa/marici-gm/src/bin/generic_lower_kummer_resonance.rs`.
