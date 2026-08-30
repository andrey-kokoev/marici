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

## Composition, descent, and path independence

Admissible configuration edges now form a checked category on the exhibited
path. The identity at a vertex preserves its complete signature and has no
linear-resource replacement boundary. Binary composition is defined only when
the target vertex and output authority of the left morphism equal the source
vertex and input authority of the right morphism. On three composable edges,

\[
(\rho_{23}\circ\rho_{12})\circ\rho_{01}
=
\rho_{23}\circ(\rho_{12}\circ\rho_{01})
\]

as complete composite summaries: boundary resources, support, edge order, and
fault obligations all agree. The checker derives both parenthesizations rather
than accepting a declared associativity flag.

Path independence is deliberately stronger. Three paths are now independently
admissible:

\[
C_0\xrightarrow{\rho_{01}}C_1\xrightarrow{\rho_{12}}C_2
\xrightarrow{\rho_{23}}C_3
\quad\text{and}\quad
C_0\xrightarrow{\sigma_{0X}}C_X\xrightarrow{\sigma_{X3}}C_3
\quad\text{and}\quad
C_0\xrightarrow{\tau_{0Y}}C_Y\xrightarrow{\tau_{Y3}}C_3.
\]

Their typed boundaries, support unions, and fault hypergraphs agree, but their
raw presentations do not. Coherence cells are no longer primitive contract
fields. Nor does each path declare its own normalization target. The
source-authorized constructor presentation contains only

\[
\rho\to\sigma,
\qquad \sigma\to\tau,
\qquad \rho\to\tau.
\]

The checker proves that this directed rewrite graph is acyclic and that every
presentation has the unique reachable sink `tau`. The two reductions leaving
`rho` form the first critical pair; their branches join at `tau`. Thus the
normal form is derived from termination plus confluence, not repeated in three
certificates. Its identifier is then hashed from the common typed boundary,
support union, and fault hypergraph. A canonical reduction trace produces the
content-addressed normalization witness

\[
n_p:p\Longrightarrow NF_{C_0,C_3}.
\]

The checker generates, rather than accepts, the comparison cell

\[
\omega_{pq}=n_q^{-1}n_p.
\]

Attempting to insert a primitive fitted cell or a fitted normal-form name is
rejected. So are an unauthorized rewrite, a duplicate rewrite, a directed
cycle, a fork with two irreducible sinks, or deletion of the required critical
pair branch.

This is the descent condition: local bridge witnesses glue to one global path
class only when the path-wide root-fault hyperedges agree under the coherence
cell. Equal endpoints without equal support, equal support without fault
descent, or two valid paths without an authorized cell do not establish path
independence.

The first higher coherence diagram now closes by cancellation rather than a
declared loop label:

\[
\omega_{\sigma\tau}\omega_{\rho\sigma}
=(n_\tau^{-1}n_\sigma)(n_\sigma^{-1}n_\rho)
=n_\tau^{-1}n_\rho
=\omega_{\rho\tau}.
\]

Thus triangle holonomy is identity because the middle normalization witness
telescopes. A fitted triangle target, nontermination, or nonconfluence breaks
the construction and is rejected. This answers the current Deutsch question
at the bounded three-presentation level: the cell is forced by a terminating
confluent constructor presentation, not appended because two readouts happen
to agree.

The central falsifier remains represented directly:

\[
\boxed{\text{locally admissible parallel paths can still differ globally}.}
\]

No temporal interpretation enters this result. Parallel paths are alternative
factorizations of a morphism, not alternative histories.

## Typed context closure and the unbounded theorem

An important correction is required before taking the unbounded limit.
`rho`, `sigma`, and `tau` all have boundary type

\[
B=(C_0,h_0,\alpha_0)\longrightarrow(C_3,h_3,\alpha_3).
\]

