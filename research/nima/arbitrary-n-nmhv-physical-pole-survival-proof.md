# Arbitrary-n NMHV physical-pole survival

## Theorem

For every `n>=6`, let

$$
\mathcal A_n^{\rm NMHV}
=
\sum_{2\le i\le n-2\atop i+2\le j\le n-1}
[n,i-1,i,j-1,j]
$$

be the standard momentum-twistor BCFW representation. At generic momentum-super-twistor kinematics, every physical codimension-one boundary of this BCFW chain is a simple pole with nonzero super-residue. No physical pole cancels in the sum.

## Five-bracket residues

For five distinct labels `a,b,c,d,e`, the super five-bracket is

$$
[a,b,c,d,e]
=
\frac{
\delta^{0|4}
\left(
\eta_a\langle bcde\rangle+
\eta_b\langle cdea\rangle+
\eta_c\langle deab\rangle+
\eta_d\langle eabc\rangle+
\eta_e\langle abcd\rangle
\right)
}
{
\langle abcd\rangle
\langle bcde\rangle
\langle cdea\rangle
\langle deab\rangle
\langle eabc\rangle
}.
$$

Each denominator factor occurs to first power. On a generic point of one facet, the other four brackets are nonzero. Taking the residue removes the selected denominator and leaves the corresponding fermionic delta numerator divided by those four nonzero factors. This is a nonzero superfunction: one can select the Grassmann monomial supplied by four independent nonzero coefficients in the delta argument. Thus every five-bracket facet has a nonzero generic residue.

## Uniqueness of physical incidence

The arbitrary-n boundary classification proves that every physical facet is one of the unpaired facets

1. `F_0(i,j)` for every BCFW cell;
2. `F_1(n-3,n-1)`;
3. `F_2(2,j)` for `4<=j<=n-1`;
4. `F_3(i,n-1)` for `2<=i<=n-3`;
5. `F_4(2,4)`.

Each occurs in exactly one cell. Every other facet belongs to one of the three explicit internal pairing families and is spurious.

Fix a physical facet `P`. Exactly one summand in `A_n^NMHV` has denominator `P`; all other summands are regular at a generic point of `P`. Therefore

$$
\operatorname{Res}_{P=0}\mathcal A_n^{\rm NMHV}
=
\operatorname{Res}_{P=0}[n,i-1,i,j-1,j]
\ne0
$$

for its unique incident cell. Cancellation is impossible because there is no second singular contribution on that generic facet.

## Count

The number of surviving physical poles is

$$
N_{\rm phys}
=
\frac{n(n-3)}2,
$$

which is the number of cyclic planar channels. Every internal facet has incidence two and cancels with opposite orientation, while every physical facet has incidence one and survives.

## Relation to executable evidence

The physical-pole checkers at `n=6,7,8,9` evaluate exact Grassmann residue components and find a nonzero component on every physical pole. The arbitrary-n theorem uses those computations only as implementation regression tests. Its universal content follows from simple five-bracket poles, generic nonzero facet residues, and the proved incidence-one classification.

## Claim boundary

This proves generic nonvanishing and absence of cancellation for every physical codimension-one pole in the standard NMHV BCFW representation. It does not fix a bosonic component normalization, prove multiparticle factorization into lower amplitudes, handle nongeneric intersections of several boundaries, or extend to `N^kMHV` with `k>1`.
