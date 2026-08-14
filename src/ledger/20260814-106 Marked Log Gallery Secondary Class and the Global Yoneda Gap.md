# Marked Log Gallery Secondary Class and the Global Yoneda Gap

## Record

Date: 2026-08-14

Status: proved for the actual loaded gallery, its filtered secondary class,
the middle log expansion, and the fixed-beta Cartier physical-normal
evaluation. The ordinary degree-zero correspondence is falsified. The full
Beck--Chevalley comparison with the global Yoneda class remains unproved.

## The actual marked gallery

Write

\[
a=\{x_1,x_3,x_5\},\qquad
b=\{D03,x_1,x_3\},\qquad
c=\{D03,x_0,x_3\}.
\]

There is a unique factorization-marked two-edge gallery

\[
\mathcal G_{+;03}:a\xrightarrow{e_c}b\xrightarrow{e_r}c,
\]

where

\[
e_c=\{x_1,x_3\},\qquad e_r=\{D03,x_3\}.
\]

It is an actual strict subcomplex of the 215-generator absolute loaded
oriented-boundary-blowup complex of entry 105. It has 32 generators, with
degree ranks

\[
(3,11,13,5),
\]

and the inherited differential squares to zero on every generator.

The occurrence boundary is forced by the scalar face incidence:

\[
d e_c=X_{03}b-x_5a,
\qquad
d e_r=x_0c-x_1b.
\]

Consequently

\[
\boxed{
\xi_{+;03}=x_1e_c+X_{03}e_r
}
\]

is the unique primitive middle-cancelling relative chain, and

\[
\boxed{
d\xi_{+;03}=X_{03}x_0c-x_1x_5a.
}
\]

The independently established reciprocal occurrence cocycle gives unit
values at both endpoints and kills both weighted edge boundaries. No endpoint
normalization is inserted into this construction.

## The filtered secondary class

Factor out the normal packet \(K(u_3)\), which is common to the entire
gallery, and pass relative to the endpoint fibres \(a,c\). In the degree-one
basis

\[
(b_U,b_1,e_c,e_r)
\]

and the degree-two basis

\[
(b_{U1},e_{c,h_1},e_{r,h_U}),
\]

the actual loaded differential is

\[
d_1=(U_{03},u_1,X_{03},-x_1)
\]

and

\[
d_2=
\begin{pmatrix}
-u_1&0&-x_1\\
U_{03}&X_{03}&0\\
0&-u_1&0\\
0&0&-U_{03}
\end{pmatrix}.
\]

These matrices are derived by restriction of entry 105's absolute
radial-plus-normal differential. They obey \(d_1d_2=0\), and \(d_2\) is
injective. The gallery chain is

\[
\xi_{+;03}=(0,0,x_1,X_{03}),
\qquad d_1\xi_{+;03}=0,
\]

and satisfies the forced relation

\[
\boxed{
d_2(X_{03}x_1,-U_{03}x_1,-u_1X_{03})
=u_1U_{03}\,\xi_{+;03}.
}
\]

Conversely, the first and last coordinates show that a scalar annihilating
\([\xi_{+;03}]\) must be divisible by both \(u_1\) and \(U_{03}\). Thus the
displayed quadratic coefficient is exact, rather than selected from the
desired answer.

This is the crucial retyping:

> The marked gallery produces a canonical filtered linking or secondary
> class. It does not produce a nonzero ordinary degree-zero morphism.

Indeed every ordinary coefficient-valued dual cocycle is proportional to

\[
(U_{03},u_1,X_{03},-x_1)
\]

and therefore evaluates to zero on \(\xi_{+;03}\). The independent global
ordinary mapping-complex calculation likewise has \(H^0=0\). The required
nonzero datum lies one derived/filtered step higher; relabelling its
obstruction module as an ordinary morphism would be false.

The same absolute differential contains a canonical closed extension kernel
before endpoint quotienting. Let \(\ell_5^a\) and \(\ell_0^c\) be the two
endpoint-exclusive normal-circle generators. The maximal-minor syzygy of the
actual three-vertex boundary matrix is

\[
\boxed{
\begin{aligned}
\kappa_{+;03}={}&u_5u_0(x_1e_c+X_{03}e_r)
+x_1x_5u_0\,\ell_5^a\\
&-X_{03}x_0u_5\,\ell_0^c .
\end{aligned}
}
\]

It obeys

