# Rees labelled-generator capability audit

Problem: decide whether the current Rees computation can directly produce an
integral labelled exceptional generator.

Bold conjecture: its existing state suffices to serialize a generator and
verify boundary and connecting image.

Rivals: the rank-only interface is irreparable; modular provenance replay is
sufficient; or exact/cross-prime reconstruction is also required.

Risky consequences: deterministic input rows plus carried combination vectors
would recover modular labelled pivots, while a single-prime vector would not
define an integral generator.

Strongest falsification attempt: the caller has a deterministic labelled column
basis and row stream, and the engine retains normalized pivot rows. It does not
transmit row identities, carry input-row combinations, or output anything but
counts. Its arithmetic is single-prime modular.

Disposition: revised. The source can be upgraded to emit modular provenance
certificates, but current receipts cannot be replayed into an integral source
generator. Integral construction additionally requires stable row labels,
combination-vector replay, cross-prime matching or exact arithmetic, and
boundary, connecting-image, primitiveness, and source-label checks. The next
leaf prototypes the provenance reducer and corrupted-certificate falsifier.
