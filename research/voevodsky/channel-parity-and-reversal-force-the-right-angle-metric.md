# Channel parity and reversal force the right-angle metric

## Question

Can the \(90\)-degree relation be derived from the channel symmetries instead of imposed as a chosen Euclidean pairing?

## Symmetry data

Let the two-dimensional normal space have ordered channel basis \((\nu_+,\nu_-)\).

Sign parity acts by

\[
S=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

Channel reversal acts by

\[
J=
\begin{pmatrix}
0&-1\\
-1&0
\end{pmatrix}.
\]

Let an unknown positive symmetric metric be

\[
G=
\begin{pmatrix}
a&b\\
b&c
\end{pmatrix}.
\]

Require both declared symmetries to be isometries:

\[
S^TGS=G,
\qquad
J^TGJ=G.
\]

## Derivation

Sign invariance gives

\[
b=-b.
\]

Over coefficients where two is invertible, this forces

\[
b=0.
\]

Reversal invariance gives

\[
a=c.
\]

Therefore every invariant positive metric has the form

\[
G=\lambda I,
\qquad
\lambda>0.
\]

The channels are orthogonal and have equal norm. The right angle is forced by the joint symmetry requirements, up to overall scale.

## Independent necessity

Reversal alone does not force orthogonality. The positive metric

\[
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix}
\]

is reversal invariant and has nonzero cross pairing.

Sign parity alone forces orthogonality but not equal scale. The metric

\[
\begin{pmatrix}
2&0\\
0&3
\end{pmatrix}
\]

is sign invariant but not reversal invariant.

Thus the two symmetries have separate consequences:

- parity removes the cross term;
- reversal equates the two channel norms.

## Disposition

The Euclidean normal metric no longer needs to be independently selected once sign parity and channel reversal are declared as isometries. The residual assumption is now concentrated in those two involutions and their isometric action.

This does not derive either involution from the 2-Segal laws. It proves that, conditional on both involutions, the normal metric is unique up to positive scale.

## Verification

```text
python research/voevodsky/checkers/check_intrinsic_right_angle_from_channel_symmetries.py
```

The checker exhausts 31 positive symmetric integer metrics in the bounded coefficient grid, confirms the invariant family, and retains counterexamples showing that either symmetry alone is insufficient.

Artifacts:

- `research/voevodsky/checkers/check_intrinsic_right_angle_from_channel_symmetries.py`
- `research/voevodsky/results/intrinsic_right_angle_from_channel_symmetries.json`
