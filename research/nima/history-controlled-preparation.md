# Resource-accounted preparation of the history-sensitive field

## Close the numerical preparation gap without changing the return law

The previous native-history encoding required

    x=u+beta*d, r=-beta*d,

with extra quadratic budget 80 beta²/3. It did not obtain that budget from
the fixed empty-bank baseline. The present construction supplies an explicit
reservoir and uses the EXISTING rank-one exchange mechanism to prepare it.
This is a conditional apparatus construction, not source selection of that
apparatus or spontaneous physical excitation.

## Reservoir and source control

The prior AB-minus-BA contrast has ||d||²=2. Therefore

    v=(d,-d)/2

is a unit mode of the existing 24-coordinate carrier/bank state, orthogonal
to the baseline (u,0). Add ONE reservoir amplitude a. Its initial value is
2g, where g is the declared conversion gain. The actual native route readings
supply a sign:

    (1,2) gives s=-1; (2,1) gives s=+1.

Use the signed exchange on the v coordinate z and reservoir a:

    (z,a) -> (s*a,s*z),

fixing the orthogonal complement. This is the prior unit-feature exchange
with a declared control sign, not a fitted force or a new feedback gain law.
The physical apparatus that reads the history and chooses this sign remains
an explicit control assumption.

Starting from (u,0,2g), the exact result is

    (u+s*g*d, -s*g*d, 0).

The reservoir is depleted; the intended history-dependent carrier/bank
preparation is obtained. Repeating the same operation returns it to the
reservoir. It is not an inexhaustible source or free memory reset.

## Checked invariants

- The full 25-dimensional preparation map E_s is orthogonal and involutive.
- The decoder x+r is preserved for EVERY input, not just the displayed orbit.
- The initial reservoir budget is exactly 80 g²/3 in inherited model units.
  It equals the extra prepared contrast budget; no energy is generated.
- An empty reservoir with baseline (u,0) remains unchanged.
- The original return U sends v to -v and fixes the baseline. Thus

      diag(U,1) E_s = E_-s diag(U,1).

  This proves compatibility of preparation with the source-history sign
  exchange, rather than merely agreement of one final sample.
- Duplicating E_s on conjugate quadratures gives a symplectic map, after
  that canonical/complex enlargement is explicitly supplied.
- P_s=(I-E_s)/2 is a rank-one orthogonal projector. The existing difference-
  mode pulse exp(-i*pi*P_s) gives this endpoint under the prior oscillator
  assumptions. Pulse area does not determine physical duration.

## What the construction now connects

The ACTUAL native history swap has a checked readout sign. A declared
controller uses that sign to select a reversible reservoir exchange. This
prepares the earlier field encoding, whose unchanged return law intertwines
with the native swap and whose existing spatial diagnostic detects it.

This closes a conditional resource-accounted chain:

    native retained history -> supplied control interface -> reservoir
        -> carrier/bank preparation -> retained return -> field readout.

It does NOT show the native source creates the reservoir, chooses g, supplies
a laboratory phase reference, or selects the apparatus. The physical charge,
mass and momentum interpretation remains distinct from mode amplitudes and
intensity centers. A conserved model norm is not automatically laboratory
energy when physical frequencies, pumps and controller costs are unspecified.

No completed square Tick is identified with a pulse duration or route-swap
count. The intrinsic-clock and physical-time obligations remain explicit.

## Verification

    uv run --with sympy python research/nima/checkers/check_history_controlled_preparation.py

28 exact rational/symbolic checks pass. The current formal source-readout
receipt and digest are verified. Receipt:
`results/history-controlled-preparation.json`.
No new Agda analytic or physical-source theorem is claimed.
