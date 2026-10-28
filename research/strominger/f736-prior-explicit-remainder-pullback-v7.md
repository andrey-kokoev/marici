# Existing analytical H234 pullback: explicit representative on retained word images

## Prior sources freshly inspected

1. `research/voevodsky/the-recovered-face-234-is-an-admissible-invertible-modification-in-the-rapid-decay-asymptotic-quotient.md`, especially represented observers, bounded-packet continuity, adjoints and composition stability.
2. `research/voevodsky/the-rank-one-v1-supported-coherence-cell-is-a-four-chart-cech-tetrahedron.md`, especially complete-form chart edges and the boundary of signed/form-valued identification.
3. `research/voevodsky/the-joint-source-graph-makes-the-chamber-twistor-tower-analytically-equivariant.md`, especially actual transported successors versus independently defined successors.

This search also uses the master source-reached universal property and word table already extracted in `f736-prior-joint-graph-form-table-v6.md`. No analytical checker or formal build was run.

## 1. The prior pullback theorem is already explicit

For an admitted test observer h the source H234 representative is

    Err_Lambda(h)
      = Tr(P_Lambda Phat_Lambda U_S(h))
        - 2 h(1) log Lambda
        - V_S(h),

where V_S(h)=<M_g_h,L_S> is the source normalized spectral/distributional pairing.

The note states bounded-packet estimates of every rapid-decay order. Its Composition stability section proves that precomposition with a continuous observer map alpha preserving bounded packets, with no cutoff-dependent seminorm blowup, preserves the rapid-decay ideal. It explicitly includes convolution polarization on bounded bilinear packets.

Thus a pullback along a specified source recovery map is available conditionally from prior results. It is too broad to keep calling the existence of such a pullback an unspecified missing theorem.

## 2. Pullback on the actual five retained word images

Use the v6 candidate word objects Gamma_w(D), source embeddings i_w and recoveries r_w, restricted to D in the admitted source test algebra. The topology here is transported from D, not an arbitrary product completion. Hence r_w is continuous and bounded-packet preserving by the declared topology. This topological choice does not prove equivalence with any independently prescribed native physical norm.

Define the represented-observer map

    alpha_w(x)=U_S(r_w x).

Then the explicit pulled-back representative is

    H_w,Lambda(x)
      = H234_Lambda_obs(alpha_w(x))
      = Tr(P_Lambda Phat_Lambda U_S(r_w x))
        - 2 (r_w x)(1) log Lambda
        - V_S(r_w x).

For polarized word inputs x in Gamma_w(D), y in Gamma_w(D), let

    h_xy=(r_w x) * (r_w y)^*.

The polarized representative is

    H_w,Lambda(x,y)
      = Tr(P_Lambda Phat_Lambda U_S(h_xy))
        - 2 h_xy(1) log Lambda
        - V_S(h_xy).

Do not replace h_xy(1) by an observation Gram chosen from the finite encoder. Do not split V_S into endpoint/current coordinates with a new normalization; use the actual source pairing and preserve its independently retained completed endpoint data.

This formula applies to each of V104,V105,V110,V111,V113 with its own retained word and recovery. It uses full represented observers, not five observations or a finite44-dimensional convolution closure.

## 3. Boundary and finite remainder are retained

Define the pulled-back cutoff and spectral families by precomposition:

    T_w,Lambda = centered_cutoff_Lambda o r_w,
    V_w = V_S o r_w.

Then, as the REPRESENTATIVE of the source difference,

    H_w,Lambda = T_w,Lambda - V_w.

In the same source-declared asymptotic modification target, this is the pullback of the existing modification between these two families. It is not a newly defined differential in an unrelated chain complex. The representative is retained at finite cutoff, even though its class vanishes modulo the rapid-decay ideal.

Let B be a bounded subset of Gamma_w(D). Its recovered source packet r_w(B) is bounded in D, so the source estimate directly gives

    sup_(x in B) |H_w,Lambda(x)| <= C_(r_w B,N) Lambda^(-N).

The polarized version uses continuity of convolution on the declared bounded bilinear packets. A source-defined cutoff change requires the additional exponent/parameter bookkeeping from the original theorem; none is inferred merely from word incidence.

## 4. Exact transport across candidate edges

For the candidate edge map T_uv=i_v r_u, source recovery satisfies

    r_v T_uv = r_u.

Consequently

    H_v,Lambda(T_uv x,T_uv y)=H_u,Lambda(x,y)

for the polarized representative, and the same identity holds for the separate pulled-back cutoff and spectral families. The parent trace order is unchanged throughout this equality. The source's adjoint rule reverses the product placement when passing to opposite polarity; it does not erase the finite skew channel.

This exact equality is useful witness-data transport on the CANDIDATE pullback diagram. It is not evidence that a separately normalized native finite readout is this family. The frozen physical readout uses its own reference/placement data, whose identification must still be supplied.

## 5. Why this still does not assign H736 by fiat

The pulled-back H234 above compares cutoff and spectral observer functionals. The retained geometric F736 triangle compares

    C32 C43  versus C42

at occurrence5, with a disjoint C21 change at occurrence4.

To make H_w,Lambda the intended geometric face witness, identify the corresponding transformation boundaries in ONE realization target and take the specified inverse/mate with its units and counits there. Equality of the scalar representative on source-recovered inputs is not that boundary identification. Nor does negating the scalar error automatically define the reverse mate.

The source Cech note supplies complete-form chart edges and their coherent inverse laws. It explicitly identifies derived C34 only at signed/form-valued strength, not as a trace-norm equivalence of unanchored cutoff operators. Thus the source comparison is usable without claiming a finite physical trace inverse.

The joint-source equivariance note likewise distinguishes conjugation-defined successors from independently defined physical/geometric successors. The former exist by construction; equality with the latter is an additional source-naturality theorem. The analogous distinction must remain explicit for the pulled-back F736 face.

## 6. Narrowed coupled construction target

The first partial deliverable is now explicit: the source remainder representative, its separate boundary families, its bounded-packet estimates and its candidate word-edge transport are given by the formulas above under the source hypotheses.

The next concrete identification is NOT to invent that pullback again. It is to supply the comparison carrying the geometric occurrence5 triangle and its adjacent-occurrence links to the two cutoff/spectral boundary transformations of this inherited modification, with the correct reverse-mate convention.

After that identification use ONE shared H736 and calculate the dependent pairs

    (H745,Theta324):Missing123(H731,H732,H736),
    (H760,Theta325):Missing123(H734,H735,H736).

Retain the actual domains, both placements, endpoint conventions and finite representative in the structured lift. The paired constructor and fixed-boundary formal bridge are already available; the boundary identification with the intended analytical/native face is not supplied merely by their existence.

## Disposition

Prior composition stability plus the declared word-source recovery maps yields an explicit conditional remainder pullback, not just a plan to find one. This is a derived instantiation of existing source theorems on the stated candidate carriers. It is not a newly certified or completed native F736 analytical filler.

No tests, certifications, native source changes or graph admissions were performed.
