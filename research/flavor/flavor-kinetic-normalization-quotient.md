# Kinetic-normalization quotient of the mediator lift

Work package: WP989  
Owner: marici.Figueiredo

## Question

What is the faithful physical quotient of the WP985/WP986 coefficient packet
once the undeclared kinetic normalizations of the WP977 mediators are exposed?

## Admitted domain

Use the labelled positive coefficients

\[
x=(\log\Gamma,\log A,\log B,\log C),
\]

where \(\Gamma\) multiplies \(s\det A\), \(A\) multiplies the cubic
adjoint entrance, and \(B,C\) are the scalar and adjoint quadratic
coefficients. WP977 declares their potential but no kinetic coefficients.

Introduce positive kinetic normalizations \(Z_s,Z_A\). Canonical
normalization acts on \(x\) with tangent generators

\[
n_s=(-1/2,0,-1,0),\qquad
n_A=(-3/2,-1/2,0,-1).
\]

These are presentation changes of the same canonically normalized theory, not
distinct physical source points.

## Exact quotient theorem

The determinant response row

\[
r_0=(2,4,-1,-5)
\]

satisfies \(r_0n_s=r_0n_A=0\). Thus the response descends through kinetic
normalization, explaining why the combined coefficient was well defined even
though its individual factors were not.

The normalization generators are independent, so the faithful quotient of the
four-dimensional labelled tangent packet has dimension two. The three WP986
coordinate rows \(e_\Gamma,e_B,e_C\) each fail descent.

The annihilator of the normalization orbit is two-dimensional. Besides
\(r_0\), one exact independent invariant row is

\[
r_1=(0,2,0,-1),
\]

corresponding to the canonical ratio \(A^2/C\). The two-row matrix has rank
two on the quotient. Therefore:

- the measured determinant response leaves one physical quotient direction
  unresolved, not three;
- exactly one additional invariant scalar channel is minimally necessary;
- three coefficient-labelled channels would over-resolve presentation data.

## Hostile pair

Changing \(Z_s\) or \(Z_A\) changes the apparent individual vertex and
mass coefficients while preserving both invariant rows. In particular, an
adjoint normalization change by four moves the apparent pole coefficient by a
factor four and the cubic coefficient by a factor two, while leaving
\(A^2/C\) fixed. Any proposed pole or vertex readout that distinguishes these
presentations without first fixing a physical normalization fails descent.

## Classification and instrument gate

This is a quotient correction, neither selector nor rigidifier. It reduces the
physical identification problem to one complementary invariant response. A
candidate instrument must measure a weak-basis-invariant realization of
\(A^2/C\), or another independent row in the same annihilator, with a declared
kinetic normalization and source-to-detector map.

The smallest falsifier is an admitted source term that physically fixes
\(Z_s,Z_A\) rather than treating them as field-coordinate choices, or a proof
that one of the normalization generators changes a measured S-matrix element.

## Reproduction

Run:

    python research/flavor/checkers/wp989_kinetic_normalization_quotient.py

The generated result is
research/flavor/results/wp989_kinetic_normalization_quotient.json.
