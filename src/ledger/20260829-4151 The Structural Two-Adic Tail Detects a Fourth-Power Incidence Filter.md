# 4151 — The Structural Two-Adic Tail Detects a Fourth-Power Incidence Filter

## Question

After Entry 4147 repairs the integral lattice, what is the smallest source-derived parameter-ring object compatible with the two terminal two-adic elementary divisors?

This entry is a finite provenance diagnostic, not an exact Fitting theorem.

## Frozen family

Use only the structural lattice of Entry 4147:

- denominator \(2\) fixed on every de Rham row;
- multiplication rows retain their source units;
- no content division after specialization;
- \(K\)-depth \(3\);
- five labelled denominator depths \(2\);
- ambient polynomial degree \(14\).

Every tested fiber has good-prime rank \(2194\), free quotient rank \(84\), and the common two-adic prefix

\[
(0^{1715},1^{420},2^{45},3^{10},4^2).
\]

One terminal factor always has valuation \(8\).

## Six generic hostile fibers

For \(x\ne y\), the second terminal valuation is:

\[
\begin{array}{c|c|c|c}
(x,y,z)&y-x&v_2(y-x)&v_2(d_{\rm terminal})\\
\hline
(5,7,11)&2&1&8\\
(3,5,7)&2&1&8\\
(3,9,13)&6&1&8\\
(7,11,17)&4&2&12\\
(3,7,11)&4&2&12\\
(3,11,17)&8&3&12
\end{array}
\]

The first prediction

\[
v_2(d_{\rm terminal})=4+4v_2(y-x)
\]

was falsified by \((3,11,17)\). The surviving law on these fibers is

\[
v_2(d_{\rm terminal})
=
\min\!\left(12,\;4+4v_2(y-x)\right).
\]

## Minimal candidate ideal

The valuation law is exactly the specialization law of

\[
I_{\rm inc}
=
\left(2^{12},\,2^4(y-x)^4\right)
\subset
\mathbf Z[x,y,z].
\]

Together with the constant terminal factor, the smallest candidate torsion prefix is

\[
T_{\rm cand}
=
R/(2^8)
\oplus
R/I_{\rm inc},
\qquad
R=\mathbf Z[x,y,z].
\]

Its first two Fitting ideals would be

\[
\operatorname{Fitt}_0(T_{\rm cand})
=
\left(2^{20},\,2^{12}(y-x)^4\right),
\]

and

\[
\operatorname{Fitt}_1(T_{\rm cand})
=
\left(2^8,\,2^4(y-x)^4\right).
\]

These formulas are predictions to be derived or killed from the structural presentation.

## Source provenance

The polynomial \(y-x\) is not fitted from an arbitrary search. It is the labelled incidence resultant obtained from

\[
q_{\mathcal G_{23}}=b-x,
\qquad
q_{\mathcal G_{31}}=a-y
\]

after restriction to the diagonal seam \(a=b\). The fourth power is compatible with the \(2\times2\) labelled denominator-depth square, while the cap \(12=3\times4\) matches the three \(K\)-pole levels across that fourfold incidence grade.

This counting explains why the candidate is natural. It does not prove that the exact structural minors have these generators.

## Equality stratum

Two equality fibers give different enhancements:

\[
(5,5,7):\quad v_2(d_{\rm terminal})=12,
\]

\[
(3,3,5):\quad v_2(d_{\rm terminal})=17.
\]

Thus \(x=y\) supports additional arithmetic specialization not controlled by the generic incidence ideal alone. The valuation-\(17\) fiber is not evidence against the generic-open candidate; it is a separate proper-support test that the exact parameter-ring module must explain.

## Narrow result

The repaired barcode has a source-labelled fourth-power incidence filter on the tested open locus \(x\ne y\). Static fiber data support, but do not yet prove,

\[
R/(2^8)\oplus R/(2^{12},2^4(y-x)^4)
\]

as the terminal torsion prefix.

The candidate makes nontrivial predictions:

1. every \(x\ne y\) all-odd fiber with \(v_2(y-x)=1\) has terminal valuations \((8,8)\);
2. every such fiber with \(v_2(y-x)\ge2\) has terminal valuations \((8,12)\);
3. exact equality may enhance the second factor but cannot lower it below valuation \(12\);
4. no dependence on \(z\) appears generically at this terminal grade.

## Next falsifier

Derive the terminal two-generator module from the structural matrix by localized elimination over

\[
\mathbf Z_{(2)}[x,y,z,(y-x)^{-1}]
\]

without specializing \(x,y,z\). Compute its actual first two Fitting ideals. The candidate survives only if the derived ideals are equivalent, up to units and already frozen support factors, to the two ideals above.

Then analyze the proper equality stratum \(x=y\) separately and determine the source polynomial responsible for the valuation-\(17\) enhancement.