\[
d\kappa_{+;03}=0,
\]

generates the corresponding polynomial kernel freely, is primitive, and is
not a boundary in the full loaded gallery. Thus the gallery supplies an
actual canonical extension kernel while its ordinary source-to-road
degree-zero shadow remains zero. These statements are compatible: the
kernel is a filtered/correspondence object, not an ordinary map between the
two endpoint costalks.

## Geometric origin: the middle log expansion

The failure of the central edge alone is also exact. Its two endpoint
supports have zero derived fibre product, and a simultaneous endpoint DNC
has empty unlocalized special fibre. A one-parameter identification forces
the Rees parameter to be invertible.

The full path has additional geometry. Both marked edges are adjacent edges
of the actual short-diagonal pentagon \(F_{x_3}\), meeting transversely at
\(b\). Blowing up the actual middle ideal

\[
(D03,x_1)\subset F_{x_3}
\]

inserts the canonical positive exceptional interval

\[
\mathbb P(L_{D03}\oplus L_1).
\]

This logarithmic expansion gives the expanded path a relative dualizing
class without inverting its Rees parameter. Its character is forced:

\[
q_{\rm exc}=q_{03}q_1,
\qquad
u_{\rm exc}=U_{03}+u_1+U_{03}u_1.
\]

The first associated grade is the exceptional ray \(U_{03}+u_1\). The
quadratic correction is exactly \(U_{03}u_1\), matching the coefficient in
the secondary gallery relation. The first column of \(d_2\) is the Koszul
syzygy \((-u_1,U_{03})\), while its other columns attach that excess line to
the two incidence directions \(X_{03},-x_1\).

This match is strong necessary compatibility evidence. It is not, by
itself, a proof of the global pull--push square.

After the completed Koba--Nielsen base change, write

\[
U_{03}=wX_{03},\qquad w=\beta v(X_{03})\in R^\times.
\]

The relative loaded complex then acquires the forced cycle

\[
\boxed{
\zeta_{03}=(1,0,-w,0),
}
\]

because \(d_1\zeta_{03}=U_{03}-wX_{03}=0\). It satisfies

\[
u_1\zeta_{03}=-c_1+wc_2,
\qquad
x_1\zeta_{03}+w\xi_{+;03}=-c_3,
\]

where \(c_i\) are the three columns of \(d_2\). Hence the physical
full-path summand is the canonical \(u_1\)-supported line generated by
\(\zeta_{03}\), and the occurrence gallery chain is its forced multiple.
This is the chain-level can--var realization of the Cartier comparison; no
unit is selected from the desired residue.

The complete unlocalized relative \(H_1\) also contains the independent
second-edge class

\[
\tau=(0,x_1,0,u_1),
\]

which is killed by \(X_{03}\). Therefore the \(\zeta_{03}\)-line is the
saturated marked full-path summand relevant to the physical comparison, not
the whole unlocalized relative homology.

## Physical normal evaluation

The local long-normal evaluation no longer remains ambiguous. In the
fixed-nonzero-\(\beta\), characteristic-zero completion already used by
entry 105,

\[
U_{03}=e^{\beta X_{03}}-1
=\beta X_{03}v(X_{03}),
\qquad v(0)=1.
\]

Therefore \((U_{03})=(X_{03})\) as Cartier ideals and

\[
d\log U_{03}=d\log X_{03}+d\log v.
\]

The last term is regular. Cartier logarithmic purity consequently gives

\[
\operatorname{Res}_{U_{03}=0}\frac{dU_{03}}{U_{03}}
=
\operatorname{Res}_{X_{03}=0}\frac{dX_{03}}{X_{03}}
=1
\]

with the positive ordered normal orientation. Composing this with entry
100's independently constructed short-normal excess/Cech trace closes the
local coefficient formula

\[
\boxed{
\eta_{3,\rm mix}
\longmapsto
\left[\frac1{u_0u_1u_3u_5}\right]
\otimes[dX_{03}].
}
\]

No normal, occurrence coefficient, integer, or Rees parameter is globally
inverted. The Cartier comparison is not claimed over the universal integral
monodromy base; its fixed-\(\beta\) completed scope is essential.

## First remaining canonical failure

Every face of \(\mathcal G_{+;03}\) contains a short diagonal. Hence

\[
\mathcal G_{+;03}\subset F_1
\]

and its image in

\[
Q=F_2/F_1
\]

is zero. But the global class

