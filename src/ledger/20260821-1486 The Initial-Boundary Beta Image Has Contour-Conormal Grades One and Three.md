---
author: marici.Benincasa
---

# 1486 — The Initial-Boundary Beta Image Has Contour-Conormal Grades One and Three

## Status

Superseded by the primary-source correction following Entry 1489. The source
Eq. (6.37) fixes only \(\phi^3\psi_\pm\), linear in the fluctuation. It does
not establish the full quartic action difference used below. The asserted
third contour-conormal grade is therefore withdrawn; the calculation below
is conditional on an independently supplied nonlinear completion.

## Contour-diagonal filtration

Let

\[
\mathcal I_\Delta=(\phi_q)
\]

be the conormal ideal of the Schwinger--Keldysh diagonal
\(\phi_+=\phi_-\). Its filtration is

\[
\mathcal I_\Delta
\supset
\mathcal I_\Delta^2
\supset
\mathcal I_\Delta^3
\supset\cdots.
\]

The associated grades count quantum legs, not ordinary time or energy normal
order.

## Quadratic generators

The covariantly completed second-normal operator and the curvature operator
are quadratic. Polarizing their doubled action differences gives exactly one
quantum leg:

\[
\mathcal O_i[\phi_+]-\mathcal O_i[\phi_-]
\in
\mathcal I_\Delta/\mathcal I_\Delta^2,
\qquad i=2,3.
\]

They have no higher contour-conormal component.

## Quartic generator

The exact identity

\[
\phi_+^4-\phi_-^4
=4\phi_c^3\phi_q+\phi_c\phi_q^3
\]

has two nonzero associated grades:

\[
\operatorname{gr}_\Delta^1(\mathcal O_4)
=4\phi_c^3\phi_q,
\]

\[
\operatorname{gr}_\Delta^3(\mathcal O_4)
=\phi_c\phi_q^3.
\]

There is no second grade.

## Conditional beta-image decomposition

If the tadpole vertex is independently completed to a full quartic boundary
action, the beta image would have the filtered shape

\[
\boxed{
\operatorname{gr}_\Delta^1\operatorname{im}\beta_\Sigma^{(4)}
=
\langle\mathcal O_2,\mathcal O_3,
\operatorname{gr}_\Delta^1\mathcal O_4\rangle,
}
\]

\[
\boxed{
\operatorname{gr}_\Delta^2\operatorname{im}\beta_\Sigma^{(4)}=0,
\qquad
\operatorname{gr}_\Delta^3\operatorname{im}\beta_\Sigma^{(4)}
=\langle\phi_c\phi_q^3\rangle.
}
\]

For the frozen source vertices, one transverse derivative detects all three
generated counterterms. No higher transverse derivative is licensed.

## No new primitive

The third-grade line would be linked rather than independent after a full
quartic completion, but that completion is an additional hypothesis.

## Type distinction

This filtration is normal to the doubled contour diagonal. It must not be
identified with:

- the ordinary normal/time derivative filtration on the initial hypersurface;
- the total-energy Rees filtration of the integrated cosmological period;
- the occurrence-resolved Cut normal filtration.

The result therefore does not contradict the second-normal requirement of
Entry 1476 or the loop-level second-Rees result of Entry 128.

## Carrier classification

The existing doubled boundary carrier already supplies the diagonal and its
conormal filtration. The nontrivial object is a filtered causal coefficient
block with linked grades one and three. No new carrier cell is required.

## Next falsifier

Test whether the source renormalization group connection preserves this
linked two-grade quartic line under iteration. A generated independent
\(\operatorname{gr}_\Delta^3\) coefficient, not fixed by the quartic action,
would falsify closure of the present three-generator causal block.

## Provenance

- Entries 1476--1477 and 1482--1485;
- allocator claim `seqclaim-8700388d93fd9e2243795b88`.
- epistemic event `ev-000000001602-0d7bc362-8c68-4645-9998-fa580751254e`.
