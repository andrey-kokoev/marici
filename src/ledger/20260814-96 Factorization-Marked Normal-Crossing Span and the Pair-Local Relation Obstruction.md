# Factorization-Marked Normal-Crossing Span and the Pair-Local Relation Obstruction

## Record

Date: 2026-08-14

Status: exact finite-nonresonant theorem for the \(D=03\) marked coefficient
span, together with a pair-local no-go theorem for the \(\Delta\) relation.

Scope: factorization-marked six-point scalar geometry, the occurrence cosheaf
of entries 83 and 86, and the facewise Pochhammer--Cousin complex of entry 38.
This is a boundary-costalk result. It is not yet the bivariant trace to a
primal circuit tag or the full scalar total-specialization map.

## Claim

The physical face \(F_{03}\) is the actual product square

\[
F_{03}=K_4\times K_4
\]

with vertices

\[
v_{00}=x_0x_3,\qquad v_{10}=x_1x_3,\qquad
v_{01}=x_0x_4,\qquad v_{11}=x_1x_4.
\]

Entry 86's sink marks select the two coordinate edges

\[
Z_0=\{03,02\}=[v_{00},v_{01}],
\qquad
Z_3=\{03,35\}=[v_{00},v_{10}].
\]

Their fiber product in the factorization-marked scalar face category is the
single actual triangulation

\[
\boxed{
W_{03}=Z_0\times_{F_{03}}Z_3
=\{03,02,35\}=v_{00}.}
\]

Thus the correspondence requested in entry 95 exists canonically:

\[
\boxed{Z_0\longleftarrow W_{03}\longrightarrow Z_3.}
\]

The fixed marks are essential. After forgetting them, both \(v_{00}\) and
\(v_{11}\) are saturated common lower cells.

On the universal normal torus, put

\[
u_0=q_0-1,\qquad u_3=q_3-1.
\]

The two pullbacks to \(W_{03}\) are the independent primitive characters

\[
u_0\longmapsto(1,0),
\qquad
u_3\longmapsto(0,1).
\]

They form a regular sequence. The minimal support-preserving middle
coefficient is therefore the oriented two-variable Koszul complex

\[
\boxed{
K(u_0,u_3)=K(u_0)\otimes K(u_3),
\qquad \operatorname{or}=h_0\wedge h_3.}
\]

Rank zero erases support, while rank one identifies the two normal divisors
up to a Laurent unit and destroys the bifiltration. No common rank-one target
character is introduced.

Because \(Z_0\) and \(Z_3\) are transverse coordinate faces, entry 38 applies
without a new coefficient specialization. It gives the occurrence-decorated
PC face tubes, normal Koszul factors, Cousin maps, and the ambient
\(F_{03}\) top-cell coherence.

Orient the four square edges by

\[
a:v_{00}\to v_{10},\quad
b:v_{01}\to v_{11},\quad
c:v_{00}\to v_{01},\quad
d:v_{10}\to v_{11}.
\]

The marked span supports only \(a\) and \(c\). The unique integral supported
primitive with the entry-86 endpoint boundary is

\[
\boxed{H_{03}^{\rm mark}=a-c,
\qquad \partial H_{03}^{\rm mark}=v_{10}-v_{01}.}
\]

The alternative \(b-d\) passes through the unmarked corner \(v_{11}\). The
two representatives remain derived-equivalent because

\[
(a-c)-(b-d)=a-b-c+d=\partial[F_{03}].
\]

This removes the strict lower-Cousin ambiguity left in entry 95. The output
is nevertheless typed on the **road costalk**. With entry 89's Laurent
duality it is the cocycle

\[
d_1^\vee\otimes\chi_N,
\]

not the primal tag \(d_1\).

There is also a sharp pair-local obstruction. The two relevant conductor
columns obey

\[
K_{\rm alt}(u_0)=-d_1,
\qquad
K_{\rm alt}(u_3)=+d_1.
\]

Every degree-one image of this pair is therefore contained in
\(\mathbb Z d_1\), while

