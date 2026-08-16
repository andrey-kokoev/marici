# Extraordinary Triple Top and the Generic \(q_\Sigma\) Comparison

## Record

Date: 2026-08-15

Status: proved in the finite extraordinary category obtained by adjoining the
pair objects of entry221 and the canonical projectivized-conductor SNC top.
The integral triple comparison with entry113's mixed block is derived and
unique. Literal entry143 six-functor realization, its rank-nine contraction,
and the physical endpoint/\(Q\) mapping fiber remain unconstructed. No graph
admission is claimed.

## Oriented triple object

For the positive conductor
\[
J_+=(x_1,x_3,x_5),
\]
the canonical projective normal cone \(\mathbf P(J_+/J_+^2)\) supplies one
oriented triple top \(W_{012}\). Its three coordinate facets are the long-road
packets and its pair strata are the external \(W_{ij}\) objects constructed
in entry221.

In cyclic road order the incidence complex is
\[
\mathbf Z\langle W_{012}\rangle
\xrightarrow{N}
\mathbf Z^3\langle\text{facets}\rangle
\xrightarrow{R-I}
\mathbf Z^3\langle W_{ij}\rangle ,
\qquad N=(1,1,1)^T.
\]
The equation \((R-I)N=0\) proves \(d^2=0\). The top column is primitive. The
pair differential has Smith form \(\operatorname{diag}(1,1,0)\), and its
kernel is exactly the image of \(N\). Thus the complex is exact at the facet
grade and introduces no integral torsion.

Tensoring the four Boolean normal states and the two conductor Tor spectator
grades gives eight exact copies:
\[
\operatorname{rank}C_2=8,\qquad
\operatorname{rank}C_1=24,\qquad
\operatorname{rank}C_0=24.
\]
All 48 Tor-decorated pair BC restrictions from entry221 remain unit maps.

## Derived generic/special comparison

The projective augmentation has boundary
\[
dW_{012}=q_\Sigma-s_{14}-s_{03}-s_{25}.
\]
Normalization provenance fixes \(\epsilon(q_\Sigma)=3\), while each labelled
special residue has augmentation one. Hence \(3-1-1-1=0\) without division by
three.

Entry113 independently fixes
\[
dH_\Sigma=q_\Sigma-\sum_Dx_D\widetilde\xi_D.
\]
The generic and three special maps are already primitive and labelled. If
\(W_{012}\mapsto aH_\Sigma\), the generic row forces \(a=1\), and every
special row independently forces the same equation. Therefore
\[
\boxed{W_{012}\longmapsto H_\Sigma}
\]
with coefficient \(+1\) is derived uniquely from the chain equation. It is
not a stipulated top scalar.

Rotation fixes the norm and cycles its facets and pair objects. Reflection
reverses the oriented top and facets; the established road-orientation twist
gives the target mixed block the same character.

## Remaining realization gate

This theorem lives in the finite external correspondence category. It does
not construct a functor carrying \(W_{ij}\) and \(W_{012}\) to literal
entry143 \([S,H]\) stalk/corestriction rows. The pair objects deliberately
land chain-valuedly in road costalks because no compatible \(K_6\) face
contains a crossing pair.

Consequently the coefficient-level \(q_\Sigma\) map is now fixed, but the
literal 24 pair-corestriction homotopies and the rank-nine acyclic-complement
contraction remain absent. Until that realization functor and the two
endpoint connector cells exist in one mapping complex, the endpoint/\(Q\)
mapping fiber cannot be instantiated. The physical \(p_{\partial,Q}\), its
Bockstein, and loaded \(D_8\)/Jordan coherence remain undefined.

## Executable evidence

Checker:
\`research/voevodsky/check_dp6_extraordinary_triple_qsigma.rs\`

SHA-256:
\`dfa71fd904b1a6febe24939ca28fa081951c7c42b6b0db62cf8b5980ccb2cd94\`

Fresh rustfmt, warnings-denied optimized compilation, runtime assertions, and
JSON output passed. Native PowerShell was used only because structured-command
MCP was not exposed in this session.

## Outcome contract

~~~json
{
  "claim": "The canonical projectivized-conductor SNC top extends the extraordinary W_ij pair category to an exact integral triple complex, and compatibility with the normalization-provenanced entry113 mixed block uniquely forces W_012 to map to H_Sigma with coefficient +1.",
  "status": "proved_scoped_finite_extraordinary_triple_qsigma",
  "scope": "finite external pair/top correspondence category; no literal entry143 six-functor realization",
  "incidence": {
    "top_boundary": [1,1,1],
    "pair_boundary": "R-I",
    "d_squared": 0,
    "middle_exact": true,
    "top_smith": [1],
    "pair_smith": [1,1,0],
    "torsion": false
  },
  "augmentation": {
    "boundary": [1,-1,-1,-1],
    "epsilon_qSigma": 3,
    "epsilon_special_sum": 3,
    "derived_unique_top_coefficient": 1
  },
  "graded_ranks": {
    "boolean_states": 4,
    "tor_grades": [0,1],
    "top": 8,
    "facets": 24,
    "pairs": 24,
    "tor_decorated_pair_bc_rows": 48
  },
  "unconstructed": [
    "literal entry143 realization of external pair/top strata",
    "24 pair-corestriction homotopies",
    "rank-nine acyclic-complement contraction",
    "two endpoint connector cells",
    "physical endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "loaded D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_extraordinary_triple_qsigma.rs",
  "checker_sha256": "dfa71fd904b1a6febe24939ca28fa081951c7c42b6b0db62cf8b5980ccb2cd94"
}
~~~
