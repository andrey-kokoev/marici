# Pfaffian-divisor valuations are tropical ordered-matching costs

## Valuation of principal Pfaffians

Fix a prime \(p\) and assign each integral gap the cost

\[
c_i=v_p(x_i).
\]

For a path weight,

\[
v_p(w(i,j))=
\sum_{r=i}^{j-1}c_r.
\]

For an even principal subset

\[
S=\{i_1<\cdots<i_{2k}\},
\]

its Pfaffian valuation is

\[
v_p(\operatorname{Pf}M_S)
=
\sum_{r=1}^k
\sum_{j=i_{2r-1}}^{i_{2r}-1}c_j.
\]

## Tropical divisor formula

Because valuation sends gcd to minimum,

\[
v_p(D_k)
=
\min_{|S|=2k}
v_p(\operatorname{Pf}M_S).
\]

Hence \(v_p(D_k)\) is the minimum cost of choosing \(k\) ordered, disjoint path pairs on the chain. The paired endpoints occur consecutively in the chosen subset, so crossings are forbidden automatically.

The elementary-divisor valuations are successive differences:

\[
v_p(d_k)
=
v_p(D_k)-v_p(D_{k-1}).
\]

## Dynamic program

Let \(F(i,k)\) be the minimum cost of selecting \(k\) pairs using vertices at or after \(i\). Then

\[
F(i,k)
=
\min\left(
F(i+1,k),
\min_{j>i}
\left[
\sum_{r=i}^{j-1}c_r+F(j+1,k-1)
\right]
\right).
\]

Boundary conditions are

\[
F(i,0)=0
\]

and infinity when fewer than \(2k\) vertices remain.

This computes all local Smith data without constructing large minors or taking integer gcds.

## Interpretation

The integral alternating torsion decomposes prime by prime into tropical matching spectra:

```text
prime p
-> gap valuation costs
-> minimum k-pair costs v_p(D_k)
-> successive increments v_p(d_k)
```

The scalar terminal Pfaffian is only the final matching cost. The lower divisor spectrum records how arithmetic torsion enters at every rank.

## Relation to the real metric model

The real exponential Pfaffian selects the unique adjacent perfect matching by ordinary additive distance. The integral torsion theory replaces distance by each prime valuation and minimizes over all principal subconfigurations. Thus metric minimum matching and arithmetic Smith reconciliation are two semiring shadows of the same ordered pairing combinatorics.

## Verification

```text
python research/coherence/check_tropical_pfaffian_divisor_matching.py
```

The checker compares exhaustive principal-subset enumeration with the dynamic program for 200 chains through eleven vertices.

Artifacts:

- `check_tropical_pfaffian_divisor_matching.py`
- `tropical-pfaffian-divisor-matching.v1.json`
