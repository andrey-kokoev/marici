---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# Generic Soft-Corner Mixed Extension Vanishes in the Final Four-Master Block

## Record

Status: exact finite-field bivariate reconstruction and common-frame
soft-corner calculation for the frozen (q_{\mathcal G_{12}}) final
four-master de Rham block. No source master, denominator, support component,
normalization, projector, or carrier cell is added.

This closes the finite target left by entry 313.

## Deutsch--Popperian claim

Freeze

[
u=\ell_4=E_T,qquad v=\ell_3,qquad B=uv,
]

the source Griffiths--Dwork basis ((e_6,e_7,e_8,e_9)), the explicit
infinity--Gysin quotient, its kernel

[
A_{--}=langle e_6,v_{m alg}angle,
]

and the nodal coordinate (n=uv/A), with (A) a unit away from
(X_1X_2=0).

Entry 313 isolated two possible mixed SNC extension coordinates,

[
(arepsilon_{e_6},arepsilon_{v_{m alg}}).
]

The hard-to-vary claim tested here is that the antisymmetric off-diagonal
residue difference vanishes after both normal residues are placed in one
Gysin-adapted logarithmic frame and their common Deligne principal part is
removed.

## Frozen calculation

The complete source connection was reconstructed over

[
mathbf F_p,qquad p=2^{61}-1,
]

from independent Griffiths--Dwork samples. The source basis closes at total
degree seven. The regular Gysin-adapted basis

[
(e_6,v_{m alg},widetildeomega_0,widetildeomega_2)
]

was constructed before taking either normal residue; its rational connection
closes at total degree twelve.

Specializing the source-basis (u)-residue before this change of frame
produces a simple (1/v) pole. After the Gysin adaptation, both normal
residues have the same off-diagonal principal part:

[
P_{m common}=
egin{pmatrix}
0&0&0&0\
0&0&0&0\
0&-rac12&0&0\
0&-rac12&0&0
end{pmatrix}.
]

Thus this singular term is diagonal coboundary data, not the mixed class.

Removing that common principal part gives equal finite residues. Their
elliptic quotient block is

[
R_u^{m ell}=R_v^{m ell}=
egin{pmatrix}
-rac14&rac14\
-rac14&rac14
end{pmatrix},
]

and their algebraic--elliptic off-diagonal block is

[
E_u=E_v=
egin{pmatrix}
0&-rac12\
0&-rac14
end{pmatrix}.
]

Therefore

[
oxed{E_v-E_u=0}
]

and hence, in the frozen normalization,

[
oxed{
(arepsilon_{e_6},arepsilon_{v_{m alg}})=(0,0).
}
]

## Narrow consequence

The hidden two-dimensional extension space identified in entry 313 is a real
space of possibilities, but the actual frozen final four-master connection
occupies its zero class at the generic soft corner.

Consequently the source last-three cyclic module also has zero hidden mixed
class. No cosmology-specific carrier stratum is required by this test.

The classification is

[
oxed{
	ext{existing signed-energy SNC carrier}
+
	ext{Tate/Kummer/Legendre coefficient data},
}
]

with no residual mixed coefficient extension in the tested final block.

## Scope boundary

This establishes only the generic rational de Rham statement away from
(X_1X_2=0), in one finite-field reconstruction with the source-fixed
normalization. It does not establish:

- extension through soft support;
- integral lattice normalization;
- compatibility with the physical relative integration chain;
- a canonical splitting of the full nine-master variation;
- any all-graph or all-loop statement;
- the location of (mathcal Q) inside the algebraic connection or a different
  global extension.

The vanishing mixed corner class does not imply that every supported
extension vanishes.

## Exact evidence

- `research/benincasa/marici-gm/src/main.rs`;
- `research/benincasa/marici-gm/soft-corner-common-frame-certificate.json`;
- prime (2305843009213693951);
- source reconstruction degree (7);
- Gysin-adapted reconstruction degree (12);
- full Rust tests passed.

## Next finite falsifier

Repeat the common-frame calculation in a second prime and a disjoint sampling
stream, then test extension through the soft loci (X_1X_2=0). A failure of
prime/stream stability retracts the present finite-field conclusion. A stable
generic result followed by a nonzero soft-supported class would locate that
class on already frozen soft support rather than create a new generic carrier
incidence.

## Outcome contract

~~~json
{
  "claim": "The generic final-block mixed SNC extension class vanishes after common Gysin adaptation and diagonal Deligne principal-part subtraction.",
  "status": "verified_generic_finite_field_de_rham",
  "prime": "2305843009213693951",
  "source_reconstruction_degree": 7,
  "adapted_reconstruction_degree": 12,
  "common_principal_part": true,
  "antisymmetric_rank": 0,
  "epsilon_e6": 0,
  "epsilon_v_alg": 0,
  "new_carrier_datum": false,
  "classification": "existing signed-energy SNC carrier plus sector-specific coefficient data",
  "scope": "generic final four-master rational de Rham locus away from soft support",
  "next_experiment": "Repeat at a second prime and disjoint stream, then test supported extension through X1*X2=0."
}
~~~
