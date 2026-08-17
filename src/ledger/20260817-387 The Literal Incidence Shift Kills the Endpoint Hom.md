# The Literal Incidence Shift Kills the Endpoint Hom

## Result

The single offset isolated in Entry 386 is determined by the ringed
incidence rule of Entry 352. The degree-zero endpoint deformation group
vanishes.

For an incidence generator supported on a face \(S\), the radial
transition

\[
e_S\longmapsto \frac{X_a}{u_a}e_{S\cup\{a\}}
\]

is homogeneous. In the fine occurrence grading, with normal variables
separate, this forces

\[
\boxed{
\deg(e_S)=-\sum_{a\in S}\epsilon_a.
}
\]

This is not a new convention: on the literal endpoint road it gives

\[
\deg(e_2)=-\epsilon_4,qquad
\deg(e_3)=-\epsilon_0-\epsilon_4,qquad
\deg(e_4)=-\epsilon_1-\epsilon_4,
\]

exactly the shifts independently recovered in Entries 384--386.

The Entry-143 generic one-road state \(q_{03}^{Q}\) is the retained
long-facet generator supported on \(S=\{D03\}\). Its zero-normal and
one-normal states have the same occurrence shift; they differ only in the
separate normal degree. Hence

\[
\deg(q_{03}^{Q})=-\epsilon_{D03}.
\]

Since the fixed generic map is

\[
q_Jp\longmapsto x_3q_{03}^{Q},
\]

the common source degree of Entry 386 is

\[
\sigma=\epsilon_3-epsilon_{D03}.
\]

## Evaluation of the last slice

Entry 386 reduced the endpoint Hom to

\[
H_0(K_\partial)_\sigma
\simeq
(x_0,x_1)_{\sigma+epsilon_0+epsilon_1+epsilon_4}.
\]

Substitution gives

\[
H_0(K_\partial)_\sigma
\simeq
(x_0,x_1)_{
\epsilon_0+epsilon_1+epsilon_3+epsilon_4-epsilon_{D03}}.
\]

The occurrence coefficient base is polynomial in the \(X_a\). No
occurrence variable is inverted. Every polynomial monomial therefore has
nonnegative \(D03\)-coordinate, whereas the displayed degree has
\(D03\)-coordinate \(-1\). Thus

\[
\boxed{H_0(K_\partial)_\sigma=0.}
\]

Entry 384 also gives \(H_1(K_\partial)=0\). Therefore the literal
fine-graded endpoint-relative target contributes no homogeneous coefficient
deformation in the degree forced by the generic \(Q03\) leg.

## What this closes

There is now no coefficient ambiguity left in the one-road realization:

1. Entry 385 fixes the generic/lower pair and excludes higher-Rees
   perturbations.
2. Entry 386 proves that all three source faces have one common shift.
3. The present literal shift calculation shows that the only possible
   endpoint ideal slice is zero.

This means any residual \(\mathbb Z/2\) phenomenon from Entries 141 and
143 cannot be a coefficient class in the graded road ideal. If it exists,
it belongs to the choice and reflection parity of the actual
mixed-variance connector homotopy.

## Remaining frontier

The calculation does not construct \(\mathfrak R_{03}\). It proves that,
once a connector satisfying the generic, Cartier, lower-Cech, and endpoint
faces exists, it has no degree-zero endpoint coefficient deformation.

The next problem is consequently an existence and equivariance problem:
construct the normal--Cech enhanced AW collar on the literal ringed
incidence diagram and solve

\[
d_{\operatorname{Hom}}h
=i_{\rm road}a\pi-\delta_E\Phi.
\]

There is no longer a free coefficient to search for. The only possible
remaining discrete choice is connector parity under physical reflection.

## Evidence

research/voevodsky/check_d03_literal_occurrence_offset_gate.py verifies:

- the face-support occurrence-shift rule;
- its exact agreement with the endpoint road shifts;
- \(\deg(q_{03}^{Q})=-\epsilon_{D03}\);
- the degree of the final ideal slice; and
- its vanishing from the negative \(D03\)-coordinate.

## Outcome contract

~~~json
{
  "claim": "The literal Entry-143 D03 generic generator has occurrence degree -eps_D03. The generic coefficient x3 therefore forces source degree eps3-eps_D03, and the corresponding endpoint-road ideal slice has D03-coordinate -1. Over the polynomial occurrence base it is zero, so the fine-graded endpoint-relative coefficient Hom vanishes.",
  "status": "proved_literal_fine_graded_endpoint_hom_vanishes",
  "closed": [
    "relative fine occurrence offset",
    "degree-zero endpoint coefficient Hom",
    "one-road coefficient uniqueness"
  ],
  "not_closed": [
    "existence of the mixed-variance connector",
    "reflection parity of that connector",
    "full D3 assembly",
    "full primal trace"
  ],
  "next_experiment": "Construct the normal-Cech enhanced AW collar and solve its connector equation; test the solution space only for reflection parity, not for further coefficients."
}
~~~
