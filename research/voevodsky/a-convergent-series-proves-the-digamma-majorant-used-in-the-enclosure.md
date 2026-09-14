# A convergent series proves the digamma majorant used in the enclosure

## Series decomposition

For \(a=1/4\) and \(b=u/2\), the real part of the digamma function has the convergent expansion

\[
\operatorname{Re}\psi(a+ib)
=
-\gamma+
\sum_{k\geq0}
\left(
\frac1{k+1}
-
\frac{k+a}{(k+a)^2+b^2}
\right).
\]

Split each summand as

\[
\frac1{k+1}-\frac1{k+a}
+
\frac{b^2}{(k+a)((k+a)^2+b^2)}.
\]

## First series

The absolute value of the first series is bounded by separating its \(k=0\) term and comparing the remainder with the reciprocal-square series. This gives the coarse bound

\[
\sum_{k\geq0}
\left|
\frac1{k+1}-\frac1{k+1/4}
\right|
<\frac{17}{4}.
\]

## Imaginary-coordinate correction

For terms with \(k+1/4\leq b\), bound the correction by \((k+1/4)^{-1}\). For the remaining terms, bound it by

\[
\frac{b^2}{(k+1/4)^3}.
\]

Integral comparison and \(\log(1+x)\leq x\) then give the deliberately loose estimate

\[
\sum_{k\geq0}
\frac{b^2}{(k+1/4)((k+1/4)^2+b^2)}
<
\frac{11}{2}+4b.
\]

Since \(4b=2u\) and \(\gamma<1\), combining the pieces proves

\[
\left|
\operatorname{Re}\psi(1/4+iu/2)
\right|
<21+2u.
\]

## Consequence

The majorant used in the gamma-tail estimate and the midpoint Lipschitz budget is now analytically sourced from an absolutely convergent series. Its large slack is intentional; sharpness is unnecessary for the selected positive sample.

The remaining nonrigorous component of the enclosure is finite evaluation of the digamma integrand and elementary functions with ordinary floating arithmetic, not the global magnitude bound.

## Verification

```text
python research/voevodsky/checkers/check_digamma_real_part_majorant.py
```

The checker stress-tests the bound from \(u=0\) through \(u=100\). The proof is the series estimate above; numerical sampling is not used as its justification.

Artifacts:

- `research/voevodsky/checkers/check_digamma_real_part_majorant.py`
- `research/voevodsky/results/digamma_real_part_majorant.json`
