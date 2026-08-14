# Conductor-to-central-vertex purity audit

Date: 2026-08-14

Scope: entries 38, 93, 100, 101, and 103, with the current Nima objective
and Voevodsky context. This is an exploratory result packet. It introduces no
kinetic or BRST differential and makes no ledger or graph change.

## Canonical result packet

```json
{
  "claim": "After separating the loaded road-to-periphery transgression, alpha_plus is already the canonical filtered purity/Thom comparison supplied by entry 38, and this comparison together with delta forces the entry-100 local traces; equivalently the half-symbol is a literal canonical d2 of the v_plus support spectral sequence.",
  "status": "falsified",
  "assumptions": [
    "Scalar occurrence coordinates x_j and universal monodromies q_j are independent coefficient layers.",
    "The base ring is R0=Z[q0^+-1,...,q5^+-1], with u_j=q_j-1 and no u_j, Rees parameter, or 3 inverted.",
    "The plus source uses reciprocal-twist regular/ordinary support and the road target uses original-twist locally-finite/Borel-Moore support.",
    "The carrier support filtration is v_plus subset B_short subset K6 with the orientations of entry 103."
  ],
  "evidence_refs": [
    "src/ledger/20260813-38 Finite-Alpha-Prime Normal-Torus Lift and Nearby-Cycle Unit Theorem.md",
    "src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md",
    "src/ledger/20260814-100 Support-Directed Can-Var Packet and Three Local Cousin Traces.md",
    "src/ledger/20260814-101 Mistyped Pairwise Coherence and the Filtered Three-Road Star.md",
    "src/ledger/20260814-103 Peripheral Transgression Derives the Global Carrier.md",
    "research/voevodsky/check_central_vertex_rees_transgression.rs",
    "research/voevodsky/check_one_normal_can_var_cousin.rs",
    "research/voevodsky/check_weighted_three_road_star.rs"
  ],
  "factorization_test": {
    "entry38_constructs_source_internal_face_tubes": "proved on actual associahedral faces and the transverse occurrence-decorated domain",
    "entry38_constructs_conductor_to_v_plus_purity": "falsified; no such cross-geometry comparison occurs",
    "source_internal_unlocalized_Thom_class": "proved at coefficient level by entry 100, not by nonresonant inversion",
    "canonical_loaded_support_two_extension": "conditional on an independently constructed loaded absolute PC object and exact support filtration",
    "literal_spectral_sequence_d2": "falsified; the carrier d1 is an isomorphism and kills the only possible p=2 source before E2",
    "dual_Yoneda_secondary_map": "conditional and correctly typed once the loaded support filtration and Verdier-dual source purity equivalence exist",
    "D3_equivariance_of_full_comparison": "inconclusive; the coefficient Thom class is covariant only with its determinant/orientation line, while the cross-geometry comparison is absent",
    "entry100_traces_forced_by_Beck_Chevalley": "conditional on an unproved excess six-functor base-change theorem and naturality of the purity equivalence"
  },
  "counterevidence": [
    "Entry 38 defines q_E=exp(2*pi*i*alpha'*X_E) for a Koba--Nielsen boundary monodromy and tensors scalar occurrence weights through unchanged; it does not identify an occurrence x_j with q_j or q_j-1.",
    "Entry 38 works nonresonantly after inverting q_E-1, whereas alpha_plus must retain the supported u_j=0 fibre over the unlocalized ring.",
    "Entry 38's face tubes are attached to actual associahedral faces; the plus conductor link is a positive projectivized normal cone, and the literal v_plus dual block contains no road.",
    "The branch/road squares have rank-one Tor_1 excess and are not transverse Beck--Chevalley squares.",
    "The loaded absolute PC object, its v_plus and B_short support subobjects, and the required six operations have not been constructed in the cited evidence.",
    "Defining alpha_plus by the desired weighted top value or by its three desired residues would be a tautological redefinition.",
    "The carrier checker proves that E1 d1 from p=2 to p=1 is an integral isomorphism and that no higher page can carry a class out of the killed p=2 term."
  ],
  "next_experiment": "Construct the loaded absolute PC object C with the independent occurrence, reciprocal-monodromy, support, and orientation layers; form F0=i_{v+!}Ri_{v+}^!C and F1=i_{B!}Ri_B^!C; then construct a Verdier-dual purity equivalence from the plus normalization-conductor object to D(F0)[-2] (with any already absorbed suspensions stated). Pull it back along only the D03 marked derived square and test whether excess base change gives eta_mix and [1/(u0*u1*u3*u5)] with occurrence endpoints (1,1) and the separate positive physical normal."
}
```

