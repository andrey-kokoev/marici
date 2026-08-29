# Prime-scale seam observability is finite but not uniformly complete

## Result

The prime-scale action used in the finite observability packet is source-derived. Prime attachment translates the additive boundary coordinate by \(\log p\), and the infinitesimal Mellin action therefore acts on a prime-labelled state by the label \(\lambda_p=\log p\).

For a finite prime set \(P=\{p_1,\ldots,p_m\}\), let

\[
A_P=\operatorname{diag}(\lambda_{p_1},\ldots,\lambda_{p_m})
\]

on the sheet-odd sector and let the aggregate seam observer be

\[
J_P=(1,\ldots,1).
\]

The finite Krylov family is

\[
J_P,\ J_PA_P,\ldots,J_PA_P^{m-1}.
\]

Its matrix is Vandermonde. Distinct primes have distinct logarithms, so its determinant is

\[
\prod_{i<j}(\log p_j-\log p_i)\ne0.
\]

Thus every finite odd prime-difference packet is observable from the seam after source-derived Mellin differentiation. This validates the finite six-column result without converting it into a static boundary isomorphism.

## Completion falsifier

No fixed finite derivative order supplies a cutoff-independent observability bound on the unrestricted prime packet.

For a fixed order \(K\), take two primes \(p<q\) with bounded gap. Such pairs exist at arbitrarily large scales. On the normalized odd difference \(v_{p,q}=e_p-e_q\),

\[
J A^k v_{p,q}=(\log p)^k-(\log q)^k.
\]

For every fixed \(k\),

\[
|(\log q)^k-(\log p)^k|
\le k(\log q)^{k-1}\log(q/p),
\]

and a bounded prime gap gives

\[
\log(q/p)=O(1/p).
\]

Hence every component of the fixed stack \(J,JA,\ldots,JA^K\) tends to zero while \(\lVert v_{p,q}\rVert\) remains constant. Its lower observability bound is therefore zero.

The static rank-four kernel is not removed by one finite global observer tower. It is separated only cutoffwise.

## Categorical interpretation

The Mellin action is an authorized endomorphism of the source packet. Precomposing the seam observer with its powers generates a jointly faithful finite family. This does not violate rank monotonicity of any individual observer composite.

Completion changes the verdict:

- finite source objects: the action-generated observer family is faithful;
- unrestricted completed source: every fixed finite truncation has approximate kernel;
- admissible completion: must either retain the full action orbit with a declared topology or add a genuinely label-discrete port.

The remaining construction is not another static row. It is a topology and admissibility law for the infinite Mellin-observer orbit.

## Finite falsifier for any proposal

Given a proposed fixed order \(K\) and claimed lower bound \(c>0\), evaluate the normalized two-prime difference on a sufficiently large bounded-gap pair. If

\[
\sum_{k=0}^{K}|(\log p)^k-(\log q)^k|^2<c^2\lVert e_p-e_q\rVert^2,
\]

the claimed uniform observability law fails.

## Verdict

Prime-scale dynamics is source-authorized and repairs the finite rank defect. It does not repair completion. The next admissible object is an infinite action-generated observer module with a source-derived topology, not a larger finite Vandermonde packet.
