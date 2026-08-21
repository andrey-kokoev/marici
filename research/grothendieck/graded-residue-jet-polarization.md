# Degree reversal polarizes the graded Xi residue boundary

Sequence claim: \`seqclaim-17a47868dc921385d10f4852\` (1407).

Epistemic-graph event: 1457.

## Local source data

Let \`lambda\` be a real Xi zero of order \`m\), put

\`t=z-lambda\`,

and write

\`Xi(z)=u_lambda t^m+O(t^(m+1))\`,

where

\`u_lambda=Xi^(m)(lambda)/m!\`

is a nonzero real number. The spectral coordinate \`z\` is fixed by the
Mellin-dilation generator, so \`t\` and the graded jet basis

\`e_k=[t^k] in q^k/q^(k+1), 0<=k<m\`

are source-defined.

## Graded residue form

The leading form induced by the Grothendieck residue pairing on the
maximal-ideal associated graded is

\`R_lambda(e_i,e_j)
 =u_lambda^(-1) delta_(i+j,m-1)\`.

Thus the unpolarized form pairs complementary jet degrees and is indefinite
for \`m>1\), as found in Ledger 1405.

Define the degree-reversal polarization

\`C_lambda e_j=u_lambda e_(m-1-j)\`.

Then

\`h_lambda(x,y)=m R_lambda(x,C_lambda y)\`

has Gram matrix

\`h_lambda(e_i,e_j)=m delta_ij\`.

It is positive definite. No sign choice, square root, zero label, or
Gram--Schmidt order is used: the leading coefficient of Xi cancels the residue
normalization, and the local length \`m\` fixes the remaining scalar.

## Weil compatibility

For a Mellin transform \`G\`, use normalized jets

\`J_lambda(G)
 =(G(lambda),G'(lambda),...,G^(m-1)(lambda)/(m-1)!)\`.

The degree-zero line is the ordinary evaluation channel. Restricting the
polarized jet norm to it gives

\`h_lambda(G(lambda)e_0,G(lambda)e_0)
 =m |G(lambda)|^2\`,

exactly the local term in the scalar Weil form. Hence this polarization is a
positive multiplicity-sensitive extension of the Weil evaluation pairing,
not an unrelated square-sum norm.

The new derivative channels are forced by the maximal-ideal filtration and
the residue duality once one requires:

1. orthogonality of distinct jet degrees after semisimplification;
2. compatibility with complementary-degree residue pairing; and
3. Weil normalization on degree zero.

## Global conditional boundary

Let

\`H_J=direct_sum_(lambda real) (Gr_lambda,h_lambda)\`

and complete the algebraic sum. Define \`A_J\` to act as \`lambda I\` on
\`Gr_lambda\). Then, conditional on RH:

- \`A_J\` is self-adjoint;
- its spectrum is discrete with multiplicity equal to the Xi zero order;
- its resolvent is compact and \`A_J^(-1)\` is Hilbert--Schmidt; and
- symmetric regularization gives

  \`det_2(I-zA_J^(-1))=Xi(z)/Xi(0)\`.

On Mellin transforms for which the jet norm is finite, the boundary map is

\`g |-> (J_lambda(G))_lambda\`,

defined without a numerical zero list by the spectral local algebras of the
source-generated ideal quotient. The *entire-function quotient* contains finite-support
jet classes (use Xi divided by the relevant local factor and finite Hermite
interpolation), so its associated-graded image is dense in the completed
direct sum. This does not by itself prove that the original compactly
supported Mellin test family is dense in every jet degree; that narrower
source-domain question remains separate.

## Exact remaining gate

This construction removes the earlier multiplicity and polarization defects.
It still does not prove that all spectral points \`lambda\` are real. For a
nonreal zero, multiplication by \`lambda\` on its nonzero fiber cannot be
self-adjoint in any positive Hermitian metric. Therefore

\`the polarized jet boundary is self-adjoint iff RH\`.

The construction is source-derived and does not ingest a zero list, but the
determinant is read from the divisor of the theta-derived Xi quotient. Its
explanatory content is the canonical passage from the Mellin source quotient
to a positive multiplicity boundary; it does not prove the RH-equivalent
reality statement.

## Smallest falsifier

For a real double zero, \`R=[[0,u^(-1)],[u^(-1),0]]\` and
\`C=[[0,u],[u,0]]\`, so

\`2 R C=2 I_2\`.

For a nonreal double zero, the same algebraic formula can produce a norm only
after pairing conjugate fibers, but the diagonal operator retains eigenvalues
\`lambda\` and \`conjugate(lambda)\`; it is normal, not self-adjoint. A single
verified nonreal Xi zero falsifies the self-adjoint boundary.

## Scope

Conditional source-ideal-saturated entire-quotient jet boundary with exact
determinant. The remaining spectral condition is RH itself. Density of the
original Mellin test-function image in all jet degrees and the physical
coefficient--Betti relative-chain pushforward are not asserted.
