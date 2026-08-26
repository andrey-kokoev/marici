# Fixed boundary jets cannot transfer the faithful theta seam Gram

## Status

Exact finite-cutoff obstruction. This packet attacks the proposed
moving-boundary oscillator–seam commutator at its smallest declared interface:
the common endpoint value and oriented normal jump.

## Source atoms

For distinct positive cuts

\[
0<q_1<\cdots<q_N,
\]

the retained seam atoms are

\[
h_{q_j}(t)
=
\mathbf 1_{0\le t\le q_j}\Phi(q_j-t).
\]

Their source-fixed boundary data are

\[
h_{q_j}(0)=\Phi(q_j),
\qquad
h_{q_j}'(0)=-\Phi'(q_j).
\]

Together with the tail derivative, the oriented jump is \(2\Phi'(q_j)\).

## Faithfulness of the full seam family

Assume \(\Phi\) is nonzero on every nonempty interval in its positive domain,
as for the theta source. Then the finite family

\[
h_{q_1},\ldots,h_{q_N}
\]

is linearly independent.

Indeed, on \((q_{N-1},q_N)\), every atom except \(h_{q_N}\) vanishes. Hence a
linear relation forces the coefficient of \(h_{q_N}\) to vanish. Descending
induction removes all coefficients.

Consequently the seam Gram matrix

\[
(K_X)_{ij}=\langle h_{q_i},h_{q_j}\rangle
\]

is positive definite and

\[
\operatorname{rank}K_X=N.
\]

## Rank of the declared boundary port

The endpoint-value and normal-jump interface is the matrix

\[
B_X
=
\begin{pmatrix}
\Phi(q_1)&\cdots&\Phi(q_N)\\
2\Phi'(q_1)&\cdots&2\Phi'(q_N)
\end{pmatrix}.
\]

Therefore

\[
\operatorname{rank}B_X\le2.
\]

Every quadratic form transported only through this port has the form

\[
Q_X=B_X^*MB_X
\]

for some fixed interface matrix \(M\), and hence

\[
\operatorname{rank}Q_X\le2.
\]

For \(N>2\), there is a nonzero coefficient vector \(c\) satisfying

\[
B_Xc=0.
\]

But seam faithfulness gives

\[
c^*K_Xc>0.
\]

Thus no finite constant \(C\) can satisfy

\[
K_X\le C B_X^*B_X.
\]

Equality with the seam Gram is also impossible.

## General finite-jet obstruction

The same argument applies to any fixed jet order \(r\). Let

\[
B_X^{(r)}
=
\left(
\Phi^{(k)}(q_j)
\right)_{
0\le k\le r,
1\le j\le N
}.
\]

Then

\[
\operatorname{rank}B_X^{(r)}\le r+1.
\]

For every \(N>r+1\), the jet port has a nonzero invisible coefficient packet
while the full seam Gram remains positive on it. Therefore no fixed finite
boundary jet can carry a cutoff-uniform faithful seam energy.

This is stronger than a failure of a particular coefficient or normalization.
It is a representation-capacity obstruction.

## Consequence for the commutator route

A commutator that factors only through

\[
\bigl(\Phi(q),2\Phi'(q)\bigr)
\]

cannot reproduce or dominate the full labelled seam Gram. The direct proposal
therefore fails unless the commutator has additional state-bearing output.

The source-derived alternatives are sharply constrained:

1. retain a boundary history indexed by the moving cut;
2. retain an infinite jet or analytic germ with a source topology;
3. introduce a genuinely label-discrete valuation/Fock boundary port;
4. derive a nonlocal arithmetic kernel whose rank grows with the cutoff.

Merely adding finitely many endpoint derivatives does not repair the problem.

## Shape derivative interpretation

For the moving projection

\[
(P_qf)(t)=\mathbf 1_{t\le q}f(t),
\]

formal differentiation gives the boundary distribution

\[
\partial_qP_q=|q\rangle\langle q|.
\]

At a single cut this is a rank-one boundary form. Allowing the cut parameter
to vary produces a boundary field; collapsing that field to a fixed endpoint
jet destroys its growing rank. The distinction is physical: instantaneous
boundary data and boundary history are different state objects.

## Minimal finite falsifier

Choose any three distinct cuts \(q_1<q_2<q_3\). Solve

\[
B_Xc=0
\]

for a nonzero \(c\in\mathbb C^3\). Linear independence of the seam atoms then
forces

\[
\left\|
\sum_{j=1}^3c_jh_{q_j}
\right\|^2>0.
\]

This three-label packet is the smallest falsifier of every proposed
endpoint-value plus normal-jump energy transfer.

## Revised physical target

The Evans–Krein colligation cannot use a finite boundary sensor as its entire
Hamiltonian. Its boundary object must itself be dynamical. Symbolically, the
required coupling has the type

\[
\mathcal H_{\mathrm{osc}}
\longrightarrow
\mathcal B_{\mathrm{history}}
\longrightarrow
\mathcal H_{\mathrm{seam}},
\]

where the middle space retains enough source information for its finite-cutoff
rank to grow with the labelled seam state.

The physical analogy has therefore become more specific: this is not a point
interaction with two boundary coordinates. It is a transmission system with
memory, or an infinite-dimensional boundary control system.

## Scope

This packet rules out only couplings that factor through a fixed finite jet at
the seam. It does not rule out a moving boundary field, an analytic germ,
valuation-resolved incidence, or another source-derived infinite-rank
commutator. It does not construct the Evans determinant or prove RH.