## Status ledger for the bounded question

| Subclaim | Verdict | Reason |
|---|---|---|
| Entry 38's nearby-cycle units identify \(x_j\) with \(u_j\) | **falsified** | Entry 38 keeps scalar occurrence coefficients and Koba--Nielsen monodromy in separate layers. |
| The plus source has a canonical internal unlocalized Thom class | **proved, coefficient scope only** | Entry 100's tensor Koszul--Cech map gives \(\tau_A=[1/(u_1u_3u_5)]\in H_A^3(R_0)\) without base-ring localization. |
| That internal class canonically identifies the conductor source with the \(v_+\) PC costalk | **inconclusive** | No map of formal normal geometries, loaded absolute PC object, or purity transformation between them is constructed. |
| Once an independent loaded support filtration exists, its Yoneda two-extension is canonical and \(D_3\)-equivariant | **conditional** | This is formal for a \(D_3\)-stable exact filtration, but existence and target identification are unproved. |
| The half-symbol is a literal spectral-sequence \(d_2\) | **falsified** | Entry 103's carrier \(d_1\) is an isomorphism, so the top term does not survive to \(E_2\). |
| The half-symbol may be the Verdier dual of the canonical Yoneda two-extension | **conditional** | This has the right secondary variance and explains ordinary nullity, but still requires the source purity equivalence and loaded filtration. |
| Purity plus the loaded extension forces all entry-100 local traces | **conditional** | It would follow from natural excess Beck--Chevalley plus local normalization/uniqueness; that six-functor theorem is not in the ledger. |

## What entry 38 actually constructs

Entry 38 has two separate inputs:

1. a scalar occurrence-decorated cell ([F;\mu]), whose coefficient (mu)
   is retained unchanged; and
