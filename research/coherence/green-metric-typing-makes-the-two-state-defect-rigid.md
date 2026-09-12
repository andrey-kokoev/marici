# Green-metric typing makes the two-state reciprocal defect rigid

## Scalar hostile

Consider

\[
\Delta_0=
\begin{pmatrix}1&0\\0&-1\end{pmatrix}
\]

and

\[
\Delta_1=
\begin{pmatrix}5/3&4/3\\-4/3&-5/3\end{pmatrix}.
\]

They are distinct, but both satisfy

\[
\Delta_i^2=I,
\qquad
\det\Delta_i=-1,
\qquad
R\Delta_iR=-\Delta_i.
\]

Thus central square, determinant, and reversal parity do not determine the framed defect.

## Green separation

Retain the hyperbolic Green metric

\[
H=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

The canonical defect is Green-skew:

\[
\Delta_0^TH+H\Delta_0=0.
\]

The hostile defect fails this identity.

## Rigidity theorem

Any two-dimensional operator odd under reversal has the form

\[
\Delta=
\begin{pmatrix}a&b\\-b&-a\end{pmatrix}.
\]

Imposing Green skewness gives

\[
\Delta^TH+H\Delta
=
\begin{pmatrix}-2b&0\\0&2b\end{pmatrix}=0,
\]

so \(b=0\). Therefore

\[
\Delta=a
\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

Its central square determines \(a^2\); retained orientation determines the sign of \(a\). Hence, in the minimal two-state carrier,

```text
reversal parity
+ Green metric
+ central square
+ orientation
```

determines the full framed defect.

## Consequence

A scalar closure is insufficient by itself. But after all source-required typing is retained, the scalar square becomes complete for this minimal representation up to orientation.

This identifies the role of the higher observer precisely: it need not remember every matrix entry independently. It must certify the structural constraints that make those entries reconstructible from the invariant closure.

## Verification

```text
python research/coherence/check_scalar_closure_frame_hostile.py
```

Artifacts:

- `check_scalar_closure_frame_hostile.py`
- `scalar-closure-frame-hostile.v1.json`