They therefore cannot be concatenated as sequential path morphisms: the target
`C3` of one does not match the source `C0` of another. The valid unbounded
object is a finite product context containing independently typed holes of type
`B`. Each hole may be filled by one of the three alternative factorizations.
This is substitution into parallel holes, not path concatenation.

The authority resources at those boundaries are parameters, not copied
constants:

\[
\alpha_i^{\mathrm{in}}\longmapsto\alpha_i^{\mathrm{out}},
\qquad i\ne j\Rightarrow
\{\alpha_i^{\mathrm{in}},\alpha_i^{\mathrm{out}}\}
\cap
\{\alpha_j^{\mathrm{in}},\alpha_j^{\mathrm{out}}\}=\varnothing.
\]

Thus enlarging the product context requires fresh pairwise-disjoint resource
instances. It does not clone the concrete `cfg_auth_C0` capability used by the
single-hole witness.

Assign the fillings rank

\[
r(\rho)=2,
\qquad r(\sigma)=1,
\qquad r(\tau)=0,
\]

and extend the rank additively over the holes of a product context. Every
authorized substitution strictly decreases total rank. Hence no finite typed
context admits an infinite reduction sequence.

There are exactly two critical-pair schemas:

- In the same hole, two rules may leave `rho`; the exhibited diamond
  joins their reducts at `tau`.
- In distinct holes, the two substitutions commute because each preserves
  the full component signature: source and endpoint boundaries, support union,
  fault hypergraph, and input/output authority resources.

These schemas prove local confluence independently of context size. Termination
plus local confluence invokes Newman's lemma, yielding

\[
\boxed{\text{every finite well-typed factorization context has a unique normal form}.}
\]

This is the first genuinely unbounded coherence statement in this lane. The
checker rejects a nondecreasing rank, loss of context closure, a smeared hole
boundary, cloned or concrete-reused authority resources,
sequential-composition laundering, omission of any preserved
semantic field, omission of the disjoint-hole schema, incomplete rule
coverage, or replacement of the theorem scope by a bounded census.

The scope remains algebraic and atemporal: a product context is neither a path
through configurations nor a sequence of moments.

## Indexed fibers and permutation equivariance

Independence also cannot be inferred from equal untagged labels. In an
`n`-hole context, support records, authority roots, and resource boundaries are
lifted to indexed fibers

\[
(i,s),\qquad(i,r),\qquad
\alpha_i^{\mathrm{in/out}}.
\]

The default fault hypergraph is the disjoint coproduct of the hole-local
hypergraphs. Consequently, two roots with the same local spelling in distinct
holes remain distinct authority loci. A cross-hole common cause is possible
only after an explicit constructor replaces that coproduct by a correlated
hyperedge; the present theorem does not authorize such a constructor.

Every finite bijection `pi` of the hole indices acts simultaneously by

\[
(i,s)\mapsto(\pi(i),s),qquad
(i,r)\mapsto(\pi(i),r),qquad
\alpha_i\mapsto\alpha_{\pi(i)}.
\]

The rewrite rules contain no distinguished hole index, so substitution is
equivariant under this action. Rank is a sum over holes, the two local
critical-pair schemas are preserved, and pointwise normalization satisfies

\[
N(\pi\cdot X)=\pi\cdot N(X).
\]

This predicts that renaming or permuting independent authority loci cannot
alter the admitted normal form. A nonbijective index map, resource aliasing,
untagged support union, position-dependent rewrite, or implicit cross-hole
fault identification is rejected. These are precisely the operations that
would turn symmetry into information loss or authority cloning.

## Authorized correlation and symmetry breaking

Cross-hole dependence is admitted only through the constructor
`dpc.cross_hole_fault_correlation.v1`. Its authority is narrow: it may extend
the fault hypergraph, but it may not identify support records or linear
resources. The exhibited hyperedge is

\[
\{(h_0,\mathrm{admin}_C),(h_1,\mathrm{admin}_C)\}.
\]

