"""Sequential request/response candidates on the existing sector-label model.
The reply consumes the received ordered word, not a separately launched trace.
"""
from pathlib import Path
import hashlib
import json
from check_two_ended_sector_trace import BASE, transport, fibrate, restore

ROOT = Path(__file__).resolve().parents[3]


def run(axes=(1,2), outbound_length=None, complete_receipt=True):
    rows = BASE
    corner = 0
    sent = []
    states = [{'stage':0, 'leg':'outbound', 'corner':0, 'rows':rows, 'fibers':fibrate(rows)}]
    # First arrival is the natural stopping policy. Explicit length is a control.
    while True:
        move = axes[len(sent) % 2]
        sent.append(move)
        corner ^= move
        rows = transport(rows,move)
        states.append({'stage':len(states),'leg':'outbound','corner':corner,'move':move,'rows':rows,'fibers':fibrate(rows)})
        if (outbound_length is None and corner == 3) or len(sent) == outbound_length:
            break
        if len(sent) > 30:
            raise AssertionError('bounded trial did not arrive')
    assert corner == 3
    receipt = {'word':tuple(sent), 'rows':rows, 'fibers':fibrate(rows), 'corner':corner}
    assert restore(receipt['fibers']) == receipt['rows']
    expected = BASE
    for move in receipt['word']:
        expected = transport(expected,move)
    assert expected == receipt['rows']
    reply = []
    # Inverse receipt replay is a declared candidate response law.
    # Each L/R is self-inverse, but ordered history is NOT erased.
    for move in reversed(receipt['word']):
        reply.append(move)
        corner ^= move
        rows = transport(rows,move)
        states.append({'stage':len(states),'leg':'response','corner':corner,'move':move,'rows':rows,'fibers':fibrate(rows)})
        if not complete_receipt and corner == 0:
            break
    return {'outbound_steps':len(sent),'response_steps':len(reply),'total_steps':len(states)-1,
            'outbound_word':sent,'reply_word':reply,'receipt':receipt,'states':states,
            'outbound_E_arrivals':[s['stage'] for s in states if s['leg']=='outbound' and s['corner']==3],
            'response_P_arrivals':[s['stage']-len(sent) for s in states if s['leg']=='response' and s['corner']==0],
            'unconsumed_receipt_steps':len(sent)-len(reply)}


def main():
    checks=[]
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)
    natural=run()
    delayed_short=run(outbound_length=14,complete_receipt=False)
    delayed_full=run(outbound_length=14)
    other=run(axes=(2,1))
    check('first arrival yields two outward and two reply steps', (natural['outbound_steps'],natural['response_steps'],natural['total_steps']) == (2,2,4))
    check('reply is constructed from received word in reverse order', all(r['reply_word'] == list(reversed(r['outbound_word'])) for r in [natural,delayed_full,other]))
    check('full receipt replay restores table but retains nonempty histories', all(r['states'][-1]['rows']==BASE and r['outbound_word'] and r['reply_word'] for r in [natural,delayed_full,other]))
    check('every stored fibration reconstructs its complete rows', all(restore(s['fibers']) == s['rows'] for r in [natural,delayed_short,delayed_full,other] for s in r['states']))
    check('return uses received endpoint table', all(r['states'][r['outbound_steps']+1]['rows'] == transport(r['receipt']['rows'],r['reply_word'][0]) for r in [natural,delayed_short,delayed_full,other]))
    check('reverse initial sense preserves four-step completion', other['total_steps']==4 and other['reply_word']!=natural['reply_word'])
    check('delayed turn is fourth E arrival not first', delayed_full['outbound_E_arrivals']==[2,6,10,14])
    check('delayed turn plus first-return stop gives sixteen not twenty-eight', delayed_short['total_steps']==16 and delayed_short['unconsumed_receipt_steps']==12)
    check('imposed fourteen-step receipt gives twenty-eight with full replay', delayed_full['total_steps']==28 and delayed_full['unconsumed_receipt_steps']==0)
    check('long reply crosses P before receipt completion', delayed_full['response_P_arrivals']==[2,6,10,14])
    check('twenty-eight-step variant is P-to-E-to-P not P-to-E', delayed_full['states'][-1]['corner']==0 and delayed_full['receipt']['corner']==3)
    census=[run(outbound_length=n) for n in range(2,31,4)]
    check('all tested arrival-delayed round trips follow four-plus-eight-m', [r['total_steps'] for r in census]==list(range(4,61,8)))
    # Equal endpoint data cannot recover the chosen return history length.
    check('two and fourteen step requests have identical delivered rows', natural['receipt']['rows']==delayed_full['receipt']['rows'])
    check('those receipts nevertheless carry different histories', natural['receipt']['word']!=delayed_full['receipt']['word'])
    inputs=['research/strominger/checkers/check_two_ended_sector_trace.py',
            'research/strominger/checkers/check_sector_request_response.py',
            'research/nima/arrow-history-window.md','research/nima/native-square-controlled-hamiltonian.md']
    report={'status':'passed','check_count':len(checks),'checks':checks,
            'natural_first_arrival':natural,'delayed_turn_first_return':delayed_short,'delayed_turn_full_receipt':delayed_full,
            'arrival_delayed_census':[{k:r[k] for k in ['outbound_steps','response_steps','total_steps']} for r in census],
            'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
            'scope':'Candidate labelled-sector request/response law only. P/E are hypothetical corner readings, not derived contextual windows. Inverse receipt replay is specified, not forced by source coherence. No spatial, coefficient, esd7 or whole-assembly realization claimed.',
            'disposition':'Sequential first-arrival transport completes in four steps. Twenty-eight is realizable only in the tested delayed fourteen-step request/full-replay control, not selected by the square law.'}
    dest=ROOT/'research/strominger/results/sector-request-response.json'
    dest.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','checks':len(checks),'natural_total':natural['total_steps'],'delayed_first_return_total':delayed_short['total_steps'],'delayed_full_replay_total':delayed_full['total_steps'],'result':str(dest)}))


if __name__=='__main__':
    main()
