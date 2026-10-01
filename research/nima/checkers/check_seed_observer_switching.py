"""Audit fixed-tour observer against endpoint-valid schedule switches.
Switch at a shared current source vertex; choose any slot of the other tour
with that source, then execute its outgoing edge. This is a declared stress
model, not an admitted physical switching law.
"""
import check_seed_history_observer as observer
seed=observer.seed

cases=[]
for state in seed.states:
    if seed.observation[state] not in 'AB': continue
    for replacement in seed.states:
        if replacement[0]==state[0] or seed.observation[replacement]!=seed.observation[state]: continue
        history=seed.past(state,3)  # observer synchronized BEFORE the switch
        possible=observer.candidates(history)
        assert possible==frozenset((state,))
        actual=replacement
        first_failure=None
        for step in range(1,14):
            actual=seed.next_state[actual]
            reading=seed.observation[actual]
            possible=observer.advance(possible,reading)
            history+=(reading,)
            if not possible:
                first_failure=step;break
        assert first_failure is not None
        cases.append((state,replacement,first_failure))
assert len(cases)==16
histogram={delay:sum(case[2]==delay for case in cases) for delay in sorted({c[2] for c in cases})}
print('Single-switch detection delays after synchronized prefix:',histogram)

# Under endpoint-valid arbitrary routing, observations give each traversed
# primitive edge (unique endpoint pairs) but not a private schedule-mode label.
# A silent change of mode at the SAME outgoing edge has no immediate signature.
silent=[case for case in cases if case[0][1]==case[1][1]]
assert len(silent)==8 and all(delay>1 for _,_,delay in silent)
# Explicit indefinitely hidden internal mode switching: follow tour0's vertex
# trajectory, but before every step choose the other tour's slot for that same
# primitive edge. Re-select again next step. Emitted edge word is unchanged.
for start in [s for s in seed.states if s[0]==0]:
    trajectory=start
    for _ in range(18):
        other=(1,trajectory[1])
        assert seed.observation[other]==seed.observation[trajectory]
        assert seed.registry[other[1]]==seed.registry[trajectory[1]]
        assert seed.observation[seed.next_state[other]]==seed.observation[seed.next_state[trajectory]]
        trajectory=seed.next_state[trajectory]
# This broad per-step re-selection model is larger than switching ONLY at A/B.
# Even without it, startup cannot detect a change preceding its first reading.
for state,replacement,_ in cases:
    window=seed.past(replacement,3)
    assert observer.candidates(window)==frozenset((replacement,))

# Full-history consistency and rolling recovery answer different questions.
# Following replacement long enough supplies its valid four-reading window,
# despite contradiction with the earlier synchronized preparation.
for state,replacement,delay in cases:
    history=seed.past(state,3); actual=replacement
    for _ in range(7):
        actual=seed.next_state[actual];history+=(seed.observation[actual],)
    assert observer.candidates(history)==frozenset()
    assert observer.candidates(history[-4:])==frozenset((actual,))
print('PASS: all 16 single shared-vertex switches eventually contradict the synchronized fixed-tour observer.')
print('PASS: same-edge switches have delayed detection; pre-observation changes cannot be diagnosed from the suffix alone.')
print('PASS: full-history rejection differs from rolling-window reacquisition after a switch.')
print('BOUNDARY: arbitrary hidden mode re-selection can preserve all edge observations; mode-change receipts are extra data.')