It records one common-cause failure across two holes. Its projection into each
affected local bridge removes only `admin_C`, leaving the independently rooted
`admin_B` member available. A hyperedge containing both `admin_B` and
`admin_C` at one hole is rejected because it exhausts that local bridge.

Correlation breaks symmetry. Before extension, every finite permutation of
the three holes is admitted. Afterwards, the permitted permutations are
exactly the automorphisms of the typed correlation hypergraph. For the fixture
they are

\[
\mathrm{id},\qquad(h_0\ h_1),
\]

so the symmetry group has order two rather than six. The checker derives this
stabilizer by transporting the complete hyperedge set; it does not accept a
claimed group size.

Pointwise normalization still commutes with this stabilizer because rewrite
rules preserve indexed root labels and mention no distinguished hole. It does
not claim equivariance under permutations that move the correlated pair to an
uncorrelated pair:

\[
N(gX)=gN(X)
\quad\text{only for}\quad
g\in\operatorname{Aut}(H_{\mathrm{fault}}).
\]

Thus an authority-bearing correlation constructor has a measurable algebraic
effect: it reduces symmetry without merging the underlying support or resource
fibers.

## Correlation cocircuit classification

The correlated-context safety test now has a complete minimal obstruction
basis. If `B` is the authority-root set of a local bridge and `i` is a typed
hole, define

\[
K_{i,B}=\{(i,r):r\in B\}.
\]

For any admitted correlation hyperedge `E`, every local bridge survives
exactly when no primitive cocircuit is contained in it:

\[
E\text{ is safe}\quad\Longleftrightarrow\quad
\forall i,B,\ K_{i,B}\not\subseteq E.
\]

This is not a bound on correlation size. An arbitrarily large cross-hole
hyperedge remains safe if every local projection leaves at least one root of
each bridge alive. Conversely, a two-root hyperedge is fatal when it contains
the complete authority basis of one local bridge. Each obstruction is
deletion-minimal: removing either root restores a surviving authorization
route.

The three-hole fixture has three derived bridge sets:
`{admin_B,admin_C}`, `{admin_C,admin_D}`, and `{admin_D,admin_E}`. It therefore
has nine primitive indexed cocircuits. The authorized correlation preserves
only the order-two stabilizer exchanging `h0` and `h1`; its action partitions
the nine cocircuits into six orbits. Both the obstruction basis and its orbit
decomposition are derived from bridge data and actual correlation
automorphisms, rather than listed as fitted exceptions.

## Correlation composition has two meanings

There are two inequivalent ways to combine valid correlation records. Ordinary
family union retains the inputs as distinct possible fault hyperedges:

\[
\mathcal H_1\sqcup\mathcal H_2.
\]

It is safe exactly when every retained hyperedge is safe. Synchronous fusion
instead asserts that the two sets of fault loci may occur as one event:

\[
E_1\star E_2=E_1\cup E_2.
\]

Fusion is therefore not supplied by ordinary union or by transport. It needs
the separate constructor `dpc.synchronous_fault_fusion.v1` rooted in the
`simultaneity_charter`.

Even when both inputs are safe, their fusion is safe only if no primitive
cocircuit is assembled across the seam:

\[
E_1\star E_2\text{ safe}
\quad\Longleftrightarrow\quad
\nexists K_{i,B}\subseteq E_1\cup E_2.
\]

The hostile witness splits `{(h0,admin_B),(h0,admin_C)}` between two separately
safe cross-hole correlations. Retaining them as alternatives is safe; fusing
them exhausts the `admin_B/admin_C` bridge at `h0`. Thus local validity is not
compositional under strengthened simultaneity semantics. The missing datum is
not another root but authority to assert that the two fault descriptions belong
to one jointly realizable event.

## Finite fusion has a source-derived witness bound

Let

\[
r=\max_{i,B}|K_{i,B}|.
\]