\[
\Delta=d_0+d_1+d_2\notin\mathbb Z d_1.
\]

Consequently:

\[
\boxed{
\text{the single }(u_0,u_3)\text{ span cannot realize the }\Delta
\text{ relation in a chain map}.}
\]

The relation can only be tested after the three already-existing pairs

\[
(u_2,u_5)\to d_0,
\qquad
(u_0,u_3)\to d_1,
\qquad
(u_1,u_4)\to d_2
\]

have been assembled with one separately typed relation object.

## Evidence

The actual scalar-face and occurrence census is

`research/voevodsky/check_d03_factorization_marked_span.rs`.

SHA-256:

```text
1c7ff7d8e3d3fbb11042929efbe45e27f75d7facfbc532b5c1a7347f54c8c337
```

The universal-character, Koszul, minimality, and pair-local relation audit is

`research/voevodsky/check_d03_minimal_normal_torus_span.rs`.

SHA-256:

```text
99fd0571bb61075fe7a44913fa3b1311ea633436f5aac2fa4159a5102a23907d
```

Reproduce both with:

```powershell
$sources = @(
  "research/voevodsky/check_d03_factorization_marked_span.rs",
  "research/voevodsky/check_d03_minimal_normal_torus_span.rs"
)
foreach ($src in $sources) {
  rustfmt --edition 2021 --check $src
  $exe = Join-Path $env:TEMP ((Split-Path $src -LeafBase) + ".exe")
  rustc --edition=2021 -D warnings -O $src -o $exe
  & $exe | ConvertFrom-Json | Out-Null
}
```

The primary audit reran both programs successfully. Inherited inputs are
entries 38, 83, 86, 89, 94, and 95 and their cited certificates.

## Boundary

- The PC statement is on entry 38's finite nonresonant domain. Resonant
  nearby-cycle extension is not claimed.
- The factorization marks are genuine extra scalar-geometric data. The bare
  one-parameter amplitude family does not select \(v_{00}\).
- The theorem constructs a supported road-costalk diagram and its dual
  cocycle. It does not identify \(d_1\cong d_1^\vee\).
- The ambient square top cell proves homotopy between the two Cousin paths;
  it does not supply a circuit relation generator.
- The no-go result is pair-local. Entry 95's complete three-pair carrier fold
  to \(\Delta\) remains valid.
- No rational splitting, new transition map, fitted differential, or new
  generator has been used.

## Consequence

The occurrence-loaded problem now separates into two coherent stages.

First construct a bivariant pairing

\[
\boxed{
\Theta_1^{\rm PC}:
\mathcal S_1^{\rm mark}\boxtimes\mathcal Q_{03}^{\rm PC}
\longrightarrow\mathbf1_{\chi_N},}
\]

where \(\mathcal S_1^{\rm mark}\) is the supported diagram
\(Z_0\leftarrow W_{03}\to Z_3\) and \(\mathcal Q_{03}^{\rm PC}\) is the road
costalk. Its associated grade must be entry 89's unit Laurent pairing and its
boundary must be entry 86's marked endpoint counit. Currying would give the
desired local primal-tag trace

\[
\operatorname{Tr}_1^{\rm PC}:
\mathcal S_1^{\rm mark}
\longrightarrow
\mathbb D(\mathcal Q_{03}^{\rm PC})\otimes\chi_N
=:\mathcal T_1^{\rm PC}.
\]

Only after constructing the rotated \(\mathcal T_0^{\rm PC}\) and
\(\mathcal T_2^{\rm PC}\) should one test a combined relation cell

\[
d\mathcal K_{\rm rel}^{\rm PC}
=\mathcal T_0^{\rm PC}+\mathcal T_1^{\rm PC}+\mathcal T_2^{\rm PC}.
\]

The next falsifier is therefore local and precise: prove or disprove the
bivariant PC pairing \(\Theta_1^{\rm PC}\) with the two independent normal
characters, all lower Cousin terms, twist reversal, and the entry-86 endpoint
normalization retained.
