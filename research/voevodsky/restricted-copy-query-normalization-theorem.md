# Restricted copier/two-query normalization theorem

**Status:** consolidated mathematical proof for the abstract fifteen-rule system below, with implementation regression evidence. This is not a proof-assistant certificate or a formal verification of Python. It supersedes the earlier fragmented conditional proof ledger for this restricted system. It does not implement insertion, union or reusable support.

## 1. Specification

Input is a finite bit word w of length n and two nonnegative integers i,j, represented as unary budgets. The graph is finite, with one symmetric wire at each port. Agent arities are: B0/B1/K: p,a; NIL/E/BOOL/OUT: p; COPY: p,a,b; Q_B/Q_S: p,a,r; Q_R: p,r. Query agents carry one of two fixed channel types. OUT1 and OUT2 are distinguished. All other allocation names are immaterial.

An active pair is an admitted consumer/data pair joined at principal ports. Each rule below reconnects the *outside peers* of the listed removed auxiliary ports. All inserted agents are fresh. Write u for the outside peer of a query's r; s for its saved a peer; t for the data agent's a peer. In COPY rules l,r are the outside peers of COPY.a,b. Unmentioned outside wires are unchanged.

| Removed pair | Replacement connections | Cases |
|---|---|---:|
| COPY,N | fresh N_L.p--l, N_R.p--r | 1 |
| COPY,B_b | fresh B_b^L.p--l, B_b^R.p--r; their a ports to fresh COPY.a,b; fresh COPY.p--t | 2 |
| Q_B,N | fresh Q_R.p--s, Q_R.r--u | 1 |
| Q_B,K | fresh Q_S.p--s, Q_S.a--t, Q_S.r--u | 1 |
| Q_S,N | FALSE.p--u, fresh E.p--s | 1 |
| Q_S,B_b | fresh Q_B.p--s, Q_B.a--t, Q_B.r--u | 2 |
| Q_R,N | FALSE.p--u | 1 |
| Q_R,B_b | BOOL_b.p--u, fresh E.p--t | 2 |
| E,N | empty | 1 |
| E,B_b or K | fresh E.p--t | 3 |

Each new query retains its channel. Original support nodes are marked ORIGINAL; initial budgets and newly produced B/N nodes are marked COPIED (meaning non-original). No rule creates ORIGINAL nodes. These are proof annotations, not extra computational payloads.

The constructor makes one original B/N chain, two disjoint K/N budgets, COPY.p at the original head, COPY.a/b at Q1_B.a/Q2_B.a, budget heads at the query principals, and OUT_i.p at Q_i.r.

## 2. Invariant I

I consists of all the following clauses, not merely local typing:

1. The port multigraph is a finite forest with the declared arities, no loops or parallel-edge cycles, and exactly two OUTs. There is at most one COPY and one Q per channel. Each OUT meets its own Q.r or BOOL.p; every Q.r meets its matching OUT.
2. Live originals are an ordered suffix of the constructor's original chain. They exist exactly when COPY exists. COPY.p meets the suffix head; original B.a meets the next original principal; the suffix ends in original NIL. Removing COPY leaves its source component equal to this suffix.
3. K.a meets COPIED K/N.p. COPIED B.a meets COPIED B/N.p or COPY.a/b. Q_B.p meets COPIED K/N.p and Q_B.a meets COPIED B/N.p or COPY.a/b. Q_S.p meets COPIED B/N.p or COPY.a/b and Q_S.a meets COPIED K/N.p. Q_R.p meets COPIED B/N.p or COPY.a/b. E.p meets COPIED B/K/N.p or COPY.a/b. These walks terminate by finiteness and acyclicity.
4. COPY auxiliary peers are Q_B.a, Q_S.p, Q_R.p, E.p, or COPIED B.a. Removing COPY leaves two disjoint auxiliary-side components, each containing OUT or E. Every full connected component has OUT or E.

Because ports are linear, the source suffix has no spare attachment into a consumer side. Two distinct actual consumer-tail paths cannot merge at a data principal: its unique incident wire fixes its predecessor. This fact will also be used for semantics.

## 3. Constructor establishes I

