# UV lift jet faithfulness

## Question

WP984 applies the cross-sector two-lift falsifier to the balanced WP983
coefficient packet. Let

\[
P=\frac{\Gamma^2A^4}{BC^5}
\]

be its normalized prefactor. A UV lift is a source-authorized deformation of
\((\Gamma,A,B,C)\) over a declared threshold coordinate \(\epsilon\).

The zeroth-order map remembers only \(P(0)\). Its logarithmic first response
is

\[
J_1
=2u_\Gamma+4u_A-u_B-5u_C,
\]

where \(u_X=X'(0)/X(0)\).

## Exact two-lift tests

A Gamma lift with \(\Gamma(\epsilon)=\Gamma(1+\epsilon)\) has normalized
response

\[
R_\Gamma(\epsilon)=(1+\epsilon)^2.
\]

An A lift with \(A(\epsilon)=A(1+\epsilon/2)\) has

\[
R_A(\epsilon)=(1+\epsilon/2)^4.
\]

They agree at zeroth and first order:

\[
R_\Gamma(0)=R_A(0)=1,qquad
R_\Gamma'(0)=R_A'(0)=2.
\]

They differ at second order:

\[
R_\Gamma''(0)=2,qquad R_A''(0)=3.
\]

Thus one threshold jet can distinguish some lifts but is not generally
faithful.

## No universal finite jet without a bounded grammar

For any fixed \(n\geq0\), compare the trivial lift with

\[
\Gamma_n(\epsilon)=\Gamma(1+\epsilon^{n+1}).
\]

Its normalized response is

\[
(1+\epsilon^{n+1})^2
=1+2\epsilon^{n+1}+\epsilon^{2n+2}.
\]

Every derivative through order \(n\) agrees with the trivial lift, while
order \(n+1\) differs. Therefore no fixed finite jet tower is jointly
faithful on an unrestricted analytic lift family.

This does not contradict finite Boolean tomography: that theorem assumes a
finite labelled source grammar. For flavor, finite threshold-jet authority
requires an independently bounded mediator grammar and a physical instrument
for every admitted jet.

## Consequence

The balanced low-energy coefficient does not identify its UV constructor.
Threshold jets refine the contextual quotient only relative to:

- a declared finite or degree-bounded lift domain;
- source-derived perturbation directions;
- full weak-basis descent;
- calibrated physical threshold instruments.

The smallest falsifier is a bounded source grammar whose complete authorized
jet family has zero contextual kernel on its UV lift domain.

## Reproduction

Run:

    python research/flavor/checkers/wp984_uv_lift_jet_faithfulness.py

The generated result is
research/flavor/results/wp984_uv_lift_jet_faithfulness.json.
