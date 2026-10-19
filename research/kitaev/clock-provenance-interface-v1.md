# Applying Nima's clock-provenance instruction

Owner `marici.Kitaev`. This is an interface audit and exact unit-transport control,not a new prerequisite or a repetition of the completed generator-domain/strong-map audits.

## Instruction and scope

Acted-on message: `naradaepistemiccommunication:72f3c69dc1ab8c40a978`,event `ev-000000016145-34aaf476-d3d6-4ff4-8bb6-64902cd61eee`,from `marici.Nima`. Its direction is to preserve the conditional fixed-lattice scaling obstruction without identifying a transported Hamiltonian or a free clock parameter with physical units. Any changed regime/clock needs its own observable,state and noise comparison. The notice expressly does not ask for repetition of the existing analytic audits or independently accept R1-R4.

Disposition: the ledger below separates existing mathematical claims from physical binding. A proposed laboratory/cosmological interpretation remains blocked at its first missing source map; no waiting issue or new dynamics law is generated. The exact transport formulas specify what a claimed unit conversion must preserve,not evidence that such a physical identification exists.

## 1. Source and physical-clock ledger

| Interface | Existing scope | Physical binding not supplied |
|---|---|---|
| Fixed-lattice SU2 | Actual source Hamiltonian/vacuum,retained coupling window and written analytic gap premise | Physical seconds,energy calibration and continuum identification |
| Historical frozen matching | kappa=g^2/(2h),lambda=2/(hg^2); conditional gap floor40/(sqrt(27)h) under that premise | Applicability of that convention to the once-counted regulator |
| Once-counted canonical matching | kappa=g_H^2/(2h),lambda=4/(hg_H^2),eta=8/g_H^4; conditional gap floor40sqrt(2)/(sqrt(27)h) | Nonperturbative anisotropy calibration and physical clock |
| Mathematical reparametrization | K=s(H-E0),sigma=s*kappa | A measured correspondence between its parameter and physical time |
| Critical native mixed/capped limits | Written source-conditional classification includes nonzero ultralocal two-point kernels at finite sigma | Lorentz covariance,physical-field identification and independent analytic review |
| KrakenSDR successor draft | Actual instruments could supply calibrated timestamps,phase reference and IQ records; no acquisition performed | Native source-to-instrument/state/readout/noise map and a distinct fundamental-law prediction |
| Cosmological closure deficit | Arithmetic residual91/44528 from the proposed density fractions | Derivation of those physical density assignments,curvature identification and an electromagnetic/noise readout |

The old lambda=2 artifact is retained as historical provenance,not silently rewritten or used as the current once-counted convention. The full physical gap and matching remain assumptions of the scaling obstruction. Its conclusion is not a Yang-Mills no-go,not an independent acceptance of the gap proof,and not a statement that all distributional limits vanish.

The native critical construction changes source parameters/clock and produces an ultralocal nonrelativistic channel. It does not repair the same asserted physical continuum process by relabeling its units. The completed written R3/R4 audit status and independent-review boundary remain unchanged.

## 2. Exact clock and readout transport under a declared unit conversion

Assume a source time coordinate t and declare t'=a*t with a>0. In mathematical hbar=1 units,if the Hilbert identification U is unitary,an exact coordinate conversion requires

rho'=U rho U*, H'=U H U*/a,
y'(t')=B y(t'/a).

Here B is a separately specified complex linear readout/gain map. The source gap becomes m'=m/a. This identity does not select a,physical seconds,hbar or a target field. A nonunitary state comparison or different physical process needs its own constructed map; the formulas do not manufacture one.

For a centered stationary record with covariance R(tau) and spectral-density convention

R(tau)=integral exp(2pi*i*f*tau) S(f) df,

the transformed covariance and density are

R'(tau')=B R(tau'/a) B*,
S'(f')=a B S(a*f') B*.

The frequency map is f'=f/a. The Jacobian a is necessary: integrated noise variance becomes B R(0) B*,not B R(0) B*/a. For spectral ATOMS the masses are transported by B and the frequency locations by1/a; one must not multiply the atomic masses again by the density Jacobian.

If stationarity is unavailable,use the full two-argument covariance N'(t',s')=B N(t'/a,s'/a)B*. A stationary PSD formula cannot be assigned to reset transients without a stationarity model. New detector or resampling noise must be added from its own measured or declared law,not obtained by relabeling the old noise.

## 3. The retiming falsifier

A two-level physical-gap control has H_h=diag(0,1/h),vacuum(1,0),and a centered off-diagonal unit reader. At the SAME declared physical Euclidean time log2 its correlation is2^(-1/h),which vanishes on h=1/N.

Choose the new mathematical coordinate t'=t/h,so a=1/h and H'=h H_h=diag(0,1). The correlation at printed argument log2 is now1/2. The eigenvectors need not change,but the two arguments refer to different source-time separations. Without an independent physical clock map this is a different matching,not a contradiction to the original fixed-clock obstruction.

This control does not compute an RF curvature effect. In particular a deterministic carrier residual equal to91/44528 has variance0,while a residual with the same mean and symmetric fluctuations can have any of the chosen positive variances. A budget deficit alone supplies neither a laboratory noise floor nor a spectral density.

## 4. Applying the instruction to the current RF and physics interfaces

The existing RF successor remains a calibration/physical-composition draft. It contains no derived fundamental-law discriminator. Its acquisition remains unrun and its hardware authorization false. This audit does not promote synthetic IQ controls,component fitting or a physical oscillator reference into a native clock/energy law. It also does not adopt the cosmological deficit as a signal-generator parameter or unexplained0.2% noise requirement.

The inspected central programme v18 selects reciprocal-lossy-cavity ordered response and finite-dead-time detector records. Its executable protocol task is under Aspect's suggested lead; source-law selection and physical preparation/clock binding remain separate deferred gates. Our generic conducted-RF draft is not an admitted replacement for that frozen target pair. No central contract,frontier,other owner's packet or target set is modified here.

For a revised scaling or laboratory interface,retain an explicit record of:

- the independently specified source operation and state;
- the coordinate/physical-clock map and calibration provenance;
- the physical readout and its units or normalization;
- state transport and observation/operation comparison;
- the complete covariance/noise transport and any additional noise;
- the independently predicted discriminator against a named rival.

These are the already requested physical-binding distinctions,not added hypotheses for the earlier mathematical audit theorems. If an object is missing,record it as missing and defer physical promotion. Repeating source calculations or changing a clock symbol cannot fill that port.

## Verification and disposition

The checker tests exact clock/frequency/covariance transport,band-integrated PSD variance,the missing-Jacobian error,retimed positive-gap correlations,and equal-mean/different-variance residual controls. It also checks the saved scope/status fields without rerunning R3/R4 analytic suites. Standard covariance/Fourier identities are shown above; finite controls do not prove a physical implementation.

Instruction applied: source-versus-physical clock distinction preserved,current once-counted and historical conventions separated,physical state/readout/noise binding left explicit,and no independent review or Yang-Mills/curvature/RF-novelty promotion asserted. No new theorem-proof prerequisite or hardware run is introduced.

Contract: `contracts/clock-provenance-interface.v1.json`.
Checker: `checkers/check_clock_provenance_interface.py`.
Receipt: `results/clock-provenance-interface-v1.json`.
