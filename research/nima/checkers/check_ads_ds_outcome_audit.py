"""Read-only scoped rule eligibility, not a theorem prover or graph writer."""
import argparse
import copy
import json
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
INPUT = 'research/nima/contracts/ads-ds-outcome-audit.v1.json'
REPORT = 'research/nima/results/ads-ds-outcome-audit.v1.json'
PLANNING = 'research/nima/contracts/ads-ds-workbench.v1.json'


def require(ok, why):
    if not ok:
        raise ValueError(why)


def pinned(certificate, root):
    files = certificate.get('files', {})
    if not files:
        return False
    for name, digest in files.items():
        path = (root/name).resolve()
        if not path.is_relative_to(root.resolve()) or not path.is_file():
            return False
        if sha256(path.read_bytes()).hexdigest() != digest:
            return False
    return True


def evaluate(data, verify):
    require(len({r['id'] for r in data['rules']}) == len(data['rules']), 'duplicate rules')
    rows = []
    for rule in data['rules']:
        missing, contexts = [], []
        for claim in rule['premises']:
            f = data['facts'].get(claim)
            if not f or f.get('outcome') != '++' or f.get('proposition') != claim:
                missing.append(claim + ': no exact proof outcome')
                continue
            if not f.get('context') or not f.get('scope') or not verify(f):
                missing.append(claim + ': absent scope/context or stale certificate')
                continue
            contexts.append(f['context'])
        if contexts and len(set(contexts)) != 1:
            missing.append('incompatible witness contexts')
        g = data['guard_certificates'].get(rule['guard'], {})
        expected = {k: data['facts'].get(k, {}).get('scope') for k in rule['premises']}
        if (g.get('rule') != rule['id'] or g.get('premise_scopes') != expected
                or not contexts or g.get('context') != contexts[0]
                or not g.get('conclusion_scope') or not verify(g)):
            missing.append('missing matched scope/guard certificate')
        rows.append({'rule': rule['id'], 'conclusion': rule['conclusion'],
                     'eligible_for_review': not missing, 'blockers': missing})
    return rows


def controls(data):
    # Synthetic contracts test gating only; never used as scientific evidence.
    fixture = {'rules': [{'id':'T', 'premises':['A','B'], 'conclusion':'C', 'guard':'G'}],
               'facts': {k:{'outcome':'++','proposition':k,'scope':k+'-scope','context':'same','fixture':True} for k in ('A','B')},
               'guard_certificates': {'G': {'rule':'T','premise_scopes':{'A':'A-scope','B':'B-scope'},'context':'same','conclusion_scope':'C-scope','fixture':True}}}
    verify = lambda c: c.get('fixture', False)
    require(evaluate(fixture, verify)[0]['eligible_for_review'], 'valid synthetic rule blocked')
    passed = ['synthetic-compatible-certificates']
    for mode in ('unresolved','refuted','wrong-proposition','different-source','missing-guard','wrong-scope','stale-proof'):
        bad = copy.deepcopy(fixture)
        if mode == 'unresolved': bad['facts']['A']['outcome'] = '+-'
        elif mode == 'refuted': bad['facts']['A']['outcome'] = '-+'
        elif mode == 'wrong-proposition': bad['facts']['A']['proposition'] = 'weaker-A'
        elif mode == 'different-source': bad['facts']['B']['context'] = 'other'
        elif mode == 'missing-guard': bad['guard_certificates'] = {}
        elif mode == 'wrong-scope': bad['facts']['B']['scope'] = 'local-only'
        else: bad['facts']['A']['fixture'] = False
        require(not evaluate(bad, verify)[0]['eligible_for_review'], 'unsafe propagation: '+mode)
        passed.append(mode)
    # Only the explicitly reviewed scoped WG-I5 proof is currently imported.
    require(set(data['facts']) == {'WG-I5'}, 'unreviewed theorem import')
    require(data['facts']['WG-I5'].get('assessment_id') == 'assessment:nima-wg-i5-written-proof-v1', 'missing scoped assessment')
    require(pinned(data['facts']['WG-I5'], ROOT), 'WG-I5 evidence drift')
    require(not any(r['eligible_for_review'] for r in evaluate(data, lambda c: pinned(c, ROOT))), 'unexpected broad outcome propagation')
    passed.append('scoped-WG-I5-alone-does-not-close-R7')
    return passed


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    data=json.loads((ROOT/INPUT).read_text(encoding='utf-8'))
    planning=json.loads((ROOT/PLANNING).read_text(encoding='utf-8'))
    require(data['graph_snapshot_head']==planning['graph_snapshot_head'], 'graph projections differ')
    rows=evaluate(data,lambda c:pinned(c,ROOT))
    tasks={t['id']:t for t in planning['tasks']}
    require(tasks['projective-metric-selection'].get('verdict')=='rejected', 'old rejection lost')
    require(tasks['interval-route-synthesis']['required_verdicts']['projective-metric-selection']=='constructed', 'old route weakened')
    repaired=tasks['repaired-interval-route-synthesis']['required_verdicts']
    require(all(repaired.get(k)=='constructed' for k in ('path-composition-interval-realization','source-scale-selector','dual-causal-realization','wg-interval-operation-square')), 'repair bypass')
    require('native-law-selection' not in tasks and 'autonomous-scheduling' not in repaired, 'retired scheduling requirement restored')
    require(any(t['id']=='native-law-selection' for t in planning.get('retired_tasks', [])), 'retirement provenance missing')
    result={'schema':'marici.nima.ads-ds-outcome-audit-result.v1','passed':True,
        'rules':rows,'eligible_count':sum(r['eligible_for_review'] for r in rows),
        'manual_rules':data['manual_rules'],'controls':controls(data),
        'current_result_scope':data['recorded_results_not_full_conjecture_proofs'],
        'graph_snapshot_head':data['graph_snapshot_head'],
        'boundary':'Read-only declared-rule eligibility projection. No certificate truth validation, no graph synchronization, no outcome writes. R4 still needs a concrete theorem instance.',
        'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in (INPUT,PLANNING,Path(__file__).relative_to(ROOT).as_posix())}}
    text=json.dumps(result,indent=2)+'\n'
    out=ROOT/REPORT
    if args.check:
        require(out.is_file() and out.read_text(encoding='utf-8')==text,'audit report drift')
    else:
        out.parent.mkdir(parents=True,exist_ok=True)
        out.write_text(text,encoding='utf-8')
    print(json.dumps({'passed':True,'eligible_count':result['eligible_count'],'rules_checked':len(rows),'controls':result['controls'],'check_only':args.check}))

if __name__=='__main__':
    main()
