# Generated rule declarations now carry checked resource interpretations

The five-package indexed trace signature is no longer validated only for endpoint matching. A generated Agda module maps each Pkg constructor to its actual two-token resource world and supplies:

* a Change witness for every unary constructor at every token;
* a Separate witness for every binary constructor at every token;
* a Fresh witness for every seed constructor at every token.

The map extends structurally to EVERY Resolve derivation over this finite signature. Applying the generic footprint theorem proves no-double-use and no-duplicate-origin for every interpreted source derivation, not only the five exported steps. Each exported step equality is also transported through this interpretation, yielding five checked domain-soundness equalities.

Fresh checks pass for5 packages,3 rules,3 seed constructors and2 token identities. A negative module declares a syntactically legal, correctly indexed revival edge from a spent world to its free predecessor; Agda then rejects the proposed semantic interpretation with UnequalTerms. Thus merely declaring a constructor no longer suffices for resource-domain admission.

Reproduce: python research/voevodsky/resolution-net-v1/check_domain_admission_export.py. It first regenerates/rechecks indexed wire certificates, then checks agda/ResolutionNetDomainAdmission.agda with --ignore-interfaces and runs the negative control. Packet SHA256 and source hashes are in results/domain-admission.json; detailed logs and rejected source text are retained.

The semantic interpretation can identify DISTINCT source witnesses: two grants at one free world may map to the same Fresh witness. That is intentional abstraction for checking resource behavior, NOT a faithful equivalence of full histories. The original indexed certificates retain those witnesses, and no reverse inference of witness equality is made.

Remaining trusted boundary: Python decides how package bytes map to world tables, constructs the signature and reifies concrete wires. Agda checks the emitted declarations/interpretation/proofs, not an independently decoded JSON packet. Fresh seed admission is an assumption of the model, not authenticated permission from an external owner. No global commitment or durable resource authority follows from this result.

Next consolidate a fresh source-bound audit of the whole prototype: identify exactly which claims are formal, finite executable, or conditional on external authority; rerun the affected regressions and compare the domain-specific machinery removed against the generic compiler/admission machinery added. This prevents a growing certificate pipeline from being mistaken for a demonstrated simplification of the runtime itself.
