---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Soft--Gram Normal Crossings and the Integrable Literal Site-Soft Endpoint

## Record

Date: 2026-08-15

Status: exact finite soft--Gram overlap census and literal simple-pole
site-soft endpoint power-counting theorem for the three-site one-loop
Bunch--Davies source at (d=3).

This entry continues entries 185, 187, 188, and the Benincasa entry 189.
It changes no source denominator, normalization, physical chain, support
summand, or carrier cell.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

[
oxed{
	ext{An intersection of fixed-base Gram components can create a new
non-product physical vanishing cycle away from pre-existing soft support.}
}
]

The finite falsifier was either:

1. a pair of distinct physical Heron components meeting in the nonnegative
   momentum cone without forcing a soft resultant; or
2. a logarithmic radial exponent in the literal source at the corresponding
   true site-soft endpoint.

Neither occurs.

## Frozen Gram factorization

For nonnegative external resultants (P_1,P_2,P_3), write the four signed
Heron factors

[
f_1=P_1-P_2-P_3,
qquad
f_2=P_1-P_2+P_3,
]

[
f_3=P_1+P_2-P_3,
qquad
f_4=P_1+P_2+P_3.
]

The fixed-base Gram polynomial is their product up to the frozen source
normalization. The physical triangle boundary uses (f_1,f_2,f_3);
(f_4=0) in the nonnegative cone only at the origin.

## Exact pair and multiple-intersection census

Solving the signed linear systems in the nonnegative cone gives

[
f_1=f_2=0
quadLongrightarrowquad
(P_1,P_2,P_3)=(t,t,0),
]

[
f_1=f_3=0
quadLongrightarrowquad
(P_1,P_2,P_3)=(t,0,t),
]

[
f_2=f_3=0
quadLongrightarrowquad
(P_1,P_2,P_3)=(0,t,t).
]

Thus every pair of distinct physical Heron components forces one soft
resultant:

[
oxed{
f_i=f_j=0, i
e j
quadLongrightarrowquad
P_k=0
}
]

for the complementary index (k).

Every pair involving (f_4) lies at

[
P_1=P_2=P_3=0.
]

The coefficient matrix of (f_1,f_2,f_3) has exact determinant

[
det
egin{pmatrix}
1&-1&-1\
1&-1& 1\
1& 1&-1
end{pmatrix}
=-4,
]

so their triple intersection is also only the origin. There is no
nonsoft physical multi-Gram stratum.

## Resolved soft--orientation corner

Entry 189 supplies resolved normals (p) and (v) with

[
Lambda_P=-4p^2v^2
]

and literal oriented source prefactor

[
3pv.
]

Freezing (p) and (v) before descent therefore gives a normal-crossing
product. The coarse Gram equation combines two already resolved rank-one
normals; it does not create a third irreducible normal.

The local coefficient characters are products of the existing soft and
orientation Kummer characters. On the resolved cover there is no new
Picard--Lefschetz transvection. In particular,

[
oxed{
T_u=1,
qquad
N=0
}
]

for this product corner. This does not assert that the semisimple character
is trivial: descent through either quadratic coarse normal may retain its
rank-one sign character.

## Literal site-soft endpoint

At a true site-soft endpoint, freeze

[
X_i=P_i=0,
qquad
ho=|ell|longrightarrow0.
]

For the literal six-term source, a term supplies at most one simple
(q_{g_i})-pole at this endpoint. In three spatial dimensions,

[
rac{d^3ell}{q_{g_i}}
sim
rac{ho^2,dho,dOmega}{ho}
=
ho,dho,dOmega.
]

The exact radial exponent is therefore

[
oxed{+1}.
]

It is integrable and is not the logarithmic exponent (-1). Hence the
literal simple-pole source produces no unipotent endpoint logarithm at this
site-soft face.

If all three resultants and all site energies are simultaneously soft, then

[
q_{mathcal G}=E_T=0.
]

That locus is the already frozen total-energy support, not a new radical
carrier generator.

