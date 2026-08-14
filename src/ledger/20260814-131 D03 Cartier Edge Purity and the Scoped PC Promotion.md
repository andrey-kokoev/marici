# D03 Cartier Edge Purity and the Scoped PC Promotion

## Record

Date: 2026-08-14

Status: proved in the definitionally scoped absolute/unlocalized D03
road-face model. The coefficient/Cousin source left unnamed in entry 130 has
an independent construction, finite Cartier purity identifies it with the
actual edge costalk, and the Bockstein-compatible normalized identification
is unique.

Scope: the \(x_3\) normal of the entry-105 absolute support complex, with the
entry-100 reciprocal-standard/original-Borel--Moore pairing and the
entry-129 occurrence Cartier map frozen. This does not construct the scalar
specialization differential, \(G_{03}^{\rm Cousin}\), a nonzero generic
\(Q\)-leg, or an unrestricted enlargement of the road-face PC complex.

## The actual target packet

Factor out the common physical line and all normal packets unrelated to
\(x_3\). The closed-star quotient of entry 105 is

\[
P_3=
\left[
A\langle g_3,h_3\rangle
\xrightarrow{(x_3,u_3)}
A\langle p_3\rangle
\right].
\]

Here \(g_3\) is radial/occurrence and \(h_3\) is the original normal-circle
generator. No occurrence or monodromy variable is inverted. Its complete
primitive syzygy is forced:

\[
z_3=u_3g_3-x_3h_3.
\]

Let \(B=A/(x_3)\). Since \(x_3\) is Cartier and \(P_3\) is perfect,

\[
\boxed{
i_{x_3}^{!}P_3
=R\!\operatorname{Hom}_A(B,P_3)
\simeq
\left(B\otimes_A P_3\right)
\otimes\operatorname{or}(x_3)[-1].
}
\]

Thus, up to the displayed coorientation shift, the target costalk is

\[
E_{3,\rm tar}=
\left[
B\langle g_3,h_3\rangle
\xrightarrow{(0,u_3)}
B\langle p_3\rangle
\right].
\]

It contains one free radial line and one \(B/(u_3)\) normal line. There is no
integer torsion. In particular, rank one is not automatic.

## Independent construction of the source

The same packet is obtained without copying the target:

1. entry 129 supplies the \(x_3\)-Cartier Thom line
   \(B\langle g_3\rangle[1]\);
2. entry 100 supplies the original/Borel--Moore can--var packet
   \(K_B(u_3)=[B\langle h_3\rangle\xrightarrow{u_3}
   B\langle p_3\rangle]\);
3. their support-typed direct sum is

\[
E_{3,\rm src}
=
B\langle g_3\rangle[1]\oplus K_B(u_3)
=
\left[
B\langle g_3,h_3\rangle
\xrightarrow{(0,u_3)}
B\langle p_3\rangle
\right].
\]

The reciprocal-regular factor is not discarded. The strict filtered
quotient/excess decomposition of \(K(u_3^\vee)\otimes P_3\), followed by
entry 97's perfect reciprocal/original pairing, curries the bivariant packet
to \(E_{3,\rm src}\). The Laurent unit in

\[
u_3^\vee=-q_3^{-1}u_3
\]

is absorbed by that pairing; it does not identify the two support variances.

This is the missing definition of entry 130's
\(\mathcal C_{x_3\text{-edge}}^{\rm coeff/Cousin}\). It is derived from the
occurrence Thom and can--var data, not from the desired endpoint fractions.

## The graph Bockstein selects one map

On the derived graph

\[
u_3=t_3x_3,
\]

the first Cartier Bockstein is forced:

\[
\beta_{x_3}(g_3)=p_3,
\qquad
\beta_{x_3}(h_3)=t_3p_3.
\]

Its primitive kernel is

\[
t_3g_3-h_3=z_3/x_3.
\]

Before Bockstein compatibility, a filtration- and support-preserving
degree-zero chain endomorphism of the edge packet has

\[
f_1=
\begin{pmatrix}
a&b\\
0&e
\end{pmatrix},
\qquad
f_0(p_3)=ep_3.
\]

The ambient homotopy classes contain one free scalar and two
\(B/(u_3)\)-ambiguities. Hence rank one is not inherited from interval
contractibility.

The equation

\[
\beta_{x_3}f=f\beta_{x_3}
\]

forces

\[
a=e,
\qquad
b=0.
\]

Therefore the admissible map module is one torsion-free scalar line. Positive
Cartier coorientation, endpoint normalization, and
\([dX_{03}]=+1\) fix its generator to \(e=1\).

## The scoped purity theorem

The independently constructed source and the actual target are canonically
identified:

\[
\boxed{
\operatorname{pur}_{x_3,\partial}^{\rm PC}:
E_{3,\rm src}\otimes\operatorname{or}(x_3)[-1]
\xrightarrow{\sim}
i_{x_3}^{!}P_3.
}
\]

This is finite Cartier purity, and it is the unique positively normalized
Bockstein-compatible map in the frozen filtration/support type.

