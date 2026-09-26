# Every abstract schedule terminates, with exact work accounting

ResolutionNetTermination.agda extends the checked local calculus without changing its rules. Fresh safe Cubical Agda checking proves five new facts for arbitrary package and rule types:

1. step-work: every permitted contextual rewrite decreases pending work by exactly one.
2. all-schedules-terminate: every term is accessible under the forward rewrite relation, ruling out infinite internal reduction paths.
3. path-work: initial work = path length + remaining work for every finite path.
4. exact-complete-length: every path ending in a Finished term has exactly the initial work length, independent of scheduling.
5. progress: every term is Finished or has a typed next rewrite. Thus incomplete structural work cannot be a stuck normal form.

The proof defines work(keep d)=0, work(pending d)=outer-size(d), with additive work beneath binary constructors. Outer size stops at seed boundaries; the pure history stored inside a seed is not re-executed. Unary and binary propagation consume exactly the current outer constructor. Accessibility is proved by recursion on the natural-number work budget, not by selecting a preferred scheduler.

This upgrades the earlier written termination argument to a checked abstract theorem. The prior semantic-preservation proof applies to every finite path, so all complete schedules preserve the same full interpreted history and have equal rewrite counts. It does not alone identify raw operational terms or receipt chronologies.

Reproduce: python research/voevodsky/resolution-net-v1/check_agda_termination.py. Results: results/agda-termination.json and agda-termination.log; checks use --ignore-interfaces with --safe --cubical --guardedness. Source hashes include the imported local-simulation module and original Nima closure.

Limits: exact rewrite count is not wall-clock complexity; current Python validation and candidate copying traverse full nets. The theorem concerns fixed abstract pending terms, not an environment that keeps generating new requests. It does not supply missing external evidence, a liveness/fairness guarantee for arrivals, or global commitment. Most importantly, a concrete Python port state has not yet been formally represented as one of these indexed terms.

Remaining part of the previous combined leaf: define an explicit concrete-port-to-term representation and check each actual wire rewrite against the corresponding abstract step. Start with closed admitted trees, including pure subnets abstracted by keep; avoid collapsing a semantic equality into an unjustified single-step simulation. That is now the next focused branch.
