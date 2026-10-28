# F736: prior source-reached form transport and five-vertex table

## Most direct prior source located

`research/voevodsky/the-full-analytical-system-is-the-joint-graph-realization-of-the-regular-and-endpoint-channels.md`, especially:

- Common augmented carrier;
- Finite-regulator incidence into the regular face;
- One source-reached analytical bulk;
- Presentation maps;
- Chamber and edgewise-subdivision realization;
- Elementary C41 star in the eight-node lattice.

These sections were freshly inspected. They provide more than the scalar form equality used in earlier searches. No source or analytical checker was executed.

## 1. Existing universal source-reached realization

The source defines

    Psi(g)=(S1 g,S2 g,S3 g,S4 g),
    Psi_tilde(g)=(Psi(g),r_S g,beta_S g).

It retains the regular and independent endpoint responses. Its image has the source graph topology and a source-coordinate retract. Its universal property is explicit: compatible maps to the four charts, regular response and endpoint response factor uniquely through this source-reached graph.

The compatibility equations are

    f_j=C_ij f_i,
    r=r_S R_i f_i,
    b=beta_S R_i f_i.

They give a source g=R_i f_i independent of i, and the unique map is Psi_tilde(g). This is a useful precise comparison criterion for correlated word presentations; it is not an arbitrary Cartesian-product construction.

## 2. Full form, operator and feature transport already proved

The section Presentation maps defines, on each admitted essential image,

    q_i(x,y)=q_source(R_i x,R_i y).

It proves

    q_j(C_ij x,C_ij y)=q_i(x,y).

With each chart carrying the Hilbert topology transported from the completed source X_S, the chart maps S_i are unitary and the operators/features obey

    W_i=S_i W_source R_i,
    W_j C_ij=C_ij W_i,
    Phi_j C_ij=Phi_i.

The source states this for both inherited augmented and minimal observer features. Radical transport and the coercive spectral filtration are also presentation invariant.

These are actual analytical realization formulas, not merely a generic symbolic inverse-law profile. They apply to the declared transported essential-image topologies. They do not equate those topologies with an independently prescribed external physical norm.

The note separately warns that pulling back an absolute operator and taking the absolute value after compression need not agree:

    Z* |G| Z != |Z* G Z|

in general. Thus feature transport must name WHICH inherited or minimal feature is retained. A finite signed compression is not automatically an ordinary absolute-Gram isometry.

## 3. Domain correction: two compatible cores, not one false intersection

The master note distinguishes:

1. regular core: finitely many character sectors with m_chi in C_c^infinity(R), dense in phase-energy space;
2. analytic endpoint core: compactly supported physical observers, whose Mellin transforms are entire and have the required off-real endpoint evaluations.

A compactly supported smooth Mellin function is generally NOT an analytic endpoint test. Requiring nonzero compact real Mellin support and analytic continuation on a connected strip simultaneously would be incompatible with analytic uniqueness. Do not use the regular core for evaluations at +/-i/2.

The note supplies an explicit endpoint-preserving approximation on the admitted analytic endpoint graph domain. Choose fixed compact physical tests p_plus,p_minus with

    ell_sigma(p_tau)=delta_sigma_tau,

and define

    g_R_corrected = chi_R g
      + sum_sigma [ell_sigma(g)-ell_sigma(chi_R g)] p_sigma.

Then both endpoints are preserved EXACTLY for every R, while the phase-energy response converges under the source's graph/cutoff convergence hypotheses. This is the concrete compatibility mechanism between regular approximation and endpoint retention.

For the F736 calculation use the admitted physical analytic source core with the extra chart/cutoff domains required by the chosen witnesses, or its justified source graph closure. Do not silently replace it by the compact-spectral core or by the five-packet subspace.

## 4. Source-linked five-vertex candidate table

The following is an explicit EXTRACTION CANDIDATE combining the prior analytical pullback formulas with the retained correlated-word realization. It is not a claim that the master note already names these five vertices or supplies their intended regulator-dependent modifications.

