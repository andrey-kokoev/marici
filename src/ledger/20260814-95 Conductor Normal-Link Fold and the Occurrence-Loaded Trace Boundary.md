# Conductor Normal-Link Fold and the Occurrence-Loaded Trace Boundary

## Record

Date: 2026-08-14

Status: proved integral carrier theorem at the first conductor normal-link
grade; the strict common-rank-one PC lift is falsified, while the intended
noninvertible Gysin lift remains open.

Scope: the factorization-marked six-point normalization--conductor geometry
of entries 93--94, with its positive normal cones and declared normal
orientations. This result is governed by `docs/nima-research-objective.md`
and `docs/research-lifecycle.md`.

The source differential previously described as absent is canonical at this
specific grade. It is the dual cellular/Cousin differential of the two
positive projectivized conductor normal cones. The first unresolved arrow is
therefore no longer an unspecified "scalar differential". It is the
occurrence-loaded coefficient/Gysin trace which must lift this carrier fold
to the full PC complexes.

## Claim

On the two normalization branches of entry 93, the conductor ideals are

\[
J_+=(x_1,x_3,x_5),
\qquad
J_-=(x_0,x_2,x_4).
\]

Their positive projectivized normal cones are canonically marked triangles

\[
L_+=\mathbb P_+(N_{Z/F_+})\simeq\Delta^2,
\qquad
L_-=\mathbb P_+(N_{Z/F_-})\simeq\Delta^2.
\]

These are normal-link vertex figures, not faces of the ordinary hexagon
associahedron. Let \(f_+,f_-\) be their oriented dual top cells and let
\(e_0,\ldots,e_5\) be the six sheet-resolved edge generators. The geometric
top differential is

\[
d_2(f_+)=e_1+e_3+e_5,
\qquad
d_2(f_-)=e_0+e_2+e_4.
\]

It is derived from the two coordinate normal cones before using
\(K_{\rm alt}\). With the independently scalar-derived QTDS incidence

\[
d_1=C_{\rm QTDS}
=
\begin{pmatrix}
1&1&0&-1&-1&0\\
0&-1&-1&0&1&1\\
-1&0&1&1&0&-1
\end{pmatrix}
\]

and road augmentation \(d_0=\epsilon=(1,1,1)\), this gives the augmented
normal-link carrier

\[
C_{\rm link}:
\mathbb Z^2\xrightarrow{d_2}\mathbb Z^6
\xrightarrow{C_{\rm QTDS}}P_{\rm road}
\xrightarrow{\epsilon}\mathbf1.
\]

It satisfies \(d^2=0\) integrally. There is a degreewise-surjective chain
map to the entry-94 augmented triangle resolution

\[
C_\triangle:
\mathbf1_{\rm or}\xrightarrow{\Delta}P_{\rm tag}
\xrightarrow{\partial_\triangle}P_{\rm road}
\xrightarrow{\epsilon}\mathbf1
\]

given by

\[
G_2=(1,-1),
\qquad
G_1=K_{\rm alt},
\qquad
G_0=\operatorname{id},
\qquad
G_{-1}=\operatorname{id}.
\]

The two nontrivial chain identities are

\[
K_{\rm alt}d_2=\Delta(1,-1),
\qquad
\partial_\triangle K_{\rm alt}=C_{\rm QTDS}.
\]

The integral kernel is

\[
\ker G_2=\mathbb Z\langle f_++f_-\rangle,
\]

\[
\ker G_1
=
\mathbb Z\langle
e_0+e_3,
e_1+e_4,
e_2+e_5
\rangle,
\]

with differential \(1\mapsto(1,1,1)\). Hence

\[
0\longrightarrow
[\mathbb Z\xrightarrow{\Delta}\mathbb Z^3]
\longrightarrow C_{\rm link}
\xrightarrow{G}C_\triangle
\longrightarrow0
\]

is a short exact sequence of integral complexes, and

\[
H_1(\ker G)
=
\mathbb Z^3/\mathbb Z(1,1,1)
\simeq A_2
\]

canonically through \(\partial_\triangle\). There is no torsion and no
division by two or three.

One-step cyclic transport acts positively on roads and tags, by
\(e_j\mapsto-e_{j+1}\) on polarity-loaded source edges, and by the signed
sheet swap

\[
f_+\mapsto-f_-,
\qquad
f_-\mapsto-f_+.
\]

The target relation generator is invariant. All chain and fold squares commute
for all six powers. Assigning a minus sign to the target top generator is
incompatible with both \(\Delta\) and \(G_2\).

## Evidence

The exact certificate is

`research/voevodsky/check_conductor_normal_link_fold.rs`.

It checks:

- construction of \(d_2\) from the two normal-coordinate triples without
  reading \(K_{\rm alt}\);
- both square-zero identities and all three fold squares;
- saturated integral kernels and degreewise right inverses;
- Smith factors and the torsion-free homology calculation;
- the canonical identification \(H_1(\ker G)\simeq A_2\);
- all six cyclic powers and the forced target-top sign.

Reproduce with:

```powershell
$src = "research/voevodsky/check_conductor_normal_link_fold.rs"
$exe = Join-Path $env:TEMP "marici-conductor-normal-link-fold.exe"
rustfmt --edition 2021 --check $src
rustc --edition=2021 -D warnings -O $src -o $exe
& $exe
```

Certificate SHA-256:

```text
61ebadf9eb8e106c69833c912ec6667dd929547f86550d17ae440906a11f8718
```

The sharp coefficient negative control is

`research/voevodsky/check_occurrence_pc_trace_obstruction.rs`.

Reproduce with:

