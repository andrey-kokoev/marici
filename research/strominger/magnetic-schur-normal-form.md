# Stable magnetic elimination has one semantic triangular form

Write one nested Hall extension as

\[
M_{k+1}=\begin{pmatrix}A&B\\C&E\end{pmatrix},
\qquad
S=E-CA^{-1}B.
\]

Order the two new observations semantically as `(r_minus,r_plus)`, rather than
using the storage order returned by an augmenting matcher. Exact elimination
then gives one normal form in both parities:

\[
\boxed{S=\begin{pmatrix}u&0\\ *&v\end{pmatrix}.}
\]

The minus pivot is always the raw endpoint character

\[
u=(-1)^{g+1}(a+g+q-1)a^{\overline g}.
\]

For odd `q`, the plus endpoint does not collide with the depth-two lattice and
is also unchanged by elimination:

\[
v=(-1)^g(a+g-q-1)a^{\overline g}.
\]

For even `q`, the raw plus endpoint collides and the selected `B1` observation
is renormalized by the old state to

\[
v=(-1)^gqg(g+3)a^{\overline{g-1}}.
\]

All remaining older-state dependence lies in the lower-left starred entry,
which the determinant cannot see. Thus

\[
\det S=uv.
\]

In semantic row orientation this equals the odd character directly and the
negative of the even character; the sign difference is the row permutation
used by the augmenting matcher. The invariant determinant magnitude is

\[
\begin{aligned}
q\text{ odd}:&\quad
(a^{\overline g})^2(a+g-q-1)(a+g+q-1),\\
q\text{ even}:&\quad
qg(g+3)a^{\overline g}a^{\overline{g-1}}(a+g+q-1).
\end{aligned}
\]

This corrects an earlier coordinate-dependent description of the even form as
anti-triangular. That shape came solely from the matcher's reversed ordering
of the two new rows. The invariant parity distinction is instead:

- odd `q`: the raw plus `B0` pivot is protected;
- even `q`: the collided plus `B1` pivot is Schur-renormalized.

Support memory survives in the starred entry, while determinant memory
vanishes because that entry is exterior-invisible.

The checker verifies the corrected semantic normal form on 276 exact stable
extensions. The remaining unbounded task is to derive the protected and
renormalized pivot formulas directly from the order-four column-contiguity
identity.