All three chains are finite, port-linear trees with distinct nodes. Connecting them through COPY and two Q_B nodes produces one tree. Its COPY cut consists of the original suffix and two Q/budget/OUT trees. Every type and root condition is immediate from those connections. There is one query per channel, no eraser, and no unused port. Thus I holds for every finite valid input, including empty words and zero budgets.

## 4. Generic forest substitution lemma

Remove a connected active pair R from a forest. Each external boundary slot has its peer in a different component of G-R. Two peers in one component would provide an outside path which, together with the path inside R, gives a cycle. A second internal pair wire would itself be a parallel-edge cycle, so the only internal wire is the principal wire.

Every replacement in the table is a forest. Attaching a fresh replacement forest once per boundary slot preserves acyclicity: each outside tree attaches to it at most once. Exactly-once use of boundary and new ports preserves port incidence. Each resulting component is rooted precisely when its replacement part has a root or one of its attached outside trees has a root. Unaffected components stay unchanged.

## 5. Closure: every admitted step preserves I

### 5.1 Counts, local types and provenance

No rule removes an OUT or creates a new OUT. Query replacement retains the same channel and its r attachment; query termination substitutes the correct unary BOOL at OUT. Query count cannot increase. COPY either replaces itself or disappears; no other rule creates COPY.

COPY--B removes exactly the original head, gives its successor to fresh COPY.p, and inserts two COPIED bits. COPY--N removes the last original and COPY and inserts two COPIED NILs. All other pairs consume COPIED data and do not touch the original suffix. Thus suffix ownership and tag consistency persist.

The table directly preserves the local peer clauses: Q_B--K moves the saved support to Q_S.p and the budget successor to Q_S.a; Q_S--B moves the budget to Q_B.p and the support successor to Q_B.a; Q_B--N moves support to Q_R.p. The terminating Q rules give remaining support/budget to E, whose admitted types include those successors. E advances to its B/K/N successor, or waits at COPY. COPY outputs give their former peers a B/N principal, accepted by all five allowed output-peer roles. Newly inserted B.a points to the new COPY auxiliary. No other local incidences change. Forest preservation makes the finite successor walks acyclic.

### 5.2 COPY steps: the three-component cut

For COPY--B, cutting the old COPY gives source suffix and two distinct rooted sides. Removing the source head and inserting the replacement gives a new COPY whose cut has precisely: the shortened original suffix; the old left side extended by its new bit; the old right side extended by its new bit. These three components remain disjoint, and both consumer roots remain. For COPY--N the source NIL disappears; each separately rooted consumer side receives a unary NIL and remains rooted. The COPY-cut clauses are then vacuous. Other components are untouched.

### 5.3 Non-COPY steps cannot cross the cut

Fix a surviving COPY C and delete it temporarily. A non-COPY active pair is connected by its principal edge, so belongs to one component of G-C. It cannot be in the source component, which consists solely of original B/N nodes; Q/E pairs consume COPIED nodes. Hence it is either wholly in one consumer side or in a detached component. It cannot involve both sides. All outside boundary peers lie in that same component except possibly C itself through its single attachment. The forest guarantees a side has only one attachment to C; two would make a cycle. A replacement introduces no connection to the other side or to the source. Consequently side disjointness and exact source exclusion persist. It remains to prove the residual side stays rooted; component root coverage alone would not be enough.

### 5.4 Non-COPY steps retain the root on the frontier side

There are three exhaustive behaviors.

**Connected boundary replacement:** Q_B--K/N and Q_S--B replace the active pair by a connected query containing all old boundary slots. The OUT boundary and any frontier boundary remain connected, so a consumer side retains its OUT root. Any other root in an attached outside tree is also retained. E--B/K replaces the old eraser/data pair by a fresh E attached to the same successor; any frontier on that successor side remains anchored by E. These statements also preserve ordinary component roots when there is no COPY.

**Query split:** Q_S--N and Q_R--B produce two pieces: BOOL attached to OUT and E attached to the saved tail/data successor. The OUT-side outside component is only the unary OUT, because OUT has no other ports. Thus any surviving connection to C is necessarily on the tail side and is anchored by the new E, not lost with the Boolean. Both resulting components have roots. In Q_S--N the saved budget is a finite K/N chain and cannot reach C at all; the same split argument still applies.

**No residual tail:** Q_R--N has only its OUT boundary, so cannot lie on a C-connected side; it becomes BOOL--OUT. E--N has no boundary and is an isolated two-node component, so cannot belong to a C-connected side; deleting it leaves no rootless residue.

