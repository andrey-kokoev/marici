---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Closed Occurrence Primitive Reconstruction Exposes the Correct Connection Test

## Record

Status: an exact rational reconstruction has produced closed homogeneous
candidates for every coefficient of the two odd primitives
(H_{31}(n)) and (H_{23}(n)). The candidates reproduce all frozen
pointwise exact solves used in the reconstruction and pass 48 held-out
exact evaluations. They obey the source involution

[
oxed{H_{23}(x,y,n)=-H_{31}(y,x,n).}
]

This is a reconstructed closed formula with exact finite validation. It is
not yet promoted to a symbolic source identity: the next test must substitute
it into the frozen derivative equation before any connection theorem is
claimed.

No regulator, projector, carrier cell, support summand, or boundary
functional is introduced.

## Deutsch--Popperian claim

The hard-to-vary candidate is

[
oxed{
H_{31}(x,y,n)=
h_1n+h_3n^3+h_5n^5+h_7n^7+h_9n^9,
qquad
H_{23}(x,y,n)=-H_{31}(y,x,n),
}
]

with

[
h_1=
rac{
1727y^6+9026xy^5+19841x^2y^4+23548x^3y^3+
16001x^4y^2+5954x^5y+959x^6
}{32x^2y^2},
]

[
h_3=
-rac{
1667y^5+6901xy^4+11640x^2y^3+10136x^3y^2+
4645x^4y+915x^5
}{16xy},
]

[
h_5=
rac{
661y^4+2113xy^3+2643x^2y^2+1585x^3y+397x^4
}{8},
]

[
h_7=
-rac{xy}{8}
left(259y^3+613xy^2+535x^2y+181x^3ight),
]

[
h_9=
rac{x^2y^2}{4}
left(25y^2+41xy+21x^2ight).
]

The finite falsifier is exact substitution into

[
H_i'v-9xynH_i
=
P_i-rac{L_i}{xy}v^5.
]

Any nonzero coefficient falsifies the reconstruction without changing the
carrier.

## Endpoint jets in closed form

Let

[
N^2=rac{2(x+y)}{xy},qquad
n_sigma(w)=sigma N
sqrt{1+rac{w^2}{2(x+y)}}.
]

Writing (H_i=sum_{j=0}^4h_{i,2j+1}n^{2j+1}), the five polar
coefficients of

[
Phi_i=rac{H_i(n)}{8(xy)^{3/2}w^9}
]

are canonically reconstructed by

[
oxed{
J_{i,sigma}^{(-9+2k)}
=
rac{sigma N}{8(xy)^{3/2}}
sum_{j=0}^4
h_{i,2j+1}N^{2j}
inom{j+	frac12}{k}
rac1{[2(x+y)]^k},
quad 0le kle4.
}
]

This makes opposite-endpoint parity and additive sewing manifest.

## Typing correction for the connection frontier

The anti-diagonal kernel of the full addition morphism

[
S:mathcal Roplusmathcal R	omathcal R,
qquad
S(alpha,eta)=alpha+eta,
]

is connection-stable formally whenever both summands carry the same
Gauss--Manin connection: (S) is constant and
(
abla S=S
abla). Testing this fact on the two distinguished source
sections would not establish the desired absolute embedding.

The nontrivial finite question is instead:

[
oxed{
	ext{Does the rank-two span of the two source-defined relative sections
close under the parameter Gauss--Manin connection?}
}
]

If it closes, one may then ask whether its sewn rank-one quotient maps
canonically into the algebraic (mathcal T_7) kernel. If it does not
close, the period-line result of entry 245 survives but no rank-two
source-section subconnection exists.

## Classification

- existing carrier: unchanged occurrence wall and endpoint divisor;
- coefficient data: two reconstructed odd relative primitives;
- involution: occurrence exchange equals (-(xleftrightarrow y));
- endpoint jets: closed binomial formula through all five polar levels;
- formally stable object: kernel of the full addition morphism;
- uncomputed object: connection closure of the two distinguished source
  sections;
- direct elliptic image: zero;
- new carrier datum: none.

## Exact evidence

- `research/benincasa/check_occurrence_jet_connection.rs`;
- `research/benincasa/occurrence-jet-connection.json`;
- ten source-graded homogeneous coefficient reconstructions;
- 48 exact held-out evaluations;
- warning-denied optimized Rust compilation.

## Next finite falsifier

1. Substitute both closed candidates into the exact frozen derivative
   equation coefficientwise.
2. Expand the closed endpoint jets and compute their (x,y) derivatives,
   including the moving endpoint (N(x,y)).
3. Test whether the two source-jet columns close under a rational
   (2\times2) connection matrix.
4. If closure holds, compute curvature and the induced sewn quotient
   connection and compare it with (omega_{m sewn}).
5. If closure fails, record the first escaping jet direction and classify
   its source-derived geometric home before considering (mathcal T_7).

## Outcome contract

~~~json
{
  "claim": "Closed homogeneous occurrence primitives are reconstructed and the correct nontrivial connection test is source-section span closure.",
  "status": "reconstructed_with_exact_held_out_validation",
  "closed_H31": true,
  "H23_relation": "-H31(y,x,n)",
  "held_out_exact_checks": 48,
  "symbolic_source_identity": "uncomputed",
  "closed_five_level_jet_formula": true,
  "full_addition_kernel_stability": "formal_by_naturality",
  "source_section_span_connection_closure": "uncomputed",
  "new_carrier_incidence": false,
  "next_experiment": "Symbolically verify the reconstructed H_i and test rank-two source-jet span closure under the moving-endpoint Gauss-Manin derivative."
}
~~~