2. a Koba--Nielsen local system with physical boundary monodromy
   (q_E=\exp(2\pi i\alpha'X_E)).

Its analytic unit

\[
\frac{q_E-1}{2\pi i\alpha'X_E}
\]

has constant term one in the physical \(V_E\)-filtration. This compares the
nonresonant Pochhammer pole with the field-theory pole \(1/X_E\). It does not
compare the scalar occurrence coordinate \(x_j\) with \(q_j\), nor does it
identify the conductor normal cone with the central-vertex costalk.

There is also a notation collision: entry 38 calls the analytic ratio

\[
u_E(\alpha',X_E)=\frac{q_E-1}{2\pi i\alpha'X_E}
\]

a *unit*, whereas entries 95--103 use \(u_j=q_j-1\) for the nonunit normal
parameter. The first is invertible at \(X_E=0\); the second defines the
support that must not be removed. They cannot be substituted for one
another.

The precise support typing gap is geometric, not a missing scalar factor.
Entry 93's regular immersion

\[
Z=\operatorname{Spec}R\hookrightarrow
F_+=\operatorname{Spec}R[x_1,x_3,x_5]
\]

lives in the scalar normalization--conductor parameter geometry. Entry 38's
normal circles live around divisors \(D_E\subset\overline{\mathcal M}_{0,n}\),
and its map starts with an *already given actual associahedral face* in the
worldsheet chamber. The cited evidence supplies no map of formal
neighborhoods, specialization correspondence, or Cartesian square carrying
the conductor zero section to the support of the triangulation vertex
\(v_+\). It therefore supplies neither a comparison of extraordinary
pullbacks \(i^!\) nor compatibility with the normalization--conductor Cech
square. Multiplication by an analytic nearby-cycle unit can renormalize a
worldsheet normal contraction only after that support map exists; it cannot
create the support map.

Moreover, entry 38 uses the nonresonant ring in which (q_E-1) is inverted.
That is suitable for a face-tube contraction. It cannot by itself define the
current alpha map, because global inversion contracts (K(u_j)) and erases
the supported class at (u_j=0).

Entry 100 supplies the support-correct replacement:

\[
[R\xrightarrow{u}R]
\xrightarrow{(1,u^{-1})}
[R\longrightarrow R[u^{-1}]].
\]

Here (u^{-1}) occurs only in the named Cech localization summand. Tensoring
the three reciprocal odd normals gives the source-internal class

\[
\tau_A=\left[\frac1{u_1u_3u_5}\right]\in H^3_A(R_0),
\qquad A=(u_1,u_3,u_5).
\]

This is a canonical coefficient Thom/local-fundamental class. Calling it the
comparison with the \(v_+\) costalk would add the missing geometric map by
name.

## Exact filtration and variance that are actually available

The only fully certified global filtration is the carrier filtration

\[
F_0^{\rm car}=C_*(v_+)
\subset
F_1^{\rm car}=C_*(B_{\rm short})
\subset
F_2^{\rm car}=C_*(K_6).
\]

Its \(E_1\) terms have ranks \(1,2,2\) in positions
\((p,n)=(0,0),(1,1),(2,2)\), and

\[
d_1:H_2(K_6,B_{\rm short})\xrightarrow{\sim}
H_1(B_{\rm short},v_+)
\]

is a saturated integral isomorphism. This fixes the homological variance
roads-to-periphery. Entry 99's carrier has the inverse/dual variance.

The proposed loaded refinement must independently retain:

- conductor order for \(J_+=(x_1,x_3,x_5)\), with scalar occurrence
  coordinates not identified with monodromy;
- reciprocal normal-support degree for
  \(I_+^\vee=(u_1^\vee,u_3^\vee,u_5^\vee)\);
- dual-block/Cousin depth \(f\to e\to q\to a\), of ranks \(1,3,3,1\);
- regular/ordinary versus locally-finite/Borel--Moore support direction; and
- the support filtration \(v_+\subset B_{\rm short}\subset K_6\).

The cited entries do not construct a single total filtration combining these
layers. Therefore an assertion of one exact total Rees indexing is presently
unsupported. What is fixed is that it must be bounded, exhaustive,
separated, integral, and \(D_3\)-stable, with neither its Rees parameter nor
any \(u_j\) nor \(3\) inverted. Its specializations must give the ordinary
zero composite at \(t=1\) and the nonzero carrier/weighted star at \(t=0\).

For the source-normal factor the variance and degree are unambiguous without
choosing a global chain convention:

- use reciprocal twist \(u_j^\vee=q_j^{-1}-1=-q_j^{-1}u_j\);
- use regular/ordinary support \(j_!\mathbb D\), not the road convention
  \(Rj_*\);
- the three-normal local class lies in support cohomological degree \(3\);
- order the determinant line as
  \(h_1^\vee\wedge h_3^\vee\wedge h_5^\vee\).

The paired road side uses the original twist and locally-finite/Borel--Moore
support. Each repeated branch/road normal contributes the entry-100 shifted
excess line generated by \(\eta_{i,\rm mix}\).

## The precise Yoneda reduction

There is a viable weaker formulation, but it is not a literal \(d_2\). Let
\(C=P_{\rm abs}^{F,\rm PC}\) be an independently constructed loaded absolute
object and define the support pieces

\[
F_0=i_{+!}Ri_+^!C,
\qquad
F_1=i_{B!}Ri_B^!C,
\qquad
0\subset F_0\subset F_1\subset C.
\]

If these are actual exact \(D_3\)-stable subobjects, the filtration supplies
the canonical Yoneda extension

\[
0\longrightarrow F_0\longrightarrow F_1\longrightarrow C/F_0
\longrightarrow C/F_1\longrightarrow0.
\]

It represents

\[
e_F\in\operatorname{Ext}^2(C/F_1,F_0)
=\operatorname{Hom}(C/F_1,F_0[2]).
\]

Verdier duality gives the direction needed by the half-symbol:

\[
\mathbb D(e_F):\mathbb D(F_0)[-2]
\longrightarrow\mathbb D(C/F_1).
\]

Consequently the genuinely minimal source theorem would be a normalized
purity equivalence of the form

\[
\operatorname{pur}_+:
\mathcal S_+^{\rm cond}
\xrightarrow{\sim}
\mathbb D(F_0)[-2],
\]

up to suspensions already included in the definitions of the conductor and
PC complexes. An unshifted identification
\(\mathcal S_+^{\rm cond}\simeq F_0\) has the wrong variance for this formula.
The degree-two shift belongs to the support-filtration extension; the
three-normal Thom class separately lies in support degree three. The cited
objects do not state enough grading conventions to collapse these into a
single further shift without assumption.

Then

\[
A_+^{\rm sec}=\mathbb D(e_F)\circ\operatorname{pur}_+
\]

is a canonical secondary filtered morphism. Its ordinary direct composite
is zero, as required. This formulation can eliminate the demand for a
strict ordinary alpha chain map or a strict inverse to delta.

It must not be called the literal spectral-sequence \(d_2\): the proved
carrier \(d_1\) is an isomorphism and no top class reaches \(E_2\). It is
better called the Verdier-dual Yoneda two-extension, or a Toda
representative of that extension. The Yoneda class is canonical once the
filtration is independently present; an arbitrary Toda bracket would still
carry null-homotopy indeterminacy.

This reduction also explains entry 102 correctly: the integral Tate class
is the constant carrier shadow of a two-extension. It is not the loaded
weighted extension itself.

## Canonicity and \(D_3\)-equivariance

The source-internal Thom packet is canonical under permutations of the three
odd normals only after retaining the ordered determinant line. The
three-cycle is orientation even, while a reflection swaps two normals and is
orientation odd. Thus an untwisted invariant Thom generator is not the
correct object. The reflection sign must be carried by the normal orientation
or \(\chi_N\) line. The one-step operation exchanging plus and minus sheets
also requires the separate polarity line \(L_{\rm pol}\).

The physical lines \([dX_{14}],[dX_{03}],[dX_{25}]\) appear on road
restrictions and remain separate from this conductor determinant. They
cannot be manufactured by a Thom isomorphism on \(J_+\).

If \(C,F_0,F_1\) are independently \(D_3\)-stable, their Yoneda extension and
its Verdier dual are formally \(D_3\)-equivariant. This proves no
\(D_3\)-equivariant source purity equivalence: that is exactly the missing
cross-geometry comparison. Entry 101's weighted star shows covariance after
assuming the top value; it does not derive that value.

## Beck--Chevalley audit

Purity plus the support extension would force the entry-100 local homotopy
classes only under all of the following unproved statements:

1. the loaded PC category has the support recollement and Verdier operations
   used to define \(F_0,F_1,C/F_1\);
2. \(\operatorname{pur}_+\) is natural for the three marked road
   correspondences;
3. derived excess Beck--Chevalley holds for the nontransverse branch/road
   squares and returns their rank-one \(\operatorname{Tor}_1\) determinant;
4. its repeated-normal comparison is the entry-100 normalization
   \(p^\vee\mapsto-qp\), hence gives \(\eta_{i,\rm mix}\) with positive top
   orientation;
5. occurrence pullbacks, the separate physical normal, and \(\chi_N\) are
   preserved; and
6. the quotients of the loaded support filtration identify with the already
   established peripheral and relative road PC objects.

Under these hypotheses, the endpoint-normalized local Hom class is unique,
so Beck--Chevalley would identify the three restrictions with
\(\Theta_{14}^{\rm loc},\Theta_{03}^{\rm loc},\Theta_{25}^{\rm loc}\).
Without them, the implication is unsupported.

The following shortcuts are tautological and are not constructions:

- defining \(\operatorname{pur}_+\) by \(f\mapsto\tau_AK_{\rm rel}\);
- defining the loaded peripheral object as the image on which the desired
  three residues glue;
- defining excess base change to be the entry-100 trace;
- calling the entry-102 Tate class the loaded Yoneda extension; or
- renaming the already desired filtered half-symbol a \(d_2\) or Toda class
  without constructing the support filtration and checking its
  indeterminacy.

No six-functor step in this section is established by entries 38, 93, 100,
101, or 103.

## Connective-\(K\) formal-group-law check

The identity

\[
F_\beta(x,y)=x+y-\beta xy,
\qquad q=1-\beta x,
\qquad \iota_F(x)=-\frac{x}{1-\beta x}
\]

does algebraically mirror

\[
u^\vee=q^{-1}-1=-q^{-1}u.
\]

Indeed \(u=-\beta x\) gives
\(u^\vee=\beta x/(1-\beta x)=-\beta\iota_F(x)\). This is a useful sign and
formal-inverse mnemonic, but it does not improve the current purity typing.
No cited construction equips the conductor coordinates with connective-\(K\)
first Chern classes, supplies canonical normal line bundles with those
classes, or identifies their \(K\)-characters with the independent universal
monodromies.

Imposing \(q_j=1-\beta x_j\) in the current coefficient model would quotient
the ring by \(u_j+\beta x_j\) and collapse the deliberately independent
occurrence and monodromy layers. It would therefore be a new base change,
not a derived bridge. It risks exactly the double-loading/conflation excluded
by entries 38, 80, 97, and 98. The formal-group-law idea becomes a genuine
test only if one first constructs a canonical normal line \(L_j\) for which
the scalar \(x_j\) is independently proved to be \(c_1^{CK}(L_j)\) and the
PC local system has character \(1-\beta c_1^{CK}(L_j)\). No such datum is
present, so this audit records the idea as analogy, not evidence.

## Smallest discriminating next test

Do not start with a road or the weighted target. On the eight-cell Boolean
coface block of \(v_+\), construct the absolute loaded costalk

\[
F_0=i_{+!}Ri_+^!C
\]

with scalar occurrence coefficients and the reciprocal packet
\(K(u_1^\vee,u_3^\vee,u_5^\vee)\) still independent. Then construct, from an
actual map of formal support diagrams, the top and one codimension-one
component of

\[
\operatorname{pur}_+:
\mathcal S_+^{\rm cond}\longrightarrow\mathbb D(F_0)[-2].
\]

The single sharp check is the \(e_3\)/\(D03\) restriction: derived pullback
must produce the labelled excess generator

\[
\eta_{3,\rm mix}
=-q_3\,\ell_3^{+,\vee}\otimes p_3^{03}
-p_3^{+,\vee}\otimes\ell_3^{03}
\]

and, after the existing Koszul--Cech comparison, the residue

\[
\left[\frac1{u_0u_1u_3u_5}\right]
\]

with occurrence endpoints \((1,1)\) and the physical line
\([dX_{03}]\) still separate. This one square tests the missing support map,
Verdier variance, determinant sign, unlocalized purity, and excess
Beck--Chevalley at once. Defining its output to be the displayed residue
would be tautological; the output must be computed from the independently
constructed formal-support comparison.

## Verification

No new Rust checker was added. The following existing certificates were
formatted, compiled with warnings denied, and rerun:

- `check_central_vertex_rees_transgression.rs`: `proved`;
- `check_one_normal_can_var_cousin.rs`: `proved`;
- `check_weighted_three_road_star.rs`: `inconclusive`, as designed.
