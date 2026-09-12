# The framed reciprocal equalizer is a Clifford-odd defect

## Full comparison

On the stationary incoming/outgoing double, define the framed reciprocal defect

\[
\Delta(z)=T(z)-RT(z)R.
\]

Since \(RT(z)R=T(z)^{-1}\),

\[
\Delta(z)
=
\begin{pmatrix}
z-z^{-1}&0\\
0&-(z-z^{-1})
\end{pmatrix}
=(z-z^{-1})A.
\]

This retains the frame: it compares direct and reciprocal transport as endomorphisms of the same declared incoming/outgoing carrier.

## Clifford covariance

The defect is odd under reversal:

\[
R\Delta(z)R=-\Delta(z).
\]

Its square is central:

\[
\Delta(z)^2=(z-z^{-1})^2I.
\]

Thus the full coherence defect is a Clifford-odd operator, while its scalar square is the associated invariant.

## Fixed locus

The following conditions are equivalent:

\[
\Delta(z)=0,
\]

\[
\ker\Delta(z)\ne0,
\]

\[
\det\Delta(z)=0,
\]

\[
z^2=1.
\]

On the positive component, this is exactly \(z=1\).

Away from the fixed locus, \(\Delta(z)\) has rank two. At the fixed locus its entire two-dimensional carrier becomes kernel; there is no intermediate rank-one state in this minimal model.

## Pyramid reading

The meta-level sequence is now concrete:

```text
P1  direct transport T(z)
P2  reciprocal comparison R T(z) R
P3  framed difference Delta(z)
P4  central closure Delta(z)^2
```

The scalar determinant sees only the square

\[
\det\Delta(z)=-(z-z^{-1})^2.
\]

The unsquared operator retains which reciprocal weight carries each sign and how reversal exchanges them.

This small model demonstrates the required logic:

```text
orbit equivalence holds everywhere;
framed equalizer degeneracy occurs only on the fixed locus.
```

Whether a larger system has the same exact separation requires deriving its framed comparison operator and proving that no additional kernel appears.

## Verification

The checker verifies the identities and fixed-locus equivalence for 55 positive rational values:

```text
python research/coherence/check_framed_reciprocal_equalizer_defect.py
```

Artifacts:

- `check_framed_reciprocal_equalizer_defect.py`
- `framed-reciprocal-equalizer-defect.v1.json`
