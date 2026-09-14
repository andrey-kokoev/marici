# Three-channel theta to six-normal source-adapter gate

Date: 2026-09-08

## Two exact rank-three objects

The completed theta source has three channels

\[
(C,U,V),\qquad \xi=C+U+V.
\]

A useful invertible coordinate system is

\[
\begin{pmatrix}\xi\\U-V\\2C-U-V\end{pmatrix}
=
\begin{pmatrix}1&1&1\\0&1&-1\\2&-1&-1\end{pmatrix}
\begin{pmatrix}C\\U\\V\end{pmatrix}.
\]

The matrix has determinant `-6`, so no theta information is lost over characteristic zero.

Independently, the six loaded conormal columns arise from

\[
K_{\rm alt}=
\begin{pmatrix}
0&0&-1&0&0&1\\
-1&0&0&1&0&0\\
0&1&0&0&-1&0
\end{pmatrix}.
\]

It satisfies

\[
K_{\rm alt}K_{\rm alt}^T=2I_3.
\]

Hence `K_alt^T` embeds a three-dimensional comparison packet into the six marked normal ports and `(1/2)K_alt` is its rational left inverse.

## Exact remaining map

The common-source transport problem has therefore reduced to one finite datum: a source-authorized matrix

\[
A_{\theta/N}(s):
(\xi,U-V,2C-U-V)
\longrightarrow
\operatorname{Rows}(K_{\rm alt}).
\]

Once this adapter is supplied,

\[
K_{\rm alt}^T A_{\theta/N}(s)
\]

is the six-normal observation map on the theta source. If the adapter is invertible on the admissible source, the return map is

\[
A_{\theta/N}(s)^{-1}\frac12K_{\rm alt}.
\]

The Cubical Agda source-transport and observer-extension theorems then apply immediately.

## Why it is still open

Rank agreement does not identify the two row bases. The theta coordinates describe completion/direct/reciprocal Mellin channels. The rows of `K_alt` are independently framed conormal incidence channels. A valid adapter must be derived from a common Fourier–Tate/source correspondence and must preserve:

- support and internal grading;
- reciprocal/reflection variance;
- determinant and polarity lines;
- the bounded source-energy completion.

Choosing an arbitrary invertible `3x3` matrix would manufacture the missing observer rather than derive it.

## Verification

```sh
python research/voevodsky/check_marici_theta_six_normal_adapter_gate_20260908.py \
  --root . \
  --output research/voevodsky/marici_theta_six_normal_adapter_gate_certificate_20260908.json
```

The checker performs 20 exact matrix assertions. The certificate status is `open_exact_adapter`, not `proved`.
