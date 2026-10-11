# Incidence-derived response on the 1836-arrow structure

## Question

Can the retained arrow structure select the response stiffness D and coupling g that were inputs to the shared-environment closure model?

## Source and explicit interpretation

Layer1 in `agda/TypedGeneratorLayers.agda` supplies a state type, witness family and generator. It does not supply a real inner product, energy functional or stiffness scale. The source for this bounded test is instead the existing, explicitly enumerated geometric witness graph in `results/twelve-triangle-1836-arrows.json`: 108 stage-typed ports and 1836 arrows. No new WG derivation of that graph is claimed.

Give each arrow the unit cost already used in the arrow count and let B be its signed incidence matrix. The candidate response is

    D = B B^T,
    x^T D x = sum_(arrows a->b) (x_b-x_a)^2.

This is an explicit unit-metric interpretation of witnesses. It uses their endpoints, not their complex transport coefficients. It is not forced by WG's type signature.

## Derived obstruction and neutral completion

The graph is connected. The sum-of-squares identity implies that D has precisely the constant vectors as its kernel. Every response source J=D x must therefore have sum zero. Positive isolated profiles, and the previous same-sign pair profile, cannot satisfy this equation on the closed graph.

For a neutral test, put source +1/36 on each raw port and -1/36 on each aligned port, with zero local source. This uniform layer fixture is not the nonuniform fine-coordinate eigenmode intensity. The following response solves all 108 equations exactly, up to a common additive constant:

| Stage | Response |
|---|---:|
| raw | 5/6912 |
| local | 1/6912 |
| aligned | 0 |

The three stage conductances are the existing counts 108, 432 and 1296. Eliminating the middle stage gives

    C_eff = 1296 + (108*432)/(108+432) = 6912/5,
    J^T x = 5/6912.

At fixed source, minimizing x^T D x/2 - J^T x gives -5/13824. These are unit-metric response values, not masses. This is a neutral-pair response, not a binding difference: isolated charged responses do not exist on the same closed graph, so the previous inclusion-exclusion subtraction is not yet available.

## Rival and scale test

The earlier model used a positive definite D and could invert arbitrary sources. The incidence construction has a mandatory zero mode; silently adding an identity stiffness would change the model. A boundary reservoir or compensating surrounding source is needed to compare isolated and paired configurations in one consistent setting.

The same witness graph also admits 2D. It gives half the response for the same J. Likewise changing the source coupling scales the eliminated energy quadratically. Thus arrow incidence alone does not fix an absolute stiffness or g. This is an explicit normalization ambiguity, not a failed numerical solver.

## Disposition and verification

We obtained an incidence-derived candidate operator and a neutral response, rather than deriving the previous invertible operator by assumption. The first missing data are the boundary/reservoir completion and the metric/coupling normalization. Their source must be specified before a proton-versus-composite energy difference can be calculated.

`python research/nima/checkers/check_wg_incidence_environment.py` passed via structured-command execution `structured_command_execution:e_32876_1791216804672459500_9`. Checks cover source counts, connectedness, sum of squares, all 108 response equations, constant-shift invariance and stiffness-rescaling sensitivity. Results: `results/wg-incidence-environment.json`, including the exact source SHA-256. No commit, publication or new formal Agda theorem is claimed.
