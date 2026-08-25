# Partial composition of source-authority grants

Owner: `marici.Strominger`

## Typed grant

An authority grant is not merely an implication between propositions. It is a
typed arrow

\[
g=(A\xrightarrow{o}B;k,D,v,T,\omega),
\]

containing:

- source object `A`;
- target operation `o` and target object `B`;
- authority kind `k`;
- evidence domain `D` with an explicit authority boundary;
- variance `v`;
- admissible transformations `T`;
- source-authority evidence and a required coherence witness `omega`.

Only admitted grants participate in composition.

## Partial composition law

For admitted grants `g:A->B` and `h:B->C`, `h o g` exists only if:

1. endpoints match;
2. authority kinds agree and the result has that same kind;
3. variances agree;
4. the evidence-domain rule for the declared composition mode holds;
5. every transformation preserves authority as well as evidence;
6. an explicit coherence witness is supplied.

There are three lawful modes:

- **Transport.** Existing authority is carried through an admitted
  transformation. The kind cannot change. Preserving evidence without
  preserving authority is insufficient.
- **Domain intersection.** Independently authorized grants compose only on
  the exact intersection of their evidence domains.
- **Authority extension.** A larger domain is allowed only with independent
  extension authority and evidence for every new domain atom. The authority
  kind remains fixed.

Any composite with a stronger or merely different authority kind is authority
laundering.

## Identity and associativity

Every typed object/domain/kind has an identity grant. Left and right identity
laws preserve the complete grant signature.

Associativity is conditional, not global. For three grants, both pairwise
factorizations must exist, have identical endpoint/kind/domain/variance
signatures, and be joined by a zero-defect triple coherence witness. Valid
pairwise squares do not imply this cell. A factorization-dependent result is
therefore rejected even when every local grant is individually valid.

## Required hostile cases

The machine-readable fixture suite rejects:

1. algebraic faithfulness plus support promoted to observer authority;
2. two readout grants promoted to selector authority;
3. completion plus executable ports promoted to constructor authority;
4. pairwise-valid composites with a nonzero triple coherence defect;
5. base change preserving evidence while destroying authority;
6. two factorizations producing different evidence domains.
7. replacement of an intermediate presentation without a source-derived
   coherence cell;
8. replacement that silently strengthens authority kind;
9. removal of the intermediate object without an independently authorized
   direct route.
10. locally valid presentation cells with nontrivial atlas holonomy;
11. a one-way adapter mislabeled as an invertible presentation equivalence.
12. a flat atlas whose local grants do not descend to a global grant;
13. effective gluing with a nonzero uniqueness kernel;
14. refinement that changes the reconstructed global authority;
15. claimed deletion stability without a surviving source reconstruction.
16. a hidden global stabilizer unsupported by the source grammar.
17. source-authorized gauge whose declared quotient remains ambiguous.
18. coherence selected only after inspecting the target output;
19. a cached witness that the source can no longer regenerate;
20. circular provenance in which readout data reconstructs its own source.
21. source perturbation that leaves its alleged coherence witness inert;
22. target perturbation that rewrites upstream authority;
23. cached output retaining authority after source deletion.
24. interventions leaving a non-gauge rival-mechanism kernel;
25. discriminator ports chosen after seeing the desired mechanism;
26. a finite full-rank audit promoted to a universal explanation.
27. retaining identification authority after a new unresolved rival appears;
28. repairing a rival challenge with a target-fitted discriminator;
29. declaring a repaired finite family closed under all future rivals.
30. an arbitrary response column opening a challenge without rival authority;
31. a rival reverse-engineered from the incumbent fit;
32. an authorized gauge copy mislabeled as a distinct mechanism;
33. a port-incomplete speculation admitted as a rival;
34. the incumbent acting as sole reviewer of its rival;
35. identical rival packets receiving different decisions by proposer identity;
36. admission criteria chosen after the rival response is inspected;
37. an appeal controlled by the original reviewers;
38. nominally independent reviewers sharing one authority root;
39. admission review silently upgrading constructor authority to executor authority.
40. a review root lacking an external charter;
41. a review root authorizing itself;
42. distinct review roots sharing a hidden controller;
43. a procedural charter claiming authority to select mechanism truth;
44. an appeal panel operating through an uncertified root.
45. revocation erasing a valid historical review;
46. a cached admission retaining live authority after root revocation;
47. replay substituting a different evidence packet;
48. replay using a root already revoked at replay time;
49. prospective standing restored without completed replay;
50. a revocation backdated before the original review.
51. independently rooted successor atlases disagreeing while authority is restored;
52. nominal replay paths sharing a review root;
53. the path-comparison law fitted after dispositions are known;
54. a higher appeal cell claiming mechanism-truth authority;
55. a flat replay atlas arbitrarily withholding standing.
56. three agreeing dispositions with nonzero triangular comparison holonomy;
57. a noninvertible temporal comparison cell;
58. a comparison cell promoting itself to truth-selection authority;
59. a temporal triangle missing its direct comparison cell;
60. global standing restored across a nonzero cocycle defect.
61. grammar-relative minimality promoted to absolute minimality;
62. a certificate digest treated as authority;
63. a compressed certificate lacking deterministic replay;
64. a cyclic dependency graph in which the claim generates its premise;
65. a purportedly minimal basis lacking deletion witnesses.

