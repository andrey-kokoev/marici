# Adams-seam coherence is a holonomy unitarization problem

## Concrete transport problem

Let \(\mathcal G_X(C)\) be the finite constructor transport graph at cutoff \(X\) over a compact off-seam region \(C\). Its vertices are typed source/feature fibers \(H_s\), and its authorized arrows are invertible transports
\[
T_\alpha:H_s\to H_t.
\]

The next theorem seeks a positive metric field
\[
G_s>0
\]
such that every authorized arrow is unitary between the corresponding metrics:
\[
T_\alpha^*G_tT_\alpha=G_s.
\]

This is simultaneous unitarization of the complete transport representation, not separate normalization of Adams and seam factors.

## Tree theorem

On a connected spanning tree, choose a positive base metric \(G_{s_0}\). For the unique tree path \(P_{s_0s}\) from \(s_0\) to \(s\), define
\[
G_s=(T_{P_{s_0s}}^{-1})^*G_{s_0}T_{P_{s_0s}}^{-1}.
\]
Then every tree edge satisfies the metric transport equation.

Thus finite existence is automatic on a tree when all arrows are invertible. The obstruction lies entirely in cycle consistency.

## Holonomy criterion

For a based cycle
\[
\gamma:s=s_0\to s_1\to\cdots\to s_n=s,
\]
define
\[
H_\gamma=T_{s_{n-1}s_n}\cdots T_{s_0s_1}.
\]
A transported metric is path-independent exactly when
\[
H_\gamma^*G_sH_\gamma=G_s
\]
for every cycle.

Equivalently, the holonomy representation is conjugate into the unitary group of one positive metric.

It is enough to test a cycle basis at finite cutoff, provided the resulting invariant metric is checked against all relations and higher coherence cells.

## One-dimensional falsifier

For a one-dimensional cycle with holonomy \(h\neq0\), the metric equation is
\[
\bar hGh=G.
\]
For \(G>0\), this implies
\[
|h|=1.
\]
Therefore any cycle with \(|h|\neq1\) is an immediate obstruction.

A positive Adams scale can be locally absorbed along a tree but becomes intrinsically amplifying when its product around an authorized cycle has modulus different from one.

## Higher-dimensional criterion

A single finite-dimensional matrix \(H\) preserves some positive-definite metric exactly when it is similar to a unitary matrix. Equivalently, \(H\) is diagonalizable and all eigenvalues lie on the unit circle.

Hence the basic obstructions are:

- an eigenvalue off the unit circle;
- a non-semisimple Jordan block at a unit-circle eigenvalue.

For a family of holonomies, each being individually unitarizable is not sufficient. They must preserve one common positive metric.

The common metric is a feasible point of the linear matrix equations
\[
H_\gamma^*GH_\gamma=G
\]
with \(G>0\).

## Combined Adams-seam holonomy

Factor an authorized edge as
\[
T_\alpha=a(\alpha)U_\alpha,
\]
where \(U_\alpha\) is the constructed moving-seam unitary and \(a(\alpha)>0\) is the typed Adams scale.

For a cycle,
\[
H_\gamma
=
\left(\prod_{\alpha\in\gamma}a(\alpha)\right)
U_\gamma
\]
when the scalar scale commutes with the geometric transport.

Then unitarizability forces
\[
\prod_{\alpha\in\gamma}a(\alpha)=1.
\]
If weights are operator-valued or grade-dependent, the scalar reduction is invalid; the full ordered holonomy must be tested.

Thus the key source question is whether the positive scale cocycle has trivial holonomy in the actual type-fiber transport system.

## Coboundary metric

If there are positive vertex weights \(g_s\) such that
\[
a(\alpha)^2=\frac{g_s}{g_t},
\]
then the scalar Adams cocycle is a coboundary and can be absorbed into
\[
G_s=g_sG_s^{(0)},
\]
where \(G^{(0)}\) is invariant under the geometric unitary transport.

Path independence of \(g_s\) is exactly the cycle-product condition.

However, algebraic absorption is not yet completion stability.

## Uniform metric equivalence

Relative to the frozen source norm, require
\[
m_CI\le G_{X,s}\le M_CI
\]
for all cutoffs \(X\) and all \(s\in C\), with
\[
0<m_C\le M_C<\infty.
\]

This gives separate uniform forward and inverse equivalence:
\[
m_C^{1/2}\|x\|
\le
\|x\|_{G_{X,s}}
\le
M_C^{1/2}\|x\|.
\]

Finite invariant metrics can exist while \(m_C\to0\) or \(M_C\to\infty\). In that case the unitarizing metric merely hides completion-scale amplification.

## Quantitative hostile

Take a path graph closed by one edge so the total cycle holonomy is \(1\), but let tree-edge scales be
\[
a_j=c,\qquad c>1,
\]
for \(j=1,\ldots,n\), and let the closing edge have scale \(c^{-n}\).

The cycle is algebraically unitarizable. Transporting a base metric along the tree gives vertex weights varying like
\[
c^{-2j}.
\]
As \(n\to\infty\),
\[
\inf_jg_j\to0.
\]
No uniform lower metric bound survives completion.

Thus trivial holonomy is necessary but not sufficient for uniform source equivalence.

## Authority and topology

A solution \(G_s\) is admissible only if it is source-derived or admitted by an explicit metric constructor. An arbitrary solution of the matrix equations does not authorize changing the source topology.

The metric field must also preserve:

- projective seminorm transport;
- cutoff inclusions;
- associators and unitors;
- endpoint and archimedean typing;
- reciprocal and Real structure;
- bounded-energy restricted limits.

## Finite theorem target

> On each finite constructor graph, the authorized transport representation admits a common positive metric field if and only if its cycle holonomies preserve one positive base metric. The theorem returns either the metric field or a cycle witness with spectral/Jordan obstruction.

The quantitative extension must additionally return \(m_{X,C}\) and \(M_{X,C}\).

## Completion theorem target

> The finite invariant metric fields can be chosen cutoff-compatible and uniformly equivalent to the frozen source metric on every compact off-seam region.

This theorem classifies the Adams-seam system:

- source-unitary if \(G\) is the source metric;
- unitarizable if a source-authorized uniformly equivalent \(G\) exists;
- merely bi-bounded if no invariant \(G\) exists but canonical composites have separate bounds;
- intrinsically amplifying if cycle or completion metric bounds fail.

## Next executable audit

For each finite cutoff:

1. build a spanning tree;
2. transport one base metric;
3. compute a cycle basis;
4. form ordered Adams-seam holonomies;
5. test common positive-metric feasibility;
6. report eigenvalue or Jordan witnesses;
7. compute extremal eigenvalues of every \(G_s\);
8. track their envelopes across cutoff and compact \(s\)-regions;
9. verify source authority and cutoff compatibility.

The first exact falsifier is the shortest cycle with nonunit-modulus holonomy. The first completion falsifier is a sequence of cycle-consistent metrics whose extremal eigenvalues escape.
