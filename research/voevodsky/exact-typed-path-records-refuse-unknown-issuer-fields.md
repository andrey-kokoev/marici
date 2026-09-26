# Exact typed path records refuse unknown issuer fields

Fresh `check_path_unknown_field_rejection.py` checks an `original-identity@1` record with exactly kind/endpoint/edges. Adding `issuer`, `origin` or `extensions` fails `UNKNOWN_OR_MISSING_FIELDS`, as does omitting required fields. Silently projecting an extra-field record onto the known subset would hash identically to the base commitment despite a different full-record hash. Hence an unrecognized `issuer` value cannot be smuggled into a structural path record and treated as authority by another verifier.

This toy strict schema defines no owner signature or observed event. Analytic S,A,R,C,G mapping remains deferred.

Next test TYPE CONFUSION with JSON Boolean versus integer (e.g., `true == 1` in Python): exact structural path field validators should reject Boolean occurrence/generation values where integer is required even when generic equality passes.
