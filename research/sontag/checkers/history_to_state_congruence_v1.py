"""Exact bounded continuation checks; analytic argument is in the packet."""
import importlib.util
import itertools
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/strominger/checkers'))
import sympy as S
from energy_task_reduction import EnergyTaskState, gain_step
spec = importlib.util.spec_from_file_location('ctx', ROOT / 'research/sontag/checkers/contextual_capability_coalgebra.py')
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

def replay(state, word):
    for q in word:
        state = gain_step(state, q).result
    return state

words = [word for n in range(4) for word in itertools.product((S.Integer(0),S.Rational(1,2),S.Integer(1)),repeat=n)]
checks = {}
checks['equal_components_transport_all_fixture_words'] = all(
    replay(EnergyTaskState(S.Integer(a),S.Integer(b),'left'),w).energy
    == replay(EnergyTaskState(S.Integer(a),S.Integer(b),'right'),w).energy
    for a,b in itertools.product(range(3),repeat=2) for w in words)
checks['gain_word_product_square'] = all(
    replay(EnergyTaskState(S.Integer(3),S.Integer(5),'retained'),w).energy
    == gain_step(EnergyTaskState(S.Integer(3),S.Integer(5),'retained'),S.prod(w)).result.energy
    for w in words)
checks['two_readings_separate_fixture_states'] = len({
    (a+b,S.Rational(a,4)+S.Rational(b,16))
    for a,b in itertools.product(range(5),repeat=2)}) == 25
checks['H_only_hostile'] = replay(EnergyTaskState(S.Integer(8),S.Integer(0),'one'),[S.Rational(1,2)]).energy == 2 and replay(EnergyTaskState(S.Integer(0),S.Integer(8),'two'),[S.Rational(1,2)]).energy == S.Rational(1,2)
checks['context_full_state_congruence'] = all(
    c.context_trace(x,word+(e,))[-1] == c.enabled_actions(c.advance(
        __import__('functools').reduce(c.advance,word,x),e))
    for x in c.CONTEXTS for word in c.words(3) for e in c.CONTEXT_COMMANDS)
checks['immediate_context_quotient_rejected'] = not c.transition_well_defined(0,0)
checks['one_step_signatures_separate_all_contexts'] = len(c.partition(1)) == 4
# A minimal independent illustration of first-order erasure, NOT the source
# path algebra: Q[x]/(x^3), I=(x), C=I/I^2. Multiplying [x] by x
# is zero in C while x*x survives in I. Terminal quotient still multiplies.
x = S.symbols('x')
checks['illustrative_first_order_action_loses_product'] = S.rem(x*x,x**2,x)==0 and S.rem(x*x,x**3,x)==x**2
out = {'schema':'marici.sontag.history-to-state-congruence.v1',
       'scope':'finite exact energy/context fixtures; toy action illustration is not a rerun of WG source',
       'checks':{k:bool(v) for k,v in checks.items()},'passed':all(checks.values()),
       'unresolved':'general WG history equivalence and continuation/witness transport'}
p = ROOT / 'research/sontag/results/history-to-state-congruence-v1.json'
p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['passed'] else 1)