For a word w of length7 on the admitted common source D, set

    i_w(g)=(S_w0 g,...,S_w6 g),
    Gamma_w(D)=image(i_w),
    r_w(i_w(g))=g,
    q_w(x,y)=q_source(r_w x,r_w y).

Retain r_S r_w and beta_S r_w, and the chosen inherited/minimal feature Phi_source r_w. Give Gamma_w the transported SOURCE topology, not an independently completed sevenfold product topology. The form is one source form, NOT a sum of seven copies.

| vertex | word w | source recovery | retained form/feature |
|---|---|---|---|
| V104 | 1,1,1,1,2,4,4 | r_w | q_source(r_w -,r_w -), Phi_source r_w |
| V105 | 1,1,1,1,2,3,4 | r_w | same source pullback |
| V110 | 1,1,1,1,1,4,4 | r_w | same source pullback |
| V111 | 1,1,1,1,1,3,4 | r_w | same source pullback |
| V113 | 1,1,1,1,1,2,4 | r_w | same source pullback |

The prior universal property supplies the candidate comparison

    J_w(x)=Psi_tilde(r_w x)

whenever all coordinate/regular/endpoint compatibility equations hold on that source domain. Its inverse onto the source-reached image is i_w composed with source projection. This states the maps rather than relying on equal dimension or scalar readouts.

To satisfy the Hermitian-presentation endpoint type, retain Gamma_w together with q_w, its observer functor action and the source natural isometry. Bare graph SETS remain insufficient; this is the precise distinction raised by the rejected C13 graph candidate.

## 5. Actual edge maps under this candidate

For a geometric edge u->v define

    T_uv=i_v r_u.

Componentwise these are the existing analytical C_ij maps at each retained occurrence, acting on the SAME source label. The only changed occurrences are4 and5:

    E511 V104->V105: occurrence5 C43,
    E519 V105->V111: occurrence4 C21,
    E513 V104->V110: occurrence4 C21,
    E535 V110->V111: occurrence5 C43,
    E514 V104->V111: occurrence4 C21, occurrence5 C43,
    E539 V111->V113: occurrence5 C32,
    E521 V105->V113: occurrence4 C21, occurrence5 C32,
    E536 V110->V113: occurrence5 C42,
    E515 V104->V113: occurrence4 C21, occurrence5 C42.

The master source's form/feature transport gives a source-linked way to interpret these conditional word maps as complete form presentations. This advances beyond an untyped graph replacement, subject to the common-domain and observer-naturality requirements.

## 6. Exact boundary of this extraction

The source also says explicitly that its chamber/esd7 statement concerns signed analytical comparisons. It does NOT manufacture Hilbert feature maps at untyped intermediate stages. The first C41-star inventory is a typed local prototype, not an automatic naming of every F736 stage.

Likewise, decorating every Gamma_w with the SAME pulled-back finite-cutoff functional would establish common observable transport, but would NOT by itself select the intended nontrivial face modification or its finite remainder. The original H234 analytical representative must be transported with its own boundary/whiskering data, not replaced by the strict identity of the newly source-defined chart maps.

Therefore distinguish:

- candidate source-linked V104/V105/V110/V111/V113 complete form presentations and edges: formulas now explicitly available by extraction;
- proof that they are the intended retained analytical stage presentations with the specific regulator-dependent H736 and both bottom/filler pairs: still requires the witness-level identification;
- positive external physical feature identification: not implied by either.

The remaining smallest comparison is now between the parent cutoff/spectral modification and its proposed source-pulled-back realization through J_w, including exact regulator placements, finite remainder, endpoint convention and adjacent-occurrence links. The paired Missing123 constructors and fixed-boundary bridge apply only after that interpretation is supplied.

## Disposition

Prior research already has an explicit source-reached universal property and full operator/feature-preserving chart maps. It also gives endpoint-preserving approximation, preventing an incorrect common-core identification. Together these yield the concrete candidate table above, not merely a request to invent five analytical objects.

No assertion is made that this derived candidate has completed the requested analytical F736 witness calculation. No tests, formal builds or analytical certifications were run.
