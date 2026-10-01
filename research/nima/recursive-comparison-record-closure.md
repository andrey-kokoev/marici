# Recursive closure of a reference comparison record

## One candidate law, used twice

A comparison record retains parallel maps C,d:A->B, their residual rho=C-d,
and its complete construction history. For composable records

    P=(C1,d1):A->U, Q=(C2,d2):U->B,

use the same constructor at every level:

    compose(P,Q)=(C2*C1, d2*d1):A->B.

The children remain attached. Its residual is forced by subtraction:

    rho_new = d2*rho1 + rho2*d1 + rho2*rho1.

This is an exact noncommutative identity. The mixed product is one term in a
reference-transported error law. Multiplying residuals alone omits both transport
terms. Equivalently, rho_new=C2*rho1+rho2*d1=d2*rho1+rho2*C1.

## Closure experiment

Supply four comparison records on a declared composable chain A0->...->A4.
Compose adjacent pairs, then compose the two results using exactly the same
constructor. The result retains four input records, composed endpoint types,
the composed reference, and the exact residual. No fresh reference is introduced
at the second application.

All five parenthesizations agree on actual map, reference and residual by
associativity. Their retained construction histories remain distinct. Agreement
C=d is preserved through both applications, including nonidentity references.
Changing basis at an intermediate object transports both actual and reference
maps and leaves the composite unchanged.

This establishes conditional recursive closure under composition. Each result
still represents maps between the original sorts of objects; tree depth increases
while cell degree stays fixed. A higher-cell interpretation requires another
constructor. This is a compositional control for the tower, alongside the selected
one-label-per-family promotion rule.

## Inputs that the current assembly does not supply

The actual137-slot composites and their direct reference all lie in Hom(A,B).
Two such records do not compose when A and B are distinct endpoint types.
Equal matrix dimensions do not identify those types. The checker rejects this
attempt. A composable network, a supplied transport, or a declared endomorphism
frame makes additional compositions possible.

At the primitive-leg level, generating the actual comparison y*x-d by this
constructor requires reference legs x0,y0 satisfying y0*x0=d. The independently
retained direct reference does not specify such a factorization. The checker
shows that an unmatched factorization changes the root residual even when the
actual composite is unchanged.

## What doubling measures

On a declared endomorphism object, repeatedly composing a record with itself
gives two and then four leaf occurrences. These can all refer to the same seed.
Four independently supplied composable records also give four occurrences, but
with different dependency data. Occurrence count or polynomial degree alone
therefore does not establish independent operand doubling or class-rank doubling.

## Cost and physical readout

The constructor determines no additive norm budget. For unit references and
errors H=E12, K=E21, the output error is H+K+KH. Its squared Frobenius norm is3,
while the input error norms sum to2. A retained metric, weighting or additional
resource account is required for a conservation or normalization statement.

## Synthesis outcome

The first closure experiment yields an exact associative, reference-aware law
and exposes the remaining interfaces: composability of the network, reference
factorization when starting from primitive legs, a type-ascending witness, and a
transported cost/readout. The next higher-cell construction should respect this
three-term propagation law and retain its mixed rectangle component. These are
concrete compatibility conditions for the intended family successor, rather than
a derivation of that successor from composition alone.

## Verification

    python research/nima/checkers/check_recursive_comparison_record_closure.py

Exact rational matrices: two recursive applications, all five bracketings,
agreement preservation, reference factorization controls, intermediate basis
covariance, endpoint rejection, repeated versus independent leaf identities,
noncommutative mixed terms and a norm-budget counterexample.
