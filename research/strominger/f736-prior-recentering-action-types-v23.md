# Prior recentering action types and an explicit one-sector response square

## Search result

The one-sector F736 carrier already names the actual log source, physical half-density chart, response functions, endpoints and represented observer. Prior response work supplies independently defined formulas and an intrinsic target topology. These permit an explicit response-coordinate intertwining calculation, without defining the target action merely by response conjugation.

The search also identifies a first typing issue with the proposed next step: Hardy carrier recentering is not automatically an action on the retained observer LABEL. Their effects on the operator coordinate differ. No source located here identifies either action with one of the native F736 fine-edge constructors.

The response dilation formulas below are derived here by substitution into the existing source definitions; they are not claimed as a newly located theorem already stated verbatim in a prior paper. No tests or formal builds were run, and no full centered-boundary or filler completion is claimed.

## Sources read

- `research/strominger/f736-derived-one-sector-carrier-assembly-v17.md` — actual retained source and coordinate map, section 4 observer action and section 5 word-edge definitions.
- `research/strominger/f736-prior-intrinsic-response-normalization-v13.md` — exact physical/log dictionary, Fourier conventions, Mellin endpoint and identity-density observations.
- `research/voevodsky/the-four-function-response-map-is-continuous-into-two-schwartz-and-two-relative-history-rungs.md` — independent target formulas and continuity.
- `research/voevodsky/the-complete-response-retract-closes-local-seam-endpoint-stability-and-radical-descent-for-the-resolved-joint-graph.md` — local response-image transport and its global scope boundary.
- `research/nima/convolution-successor-and-observation-have-a-common-joint-graph-domain.md` — actual fixed-observer multiplication/endpoint square and the graph-domain extension criterion.
- `research/voevodsky/exact-hardy-transport-places-the-observer-at-one-boundary-not-across-the-expanding-prolate-window.md` — fixed observer multiplier under cutoff-carrier transport and boundary-local interpretation.
- `research/voevodsky/the-recentered-relative-difference-leg-is-exactly-cutoff-independent.md` — exact difference-feature covariance, with moving left placement still separate.
- `research/strominger/f736-correlated-word-edges-result-v1.md` — actual correlated-word edge orientations and limits of the declared realization.

The complete-response retract defines its source-translation action through source recovery; that alone is not an independent native target-action verification. The explicit formulas in section 2 below avoid relying solely on that argument.

## 1. Two different action types

The v17 source is

    D=C_c^infinity(R),
    A_h = integral h(u) U_(exp u) du,
    F(h)(x)=x^(-1/2)h(log x), x>0,

extended by zero. On the declared source the dilation representation is abelian and unitary. The same h is retained across F(h), A_h, the compatible spectral chart, response, endpoints and cutoff families.

### Hardy cutoff recentering

On the operator carrier the known action is

    V_t=M_(exp(2its)).

Since the represented observer is M_mh,

    V_t M_mh V_t^* = M_mh.

This changes the cutoff/carrier frame while leaving the observer label fixed. It is a transformation of the realization/index data, not automatically the transformation h(u)->h(u-s) on D.

### Translation of the observer label

Define for fixed real s

    (sigma_s h)(u)=h(u-s).

This is continuous D->D in the LF topology, translating each compact support stage to another compact stage. With the frozen log Fourier convention,

    m_(sigma_s h)(z)=exp(-isz)m_h(z),
    A_(sigma_s h)=U_(exp s) A_h.                  (LABEL)

The operator equation follows by u=v+s and the source representation law. It is LEFT composition, not conjugation. Abelian source conjugation by U_(exp s) instead leaves A_h unchanged.

Thus one cannot simultaneously translate the F(h) source-vector coordinate and conjugate A_h as if those were two descriptions of the same retained-label action. The graph carries both coordinates, so the mismatch cannot be hidden by forgetting the source.

This rejects that naive combination of actions, not existence of a coherent recentering action with the correct fields.

## 2. An explicit naturality equation on the actual physical response

For the physical half-density define

    (D_s f)(x)=exp(-s/2) f(exp(-s)x).

Direct substitution in F gives

    F sigma_s = D_s F.                            (HALF-DENSITY)

Unlike additive physical translation, D_s preserves the positive half-line and compact support away from zero. It is therefore an actual continuous source operation on the one-sector response inputs.

The independently defined response is

    R(f)=(B_f,Q_f,A_f,C_f),
    B_f(a)=f(a),
    Q_f(a)=integral exp(-2pi i a x)f(x)dx,
    A_f(a)=integral_(-infinity)^a f(x)dx,
    C_f(a)=PV integral exp(-2pi i a x)f(x)/x dx.

Define an EXPLICIT target coordinate action rho_s, before using the inverse response projection, by

    (rho_s B)(a)=exp(-s/2) B(exp(-s)a),
    (rho_s Q)(a)=exp( s/2) Q(exp( s)a),
    (rho_s A)(a)=exp( s/2) A(exp(-s)a),
    (rho_s C)(a)=exp(-s/2) C(exp( s)a).

Changing variable x=exp(s)y in the source integrals proves

    R D_s = rho_s R,
    R F sigma_s = rho_s R F.                     (RESPONSE-SQUARE)

