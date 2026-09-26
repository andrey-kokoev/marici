# Fresh prototype audit: what became simpler, what remains trusted

Fresh command:

`python research/voevodsky/resolution-net-v1/check_trust_surface.py`

The final run passed29 stages in216.799 seconds:19 Python checkers, the admission checker again under -O, and fresh --ignore-interfaces checks of all9 live Agda modules. The static local-Python/resolved-Agda import inventory contains80 source files, including original reference and library dependencies. All inventoried bytes were unchanged during the run, including regenerated Agda certificates. This is a source/import audit, not a hash closure over the Python/Agda binaries, OS or every implicit toolchain dependency. Result: results/trust-surface-audit.json.

## Claim levels

FORMALLY CHECKED: generic substitution laws; abstract contextual rewrite simulation; administrative pure compression; abstract all-schedule termination/progress and exact step count; per-token use/origin accounting with binary separation; finite exported abstract step certificates; interpretations of the finite signature into resource semantics.

EXECUTABLY CHECKED: concrete Python port rewrites, atomic failures, typed admission, closed/open schedules, projected arrival diamonds, exact snapshot replay, finite legacy saturated-availability comparison, and single-authority ticket races.

STILL TRUSTED/OPEN: Python decoding/reification/export, fidelity of package-byte-to-world assignment, authenticated grant issuance, global commit authority across independently forked realms, a universal concrete graph refinement theorem, and higher dependent index paths. Nima's reported index-coherence results have not yet been imported or independently inspected here.

## Actual simplification ledger

* Structural core:5 fixed-arity agent signatures,3 local rewrite schemas.
* Incremental evidence:0 additional agent signatures or rewrite schemas;1 explicit boundary splice operation.
* Domain resource behavior:typed package/rule evidence, no added internal evaluator primitive.
* Exclusive commitment:an explicitly separate shared-authority model; not eliminated by the resolution operator.
* Construction/admission/runtime modules comprise reference.py(67), admission.py(65), local_net.py(113), open_net.py(48), pending.py(63):356 nonblank lines. These counts include comments, exclude proof/export/test code and are NOT a performance measure or full system-size comparison.
* Concrete comparison remains unfavorable for a small closed join:7 versus6 rewrites; online projected states416 versus57. No speed, state-space or total code-size advantage is established.

What IS simplified is the operational vocabulary: several domain operations are handled as typed rule witnesses by the same structural calculus, with common preservation and termination laws. The proof/export machinery grew because the project now records which part of that assertion is verified. That verification cost must not be hidden when evaluating overall maintenance complexity.

## Next

Investigate the existing dependent-index-crosswalk branch. The finite exported Pkg datatype is discrete; genuine dependent families may have nontrivial index loops that act on witnesses. Read the upstream circle-cover regression and decide which comparisons the current calculus can represent without erasing transport. This is a real remaining semantic boundary, not a reason to stop at the iteration budget.
