# The complementary electric kernel

The sheet packet has parity projections

\[
E=A+B,
\qquad
M=A-B.
\]

For every reflected component `q>0`, split the source columns into its two
signed branches.  After identifying the reflected target coordinates, the
two blocks have the form

\[
M_q=[C_q,-\bar C_q],
\qquad
E_q=[C_q,+\bar C_q].
\]

Multiplying every column of one source branch by `-1` carries one matrix to
the other.  Hence

\[
\operatorname{rank}E_q=\operatorname{rank}M_q
\qquad(q>0),
\]

and their kernel circuits are related by the same branch-sign gauge.

Combining this with the magnetic classification gives exactly two electric
kernel classes:

\[
\widetilde E_1=1+\bar z^{-2}.
\]

\[
\widetilde E_2=\bar z^{-8}+3z^{-4}\bar z^2-2z^{-6}.
\]
Both occur only at grade two, with the second requiring pole depth six.

The center component behaves differently.  At `q=0`, reflection fixes every
target.  Magnetic antisymmetrization kills each column, producing all tower
classes.  Electric symmetrization instead gives

\[
E=2A.
\]

The proved one-sheet theorem `ker A=0` therefore makes the entire electric
center injective.  There are no electric tower classes.

For sufficiently wide cutoffs,

\[
\dim\ker E_g=
\begin{cases}
1+\mathbf1_{k\ge3},&g=2,\\
0,&g\ge3.
\end{cases}
\]

The electric circuits are magnetically visible, while every magnetic kernel
class is electrically visible.  Thus

\[
\ker E_g\cap\ker M_g=0
\]

and the complementary pair is faithful.

This yields the complete parity routing picture:

\[
\begin{array}{c|c|c}
\text{source class}&E&M\\
\hline
\text{magnetic tower/circuit}&\ne0&0\\
\text{electric circuit}&0&\ne0\\
\text{generic source}&\text{possibly nonzero}&\text{possibly nonzero}
\end{array}
\]

The checker verifies equal `q>0` ranks across 220 exact component pairs,
classifies their only defects, checks the two primitive circuits, and audits
the center through grade 30 at pole cutoff 20.
