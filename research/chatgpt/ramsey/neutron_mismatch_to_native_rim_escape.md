# Neutron mismatch to native rim escape

Research continuation, 2026-11-01. All numerical energies, pulse areas and contact coefficients below are model quantities, not physical calibration.

## Result

The existing *static two-collective-rim contact* cannot emit the neutron sector-contrast precursor: its outgoing ports average over three sectors and annihilate their disagreement. The source's aligned native subspace is invariant, so subsequent evolution under that contact cannot make the missing coupling appear.

An already defined **addressed native-rim/source-bank pulse** does remove this obstruction. One such pulse transfers some of the contrast into a collective rim direction. The source's autonomous contact then has a calculable continuum escape fraction for that direction. Under its pre-existing illustrative parameters, a normalized collective-rim excitation has escape weight approximately **0.780828766716158**, with the remaining weight in two localized bound levels.

For a pi pulse at the same sector as the missing input, **0.0406034827533065 of the isolated contrast norm** escapes; at either other sector the fraction is **0.0101508706883266**. This four-to-one location dependence follows from the source geometry and three-sector contrast vector. These are not neutron-decay probabilities, and component norms cannot be added as independent branches when the common and contrast parts interfere in the outgoing field.

The selected pulse and contact operators therefore provide an explicit conditional escape route without inserting a new product-routing probability. They do not select a spontaneous failure event, pulse activation, or beta-decay product identities.

## 1. Inputs and source boundary

This audit reads the attached prior construction and reuses only the pure `geometry()` function in its `local_input_successor_audit.py`. The copied file is unmodified. It reconstructs the native 36-coordinate field, three selected sector modes, and twelve input weights. Its original source-binding qualifications remain in force.

Fresh repository sources inspected through the GitHub connection:

- `research/strominger/neutron-autonomous-rim-scattering.md` and `checkers/check_neutron_autonomous_rim_scattering.py`.
- `research/strominger/neutron-two-rim-contact-binding.md` and `checkers/check_neutron_two_rim_contact_binding.py`.
- `research/strominger/neutron-canonical-occupied-closure.md`.
- `research/strominger/checkers/check_neutron_seam_control_transport.py`.
- `research/strominger/encoder-single-residual-pulse-v1.md`, as a control against treating a chosen polar map as an automatically implemented pulse.

The two-rim checker gives exact rational even/odd response functions. They determine a five-dimensional minimal accessible spectral realization, which was reconstructed here. Its scattering values and bound-state energies match the source's reported values. The source's remaining 19 directions are retained in the reasoning as its dark complement; they were not re-created by silently declaring a 5D space to be the entire neutron.

This is **not** a fresh replay of the entire 24D source matrix producer, stored dependency hashes, or all prerequisite suites. The source code's exact invariant-subspace identities are reused. No repository files, production admission rules, or source parameters were changed.

## 2. Native rim channels and exact darkness

Write the selected local field as

    u = a tensor v,     a=(1,1,1)/sqrt(3),     v†v=1.

Let Q be the two-column orthonormal basis of vectors orthogonal to a. The contrast frame is

    Cframe = Q tensor v.

Each sector has six triangle modes. The source's two rim triangles occupy positions 1 and 4 within that six-triangle sector. Its collective rim columns have support

    lower: 1,7,13
    upper: 4,10,16

in the 18-triangle coefficient chart. Each column inserts equal amplitudes at its three positions. In whitened coordinates, let f_(h,s) be the unit local rim mode, with h the rim and s the sector. Then

    W_h = (f_(h,0)+f_(h,1)+f_(h,2))/sqrt(3).

The exact weight of each rim triangle within a unit sector mode is

    rho = 2099/8970.

It follows directly that

    W† Cframe = 0,
    W† u = sqrt(rho) (1,1).

Thus the contact sees the common neutron mode, not the contrast. The unchanged neutron is not automatically dark to this contact.

The source checker supplies a six-dimensional native aligned subspace A: each of the six triangle coefficients is repeated across the three sectors. It checks that the self-adjoint core K leaves A invariant and that both W columns lie in A. Therefore A-perpendicular is invariant as well. The contact adds terms only through W and cannot couple a state in A-perpendicular to its leads.

This proves, for empty incoming leads and the static source contact,

    lead_readout exp(-it H_static) (contrast,0) = 0

