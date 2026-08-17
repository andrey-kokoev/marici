---
id: 389
date: 2026-08-17
title: The Connector Equation Requires a Physical Realization Functor
---

# The Connector Equation Requires a Physical Realization Functor

Entry 388 reduced the \(D_{03}\) endpoint problem to existence. If one
admissible connector exists, its endpoint-relative deformation torsor is
trivial, so its coefficients, homotopy class, and reflection parity are forced.
This entry identifies the first datum needed even to pose that existence
problem in one category.

## The two sides presently live in different models

The geometric exceptional input is the raw, unlocalized \(q^!\) object.
Entries 363 and 367 show that its interval contribution contains a
localization-dual telescope and is not perfect. It also retains the exceptional
\(x_4\)-supported sector isolated in Entry 370.

The target used by the successful cap and trace calculations is instead the
independently constructed finite physical PC/Rees packet. Entry 377 gives on
that packet the unique positive cap
\[
  \operatorname{cap}^{PC}_{176}
  =\operatorname{cap}_{\rm norm}\otimes
    \operatorname{pur}^{PC}_{x_3,\partial}.
\]
This packet is finite perfect; its physical support projection has removed the
telescope tail and the \(x_4\) sector.

Consequently the two objects cannot simply be declared isomorphic, nor related
by an equivalence: perfectness is invariant under equivalence, and the
localization-completion tail is present on only one side.

## What is actually missing

Before solving
\[
 d_{\operatorname{Hom}}h
   =\iota_{\rm road}a\pi-\delta_E\Phi ,
\]
one must construct a support-directed realization
\[
 \operatorname{Real}_{\rm phys}:
   (q^!_{\rm raw})_{\text{selected }D_{03}\text{ support}}
   \longrightarrow Q^{PC/Rees}_{03,\partial}.
\]
It must be nonconservative: it has to kill the localization-completion
telescope and the \(x_4\) exceptional sector. Simultaneously it must preserve
the generic \(q_{03}^{Q}\) leg, the positive \(x_3\)-Cartier symbol, incidence
differentials, both endpoint restrictions, and the \(D_3\) action.

Only after these properties are supplied do
\(\iota_{\rm road}a\pi\) and \(\delta_E\Phi\) become comparable morphisms in a
single mapping complex. At present the connector equation is therefore
**untyped**, not inconsistent.

## Consequence

Connector nonexistence has not been proved. The remaining frontier is:

1. define \(\operatorname{Real}_{\rm phys}\) on the raw support generators;
2. prove that it kills exactly the two unwanted sectors;
3. verify its chain, endpoint, and \(D_3\)-equivariance squares;
4. transport the frozen right-hand side into the finite PC mapping complex;
5. solve the now-typed connector equation.

The executable audit is
research/voevodsky/check_d03_connector_category_gate.py.
