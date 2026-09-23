# Two local row-edit candidates need version CAS and revalidation

Two IN-MEMORY candidates are staged against the same four-row square version 1. Candidate A changes y-upper bound to 2; candidate B changes x-upper bound to 2. Each individually retains a valid one-row x<=2 proof with the appropriate surplus. Fresh `check_concurrent_local_source_candidates.py` commits A as local math version 2 by checking expected version and manifest digest. B's attempted write against the OLD snapshot is `STALE_CANDIDATE_REVALIDATION_REQUIRED`; no last-writer-wins occurs. Rebasing B on A creates a DIFFERENT combined manifest and revalidates x-upper proof/surplus before local version 3. The original version 1 stays untouched and repeating the rebased ID is idempotent.

This models a mathematical versioned catalogue only, not actual concurrent file editing or a publisher authorization. Even successfully rebased proof packets do not inherit a source grant from version 1. The current source owner is still unassigned and analytic S,A,R,C,G remains deferred.

Next test a HOSTILE rebased edit whose individual candidate was valid on version 1 but becomes invalid on the winner's rows because their two changes interact. Require full staged reproof rather than assuming commutativity from disjoint-looking row IDs. Local logic only; no actual source mutation.
