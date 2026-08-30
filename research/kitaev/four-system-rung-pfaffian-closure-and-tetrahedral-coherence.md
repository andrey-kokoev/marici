# Four-system rung: Pfaffian closure and tetrahedral coherence

## Question

What new structure appears after the three-system interaction holonomy when a fourth system is added?

## Claim boundary

The four-system rung has two complementary meanings.

Algebraically, four is the first even size at which a purely real skew interaction can gap every defect mode. Categorically, four is the first size at which the triangle holonomies themselves must satisfy a coherence law.

### Pfaffian closure of four real skew defects

Let four real one-dimensional defect modes interact through a skew-symmetric matrix

\[
D=
\begin{pmatrix}
0&a_{12}&a_{13}&a_{14}\\
-a_{12}&0&a_{23}&a_{24}\\
-a_{13}&-a_{23}&0&a_{34}\\
-a_{14}&-a_{24}&-a_{34}&0
\end{pmatrix}.
\]

Its Pfaffian is

\[
\operatorname{Pf}(D)
=
a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23},
\]

and

\[
\det D=\operatorname{Pf}(D)^2.
\]

Thus four skew-coupled defects are fully paired exactly when the signed sum of the three perfect matchings is nonzero.

This is qualitatively new relative to three systems. Every real three-by-three skew matrix has a zero mode. Adding a fourth mode allows the odd obstruction to self-close, but closure depends on interference among three pairing channels rather than on one edge.

Deleting any one system returns an odd skew matrix and therefore restores a zero mode. The four-system packet is consequently minimally collective.

### What the coefficient lenses retain

The scalar determinant sees only

\[
\operatorname{Pf}(D)^2
\]

and loses the sign or phase of the pairing orientation.

The determinant-line lens retains the Pfaffian as the oriented square root of the determinant.

An ordered noncommutative lens must retain the three matching products with their order and incidence before combining them. Their cancellation or reinforcement can depend on commutators and cannot generally be reconstructed from a scalar determinant.

Thus rung four supplies a pinned example in which the three coefficient lenses separate:

- scalar lens: whether the aggregate pairing is singular;
- determinant-line lens: its oriented pairing phase;
- ordered lens: how the competing matchings compose.

### Tetrahedral coherence

Label the four systems \(1,2,3,4\). Their six pairwise interaction arrows form the edges of a tetrahedron. Each triangular face carries a holonomy

\[
\Omega_{ijk}=c_{ki}c_{jk}c_{ij}
\]

with the order chosen by face orientation.

The four faces must now fit together. In an additive Abelian lens, the oriented sum of face residues must vanish. In a multiplicative Abelian lens, the oriented product of face phases must equal one. In a noncommutative lens, face holonomies must first be transported to a common basepoint and then multiplied in the prescribed order.

This is the discrete Bianchi or tetrahedral coherence law. Its failure is a volume defect: pairwise interactions exist and every triangle may be meaningful, yet the comparison of triangle comparisons is path-dependent.

### Self-closure versus a new constructor

If all edge arrows are globally defined in one strict Abelian coefficient system and every face holonomy is their ordinary coboundary, tetrahedral coherence is automatic:

\[
\delta^2=0.
\]

In that case rung four unexpectedly self-closes. It introduces no new source datum; it certifies that the triangle residues really came from common edge data.

A new constructor is required only when at least one of the following occurs:

- composition is partial and some edge products live on different domains;
- local frames require nontrivial transport before face comparison;
- the coefficient system is noncommutative;
- face maps are independently supplied rather than derived from edges;
- completion changes the order or domain of composition;
- an associator is nontrivial.

Then the tetrahedral comparison is a genuine 3-cell rather than an automatic identity.

### Associator interpretation

Three systems compare the two ends of a compositional loop. Four systems compare alternative ways of composing three interactions. In a weak categorical setting, the relevant datum is an associator. Its coherence is the pentagon law on four composable objects.

A failure of the pentagon is not another missing state coordinate. It is a failure of the law that says different bracketings implement the same constructor.

This yields the rung interpretation:

\[
2\text{ systems}:\text{ pairing},
\]

\[
3\text{ systems}:\text{ curvature or holonomy},
\]

\[
4\text{ systems}:\text{ coherence of holonomy or associator}.
\]

### Finite falsifiers

The proposed fourth rung is falsified as genuinely new if every tetrahedral residue reduces identically to \(\delta^2=0\) from already authorized edge data.

It is required if one can exhibit:

- four compatible pairwise systems;
- well-typed triangle holonomies on all faces;
- two legal composites between the same higher boundary data;
- a nonidentity discrepancy between those composites.

For skew defect pairing, the exact finite falsifier is

\[
a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}=0.
\]

All pairwise arrows may be nonzero while the three matching channels cancel, leaving the full four-system interaction singular.

### Programme implication

The next source-native experiment should use four objects only after a real triangle has been instantiated. Construct its fourth compatible extension and ask two questions separately:

1. Does the Pfaffian pairing close the odd defect left by every three-object restriction?
2. Is the tetrahedral holonomy forced to close by existing edge data, or does it expose a nontrivial associator?

The first is an operator pairing question. The second is a constructor-coherence question. Their numerical shadows can coincide, but their authority and falsifiers differ.

## Disposition

Adding the fourth system may be the rung that unexpectedly self-closes. For real skew defects, it can close the unavoidable odd zero mode through a nonzero Pfaffian. For interaction holonomies, it self-closes automatically when all faces are coboundaries of one strict edge system.

If it does not self-close, the residue is categorically sharper than the three-system loop phase: it is a 3-cell or associator anomaly measuring whether the laws of composition themselves compose. This is the correct next-rung hypothesis, with the Pfaffian and tetrahedral Bianchi identities as its smallest exact tests.