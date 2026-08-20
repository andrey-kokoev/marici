# Cyclic \(\mathcal Q\) sector and physical-chain assembly certificate

Date: 2026-08-15

## Frozen source

Primary source: Benincasa--Brunello--Mandal--Mastrolia--Vazão,
arXiv:2408.16386v2, source file
`temp/arxiv-2408.16386-source/sections/applications.tex`,
SHA-256
`3e92460fe2e34dc21a537c784dab3b2fbcd9b7cfee9e7372f06971b50d8b6f9b`.

Equation `eq:Triangle` (source lines 204--243) is
[
I_{{1}}^{(3,1)}
=kappa_0int_Gammaprod_e(dy_e,y_e)
rac{K^gamma}{q_{mathcal G}prod_{j=1}^3q_{mathfrak g_j}}
sum_{m cyc}
rac1{q_{mathcal G_{ij}}}
left(rac1{q_{mathfrak g_{jk}}}+rac1{q_{mathfrak g_{ki}}}ight).
]
All six displayed coefficients are (+1); all terms use the same oriented
chain (Gamma) and common measure. Source lines 245--260 give
[
q_{mathcal G}=E,qquad
q_{mathfrak g_j}=y_{j-1,j}+X_j+y_{j,j+1},qquad
q_{mathcal G_{j,j+1}}=E+y_{j,j+1}.
]

The cyclic relabeling
[
ho:(1,2,3)mapsto(2,3,1)
]
acts simultaneously on (X_i,y_{ij}), denominators, and the
Cayley--Menger geometry. It preserves the loop orientation because
[
dy_{12}wedge dy_{23}wedge dy_{31}
mapsto
dy_{23}wedge dy_{31}wedge dy_{12}
]
is an even three-cycle.

## Three quartics

Put (E=X_1+X_2+X_3). Define
[
mathcal Q_{ij}
=-16X_i^2X_j^2-8X_iX_jE^2
+8(X_i+X_j)E^3-5E^4.
]
The published quartic is (mathcal Q_{12}), and
[
ho(mathcal Q_{12})=mathcal Q_{23},qquad
ho^2(mathcal Q_{12})=mathcal Q_{31}.
]

For the cyclicly transported sectors,
[
ho^{-1}(mathcal Q_{12})=mathcal Q_{31}
quad	ext{on the canonical }q_{mathcal G_{12}}	ext{ model of sector }23,
]
and
[
ho^{-2}(mathcal Q_{12})=mathcal Q_{23}
quad	ext{on the canonical model of sector }31.
]

## Exact raw-discriminant test

`check_cyclic_q_log_smoothness.rs` extends the exact checker of ledger 175.
For every one of the 1,719 nonconstant raw codimension-one conditions it
performs fraction-free multivariate pseudo-division by all three targets:
(mathcal Q_{12}) in (z), (mathcal Q_{23}) in (x), and
(mathcal Q_{31}) in (y). No specialization is used.

The executed optimized Rust binary returned exit code zero. Thus all
[
3cdot1719=5157
]
factor tests reject the target quartic. The census still contains:

- seven surface singularity conditions;
- twelve displayed surface codimension-one factors;
- the complete 23-line marked arrangement;
- line tangencies;
- 60 nonconstant line-coincidence conditions;
- 250 nonconstant branch-at-pair conditions;
- 1,360 nonconstant triple-incidence conditions.

Together with the sheet-switch lemma and simultaneous-resolution argument
of ledger 181, cyclic covariance therefore gives, at generic nonsoft
kinematics,
[
T_{mathcal Q_{12}}^{(12)}
=T_{mathcal Q_{12}}^{(23)}
=T_{mathcal Q_{12}}^{(31)}=1,
]
[
N_{mathcal Q_{12}}^{(ij)}=0,qquad
operatorname{Var}_{mathcal Q_{12}}
(Gamma^{m res}_{ij,+})=0.
]

## Exhaustion of the non-residue alternative

Residue regularity alone would not exclude a pinch supported entirely in
the shared lower sector, omitting (q_{mathcal G_{ij}}). The primary
source supplies the independent check.

Source lines 330--366 identify that lower/zero sector and print its complete
homogeneous dlog alphabet:
[
{X_1,X_2,X_3,X_1+X_2,X_2+X_3,X_1+X_3,
X_1-X_2-X_3,X_1-X_2+X_3,
X_1+X_2-X_3,E}.
]
It contains no (mathcal Q_{12}) component. Hence its connection and
physical periods extend across a generic point of (mathcal Q_{12}=0)
away from intersections with those ten linear supports.

The source introduces the algebraic letter only in the
(q_{mathcal G_{12}})-containing elliptic sector (lines 448--455), which
is precisely the sector closed by ledgers 175--181 and the cyclic test
above.

## Source-weighted assembly

Let (I_{ij}^{(a)}), (a=1,2), be the two displayed terms in the
(q_{mathcal G_{ij}}) sector. Equation `eq:Triangle` fixes
[
I_{{1}}^{(3,1)}=sum_{ij=12,23,31}sum_{a=1}^2 I_{ij}^{(a)}
]
with constant coefficient (+1) and one boundary-value chain (Gamma).
Analytic continuation is linear, so
[
operatorname{Var}_{mathcal Q_{12}}I_{{1}}^{(3,1)}
=sum_{ij,a}operatorname{Var}_{mathcal Q_{12}}I_{ij}^{(a)}=0.
]
Thus
[
oxed{
T_{mathcal Q_{12}}^{m phys}=1,qquad
N_{mathcal Q_{12}}^{m phys}=0,qquad
operatorname{Var}_{mathcal Q_{12}}(Gamma_{m phys})=0
}
]
at a generic nonsoft point outside the frozen linear/discriminant union.

This proves no (mathcal Q_{12})-supported extension at the level of the
source scalar period and its physical relative chain. It does **not** prove
that an arbitrary master-basis Gauss--Manin filtration splits canonically;
a singular matrix representation may still contain apparent
(mathcal Q_{12}) poles.

## Classification

- existing carrier: energy/Cut incidence, Cayley--Menger domain, source
  hyperplanes, signed-minor boundary, and their frozen resolutions;
- coefficient support at generic (mathcal Q_{12}=0): none in the
  homogeneous source system;
- relative-cycle support: none;
- cross-sector extension detected by the physical scalar period: none;
- (mathcal Q_{12}): globally apparent for the displayed homogeneous
  simplex integral at generic nonsoft kinematics;
- genuinely new carrier datum: none.

## Scope

The result excludes intersections of (mathcal Q_{12}=0) with soft
support, the ten lower-sector letters, and the frozen residue
discriminants. It is a theorem for the displayed homogeneous simplex
integral and its cyclic sectors, not an integral-lattice or
discriminant-extension theorem and not a result for the generic
multi-external-leg specialization.
