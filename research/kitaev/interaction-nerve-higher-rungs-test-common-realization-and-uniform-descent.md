# Interaction nerve: higher rungs test common realization and uniform descent

## Question

What exactly do the two-, three-, and four-system rungs certify, and when does the tower self-close rather than demand another constructor?

## Claim boundary

Let systems be vertices of a simplicial interaction nerve. An authorized comparison between systems \(i\) and \(j\) is an edge map \(g_{ij}\). Assume initially that the maps are invertible on the relevant defect objects.

### Rung two: existence of transport

An edge \(g_{ij}\) says that one system's defect frame can be transported to the other. This is relational existence. It does not say that different transports agree.

Pairwise validity is therefore only a 1-skeleton theorem.

### Rung three: path independence around a face

On a triangle, define the face defect

\[
h_{ijk}=g_{ik}^{-1}g_{jk}g_{ij}
\]

with conventions fixed so that \(h_{ijk}=I\) means direct and two-step transport agree.

A nonidentity \(h_{ijk}\) is curvature or contextual holonomy. Every edge can be individually valid while the three cannot be restrictions of one flat global frame.

Thus rung three asks whether pairwise comparisons come from one common realization.

### Rung four: coherence among face witnesses

Suppose triangle defects are themselves equipped with fillers or coherence maps \(\alpha_{ijk}\). On four vertices, there are several ways to combine those face fillers. Their discrepancy is a tetrahedral 3-cell.

In a strict Abelian system where all face data are derived from globally defined edges, the tetrahedral residue vanishes automatically:

\[
\delta^2g=0.
\]

In a noncommutative system, the corresponding transported ordered product of face holonomies is the identity. This is the discrete Bianchi law.

Therefore a nonzero tetrahedral residue has a very specific meaning: at least one face witness is not the boundary of the same global edge system, or composition is weak, partial, domain-changing, or anomalous.

The fourth rung is consequently a provenance auditor for the third rung.

### The self-closure criterion

A rung self-closes when all of its cells are functorially generated as boundaries of cells one degree lower in a strict admitted complex. Then the next residue vanishes by boundary-of-boundary.

A new constructor is required only when:

- fillers were chosen independently rather than derived;
- comparison maps live on incompatible domains or completions;
- transport changes local frames nontrivially;
- composition is noncommutative and lacks specified ordering;
- associativity holds only up to a noncanonical map;
- the lower cells form a torsor with no source-fixed reference.

This gives a disciplined stopping rule. Do not invent a higher tower until the canonical boundary construction fails.

### The associator obstruction

If edge composition is weakly associative, threefold composition carries an associator. Four objects generate five bracketings, and their comparison is the pentagon.

Pentagon failure is a 3-cocycle anomaly. It says the laws of composition do not themselves compose.

This is categorically different from a missing edge or triangle:

- missing edge: no transport;
- nontrivial triangle: transport is path-dependent;
- nontrivial tetrahedron or pentagon: the chosen path-dependence witnesses are mutually incoherent.

### Effectivity is stronger than cocycle vanishing

Even exact vanishing of all finite obstruction cells may not construct a global object. Descent data must be effective: there must exist an admitted global constructor whose restrictions produce the local systems and their comparisons.

This separates:

\[
\text{formal cocycle coherence}
\neq
\text{source-authorized global realization}.
\]

A fitted family of transition maps can satisfy every finite cocycle equation without belonging to the source constructor monoid.

### Uniform descent

Completion adds a quantitative layer. Let every edge be invertible and every triangle be exactly flat. A global completed realization may still fail if transition condition numbers escape.

For example, scalar transitions can obey

\[
g_{12,N}=N,\qquad
g_{23,N}=N,\qquad
g_{31,N}=N^{-2},
\]

so the triangle holonomy is exactly one for every N, while edge norms and inverse norms diverge.

Thus exact descent does not imply uniformly conditioned descent.

The completed nerve requires source-derived metrics and bounds

\[
\sup_N\|g_{ij,N}\|<\infty,\qquad
\sup_N\|g_{ij,N}^{-1}\|<\infty
\]

on the admitted reachable sectors, together with uniform bounds for higher coherence maps.

### Conditioned obstruction tower

The full hierarchy is therefore doubled:

| Algebraic rung | Quantitative strengthening |
|---|---|
| edge exists | edge gain bounded below |
| triangle commutes | loop transport uniformly conditioned |
| tetrahedron or pentagon closes | higher fillers remain uniformly controlled |
| descent datum is coherent | descent is effective in the completed source category |

A scalar projection may preserve every algebraic equality while destroying all four quantitative statements.

### Relation to the top coherencer

The top coherencer is not another observer of each system. It compares the final source-side coherencer with the final behavior-side coherencer over the entire nerve.

Its job is to establish that:

1. both sides use the same edge incidence;
2. their triangle holonomies match;
3. their tetrahedral or associator witnesses agree;
4. the agreement is effective and uniformly conditioned.

This makes precise the earlier convergence with Nima and Strominger: the highest cell compares coherencers, not raw states.

### Falsifiers

The common-realization conjecture is falsified by the first of:

- valid pairwise edges with nonidentity triangle holonomy;
- valid face fillers with nonidentity tetrahedral residue;
- exact finite cocycles with no source-authorized global constructor;
- exact global realization whose transition condition numbers diverge;
- scalar equality after forgetting a nontrivial typed cocycle.

## Disposition

The interaction tower has a clean semantics: two systems test transport, three test flatness, four test coherence and provenance of flatness, and completion tests uniform effectivity. Higher rungs are warranted only when the preceding cells are not canonical boundaries in one strict source complex.

This is important because it predicts both outcomes without bias. The fourth rung may self-close, proving the lower comparisons share one realization. Or it may expose a genuine associator anomaly, proving that the constructor theory itself lacks a composition law. Either result is more informative than adding another scalar observable.