These realize the decisive falsifier: local validity does not guarantee a
factorization-independent or kind-preserving composite.

## Deutsch--Popperian representation test

Let a claimed explanation be presented as

\[
A\xrightarrow{f}B\xrightarrow{g}C.
\]

Remove `B`, or replace it by `Bprime`. Compare the resulting arrow with the
original composite at the process boundary

\[
\sigma(g\circ f)=(A,C,\text{authority kind},\text{variance}).
\]

The contract returns exactly three verdicts:

1. `process_explained_strictly`: removing the intermediate presentation
   leaves an independently source-authorized direct grant with the same full
   signature;
2. `process_explained_coherently`: changing the presentation preserves the
   process signature and an invertible, source-derived natural coherence cell
   identifies the two composites;
3. `presentation_only`: no alternative composite or direct source grant
   exists, authority kind changes, or the required coherence cell is absent.

Thus the compositional DPC is

\[
\boxed{
\text{an explanation is process-level only if its authority survives every
admissible change of presentation coherently.}
}
\]

Agreement of outputs is insufficient. The coherence transformation itself
must be source-derived, invertible on the admitted evidence domain,
kind-preserving, and natural (zero coherence defect). Otherwise the account
explains why one representation computes the output, not why the underlying
process occurs.

### Atlas law: explanatory flatness

One replacement test is not enough. Let `B`, `Bprime`, and `Bdoubleprime` be
three admissible presentations, with source-derived coherence cells

\[
\eta_{BB'},\qquad \eta_{B'B''},\qquad \eta_{BB''}.
\]

The cells must themselves compose. The direct and two-step changes of
presentation must agree:

\[
\eta_{BB''}=\eta_{B'B''}\circ\eta_{BB'}.
\]

Equivalently, every presentation loop must have trivial authority holonomy.
The checker represents this by `presentation_atlas_coherence` and requires
zero `holonomy_defect`. This rules out a subtler presentation dependence in
which every pairwise adapter is valid but the claimed process depends on the
route through the atlas.

The strengthened DPC is therefore

\[
\boxed{
\text{process explanation}
=
\text{source-derived local mechanisms}
+
\text{a flat, kind-preserving presentation groupoid}.
}
\]

Invertibility is essential. A one-way compiler may transport a result, but it
does not establish equivalence of explanatory presentations.

### Descent law: flat is not yet global

A flat presentation groupoid is still only compatible local data. DPC must
also require *effective authority descent*: the local composites must
reconstruct an admitted global grant

