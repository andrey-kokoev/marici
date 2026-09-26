# Incremental evidence without pretending holes are witnesses

A separate open-context layer now distinguishes Hole(slot,package) obligations from Admission witnesses. Branch nodes contain already supplied unary/binary rule witnesses; they do not execute arbitrary domain code or invent future witnesses. `Pending.accept` persistently attaches a ticketed admission to one uniquely occurring slot. Matching package, unique slot and ticket, and immutable package/witness shape are checked. These are local revision checks, not authentication or global linear authority across forks.

`materialize` refuses any unfilled obligation. Once complete, it produces an ordinary closed reference history that the existing local net can process unchanged. Receipt chronology is retained separately: swapping independent arrivals changes the receipts but not the eventual resolution derivation. No quotient silently identifies these receipt histories.

Fresh check_pending.py passes all24 permutations of four arrivals, rejects96 incomplete prefixes and six malformed/reuse cases, and compares each resulting closed-net normal form. The original immutable revision survives success and failure. Results: results/pending.json.

There are zero additional net-agent signatures, but this does NOT prove online execution was simplified: waiting has explicitly been placed in an external context boundary. Rewrites still start only after all seeds are admitted. We have implemented incremental evidence collection, NOT interleaved local reduction or equivalence with legacy GATE/HOLD timing. The fixed closed-tree admission and termination theorems are unchanged.

The next genuinely operational experiment is an open-port extension: represent missing evidence as typed external interfaces, permit structural substitution on available regions, splice admitted pure histories into those interfaces, and test mixed arrival/rewrite schedules. Such a calculus must have its own admission and availability invariant. In particular a structural normal form may still contain obligations, so normality must not imply release. Do not introduce fake Seed admissions as placeholders.

A further ownership limitation is explicit: persistent contexts can fork and reuse the same ticket independently in two descendants. Global single-use consumption would need a shared authority/CAS discipline or an explicit resource calculus. Neither this adapter nor proof-history closure grants that automatically.