```powershell
$src = "research/voevodsky/check_occurrence_pc_trace_obstruction.rs"
$exe = Join-Path $env:TEMP "marici-occurrence-pc-trace-obstruction.exe"
rustfmt --edition 2021 --check $src
rustc --edition=2021 -D warnings -O $src -o $exe
& $exe
```

Certificate SHA-256:

```text
3e4dee2b54dcaeb6147d3d7cf9c431fd676ec71d0dd2902b1fb5065db157e6da
```

Inherited inputs are entries 20, 38, 66, 86, 93, and 94 and their cited
certificates. In particular, entry 20 supplies \(C_{\rm QTDS}\), entry 93
supplies the two regular conductor embeddings, entry 38 supplies the
nonresonant normal-cone/Cousin framework, and entry 86 supplies the marked
physical endpoint counit.

## Boundary

This theorem is a carrier and first-associated-grade statement. It does not
yet construct the full scalar total-specialization differential
\(d_{\rm sp,sc}\), nor the filtered map
\(G_{03}^{\rm Cousin}\) required by the current formula objective.

In particular:

- \(L_\pm\) are positive projectivized normal cones/vertex figures. No literal
  triangle is asserted to be an associahedral face, and entry 84's warning
  about a global barycentric representative and its factor \(1/2\) remains
  intact.
- The certificate retains the integral carrier but not the actual
  \(y_i\)-weights, occurrence modules, Koba--Nielsen monodromies, or forced
  lower Cousin terms.
- Entry 86 fixes the boundary values on the marked road occurrences. It does
  not by itself define the image of the target relation generator or a trace
  between the two branchwise loaded edge systems.
- No "scalar BRST" differential is introduced. Gauge BRST remains downstream
  in Yang--Mills descent.
- The fold is a quotient of complexes, not an equivariant splitting or a
  transition automorphism.

The first sharp missing map is the occurrence-loaded trace

\[
\operatorname{Tr}_{\rm occ}^{\rm PC}:
\operatorname{PC}(L_+;\mathcal L_+)
\underset{P_{\rm road}}{\sqcup^{\mathbb L}}
\operatorname{PC}(L_-;\mathcal L_-)
\longrightarrow
\mathcal R_{03}^{\rm circ,PC}
\]

whose carrier grade is \(G\). It must simultaneously:

1. include every normal and lower Cousin term;
2. send the relation-level source to the \(\Delta\) generator;
3. restrict to entry 86's four unit \(D=03\) road occurrences;
4. intertwine the PC differentials; and
5. obey the physical-Cut/Beck--Chevalley square.

The established data prove neither existence nor nonexistence of this trace.
They do, however, falsify its strongest strict replacement. Put

\[
R_u=\mathbb Z[u_0,\ldots,u_5],
\qquad
K(u_j)=[R_u\xrightarrow{u_j}R_u],
\qquad
u_j=q_j-1.
\]

The three tag pairs selected by \(K_{\rm alt}\) are

\[
(u_2,u_5),
\qquad
(u_0,u_3),
\qquad
(u_1,u_4).
\]

Suppose a pair folded strictly over the identity universal-monodromy base to
one supported rank-one target \(K(v_i)\), with the unit coefficients forced
by the carrier fold. The two chain equations require

\[
v_i\mid u_j,
\qquad
v_i\mid u_{j+3}.
\]

The paired universal monodromy variables are independent, so their greatest
common divisor is one. Hence \(v_i\) must be a unit and the target loses its
boundary support. Therefore

\[
\boxed{
\text{no strict supported common rank-one target exists over }R_u.
}
\]

Nonresonant localization can manufacture maps by ratios, but it erases this
support and does not canonically choose a target character. This negative
control does not rule out the desired Gysin span: its two legs may pull one
coefficient object back to distinct source characters.

The occurrence calculation locates the missing coherence. In the normalized
\(D=03\) road square, write the four corners as

\[
(v_{00},v_{10},v_{01},v_{11}).
\]

Entry 86 gives the two selected-edge supports

\[
p_+=v_{00}+v_{10},
\qquad
p_-=v_{00}+v_{01}.
\]

Their difference \(v_{10}-v_{01}\) has two exact lower-Cousin primitives,
one through \(v_{00}\) and one through \(v_{11}\). Their difference is
exactly the boundary of the road-square top cell. Thus the endpoint periods
fix the derived null class, but they do not select the strict lower-Cousin
primitive or the top coherence realizing \(\Delta\).

A nonzero occurrence-relative class of the forced \(\Delta\)-boundary would
be a stronger canonical falsifier. Defining the target coefficient system so
that the trace exists tautologically would not be a solution.

## Consequence

The blocker in entries 93--94 is narrowed by one full categorical level:

\[
\text{normal-link carrier differential}
\quad\text{is now canonical,}
\]

while

\[
\text{occurrence-loaded PC trace and its Beck--Chevalley naturality}
\quad\text{remain open.}
\]

Thus the integral augmented triangle is not merely an algebraic pattern. It
is a quotient of an independently constructed scalar conductor normal-link
complex, and its kernel is exactly the QTDS contact \(A_2\) sector.

The next discriminating experiment is the single paired correspondence

\[
Z_0\longleftarrow W_{03}\longrightarrow Z_3.
\]

Construct it in the factorization-marked scalar geometry, specify both
pullbacks on universal normal tori and occurrence cosheaves, and compute its
PC trace on the two road-square Cousin primitives. Geometry must select the
lower-Cousin representative and send their top-cell difference to the
\(\Delta\) relation. Only after this \(D=03\) square commutes should it be
rotated or the primitive Cut square be promoted to a full chain-level
theorem.