Together with the COPY analysis and generic substitution lemma, these cases prove every clause of I after each rule, including the previously missing independent COPY-side anchors. This establishes closure for arbitrary finite outside contexts satisfying I; it is not an extrapolation from bounded tests.

## 6. Progress and exact termination

If COPY exists, its original B/N head is an admitted redex. Otherwise every remaining Q/E principal faces admitted COPIED data (no COPY wait remains), so any Q/E supplies a redex. If no redex exists, there is no COPY,Q,E. The two OUTs must therefore meet BOOL. Those unary pairs are complete components; root coverage excludes any further component. Normal forms are exactly two BOOL--OUT pairs.

Let O and C count ORIGINAL data and COPIED B/N/K data respectively. P=3O+C is a natural number. Each COPY step changes it by -3+2=-1; each other rule changes it by -1. Initially P=3(n+1)+(i+j+2)=3n+i+j+5. There is no infinite sequence of actual rewrites. Every maximal reduction sequence ends in a normal form with P=0, and therefore has exactly **3n+i+j+5 steps**. No fairness assumption is needed for sequences taking actual enabled steps; a scheduler that simply stops or stalls is not a maximal reduction sequence.

## 7. Local diamonds and confluence

Two different enabled principal pairs have disjoint agents. A rewrite never changes the other pair's principal wire, so its residual remains enabled. Each rule substitutes each outside boundary endpoint exactly once. For a wire between auxiliary ports of the two redexes, the two substitutions act on its two endpoints independently. Other context wires are unchanged, and each rule's new internal edges depend only on that rule. Label fresh nodes by (redex,local slot); the two orders then give identical incidence and types, hence the same graph up to fresh names, including provenance tags. Identical redex choices give identical reducts. Closure permits these arguments within I. Termination and local confluence give confluence (Newman's lemma), hence a unique normal form modulo names.

## 8. Membership correctness

Define M([],k)=false, M(b::s,0)=b, M(b::s,k+1)=M(s,k). Interpret a support path ending at COPY auxiliary by appending the original suffix at COPY.p. Q_B with budget k denotes M(s,k), Q_S denotes M(s,k+1), Q_R denotes M(s,0); BOOL denotes its value.

The Q equations follow immediately from M: consuming K changes B(k+1) to S(k); skipping B changes S(b::s,k) to B(s,k); consuming budget NIL changes B(s,0) to R(s); reading returns the head or false; skipping empty support returns false. COPY materializes one head on each side without changing either virtual word, or materializes NIL for the empty suffix.

Actual tails of different consumers are disjoint by unique principal incidence. E cannot consume an original or any query-owned copied head; advancing E therefore leaves both query interpretations unchanged. Likewise one query's consumption cannot alter the other's actual tail. Queries may share originals only through virtual COPY expansion, and only COPY changes that suffix, in the meaning-preserving manner just described. Thus every rule preserves both channel values. Initially they are M(w,i),M(w,j); in the terminal Boolean pairs they are the actual Boolean values. This proves correctness.

## 9. Executable scope and assurance

The Python scheduler's table matches these rules on I, as reviewed in `check_copy_two_queries_interleavings.py`; the AST interface audit checks its actual connection expressions, with a manually reviewed branch manifest. For constructor-origin runs, `serial` starts at zero and monotonically exceeds all allocated numeric suffixes. Each fresh call is collision-free; deletion preserves this execution premise. Imported/renamed graphs need a separate safe allocator state. Failed rewrites on malformed graphs are not transactional and are outside this theorem.

The theorem is about finite abstract reduction, not a resource-unbounded promise about Python wall time, memory, recursive serializers, arbitrary scheduler callbacks or corrupted metadata. Proof annotations and runtime bookkeeping are not external provenance credentials. The implementation tests are regression evidence, not the logical basis of the universal context argument.

The mathematical argument above is complete at written-proof level for this restricted model; independent review or proof-assistant formalization can strengthen its assurance. The next programme milestone should be a genuinely new operation—e.g. a surviving support plus two queries—not another unbounded sequence of duplicate small-input checks. Insertion and union still require specifications and proofs. No correspondence with physical nine-point superforms follows.
