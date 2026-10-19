# Coefficient-valued first-simple-root successor — 2026-10-13

## Explicit change of realization class

The single rational-seed admission test failed for the retained F0 candidate. This successor therefore proposes a different, explicitly coefficient-valued differential-form class; it does not relabel F0 as an ordinary canonical form or resolve the original net gate.

Let omega_F be the ordered eight-dlog form of the transported F chart. Over the rational function field of external spinor/dual kinematics, on the source-defined nonsingular localization, define

    omega_0 = c omega_F,
    omega_B = (1-c) omega_F.

The coefficient c is fixed by the external-versus-transported endpoint rule, not fitted to a desired residue. Then omega_0+omega_B=omega_F as an identity in this proposed module.

Source authority supplies the endpoint operation and rational superfunction factor. It does NOT yet supply a component-extraction/target map identifying these differential forms with F0 and its correction. Accepting the coefficient-valued extension as the intended weighted canonical descent is a separate specification/admission, not an implication of this construction.

## Symbolic coefficient and localization controls

For the source fixture family with symbolic parameter t,

    lambda_j = (1,j^2+j+1+t*j),
    tilde-prefix_j = (1,j^3+2*j+1+t*j^2),

momentum-conserving completion and the exact endpoint formula give

    c(t) = 3(t+3)(t+10)(18t^2+217t+639)
             / [2(7t^2+77t+183)(11t^2+156t+489)].

The numerator and denominator are coprime. The denominator has four simple complex-root poles; the two quadratic pole discriminants are positive. This extends the previous three-fixture nonconstant-ratio control to a symbolic rational slice.

The receipt retains all four raw endpoint factors before cancellation. Reducing c does not remove generalized-R source exclusions: all original denominator/localization conditions must still hold. Slice poles and zeros are not identified as positroid boundaries or physical factorization divisors.

## Residue contract: two conventions must not be conflated

1. **External coefficient fixed during a source-chart residue.** If residue is in alpha and c is a regular external parameter, Res_alpha(c omega)=c Res_alpha(omega). This is the tensor-module convention of the proposed source form.
2. **Coefficient realized as a target/local-normal function.** This requires an explicit map that is currently absent. If c is regular in normal z, restrict c to z=0. If it has poles, compute Laurent cross terms instead of scalar restriction.

Exact local model:

    omega = (b_minus1/z+b0+b1*z) dz wedge eta,
    c = c_minus1/z+c0+c1*z.

Then

    Res(c omega) = (c_minus1*b0+c0*b_minus1) eta.

The naive c0 Res(omega) misses c_minus1*b0. A pole in c can create a residue even where omega is regular. In general use sum_{i+j=-1} c_i b_j. Higher-order poles can also take the product outside the logarithmic-form class.

The split c omega+(1-c)omega recombines, including opposite Laurent corrections. This tautological recombination for one parent form is NOT cancellation between different histories or proof of nine-facet descent.

## Verification and failed implementation control

The exact checker passes ten controls: symbolic endpoint ratio, original three fixtures, coprimality, squarefree four-pole denominator, regular restriction, pole correction, orientation reversal, regular split recombination, pole split recombination and new residue on a regular form.

An initial squarefree test incorrectly required polynomial gcd(D,D')=1 including integer content; it failed because the denominator's constant content is a unit over Q. The corrected test checks degree zero of that gcd. No coefficient formula, candidate class or scientific criterion was changed to obtain a pass.

Run:

    python research/benincasa/checkers/check_simple_root_coefficient_form_successor.py

Receipt: `research/benincasa/results/simple_root_coefficient_form_successor.json`.

Verification is symbolic one-parameter kinematic algebra and formal Laurent residue algebra, not a full positive-atlas replay, kernel proof or physical-boundary classification.

## Net disposition and next test

The original `untransported-simple-forms` node remains open. A coefficient-valued successor is now specified with source-fixed c and nontrivial residue controls. No broader multi-cell witness or ordinary canonical admission was constructed.

Next: supply a typed target/component extraction map and decide, for an actual boundary route, whether c is fixed externally or pulled back as a local-normal function. Verify its localization and resulting residue. The missing full source bundle remains an operational gate for the final eighty-facet comparison. If that map cannot yet be sourced, the independent composite-normalization task remains the ready alternative; arbitrary fitted coefficients cannot replace it.
