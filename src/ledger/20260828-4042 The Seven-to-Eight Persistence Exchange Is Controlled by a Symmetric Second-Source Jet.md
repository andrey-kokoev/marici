---
author: marici.Benincasa
---

# 4042 — The Seven-to-Eight Persistence Exchange Is Controlled by a Symmetric Second-Source Jet

## Question

Entry 4039 identified a chart-invariant exchange between a
seven-dimensional high-fiber quotient (D_7) and an eight-dimensional
occurrence-pair quotient (U_8). Does the frozen source connection
provide the missing map?

## Typed construction

The source has three labelled base derivatives. Therefore the admitted
first tests are

[
D_7\longrightarrow U_8\otimes T^*
]

and

[
D_7\longrightarrow U_8\otimes (T^*)^{\otimes2},
]

not an unmotivated scalar map (D_7\to U_8).

For every domain label, apply all derivative words of lengths one and
two to its exact source representative. Reduce through the depth-six
quotient, then project through the declared low-plus-occurrence frame.
Retain derivative-word labels and test ordered mixed commutators.

Repeat in (G_{12}) and (G_{31}) over (mathbf F_{32009}).

## Result

Every first derivative vanishes in (U_8):

[
D_7\longrightarrow U_8\otimes T^*=0.
]

At second order:

- every route lands inside the declared low-plus-occurrence frame;
- every ordered mixed-derivative commutator has rank zero;
- the map therefore factors through
  (operatorname{Sym}^2T^*);
- the combined domain map has rank seven;
- the values of all Hessian components collectively span (U_8).

Thus the source-derived object is

[
H_{m src}:
D_7\hookrightarrow
U_8\otimesoperatorname{Sym}^2T^*.
]

The aggregate ranks and commutator vanishing agree in (G_{12}) and
(G_{31}). Individual Hessian-component ranks are permuted by the chart
change, as expected for labelled base directions.

## Narrow conclusion

The (7/8) exchange is real and source-generated, but it is not yet a
two-term scalar complex

[
D_7\to U_8.
]

Its first nonzero operation is a symmetric second-source jet. Therefore
the numerical rank difference (8-7=1) is not by itself the dimension
of a cohomological cokernel: the actual target includes
(operatorname{Sym}^2T^*).

This matches the independent cosmological warning that first normal
order does not control the integrated loop deformation.

A rank-one residual becomes typed only if the frozen source supplies a
canonical contraction

[
kappa:
operatorname{Sym}^2T^*\longrightarrowmathbf 1
]

for which

[
(mathrm{id}_{U_8}\otimeskappa)H_{m src}
]

has rank seven. The next finite falsifier is to inventory only
source-derived contractions—ambient metric, Cayley--Menger Hessian,
Gram inverse, or physical-chain second jet—and test them before
examining their ranks. No fitted contraction is admissible.

## Artifacts

- `research/benincasa/checkers/check_persistence_exchange_source_derivative.py`
- `research/benincasa/results/persistence-exchange-source-derivative-g12-p32009.json`
- `research/benincasa/results/persistence-exchange-source-derivative-g31-p32009.json`

Sequence claim: `seqclaim-0a7e731fd9799a42f6ba0f25`.
