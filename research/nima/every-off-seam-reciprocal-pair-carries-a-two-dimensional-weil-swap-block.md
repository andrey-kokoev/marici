# Every off-seam reciprocal pair carries a two-dimensional Weil swap block

The Weil form from event 10287 has a completely explicit local hostile.

Let

\[
\rho^\vee=1-\bar\rho.
\]

For an off-seam zero, \(\rho^\vee\ne\rho\). Set

\[
x=\widehat f(\rho),
\qquad
y=\widehat f(\rho^\vee).
\]

The contribution of the reciprocal pair to the diagonal Weil form is

\[
x\bar y+y\bar x
=
2\operatorname{Re}(x\bar y).
\]

In the evaluation coordinates \((x,y)\), its Hermitian Gram is

\[
J_{\mathrm{swap}}
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

Its coherent and disagreement vectors are

\[
v_+=\frac1{\sqrt2}(1,1),
\qquad
v_-=\frac1{\sqrt2}(1,-1),
\]

with eigenvalues

\[
J_{\mathrm{swap}}v_+=v_+,
\qquad
J_{\mathrm{swap}}v_-=-v_-.
\]

Thus every isolated off-seam reciprocal pair contributes one positive and one
negative direction.

On the seam,

\[
\rho^\vee=\rho,
\]

so the two evaluation coordinates identify and the block collapses to

\[
|\widehat f(\rho)|^2.
\]

This is the smallest exact matrix mechanism behind the Weil criterion.

## Interpolation gate

The negative vector exists in the abstract evaluation fiber, but the source
test class must realize it. One needs an authorized interpolation/localization
theorem producing \(f\) with

\[
\widehat f(\rho)=1,
\qquad
\widehat f(\rho^\vee)=-1,
\]

while controlling all other zero, pole, and endpoint evaluations.

For a finite divisor packet this is ordinary finite interpolation once the
test transform class separates points. At completion, leakage to the
remaining divisor must be bounded or made arbitrarily small.

Therefore the exact terminal obligations are:

1. complete explicit-formula identification of the Weil form;
2. point separation of reciprocal evaluations;
3. completion-stable localization of the disagreement mode.

Without the third item, a local negative swap block might be concealed by
positive contributions elsewhere.

## Relation to the five margins

The earlier coherent/disagreement decomposition is now literal. The
off-seam pair produces a disagreement direction with negative energy. The
global diagonal and mixed margins must prevent that direction from being
hidden by assembly or terminal cancellation.

This also sharpens the Birman–Schwinger language. The relevant local
collision is not merely an eigenvalue reaching \(1\); before positivity, the
coefficient geometry already contains a signature \((1,1)\) swap block.
Positive contraction geometry becomes available only after all reciprocal
evaluation pairs have collapsed onto fixed seam evaluations.

The minimal hostile for any proposed positive constructor is therefore the
two-coordinate packet

\[
(x,y)=(1,-1).
\]

If the constructor reports nonnegative energy on this packet while claiming
to equal the Weil form, then either:

- it erased reciprocal orientation;
- it failed point separation;
- or an omitted comparison cell changed the form.

This \(2\times2\) swap block is the finite categorical core of the RH
obstruction.
