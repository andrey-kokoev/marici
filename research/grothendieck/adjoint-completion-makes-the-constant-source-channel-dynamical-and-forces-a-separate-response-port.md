# Adjoint Completion Makes the Constant Source Channel Dynamical and Forces a Separate Response Port

## Native affine tail system

The source-derived one-sided tail equation can be homogenized by adjoining a
constant source amplitude \(c\):

\[
\frac{d}{dq}
\begin{pmatrix}u\\c\end{pmatrix}
=
\begin{pmatrix}-z&-f\\0&0\end{pmatrix}
\begin{pmatrix}u\\c\end{pmatrix},
\qquad c'=0.
\]

The upper-right entry is the forward source incidence

\[
B:c\longmapsto-fc.
\]

## Unique positive-metric adjoint completion

On the unitary seam, a conservative completion with the standard positive
metric requires the source-coupling block to be skew-adjoint. For real \(f\),
the unique missing lower entry is therefore \(+f\):

\[
K_f=
\begin{pmatrix}0&-f\\f&0\end{pmatrix},
\qquad K_f^*=-K_f.
\]

The completed dynamics is

\[
u'=-zu-fc,
\qquad
c'=fu.
\]

The coupling contributions to the positive norm cancel exactly:

\[
\frac{d}{dq}\left(|u|^2+|c|^2\right)_{\rm coupling}=0.
\]

But the source amplitude is no longer constant. Unless \(fu=0\), the affine
slice \(c=1\) is not invariant.

## No two-state conservative realization of the native source equation

The two desired properties are incompatible on the same carrier:

1. native theta forcing requires \(c'=0\);
2. positive-metric adjoint completion requires \(c'=fu\).

For nonzero theta forcing and nontrivial tail state, both cannot hold. Thus one
cannot repair the missing variance arrow by inserting the lower-left matrix
entry while claiming to preserve the original source dynamics.

## Minimal retyping

The forcing amplitude and its adjoint response must be different ports:

\[
\mathcal U_{\rm in}
\xrightarrow{B}
\mathcal H_{\rm tail}
\xrightarrow{B^*}
\mathcal U_{\rm out}.
\]

The input coordinate remains fixed by the source, while the output coordinate
records the response

\[
r'=f\,u
\]

or its completed reciprocal analogue. This is a conservative colligation or
input--state--output system, not a closed two-state evolution.

For the reciprocal double, the response is sourced by an explicitly typed
combination of \(u\) and \(v\); deciding whether it is the common mode, the
relative mode, or a boundary-graded pair is the next source calculation.

## Multi-tower meaning

The new channel is not an optional fifth wall. It separates two roles that the
homogeneous presentation had collapsed:

1. source input or constructor;
2. transported state;
3. adjoint response or observation.

Reciprocal doubling acts on the transported-state tower. It cannot by itself
manufacture the response tower. The conservation cell must compare all three.

## Next falsifier

At finite theta-label cutoff, derive the response row from the labelled source
pairing and compare it with the Hilbert adjoint of the input column. The route
fails at the first cutoff for which

\[
R_X^{\rm adj}=B_{\rm out,X}-B_{\rm in,X}^*
\]

is nonzero after all primitive, square, seam, and archimedean grades are
retained.

