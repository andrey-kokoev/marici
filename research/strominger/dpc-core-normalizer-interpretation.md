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

## Linear SSA resource flow

The native resource programme now executes

\[
\text{issue}\to\text{partition}\to\text{reserve}\to
\{\text{consume},\text{release}\}\to\text{consume}\to\text{compensate}.
\]

Every resource name has one definition and a consuming use removes it from the
live environment immediately. Partitions conserve quantity at each prefix;
reservations block reuse until an authorized release or consumption; and
compensation produces a settled effect rather than reminting the original
capability. Declared concurrent consumers may proceed without a linearizer only
on disjoint partition regions. Resource reuse, inflation, unauthorized release,
reminting compensation, and overlapping concurrent consumption are rejected.

## Forgetful projection to legacy evidence

The named projection forgets identity, resource quantity, modality, physical
roots, and epoch, retaining only target operation, authority kind, and source
evidence. It maps two inequivalent core capabilities—one linear use at `e` and
one bounded-two-use capability at independent epoch family `f`—to the same
legacy evidence packet:

\[
U(c_{\mathrm{linear},e})=U(c_{\mathrm{bounded2},f}).
\]

Hence the projection is non-injective and has no canonical reverse lift. A
reverse construction must choose precisely the fields the legacy calculus does
not contain, so it requires new source authority. Claiming a canonical lift,
omitting the projection constructor, or smuggling resource fields into the
legacy signature is rejected.

## Finite successor-chain induction

The one-step successor theorem now extends to arbitrary finite nonempty chains.
The induction state is the current symbolic epoch, current physical-state
digest, accumulated support set, and previously used transition identities.
Appending one step is valid exactly when it is adjacent, digest-linked,
nonforking, physically realized, and contributes an explicit support witness.

The bounded three-step replay reaches `e+3` and retains bootstrap plus all three
transition obligations. Because the checker iterates the same invariant over
an arbitrary input list, the proof is by finite induction rather than a
three-epoch special case. Offset gaps, broken digest links, competing
successors, and support deletion are rejected independently.

## Native reconfiguration

Configuration change is a joint constructor in the core IR, not a legacy-side
convention. It consumes old-configuration authority, a new proposal, and a
physically attested successor; it emits one replacement configuration while
retaining the complete support union. Neither configuration can activate the
successor alone.

The bridge condition is typed over authority-root fault fibers. In the fixture
the common bridge is `r2,r3`, rooted independently at `admin_B,admin_C`; loss
of either root remains survivable, while loss of the whole bridge is rejected.
Omitting an admitted common-cause fiber is also rejected. Thus the checker
distinguishes a real fault-hypergraph guarantee from an overlap count or an
empty fault model.

## Varying-membership configuration-path theorem

No time object is required. The invariant attached to a configuration vertex
`C` is

\[
I(C)=(C,h_C,M_C,Q_C,\alpha_C,S_C),
\]

where `h` is a state-record digest, `(M,Q)` is membership and quorum, `alpha`
is the configuration-authority resource presented at that vertex, and `S` is
its support. An oriented edge `rho: C -> D` is admissible exactly when:

1. its source signature is incident with the current partial composite;
2. a source-derived correspondence relates the two endpoint state records;
3. the source and target quorums jointly authorize the edge;
4. their nonempty bridge survives every admitted authority-root fault fiber;
5. the input resource `alpha_C` occurs once on the input boundary and exactly
   one distinct `alpha_D` occurs on the output boundary; and
6. the output support is exactly the union of source, target-presentation,
   correspondence, and constructor supports.

The edge list is a presentation of a composable path. Its position is used
only for structural induction on path length; it is not a clock, epoch,
duration, causal history, or claim that one configuration physically existed
before another. The bounded witness is the path
`123 -> 234 -> 345 -> 456`. Replays of its one-, two-, and three-edge partial
composites exercise the same generic incidence rule.

The theorem is conditional on the declared fault hypergraph. Replica labels do
not imply independent authority roots. If two bridge members share one root,
that entire root fiber must be admitted as one correlated failure. Path-wide
root-fault hyperedges are projected through every edge's root map and must
leave a survivor in every bridge they touch. Thus `{admin_C,admin_D}` is
rejected because it exhausts the middle bridge; this is an incidence fact, not
a statement about a persistent failure through time.

The global law is

\[
\text{admissible path}
\iff
\text{every edge preserves }I\text{ under composition and its declared
fault-root projections preserve bridge support}.
\]

This is a theorem about typed contract admission. It does not manufacture a
consensus implementation, temporal order, or executable authority from
geometric overlap.

The file still contains separate epoch-fence audits for capabilities whose
source contracts explicitly declare temporal validity. Those audits neither
feed nor justify the configuration-path theorem. There is no forgetful map
from path orientation to an epoch order: adding one would require an explicit
source-authorized clock or causality constructor.
