# A readable clock in the retained native phase records

## Question and claim boundary

Can changes of the existing arrow-related phase records supply a clock reading without consulting an external elapsed-time value?

We reuse the original twenty-coordinate pentachoron operator `H=L_original+cycle_X` serialized in the supplied high-energy archive. No geometry, coupling, clock degree of freedom, or supplier execution is added. A positive-control **preparation** is added and is identified explicitly. This is a finite internal-clock reading on a previously declared native orbit, not a derivation of physical time or its inevitable processing rule.

## Frozen conjecture and falsifier

- **Problem:** construct a state-readable internal change rather than rename an external parameter.
- **Bold conjecture:** the actual incoming lowest-mode mixture already supplies a clock because it has positive energy.
- **Rivals:** a stationary mixture has no internal change; common phase is mistaken for time; a fabricated phase path does not match the native generator.
- **Risky consequences:** the source incoming density changes; a coherent control on source modes has measurable relative-phase quadratures; native populations are reconstructible from them without an external time argument.
- **Strongest falsifier:** test stationarity of the actual source input; require native-generator compatibility and offset/common-phase invariance for any control.
- **Disposition:** the source-input clock conjecture fails. A separately prepared coherent control supplies a conditional phase reading.

The [preregistration](C:/Users/andrey/src/marici/research/strominger/inputs/native-relational-clock-freeze.json) remained unchanged. The completed standard-library implementation was frozen before execution with fingerprint `c3d40c51ec6d7448455aa1eaa23f8ef00304a0a060e12cefdb4e03e3c7140a75`.

## Actual source input: energy without a clock

The inherited original ground energy is approximately `1.932476268466936`, with a four-dimensional ground eigenspace. The incoming equal mixture is its normalized projector, `rho_in=P_ground/4`.

It commutes with H. Therefore it has no distinguishable free internal evolution. Positive energy and persistent records alone do not supply a ticking clock. A common phase cannot change its density or its internal observables.

This statement is about the internal phase record in the declared free model, not the entire moving scattering packet: the latter also has a coherent distribution of radial energies and can change during an encounter.

## A control constructed from the same source records

Project the existing raw source coordinate zero into the ground and first excited eigenspaces. Normalize these projections to obtain g and e; then prepare an equal coherent superposition.

Both projection weights are approximately `1/5`. The first two native energies differ by approximately `2.236067977499784`, consistent with the retained source gap `sqrt(5)`.

Keep the state in the form

    psi(theta) = [g + exp(-i theta) e]/sqrt(2).

This is not assumed to be the source's actual beam preparation. It is a new preparation using its existing coordinates and operator.

### Read phase from relationships, not from t

Construct the two quadratures of

    Gamma = 2 Tr(rho |g><e|).

They recover `cos(theta)` and `-sin(theta)`. Thus the relative phase is read from the state itself. It is invariant under a common phase and under a common additive energy offset.

Every native coordinate population follows directly:

    |psi_j|^2 = (|g_j|^2+|e_j|^2)/2
                + Re(conj(g_j) e_j exp(-i theta)).

No external elapsed-time value enters that reconstruction. The addressed coordinate's population ranges between approximately zero and `0.4` while total norm and mean native energy remain constant.

The phase path is not an arbitrary incompatible rotation. Direct matrix checks establish

    d psi/d theta = -i (H-E_ground I) psi / gap.

It is the native orbit with its unobservable common phase removed. This establishes an internal reading of that orbit; it does not explain why source processing chooses to traverse it.

### History remains necessary

After one relative-phase revolution the entire state endpoint returns, while retained oriented phase history advances by a revolution. An endpoint alone cannot determine elapsed cycles.

The test reconstructs two turns from sufficiently closely spaced phase records. The sampling and direction are declared controls. Neither monotone advancement nor its selection by the two-cycle assembly has been derived.

### Strong negative control

Erase coherence between g and e while retaining the same energy-sector populations. The resulting mixture has the same mean energy and energy distribution, but commutes with H and loses the clock quadratures.

Therefore a count or even an energy distribution is not enough for this clock: the changing **phase relationships** are essential.

## What advances—and what remains

We have constructed a conditional phase-clock reading from retained source records, and shown that the actual stationary input does not already provide it.

To get **time emerging from arrow processing**, rather than merely read a clock on an admitted orbit, the next obligation is specific: show that the actual two-cycle operation creates/preserves the required relative coherence and advances its retained phase history. Then compare a local reading with a reading of the whole configuration using the same operation. No inverse-density law, physical seconds, time dilation or Einstein law follows from the present test.

## Verification and provenance

[Checker](C:/Users/andrey/src/marici/research/strominger/checkers/check_native_relational_clock.py) · [full result](C:/Users/andrey/src/marici/research/strominger/results/native-relational-clock.json)

Ten checks pass in a fresh run and SCC closure. Maximum displayed finite-matrix residual is approximately `1.29e-13`. These are numerical implementation checks, not rigorous error bounds or exact upstream proofs.

The checker validates the archive member hashes. Archived spectral values propose polynomial projectors; direct tests against the actual matrix verify idempotence, mutual orthogonality, completeness, traces and spectral reconstruction. A corrupted spectral value is rejected. All twenty original phase coordinates remain represented. The supplier and its ancestors are not rerun.

The first implementation could not execute because NumPy was absent. A requested offline dependency command was refused and was not executed. That freeze is retained. The completed audit instead uses standard-library polynomial matrix calculations and requires no dependency provisioning; it was separately frozen before its first numerical run.
