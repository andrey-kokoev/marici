# KrakenSDR conducted-RF route-residue experiment

## Question

Can a calibrated conducted-RF apparatus implement the finite shell modulation

\[
D_t(e)=t^{j(e)}
\]

and retain enough coherent response to detect the declared finite cycle sector after a fixed common-history readout?

## Claim boundary

A passing experiment establishes an engineered finite-cutoff realization: arithmetic shell and edge labels are deliberately compiled into RF tones and codes, the apparatus transfer is measured, and a preregistered detector reconstructs the response. Conditional distinguishability through a compatible faithful probe is already a categorical consequence and is not an experimental hypothesis here. The experiment tests construction, calibration, compatibility, and finite sensitivity of one probe. It does not establish that an independently occurring physical system naturally assigns arithmetic shells to RF modes. It does not establish the completed countable theorem experimentally. The identifier `history` in inherited operator names denotes a coarse composition readout and carries no temporal meaning. The mathematical target and the stronger physical gates are recorded in:

- `a_countable_shell_generating_family_detects_the_completed_cycle_residue_20260912.md`;
- `optical_attenuation_can_realize_the_shell_probe_only_after_a_label_mode_embedding_20260912.md`;
- `route_residue_optical_probe_acceptance_protocol_20260912.md`.

## Apparatus

Record manufacturer, model, serial number, firmware, calibration date, connector type, and measured impedance behavior for every active instrument and passive component.

The intended apparatus is:

- existing five-channel phase-coherent KrakenSDR receiver;
- Siglent SDG2042X dual-channel 40 MHz arbitrary waveform generator;
- Rigol DHO924 four-channel 250 MHz 12-bit oscilloscope;
- NanoVNA V2 Plus4 with open, short, load, and thru standards;
- TOJOIN PS-8SM-00510 eight-way 50-ohm SMA divider, nominally 5 MHz--1 GHz;
- six matched SMA-male-to-SMA-male RG316 cables;
- one BNC-to-SMA cable pair;
- one SMA DC block;
- one source-side 30 dB fixed attenuator and one spare;
- six matched 10 dB fixed attenuators;
- at least seven ordinary 50-ohm SMA male loads for divider characterization;
- two 50-ohm BNC feed-through terminations.

The NanoVNA calibration-standard load is not an ordinary divider termination.

## Conducted topology

No antenna or over-the-air transmission is used.

```text
SDG2042X channel 1
  |
BNC-to-SMA cable
  |
DC block
  |
30 dB source attenuator
  |
TOJOIN eight-way divider
  |-- 10 dB -- matched cable -- Kraken channel 0, in-run reference
  |-- 10 dB -- matched cable -- Kraken channel 1
  |-- 10 dB -- matched cable -- Kraken channel 2
  |-- 10 dB -- matched cable -- Kraken channel 3
  |-- 10 dB -- matched cable -- Kraken channel 4
  |-- 50-ohm load
  |-- 50-ohm load
  `-- 50-ohm load
