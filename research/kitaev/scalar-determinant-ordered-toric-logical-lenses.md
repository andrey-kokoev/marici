# From stable loop bits to the toric logical operator algebra

## Question

What additional structure appears when the stable Carrier intersection pairing is interpreted through the quantum coefficient lens rather than as scalar logical labels?

Let

\[
H=H_1(T^2;\mathbf F_2)\simeq\mathbf F_2^2,
\qquad
H^\vee=H_1(T^{2,*};\mathbf F_2)\simeq\mathbf F_2^2.
\]

Set \(V=H\oplus H^\vee\). The primal-dual intersection pairing defines the symplectic form

\[
\omega((a,\alpha),(b,\beta))
=
\alpha(b)+\beta(a).
\]

## Claim boundary

Scalar probes use elements of \(H^\vee\) to label the four classes in \(H\). They retain the additive evaluation pairing but do not retain operator order.

The quantum lift assigns Weyl operators \(W_v\) to \(v\in V\), with multiplication twisted so that

\[
W_vW_w=(-1)^{\omega(v,w)}W_wW_v.
\]

Equivalently, choose primal generators \(Z_1,Z_2\) and dual generators \(X_1,X_2\). Then

\[
Z_iX_j=(-1)^{\delta_{ij}}X_jZ_i,
\]

while equal-type generators and generators with unequal indices commute.

The resulting complex twisted group algebra is

\[
\mathbf C^\omega[V]\cong M_4(\mathbf C).
\]

One direct construction sends the generators to the two-qubit Pauli operators

\[
Z_1=Z\otimes I,\quad X_1=X\otimes I,\quad
Z_2=I\otimes Z,\quad X_2=I\otimes X.
\]

Their sixteen ordered monomials form a basis of \(M_4(\mathbf C)\). Hence the map from the twisted algebra is surjective; both sides have complex dimension sixteen, so it is an isomorphism.

Every nonzero representation of \(M_4(\mathbf C)\) is a direct sum of copies of its four-dimensional defining module. Therefore a faithful realization requires Hilbert-space dimension at least four, and dimension four is attainable. This is distinct from the two scalar bits required to identify an element of \(H\).

A commutative coefficient target cannot preserve the quantum multiplication. If \(A\) is commutative and \(\phi\) is a unital algebra map, anticommuting generators would give

\[
\phi(Z_i)\phi(X_i)
=
-\phi(X_i)\phi(Z_i)
=
-\phi(Z_i)\phi(X_i),
\]

so \(2\phi(Z_i)\phi(X_i)=0\). Over characteristic zero, invertible Pauli images make this impossible. Thus scalar characters can retain logical labels or expectation values, but not the ordered constructor algebra.

A determinant-only lens is also not faithful on the logical algebra. For any commutator of invertible matrices,

\[
\det(ABA^{-1}B^{-1})=1.
\]

For the four-dimensional toric logical representation, the anticommutation commutator is \(-I_4\), whose determinant is also \(1\). The determinant phase therefore erases this central commutator even though the ordered holonomy retains it.

These conclusions concern the finite toric logical algebra. They do not prove that a proposed physical interface can execute every matrix in \(M_4(\mathbf C)\), nor that scalar measurement statistics reconstruct an unknown quantum state without an authorized measurement family.

## Disposition

The same Carrier pairing has three inequivalent coefficient realizations:

| coefficient lens | retained object | first lost structure |
|---|---|---|
| additive scalar | two logical bits in \(H\) | ordered multiplication |
| determinant line | multiplicative volume or phase character | commutator data with unit determinant |
| ordered quantum holonomy | twisted algebra \(M_4(\mathbf C)\) | physical executability remains external |

The number “two” counts minimal scalar classification ports. The number “four” is the minimal carrier dimension of a faithful representation of the ordered logical algebra. They answer different questions.

The first falsifier is one of:

1. the proposed pairing on \(V\) is degenerate, so the twisted algebra need not be simple;
2. the claimed operator assignment violates a Weyl relation;
3. fewer than sixteen monomials are shown independent while surjectivity is claimed;
4. a commutative readout is claimed to preserve anticommutation;
5. determinant agreement is used to infer equality of ordered holonomies;
6. algebraic faithfulness is used to infer executable physical control.

The shared Carrier contribution is the labelled primal-dual intersection form. The Pauli/Weyl twist, matrix algebra, and four-dimensional logical module require the quantum coefficient lens.
