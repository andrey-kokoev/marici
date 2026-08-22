# Future-Shape Dominance Falsifier

## Frozen comparison

Before testing, future dominance was fixed as follows.  A history \(A\)
dominates \(B\) only if there is a natural, port-preserving,
spectator-reduced embedding of complete depth-indexed extension towers

\[
\eta:\mathfrak E_B\hookrightarrow\mathfrak E_A.
\]

The finite pilot uses tower cardinalities

\[
|\mathfrak E_A|=(1,2,2),
\qquad
|\mathfrak E_B|=(1,1,1),
\]

with an explicit injective natural transformation at every depth.  The extra
extension of \(A\) produces a distinct future record label and is therefore
not an independent spectator.

## Exact positive countermodel

Use the normalized preparation

\[
|\psi\rangle
=\frac1{\sqrt{10}}|A\rangle
+\frac3{\sqrt{10}}|B\rangle.
\]

Its source weights are

\[
p_A=\frac1{10},
\qquad
p_B=\frac9{10}.
\]

A lawful isometric extension sends

\[
|A\rangle\mapsto
\frac{|r_0,e_0\rangle+|r_1,e_1\rangle}{\sqrt2},
\qquad
|B\rangle\mapsto|r_0,e_2\rangle.
\]

After forgetting the environment tag, the joint effect-value table is

\[
P=
\begin{pmatrix}
1/20&1/20\\
9/10&0
\end{pmatrix}.
\]

Its determinant is

\[
\det P=-\frac9{200}\ne0,
\]

so the additional \(r_1\) alternative is connected to \(A\); it is not the
spectator-noise loophole.

Nevertheless,

\[
\boxed{
A\succ_{\rm future}B
\quad\text{but}\quad
p_A<p_B.
}
\]

## Disposition

Future-shape dominance does not imply source-weight monotonicity in the
currently admitted positive state/effect and isometric-channel calculus.  The
weights of present alternatives and the shapes of their later extension
towers are independent data unless an additional law couples them.

This countermodel does not prove that nature realizes every such finite
packet.  It proves that the Marici architecture and ordinary positive quantum
kinematics do not force the proposed preference.  Any surviving developmental
principle must add a new constraint excluding this exact packet and must derive
that constraint from physical sources rather than from the desired ordering.

The meaningful survivor is therefore descriptive, not selective:

\[
\text{future-extension towers can be compared naturally,}
\]

but

\[
\text{their dominance does not currently determine physical weight.}
\]

Certificate:
`research/nima/checkers/check_future_shape_dominance.py`