For C the factor 1/x cancels the Jacobian; positive dilation preserves the PV prescription. On the compact-away-from-zero inputs there is no singular integral at x=0 in the first place.

For each fixed s, these coordinate actions are continuous on the two Schwartz and weighted second-order relative-history rungs. Polynomial weights at scaled arguments are comparable by finite s-dependent constants, derivatives acquire finite scale factors and endpoint limits scale as displayed. No uniform estimate for all s is claimed. The actions compose rho_s rho_t=rho_(s+t).

This proves a genuine coordinate-level response square from independent formulas. It is not just a target action defined as R D_s R_inverse, although it agrees with that action on the actual response image.

## 3. Endpoints and source density are NOT stationary under label translation

The v13/v17 endpoint convention is

    beta(h)=(m_h(i/2),m_h(-i/2))
           =(A_(F h)(+infinity),C_(F h)(0)).

Consequently

    beta(sigma_s h)=diag(exp(s/2),exp(-s/2)) beta(h).

Both this identity and its response-side version follow from the explicit formulas above. The second coordinate is the C seam evaluation at 0, not its limiting values at infinity.

The source identity density changes by

    (sigma_s h)(0)=h(-s),
    B_(D_s Fh)(1)=exp(-s/2)B_(Fh)(exp(-s))=h(-s).

Thus the volume field for the transformed observer at cutoff L' is

    2 L' h(-s),

not automatically 2 L' h(0). The exact cutoff-volume cocycle with FIXED observer h and the observer-label translation law are distinct operations. If a construction uses both, keep both effects explicitly.

The spectral form W(sigma_s h) likewise must be evaluated on the transformed observer; no general invariance of that linear functional is asserted.

## 4. What is already exact on the signed source FORM

The polarized source form in v17 is q(h,k)=W(h*k_star). Simultaneous label translations satisfy

    (sigma_s h)*(sigma_s k)_star = h*k_star.

Hence q(sigma_s h,sigma_s k)=q(h,k). This does not contradict the change of the LINEAR observation W(sigma_s h): the polarized test h*k_star is unchanged when BOTH amplitudes move, whereas translating one already assembled observer test is a different operation.

This is another reason to state whether the source variable in a proposed square is an amplitude, a polarized pair, its convolution test, or a vector in the operator carrier. Similar notation does not identify these action types.

## 5. The remaining full ordered-coordinate comparison is concrete

For label translation, the actual v17 ordered coordinates become

    B_Lambda(sigma_s h)
      =P_Lambda Q_Lambda U_(exp s) A_h,
    B_Lambda_rev(sigma_s h)
      =Q_Lambda P_Lambda U_(exp s) A_h.

These are not inferred to equal conjugates of the old B_Lambda coordinates. Any replacement by shifted cutoff projections needs the actual dilation/cutoff identities with consistent physical/Fourier scaling, and the true outer regulator must follow those identities.

For fixed-label Hardy recentering, the difference-feature square from v22 applies instead; the full ordered field retains its moving left projection and placement comparison. Neither action erases the finite reference-calibration term from v21.

A target operation on the full retained graph can always be proposed by reevaluating all coordinates at sigma_s h. Calling it native still requires comparison with the independently intended physical/native constructor. The response, endpoint and density components above now have explicit formulas; the cutoff/spectral/composition-level identifications must still be supplied.

## 6. Why an F736 edge is not already this cutoff step

The existing retained word-edge maps have

    T_uv=I_v r_u,
    r_v T_uv=r_u.

They change presentation while preserving the SAME recovered h. Their geometric occurrence labels include C21,C43,C32,C42. The source-backed word realization does not identify such an edge with sigma_s, a cutoff-L increment or V_t acting on Hardy vectors.

The corrupted flattened-program shortcut was already rejected in the word-edge result; reinterpreting an entire word program as a fine edge was a type error. Likewise, declaring one fine edge to be a nontrivial recentering step requires an actual source indexing/constructor comparison, not only a suggestive stage label.

The exact response square in section 2 lives on the actual candidate carrier's declared coordinates, but it has not thereby become the desired K(eta24) naturality square on the independently intended native objects.

## Narrowed next step

First state which source action the intended native recentering constructor uses:

1. fixed-observer change of cutoff/carrier frame; or
2. translation/dilation of the retained observer amplitude; or
3. simultaneous motion of a polarized pair whose assembled convolution test stays fixed.

Then specify its target action and the comparison to the F736 word/index structure. For option 2, use (RESPONSE-SQUARE), (LABEL), the endpoint matrix and h(-s) density formulas rather than stationary substitutes. For option 1, use the existing Hardy difference-feature covariance and retain the left placement/volume/reference fields.

The first unprovided native datum is the identification of the intended generator/action type, followed by its full ordered-boundary comparison. This is an interpretation/typing obligation, not evidence that the parent signed H234 is absent, that the candidate graph is invalid, or that no enhanced K can exist.

Full K and both coupled bottom/filler pairs over one H736 remain open. No uniform operator-family norm, physical positive metric or native completion is asserted.
