# Unsplit Conductor--Road Endpoint Pullback and the Spatial Realization Blocker

## Record

Date: 2026-08-15

Status: exact integral coefficient/carrier theorem and one sharp spatial
blocker. The two-sheet conductor quotient and the orientation-twisted road
augmentation admit a canonical derived endpoint pullback. Its chain complex
is integral, \(D_3\)-equivariant, and has one primitive torsion-free homology
line. It requires neither an equivariant splitting nor division by two or
three.

This corrects a tempting construction after entry 141. Splicing the
conductor one-extension with the entire augmented triangle two-extension
produces an \(\operatorname{Ext}^3\) object. The desired loaded obstruction is
degree two: it combines the conductor one-extension with an endpoint-defect
one-extension. The correct coefficient object is therefore a homotopy
pullback over the common endpoint-orientation quotient, not the five-term
Yoneda splice.

The theorem does not construct the corresponding endpoint object or quotient
maps in the filtered support-PC category. That spatial realization is now
the first missing datum for \(d_{\rm sp,sc}\) and
\(G_{03}^{\rm Cousin}\).

## The two canonical quotient resolutions

Let
\[
P_{\rm sh}=\mathbb Z\langle e_+,e_-\rangle
\]
be the normalization-sheet permutation module. Entry 93 and entry 141 give
the exact conductor sequence
\[
0\longrightarrow \mathbb Z
\xrightarrow{\Delta_{\rm sh}}P_{\rm sh}
\xrightarrow{\operatorname{diff}}\mathbb Z_{\rm or}
\longrightarrow0,
\]
where
\[
\Delta_{\rm sh}(1)=e_++e_-,
\qquad
\operatorname{diff}(a e_++b e_-)=a-b.
\]
Rotations preserve both sheets and physical reflection exchanges them.

The augmented road triangle of entries 94 and 115 is
\[
0\longrightarrow\mathbb Z_{\rm or}
\xrightarrow N P_{\rm tag}
\xrightarrow{1-r}P_{\rm road}
\xrightarrow\epsilon\mathbb Z
\longrightarrow0.
\]
Tensor it by the road-orientation line. Write the result as
\[
0\longrightarrow\mathbb Z
\xrightarrow N P_{\rm tag}^{\rm or}
\xrightarrow{1-r}P_{\rm road}^{\rm or}
\xrightarrow\epsilon\mathbb Z_{\rm or}
\longrightarrow0.
\]
This twist is forced by typing: the road augmentation and the conductor
difference must land in the same endpoint-orientation line before they can be
compared. It is distinct from the once-relative polarity line used after
the pullback.

Thus both exact resolutions have a canonical map to
\(\mathbb Z_{\rm or}\).

## The derived endpoint pullback

The mapping-fibre model of the difference of those two quotient maps is
\[
\boxed{
C_{\partial}^{\rm coeff}:
\quad
C_3\longrightarrow C_2\longrightarrow C_1\longrightarrow C_0
}
\]
with
\[
\begin{aligned}
C_3&=\mathbb Z,\\
C_2&=\mathbb Z\oplus P_{\rm tag}^{\rm or},\\
C_1&=P_{\rm sh}\oplus P_{\rm road}^{\rm or},\\
C_0&=\mathbb Z_{\rm or},
\end{aligned}
\]
and
\[
\begin{aligned}
d_3(c)&=(0,Nc),\\
d_2(a,t)&=(\Delta_{\rm sh}a,(1-r)t),\\
d_1(s,q)&=\operatorname{diff}(s)-\epsilon(q).
\end{aligned}
\]
The two identities
\[
(1-r)N=0,
\qquad
\operatorname{diff}\Delta_{\rm sh}
=\epsilon(1-r)=0
\]
give
\[
d_2d_3=0,
\qquad
d_1d_2=0.
\]

With the physical road basis and the corresponding twisted tag basis, every
differential commutes with rotation and reflection. Hence
\(C_{\partial}^{\rm coeff}\) is a strict integral \(D_3\)-complex. It is the
coefficient/carrier skeleton of a derived endpoint correspondence; it is not
an invertible transition between sheet and road objects.

## Exact integral homology

The chain ranks are
\[
( \operatorname{rk}C_3,\operatorname{rk}C_2,
   \operatorname{rk}C_1,\operatorname{rk}C_0 )
=(1,4,5,1),
\]
and the differential ranks are
\[
(1,3,1).
\]

The certificate proves saturation with explicit determinant-one bases, not
only by ranks over a field.

