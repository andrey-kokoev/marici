"""Finite native endpoint/cache collision with differing Ramsey color queries."""
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from research.voevodsky.checkers.check_ramsey_native_word_trace import independent_decode

ATTEMPT = 'research/voevodsky/contracts/ramsey-native-query-descent-attempt.v1.json'
PROOF = 'research/voevodsky/ramsey-native-query-descent-obstruction-v1.md'
NODE = r'''
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {encodeWord,decodeWord,replayTrace,canonical,same} from './research/voevodsky/ramsey-native-word-trace.mjs';
const alphabet=['s0','s1','s2'],words=[[0,2],[1,0]],pattern=[[0,0,0],[1,1,0],[1,0,1]];
const traces=words.map(w=>encodeWord(alphabet,w)),states=traces.map(t=>replayTrace(t));
assert(same(traces[0].endpoint,traces[1].endpoint));
assert(same(states[0].rules,states[1].rules));
assert(traces.every(t=>t.events.length===7));
assert.deepEqual(traces.map(decodeWord),words);
const queries=words.map(w=>[0,1,2].map(j=>w.reduce((sum,i)=>sum+pattern[i][j],0)));
const colors=queries.map(v=>(v[1]%2+2)%2);assert.deepEqual(colors,[0,1]);
const coloring=[];for(let x=-2;x<=2;x++)for(let y=-2;y<=2;y++)for(let z=-2;z<=2;z++)if((x+y+z)%2===0)coloring.push({point:[x,y,z],color:(y%2+2)%2});
const cacheHashes=states.map(s=>createHash('sha256').update(JSON.stringify(canonical(s.rules))).digest('hex'));
console.log(JSON.stringify({alphabet,words,pattern,traces,queries,colors,coloring,cacheHashes,
 completeEndpointsEqual:true,completeCachedModelsEqual:true,totalEventCounts:[7,7]}));
'''


def main():
    attempt = json.loads((ROOT / ATTEMPT).read_text(encoding='utf-8'))
    run = subprocess.run(['node', '--input-type=module', '-e', NODE], cwd=ROOT,
                         capture_output=True, text=True, check=True, timeout=60)
    raw = json.loads(run.stdout)
    assert raw['alphabet'] == attempt['alphabet'] and raw['words'] == attempt['words']
    assert raw['pattern'] == attempt['pattern']
    assert all(len(word) == attempt['word_length'] == 2 for word in raw['words'])
    assert raw['traces'][0]['endpoint'] == raw['traces'][1]['endpoint']
    assert raw['completeEndpointsEqual'] and raw['completeCachedModelsEqual']
    assert raw['cacheHashes'][0] == raw['cacheHashes'][1]
    assert raw['totalEventCounts'] == [7, 7]
    assert [independent_decode(t) for t in raw['traces']] == raw['words']
    assert raw['traces'][0]['events'] != raw['traces'][1]['events']
    domain = {p for p in product(range(-2, 3), repeat=3) if sum(p) % 2 == 0}
    colors = {tuple(row['point']): row['color'] for row in raw['coloring']}
    assert len(raw['coloring']) == len(colors) == 63 and set(colors) == domain
    assert all(colors[p] == p[1] % 2 for p in colors)
    queries = [tuple(sum(raw['pattern'][i][j] for i in word) for j in range(3)) for word in raw['words']]
    assert queries == [(1, 0, 1), (1, 1, 0)]
    assert [list(q) for q in queries] == raw['queries']
    assert [colors[q] for q in queries] == raw['colors'] == [0, 1]
    # Reuse source pin inventory, not its prior scientific outcome. Every
    # native history in this test is freshly encoded and replayed above.
    prior_path = ROOT / 'research/voevodsky/results/ramsey-native-word-trace-v1.json'
    prior = json.loads(prior_path.read_text(encoding='utf-8'))
    sources = dict(prior['source_sha256'])
    for relative in [ATTEMPT, PROOF, 'research/voevodsky/checkers/check_ramsey_native_query_descent.py']:
        sources[relative] = sha256((ROOT / relative).read_bytes()).hexdigest()
    for relative, digest in sources.items():
        path = (ROOT / relative).resolve()
        assert path.is_relative_to(ROOT) and sha256(path.read_bytes()).hexdigest() == digest
    result = {
        'schema': 'marici.ramsey-native-query-descent.verification.v1', 'status': 'passed',
        'scope_id': attempt['scope_id'], 'outcome': '-+',
        'verification_level': 'written finite nonfactorization argument, fresh native packet replay and independent arithmetic; not a general native-forcing refutation or kernel proof',
        'witness': raw,
        'fixed_word_length': 2, 'same_total_event_count': 7,
        'same_complete_endpoint': True, 'same_complete_cached_model': True,
        'different_required_queries': True, 'different_required_colors': True,
        'projected_query_factors': False, 'retained_history_query_recovers_both': True,
        'all_endpoint_encodings_refuted': False, 'native_forcing_refuted': False, 'root_resolved': False,
        'source_sha256': dict(sorted(sources.items())),
    }
    target = ROOT / 'research/voevodsky/results/ramsey-native-query-descent-v1.json'
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k not in ('source_sha256', 'witness')}))


if __name__ == '__main__':
    main()
