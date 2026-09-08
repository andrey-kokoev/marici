# Supported Gysin two-extension versus physical Q-homotopy

## Claim

Let

\[
\eta_{\partial}
\in
\operatorname{Ext}^2_A(D,A)\otimes
L_\partial^\vee\otimes
\det(N_{s,t})^\vee
\]

be the positively oriented supported Gysin class for the ordered pair

\[
(s,t)=(t_{04},t_{35}),
\qquad
D=A/(s,t).
\]

Then \(\eta_\partial\) is **not** literally the \(Q\)-roof inside the source
category.  Under the complete mixed-variance physical transform, however, its
distinguished \(D03\) component maps to the unique framed \(Q\)-homotopy
represented by the descended \(q_J\) roof:

\[
\boxed{
\Psi_{03}(\eta_\partial)
=
[q_J]_{\rm framed}.
}
\]

On the \(Q\)-associated grade,

\[
\boxed{
\operatorname{gr}_Q\Psi_{03}(\eta_\partial)
=
[\mathrm{top},D03].
}
\]

The coefficient is \(+1\).

## Reason

The full local physical transform contains three independently normalized
factors:

1. supported codimension-two Gysin residue:
   \[
   \eta_\partial\mapsto +1;
   \]

2. exceptional logarithmic Thom trace:
   \[
   [I]\mapsto +1;
   \]

3. normalized log blowdown:
   \[
   \operatorname{gr}_Q(q_J)=[\mathrm{top},D03]
   \]
   with coefficient \(+1\).

Hence the composite coefficient on the \(D03\) roof is

\[
(+1)(+1)(+1)=+1.
\]

The endpoint line and ordered normal determinant both reverse under physical
reflection, so their tensor product is reflection-even.  Thus the resulting
class has the same endpoint parity and reflection character as the unique
physical connector.

The complete lower roof is

\[
q_J
=
-[\mathrm{top},v_+]
+
[\mathrm{top},D03]
+
X_{D03}[D03,c].
\]

The two lower terms are not independently chosen by the supported residue.
They are forced by the loaded chain identity once the primitive \(Q\)-roof,
Cartier residue, endpoint swap, and Tor orientation are fixed.

The local relative deformation group is zero, so there is no second framed
homotopy with the same complete boundary data.

## Important distinction

The correct identification is therefore

\[
\eta_\partial
\stackrel{\Psi_{03}}{\longmapsto}
[q_J]_{\rm framed},
\]

not

\[
\eta_\partial=q_J
\]

inside one ordinary derived category.

The supported two-extension is the coefficient/duality input; \(q_J\) is its
physical support-filtration realization after the conductor kernel,
exceptional relative dualizing trace, normalized blowdown, and framed
endpoint/Q descent are applied.
