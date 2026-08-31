# Aspect instrument registry

## Question

Which concrete instruments are already modeled, how are they organized, and which metadata are still missing before they can be compared through the SCC Instrument Profile Lattice?

## Claim boundary

This registry records mathematical models, bounded audits, conditional designs, and executable simulations. The 49-packet optics laboratory index is the portfolio inventory; the machine registry currently contains twenty-four named instruments whose operational topology is explicit.

## Families

| Family | Capability boundary |
|---|---|
| Sequential polarization and Bell | Conditional continuation, disturbance, context comparison, no-signalling |
| Route interferometry | Path coherence, closure, erasure, phase, and dark terminals |
| Cavity and control | Storage, delay, feedback, transfer zeros, and controller interfaces |
| Detection and tomography | Counting, quadratures, determinants, loss, scale, and detector memory |
| Bath and thermal | Unitary dilation, noise completion, detailed balance, and KMS coherence |
| Timing and acquisition | Anti-aliasing, event matching, calibration epochs, and raw-record binding |
| Cross-sector compilers | Source-bound optical realization and criticism of non-optical constructors |

## Initial canonical instrument set

| Instrument | Family | Interaction Net topology | Model status |
|---|---|---|---|
| Three-polarizer Z-X-Z | Sequential polarization | Open continuation path | Exact finite model |
| Bell plus sequential analyzer | Sequential polarization | Context cover without global gluing | Exact finite model |
| X-state determinant | Detection and tomography | Multi-setting terminal evaluator | Exact finite model |
| Amplitude-damping crossing | Detection and tomography | Parameter-bracketing path | Exact finite model |
| Lossy photodetection | Detection and tomography | Loss dilation followed by record | Exact finite model |
| Dead-time photodetection | Detection and tomography | Memory-state continuation | Exact finite model |
| Six-port scale identification | Detection and tomography | Six-port comparison mesh | Exact finite model |
| Global-unit dark-port correlation | Route interferometry | Global closure with dark terminal | Bounded audit |
| Magneto-optic loss dilation | Bath and thermal | Two-channel system-bath dilation | Exact finite model |
| Thermal sideband balance | Bath and thermal | Paired-sideband evaluator | Exact finite model |
| Multifrequency KMS | Bath and thermal | Multifrequency coherence mesh | Bounded audit |
| Dual-clock anti-alias | Timing and acquisition | Two-clock comparison | Exact finite model |
| Two-frontier build audit | Cross-sector compiler | Two-frontier comparison | Bounded audit |
| Archimedean Tate-area | Cross-sector compiler | Infinitesimal comparison cell | Conditional design |
| 3-2-1 spin-two output | Cross-sector compiler | Graded output tree | Conditional design |
| Minimal two-path interferometer | Route interferometry | Coherent route recombination | Exact finite model |
| Polarization marker and quantum eraser | Route interferometry | Conditional marker/eraser branching | Exact finite model |
| Reciprocal lossy cavity | Cavity and control | Ordered feedback loop with loss dilation | Exact finite model |
| Free propagation and Green transfer | Route interferometry | Ordered propagation and Green inversion | Exact finite model |
| Selected-channel transmission zero | Cavity and control | Dark selected channel with complementary tomography | Exact finite model |
| Nonreciprocal polarization scattering | Route interferometry | Forward/reverse Jones scattering with loss dilation | Exact finite model |
| Calibrated homodyne and heterodyne | Detection and tomography | Phase-referenced balanced detection | Exact finite model |
| Calibrated photon counting | Detection and tomography | Loss and dark count before count record | Exact finite model |
| Finite-bandwidth completion audit | Timing and acquisition | Finite-to-continuum completion gate | Exact finite model |

## Three-polarizer reference instrument

The sequence Z-X-Z is represented by three composable instruments, not three terminal effects. The first Z record selects a continuation, X disturbs that continuation, and the final Z reads the resulting branch. The exact model gives unit repeat probability for Z-Z and one-half return probability for Z-X-Z. Its nine-factor matrix is complete except for physical authority, which requires bound polarizer settings, calibration, detector records, and an execution artifact.