## Physical Picard--Lefschetz classification

For the overlap strata proved here:

- oriented physical-chain intersection: no new non-product thimble;
- resolved variation: zero;
- semisimple monodromy: product of existing rank-one Kummer characters;
- unipotent logarithm: (N=0);
- existing carrier incidence: fixed-base Cayley--Menger/Gram boundary;
- soft support: exactly the forced (P_k=0) loci and the all-soft origin;
- graph homology: not invoked;
- genuinely new carrier datum: none.

Thus

[
oxed{
	ext{physical multi-Gram overlap}
=
	ext{soft support}
+
	ext{normal-crossing Gram Kummer data}
}
]

within the stated literal-source scope.

## Scope boundary

This theorem covers:

- all pair and multiple intersections of the four signed fixed-base Heron
  factors in the nonnegative external-momentum cone;
- the resolved (p)-(v) soft--orientation corner;
- literal six-term source terms having one simple site-soft pole.

It does not cover:

- higher-power master insertions;
- simultaneous marked-pole and unmarked-face collisions;
- non-site-soft endpoints of the loop-distance integration domain;
- lower-dimensional Cayley--Menger face degenerations not equivalent to a
  fixed-base Heron intersection;
- extension data after integrating across several boundary faces.

Those remain separate finite falsifiers.

## Exact evidence

- `research/benincasa/verify_soft_gram_overlap_census.py`
  - dependency-free exact signed-factor and radial-power verifier;
- `research/benincasa/soft_gram_overlap_census_result.json`
  - result packet, SHA-256
    `70efd91360d02819dfa5478eff99e1e0409c60cac83723a92ccd6e97f788975f`;
- native Scheduler execution:
  - task `\Narada\MariciSoftGramOverlapCensus`;
  - last result (0);
- entry 189:
  - exact oriented-chart identity (Lambda_P=-4p^2v^2);
  - exact source prefactor (3pv);
- frozen primary source:
  - Benincasa et al., arXiv:2408.16386,
    equations `eq:mCM`, `eq:ukchi`, and `eq:Triangle`.

## Next finite falsifier

Freeze the complete unmarked boundary of the three-distance
Cayley--Menger integration domain. Resolve, one component at a time:

1. loop-point coplanarity (z=0);
2. distance endpoints (a=0,b=0,c=0);
3. lower-dimensional face-volume degenerations;
4. their intersections with each of the ten marked affine poles.

For each component, pull back the literal six-term form to a regular
oriented chart and compute the radial exponent and oriented
Picard--Lefschetz intersection. A new carrier datum is admissible only if
a physically intersecting vanishing cycle survives and cannot be expressed
as an existing Cayley--Menger face, soft support, or coefficient-local
Kummer/relative-period class.

## Outcome contract

~~~json
{
  "claim": "Physical intersections of distinct fixed-base Gram components can create a new non-product vanishing cycle away from existing soft support.",
  "status": "falsified_in_literal_simple_pole_scope",
  "pair_intersections": {
    "f1_f2": "(t,t,0); P3=0",
    "f1_f3": "(t,0,t); P2=0",
    "f2_f3": "(0,t,t); P1=0",
    "any_with_f4": "origin"
  },
  "triple_factor_matrix_determinant": -4,
  "resolved_normals": ["p", "v"],
  "coarse_gram_normal": "-4*p^2*v^2",
  "resolved_source_normal": "p*v",
  "site_soft_radial_power_d3": 1,
  "site_soft_integrable": true,
  "site_soft_logarithm": false,
  "T_u": 1,
  "N": 0,
  "classification": "soft support plus fixed-base Gram Kummer data on existing Cayley-Menger carrier",
  "new_carrier_datum": "none",
  "scope_boundary": "Literal six-term source with one simple site-soft pole; higher-power masters and simultaneous marked-face collisions remain open.",
  "next_experiment": "Audit every unmarked Cayley-Menger endpoint and face, then its overlaps with all ten marked affine poles."
}
~~~
