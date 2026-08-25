# Shared-predicate fault safety depends on pointer-block typing

Owner: `marici.Kitaev`

## Bounded question

Does ledger entry 2507's four-episode shared-predicate compiler preserve the
one-fault output contract at its pointer contacts?

## Two compatible pointer models

The frozen statement supplies “one four-level coherent pointer per Wilson
observable” but does not specify its encoded-block decomposition.

For a monolithic encoded ququart, the shared \(111\) predicate contacts each
of the C, F, and G pointer blocks twice, once for controlled \(U\) and once
for controlled \(U^2\). A persistent predicate fault may therefore place two
errors in one pointer block. One power-layer hygiene boundary is necessary;
discard-and-recompute raises the conjunction-episode upper bound from four to
six.

For two independently protected binary pointer components, the two powers
touch distinct encoded blocks. Every predicate then contacts each component
at most once, so this particular multiplicity obstruction disappears.

## Disposition

The ideal algebraic 193T theorem remains valid. Its fault-safe interpretation
is blocked until the pointer encoding declares whether the power controls are
one correction block or two. Even the split model does not settle
compute/uncompute propagation into sector data or microscopic phase-gadget
faults.

## Falsifiers

- A frozen pointer encoding already identifying its correction blocks.
- A monolithic schedule avoiding repeated 111 contact without charged hygiene.
- A split-component schedule revisiting one protected component twice.
- A microscopic primitive whose internal recovery clears predicate faults.

## Artifacts

- Checker: `checkers/check_s3_shared_predicate_pointer_typing.py`
- Result: `results/s3-shared-predicate-pointer-typing.json`
- Result SHA256:
  `03646B6D4552833691EBEBE0CAF4ADFE525B4EB845FF7F8C3BF276778F733CC5`
- Graph admission: `ev-000000003464-eee0a2dd-e382-4123-b687-a267e5470f70`
- Ledger: entry 2508, `seqclaim-3950ae3fdb239ee9708ef588`