In degree two, the basis
\[
(\Delta_{\rm sh},N,d_0,d_1)
\]
has determinant \(+1\); its image is respectively
\[
(\Delta_{\rm sh},0,m_0,m_1).
\]
Thus the only kernel generator is the norm \(N\), already the image of
\(d_3\).

In degree one, the columns
\[
(\Delta_{\rm sh},m_0,m_1,z,w)
\]
form a determinant-one basis, where
\[
z=(e_+,q_0),\qquad d_1z=0,
\]
and \(w\) maps to the primitive generator of \(C_0\). The first three
columns are exactly the saturated image of \(d_2\), while the first four are
exactly \(\ker d_1\). Consequently
\[
\boxed{
H_1(C_{\partial}^{\rm coeff})\simeq\mathbb Z_{\rm or},
\qquad
H_i(C_{\partial}^{\rm coeff})=0\quad(i\ne1),
}
\]
with no torsion.

The quotient functional can be taken as
\[
\phi(s;q_0,q_1,q_2)=q_0+q_1+q_2.
\]
It sends \(z\) to one. Rotation fixes its class and reflection negates it.
After tensoring the once-relative polarity line,
\[
\mathbb Z_{\rm or}\otimes L_{\rm pol}\simeq\mathbb Z,
\]
so the physical primitive line is trivial, exactly as required by the
associated-grade normalization of entry 94.

## Why strictification asks for fractions

The complex has a primitive quotient but no strict integral
\(D_3\)-equivariant cycle section of that quotient. If
\[
\sigma(1)=(a,b;c,c,c)
\]
were such a section, rotation invariance would force equal road
coefficients, and \(\phi\sigma=1\) would give
\[
3c=1.
\]
Reflection oddness gives \(b=-a\), while the cycle equation gives
\[
2a=3c=1.
\]
Thus a strict representative would require both \(1/3\) and \(1/2\).

The certificate records the same obstruction without a bounded search: the
complete integral section system is inconsistent modulo three and modulo
two. This is not an obstruction to the derived object. It is the precise
cost of replacing a canonical quotient/correspondence by a chosen invariant
summand.

## Degree audit and simplification

One can compose the conductor difference with the road norm and write the
exact sequence
\[
0\to\mathbb Z\to P_{\rm sh}\to
P_{\rm tag}\to P_{\rm road}\to\mathbb Z\to0.
\]
That sequence is mathematically legitimate, but it represents
\[
e_{\rm pol}\circ\beta_\triangle
\in\operatorname{Ext}^3,
\]
because it splices a one-extension with a two-extension.

The loaded obstruction sought after entry 141 has the form
\[
e_{\rm pol}\circ p_{\partial,Q}
\in\operatorname{Ext}^2.
\]
Therefore the five-term splice is the wrong degree and contains one stage too
many. The derived endpoint pullback above is the degree-correct unsplit
object. It retains both resolutions and compares only their common endpoint
quotient.

This changes the economical strategy:

1. do not split the primitive road quotient;
2. do not choose the residual reflection parity first;
3. do not splice the conductor onto the full Tate class;
4. construct the common endpoint-orientation object and its two quotient
   maps geometrically;
5. form their derived pullback in the filtered support-PC category;
6. only then read the endpoint defect parity as an obstruction to spatial
   realization or pointing.

Entry 141's Bockstein remains valid. The present theorem identifies the
integral coefficient object on which its still-missing geometric input must
live.

## Sharp blocker

No established entry constructs one ringed, filtered extraordinary endpoint
object
\[
\mathcal E_{\partial,Q}^{!,{\rm PC}}
\]
together with both maps
\[
\mathcal S_{\rm sh}^{\rm norm}
\longrightarrow\mathcal E_{\partial,Q}^{!,{\rm PC}}
\longleftarrow
\mathcal Q_{\rm road}^{\rm or}
\]
whose coefficient shadows are respectively
\(\operatorname{diff}\) and \(\epsilon\).

Such a construction must retain, simultaneously:

- the two normalization sheets and their conductor difference;
- the based nonzero \(Q\)-leg and both endpoint connector cells;
- the complete unsplit \(N/(1-r)/\epsilon\) road resolution;
- occurrence and independent multi-Rees filtrations;
- reciprocal-regular versus Borel--Moore variance;
- the physical normal and once-relative polarity lines.

Without these two spatial quotient maps, the derived pullback is only a
coefficient/carrier theorem. It cannot be promoted to
\(\mathcal S_F^{\rm sp}\), and no
\[
d_{\rm sp,sc}
\quad\text{or}\quad
G_{03}^{\rm Cousin}
\]
is inferred. In particular, the theorem does not decide
\(p_{\partial,Q}\), full PC Cut naturality, or the global half-object.