\[
e_F\in\operatorname{Ext}^2(Q,F_0)
\]

essentially involves the long-road quotient \(Q\). The gallery subcomplex
contains no \(Q\)-generator, no representative of the global two-extension,
and no pull--push homotopy identifying its local secondary class with the
restriction of \(e_F\).

Therefore the strict ordinary formula for \(G_{03}^{\rm Cousin}\) must be
replaced by a filtered cohomological correspondence, but that correspondence
is not yet globally constructed. The exact next arrow is a filtered
chain/sheaf map, or a specified homotopy, from the global extension diagram
through the log-expanded gallery such that

\[
\operatorname{BC}_{+;03}(\Gamma_{+;03}^{\rm log},e_F)
=\Theta_{03}^{\rm loc}
\]

on the mixed excess class. Its associated-grade component must be
\([\xi_{+;03}]\), and its physical normal component is now fixed by Cartier
purity.

## Evidence

Exact certificates:

- `research/voevodsky/check_d03_central_flip_derived_hom.rs`
- `research/voevodsky/check_d03_central_flip_dnc_obstruction.rs`

with SHA-256 values

```text
4f491ca5100279c406a8699e21d6d4fea9bbba93e670000d7f81e931829e7e64
ddd1f49ea6a1a539438e214b5943055e849280bb7fda871d025e595bda18091d
```

They verify the full loaded gallery, every differential, the relative
matrices, maximal-minor kernel, secondary relation, completed-graph cycle,
the ordinary \(H^0\) no-go, the actual pentagon incidence, the log blowup
character, the central-edge DNC negative control, occurrence endpoints, and
the fixed-beta Cartier residue.

The primary audit also reran the decisive entry 100 and entry 105
certificates and the repository checks.

## Consequence

The research frontier has moved one categorical degree:

\[
\text{ordinary restriction/map}
\quad\text{(canonically zero)}
\]

is replaced by

\[
\boxed{
\text{log-expanded filtered linking class}
\quad\text{(canonical and nontrivial).}
}
\]

The remaining problem is no longer the local normal coefficient, occurrence
normalization, or physical residue. It is global functoriality: prove that
the log-expanded local \(k\)-invariant is the Beck--Chevalley pullback of the
absolute support filtration's Yoneda class.

## Outcome contract

```json
{
  "claim": "The actual D03 marked two-edge gallery is a strict loaded scalar subcomplex carrying a canonical filtered secondary class, and its middle logarithmic expansion plus fixed-beta Cartier purity canonically reproduces the local physical-normal coefficient. The class is not a nonzero ordinary morphism.",
  "status": "conditional",
  "assumptions": [
    "The absolute scalar object is the entry-105 original-twist/Borel--Moore oriented-boundary-blowup complex with its strict support filtration.",
    "The middle expansion is the actual log blowup Proj Rees(D03,x1) inside the x3 pentagon.",
    "The physical-normal comparison is scoped to the fixed-nonzero-beta characteristic-zero Koba--Nielsen completion already used for local purity.",
    "No t, normal parameter, occurrence coefficient, or integer is inverted."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_central_flip_derived_hom.rs",
    "research/voevodsky/check_d03_central_flip_dnc_obstruction.rs",
    "ledger entries 100, 103, 104, and 105"
  ],
  "factorization_test": {
    "strict_loaded_gallery": "passed",
    "weighted_relative_chain": "passed",
    "filtered_secondary_relation": "passed",
    "primitive_extension_kernel": "passed",
    "completed_graph_zeta_line": "passed, with the separate tau summand retained",
    "ordinary_H0_correspondence": "falsified; uniquely zero",
    "middle_log_expansion": "passed",
    "physical_Cartier_trace": "passed in fixed-beta completed scope",
    "global_Beck_Chevalley_with_e_F": "unconstructed"
  },
  "counterevidence": [
    "The central edge alone has empty derived endpoint intersection.",
    "The entire marked gallery lies in F1 and has zero image in Q=F2/F1.",
    "Matching the quadratic associated-grade correction does not itself construct a six-functor pull--push comparison with e_F.",
    "The Cartier comparison is not a universal integral monodromy theorem."
  ],
  "next_experiment": "Construct a filtered pull--push map or explicit homotopy from the global Yoneda extension through the log-expanded gallery and test that its k-invariant restricts to the proved secondary class and its Beck--Chevalley evaluation is the entry-100 trace."
}
```
