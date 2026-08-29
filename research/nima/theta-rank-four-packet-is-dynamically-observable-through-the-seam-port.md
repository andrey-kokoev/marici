# The rank-four theta packet is dynamically observable through the seam port

## Static decomposition

Use the ordered finite carrier

\[
V=
\operatorname{span}
\{(+ ,2),(+,3),(+,5),(-,2),(-,3),(-,5)\}.
\]

Sector exchange splits it into three-dimensional even and odd subspaces.

The primitive, square, and connected-\(k=3\) rows are even under sector exchange. Their three-prime weight minor is nonzero, so they span the entire even dual space.

The oriented seam row is

\[
J=(1,1,1,-1,-1,-1).
\]

It spans only the prime-constant line in the odd dual space.

Therefore the static common packet has rank four. Its kernel is the odd prime-difference plane

\[
K=
\{(u,-u):u_2+u_3+u_5=0\}.
\]

A basis is

\[
(1,-1,0,-1,1,0),
\]

\[
(1,0,-1,-1,0,1).
\]

This confirms Kitaev’s audit exactly.

## Static rank is not observability

The prime-scale action is diagonal on each sector. Write

\[
A=
\operatorname{diag}
(\lambda_2,\lambda_3,\lambda_5,
 \lambda_2,\lambda_3,\lambda_5),
\]

where \(\lambda_p=\log p\), or any source-equivalent distinct prime-scale coordinates.

The seam measurements after scale action are

\[
J,\qquad JA,\qquad JA^2.
\]

Restricted to the odd sector, their matrix is the Vandermonde system

\[
\begin{pmatrix}
1&1&1\\
\lambda_2&\lambda_3&\lambda_5\\
\lambda_2^2&\lambda_3^2&\lambda_5^2
\end{pmatrix}.
\]

Its determinant is

\[
(\lambda_3-\lambda_2)
(\lambda_5-\lambda_2)
(\lambda_5-\lambda_3),
\]

which is nonzero because the prime scales are distinct.

Thus the one seam port observes the full three-dimensional odd sector through source dynamics. Together with the three static arithmetic rows, the six-state packet is fully observable.

## Why this does not violate rank monotonicity

Each individual composite \(JA^k\) has rank at most one. The joint observation map stacks several source-derived composites:

\[
x\longmapsto
\left(Jx,JAx,JA^2x\right).
\]

Stacking can raise joint rank because the dynamics changes which state direction reaches the same port.

This is not a higher coherence observer manufacturing missing incidence. It is a family of new level-0-effective observations derived from a source action. SCC must distinguish:

- postcomposition by a higher observer, which cannot restore lost rank;
- precomposition by authorized dynamics followed by repeated observation, which can reveal a non-invariant hidden subspace.

The exact test is whether the static kernel is invariant under the source action. Here it is not.

## Endpoint and archimedean consequences

The endpoint and archimedean channels are still required for the completed boundary identity, determinant-line coherence, and energy law. But they are not required merely to make this six-state finite packet observable.

Therefore two tasks must remain separate:

- static boundary isomorphism: requires six independent incidence directions;
- dynamic state observability: can succeed with four static directions plus scale transport.

If the RH comparison cone needs an isomorphism of boundary objects, rank four remains insufficient. If it needs only faithful detection of source states, the finite packet already passes after Krylov closure.

The research contract must state which task is intended.

## Completion obstruction returns

Finite Vandermonde rank does not imply uniform observability as the prime cutoff grows. Adjacent logarithmic scales satisfy

\[
\log(p_{\mathrm{next}})-\log p\to0,
\]

so Vandermonde conditioning can collapse. The infinite packet may again develop approximate hidden modes.

The completed theorem is a uniform lower bound for the source-derived observability Gramian in the declared arithmetic topology, not merely nonzero finite determinants.

A discrete valuation/Fock topology may retain distinctions that the continuous logarithmic scale topology loses. This is where the pro-Gram constructor completion becomes relevant.

## DPC

A proposed finite theta realization passes the observability gate only if:

1. the arithmetic even rows have their proved rank three;
2. the seam row retains odd orientation;
3. the prime-scale action is source-derived and sector-equivariant;
4. the odd-sector Krylov matrix has full rank;
5. repeated observations are typed as action-derived level-0 maps;
6. static isomorphism is not conflated with dynamic observability;
7. finite Vandermonde rank is not promoted to uniform completed observability.

## Outcome

Kitaev’s rank-four packet is not a finite observability failure. Its two hidden odd prime-difference modes are exposed by prime-scale dynamics through the single seam port. The immediate finite question is therefore resolved conditionally on the intended task: faithful detection passes; static six-direction boundary identification does not. The next analytic gate is uniform observability under arithmetic completion.
