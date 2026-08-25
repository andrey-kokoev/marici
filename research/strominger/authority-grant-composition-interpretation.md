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
