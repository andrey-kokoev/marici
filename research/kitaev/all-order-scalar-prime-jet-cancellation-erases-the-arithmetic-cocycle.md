# All-order scalar prime-jet cancellation erases the arithmetic cocycle

## Question

Can one cancel every divergent central jet of the finite-prime transition in
one scalar channel while retaining the arithmetic constructor data?

## Analytic all-order cancellation

Let (gamma_X) be holomorphic and nonzero near (s=1/2), normalized by

\[
\gamma_X(1/2)=1.
\]

Let (ho_X) be a holomorphic nonzero counterterm and set

\[
\Gamma_X=\rho_X\gamma_X.
\]

Suppose the renormalized transition satisfies

\[
\Gamma_X(1/2)=1
\]

and

\[
\Gamma_X^{(n)}(1/2)=0
\qquad
n\ge1.
\]

Its Taylor series is constant. By the identity theorem,

\[
\Gamma_X\equiv1
\]

on the connected local domain. Therefore

\[
\rho_X=\gamma_X^{-1}.
\]

The unique analytic counterterm cancelling every jet is the inverse of the
entire transition.

## Erasure theorem

The scalar output (Gamma_X=1) contains none of the primitive, square, or
higher valuation grades carried by (gamma_X). Full scalar jet cancellation
is exact arithmetic-cocycle erasure.

This is not a defect in the algebra. It is a typing fact: a quotient that
removes every response of a constructor also removes the constructor from
that output.

Therefore the all-orders scalar-normalization route cannot simultaneously
claim:

1. a completely flat renormalized transition;
2. retention of the finite-prime arithmetic incidence in that same scalar.

## Lossless extension

Let

\[
L_X=\log\gamma_X
\]

on the normalized local branch. A lossless renormalized packet is

\[
\mathcal R_X=(\Gamma_X,L_X).
\]

In the fully flattened frame,

\[
\mathcal R_X=(1,L_X).
\]

The original transition is reconstructed by

\[
\gamma_X=e^{L_X}.
\]

Reflection acts by

\[
L_X(1-s)=-L_X(s),
\]

and cutoff composition is additive:

\[
L_Y=L_X+L_{X,Y}.
\]

Thus the counterterm history is an additive reflection-odd port attached to
the normalized scalar line.

## Minimality

If downstream constructors require only the original scalar transition, the
complete function (L_X) is sufficient for reconstruction. If they require
labelwise primitive and square incidence, (L_X) must remain grade-labelled
rather than aggregated into one unlabelled function.

The minimal port therefore depends on the declared constructor family:

- aggregated logarithmic transition for scalar reconstruction;
- graded logarithmic coordinates for valuation-current reconstruction;
- full ordered Euler history for noncommutative or route-sensitive actions.

Renormalization does not determine which quotient is authorized.

## Completion problem

The raw (L_X) jets diverge, so merely adjoining (L_X) does not solve the
topology. A valid completion must split

\[
L_X=C_X+L_X^{\rm ren}
\]

where (C_X) is a source-derived divergent odd connection and
(L_X^{\rm ren}) converges in the declared topology. The packet must retain
enough of (C_X) or its provenance to reconstruct every admitted current.

The split requires a cocycle law. Fitting (C_X) independently at each
cutoff destroys composition authority.

## Architectural meaning

The normalization port is not a residue bin appended after scalar closure.
It exposes the constructor history required to compose normalized objects.
This is an explicit instance where the additional tower adds composition
capability rather than merely repairing a lower tower.

## Falsifier certificate

    {
      "code": "all_order_scalar_renormalization_erases_arithmetic_cocycle",
      "all_central_jets_cancelled": true,
      "renormalized_transition": 1,
      "counterterm": "gamma_X^{-1}",
      "arithmetic_history_port_retained": false,
      "lossless_reconstruction": false
    }

## Disposition

All-order analytic cancellation in one scalar channel necessarily trivializes
the finite-prime transition. A lossless completion must retain a separate
reflection-odd, cutoff-additive counterterm or constructor-history port.

## Claim boundary

This theorem is local and analytic near the central point. It does not
construct the convergent split (L_X=C_X+L_X^{\rm ren}), determine the
minimal labelled history required by the theta/Tate source, or prove bounded
reconstruction after completion.
