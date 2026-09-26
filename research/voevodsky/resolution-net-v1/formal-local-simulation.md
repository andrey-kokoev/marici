# Abstract local simulation is now Agda-checked

New module agda/ResolutionNetLocalSimulation.agda introduces a package-indexed operational syntax: keep(d) for a pure retained subnet, pending(d) for a flattening request over a pure nested resolution, and unary/binary reconstructed constructors retaining their actual rule witnesses.

Its three root rules are exactly the abstract F/seed, F/unary and F/binary transformations. Context rules allow a rewrite under any reconstructed unary/binary premise. Types enforce premise/output compatibility throughout, for arbitrary type-valued P,U,V,S, not merely string identifiers.

Fresh Agda --ignore-interfaces checking under --safe --cubical --guardedness proves:

* step-sound: every permitted contextual one-step rewrite preserves interpretation as a complete Resolve history;
* path-sound: every finite rewrite path preserves that interpretation;
* settle-path: every initial pending request has a constructively supplied rewrite path to settle(d);
* settle-finished: that target has no pending constructors;
* settle-correct: its interpretation is the original reference flatten(d).

No new postulates or holes. The reference closure is imported unchanged. Reproduce via check_agda_local_simulation.py; results/agda-local-simulation.json records source hashes and environment.

This advances beyond the previous substitution-law bridge: the operational rules themselves now have typed semantic-preservation proofs. It still does NOT prove that Python port edits implement this indexed relation. keep(d) abstracts a pure subnet, so the relation between concrete graph shape and this term syntax remains a separate refinement obligation. Existence of a settling path is not yet a checked proof that EVERY schedule terminates; that needs the decreasing-measure/accessibility argument. Receipt chronology and external ticket consumption are outside this module.

Next prioritize the already-open resource-fork boundary: determine exactly what single-use guarantee is needed and whether it belongs in rule data, external authority, or an additional primitive. Keep formal all-schedule termination/port refinement as a distinct continuation rather than treating semantic preservation as runtime completeness.
