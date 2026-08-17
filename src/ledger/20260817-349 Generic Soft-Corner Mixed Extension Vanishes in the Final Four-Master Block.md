---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# Generic Soft-Corner Mixed Extension Vanishes in the Final Four-Master Block

## Record

Status: replicated finite-field bivariate reconstruction and common-frame
soft-corner calculation for the frozen \(q_{\mathcal G_{12}}\) final
four-master de Rham block. No source master, denominator, support component,
normalization, projector, or carrier cell is added.

This closes the finite target left by entry 313.

## Deutsch--Popperian claim

Freeze

\[
u=\ell_4=E_T,\qquad v=\ell_3,\qquad B=uv,
\]

the source Griffiths--Dwork basis \((e_6,e_7,e_8,e_9)\), the explicit
infinity--Gysin quotient, its kernel

\[
A_{--}=\langle e_6,v_{\rm alg}\rangle,
\]

and the nodal coordinate \(n=uv/A\), with \(A\) a unit away from
\(X_1X_2=0\).

Entry 313 isolated two possible mixed SNC extension coordinates,

\[
(\varepsilon_{e_6},\varepsilon_{v_{\rm alg}}).
\]

The hard-to-vary claim tested here is that the antisymmetric off-diagonal
residue difference vanishes after both normal residues are placed in one
Gysin-adapted logarithmic frame and their common Deligne principal part is
removed.

## Frozen calculation

The complete source connection was reconstructed independently over

\[
p_1=2305843009213693951
\]

and

\[
p_2=2305843009213693921
\]

using disjoint deterministic sampling streams. The source basis closes at
total degree seven. The regular Gysin-adapted basis

\[
(e_6,v_{\rm alg},\widetilde\omega_0,\widetilde\omega_2)
\]

was constructed before taking either normal residue; its rational connection
closes at total degree twelve.

Specializing the source-basis \(u\)-residue before this change of frame
produces a simple \(1/v\) pole. After Gysin adaptation, both normal residues
have the same off-diagonal principal part:

\[
P_{\rm common}=
\begin{pmatrix}
0&0&0&0\\
0&0&0&0\\
0&-\frac12&0&0\\
0&-\frac12&0&0
\end{pmatrix}.
\]

Thus this singular term is diagonal coboundary data, not the mixed class.

Removing that common principal part gives equal finite residues at both
primes. Their elliptic quotient block is

\[
R_u^{\rm ell}=R_v^{\rm ell}=
\begin{pmatrix}
-\frac14&\frac14\\
-\frac14&\frac14
\end{pmatrix},
\]

and their algebraic--elliptic off-diagonal block is

\[
E_u=E_v=
\begin{pmatrix}
0&-\frac12\\
0&-\frac14
\end{pmatrix}.
\]

Therefore

\[
\boxed{E_v-E_u=0}
\]

and hence, in the frozen normalization,

\[
\boxed{
(\varepsilon_{e_6},\varepsilon_{v_{\rm alg}})=(0,0).
}
\]

## Narrow consequence

The hidden two-dimensional extension space identified in entry 313 is a real
space of possibilities, but the actual frozen final four-master connection
occupies its zero class at the generic soft corner. The source last-three
cyclic module therefore also has zero hidden mixed class.

No cosmology-specific carrier stratum is required by this test. The
classification is

\[
\boxed{
\text{existing signed-energy SNC carrier}
+
\text{Tate/Kummer/Legendre coefficient data}.
}
\]

## Scope boundary

This establishes only the generic rational de Rham statement away from
\(X_1X_2=0\), replicated at two finite primes in the source-fixed
normalization. It does not establish:

- extension through soft support;
- integral lattice normalization;
- compatibility with the physical relative integration chain;
- a canonical splitting of the full nine-master variation;
- any all-graph or all-loop statement;
- the location of \(\mathcal Q\) inside the algebraic connection or another
  global extension.

The vanishing generic mixed corner class does not imply that every supported
extension vanishes.

## Exact evidence

- research/benincasa/marici-gm/src/main.rs;
- research/benincasa/marici-gm/soft-corner-common-frame-certificate.json;
- research/benincasa/marici-gm/soft-corner-common-frame-replication-certificate.json;
- primary prime \(2305843009213693951\);
- replication prime \(2305843009213693921\);
- disjoint deterministic reconstruction streams;
- identical rational principal and finite-part matrices at both primes;
- source reconstruction degree \(7\);
- Gysin-adapted reconstruction degree \(12\);
- Rust tests passed in both feature configurations.

## Next finite falsifier

Test extension through the soft loci \(X_1X_2=0\). A nonzero supported class
there would live on already frozen soft support rather than define a new
generic carrier incidence. If no supported class survives, the final-block
soft-corner extension problem closes in its present rational de Rham scope.

## Outcome contract

~~~json
{
  "claim": "The generic final-block mixed SNC extension class vanishes after common Gysin adaptation and diagonal Deligne principal-part subtraction.",
  "status": "replicated_generic_finite_field_de_rham",
  "primes": [
    "2305843009213693951",
    "2305843009213693921"
  ],
  "disjoint_sampling_streams": true,
  "source_reconstruction_degree": 7,
  "adapted_reconstruction_degree": 12,
  "common_principal_part": true,
  "antisymmetric_rank": 0,
  "epsilon_e6": 0,
  "epsilon_v_alg": 0,
  "new_carrier_datum": false,
  "classification": "existing signed-energy SNC carrier plus sector-specific coefficient data",
  "scope": "generic final four-master rational de Rham locus away from soft support",
  "next_experiment": "Test supported extension through X1*X2=0."
}
~~~
