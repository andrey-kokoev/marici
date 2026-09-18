# Arbitrary-n one-loop MHV Kermit spurious-pole cancellation

## Theorem

For

$$
\mathcal A_n^{(2),1}=\sum_{1<a<b<n}K[a;b],
$$

every nonlocal anchor pole

$$
L_k:=\langle AB\,1k\rangle=0,
\qquad 3\le k\le n-1,
$$

cancels pairwise for every `n>=5`.

## Cell indexing

Regard `K[a;b]` as indexed by an unordered pair from

$$
I_n=\{2,3,\ldots,n-1\}.
$$

Fix `k` and choose

$$
r\in I_n\setminus\{k-1,k\}.$$

There are two cells

$$
C^-_{k,r}=K[\{k-1,r\}],
\qquad
C^+_{k,r}=K[\{k,r\}],
$$

where each unordered pair is written increasingly in the actual Kermit sum.
Both have the facet `L_k=0`: in the first it is the endpoint denominator associated with `(k-1)+1`, and in the second it is the endpoint denominator associated with `k`.

The adjacent cell `K[k-1;k]` has apparent repeated anchor incidence, but its intersection numerator contains the compensating power of `L_k`; it has zero residue. No other Kermit term contains `L_k`. Therefore the nonzero incident residues are exactly the two cells above for every allowed `r`. Their number is

$$
2|I_n\setminus\{k-1,k\}|=2(n-4).
$$

## Opposite residues

The Kermit terms are canonical forms of adjacent one-loop BCFW cells. Replacing `k-1` by `k` is the local boundary move across their common anchor facet. With the source wedge orientation, the induced facet orientations are opposite:

$$
\operatorname{Res}_{L_k=0}C^-_{k,r}
=-
\operatorname{Res}_{L_k=0}C^+_{k,r}.
$$

Equivalently, substituting `langle AB 1k rangle=0` into the two rational formulas and applying the four-bracket Schouten relation leaves identical facet numerators and denominators with opposite deleted-coordinate signs.

Thus the involution

$$
\iota_k:C^-_{k,r}\longleftrightarrow C^+_{k,r}
$$

is fixed-point free on all nonzero `L_k` residues. Summing by its orbits gives

$$
\operatorname{Res}_{L_k=0}\mathcal A_n^{(2),1}
=
\sum_{r\notin\{k-1,k\}}
\left(
\operatorname{Res}C^-_{k,r}
+
\operatorname{Res}C^+_{k,r}
\right)
=0.
$$

Hence every nonlocal anchor pole cancels at arbitrary multiplicity.

## Physical boundary contrast

The local divisors

$$
\langle AB\,i(i+1)\rangle=0
$$

are not paired by this involution. Exact generic-kinematics checks through eight points find nonzero total residues on every cyclic physical propagator.

## Executable evidence

`check_one_loop_mhv_kermit_pole_census.py` computes exact rational residues. For every spurious divisor through eight points it finds the pairing

$$
K[\{k-1,r\}]\leftrightarrow K[\{k,r\}]
$$

with opposite values, while every physical pole survives.

## Claim boundary

This proves codimension-one cancellation of all anchor-type nonlocal poles in the sourced one-loop MHV Kermit sum. It does not classify higher-codimension intersections, prove cyclic invariance independently, or evaluate the loop integral.
