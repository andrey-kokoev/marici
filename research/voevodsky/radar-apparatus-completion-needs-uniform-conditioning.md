# Radar apparatus completion needs uniform conditioning

## Result and fresh leaf

Fresh resume selected `radar-apparatus-conditioning-completion:v1`.
The finite radar-shape map extends continuously when both the records and the
apparatus vary, provided their joint domain retains a uniform inverse-design
bound and positive baseline/time resolution margins. A quantitative joint
Lipschitz estimate is given below.

Pointwise invertibility at every finite stage is insufficient. An exact
near-redundant probe example has vanishing candidate-record discrepancy but
constant processed discrepancy. This is an apparatus/record hostile, NOT a
newly established vacuum-source counterexample.

## Domain certificate

Keep the labelled three-time, three-direction record, actual probe vectors,
clock calibration, source reference and instantaneous-return convention.
For vectors v_d=(x_d,y_d), define L_d=(x_d^2,2*x_d*y_d,y_d^2), and use induced
infinity matrix norm and maximum component vector norm.

A sufficient certificate is

    ||L^-1||_infinity <= K,
    epsilon >= e0 > 0, h >= h0 > 0,
    r0 <= R_jd <= M, with r0>0.

Here h is a proper-time step and R is calibrated half-round-trip distance.
K bounds the inverse norm, not merely a scale-free condition number. It must
be checked in the declared coefficient normalization. These conditions are
sufficient, not necessary; coordinated parameter rescalings may leave the
physical reading unchanged even outside this convenient domain.

The clock center, raw emission/reception pairs and all protocol metadata remain
in the package. Varying the center is not silently identified with observing
the same spacetime event. A physical source also retains its own metric positivity,
ray-domain and reflection gates. This certificate bounds record processing;
it does not prove that new apparatus positions lie in an existing radar patch.

A concrete certificate used in the checks is

    K=1, e0=1/64, h0=1/8, r0=1/128, M=1.

The original design has ||L^-1||=1/8. Both previously certified rounded physical
packets satisfy these bounds. This is ordinary certificate membership, not a
new proof of their source realizations.

## Joint perturbation theorem

Write w=D(R^2), with temporal weights (1,-2,1). Then

    Y=-[1/(2 epsilon^2 h^2)] L^-1 w.

For two packets in the common certificate domain let

    delta_R=max |R-R'|,
    delta_L=||L-L'||_infinity,
    delta_e=|epsilon-epsilon'|, delta_h=|h-h'|.

The following conservative bound holds:

    ||Y-Y'||_max <=
        4KM/(e0^2 h0^2) delta_R
      + 2K^2 M^2/(e0^2 h0^2) delta_L
      + 4KM^2/(e0^3 h0^2) delta_e
      + 4KM^2/(e0^2 h0^3) delta_h.                 (*)

Proof: ||w||<=4M^2, ||w-w'||<=8M delta_R and

    ||L^-1-L'^-1||<=K^2 delta_L.

For a=epsilon^-2 h^-2, the mean-value estimate gives

    |a-a'|<=2 delta_e/(e0^3 h0^2)+2 delta_h/(e0^2 h0^3).

Insert these estimates in the three-term telescoping difference of
-(1/2)a L^-1 w. No differentiability or frequency prior on a spacetime metric
is used. The theorem concerns the declared finite reading, not instantaneous E.

If probe components are bounded by V and their maximum discrepancy is delta_v,
then delta_L<=8V delta_v. Alternatively, certificate comparison may directly
retain delta_L and avoid an unnecessary coordinate upper bound.

This treats calibrated parameter uncertainty as uncertainty in the processing
inputs. Emission-time jitter that changes which physical rays were measured
must additionally be propagated into delta_R by a source or instrument bound;
it is not magically covered by changing h alone.

## Closure and comparison

Suppose a sequence of certified records/apparatus data is Cauchy in these
finite coordinates, retaining the same discrete labels. If L_n converges to L,
then

    ||L_n x|| >= ||x||/K

passes to the limit. Thus L is injective, hence invertible in this square finite
space, and ||L^-1||<=K. The epsilon/h and range margins also survive. The
clock-grid relations are closed and r0 keeps reception strictly future-pointing.
Therefore the readout has a unique continuous extension to the closure of
ANY admitted subset of this domain, including the actual physical source image.
The closure of that image is not asserted to equal the whole coordinate domain.

Passive orthogonal comparison remains compatible with this extension. In
components (11,12,22), its congruence map C_Q has infinity norm at most 2.
The transformed design satisfies L'=L C_Q^-1, so a valid transported certificate
is K'=2K. One must not claim this particular component-norm K is rotation
invariant. A Frobenius-coordinate singular-value formulation can instead make
the rotational norm invariance explicit. Either way the comparison is bounded
and its equality with direct section reading extends by continuity.

## An exact degenerating-apparatus hostile

Take v1=(1,0), v2=(0,1), v3=(1,delta), with delta=1/n>0. Then

    L_delta=[[1,0,0],[0,0,1],[1,2delta,delta^2]],
    G_12=(q3-q1-delta^2 q2)/(2delta),
    ||L_delta^-1||=1/delta+delta/2   (0<delta<=1).

Every finite design is invertible, but the limit duplicates the first probe.
At every time take the static flat squared-distance data

    q=(1,1,1+delta^2).

This base packet is physically realized by static reflectors in Minkowski
space, with distances epsilon*sqrt(q). At the central time ONLY, perturb q3
by delta/2. All candidate clock differences remain positive. The fitted
central G_12 increases by exactly 1/4, while the squared-data discrepancy
tends to zero. Since both affected q values are at least one,

    distance discrepancy <= epsilon*delta/4.

For the retained h=1/4, the processed Y_12 discrepancy is exactly

    (1/4)/h^2=4.

The two candidate sequences converge to the same singular apparatus and same
raw records, but their processed limits differ. No single continuous extension
through that limit can agree with both. The fixed-K domain excludes this
hostile for a mathematically specified reason, rather than rejecting a result
after looking at the desired physical answer.

The perturbed sequence is a synthetic record/noise control. Its positive clock
pairs and even its fitted positive metric do not establish a vacuum realization
or a physical noise law. This leaf does not upgrade it to such a claim. Physical
noncollapse within the regular source image was already certified separately.

## Verification and synthesis gate

Run:

    python research/voevodsky/check_radar_apparatus_certificate.py

All 42 exact controls passed: original/physical certificate membership, joint
perturbation bounds, explicit inverse norms and constant hostile output gaps,
and refusal of singular or zero-resolution limits. Receipt:
`research/voevodsky/radar-apparatus-certificate.json`.

The general Lipschitz and completion results are written proofs. The finite
controls do not prove the universal statement by sampling.

The selected conditioning leaf is resolved. The remaining synthesis task is
to state precisely the established source -> causal record -> direct section
reading -> certified completion chain, and separate its scoped mathematical
closure from outstanding owner adoption and any common-foundation claim.
