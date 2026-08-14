# General Marked-Deletion Evidence

## Record

Date: 2026-08-13

Status: the component/innermost edge-deletion rule of entry 56 passes an
exhaustive finite audit on every connected simple graph through five labeled
vertices.  An all-graph argument now proves that it is well defined on marked
tubings, face-poset order preserving, dimension nonincreasing, relabeling
covariant, and strictly functorial.  Face surjectivity remains finite evidence
through five vertices.

Thus the full face-surjective cellular-carrier theorem is still conditional,
but all parts except surjectivity are no longer merely computational.

Reproducible certificate:

```text
research/nima/check_marked_edge_deletion_general.rs
```

## Candidate carrier

Let \(G\subseteq H\) be connected simple graphs on the same finite vertex
set.  For every marked \(H\)-tube \(u\), take the connected components of the
restriction \(G|_u\).  Deduplicate the resulting \(G\)-tubes.

If a target component \(C\) is produced by several source tubes, give it the
mark of the unique innermost contributing source tube.  This defines the
candidate contravariant face carrier

\[
r_{H,G}:\operatorname{Face}(\mathcal JH)
\longrightarrow
\operatorname{Face}(\mathcal JG).
\]

The innermost contributor is well defined: any two source tubes contributing
the same nonempty component overlap, hence are nested in a tubing.  The finite
test also supports the stronger strict identity

\[
\boxed{r_{K,G}=r_{H,G}\,r_{K,H}}
\]

for \(G\subseteq H\subseteq K\).

## Exact scope

The certificate enumerates all connected labeled graphs:

\[
(1,1,4,38,728)
\]

for \(n=1,2,3,4,5\).  It then enumerates all connected one-edge deletion
diagrams:

\[
(0,0,3,84,3140),
\]

and all connected two-edge deletion diagrams:

\[
(0,0,0,63,5730).
\]

Expensive face-poset calculations are performed on 49 one-edge and 74
two-edge isomorphism-class representatives only after every labeled diagram
has been classified.  Full relabeling covariance is checked under every
permutation in \(S_n\).

For the component/innermost rule, the audit covers:

- 157,643 marked source faces;
- 557,618 source cover relations;
- 18,627,714 permutation-covariance checks;
- 274,964 two-edge source faces.

It finds zero undefined images, order failures, dimension failures, missed
target faces, covariance failures, deletion-order failures, or discrepancies
from direct deletion.

The unmarked component projection agrees with the known
graph-associahedral \(\Theta\) map on all 23,082 marked-forgetful and 2,514
unmarked marked-theta baseline checks.

## Why innermost is selected

Two simpler alternatives already fail at three vertices.

Forget-only has:

- 12,679 order failures;
- 32,564 dimension failures;
- 17,295 missed target faces.

Component/outermost has:

- 9,273 order failures;
- 2,565 dimension failures;
- 9,374 missed target faces.

Both alternatives remain strictly functorial as set-level deletion rules in
the audited range.  Their failure is subtler: they do not define the required
cellular face carrier.  The marking therefore contains genuine homotopy-map
data, and the innermost rule is not cosmetic.

## All-graph structural lemmas

The following parts admit direct proofs for every finite graph inclusion
\(G\subseteq H\) with both graphs connected.

First, source tubes contributing one target component overlap and hence form
a nested chain.  Their innermost member is unique.

Second, if target components \(A\subsetneq B\) select innermost source tubes
\(x,y\), then \(x\subsetneq y\).  Indeed, \(y\subseteq x\) would put the
\(G\)-component \(B\) inside the \(G\)-component \(A\), contradicting strict
containment in the other direction.  Source marked compatibility therefore
implies

\[
\operatorname{mark}(y)=\mathrm{thick}
\quad\text{or}\quad
\operatorname{mark}(x)=\mathrm{thin},
\]

which is precisely target marked compatibility.  Together with the known
unmarked component projection, this proves totality and validity.

Third, dimension nonincrease follows from a distinguished-component
injection.  For each source tube \(u\), let \(u_1,\ldots,u_r\) be its maximal
proper child tubes in the source tubing.  They are pairwise disjoint and
nonadjacent in \(H\), so they cannot cover the connected tube \(u\).  Choose

