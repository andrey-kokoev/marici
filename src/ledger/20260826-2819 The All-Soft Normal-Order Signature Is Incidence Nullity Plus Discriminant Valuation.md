# 2819 — The All-Soft Normal-Order Signature Is Incidence Nullity Plus Discriminant Valuation

## Hard-to-vary claim

For a retained labelled marked family \(S\), let

\[
\iota_S:\mathbb F^S\longrightarrow\langle a,b\rangle
\]

be its all-soft incidence map. Let \(v_{\rm ext}(K)\) be the external normal valuation of the frozen Cayley–Menger factor. Then the multiplication-Koszul fiber has

\[
|S|-\operatorname{rank}(\iota_S)
\]

first-normal exterior generators, together with one Cayley–Menger generator at order

\[
v_{\rm ext}(K)=2.
\]

Equivalently,

\[
H(K_S|_0)
\simeq
\mathbb F[a,b]/I_S
\otimes
\Lambda^{\bullet}
\left(ker\iota_S\oplus\mathbb F e_K\right).
\]

This derives the complete-family signature \((1,1,1,2)\): three dimensions of incidence nullity and one order-two discriminant direction.

## Labelled deletion test

The prediction was frozen and tested on all 31 nonempty labelled subfamilies of

\[
(q_{g1},q_{g2},q_{g3},q_{g23},q_{g31}).
\]

Their signatures partition as follows:

| incidence rank | first-normal generators | total exterior generators | sectors |
|---:|---:|---:|---:|
| 1 | 0 | 1 | 5 |
| 1 | 1 | 2 | 2 |
| 2 | 0 | 1 | 8 |
| 2 | 1 | 2 | 10 |
| 2 | 2 | 3 | 5 |
| 2 | 3 | 4 | 1 |

The Cayley–Menger order remains two in every deletion sector because deletion changes the marked incidence packet, not the frozen discriminant polynomial.

## Interpretation and limitation

The \(3+1\) pattern is no longer an unexplained census. It is forced by two independently typed quantities:

1. incidence nullity of the occurrence-labelled marked map;
2. external valuation of the sector-specific discriminant coefficient.

This is an internal deletion theorem, not yet a hostile independent-graph confirmation. A genuine explanatory test must freeze the same rule on another source-defined marked graph and predict its signature before computing its all-soft fiber.

## Durable artifacts

- `research/benincasa/check_rank26_deletion_normal_order_signature.py`
- `research/benincasa/rank26-deletion-normal-order-signature.json`
