# Next bounded mathematical test: finite-sample interval certification

Scope: mathematical repeated-trial model only. Hardware construction, acquisition and apparatus authority are excluded from this work item, per operator request; no physical gate is thereby proved.

Inputs: the completed six-interval, three-probe response table in `interval-cavity-probes.md`. For each of three ports observe independent Bernoulli reference and validation trials with probabilities b_k=a_k and c_k=a_k*t_k, where t_k is 9/25 or 1 according to a canonical interval, and static factors satisfy a_k>=1/5. All trial outcomes and fixed sample counts are retained. Assume independent freshly prepared trials, shared reference/validation factors and no drift. Do not assume independence between estimated ratios to obtain simultaneous coverage.

Test to construct: at confidence 1-alpha, alpha=1/100, derive simultaneous bounds for all six rates by a stated concentration theorem and union bound. Select a fixed sample size before trials sufficient to obtain absolute rate error epsilon<=1/100 (a conservative bound is acceptable). Propagate positive reference denominators into ratio intervals. Report an interval only when the confidence region is compatible with exactly one of the six canonical response vectors; otherwise abstain. Reject impossible/out-of-domain data or distinguish model inconsistency from ambiguous identification. Do not use point estimates as certificates.

Acceptance: prove probability of an incorrect certified interval <=alpha under the stated model, normalization and stopping rules; compute the fixed sample count; demonstrate unique identification for every interval on the simultaneous good event using the existing ratio separation bound. Exact or outward-rounded arithmetic must prevent a rounding-induced loss of coverage. Test all six interval patterns, boundary efficiency, ambiguous counts, zero reference counts, invalid counts, incomplete records and deliberately violated shared-factor assumptions. Simulations, if used, are regression tests rather than proofs of coverage.

Falsifier: exhibit a model-admitted confidence region that certifies the wrong interval on the good event, a failure of uniform separation at the frozen bounds, or an invalid concentration/ratio/stopping argument. Drift examples refute extension beyond the stated model, not its conditional theorem. Stop after one focused proof/checker/review cycle; if unresolved, record inconclusive rather than changing assumptions to force success.

Dependencies: completed conditional three-probe theorem. This is not a prerequisite for, or a solution of, the causal-orientation conjecture. No laboratory inverse controls are dependencies.

Planning estimates: subjective, uncalibrated assistant estimates (accepted, rejected, inconclusive)=(0.8,0.1,0.1); effort=1 focused cycle. These are planning inputs, not theorem probabilities or a claim that this is the globally best research direction.
