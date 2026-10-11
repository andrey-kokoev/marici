# Prior Hamiltonian attachment recovered for the triangle contrast

## Search result: the close bridge already exists

`photon-native-spatial-step.md` attaches the existing retained rotor clock
to the SAME six-arrow endpoint continuation used by the current triangle
composition branch. This is closer than the generic native-square
Hamiltonian realization and was missed by the recent execution-cost detour.

Its implementation is `checkers/photon_native_spatial_step.py`; the full
`check_photon_native_spatial_step.py` checker was rerun successfully during
this search. It also reruns the prior retained-clock audit.

Other recovered links:

- `retained-rotor-generator.md`: conditional continuous adjoint generator
  and Hamiltonian/symplectic realization.
- `retained-rotor-phase-transport.md`: specified module-compatible phase lift.
- `retained-rotor-history-clock.md`: unwrapped T with unit angular rate on
  that lift, retaining winding rather than identifying it with endpoint data.
- `recovered-source-to-qp-clock-chain.md`: canonical coordinate attachment,
  counting-metric normalization and remaining source/readout distinctions.
- `retained-clock-calibration-identifiability.md`: rate and action-scale
  freedoms not fixed by the retained comparisons.

## Exact match to today's source-derived operand difference

Use original occurrence order AB,BC,CA,BA,AD,DB. The final-occurrence summary
of today's LR-RL is

    z=(-1,-1,0,1,1,0).

The prior plane basis is

    U=(1,-1,1/2,-1,1,-1/2),
    W=(0,0,1/2,0,0,-1/2).

Let B=[U W], K be the existing continuation and R the actual target reader.
An exact SymPy calculation importing those existing definitions verifies

    C=[[-1/2,1/2],[-3/2,-1/2]],
    K B=B C.

Today's target profile corresponds to prior plane coordinates (a,b)=(1,3):

    v=B(1,3)=(1,-1,2,-1,1,-2),
    Rv=Rz=(1,-1,-1,1).

The distinction MUST be retained:

    h=z-v=(-2,0,-2,2,0,2),
    Rh=0, Kh=0.

Thus today's initial occurrence summary is not itself in the prior plane.
Its endpoint observation is already represented there, and after one actual
continuation its occurrence summary enters that plane:

    Kz=K v=B(1,-3)=(1,-1,-1,-1,1,1).

This is an observer/continuation bridge, not an identification of complete
retained histories. The kernel component and initial provenance cannot be
deleted from the retained source merely because the reader forgets them.

## What can be inherited

The prior identification q=sqrt(3)*a, p=b realizes C by the existing adjoint
rotor at theta=pi/3. Its specified positive phase lift gives

    Delta T=pi/3 per continuation,
    T_n-T_0=n*pi/3.

This therefore attaches to today's actual source-derived endpoint contrast;
it is not necessary to invent a new clock or treat all formal branches as
sequential physical events. The old endpoint spatial reader E(a,b) gives
E(1,3)=(0,0,4), agreeing with today's raw spatial contrast.

The prior angular Hamiltonian's quadratic part q²+p²=3a²+b² is 12 for
(1,3), preserved by C. This is not the Euclidean squared length of the
endpoint spatial contrast, whose values are 16,40,40. Its preservation does
not turn the latter readout into rigid rotation or normalized particle motion.

## Correction to the recent stopping boundary

The statement that there is no existing clock attachment was too broad.
There IS a checked conditional Hamiltonian/clock attachment to precisely
this continuation's cyclic sector. The present composition supplies a
source-bound endpoint contrast in that sector (with the initial kernel
qualification above).

The all-branch execution-cost calculation remains valid only for its stated
physical-event interpretation. It does not obstruct Hamiltonian evolution
of the observed cyclic sector and cannot justify demanding a new scheduler
before reusing this earlier bridge.

Still unselected: the positive continuous lift versus added windings,
physical rate/seconds calibration, full-history Hamiltonian realization,
and identification of the finer endpoint reader with the intended physical
rung-4 measurement. No photon, charge, Born law or translating particle is
established by this recovery.

## Verification scope

Fresh prior suite:

    uv run --with sympy python research/nima/checkers/check_photon_native_spatial_step.py

The z/v/kernel calculations and the full attachment are now persisted in:

    uv run --with sympy python research/nima/checkers/check_triangle_hamiltonian_clock_bridge.py

63 exact integration checks pass. Both the old photon/native-clock suite
and the new actual-composition/clock suite rerun. The new test derives its
input from the registered LR/RL products, rather than supplying a signed
mode as preparation.

For the formal sector `(a,-a,b,-b)`, the all-sector adapter to the old plane
is `D=[[0,-1],[2,-1]]`. Exact identities `RB D=F` and `C D=D A` establish
observer and dynamics compatibility on the whole two-dimensional sector,
not just the current initial vector. Here F embeds that formal sector and
A is its already proved update `(a,b)->(b-a,-a)`.

| Continuation n | Old plane coordinates | (T-T0)/pi | Words per role |
|---|---|---|---|
|0|(1,3)|0|2|
|1|(1,-3)|1/3|3|
|2|(-2,0)|2/3|5|
|3|(1,3)|1|8|

The inherited quadratic Hamiltonian is 12 at every phase; the existing
phase convention adds kappa, giving H+=12+kappa. Neither number is a
calibrated physical energy. The clock lift is checked explicitly through
six continuations, with parents recovered at every composition and the
initial kernel component recorded separately.

Receipt: `results/triangle-hamiltonian-clock-bridge.json`. These are exact
finite/symbolic integration checks, not a new Agda theorem of continuous
Hamiltonian analysis.