for every time. No small-coupling or short-time approximation is needed.

For a clean input-loss precursor y=(1-r/3)u+c, the lead amplitude without another operation is simply (1-r/3) times the no-fault preparation's lead amplitude. The contrast c does not create a new outgoing channel.

The source's static bank block is zero and lacks direct lead attachment. The previous abstract completion record is not automatically the same object as this bank: its binding and rotation-frame controller still require specification.

## 3. A source-supplied operation that makes contrast visible

The canonical source defines an addressed pulse between a normalized rim mode f and a normalized bank feature b. Their native and bank sectors are orthogonal. Its projector and evolution are

    d=f-b,
    P=d d†/2,
    U(theta)=I+(exp(-i theta)-1)P.

For theta=pi, U=I-2P exchanges the addressed amplitudes. This is a retained source operation, not a projector invented to force a decay product.

On a contrast state c with initially empty bank, the native component after the pi pulse is

    c' = c-f(f†c).

Because W†c=0 and W_h†f_(h,s)=1/sqrt(3), its newly visible amplitude is

    W†c' = -e_h (f†c)/sqrt(3).

It lies exactly along one collective rim column, hence within the source's accessible core subspace. Other components remain in the native dark subspace and bank. A single addressed pulse breaks the averaging cancellation; the static symmetric contact alone does not.

For general pulse area the visible squared norm is multiplied by sin²(theta/2).

One-pulse calculation scope: every bank feature has norm one, and starts empty, so its nonorthogonal Gram relations with *other* bank features do not enter. The computation does not replace the full bank by one mode for arbitrary multi-pulse histories.

The same addressed pulse acts nontrivially on the intact neutron. The source does not yet specify that a missing-input record, rather than an external schedule, activates it. This is a real remaining distinction between a conditional escape calculation and spontaneous decay.

## 4. Exact accessible contact reconstruction

Let z be the complex spectral variable. In normalized even/odd rim coordinates, the source core resolvent is diagonal, with entries

    g_even(z) = (z-2099/3292) / (z²-(4485/3292)z),

    g_odd(z) = (z²-(5391/1646)z+23644249/10837264)
               / (z³-4z²+(44361887/10837264)z-6431463/10837264).

These are `-R(-z)` in the source's positive-x convention. Their poles and positive residues give a five-state diagonal realization and normalized contact columns. Each parity's residues sum to one.

The reconstructed isolated core poles are approximately

    0, 1.36239368165;
    0.17293863106, 1.43395978071, 2.39310158823.

The semicolon separates the parity channels. This minimal realization reproduces the complete two-port source response; the construction does not fit a pole or a gap.

