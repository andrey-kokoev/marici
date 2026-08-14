# Reciprocal-Twist D03 Bivariant Road Trace

## Record

Date: 2026-08-14

Status: exact finite-nonresonant theorem on the established \(D=03\)
road-face Pochhammer--Cousin costalk, together with a scope obstruction for
any larger full-object interpretation.

This entry closes stage 1 of `docs/nima-research-objective.md`. It constructs
the bivariant trace requested in entry 96 after making its support and twist
directions explicit. It does not construct the three-pair \(\Delta\) relation.

## Claim

Write

\[
\mathcal Q_{03,\partial}^{\rm PC}
\]

for exactly the entry-38 regularized road-face costalk: the weighted
\(K_4\times K_4\) square, all its forced lower Cousin faces, and its normal
Koszul factors. This notation does **not** denote the full
\(\operatorname{PC}(\mathsf J_4\boxtimes\mathsf J_6)\), whose contact kernel
was isolated in entry 89.

The correct two inputs have opposite support and twist types:

\[
\mathcal S_{1,\rm reg}^{\rm mark,\vee}
\quad\text{and}\quad
\mathcal Q_{03,\partial,\rm lf}^{\rm PC}.
\]

The first is the reciprocal-twist, regularized/ordinary image of the marked
span \(Z_0\leftarrow W_{03}\to Z_3\). The second is the locally
finite/Borel--Moore road factor with the original twist. Thus the coefficient
evaluation is

\[
\mathscr L^\vee\otimes\mathscr L\longrightarrow\mathbf1,
\]

not an identification of two same-twist PC chains.

Over

\[
R_{03}
=
\mathbb Z[
x_0^{\pm1},x_1^{\pm1},x_3^{\pm1},x_4^{\pm1},
q_0^{\pm1},q_3^{\pm1},
(q_0-1)^{-1},(q_3-1)^{-1}],
\]

there is a canonical homotopy class

\[
\boxed{
\Theta_{1,\partial}^{\rm PC}:
\mathcal S_{1,\rm reg}^{\rm mark,\vee}
\boxtimes
\mathcal Q_{03,\partial,\rm lf}^{\rm PC}
\longrightarrow
\mathbf1_{\chi_N}.
}
\]

The codimension-two shift is carried by the ordered conductor orientation
\(h_0\wedge h_3\). The common physical normal line \([dX_{03}]\) is a
separate factor and evaluates with sign \(+1\).

### Tangential and occurrence part

After the forced Laurent diagonal normalization, the marked source is the
cellular V

\[
S_1=R\langle a,c\rangle
\xrightarrow{\ d\ }
S_0=R\langle v_{00},v_{10},v_{01}\rangle,
\]

\[
da=v_{10}-v_{00},
\qquad
dc=v_{01}-v_{00},
\]

and the road object is the ordinary cellular square. Before normalization its
weighted differential is

\[
Q_2=R
\xrightarrow{(x_3,-x_4,-x_0,x_1)^T}
Q_1=R^4
\xrightarrow{d_1}
Q_0=R^4,
\]

with columns

\[
\begin{aligned}
a&=(-x_0,x_1,0,0)^T,\\
b&=(0,0,-x_0,x_1)^T,\\
c&=(-x_3,0,x_4,0)^T,\\
d&=(0,-x_3,0,x_4)^T.
\end{aligned}
\]

On an occurrence-loaded marked vertex \(\widehat v\) and an ordinary road
vertex \(e_{ij}\), the normalized representative is

\[
\boxed{
\Theta_{\rm tan}(\widehat v\otimes e_{ij})
=
(x_i x_j)^{-1}.
}
\]

Equivalently, it is one on every occurrence-normalized product vertex.

The total cellular source has ranks

\[
(12,20,11,2),
\]

and its integral differentials have ranks

\[
(11,9,2).
\]

Explicit integral contractions of the V and the square onto \(v_{00}\)
therefore give

\[
\boxed{
H^k\operatorname{Hom}_{R_{03}}
\bigl(\operatorname{Tot}(S\otimes Q),R_{03}\bigr)
=
\begin{cases}
R_{03},&k=0,\\
0,&k>0.
\end{cases}
}
\]

There is no torsion. The positive value at the common marked occurrence fixes
the unique \(H^0\) generator, so the trace is unique up to chain homotopy.

### Normal part

Put \(u_i=q_i-1\). Twist reversal gives

\[
u_i^\vee
=q_i^{-1}-1
=-q_i^{-1}u_i.
\]

For one normal Koszul factor the complementary-degree pairing is

\[
\boxed{
\beta_i(p_i,h_i^\vee)=1,
\qquad
\beta_i(h_i,p_i^\vee)=-q_i.
}
\]

Indeed, on \(d(h_i\otimes h_i^\vee)\) the two contributions are

\[
u_i
+q_i u_i^\vee
=0.
\]

Tensoring \(\beta_0\) and \(\beta_3\) with the exterior/Koszul sign of
\(h_0\wedge h_3\) gives a perfect two-normal chain pairing. It retains the
independent characters \(u_0,u_3\); no common target character is introduced.