\[
x_u\in u\setminus\bigcup_i u_i
\]

and let \(C_u\) be the \(G\)-component of \(u\) containing \(x_u\).  No proper
source tube inside \(u\) contains \(x_u\), so \(u\) is the unique innermost
contributor to \(C_u\).  If \(u\subsetneq v\), then \(u\) lies inside a
maximal proper child of \(v\), while \(x_v\) does not; hence
\(C_u\ne C_v\).  Disjoint source tubes plainly give disjoint components.
Thus

\[
u\longmapsto C_u
\]

injects all source tubes into target tubes and preserves their marks.  In
particular it injects nonbroken source tubes into nonbroken target tubes, so
target codimension is at least source codimension.

Finally, for \(G\subseteq H\subseteq K\), let \(u_*\) be the innermost
\(K\)-tube contributing a final \(G\)-component \(C\).  The \(H\)-component
of \(u_*\) containing \(C\) is the innermost intermediate contributor, and
its mark is again inherited from \(u_*\).  This proves

\[
r_{K,G}=r_{H,G}r_{K,H}
\]

as marked-tubing set maps.  Relabeling covariance is immediate from the
component construction.

Order preservation can be checked on the four generators of the marked face
order.

1. Resolving a broken source tube changes exactly those target components for
   which it is the innermost contributor, resolving each from broken to the
   same chosen mark.
2. Adding a thin source tube either adds thin target components or changes a
   coincident component from broken to thin.  Any intervening source tube is
   thin because the added tube lies in a nonthick paint region, so no
   thick-to-thin target change can occur.
3. Adding a thick source tube adds only thick components inside thick target
   components.  Every source ancestor of a thick tube is thick.
4. In the broken-family move, treat each \(G\)-component \(B\) of the
   resolved source tube separately.  Components of the new closely nested
   broken tubes are either invisible because an older inner tube remains
   selected, coincide with \(B\), or form a compatible family of broken tubes
   closely nested in \(B\).  In the last case \(B\) changes from broken to
   thick, exactly the fourth target refinement move.  Components cannot gain
   an intervening target tube: such a tube would come from a source tube
   strictly between a new broken tube and its resolved parent, contradicting
   close nesting.

Disjoint affected target components can be refined successively.  Hence every
source cover maps to a target refinement, and transitivity proves all-graph
face-poset order preservation.

The complete cellular theorem still must:

- construct a marked source lift for every target face, proving
  surjectivity;
- extend from simple edge deletion to the pseudograph operations required by
  loop contraction, if those operations are used later.

## Consequence for the Nima program

At present there is no evidence that bare carrier geometry causes the
two-sewing anomaly.  The graph-deletion maps commute strictly throughout the
entire audited range.  Nontrivial coherence should therefore be sought first
in the Ward/Brauer coefficient system—especially its circuit intersection
data—rather than inserted into every cellular transition.

## Evidence boundary

Proved for arbitrary finite connected simple graph inclusions:

- totality and marked validity;
- face-poset order preservation;
- dimension nonincrease;
- relabeling covariance;
- strict compositional functoriality as a set map.

Proved by exact finite enumeration through five vertices:

- face surjectivity in all stated cases;
- all stated counts and zero-failure results;
- minimal three-vertex failures of forget-only and outermost marking;
- strict two-edge functoriality in the audited range.

Not proved:

- all-graph face surjectivity;
- affine realizability on the original convex graph multiplihedra;
- compatibility with the scalar-derived physical coefficient system;
- loop-contraction or pseudograph functoriality.

## Next falsifier

Construct a marked lift of an arbitrary target face.  The lift must resolve
the case in which several disjoint \(G\)-tubes become adjacent in \(H\) and
therefore can only arise as components of nested \(H\)-tubes, while retaining
their possibly different marks.  A proof or counterexample decides whether
the all-graph cellular functor is face surjective.

## Internal dependencies

- Entry 56: marked-theta graph-multiplihedral carrier.
- Entry 57: Ward coefficient system and graph-cycle kernel.
- Working context: `research/nima/ward_brauer_math_context.md`.