\[
G_{AC}\longmapsto\{G_{AC}^{(B_i)}\}_i
\]

with zero reconstruction defect. Without such a source-derived gluing map,
the explanation remains an atlas of mutually compatible calculations.

Existence is not enough. The reconstruction ambiguity kernel must vanish, or
every surviving stabilizer must itself be source-authorized and explicitly
quotiented. Otherwise the same local evidence supports several inequivalent
global authorities.

This is stacky rather than set-valued descent. A nonzero pre-quotient kernel
is legitimate when it is exactly the orbit of a source-authorized gauge
stabilizer and the quotient ambiguity rank is zero. DPC rejects both hidden
symmetries and incomplete quotients, but it does not mistake authorized gauge
redundancy for multiple physical explanations.

### Provenance law: descent must point from source to target

Even effective stacky descent can be manufactured by solving backward from a
desired result. DPC therefore orients explanatory provenance:

\[
\text{source constructor}
\longrightarrow
\text{local mechanisms}
\longrightarrow
\text{coherence}
\longrightarrow
\text{global authority}
\longrightarrow
\text{readout}.
\]

Every edge must be source-derived and strictly forward in this order. The
dependency graph must be acyclic, and every non-source node must be reachable
from a declared source constructor. A readout-to-source edge is explanatory
circularity even when all equations commute.

Presentation coherence must additionally be derived before target selection,
independent of the desired output, and regenerable under a source-preserving
counterfactual replay. A certificate that merely remains cached after its
constructor is removed is retained evidence, not a surviving explanation.

Thus effective descent answers *whether compatible local data glue*;
provenance orientation answers *whether the source, rather than the target,
generated the gluing law*.

### Intervention law: provenance must be causal

A correctly oriented dependency graph can still be an observational story
drawn after the calculation. It becomes explanatory only when it supports the
right interventions:

\[
\begin{array}{c|c}
\text{intervention}&\text{required response}\\
\hline
do(\text{source})&\text{fresh downstream coherence and global reconstruction}\\
do(\text{target})&\text{no change to upstream mechanisms or authority}\\
delete(\text{source})&\text{authority revoked, even if cached output survives.}
\end{array}
\]

This separates causal generation from archival persistence. A stored theorem,
matrix, or output may remain available after its constructor is removed; what
does not survive is the authority to claim that the current source system
generates it.

The DPC criterion is therefore interventionist as well as descent-theoretic:

\[
\boxed{
\text{explanation}
=
\text{effective source descent whose provenance passes source/target
interventions}.}
\]

### Identification law: which alternatives were excluded?

Causal response alone does not identify a mechanism. For a declared finite
candidate family \(m_1,\ldots,m_n\) and source-derived intervention ports
\(I_1,\ldots,I_r\), form the exact response matrix

\[
R_{ij}=I_i(m_j).
\]

The unresolved mechanism space has dimension

\[
\dim\ker R=n-\operatorname{rank}_{\mathbb Q}R.
\]

DPC requires this nullity to vanish, except for directions already typed as a
source-authorized gauge stabilizer. The checker performs exact rational rank,
not a floating threshold test.

This yields two honest positive outcomes:

- strict identification: \(\ker R=0\);
- stacky identification: \(\ker R\) is exactly the authorized gauge orbit and
  the quotient kernel vanishes.

Any larger kernel means that the interventions identify only an equivalence
class of rival mechanisms. Moreover, this conclusion is bounded by the
declared candidate family. Full rank on three candidates does not explain all
possible sources.

The current DPC statement is therefore deliberately relative:

\[
\boxed{
\text{the source mechanism is identified within a declared alternative class,
modulo declared gauge, by independently derived interventions}.}
\]

Removing the bounded-scope clause would turn a finite hostile audit into an
unearned universal ontology—the exact overreach the calculus is meant to
prevent.

