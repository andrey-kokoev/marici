# 20260817-351 — Both Soft Branches and the Nine-Master Supported Extension Close

## Hard-to-vary claim

For the frozen homogeneous nine-master (q_{mathcal G_{12}})-residue system, the total-energy nearby object acquires no algebraic-kernel-to-elliptic logarithmic extension supported on

[
X_1X_2=0.
]

This claim concerns the supported principal part. It does not assert that all soft-local connection coefficients vanish.

## Frozen structure

The source decomposition is

[
1+2+2+4
]

under (C_2^{(a)}	imes C_2^{(b)}). The elliptic quotient occurs only in the final four-master character. The other three blocks belong to distinct algebraic Tate/Kummer characters.

The source involution is

[
xleftrightarrow y,qquad
aleftrightarrow b,qquad
e_8leftrightarrow e_9,
]

with the compensating sign from reversal of (dawedge db).

## Direct branch

Entry 350 directly computed the (X_2=0) branch in the (X_1=1) chart. After the source-forced saturation

[
widetilde v_{m alg}=v_{m alg}/X_2^2,
]

the kernel-to-elliptic soft principal part vanished.

## Transported branch

The point (X_1=0) is not a finite point of the (X_1=1) chart. It was therefore not evaluated by substituting an affine infinity.

Instead, the frozen source involution transports the calculation to the (X_2=1) chart. It sends

[
v_{m alg}/X_2^2
longmapsto
v_{m alg}/X_1^2
]

and exchanges (e_8,e_9). In the involuted adapted basis the residue matrix is identical, up to the source orientation sign. Consequently,

[
oxed{
operatorname{PP}_{X_1=0}
igl(R_{E_T}^{m ext}igr)=0.
}
]

This branch is source-derived by exact involutive transport; it is not an independent affine specialization.

## Remaining algebraic blocks

The exact other-block connections give soft-principal ranks

[
(0,0,1)
]

at (X_2=0), and after site exchange,

[
(0,1,0)
]

at (X_1=0).

These rank-one poles remain internal to the corresponding algebraic rank-two character blocks. Exact character decomposition gives zero off-character entries into the elliptic block.

Therefore the full nine-master kernel-to-elliptic supported principal rank is

[
oxed{0}.
]

## Replication

The direct final-block reconstruction and the resulting nine-master synthesis agree over

[
p_1=2305843009213693951,
qquad
p_2=2305843009213693921,
]

using disjoint deterministic streams.

## Narrow result

[
oxed{
	ext{On }E_T=0,	ext{ no algebraic-to-elliptic logarithmic extension is supported on }X_1X_2=0
}
]

in the frozen homogeneous nine-master de Rham system.

What remains at the soft branches consists of:

- the elliptic quotient degeneration;
- Tate/Kummer poles internal to algebraic character blocks;
- regular finite coefficient mixing.

All are carried by the existing site-soft divisor. No new cosmological carrier incidence is required by this test.

## Scope boundary

This does not prove:

- compatibility with the physical relative integration chain;
- integral-lattice or integral-monodromy closure;
- extension across every nonsoft discriminant component;
- the global Cut--nearby comparison;
- absence of supported classes after character symmetry is broken by additional marked data.

## Evidence

- `research/benincasa/soft-support-both-sites-certificate.json`
- `research/benincasa/soft-support-both-sites-replication-certificate.json`
- `research/benincasa/soft-support-nine-master-certificate.json`
- `research/benincasa/soft-support-nine-master-replication-certificate.json`
- executable commands:
  - `soft-support-both-sites-test`
  - `soft-support-nine-master-test`

## Prior update

This closes the finite homogeneous soft-support loophole left by generic localization. It strengthens H2:

[
	ext{shared carrier and calculus}
+
	ext{sector-specific coefficient objects}.
]

It does not distinguish H2 from H3 globally, because the physical relative chain and Cut--nearby square remain unconstructed.

## Next falsifier

Construct the physical relative-chain realization of the nine-master nearby object and test whether the chain boundary map commutes with the frozen infinity-Gysin quotient at both soft branches. A failure that cannot be represented by the existing marked denominator boundary or site-soft support would be the first evidence here for new carrier data.