The complete local representative is therefore

\[
\boxed{
\Theta_{1,\partial}^{\rm PC}
=
\Theta_{\rm tan}
\widehat\otimes\beta_0
\widehat\otimes\beta_3
\widehat\otimes
\operatorname{ev}_{[dX_{03}]}.
}
\]

Currying constructs the requested primal-tag trace on the road boundary
costalk:

\[
\boxed{
\operatorname{Tr}_{1,\partial}^{\rm PC}:
\mathcal S_{1,\rm reg}^{\rm mark,\vee}
\longrightarrow
\mathbb D(\mathcal Q_{03,\partial,\rm lf}^{\rm PC})
\otimes\chi_N.
}
\]

It does not identify \(d_1\) with \(d_1^\vee\); it constructs the arrow
between them by Verdier evaluation.

The associated grade is entry 89's Laurent unit pairing. Every primitive
occurrence has value one, each selected sheet has value two, their endpoint
difference is killed, and the four-occurrence polarized road element retains
value four. No division by two or four occurs.

## Evidence

The exact certificate is

`research/voevodsky/check_d03_bivariant_pc_hom.rs`.

SHA-256:

```text
e7328ea87a7581eaa1425653786a728fcb245d26dd73c221325a82c85606f12c
```

It checks:

- both source and road differentials and the total differential square to
  zero;
- the integral contractions, exact ranks, and torsion-free Hom calculation;
- the normalized cocycle and its unique endpoint-normalized homotopy class;
- primitive, sheet, endpoint-difference, and polarized values;
- one- and two-normal twist-reversed chain identities and perfectness;
- ordered exterior/Koszul signs and the independent \([dX_{03}]\) sign;
- strict separation of scalar occurrence and Pochhammer monodromy layers.

Reproduce with:

```powershell
$src = "research/voevodsky/check_d03_bivariant_pc_hom.rs"
$exe = Join-Path $env:TEMP "marici-d03-bivariant-pc-hom.exe"
rustfmt --edition 2021 --check $src
rustc --edition=2021 -D warnings -O $src -o $exe
& $exe | ConvertFrom-Json | Out-Null
```

The standard support/twist typing is the twisted-homology pairing between a
reciprocal-twist ordinary class and an original-twist locally finite class;
see equations (2.3)--(2.6) of
[Mazloumi--Stieberger, *One-loop double copy relation from twisted
(co)homology*](https://arxiv.org/abs/2403.05208). The present theorem is the
explicit local normal-cone/PC representative selected by the scalar marked
span and its endpoint normalization.

Inherited Marici inputs are entries 38, 77, 89, 95, and 96.

## Boundary

- The theorem is finite and nonresonant. The Laurent/nearby-cycle associated
  grade is retained, but no point-set trace at resonance is claimed.
- The source uses the reciprocal local system and the road uses the original
  local system. A same-twist version of the displayed pairing is mistyped.
- The result is exact for \(\mathcal Q_{03,\partial}^{\rm PC}\), the named
  road-face costalk. It does not extend by declaration to the full
  \(\operatorname{PC}(\mathsf J_4\boxtimes\mathsf J_6)\). Extra
  contact/filtered summands there could add Hom classes and must be treated by
  contact recollement or an explicit deformation retract.
- Canonicity is a canonical derived class and a strict representative in the
  facewise normal-cone model. No privileged smooth current or collar is
  selected.
- The local trace lands in the Verdier dual road tag. It does not split the
  augmented triangle, identify \(u_0\) with \(u_3\), or construct the
  relation generator \(\Delta\).
- Physical Cut/Beck--Chevalley naturality beyond this single boundary costalk
  has not been tested.

The sharp negative result is therefore:

\[
\boxed{
\Theta_{1,\partial}^{\rm PC}
\text{ is proved, but }
\Theta_{1,\rm full}^{\rm PC}
\text{ is not typed by the road data alone.}
}
\]

## Consequence

The first local bivariant trace is no longer the frontier. Rotate its formula
through the two remaining marked pairs

\[
(u_2,u_5)\to d_0,
\qquad
(u_0,u_3)\to d_1,
\qquad
(u_1,u_4)\to d_2.
\]

Then construct one relation object \(\mathcal K_{\rm rel}^{\rm PC}\) and test

\[
\boxed{
d\mathcal K_{\rm rel}^{\rm PC}
=
\mathcal T_0^{\rm PC}
+\mathcal T_1^{\rm PC}
+\mathcal T_2^{\rm PC}.
}
\]

The source top map must be the independently derived conductor fold

\[
(f_+,f_-)\longmapsto(+1,-1)\mathcal K_{\rm rel}^{\rm PC},
\]

and its associated grade must reproduce

\[
K_{\rm alt}d_2=\Delta(1,-1).
\]

Failure must be located in the first lower-Cousin, twist, or relation-level
chain equation. Do not test \(\Delta\) on one pair, split the three-road
sequence, or add a relation generator merely to force commutativity.
