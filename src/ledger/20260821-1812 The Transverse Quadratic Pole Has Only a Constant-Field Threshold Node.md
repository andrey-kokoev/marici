# 1812 — The Transverse Quadratic Pole Has Only a Constant-Field Threshold Node

## Question

Does Entry 1811's quadratic coefficient pole acquire a new kinematic branch
when specialized to the central threshold divisor \(\tau=0\)?

## Exact factorization

Let

\[
L=
\begin{pmatrix}a&b\\c&d\end{pmatrix},
\qquad
D=ad-bc\neq0.
\]

At \(\tau=0\), the quadratic pole equation is

\[
q(h)=h^TL^{-T}L^{-1}h=0.
\]

Writing \(x=L^{-1}h\) gives

\[
q=x_1^2+x_2^2.
\]

Equivalently,

\[
q(h)=
\frac{
(dh_1-bh_2)^2+(-ch_1+ah_2)^2
}{D^2}.
\]

Its binary discriminant is

\[
\boxed{
\operatorname{disc}_h(q)=-\frac4{D^2}.
}
\]

Therefore its square class is the constant \(-1\). Over the constant étale
extension \(\mathbb Q(i)\),

\[
q=
\frac{((d-ic)h_1+(-b+ia)h_2)
((d+ic)h_1+(-b-ia)h_2)}{D^2}.
\]

## Result

The central fiber is the ordinary node

\[
uv=0
\]

after a constant field extension and an invertible normal-coordinate change.
Its vanishing-cycle rank is one and its nodal monodromy is trivial:

\[
T=1.
\]

No kinematics-dependent Kummer character is introduced. In particular, the
factorization does not define a new kinematic carrier divisor.

This is a statement about the \(g_5\)-threshold normal \(\tau\). It is not a
total-energy specialization.

## Architectural consequence

The 22 quadratic quotients may have different labelled normal matrices
\(L\), but their central nodal square class is universally constant. Their
apparent algebraic factorization complexity is therefore coordinate data in
the coefficient system, not new carrier incidence.

## Next falsifier

Construct the supported nearby-cycle comparison from the threshold
logarithmic extension to this nodal quotient. Determine whether the nodal
rank-one line is exactly the iterated residue of the existing threshold and
two wall maps, including orientation and cyclic transport.

## Evidence

- research/benincasa/checkers/five_site_g5_transverse_pair_threshold_node.py
- research/benincasa/results/five-site-g5-transverse-pair-threshold-node.json
- Entry 1811
- allocator claim: seqclaim-b4e58c8b6c08586c0e958143