## Distinct statuses

`model_status` records whether a mathematical instrument is exact, audited, or conditional. `simulation_status` records execution of the linked mathematical fixture, and `simulation_receipt` identifies its persisted result. `profile_status` independently records execution of the SCC Instrument Profile Lattice classifier.

Every factor matrix is evaluated relative to an `assessment_regime` with five
coordinates: scale, truncation, access, calibration, and physical binding.
Every `partial` or `open` cell carries one or more typed residual reasons.
Regime is a base coordinate for evaluating the nine factors, not a tenth
source factor.

## Current residual

The repository has more instrument packets than canonical registry entries. The present registry deliberately exposes rather than hides three metadata gaps:

1. all twenty-four instruments have complete scoped nine-factor matrices;
2. all twenty-four entries have explicit checker/result links in the registry;
3. no canonical instrument has yet received a checked SCC Instrument Profile assignment.

## Executed SCC profiles

Profiles are executed only relative to the recorded assessment regime; factor
completeness does not assign them automatically. `checked` means that the
linked model result passes and every claimed classifier dimension satisfies
the executable scoped predicate in `check_instrument_profiles.py`.

| Instrument | Scale | Carrier | Action | Observation | Estimate |
|---|---|---|---|---|---|
| Three-polarizer Z-X-Z | finite system | compatible | typed | natural | uniform |
| X-state determinant | finite system | compatible | typed | faithful | bounded |
| Lossy photodetection | finite system | compatible | typed | natural | uniform |
| Dead-time photodetection | finite system | compatible | typed | natural | uniform |
| Thermal sideband balance | finite system | compatible | typed | faithful | uniform |
| Multifrequency KMS | packet | compatible | typed | natural | uniform |
| Amplitude-damping crossing | finite system | compatible | typed | faithful | bounded |
| Magneto-optic loss dilation | finite system | compatible | typed | natural | uniform |
| Dual-clock anti-alias | finite system | compatible | typed | faithful | uniform |
| Bell plus sequential analyzer | finite system | split | typed | natural | uniform |
| Six-port scale identification | finite system | compatible | typed | faithful | uniform |
| Global-unit dark port | packet | split | typed | faithful | bounded |
| Two-frontier build audit | packet | split | typed | natural | bounded |
| Archimedean Tate area | local | split | typed | faithful | bounded |
| 3-2-1 spin-two output | finite system | split | typed | natural | bounded |
| Minimal two-path interferometer | finite system | compatible | typed | natural | uniform |
| Polarization marker and quantum eraser | finite system | compatible | typed | natural | uniform |
| Reciprocal lossy cavity | finite system | compatible | typed | natural | uniform |
| Free propagation and Green transfer | finite system | compatible | typed | natural | uniform |
| Selected-channel transmission zero | finite system | compatible | typed | faithful | uniform |
| Nonreciprocal polarization scattering | finite system | compatible | typed | natural | uniform |
| Calibrated homodyne and heterodyne | finite system | compatible | typed | faithful | uniform |
| Calibrated photon counting | finite system | compatible | typed | natural | uniform |
| Finite-bandwidth completion audit | packet | split | typed | natural | uniform |

The first and third instruments deliberately collide in the classifier while
remaining different instruments: one transports polarization continuations,
whereas the other is a destructive phase-blind detector. This is a direct
registry example of the SCC projection being many-to-one.

Expansion should promote packets from the 49-item portfolio only after adding topology, status, readout, first open gate, checker/result links, and—when justified—a nine-factor matrix and SCC profile.

## Durable verification

- Portfolio: `research/aspect/optics-integrating-laboratory-index.md`
- Contract: `research/aspect/contracts/instrument-registry.v1.json`
- Checker: `research/aspect/checkers/check_instrument_registry.py`
- Result: `research/aspect/results/instrument_registry.json`
