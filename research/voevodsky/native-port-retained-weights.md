# Interaction continuation — iteration 7: quantified retention and bandwidth dependence

## Typed-channel follow-up

`typed-spin-channels.md` completes the subsequent spin/output audit with 52 exact
checks: conditional normalized typed maps exist, but a spinor copy-algebra
identification and a diagonal-lead multi-object interpretation fail covariance
and kinetic closure respectively. The retained weights below remain internal
preparation results, not physical reaction branching fractions.

## Result

The bound-state overlaps from iteration 6 are now quantitative, with certified
intervals that include the full infinite lead tails. All **22 exact checks** pass.

For normalized states prepared initially in the central system, with the original
unit lead/contact scale:

| Preparation | Total bound-subspace weight, approximately |
|---|---:|
| Native belt character | **7.086039%** |
| Sum of carrier characters | **13.545871%** |
| Difference of carrier characters | **12.081896%** |
| Proton-port character alone | **12.813883%** |
| Electron-port character alone | **12.813883%** |

These are not capture probabilities for incoming lead waves and not probabilities
of photon multiplicities. They quantify the already present bound component of
a specifically prepared internal state.

A second exact control changes the declared environment: scaling lead hopping
and contact strength together by eight removes all above-band bound modes in
the coupled eleven-state space. Therefore retention is conditional on the
lead/contact law, not forced by the annulus topology.

## 1. Fresh inputs

Freshly read `native-port-bound-spectrum.md` and the source-bound joint-generator
and bound-spectrum receipts. All source hashes are checked before calculations.
The preceding five simple bound roots, preparation blocks and rational root
brackets are retained; brackets are refined by exact inertia when necessary.

No coupling or probability is fitted to 372.

## 2. Residue formula with the infinite tails included

For an above-band mode, let

    E(r)=2+r+1/r,  0<r<1,
    M(E)=E I-K-(1+r)P.

The actual state includes tails psi_(j,n)=(-r)^n u_j. Its norm is

    N_full = u* H u + [r^2/(1-r^2)] sum_j h_j |u_j|^2.

For a normalized central port preparation j, the bound spectral weight is the
residue of the diagonal central Green function:

    w_j = h_j |u_j|^2 / N_full.

To calculate this without numerically normalizing a nearly singular eigenvector,
form

    T(r)=r M(E(r)),
    p(r)=det T(r),
    c_j(r)=the jth diagonal cofactor of T(r).

Since (M^-1)_jj=r c_j(r)/p(r), at a simple root

    w_j = (r-1/r) c_j(r)/p'(r).

The derivative includes the lead self-energy dependence. Omitting it would
normalize the central component alone and overestimate the overlap.

An independent scalar control, K=4 with one identical lead, has r=1/3 and
central bound weight 8/9, with tail weight 1/9. The residue formula reproduces
that result exactly, rather than incorrectly assigning weight one.

## 3. Exact polynomials and certified intervals

The symmetric and antisymmetric blocks have dimensions five and six, with two
and one active ports. Expanding the rank-one/rank-two contact determinant gives
univariate polynomials of degrees eight and eleven in r. Their coefficients
are calculated in Q(sqrt(151)); no interpolation or floating root solver is used.

The construction reuses independently verified characteristic/adjugate identities
and checks the resulting determinant and cofactor polynomials against direct
matrix determinants at exact controls.

Interval evaluation encloses the residues over the certified root brackets.
If a derivative interval includes zero, a weight is not certified positive, or
the interval is too wide, the root bracket is refined using exact inertia.
All endpoint arithmetic and ordering remain exact in Q(sqrt(151)).

Readable outward-rounded total probability enclosures are:

| Preparation | Certified enclosing range |
|---|---|
| Belt | [0.0708603897, 0.0708603912] |
| Carrier sum | [0.1354587102, 0.1354587118] |
| Carrier difference | [0.1208189575, 0.1208189603] |
| Either individual carrier | [0.1281388339, 0.1281388360] |

The receipt retains tighter exact algebraic endpoints. Long decimal views in
that receipt are rounded representations; the algebraic endpoints are the
certificate.

## 4. Individual carrier weights and normalization controls

The normalized individual carrier preparation has equal norm weight in the
orthogonal symmetric and antisymmetric sectors. Consequently

    W_proton = W_electron = (W_carrier_sum + W_carrier_difference)/2.

