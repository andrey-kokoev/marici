# Complete spatial transport around the six-short-normal orbit

Date: 2026-09-08

## Result

The complete framed/support map previously compiled at `35/04` transports around both rotation orbits:

\[
35\to13\to15\to35,
\qquad
04\to24\to02\to04.
\]

For each of the six normals and each of the four rotated channels `T`, this gives

\[
b_{k,T}:G_{k,T}\longrightarrow D_k,
\qquad
b_{k,T}(x)=(0,j_k\kappa_{k,T}(x),0).
\]

There are 24 maps in total.

The transport rotates the complete data, not only the target label:

- all six occurrence coordinates;
- the endpoint Rees triple;
- the product support `T`;
- the complete 1024-column Cech source;
- the determinant and polarity lines;
- the normalized native operation mate;
- the antipode and its decomposable terms.

Each support map has zero defect on 1024 basis columns. Thus 24,576 transported support columns are covered. Each pullback chain defect is `(0,0,0)`.

## Signs and reflection

In ordered occurrence coordinates the raw determinant signs alternate. The polarity row alternates identically, so their product is one in every column. Consequently every transported primitive map has coefficient

\[
+1.
\]

Reflection pairs

\[
02\leftrightarrow13,
\qquad04\leftrightarrow35,
\qquad24\leftrightarrow15
\]

and preserves the loaded coefficient while exchanging marked targets.

## Joint rank

Each normal carries four independent marked source channels, and its maps land in the corresponding kernel line `Cv_k`. On the six-normal marked quotient the normal-incidence matrix is `I_6`, hence has rank six. Thus the six-normal observer family genuinely separates all six labelled conormal directions; it is no longer merely an available family of targets.

This does not yet establish conservativity on the full completed admissible Xi source. It establishes the finite endpoint/conormal block that such a theorem must contain.

## Verification

```sh
python research/voevodsky/check_marici_six_normal_spatial_transport_20260908.py \
  --root . \
  --output research/voevodsky/marici_six_normal_spatial_transport_certificate_20260908.json
```

The checker performs 159 integration assertions across 24 complete frames.
