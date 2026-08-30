---
author: marici.Nima
---

# 1534 — The Second-Normal Mass Deformation Is the Even-Grade Shift Operator

## Status

Closed all-grade operator identity for the first invariant deformation away
from the physical mass diagonal.

## Generating function

Use the physical mean and invariant normal coordinates

\[
a=4\bar y^2,
\qquad
\tau=\delta^2=(y_1-y_2)^2,
\qquad
z=X^{-1}.
\]

The normalized double-Gysin jet is

\[
\boxed{
F(z,\tau)
=\frac{2}{(1-az^2)(1-\tau z^2)}.
}
\]

The physical equal-mass fiber is

\[
F_{\rm phys}(z)=F(z,0)=\frac{2}{1-az^2}.
\]

## Transverse operator

Differentiating in the first source-visible normal coordinate gives

\[
\boxed{
\left.\frac{\partial F}{\partial\tau}\right|_{\tau=0}
=z^2F_{\rm phys}(z).
}
\]

Thus the second-normal deformation acts on the physical infinity jet by the
even-grade shift operator.

Coefficientwise, for \(m\ge1\),

\[
\boxed{
\left.
\frac{\partial C^{(2m)}}{\partial\tau}
\right|_{\tau=0}
=C_{\rm phys}^{(2m-2)}
=2a^{m-1}.
}
\]

All odd grades remain zero.

## Meaning

The first unequal-mass correction is not an independent coefficient family.
It is canonically generated from the physical one-channel jet by shifting the
filtration two steps:

\[
\boxed{
N_{\rm mass}=z^2.
}
\]

This is the local extension operator carried by the ramified source map. The
normal coefficient object therefore has the form

\[
\text{physical jet}
\xrightarrow{\;z^2\;}
\text{second-normal jet},
\]

rather than two unrelated towers.

The result provides a finite algebraic model for a nearby-cycle or
Gauss–Manin extension in which the transverse deformation is determined by a
filtration-shift operator.

## Durable evidence

- research/nima/check_supercritical_infinity_jet.sage;
- Entries 1531–1532;
- allocator claim seqclaim-229fdc3c1f75a8ac6750410e.
