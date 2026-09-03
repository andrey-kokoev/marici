# The quarter pivot second coefficient is not minus seven quarters

## Question

Does the exact grid support

\[
c_m=1+\frac{2}{m}-\frac{7}{4m^2}+O(m^{-3})?
\]

Extending the determinant grid through degree twenty-four and fitting

\[
m^2\left(c_m-1-\frac{2}{m}\right)
=\beta+\frac{a}{m}+\frac{b}{m^2}
\]

over \(m=10,\ldots,23\) gives

\[
\beta=-1.70960002.
\]

This is separated from \(-7/4=-1.75\) by \(0.0404\), so the proposed rational is rejected under the quadratic inverse-degree correction model. The logarithmic local expansion remains

\[
\log c_m=\frac{2}{m}+\frac{\beta-2}{m^2}+O(m^{-3}),
\]

but the exact value of \(\beta\) is unidentified.

## Disposition

Reject the \(-7/4\) candidate rather than fitting it to the earlier shorter grid. The next leaf is `quarter-pivot-second-coefficient-from-recurrence`: derive \(\beta\) from the pivot recurrence before attempting further rational recognition.

## Claim boundary

The value \(-1.70960002\) is a finite extrapolation, not a theorem or an exact constant. The rejection is conditional on the displayed correction model.