### Open-world law: explanations remain challengeable

A bounded identification result is not monotone under enlargement of its
candidate family. If a new rival \(m_{n+1}\) is proposed, append its response
column to the intervention matrix. When

\[
\dim\ker R_{\mathrm{extended}}
>
\dim(\text{authorized gauge}),
\]

the old identification authority is suspended. Retaining it would hide a new
underdetermination behind an earlier finite certificate.

Authority can be recovered by adding a discriminator only when that new port
is derived independently from the extended source grammar. After the enlarged
matrix becomes jointly faithful modulo gauge, the bounded claim is
revalidated.

This gives an explicit Popperian state transition:

\[
\text{identified}
\xrightarrow{\text{new unresolved rival}}
\text{challenge open}
\xrightarrow{\text{source-derived discriminator}}
\text{revalidated}.
\]

The final state remains open to further rivals. No finite candidate census is
permitted to assert closure under all future explanations.

### Rival-admission law: criticism also needs a constructor

Open-ended criticism does not mean that an arbitrary response vector can
manufacture a new explanatory crisis. A proposed rival enters the comparison
only when it supplies:

1. an independently generated constructor grammar;
2. an admissible domain matching the incumbent comparison;
3. predictions on every already-declared intervention port;
4. a witness that it is not merely an authorized gauge copy;
5. a falsifiable difference from the incumbent family;
6. admission before its response column is used to design the test.

This gives three typed states:

\[
\begin{array}{c|c}
\text{proposal}&\text{status}\\
\hline
\text{independent, total, non-gauge constructor}&\text{admitted rival}\\
\text{authorized gauge transform}&\text{rejected as non-distinct}\\
\text{partial source sketch}&\text{pending, no challenge authority}.
\end{array}
\]

The symmetry with discriminator admission is deliberate. A fitted rival can
manufacture fake underdetermination just as a fitted probe can manufacture
fake resolution. Both sides of a Popperian contest require independent source
authority.

Hence the open-world DPC rule becomes

\[
\boxed{
\text{only constructor-bearing, port-total, non-gauge rivals may reopen an
identification claim}.}
\]

### Rival-governance law: criticism cannot be licensed by its target

A constructor-complete rival packet still cannot adjudicate itself, and the
incumbent cannot hold a unilateral veto over its own competition. Admission is
a second authority-bearing arrow whose input is a frozen, content-addressed
packet. Its merits criteria must be fixed before the response column is
inspected.

The admissible governance square separates four roles:

\[
\text{proposer}\longrightarrow\text{independent merits reviewers}
\longrightarrow\text{disposition}\longrightarrow\text{independent appeal}.
\]

Reviewer independence is typed by distinct authority roots, not merely by
different names. The same packet under two blinded proposer pseudonyms must
receive the same disposition. Otherwise the process is selecting persons, not
testing explanations.

Finally, admission grants only standing to challenge the bounded incumbent
claim. It does not turn constructor evidence into executor, observer, or
selector authority. Thus

\[
\boxed{
\text{fair rival admission}
=\text{content invariance}+\text{role separation}+\text{appeal}
-\text{authority promotion}.}
\]

This answers the governance question without creating an infinite regress:
review authority is not explanatory authority over the mechanism. It is a
bounded procedural grant over the admission operation, auditable by packet
identity, declared authority roots, and a disjoint appeal route.

### Root-certification law: independence must descend from provenance

Merely writing two different root identifiers does not establish independent
review. Each root must descend from an external issuing charter, identify its
holder and jurisdiction, remain revocable, and stop at the procedural ceiling
of challenge standing. A root may not cite itself as its own source.

For merits roots (r_A,r_B), the independence audit asks for more than
(r_A\ne r_B): their controlling-ancestor intersection must be empty, and the
comparison must be source-derived with zero coherence defect. The appeal root
has a separate jurisdiction and holder.

