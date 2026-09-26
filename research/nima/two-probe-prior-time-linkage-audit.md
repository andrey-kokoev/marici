# Prior time linkage: resume the future-probe programme, not external calibration

Operator priority: inspect prior research connecting consecutive probes to
time before extending the new two-probe construction.

## Existing results located

1. `physical-coyoneda-future-probe-conjecture.md`: present record laws can agree
   while successor capabilities differ. Controlled future probes can separate
   them. The physical conjecture requires a source-derived admissible probe
   family; Yoneda alone does not supply that family or physical separation.
2. `future-probe-causal-speed-conjecture.md`: future probes locate where an
   event can be distinguished. A nearest-neighbor finite-chain model bounds
   support after d layers by d edges. A nonlocal interaction defeats the bound.
   Locality, not probing alone, supplies the bound. Its checker was freshly rerun.
3. `carrier-incidence-support-filtration.md`: a pentagon incidence model supplies
   automorphism-natural support balls and subadditive composition depth without
   an external spatial coordinate. It does not select future direction.
4. `carrier-polarity-time-orientation-character-gate.md`: Carrier polarity
   changes sign under a reflection that can preserve physical time orientation.
   Their identification therefore requires a typed involution comparison, not
   shared terminology. The reference was read; its checker was not rerun here.
5. `finite-horizon-frame-covariance-selection.md`: within a specified velocity
   composition family, a fixed finite horizon selects the positive Lorentz-like
   branch. Its algebraic checker was freshly rerun. The interpretation needs the
   qualification below.
6. `speculations/time-as-the-interior-of-realization.md` explicitly separates
   constructor depth, causal order and metric duration. Its process-category
   proposal is a conjectural linkage, not a derived physical clock.
7. Voevodsky's `causal-radar-carrier-readout-completion-synthesis.md` constructs
   distance readings from emission/return clock records in a declared metric,
   with an observer, null propagation and apparatus. It is useful operational
   precedent, but assumes the time/metric structure sought here. Its reported
   167 controls were not rerun in this audit.

## Important qualification to the older frame-naturality argument

Passive covariance of an apparatus-dependent cone is not the same as an
invariant numerical speed in every inertial frame. Consider, for t>=0,

\[
|x-wt|\leq Lt.
\]

A Galilean re-expression x'=x-vt and w'=w-v preserves this SAME cone and all
its labelled outcomes. Its boundary velocities become w-v +/- L. Thus finite
local reach and passive covariance can coexist with Galilean frame changes
when the medium/apparatus velocity is retained.

The old exact algebra remains correct under its stronger premise:

\[
\frac{L+v}{1+kLv}=L\quad\Longrightarrow\quad k=1/L^2.
\]

But requiring L itself to be a fixed point is stronger than transporting a
cone naturally with its source/apparatus. Universality or an appropriate
relativity principle must be supplied or derived explicitly. The coefficient
k in this velocity law is NOT the action-phase kappa in the rotor Hamiltonian.

`checkers/check_time_linkage_covariance_audit.py` verifies the covariant
Galilean countermodel and the stronger fixed-point implication symbolically.
This does not refute that conditional implication; it prevents overreading it.

## Consequence for the current two-probe proposal

Do not start by assigning seconds to theta or declaring a minimum length.
Start with source-admissible preparation, successor transport and future
readout. Ask which retained difference becomes accessible after which allowed
continuations. Then test whether source incidence constrains that accessibility
and whether the constraint survives the full retained comparisons.

Only subsequently seek a directed causal interpretation, frame universality
and a duration measure. A finite test depth or Boolean output gap is not a
minimum physical interval. Nor can the native pointed-equivalence rule alone
supply locality: it allows supplied equivalences without a locality certificate.

The small source proof begun before this literature check is now freshly
compiled in `agda/TwoProbeDistinguishability.agda`. It uses the actual existing
native filler bridge, not Clifford data. It establishes:

- the marked (false,false) preparation cannot distinguish any pointed filler
  through the chosen readout;
- an explicitly repointed challenge distinguishes identity from swap;
- identity and a pointed controlled flip agree under a coarse readout, but a
  subsequent swap reveals the difference;
- two context-indexed bit readings recover this finite carrier point.

These are distinctions in a native finite carrier, not physical apparatus or
time. The repointed package makes the extra preparation explicit. The source
proof is a possible starting test for the older future-probe bridge, not a
replacement for its missing locality and temporal comparison constructors.

Verification performed this turn:

```text
pwsh -NoProfile -File research/nima/checkers/check_two_probe_formal.ps1 -Fresh
python research/nima/checkers/check_future_probe_causal_speed_gate.py
uv run --with sympy python research/nima/checkers/check_finite_horizon_frame_covariance_selection.py
uv run --with sympy python research/nima/checkers/check_time_linkage_covariance_audit.py
```

The new receipts are `results/agda-TwoProbeDistinguishability.json` and
`results/time-linkage-covariance-audit.json`. No native physical admission or
minimum-distance claim is made. The prior product-policy owner request remains
unresolved while the operator-directed probe-to-time bridge becomes local work.