If a finite synchronous fusion is unsafe, choose a blocking cocircuit and, for
each of its loci, one input hyperedge containing that locus. Those choices use
at most `r` inputs and their subfusion is already unsafe. Hence

\[
\bigcup_{j\in J}E_j\text{ unsafe}
\quad\Longrightarrow\quad
\exists J_0\subseteq J,quad |J_0|\le r,quad
\bigcup_{j\in J_0}E_j\text{ unsafe}.
\]

The bound comes from constructor geometry—the largest local bridge basis—not
from the number of holes or the size of the correlation family. In the present
contract every primitive cocircuit has cardinality two, so pairwise fusion
checks decide safety for an arbitrary finite family. The binary split witness
shows that this bound is sharp: checking inputs individually is insufficient,
while no ternary-only obstruction exists.

This is the first useful complexity theorem for the fault-correlation layer.
An unbounded family does not require an unbounded global census; its safety
reduces to subfamilies whose size is bounded by local authority redundancy.

## Repairs are cocircuit transversals

Diagnosis and repair remain different authority kinds. Discovering that a
fused hyperedge is unsafe does not authorize changing its fault declaration.
The constructor `dpc.fault_locus_repair.v1`, rooted in the `repair_charter`, may
remove repaired loci; it may not mint replacement authority.

For an unsafe hyperedge `E`, let

\[
\mathcal K(E)=\{K_{i,B}:K_{i,B}\subseteq E\}.
\]

A repair set `R` restores safety exactly when it intersects every member of
`mathcal K(E)`. The complete primitive repair family is therefore the family of
inclusion-minimal transversals of the blocking cocircuit hypergraph:

\[
R\text{ primitive repair}
\quad\Longleftrightarrow\quad
R\cap K\ne\varnothing\ \text{for all }K\in\mathcal K(E),
\]

with no proper subset of `R` satisfying the same condition.

The overlapping fixture contains the two blockers `{B,C}` and `{C,D}` at one
hole. Its primitive repairs are

\[
\{C\},\qquad \{B,D\}.
\]

This exposes a distinction that a single repair score would hide. Both are
minimal in the order of authorized changes, but they have different
cardinalities and operational shapes: one repairs a shared failure locus; the
other repairs two independent outer loci. Choosing between them requires a
separate cost or feasibility readout and cannot be derived from safety alone.

## Safety does not contain a repair selector

The repair antichain is invariant under changes of operational preference. A
valuation is additional source data, represented here by a strictly positive
additive cost on repairable loci. The selector then computes

\[
\operatorname*{argmin}_{R\in\operatorname{Tr}_{\min}(\mathcal K(E))}
\sum_{x\in R}w(x).
\]

Valuation and selection have their own constructors. Neither safety diagnosis
nor the existence of a minimum authorizes executing the selected repair.

The two authorized schedules give a preference-reversal witness. When the
outer loci cost one each and the shared locus costs three, the selected repair
is `{B,D}` with total cost two. When the shared locus costs one and each outer
locus costs three, the selected repair is `{C}` with total cost one. The
cocircuit geometry and primitive repair family are unchanged.

Therefore there is no canonical repair selector in the safety structure:

\[
\text{safety}\longrightarrow\text{valid repair antichain},
\qquad
\text{safety}+\text{authorized valuation}
\longrightarrow\text{preferred repair}.
\]

Treating “fewest changed loci” as automatic would merely smuggle in the unit
cost valuation. It is a legitimate policy only when that valuation has an
authority-bearing source.

## Selection is not execution

The selected repair is a content-addressed decision record, not an operative
capability. Its certificate binds four objects:

\[
(\text{unsafe hyperedge},\ \text{primitive repair family},\
\text{valuation profile},\ \text{selected repair}).
\]

Execution requires a separately issued linear capability rooted in the
`repair_execution_charter`. Its only admitted transition is an atomic
compare/apply/consume operation:

\[
(E,R,u=1)
\longmapsto
(E\setminus R,u=0),
\]

