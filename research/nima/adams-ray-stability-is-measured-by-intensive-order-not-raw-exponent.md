# Adams-ray stability is measured by intensive order, not raw exponent

## Cycle and end decomposition

In an infinite typed object graph, completion stability requires both:

1. nonexpanding affine holonomy on repeated typed cycles;
2. controlled topology at every admitted infinite end.

The Adams ray

[
1	o2	o4	o8	ocdots
]

has no cycle, so cycle tests alone cannot decide it.

## Two order coordinates

At Fock grade (k), the physical Mellin location is

[
q=klog p.
]

There are two ways to record exponential order:

- raw prime exponent (r_k), using (p^{r_k});
- intensive physical order
  [
  eta_k=rac{r_k}{k},
  ]
  using (e^{eta_k q}=p^{keta_k}).

Under grade doubling (kmapsto2k), a raw profile

[
r_{2k}=2r_k
]

looks exponentially expanding along the ray. But

[
eta_{2k}
=
rac{r_{2k}}{2k}
=
rac{r_k}{k}
=
eta_k.
]

Thus (ho(r)=2r) can be exact preservation of physical exponential order,
not runaway. The apparent growth is caused by expressing one fixed decay rate
in coordinates whose grade is doubling.

## Source-compatible end object

For each grade (k), define a test rung by the physical weight

[
q_{eta,k}(x)
=
sum_p |x_{p,k}|e^{eta klog p}
=
sum_p |x_{p,k}|p^{keta}.
]

A natural Adams-end space controls one common intensive parameter (eta)
across all grades. For example, a projective test topology may use seminorms

[
q_eta(x)
=
sum_{k,p}|x_{p,k}|p^{keta}
]

with the source-authorized grade weights included separately.

If Adams transport satisfies

[
q_{eta,2k}(A_2x)
le C_eta q_{eta,k}(x)
]

with constants stable along admitted iteration, the infinite grade ray is
continuous at fixed intensive order.

## End obstruction

Let (r_k) be the least raw exponent needed to contain the grade-(k)
constructor image. The sharp end invariant is

[
sup_krac{r_k}{k}.
]

A finite bound gives one physical exponential order controlling the entire
Adams ray. If

[
rac{r_k}{k}	oinfty,
]

no fixed intensive rung receives the ray, even though every finite grade lies
in some raw dual step.

For the dyadic ray, the same criterion is

[
sup_nrac{r_{2^n}}{2^n}<infty.
]

This is stronger and more source-invariant than boundedness of the raw
(r_{2^n}), which is generally the wrong requirement.

## Norm constants remain separate

Stable order indices do not control operator amplification. One also needs

[
sup_n
left|
A_2^{(2^{n-1})}cdots A_2^{(1)}
ight|_{eta}<infty
]

or a declared weaker bound appropriate to the end topology. The half-density
coefficients may make these composites contractive, but that is a separate
calculation.

Thus Adams-end stability has two independent coordinates:

[
	ext{intensive order orbit},
qquad
	ext{absolute transport norm}.
]

## Regrading authority

The change (r_kmapstoeta_k=r_k/k) is legitimate only because the source
incidence is at (klog p). It is not an arbitrary gauge chosen to hide
growth. Any further object-dependent regrading must be uniformly equivalent to
this physical source topology.

The minimal hostile has bounded raw transport norms but
(r_k/k	oinfty). Another has bounded intensive order but composite norms
diverging along the ray.

## Full audit

For each admitted infinite path, record:

1. object grade or physical length scale;
2. raw affine order composite;
3. normalized intensive order;
4. composite norm and inverse norm where applicable;
5. the declared end object and convergence mode.

For closed paths, retain affine cycle holonomy. For infinite Adams rays, test
the intensive order and norm limits.

The first Adams edge uses only grade (1	o2), but constructor coherence under
all Adams operations requires this end theorem. It prevents both false
rejection of harmless grade scaling and false acceptance of genuine
superlinear order escape.
