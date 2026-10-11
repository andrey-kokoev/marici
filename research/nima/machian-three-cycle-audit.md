# Machian three-cycle reconstruction: the bootstrap factor is a possible return map

## Question

Recover the old proposed gravitational-constant construction as operations and witnesses, and determine whether cycle closure selects its coefficients. The old source is `checkers/check_machian_3cycle.py`, with related formulas in `checkers/check_constant_table.py`. Active obligation: typed composition and identity-return compatibility before any gravitational readout.

## What the source actually supplies

The script sets the four numbers (11,12,4,10) and computes k1=1/90 and k2=1/5280 from explicit rational expressions. It does not construct physical state spaces or native WG operations forcing those values. Its chirality/Sciama/back-reaction interpretations are prose attached to the formulas. The audit reads these expressions from the original AST and evaluates them exactly without executing the old claim-generating script or overwriting its artifacts.

A minimal scalar realization of the declared stages has arrows with gains

\[
L=1+\frac1{90}=\frac{91}{90},\qquad
R=1-\frac1{5280}=\frac{5279}{5280}.
\]

Arrows carry source/target stage tags, so mismatched composition is rejected. This realizes the quoted multiplicative arithmetic; it is not an independently generated physical WG cycle.

## State return versus a loop of stage labels

The old claim that a zero-correction return leg closes the cycle must distinguish returning to the same stage from returning the scalar state unchanged. With that third gain equal to one,

\[
RL=\frac{480389}{475200}\ne1,
\qquad RL-1=\frac{5189}{475200}.
\]

The zero input conceals this defect, but the unit input detects it. To make the full scalar loop the identity, the return gain must instead be

\[
C=(RL)^{-1}=\frac{475200}{480389},\qquad
C-1=-\frac{5189}{480389}.
\]

This supplies a coherent interpretation of the old multiplicative bootstrap Z: it can be the **compensating return arrow**, rather than the gain of the entire closed identity loop. The full gain C*R*L is one. Reading C as a physical scale correction still requires a rule selecting that leg and its normalization.

A nonidentity loop could instead describe holonomy. That is not an algebraic inconsistency, but then it must not be called an unchanged-state return. If scalar rescalings are quotiented projectively, amplitude/energy recovery requires additional retained scale data.

## The additive and multiplicative versions differ

The older constant table uses the additive denominator

\[
1+\frac1{90}-\frac1{5280}=\frac{16013}{15840}.
\]

It exceeds RL by 1/475200. The return increment needed to match that prescribed additive target is +1/480389, not the identity-return increment above.

Likewise, the old script computes epsilon_id_theory by dividing a prescribed series target by the first-two-leg product. This guarantees the chosen target by construction; it does not derive the target or establish identity return. The exact infinite tail of its displayed n>=3 series is 1/11880. The checker separately reproduces the finite n=3,...,19 compensation actually computed by that script.

## Does closure select the coefficients?

No: the triples of gains (91/90,5279/5280,475200/480389), (2,3,1/6), and (3/2,4/5,5/6) all have matched boundaries and exact identity return. In general the condition determines C=1/(LR) for any nonzero L,R. It does not select the first two maps, the exponent 15, the factor 12 or a physical mass scale.

For comparison only, retaining the old conditional hierarchy M_Pl=246*12*11^15*Z gives:

| Readout convention | Conditional M_Pl, GeV | Relative error in G versus the old reference |
|---|---:|---:|
| Additive inverse | 1.2198013344e19 | +0.1785785% |
| Two-leg product inverse | 1.2198038736e19 | +0.1781614% |
| Complete identity-loop gain 1 | 1.2331236596e19 | -1.9743316% |

The last row is a diagnostic replacement, not a proposed new physical formula. The old v=246 GeV and M_Pl reference 1.220890e19 GeV are supplied numerical inputs. No uncertainty or renormalization argument was computed that would explain these discrepancies. Assigning GeV to a pure count remains an additional scale identification.

## Disposition and verification

The old proposal contains an algebraically coherent candidate return factor, but its claim of an unchanged return with zero third correction is false in the explicit scalar interpretation. The reconstruction fixes this distinction without fitting new coefficients. It does not recover a derivation of G: source-defined left/right response maps and the physical scale/readout remain absent. That is the first missing construction, not a request for another fitted closure term.

`python research/nima/checkers/check_machian_three_cycle_audit.py` passed via `structured_command_execution:e_32876_1791229527041853800_55`. Results: `results/machian-three-cycle-audit.json`, including original-source digest, alternative closed cycles and exact discrepancies. No commit or publication is claimed.
