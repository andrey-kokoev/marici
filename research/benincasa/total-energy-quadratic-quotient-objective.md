# Total-energy second grade to the quadratic Cayley–Menger quotient

## Bounded question

Does the frozen source define a transport-invariant linear map from the total-energy second Rees grade

\[
\operatorname{gr}^{(2)}_{E_T}
\]

to the one-dimensional quadratic quotient isolated by Ledger 2554?

## Source gate

The map must be derived from the relation between the generic labelled normals

\[
\nu_i=P_i^2-X_i^2
\]

and the homogeneous total-energy deformation. Matching one-dimensional ranks, choosing \(\nu_1^2\) as a convenient representative, or fitting the known coefficient \(-8p\) is inadmissible.

The four kinematic backgrounds `A`, `B`, `HOMA`, and `SOFT1` remain separately labelled. Any proposed map must commute with admitted source transports between presentations.

## Predeclared branches

1. **Invariant nonzero.** The total-energy second grade maps nontrivially to the quadratic quotient in every admitted background and transport square.
2. **Invariant zero.** The source-derived map exists but kills the total-energy second grade.
3. **Background dependent.** Candidate values exist but fail transport invariance; no coefficient morphism descends.
4. **Untyped.** The frozen source supplies no map between these normal systems.

No fifth branch may be introduced after inspecting \(\mathcal Q\).

## Acceptance tests

- derive the normal-coordinate Jacobian through second order;
- preserve the three labelled \(\nu_i\) directions;
- project using the quotient relations, not a chosen scalar representative;
- test all four backgrounds separately;
- verify source-transport commutation;
- export the smallest kernel, transport defect, or missing datum if the map fails.

## Optionality-space snapshot

- open branches: 4;
- source-admissible branches: 4;
- constructed canonical maps: 0;
- passed coherence tests: 0 of the above 5 declared tests;
- unresolved missing datum: the second-order source coordinate map;
- established dimensional reduction: ten normal labels map to a rank-four image with a one-dimensional quadratic quotient beyond first order.

## Activation observation

- topic: total-energy-to-quadratic quotient comparison;
- phase: pre;
- excitement: 8/10;
- confidence: 5/10;
- expected information gain: 9/10;
- immediate reason: the rank-four compression makes the comparison finite and unique if typed;
- confound: contrast with the recently terminated non-telemetric Gröbner run may inflate activation;
- epistemic status: process observation, not evidence.

## Tested disposition

Branch 4 survives:

\[
\boxed{\text{the reverse map is untyped without a source-derived splitting}.}
\]

Ordinary pullback along the homogeneous family is canonical and zero because

\[
P_i=X_i\quad\Longrightarrow\quad \nu_i=0
\]

identically, in every positive normal grade. A transverse lift

\[
P_i=X_i+\alpha_i\tau
\]

instead gives

\[
[\tau^2](\nu_i\nu_j)=4\alpha_i\alpha_jX_iX_j.
\]

The arbitrary \(\alpha_i\) are not supplied by the homogeneous source. The resulting ambiguity remains nonzero after projection through Entry 2554's actual one-dimensional quadratic quotient at all four labelled backgrounds. Therefore neither dimension matching nor the known second-order coefficient of \(\mathcal Q\) defines the missing reverse map.

Checker: `research/benincasa/checkers/check_total_energy_quadratic_quotient_typing.py`.

Packet: `research/benincasa/results/total-energy-quadratic-quotient-typing.json`.

## Post-objective optionality delta

- open branches: 1 of 4;
- branches eliminated: invariant nonzero, invariant zero reverse map, and background-dependent descended map;
- surviving branch: absent source typing;
- canonical maps constructed: one ordinary pullback, with value zero on every positive transverse grade;
- reverse comparison maps constructed: 0;
- declared checks passed: 5 of 5;
- unresolved missing datum: an independently derived splitting of the conormal transitivity sequence;
- dimensional reduction retained: the transverse quadratic quotient remains one-dimensional, but is not selected by total energy.

## Post-activation observation

- topic: total-energy-to-quadratic quotient comparison;
- phase: post;
- excitement: 8/10;
- confidence in the surviving untyped classification: 9/10;
- realized information gain: 9/10;
- immediate reason: the obstruction survives the actual quotient at every labelled background;
- confound: the result is algebraic/source-typing evidence, not physical-cycle evidence;
- epistemic status: process observation, not evidence.
