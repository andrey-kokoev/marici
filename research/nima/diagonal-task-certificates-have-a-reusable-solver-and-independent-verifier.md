# Diagonal task certificates have a reusable solver and independent verifier

## Deliverable

The fixture-specific feasibility logic is now a reusable exact-rational engine, with a separate verifier that does not import or execute the solver.

Supported problem: real source coefficients, positive diagonal calibration intervals, real data intervals, one weighted l1 budget, and an exact linear target tested against a strict threshold.

Outcomes are TARGET_TRUE, TARGET_FALSE, AMBIGUOUS, INFEASIBLE and UNRESOLVED. Every substantive conclusion carries independently checkable evidence. The model is deliberately limited: it is not an arbitrary sensor-matrix solver or a reconstruction of intrinsic observer-module data.

## 1. Exact input and certificate contract

A versioned JSON problem specifies

`d_i in [l_i,u_i]`, `d_i=E_i x_i`, `E_i in [e_i,f_i]`, `e_i>0`,

`sum_i w_i |x_i|<=B`, `w_i>0`,

and the target `sum_i t_i x_i > threshold`.

Every numerical input is a rational STRING. JSON floating-point values are rejected. The current implementation supports 1 through 64 coordinates. Calibration intervals enclose fixed physical parameters; they are not assumed independently adjustable in nature.

A SHA-256 digest of the complete problem binds each certificate to its inputs. This is an input-integrity check, not an authentication mechanism or proof that the acquisition and calibration assumptions are true.

Implementation:

- `research/nima/certificates/diagonal_task_solver.py`
- `research/nima/certificates/verify_diagonal_task.py`

Both use only the Python standard library.

## 2. What the independent verifier proves

### Feasible witnesses

Each supplied source vector must satisfy the budget and the data constraints at BOTH endpoints of every positive calibration interval. Since the prediction is affine in E_i, this verifies compatibility for every calibration value in the enclosure, including the actual correlated calibration.

This robust witness condition is sufficient, not necessary. A feasible physical source can remain unproved when the calibration enclosure is too broad.

### Infeasibility

The verifier independently constructs the outer coefficient interval from the four endpoint quotients. Its weighted minimum absolute value is a necessary source cost. A claimed contradiction is accepted only if the exactly recomputed sum exceeds B.

### Universal task bounds

For a nonnegative rational multiplier lambda and an outer box [a_i,b_i],

`sum_i t_i x_i
 >= sum_i min_(u in [a_i,b_i]) [t_i u+lambda w_i|u|]-lambda B`.

Each scalar minimum is attained at an endpoint or at zero when zero is in the interval. The verifier recomputes this bound exactly. It does not need to trust how the solver chose lambda, or whether that choice was optimal.

A lower bound strictly above the threshold certifies TARGET_TRUE. Applying the same inequality to -t proves TARGET_FALSE when the resulting upper bound is at most the threshold. BOTH statuses additionally require a feasible witness, preventing conclusions based on an empty feasible set.

### Ambiguity

Two robust source witnesses must satisfy the same problem. One satisfies the strict target; the other does not. This directly proves that the declared data and assumptions cannot settle that target.

### Unresolved

UNRESOLVED asserts no substantive conclusion. It is not evidence of physical ambiguity or a claim that every possible proof procedure must fail.

## 3. Solver strategy, separate from certificate validity

The solver forms outer coefficient boxes for universal bounds and inner boxes whose members fit all calibrations. It constructs low-cost witnesses and optimizes linear targets on the inner boxes by a rational greedy budget allocation.

For universal bounds it searches nonnegative multipliers drawn from zero and the finitely many ratios |t_i|/w_i. Even if this search were improved or replaced, the same independent verifier would validate the resulting evidence.

The solver never promotes a failed outer bound to an ambiguity claim. It needs actual opposing witnesses. It likewise never promotes a low necessary budget cost to feasibility.

## 4. Held-out algebraic validation and adversarial checks

The test run covers 400 seeded generated interval problems that were not the motivating physical fixtures:

- 300 exact-calibration cases are also checked against exhaustive rational vertex enumeration in dimensions one through three;
- 100 uncertain-calibration cases exercise conservative interval outcomes;
- all 400 certificates pass the separate verifier;
- 875 deliberately corrupted digests, dual values or source witnesses are rejected.

The generated statuses include all five supported outcomes. These are algebraic tests, not statistical evidence of experimental performance.

The vertex oracle uses a different optimization method from the solver. The certificate verifier itself imports no solver code and does not run either optimization routine.

## 5. Adapter for the existing vacuum acquisition problem

The saved physical-source fixtures are mapped to four variables:

1. the local retained coefficient a_0;
2. b_2;
3. b_3;
4. the aggregate unacquired vacuum tail from A>=4.

The fourth variable is explicitly labelled as a PRIOR-BOUNDED AUXILIARY VARIABLE, not as an acquired reading. Its weight is 8*2^12. The triangle inequality gives this necessary tail cost; a finite source at A=4 realizes an auxiliary coefficient in a witness. The unused crossed coefficient may be zero, which fits its original interval. Other unobserved source coefficients can only consume budget.

The refined actual E_0 enclosure is imported conservatively as exact rational endpoints from its certified printed ball. The rational verifier does not re-prove completed-theta analysis; that enclosure and the source embedding remain separately justified inputs.

The engine reproduces all 29 saved vacuum outcomes:

- 19 TARGET_TRUE;
- 4 AMBIGUOUS;
- 6 INFEASIBLE.

This adapter certifies the vacuum-sum target. The residual positivity guarantee remains the independently established baseline result; the engine does not silently absorb uncertain residual target coefficients into its exact-target model.

## 6. Reproduction and independent use

Run all generated tests and physical adapters:

`python research/nima/checkers/check_diagonal_certificate_engine.py`

Solve a saved problem:

`python research/nima/certificates/diagonal_task_solver.py research/nima/results/diagonal-task-example-problem.json`

Verify the independently saved example certificate:

`python research/nima/certificates/verify_diagonal_task.py research/nima/results/diagonal-task-example-problem.json research/nima/results/diagonal-task-example-certificate.json`

The test run saves complete problem/certificate bundles in:

- `research/nima/results/diagonal-task-held-out-certificates.json`
- `research/nima/results/diagonal-task-physical-certificates.json`

Summary: `research/nima/results/diagonal-certificate-engine.json`.

## 7. Boundary of the deliverable

The engine verifies conditional mathematical claims. It does not certify that measurements were performed, that a source prior is appropriate, or that a calibration enclosure is analytically valid without its external proof.

It does not handle arbitrary mixed observation matrices, uncertain target coefficients without an explicit reduction, complex source coefficients, or optimal acquisition costs. Nor does it infer the source algebra, ideal action, relative boundary or source-calibrated derived comparison from state values.

Within its declared model it now provides a stable evidence format and a separate checking boundary. Acquisition planning can build on those certificates rather than treating a fixture-specific script's success flag as the conclusion.
