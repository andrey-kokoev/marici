# The concrete source pairing is the Weil form on Gaussian squares

## Question

What pre-positivity source space and exact identity replace the rejected generic mixed-Gram conjecture?

## Polynomial packet

For a finite coefficient vector `c=(c_0,...,c_N)`, define

\[
p_c(y)=\sum_{j=0}^N c_jy^j.
\]

For raw completed heat values, the sampled localizer quadratic form is

\[
Q_{t,h}(c)
=
\sum_{i,j}\overline{c_i}c_j
\bigl[H(t+(i+j)h)-H(t+(i+j+1)h)\bigr].
\]

By linearity of the completed Weil distribution `W`, this is exactly

\[
Q_{t,h}(c)
=
\left\langle W,
 e^{-tu^2}(1-e^{-hu^2})
 |p_c(e^{-hu^2})|^2
\right\rangle.
\]

Thus the pre-positivity source space is the finite polynomial algebra evaluated through `y=e^(-hu^2)`, and the pairing is the completed Weil explicit-formula functional on the displayed Gaussian square.

## Source decomposition

Applying the explicit formula to the single test function

\[
\phi_{t,h,c}(u)
=e^{-tu^2}(1-e^{-hu^2})|p_c(e^{-hu^2})|^2
\]

produces endpoint, gamma, and prime terms with one common test and normalization. The source functional remains additive. There is no independently defined gamma--prime off-diagonal operator.

The cross term seen in

\[
D_2=D_2^\Gamma+D_2^{\mathbb P}+C_{\Gamma,\mathbb P}
\]

arises from taking a nonlinear determinant of the sum of two moment matrices. It is not evidence for a source coupling map between gamma and prime Hilbert spaces.

## Exact positivity target

The remainder cone asks for positivity of the modified source functional after deleting the polar endpoint contribution. The completed cone itself is

\[
\langle W,\phi_{t,h,c}\rangle\ge0
\]

for every `t,h>0` and every polynomial `p_c`.

This is a Gaussian-square subfamily of the Weil positivity criterion. The pole-rigidity argument shows that its all-mesh closure already detects every off-line zero, so the subfamily retains RH strength.

## Risky source law

Any proposed source construction must act before positivity and verify the explicit identity above. A noncircular factorization would need a concrete operator `A` on a declared test-function completion such that

\[
\langle W,\phi\rangle=\|A\phi\|^2
\]

for this Gaussian-square family, with `A` derived from endpoint--gamma--prime data rather than from GNS applied after assuming `Q>=0`.

A recurrence that only manipulates Hankel minors or orthogonal polynomials after positivity does not meet this requirement.

## Consequence for the numerical role reversal

The observed gamma--prime role reversal means no additive sector restriction of the Weil form is positive on the Gaussian-square family. Positivity, if proved, must be a theorem about the completed explicit-formula functional evaluated on the common test—not a blockwise Gram theorem.

## Boundary

The exact normalization connecting the repository heat source to the standard Weil functional must be cited. Density of this Gaussian-square family in the full admissible Weil test class is unnecessary for the forward RH implication because generic-mesh pole rigidity was proved directly, but it would be needed to claim equality with the entire classical Weil cone.

## Disposition

Withdraw language suggesting an unspecified gamma--prime coupling operator. Use the completed Weil pairing on Gaussian polynomial squares as the sole concrete pre-positivity source object. The remaining proof problem is positivity of that explicit source functional.