# All-translate Weil-kernel faithfulness

## Question

Why does positivity of a zero-character heat slice not supply the full Weil/RH positivity criterion?

## Claim boundary

This identifies the missing positivity and density arrows. It does not construct them from arithmetic data.

## Positivity hierarchy

For the centered Weil form \(q\), a test packet \(f\), and translations

\[
(T_af)(x)=f(x-a),
\]

define

\[
K_f(a,b)=q(T_af,T_bf).
\]

When \(q\) is translation invariant,

\[
K_f(a,b)=k_f(a-b).
\]

There are four distinct strengths:

1. zero-character positivity: \(k_f(0)=q(f,f)\geq0\) for one packet;
2. pointwise information about individual translated values;
3. cyclic all-translate positivity: every matrix \([k_f(a_i-a_j)]\) is positive semidefinite;
4. full Weil positivity: cyclic positivity holds for a source-derived family whose translated spans are dense in the Weil test space.

No lower level promotes to the next without a separate positive-definiteness or density proof.

## Exact separation

The checker exhibits a positive zero slice with two-translate matrix

\[
\begin{pmatrix}1&2\\2&1\end{pmatrix},
\]

whose determinant is \(-3\). Thus diagonal positivity does not even imply rank-two translate positivity.

For comparison, \(k(a-b)=\cos(a-b)\) factors through the two features \((\cos a,\sin a)\), so every translate Gram matrix is positive. This also exposes the density issue: the cyclic realization has rank two and cannot certify an unrestricted test space.

## Bochner target

For continuous translation-invariant kernels, all-translate positivity is equivalent to a positive Fourier measure. The arithmetic problem is therefore not positivity of one heat value but construction of the full positive spectral measure, followed by proof that the admitted source family is faithful for the complete Weil form.

## Disposition

The surviving acceptance test is to construct positive two-variable translate kernels for a source-derived dense family and prove their compatibility with the completed endpoint–gamma–prime Weil form. The zero-character heat slice and rank-two Schwarzian consequence are strict projections of this target.

## Verification

- `research/voevodsky/all-translate-weil-kernel-faithfulness-v1.json`
- `research/voevodsky/checkers/check_all_translate_weil_kernel_faithfulness.py`
- `research/voevodsky/results/all_translate_weil_kernel_faithfulness.json`