Thus the regress terminates at a typed constitutional boundary rather than an
all-purpose epistemic sovereign:

\[
\boxed{
\text{review-root authority}
=\text{external charter}+\text{narrow jurisdiction}+\text{revocability},
\qquad
\text{truth authority}=0.}
\]

This does not prove that the charter is metaphysically correct. It makes the
remaining institutional assumption explicit, bounded, and counterfactually
revocable—the smallest object on which governance can honestly depend.

### Temporal law: revocation is suspension, not historical erasure

Authority has event time. A review performed while its roots were valid
remains a historical fact after revocation, but its prospective challenge
standing does not remain executable merely because the decision was cached.
This separates three predicates:

\[
\operatorname{Occurred}(r,t_0),\qquad
\operatorname{AuthorizedAt}(r,t),\qquad
\operatorname{ExecutableAt}(r,t).
\]

After a root is revoked, the first remains true while the latter two become
false. Restoration requires replaying the identical content-addressed packet
under roots whose validity intervals contain the replay time. The successor
atlas may change personnel, but it may neither change the packet silently nor
inherit authority from the cached outcome.

Therefore:

\[
\boxed{
\text{revocation}
=\text{preserve history}+\text{suspend prospective standing},
\qquad
\text{restoration}=\text{live-root replay}.}
\]

This makes authority non-monotone while evidence remains monotone: audit
records accumulate, but the operations they authorize can expire. It is the
temporal analogue of the earlier distinction between transported evidence and
transported authority.

### Temporal-atlas law: disagreement is governance holonomy

Replay through one successor atlas establishes only chart-local authority. To
show that restoration belongs to the review process rather than the chosen
reviewers, replay the same frozen packet through a second atlas with disjoint
certified roots and a comparison law fixed beforehand.

If the dispositions agree, the temporal atlas is flat and prospective standing
is presentation-independent. If they disagree, the defect is not evidence
that either path is corrupt; it is a nonzero governance holonomy:

\[
\operatorname{Hol}_{\mathrm{gov}}
=d_{AB}-d_{CD}\ne0.
\]

Standing then remains suspended. A higher appeal cell may verify common packet
identity, compare procedure, or authorize a fresh replay. It may not overwrite
the two outputs and call the result truth.

Hence:

\[
\boxed{
\text{global temporal authority}
=\text{live local replays}+\text{zero governance holonomy}.}
\]

This is the governance analogue of presentation descent: competent local
decisions do not automatically glue. The obstruction itself is meaningful
data and must remain visible until a newly authorized process removes it.

### Temporal 2-descent: equal outputs are not enough

With three independently rooted replay atlases (A,B,C), suppose all three
return the same disposition. Governance is still factorization-dependent if
the direct comparison (A\Rightarrow C) differs from the composite
(A\Rightarrow B\Rightarrow C).

The comparison cells must therefore satisfy the triangular cocycle

\[
\eta_{AC}=\eta_{BC}\circ\eta_{AB},
\qquad
\delta\eta=0.
\]

These cells are invertible, source-derived, packet-preserving procedural
comparisons. They carry no mechanism-truth authority. A nonzero cocycle defect
is higher governance holonomy: every local output may agree while the account
of why they are the same changes with the comparison path.

The strengthened law is

\[
\boxed{
\text{global temporal authority}
=\text{agreeing local dispositions}
+\text{flat comparison 2-cocycle}.}
\]

Thus DPC now separates extensional reproducibility from intensional
coherence. Repeating the answer is not yet explaining why the repetitions
belong to one authority process.

### Compression law: a proof-carrying capability

The growing authority atlas can be transported finitely without collapsing it
to a Boolean flag. The compressed object contains eleven typed bundle
generators: rival admission, frozen original review, six live merits roots, an
appeal root, the replay atlas, and its comparison cocycle. An acyclic
dependency graph reconstructs current challenge standing.