This is a consequence of the preparation decomposition, not an averaging of
unrelated experiments. Each parity sector's bound eigenstates have been
normalized on the full infinite system.

For a bound state, the lead-tail norm fraction is

    [r^2/(1-r^2)] sum_(active ports j) w_j.

It is strictly positive in every certified mode. Dividing w_j by one minus that
fraction gives the incorrectly central-only-normalized overlap; it is strictly
larger than the correct weight. The checker retains both quantities as a loss
control, without treating the latter as a probability certificate.

The total retained weights lie strictly between zero and one. Their bound-energy
contributions also satisfy the spectral budget:

    0 < initial_mean_energy - bound_energy
      < 4 (1-total_bound_weight).

Here the initial mean includes the positive contact shift: it is K_jj+1 for
a central-only preparation in the chosen port basis.

For this finite core coupled to free discrete leads, the central resolvent is
algebraic in the lead square root. Away from its finite set of poles and
thresholds the spectral density is absolutely continuous. The prior audit
excludes embedded and threshold L2 modes in the coupled space. The remaining
weight is therefore the continuum component, not an unidentified missing
probability channel.

## 5. Retained spectral weight is not constant central occupation

The certified W is the norm of projection onto the full bound spectral subspace.
It includes evanescent lead tails and remains constant under autonomous evolution.
It is not the probability of occupying the central coordinates at every time.

Different bound energies accumulate different phases; local probabilities can
oscillate. This does not supply noise protection, a readable register, autonomous
capture or a memory-recovery operation.

An asymptotically incoming propagating state belongs to the scattering subspace.
The static model does not transfer it into an orthogonal bound subspace merely
because the bound states exist. Preparing the localized initial states used
here is a separate operation whose work and control resources have not been
provided by this calculation.

## 6. Exact bandwidth/contact control

Now retain K and scale the lead hopping and positive contact differences together
by t>0. The continuum band becomes [0,4t]. The upper-threshold secular matrix is

    t(4I-2P)-K.

Its negative inertia gives the number of above-band modes. The coefficient
4I-2P is strictly positive, so the bound count cannot increase as t grows.

| Lead/contact scale t | Band | Above-band bound modes |
|---:|---|---:|
| 1/4 | [0,1] | 7 |
| 1/2 | [0,2] | 7 |
| 1 | [0,4] | 5 |
| 2 | [0,8] | 4 |
| 4 | [0,16] | 2 |
| 8 | [0,32] | **0** |
| 16 | [0,64] | **0** |

All table entries are exact inertia results. The threshold matrix is already
positive definite at t=8; monotonicity excludes above-band modes for every t>=8,
not just the two sampled wide bands. Positivity still excludes negative-energy
modes, and the coupled-space cyclicity excludes invisible in-band bound states.

This changes both hopping and contact strength; it is not a pure bandwidth
variation with a fixed contact. Nor does it invalidate the fixed-t=1 theorem.
It demonstrates which supplied environmental assumptions the retention depends on.
Decoupled spectators in the larger retained model are outside this coupled-space
claim and are not erased.

## 7. Implication for the shape-interaction effort

We now have quantitative transport and retention results for a fully specified
conditional port model. But we must not convert those results into a physical
particle interpretation by relabelling states:

- the two carrier ports remain symmetric in this fixture;
- the above-band trapping depends on a finite lead band;
- the channel space still describes one-excitation port waves, not a constructed
  two-/three-object asymptotic configuration space;
- full electron spinor coupling and a physical energy/clock scale remain open.

The next useful gate is the **typed-channel and spin/phase compatibility audit**:
state exactly what Hilbert spaces represent incoming object pairs and two-/three-
object outputs, and test whether the proposed merge/split maps act on the retained
native records with the required symmetries. In particular, the electron's two
edge-seed orbits do not justify identifying its state space with the two-state
Frobenius algebra. Any such identification needs an explicit map and covariance
check before the working reaction ratio can be compared.

A later capture protocol would additionally need admitted time dependence or
energy-exchange channels. The static incoming-scattering result and the internally
prepared bound weights must not be conflated to bypass that obligation.

## Reproduction

```sh
python research/voevodsky/checkers/check_native_port_retained_weights.py
```

Receipt: `results/native_port_retained_weights.json`, with current source hashes,
exact residue polynomials, refined brackets, probability/energy enclosures,
full-tail normalization controls and the bandwidth table.