## Next experiment

Construct the \(D=03\) endpoint-orientation costalk
\(\mathcal E_{\partial,Q}^{!,{\rm PC}}\) independently of
\(K_{\rm alt}\), \(q_\Sigma\), the desired residue, and the desired parity.
Then:

1. construct the sheet and road quotient maps into it;
2. form their derived pullback;
3. verify that forgetting endpoint/support framing contracts the result as
   in entry 133;
4. only afterward test
   \[
   \operatorname{gr}_{\mathfrak c}^1
   =K_{\rm alt}\otimes L_{\rm pol},
   \qquad
   \operatorname{gr}_Q=+[q_\Sigma],
   \qquad
   \operatorname{Res}_{x_3}
   =\operatorname{pur}_{x_3,\partial}^{\rm PC};
   \]
5. read the reflection parity and apply entry 141's proved Bockstein.

A zero spatial pullback falsifies the local synthesis. A primitive rank-one
pullback gives the unique realization up to orientation. Extra rank or
torsion signals missing coherence.

## Evidence

Exact certificate:

- research/voevodsky/check_conductor_road_endpoint_pullback.rs
- SHA-256
  78c6af824451f46375455ec1eb6bf0b7a1c8c302548a1ffcd593c3f7ee13b84a

It verifies \(d^2=0\), all \(D_3\) actions and covariance equations, explicit
unimodular saturation bases, the primitive orientation character, the exact
mod-two/mod-three strict-section obstruction, and the Ext-degree audit.

Verification:

~~~text
rustfmt --edition 2021 --check: pass
rustc --edition=2021 -D warnings -O: pass
executable assertions: pass
JSON output parse: pass, status=proved
~~~

Dependencies:

- entry 93: normalization--conductor square and the sheet quotient;
- entry 94: the self-dual augmented triangle and primitive symbol;
- entry 115: the geometric \(N/(1-r)/\epsilon\) road resolution;
- entry 133: ordinary-derived contraction ablation;
- entries 136--141: canonical roof, endpoint pointing, reflection, and
  conductor Bockstein reductions.

Epistemic-graph admission is pending MCP availability. The theorem and
blocker are also attached to task-lifecycle cross-audit task #2515; that task
was still awaiting a worker executability assessment at publication time.

## Outcome contract

~~~json
{
  "claim": "The two-sheet conductor quotient and the orientation-twisted road augmentation have a canonical integral D3-equivariant derived endpoint-pullback skeleton. Its only homology is one primitive torsion-free orientation line, which becomes trivial after the once-relative polarity twist. No transition, splitting, or division by 2 or 3 is required.",
  "status": "proved",
  "assumptions": [
    "The conductor sequence is 0 -> Z -> P_sh -> Z_or -> 0 with physical reflection exchanging the sheets.",
    "The exact augmented road triangle is tensor-twisted by the road-orientation line before its augmentation is compared with the conductor difference.",
    "The theorem is scoped to the coefficient/carrier skeleton and does not assert its filtered support-PC realization."
  ],
  "factorization_test": {
    "chain_ranks": [1, 4, 5, 1],
    "differential_ranks": [1, 3, 1],
    "d_squared": "zero",
    "D3_covariance": "strict in every degree",
    "integral_homology": "H1=Z_or and all other groups zero; determinant-one saturation bases; no torsion",
    "once_polarity_loaded_homology": "Z_triv",
    "strict_integral_section": "absent; exact systems are inconsistent mod 2 and mod 3",
    "naive_full_triangle_splice": "wrong degree: Ext1 composed with Ext2 is Ext3"
  },
  "counterevidence": [
    "The module complex does not construct the geometric endpoint/Q quotient or extraordinary support variance.",
    "It does not determine the endpoint-defect parity or select a pointed butterfly.",
    "No occurrence, multi-Rees, reciprocal/BM, PC/Cousin, or physical-Cut map follows from coefficient exactness."
  ],
  "sharp_blocker": "Construct one filtered support-PC endpoint-orientation object and lift both the sheet difference and orientation-twisted road augmentation to it. Only then form the spatial derived pullback and test the established conductor, Q, and edge-purity outputs.",
  "next_experiment": "Construct the D03 endpoint-orientation extraordinary costalk independently of the desired outputs, form the two-map derived pullback, perform the mandatory forgetting ablation, and only then compute rank, torsion, boundary values, and reflection parity."
}
~~~
