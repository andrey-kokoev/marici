# The meromorphic determinant target does not close the operator pyramid

## Question

Does construction of the canonical meromorphic determinant target supply the missing operator comparison or analytic fourth-to-source edge?

## Claim boundary

No. Determinant data forget the incidence/return factorization, while the independently constructed adjoint completion produces an autocorrelation Schur term rather than the endpoint Evans section. The exact remaining comparison is vector-valued and RH-bearing.

## Determinant forgetfulness

For a block colligation

$$
L(z)=
\begin{pmatrix}
A(z)&B(z)\\
B(z)^*&C(z)
\end{pmatrix},
$$

the determinant records the product of \(\det A\) with the Schur complement

$$
S(z)=C(z)-B(z)^*A(z)^{-1}B(z).
$$

It does not recover \(B\) and \(C\) separately. Distinct source/return blocks can have the same determinant and Schur scalar. Therefore the meromorphic determinant line is a necessary coherence shadow, not a reconstruction functor for the operator pyramid.

## Canonical adjoint mismatch

The source-forced history has endpoint Evans readout

$$
F(z)=E_0(D-z)^{-1}B_f.
$$

Canonical adjoint closure instead produces

$$
M_f(z)=B_f^\times(D-z)^{-1}B_f,
$$

which is quadratic source autocorrelation. No source-independent nowhere-zero unit identifies these two functions. Thus adjoining the metric adjoint does not construct the Evans determinant comparison.

## Exact remaining residual

For the independently constructed paired pencil, an Evans history \(u_z\) and labelled lift \(x_z\) enter the conservative kernel exactly when

$$
\mathcal R_U(z)
=
B^\dagger u_z+D_U(z)x_z
=0.
$$

At a zero of order \(m\), multiplicity preservation requires

$$
\partial_z^j\mathcal R_U(z_0)=0,
\qquad 0\le j<m.
$$

A scalar determinant identity cannot imply this complete prime/grade-valued equation without a source intertwining theorem.

## Consequence for the current programme

The determinant-line work establishes:

- correct finite-stage cumulant composition;
- direct Sonin orientation;
- reflected meromorphic divisor typing;
- uniqueness of any eventual scalar comparison.

It does not establish:

- the source lift \(Bx_\Phi=\Phi\) with bounded cutoff-natural control;
- vanishing of \(\mathcal R_U\);
- external G4 sewing identification;
- Hilbert analytic \(C_{41}\).

## Disposition

The determinant branch has reached its noncircular boundary. The next operator-level theorem is the source-derived vector residual identity \(B^\dagger u+D_Ux=0\), not another scalar determinant normalization. Proving that identity on the Xi divisor would already contain the RH confinement step and cannot be assumed as a filler.