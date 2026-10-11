# Witnessing as retained Hamiltonian full turn: prior-work refresh

## Operator clarification

The operator identifies observation with witnessing, and witnessing with a
2pi rotation in the Hamiltonian realization. Use that intended connection,
not an external classical measurement device or a freely selected numerical
projection. Endpoint summation is a representation of selected information;
it is not by itself the witnessing operation.

This clarification supplies the intended interpretation. The inspected prior
results establish particular retained-return and rotor realizations, not a
universal theorem that every generic witness type is a Hamiltonian rotation.

## Recovered chain

- `retained-square-cone-clock.md`: a completed square-and-return record
  retains forward schedules, their comparison, return section and endpoint
  laws. It embeds recoverably in the tetrahedral whole. Counting completions
  cannot descend to the returned endpoint alone.
- `native-square-controlled-hamiltonian.md`: the actual native Bool square
  has a Hamiltonian realization. A reflected return and positive continuation
  can share endpoints but differ between them. Which route is retained matters.
- `retained-rotor-phase-transport.md`: the specified module-compatible phase
  lift supplies the angular Hamiltonian and its additive constant.
- `retained-rotor-history-clock.md`: T advances with the lifted angle; a full
  rotor return does not erase T or construction history.
- `paw-half-turn-promotion.md`: two same-direction half-turns make a completed
  vector turn that can be promoted to a fresh addressed identity record, with
  event occurrences and parents retained. A forward/backtrack is distinct.
- `photon-native-spatial-step.md`: the same six-arrow continuation is attached
  to that rotor with increment theta=pi/3 and adjoint phase increment 2pi/3.

## Keep the angle convention explicit

For U(theta)=exp(theta J), J²=-I, the existing adjoint plane rotates through
angle 2theta (with orientation set by the chosen convention):

| Seed updates | Rotor angle theta | Adjoint phase | Signed lift |
|---|---|---|---|
|3|pi|2pi|-I|
|6|2pi|4pi|+I|

Both return the cyclic endpoint reading. Only six updates return the signed
rotor itself. Neither returns the accumulated record to empty history.
Thus a 2pi witness measured in the Hamiltonian rotor parameter corresponds
to six of the current updates; a 2pi adjoint/vector turn corresponds to three.
The earlier least-three-period result is a statement about the latter
reading, not proof that the signed full witnessing cycle has only three steps.

The paw convention makes the same factor explicit with physical vector angle
alpha and rotor cos(alpha/2)-J sin(alpha/2): alpha=2pi returns the vector but
leaves signed lift -1; alpha=4pi returns +1. This is bookkeeping in the chosen
realization, not a particle-spin assertion.

## Consequence for the current research table

Question 6 should concern attachment of the actual retained full-turn witness
to rung4, preserving its lifted phase, comparison data and history. It should
not ask us to invent a separate classical observer or identify witnessing
with an endpoint aggregate. The continuous generator and coherent stage
transport already constructed concern representations of that retained
process; they do not erase its distinction from the identity endpoint.

## Fresh verification

    uv run --with sympy python research/nima/checkers/check_retained_rotor_history_clock.py
    python research/nima/checkers/check_paw_half_turn_promotion.py

Both pass. The square/cone and square-Hamiltonian documents were inspected;
their formal roots were not freshly rerun during this refresh.