Endpoint transitivity is the standard adjunction

\[
R\!\operatorname{Hom}_B
\left(B/(x_i),R\!\operatorname{Hom}_A(B,P_3)\right)
\simeq
R\!\operatorname{Hom}_A\left(A/(x_3,x_i),P_3\right),
\qquad i=0,1.
\]

After the complete occurrence and normal Koszul--Cech comparisons, every
lower term is retained and the two endpoint restrictions are

\[
+\left[
\frac1{x_0x_3u_0u_1u_3u_5}
\right]\otimes[dX_{03}],
\qquad
+\left[
\frac1{x_1x_3u_0u_1u_3u_5}
\right]\otimes[dX_{03}].
\]

Thus entry 130's \(\Gamma_0,\Gamma_1\) are actual morphisms in the
definitionally scoped road-face PC model once its source is retyped as
\(E_{3,\rm src}\). They are two restrictions of one edge purity arrow, not
two fitted maps.

## Sharp remaining blocker

The local target-side PC promotion is closed only for the established
road-face complex. It does not produce the scalar-side specialization
correspondence. The first remaining formula objective is

\[
\boxed{
d_{\rm circ}^{\rm PC}G_{03}^{\rm Cousin}
=G_{03}^{\rm Cousin}d_{\rm sp,sc},
\qquad
\operatorname{gr}(G_{03}^{\rm Cousin})=K_{\rm alt},
\qquad
\operatorname{Res}_{x_3}G_{03}^{\rm Cousin}
=\operatorname{pur}_{x_3,\partial}^{\rm PC},
\qquad
q_Q(G_{03}^{\rm Cousin})\ne0.
}
\]

The final condition is decisive. Any construction supported wholly in
\(F_1\) has zero ordinary \(Q=F_2/F_1\) leg and cannot solve this problem.
Nothing in the Cartier theorem manufactures that generic component.

## Admissible ablations

- Without the graph Bockstein, two \(B/(u_3)\) ambiguities remain.
- Deleting the radial/Tor-zero line makes unit normalization require a
  forbidden \(t_3^{-1}\).
- Deleting the normal/Tor-one line loses
  \(\eta_{3,\mathrm{mix}}\) and the primitive excess trace.
- Dropping lower Cech terms breaks the endpoint chain equations.
- Globally inverting \(x_3\) or \(u_3\) kills the supported costalk.
- Defining the source from the desired endpoint fractions is circular; the
  Thom-plus-can--var construction is required.

## Evidence

The proof is the explicit packet, finite Cartier duality, and two-by-two
Bockstein calculation above. Its independently established inputs are:

- research/voevodsky/check_absolute_unlocalized_support_pc.rs (entry 105);
- research/voevodsky/check_one_normal_can_var_cousin.rs (entry 100);
- research/voevodsky/check_d03_bivariant_pc_hom.rs (entry 97);
- research/voevodsky/check_d03_toric_cox_cousin_trace.rs (entry 129);
- research/voevodsky/check_d03_x3_loaded_pc_endpoint_boundary.rs
  (entry 130).

No new checker is required: the new assertion is standard Cartier duality for
the already enumerated entry-105 packet plus the displayed admissibility
calculation.

## Outcome contract

~~~json
{
  "claim": "In the definitionally scoped absolute D03 road-face model, the independently assembled x3 Thom-plus-BM source is canonically the finite Cartier costalk of P3, and its unique positively normalized Bockstein-compatible purity map has the two entry-130 endpoint restrictions.",
  "status": "proved_scoped_pc_edge_purity__global_scalar_specialization_open",
  "assumptions": [
    "P3 is the actual closed-star packet extracted from entry 105.",
    "The source is independently assembled from entry 129's Thom line and entry 100's original/BM packet.",
    "The graph Bockstein u3=t3*x3 is part of the admissible filtered structure.",
    "Reciprocal-standard and original/BM variances remain distinct until currying through entry 97."
  ],
  "evidence_refs": [
    "ledger entries 97, 100, 105, 129, and 130",
    "the explicit Cartier and two-by-two Bockstein calculation in this entry"
  ],
  "factorization_test": {
    "ambient_costalk": "one free line plus one B/(u3) line; no integer torsion",
    "unconstrained_endomorphisms": "larger than rank one",
    "Bockstein_compatible_maps": "one torsion-free scalar line",
    "positive_normalization": "unique unit",
    "v00_endpoint": "entry-130 positive residue",
    "v10_endpoint": "entry-130 positive residue",
    "generic_Q_leg": "not constructed"
  },
  "counterevidence": [
    "The theorem is scoped to the established road-face PC model.",
    "A correspondence supported wholly in F1 has zero ordinary Q leg.",
    "No scalar total-specialization differential or G03 chain map is constructed."
  ],
  "next_experiment": "Construct d_sp,sc and G03^Cousin with nonzero generic Q leg, and require its x3 residue to be the canonical purity map proved here."
}
~~~
