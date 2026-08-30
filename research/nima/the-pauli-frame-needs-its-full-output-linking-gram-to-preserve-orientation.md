# The Pauli frame needs its full output linking Gram to preserve orientation

## The summed frame is coercive but not faithful on polarization

Let

\[
\Phi(M)=XMX+YMY.
\]

For an endpoint Gram

\[
G=
\begin{pmatrix}
a&z\\
\bar z&b
\end{pmatrix},
\]

one has

\[
\Phi(G)=2\operatorname{diag}(b,a).
\]

This proves the desired frame lower bound, but it erases the complete
off-diagonal coordinate \(z\), including its reciprocal odd sign.

The loss is already visible on matrix units:

\[
\Phi(|e_1\rangle\langle e_2|)=0,
\qquad
\Phi(|e_2\rangle\langle e_1|)=0.
\]

Therefore the summed Pauli frame cannot itself be the quadratic constructor
identity.

## The correct retained object

Write the two output maps as

\[
O_X=J_pX,
\qquad
O_Y=J_pY.
\]

Their full output linking Gram is the operator-valued matrix

\[
\mathbb G_p^{\mathrm{out}}
=
\begin{pmatrix}
O_X^*O_X&O_X^*O_Y\\
O_Y^*O_X&O_Y^*O_Y
\end{pmatrix}
=
\begin{pmatrix}
XG_pX&XG_pY\\
YG_pX&YG_pY
\end{pmatrix}.
\]

The diagonal sum is

\[
O_X^*O_X+O_Y^*O_Y
=
2\operatorname{diag}(b_p,a_p),
\]

and supplies uniform observability. The mixed output blocks retain the
orientation and relative phase discarded by that sum.

Thus the Pauli construction has two logically different shadows:

- its diagonal trace is a uniformly coercive frame operator;
- its full linking Gram is the faithful polarized constructor datum.

## Faithfulness

The linking Gram determines the original endpoint Gram. For example,

\[
G_p=X(O_X^*O_X)X.
\]

More importantly, retaining the declared output labels prevents an
orientation-reversing exchange of the \(X\) and \(Y\) channels from being
hidden by the total energy.

Faithfulness does not imply uniform invertibility of the raw Gram. The soft
endpoint disagreement remains soft. What becomes uniformly invertible is the
analysis map into the doubled output space.

## Correct quadratic functoriality theorem

Let \(\widetilde O_X\) and \(\widetilde O_Y\) be the corresponding typed
theta-history output maps obtained from the fixed linear Adams constructor.
The required local theorem is

\[
O_\alpha^*O_\beta
=
\widetilde O_\alpha^*\widetilde O_\beta,
\qquad
\alpha,\beta\in\{X,Y\},
\]

as closed polarized forms on the common rapid core, after the declared
radical quotients.

This is a four-block output-channel test. Combined with the four endpoint
matrix units, it is a finite sixteen-entry audit. Symmetries may reduce the
number of independent calculations, but that reduction must be proved rather
than assumed.

The diagonal sum alone proves only a frame estimate. The two diagonal output
blocks alone still do not test the relative \(X\)-\(Y\) phase. At least one
mixed block is indispensable.

## Completion order

The valid completion order is:

1. prove the full primewise output linking-Gram identity;
2. derive the diagonal Pauli frame bound;
3. pass each typed block through twisted Mellin prime diagonality;
4. complete the soft disagreement only after Euler weighting;
5. assemble the global Green system without merging output labels;
6. test the terminal mixed-cancellation margin.

At no stage is the collapsing raw endpoint Gram inverted.

## Minimal hostiles

1. Preserve \(O_X^*O_X+O_Y^*O_Y\) while reversing the sign of
   \(O_X^*O_Y\).
2. Verify both diagonal output blocks but replace the mixed blocks by zero.
3. Merge the output labels before reciprocal sewing.
4. Recover the correct scalar Euler packet from an output-channel swap.
5. Prove the linking identity primewise but lose closability in one mixed
   block at completion.

## Verdict

The Pauli dilation repairs observability, but its summed frame operator is not
a faithful quadratic invariant. Source orientation survives only in the full
two-output linking Gram.

Accordingly, the earliest remaining Adams theorem is sharper than a
Pauli-frame isometry: the fixed linear constructor must intertwine all four
typed output-channel pairings. Coercivity is then obtained by taking the
diagonal trace, while reciprocal orientation remains in the untraced linking
blocks.
