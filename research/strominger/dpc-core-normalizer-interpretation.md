# DPC core normalizer: interpretation

The bounded normalizer implements seven named rewrite rules and compares
critical-pair outputs using the complete core signature

\[
(\text{authority kind},\text{scope},\text{modality},
  \text{support},\text{resource}).
\]

Equal executable output is not enough to join two presentations.  Support or
modality differences remain typed defects, and a selector result requires an
explicit selector coherence cell.

## Legacy projection boundary

The existing authority-composition contract contains twenty valid grants in
its own evidence calculus.  None can be imported automatically into the
resource-sensitive core because the legacy grant records do not declare:

- nominal capability identity;
- exact operation scope;
- resource modality;
- conserved resource measure;
- physical support roots;
- temporal validity epoch.

The result `0/20 core-importable` is therefore not a rejection of those legacy
readout and executor theorems.  It proves that evidence-level grants cannot be
silently upgraded into linear executable capabilities.  Supplying defaults is
explicitly hostile: each missing field requires a source-derived constructor.

The smallest safe next step is to author one native core capability end to end,
then compare its evidence projection with a legacy grant.  Retrofitting all
twenty grants would manufacture authority the original records never claimed.

## First native capability

`native_manifest_challenge_use` is constructed directly in the core rather
than upgraded from a legacy grant. It declares one nominal identity, the
single operation `submit_manifest_challenge`, linear modality, one conserved
challenge use, physical roots at the challenge ledger and configuration
quorum, and an arbitrary active epoch `e`. Its epoch fence normalizes
symbolically at offset zero. The theorem depends only on affine comparisons
within one epoch family, never on a privileged numerical epoch.

Deleting any one of the six constructor fields makes compilation fail. This
is a bounded minimality result: the native inhabitant is not obtained by
defaults, and every field excluded by the legacy projection audit is operative
in the import boundary.

## Authorized epoch successor

The symbolic order is realized by `advance_e_0_to_e_1`, not by labels alone.
The event binds predecessor and successor state digests, carries a joint
configuration certificate, requires durable non-equivocation, and includes an
executor-side physical-state correspondence before `e+1` is accepted.

Three deletion-style hostiles separate the mechanism: a competing successor
creates a fork, offset two is not an adjacent successor, and a label advance
without physical correspondence does not advance the executor. Thus epoch
order is induced by an authorized state transition rather than presumed from
symbolic arithmetic.

The joint certificate is expanded into two independently rooted configuration
signers. Its admitted singleton fault sets leave at least one signer witness,
and shared administration fails the fault-model audit. Physical correspondence
is likewise exact: an executor attestation binds the measured state digest to
the certified successor digest and must be verified before accepting `e+1`.

The attestation now binds the transition nonce and symbolic successor epoch,
uses a monotone boot counter above the accepted floor, and is verified by an
authority root independent of both configuration signers. Replayed nonces,
rolled-back counters, and correlated verifier governance are independently
rejected. Absence of the attestation is a typed error rather than a checker
exception.

The explanatory regress terminates at a declared attestation trusted base:
one hardware-root identity, measured boot/manifest/configuration ports, and
anti-rollback counter storage under a bounded threat model. This is not an
absolute noncloning theorem or a universal execution-port census. A live
challenge interface admits newly discovered ports and hardware common causes,
which must suspend and refine the affected claim.

## End-to-end native execution

The native challenge capability now has a complete trace: source-authorized
issuance, atomic `unspent -> spent` consumption, durable nonce recording,
effect commitment under the same epoch fence, receiver-signed receipt, and an
append-only history retaining the execution fact. The receipt binds both the
consumption nonce and effect digest.

Execution is deliberately bound to the capability's state digest at epoch
`e`; it does not inherit authority from the separately certified `e+1`
successor. Moving an unconsumed capability across that boundary will require a
future explicit lift constructor. Nonatomic consumption, replayable nonces,
effects outside the fence, mismatched receipts, and historical erasure are
independently rejected.

## Trusted-base cocircuits

Five singleton deletions form the bounded primitive trusted-base cocircuit
basis:

\[
\{\text{rollback},\text{hidden port},\text{clone},
  \text{signer fork},\text{attestation replay}\}.
\]

Each deletion changes the successor certificate from admitted to rejected with
its declared primitive failure class. The cocircuit audit is total under other
hostile mutations: a missing baseline attestation produces a typed failed
minimality audit, never a checker exception. Minimality here is explicitly
bounded to the five declared trusted-base assumptions.