The source's positive continuum form retains both contact diagonal terms:

    E = integral [kappa |psi'|² + Delta |psi|²] dx
        + chi†Kchi + g_c |sqrt(ell)psi(0)-W†chi|².

Here g_c denotes the source contact strength called `eta` in its code. It is distinct from the previous arbitrary product-routing fraction. We retain the existing fixture

    kappa=1, g_c=2, ell=1, Delta=1/2, hbar=1.

For k(z)=sqrt((z-Delta)/kappa), with the outgoing resolvent branch, eliminating the leads gives

    s(z) = g_c (2i kappa k)/(2i kappa k-g_c ell),
    G_parity(z) = g_parity(z)/(1-s(z)g_parity(z)).

Below threshold, k=iq and s=g_c (2kappa q)/(2kappa q+g_c ell), reproducing the source's positive bound-state Schur equation. Above threshold, the spectral density is

    density(E) = -Im G_parity(E+i0)/pi.

This derives the escape fraction from the existing dynamics rather than assigning a transition probability.

## 5. Bound weight and continuum escape

There is one accessible bound state in each parity channel below Delta. The source already supplies the two-level count; the reconstructed bound roots, normalized exterior tails, and the continuum mass provide independent checks within the same accessible response.

| Parity | Bound energy | Bound weight of unit parity-rim input | Continuum weight |
|---|---:|---:|---:|
| Even | 0.239564867091772 | 0.209387776292597 | 0.790612223707403 |
| Odd | 0.406258480175608 | 0.228954690275087 | 0.771045309724913 |

A unit lower-rim or upper-rim state has equal parity weights, so its continuum mass is

    chi_escape = 1-(Z_even+Z_odd)/2
               = 0.780828766716157897...

The bound weights are resolvent residues, not merely the bound states' total core norms. An independent core-plus-exterior normalization gives the same overlaps. Direct integration of the positive continuum density also gives `continuum+bound=1` in both channels.

In this finite-rank continuum contact, that absolutely continuous component disperses away; the bound component remains localized. A transient change of core occupation alone was not counted as escape. Numerical values are evaluated to high precision, but are not interval-certified physical uncertainties.

The existing scattering benchmark was also reproduced:

| E | Reflection | Transmission | Other-rim flux |
|---|---:|---:|---:|
| 0.80 | 0.74557149 | 0.25442851 | 0.14092687 |
| 1.13 | 0.14680813 | 0.85319187 | 0.02788415 |
| 2.00 | 0.42103017 | 0.57896983 | 0.01336435 |
| 3.00 | 0.99806464 | 0.00193536 | 0.00283262 |

Flux conservation was checked on the source's 201-energy grid. No incoming scattering state was confused with permanent capture into a bound state; the escape calculation instead uses a prepared core-rim excitation and its spectral measure.

## 6. Fault location and the four-to-one test

For input weight r_j omitted in sector s,

    c = -(r_j/sqrt(3)) (e_s-a/sqrt(3)) tensor v,
    ||c||² = 2r_j²/9.

Address a rim site in sector t. The exact new collective-rim squared norm is

    b² = rho r_j² (3 delta_(s,t)-1)² /81.

The escaping squared norm contributed by that isolated contrast component is

    q_escape = chi_escape sin²(theta/2) b².

For a pi pulse, its fraction of the original contrast norm is

    same sector:  chi_escape (2rho/9) = 0.0406034827533065,
    other sector: chi_escape (rho/18) = 0.0101508706883266.

Both rims give the same result by parity symmetry. The ratio is exactly four. All 36 whole-input faults against all six addressed rim sites were checked: 216 fault/site combinations, plus continuous-area controls. Matching-sector escape norm relative to the original unit field ranges from about 6.14e-7 to 4.60e-4 over the inherited four weight classes.

These component calculations cannot be silently added to common-mode escape: applying the pulse to the full faulty state can make common and contrast amplitudes interfere in the same outgoing field. A physically retained distinction, or the complete coherent state calculation, is required for probabilistic branch accounting.

## 7. Four record directions fit phase-resolved rim ports, but the existing contact omits them

The six individual rim sites carry two invariant averages and four nonuniform directions. In cap-by-sector ordering, a fixed isometry from two contrast records into these six sites is

    F4 = (1/sqrt(2)) [[Q,Q],[Q,-Q]].

The first record uses equal lower/upper contrast and the second uses opposite lower/upper contrast. F4†F4=I4, it intertwines the actual threefold sector cycle, and both collective averages annihilate it.

This supplies representation capacity for the earlier two-valued history label in existing rim-position degrees of freedom. It does **not** establish that the source bank actually transfers into those combinations or that a six-phase-resolved lead contact is already the source production law. The inspected contact has only two collective ports. No replacement contact was inserted into the calculations above.

## 8. What remains for decay

The now concrete source-level candidate is an input-loss record followed by an addressed native rim/bank operation, followed by the existing autonomous outgoing contact. The failure alone and the unchanged symmetric contact give zero contrast escape. The addressed operation makes a definite part visible, and its subsequent escape is computable.

Three essential identifications remain absent: which native rule triggers that addressed operation on the retained fault record; how the combined pulse and contact account for energy without an externally supplied intervention; and how the escaping same-particle internal/rim field becomes the joint proton-electron-antineutrino state with neutron occupation retired. Neither source geometry nor the new spectral calculation selects those automatically.

No microscopic error probability, Planck period, measured lifetime, physical mass difference, or weak coupling was fitted. The output is a conditional escape mechanism inside a supplied dynamical model, not a derived neutron lifetime.

## Reproduction

Python 3.10+, NumPy, SciPy and mpmath:

    python escape_audit.py

The script imports only the included pure geometry constructor. It writes `results.json` and `fault_site_census.json`. `run.log` records the completed run. `sources.json` provides source URLs, operation formulas and scope. Maximum linear-algebra residual in the completed calculation is below 2.6e-15; continuum quadrature error estimates are approximately 1.4e-11 and 6.7e-11. Exact identities, numerical residuals and physical interpretation are kept separate.
