# What the alternate chart repairs over the integers

The alternate row-\(3\) chart has nonzero determinant for every admissible
even grade. It is therefore injective as a map between free integral modules:
no nonzero integral source packet is invisible to this chart.

It is not unimodular. Its image has finite index

\[
I_g=
|\det A_g|\,(2g+7)(4)^{\overline g}\,|\sigma_g|,
\]

where \(A_g\) is the proved triangular interior core and

\[
\sigma_g=
-\frac{8(2g+3)(g^2-g-26)(2g+1)!}
{3(g+5)(g+6)(g+7)(g-1)!}.
\]

The core factor is the product of its source pivots:

\[
|\det A_g|
=(2g+9)(4)^{\overline g}
\prod_{\substack{2\le a\le g+6\\a\in2\mathbb Z}}
(3g+7+a)(g+9-a)\bigl(a^{\overline g}\bigr)^2
\,(4g+15)(g+8)^{\overline g}.
\]

Thus the alternate chart restores integral injectivity but not integral
surjectivity. Its cokernel is finite of order \(I_g\). This finite cokernel
does not represent hidden source states: it measures target observation
packets that cannot be produced with the fixed integral source
normalization.

This separates two notions previously compressed into “faithfulness”:

- source faithfulness is injectivity and is fully restored;
- target saturation would require unimodularity and is not restored.

The exact determinant formula agrees with generated matrices through even
grade \(20\), and its nonunimodularity is replayed through even grade \(200\).

There is also an unbounded coefficient-level reason for nonunimodularity.
For integral \(a\),

\[
a^{\overline{g-j}}\in (g-j)!\mathbb Z,\qquad
(4-a)^{\overline j}\in j!\mathbb Z.
\]

After multiplication by \(\binom gj\), every source coefficient is divisible
by \(g!\). The first-order path operation preserves this divisibility.
Consequently the full alternate matrix factors as

\[
M_{\mathrm{alt}}=g!N_g
\]

with \(N_g\) integral. If its order is \(n\), then

\[
\operatorname{coker}M_{\mathrm{alt}}
\longrightarrow(\mathbb Z/g!)^n
\]

is surjective. Thus the finite cokernel is intrinsically multilayered; it
cannot be compressed to a single scalar granularity. Exact Smith forms at
\(g=2,4,6,8\) confirm that every invariant factor is nonunit and divisible
by \(g!\).