provided the observed configuration and requested repair match the certificate
exactly. Safety is recomputed from the resulting hyperedge; it is not inherited
from the earlier selection proof.

This rules out four distinct authority shortcuts: treating a selector output as
an actuator, replaying a consumed capability, applying a valid repair to a
different configuration, or assuming the postcondition without rerunning the
cocircuit test. The successful fixture consumes its one use and records
certificate digest
`08337b0bd40cbf3492d3282ed94b2a3fd54c887fd413a0b46f762d3db0d925fe`.

## Commuting effects do not imply distributable authority

The selected outer repair has two loci, `{B,D}`. As set operations its parts
commute:

\[
(E\setminus\{B\})\setminus\{D\}
=
(E\setminus\{D\})\setminus\{B\}
=E\setminus\{B,D\}.
\]

But the endpoint proof does not factor. Removing only `B` leaves the `{C,D}`
cocircuit, while removing only `D` leaves `{B,C}`. Thus both proper nonempty
subrepairs are unsafe even though the joint repair is safe.

Consequently an atomic two-locus capability cannot be transported into two
independent endpoint capabilities merely because their underlying mutations
commute. There are exactly two admitted execution architectures at this layer:

- preserve one joint atomic execution capability; or
- introduce a staged-execution constructor carrying explicit authority for the
  unsafe intermediate configuration and a residual certificate for completion.

This obstruction is atemporal. It concerns factorization through an
intermediate object, not which action occurs “first.” Algebra supplies a
commuting square of effects; authority fails because neither intermediate leg
has the endpoint type.

## Authorized staging produces a coherence diamond

The staged constructor supplies precisely the authority missing from the raw
effect factorization. For the two-locus repair there are two paths:

\[
E\xrightarrow{-B}E_B\xrightarrow{-D}E_{BD},
\qquad
E\xrightarrow{-D}E_D\xrightarrow{-B}E_{DB}.
\]

The intermediate configurations `E_B` and `E_D` are distinct and both retain a
blocking cocircuit. They carry the typed status `unsafe_repair_in_progress`,
not endpoint safety. Each first leg emits a linear residual certificate binding
the source configuration, applied subrepair, remaining subrepair, and target
configuration.

The endpoints agree and are safe:

\[
E_{BD}=E_{DB}=E\setminus\{B,D\}.
\]

Their coherence cell is generated by commuting set difference, rather than
declared from observed endpoint equality. The two residual certificates remain
different because they authorize different second legs; the coherence cell
does not identify or interchange them.

This is the correctly typed version of distributed repair. Factorization is
allowed only after intermediate-state authority has been constructed, and path
coherence appears only after both residual obligations have been discharged.

## Finite staged coherence is generated by adjacent swaps

For a selected repair with `n` distinct loci, every staged factorization is a
permutation of those loci. Adjacent transpositions generate the complete path
graph. Their coherence is controlled by the Coxeter relations

\[
s_i^2=1,
\qquad
s_is_j=s_js_i\quad(|i-j|>1),
\qquad
s_is_{i+1}s_i=s_{i+1}s_is_{i+1}.
\]

The involution removes a redundant swap, far commutation compares independent
local reorderings, and the braid relation compares the two ways of moving one
repair locus through two neighbors. These relations generate all coherence
between finite staged paths; no endpoint-fitted higher cells are added.

The three-locus witness is source-derived from three independent bridge
cocircuits. It has eight primitive repairs of size three. For the selected
repair `{(h0,B),(h1,B),(h2,B)}`, all six permutation paths were generated.
Every proper prefix remains unsafe, all completed paths reach the same safe
endpoint, the adjacent-swap graph is connected, and the braid relation holds.

Thus the two-locus diamond was not an isolated coincidence. It is the rank-two
face of an atemporal permutohedral coherence system. Local swap cells plus the
Coxeter relations are sufficient to transport residual authority coherently
across every authorized factorization of a finite repair.