```

The NanoVNA replaces the source and receiver temporarily during passive calibration. The oscilloscope observes the generator-side waveform through a properly terminated input; it is not placed across two driven outputs.

## Safety gate

Before connection, read the current SDG2042X, DHO924, NanoVNA, and KrakenSDR manuals and record their port limits. Power down before changing the passive network. Begin at the lowest useful SDG amplitude with the 30 dB source pad and all five 10 dB receiver pads installed. Disable receiver AGC and any bias supply. Verify absence of unintended DC before connecting the KrakenSDR. Never connect an SDG output to a NanoVNA source port or another active output.

No acquisition proceeds until the calculated worst-case level at each Kraken input lies below its documented maximum with a recorded margin. Nominal attenuator and splitter labels are not a substitute for this link-budget check.

## Frozen finite mathematical packet

Before discriminating acquisition, freeze:

1. integer cutoff and vertex ordering;
2. ordered edge list;
3. incidence matrix \(\partial\);
4. shell map \(j(e)\geq1\);
5. exact cycle basis \(F\);
6. common-history matrix \(C\);
7. source-vector normalization;
8. RF mode and edge-code assignment;
9. probe settings and acquisition order;
10. uncertainty construction and acceptance rules.

Start with the smallest packet containing the exact four-edge rectangle and three consecutive-prime shells. Add larger packets only as separate preregistered runs.

Use the generating-family settings

\[
t_n=\frac12+\frac1{n+3}.
\]

For the first pilot use \(n=0,1,2,3\), hence

\[
(t_0,t_1,t_2,t_3)=
\left(\frac56,\frac34,\frac7{10},\frac23\right),
\]

plus the unmodulated control \(t=1\). Do not renormalize total emitted power separately at each setting: the missing power is part of the measured attenuation effect.

## RF encoding map

Choose a carrier \(f_c\) only after receiver and generator preflight. The expected initial region is approximately 25--35 MHz. Place all shell tones inside one alias-safe KrakenSDR capture band; the generator's 40 MHz ceiling does not imply that the receiver captures a 40 MHz instantaneous span.

Assign each shell \(j\) a distinct tone \(f_j\). Distinct edges in the same shell require distinct preregistered orthogonal codes or separate fixed slots. The finite source embedding is therefore

\[
\iota:e\longmapsto(f_{j(e)},c_e),
\]

not merely \(e\mapsto f_{j(e)}\). Verify code orthogonality through the measured Gram matrix. If edge recovery is sequential, the order and linear synthesis rule are frozen before cycle data are taken.

At setting \(t\), the programmed coefficient of edge \(e\) is multiplied by \(t^{j(e)}\). A fixed global amplitude factor keeps the largest waveform within the linear source range. Crest-factor management may rescale the entire frozen packet once; setting-dependent normalization is prohibited.

## Calibration phase

Calibration data may be used to choose a clean carrier band and safe source level. It may not be used to change the frozen shell assignment or detector after discriminating cycle data are inspected.

### NanoVNA SOLT calibration

Perform full open-short-load-thru calibration at the cable reference planes. Save the calibration state and raw verification traces. Verify the thru and load after calibration and record the residual magnitude and phase errors.

### Component measurements

Measure complex \(S_{21}\), return loss, and repeatability for:

- DC block;
- each source and receiver attenuator;
- every matched cable;
- each complete cable-plus-attenuator receiver path.

For divider output \(k\), connect NanoVNA port 1 to the divider input and port 2 to output \(k\); terminate the other seven outputs. Repeat for all eight outputs. Measure relevant output-to-output isolation with the input and every unused output terminated. Repeat critical traces after disconnecting and reconnecting the cables.

Amplitude or phase imbalance is calibratable. An unstable notch, materially inadequate isolation, source-level dependence, or reconnection drift larger than the propagated response margin rejects the component.

### Generator characterization

With a 50-ohm oscilloscope termination, inspect single-tone and multitone waveforms before the protection chain. Record clipping, settling, amplitude, and phase. Sweep at least three source levels through the assembled passive network. The inferred normalized transfer must agree within its preregistered uncertainty; otherwise the operating level is nonlinear and rejected.

### End-to-end basis calibration

Inject each shell-tone/edge-code basis vector separately. Record raw IQ on all Kraken channels with fixed gain and sample configuration. Estimate the complete complex basis-response matrix, cross-talk, channel phase offsets, and demodulation Gram matrix. Freeze the detector map from these basis runs before reading cycle trials.

## Acquisition phase

Record raw coherent IQ rather than only FFT magnitudes. For every run retain:

- UTC acquisition time;
- instrument settings and firmware;
- source waveform digest;
- mathematical-packet digest;
- sample rate, center frequency, gain, and channel ordering;
- run order and setting label;
- temperature or available environmental readings;
- raw-file digest;
- overload, dropped-sample, and synchronization indicators.

Acquire the following blocks in randomized order:

1. all inputs terminated for receiver-noise measurement;
2. source-off assembled-network measurement;
3. single basis vectors;
4. unmodulated \(t=1\) packet;
5. every declared \(t_n\) packet;
6. zero-cycle control;
7. exact four-edge rectangle with unmodulated history cancellation;
8. modulated rectangle with predicted nonzero response;
9. injected synthetic blind direction;
10. repeated source levels for linearity;
11. repeated initial block at closeout for drift.

A short non-discriminating pilot determines acquisition length and repetition count from observed variance. Freeze both quantities before the cycle trials. Preserve failed and overloaded trials with status flags; do not silently delete them.

## Detector and transfer reconstruction

Demodulate by the frozen tone/code basis. Let \(x\) be the recovered edge-coordinate vector and let \(\widetilde C\) be the fixed calibrated instrument detector. The detector pullback test is

\[
\|\widetilde C\iota-C\|\leq\varepsilon_C.
\]

At each setting estimate the complex apparatus transfer \(M_n\). Test

\[
\|M_n\iota-\iota D_{t_n}\|
\leq\varepsilon_{M,n}.
\]

The error bounds include NanoVNA verification residuals, reconnection variation, generator nonlinearity, demodulation conditioning, channel drift, finite samples, and repeatability. Dimensional agreement is not evidence for either intertwining equation.

## RF loss accounting

The RF experiment uses calibrated power flow rather than photon-count no-detection events. Record incident, reflected when measured, transmitted, delivered, and terminated-port power in declared units. The residual dissipated or unobserved power and its uncertainty form the RF loss channel. Do not normalize surviving output power to unity.

A two-port NanoVNA does not by itself reconstruct an unrestricted nine-port scattering matrix. The stated loss result is conditional on the measured terminated configuration and its load uncertainties.

## Noise and robust residue certificate

From repeated blocks estimate the joint covariance \(N\) of the stacked complex readouts across channels and probe settings. Retain correlations caused by the common source, shared reference, block order, and drift. State the regularization rule before inversion; a singular or poorly conditioned covariance is a residual, not permission to discard a mode.

For the frozen cycle basis form the measured stacked differential response

\[
\widehat R=
\begin{pmatrix}
\widehat R_0F\\
\widehat R_1F\\
\vdots
\end{pmatrix}.
\]

Propagate a validated operator error bound \(\eta_R\). The finite cycle sector is robustly detected only if

\[
\sigma_{\min}(\widehat R)>\eta_R.
\]

When \(N\) is positive and invertible on the response range, report

\[
Q=\widehat R^*N^{-1}\widehat R
\]

with a confidence-bounded smallest eigenvalue. This is an apparatus response or Fisher form. It is not promoted to a natural physical cycle covariance.

## Required falsifiers

The analysis must demonstrate all of the following:

- the zero-cycle control is compatible with zero within uncertainty;
- the unmodulated rectangle history cancels;
- the modulated rectangle has the preregistered nonzero response;
- the injected blind direction fails the robust singular-value gate;
- deleting the loss residual fails power normalization;
- inflating \(\eta_R\) beyond the measured singular margin reverses acceptance;
- permuting the frozen shell labels breaks the intended intertwining unless the same permutation is transported through every typed map.

A checker defect, dropped channel, saturation, synchronization loss, or malformed raw record is an execution defect and requires repair and repetition. It is not scientific evidence against the mathematical probe.

## Decision table

- All calibration, intertwining, detector, loss, linearity, noise, and robust-injectivity gates pass: admit engineered finite-cutoff RF measurability.
- Transfer passes but detector pullback fails: modulation was realized, common-history coupling was not.
- Detector passes but robust injectivity fails: retain the detected null or unresolved direction.
- Power normalization fails: no response or Fisher form is admitted.
- Only software-generated or synthetic controls pass: pipeline validation only, with no physical promotion.

## Data layout

Store raw acquisitions outside Git in an ignored run directory. Commit only bounded manifests, analysis code, packet definitions, and results summaries. One run manifest records exact commands, software and firmware versions, source and input digests, start and end times, output paths, expected schemas, and exit status. Prefer SigMF-compatible metadata for raw IQ, plus a separate immutable JSON file for apparatus calibration and mathematical packet identity.

## Disposition

The purchased apparatus is sufficient for the conducted finite-cutoff experiment once delivered and individually accepted. The first executable action is inventory and port-safety verification, followed by NanoVNA calibration and passive-network characterization. No cycle trial is admissible before the finite mathematical packet and uncertainty construction are frozen.