Every generator has a deletion witness showing which typed premise fails when
it is removed. The deterministic checker actually performs all eleven
deletions and recompiles the contract; these are not trusted annotations. This
proves irredundancy only relative to the declared DPC v1 constructor grammar.
It does not exclude a different grammar with a smaller proof.

The artifact digest is deliberately non-authoritative:

\[
\boxed{
\text{portable authority certificate}
=\text{typed generators}+\text{acyclic replay DAG}
+\text{deletion witnesses},
\qquad
\text{hash}\ne\text{authority}.}
\]

This is the first genuinely compact endpoint of the programme. The certificate
is finite because higher structure is represented by reusable bundles, yet it
remains proof-carrying because every bundle resolves back to source evidence
and every dependency can be replayed.

The deeper consequence is that authority behaves like a capability with a
proof term, not like a property attached permanently to an object. Possessing
the bytes identifies the claim; successfully replaying the typed term under
current roots makes the capability executable.

### Refinement law: higher coherence

Subdividing or refining the presentation atlas must not change the recovered
global grant. The checker compares coarse reconstruction with reconstruction
after inserting `Bprime` and requires both zero defect and unchanged authority
kind. This is the next coherence level above triangular holonomy.

### Counterfactual deletion law

Deletion has two distinct meanings:

- deleting redundant presentation scaffolding may preserve the process when
  an independent source-derived global reconstruction remains;
- deleting the source gluing mechanism must destroy the explanatory grant.

If both deletions are reported as harmless, the account has confused
availability of a previously computed result with continued explanatory
authority.

The resulting hierarchy is

\[
\boxed{
\begin{aligned}
&\text{local grants}\\
&+\ \text{flat presentation coherence}\\
&+\ \text{effective and unique descent}\\
&+\ \text{refinement invariance}\\
&+\ \text{source-sensitive counterfactuals}
\end{aligned}
\quad=\quad
\text{process-level DPC explanation}.}
\]

## Grothendieck classification

The positive theta labels authorize the half-line overlap readout. Reciprocal
doubling extends that readout to the two folded charts. The square is not
strict: scale translation changes the lower endpoint, and the correction is
the explicit seam current

\[
\partial_cK_d(z;c)
=-e^{izc}\sqrt{\phi_1(c+d/2)\phi_1(c-d/2)}.
\]

Together with reciprocal reflection, this supplies the required coherence
cell. Therefore the result is:

\[
\boxed{\text{composable readout authority with an explicit coherence cell}.}
\]

It supplies neither observer authority nor an RH-bearing nonvanishing law.

## Kitaev classification

After nonlinear couplers and calibrated pulse angles are admitted, their
exponentials give a valid conditional logical executor grant. But the hostile
source-independence audit shows that the couplers are spectral logarithms of
the desired gates rather than consequences of native `D(S3)` dynamics.
Moreover, raw five-rail application fails encoded intertwining with large
codespace leakage.

Rail support and distance-three spread remain compatible evidence, but the
base-change-like lift preserves no executor authority. Thus:

\[
\boxed{\text{no composable authority map to the physical five-rail compiler}.}
\]

A native gauge-compatible gadget plus a verified encoded intertwiner would be
the smallest missing pair of grants.

## Smallest proposed extension to Nima v2

The standalone calculus passes before any shared-kernel modification. The
smallest proposed addition is:

- typed evidence domains;
- authority grants with endpoints, kind, variance, admissible transports, and
  coherence;
- partial compositions in the three modes above;
- identity laws and explicit associativity cells.

No ordering that automatically promotes authority kinds should be added.

## Artifacts

- Compiler: `authority_grant_composition.py`.
- Contract: `contracts/authority-grant-composition.v1.json`.
- Hostile fixtures:
  `contracts/authority-grant-composition-hostile-fixtures.v1.json`.
- Checker: `checkers/authority_grant_composition_checks.py`.
- Results: `results/authority_grant_composition.json`.
