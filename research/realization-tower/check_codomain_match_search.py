"""Bounded compare-first pilot: 144 directed-edge comparisons, then local filling.

Codomain: the common FCC incidence complex. Match: exact oriented edge equality.
Candidate completion: face-connected A--C--B (or direct A--B), retaining the
matched edge and every face inclusion. Candidate pool is the six prior carriers.
This is NOT a coefficient comparator or a full WG filler validator.
"""
from itertools import permutations, combinations
from collections import Counter
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[2]


def channels(cell):
    v=cell['vertices']
    return [{'local':[i,j], 'codomain_edge':(v[i],v[j])} for i,j in permutations(range(4),2)]


def comparison(a,b):
    aa,bb=channels(a),channels(b)
    return [{'left_channel':i,'right_channel':j,'left_local':x['local'],'right_local':y['local'],
             'left_image':x['codomain_edge'],'right_image':y['codomain_edge'],
             'match':x['codomain_edge']==y['codomain_edge']}
            for i,x in enumerate(aa) for j,y in enumerate(bb)]


def face(a,b): return frozenset(a['vertices']) & frozenset(b['vertices'])


def validate(a,b,match,chain):
    assert match in comparison(a,b) and match['match'], 'not an actual codomain match'
    assert len(chain) in (2,3) and chain[0]==a and chain[-1]==b
    assert len({c['id'] for c in chain})==len(chain), 'reused cell'
    edge=frozenset(match['left_image'])
    assert len(edge)==2 and all(edge<=set(c['vertices']) for c in chain)
    interfaces=[face(x,y) for x,y in zip(chain,chain[1:])]
    assert all(len(f)==3 and edge<=f for f in interfaces), 'missing shared face'
    if len(chain)==3:assert interfaces[0]!=interfaces[1], 'same face used twice'
    counts=Counter(frozenset(f) for c in chain for f in combinations(c['vertices'],3))
    assert max(counts.values())<=2, 'nonmanifold face incidence'
    return {'cells':[c['id'] for c in chain],
            'interfaces':[sorted(f) for f in interfaces],
            'matched_codomain_edge':match['left_image'],
            'outer_faces':sum(n==1 for n in counts.values()),
            'internal_faces':sum(n==2 for n in counts.values())}


def search(a,b,pool):
    table=comparison(a,b);assert len(table)==144
    witnesses=[]
    for m in table:
        if not m['match']:continue
        proposals=[[a,b]] if len(face(a,b))==3 else [[a,c,b] for c in pool if c['id'] not in (a['id'],b['id'])]
        for chain in proposals:
            try:record=validate(a,b,m,chain)
            except AssertionError:continue
            witnesses.append({'comparison':m,'completion':record})
    # Retain all witnesses even if opposite oriented matches yield one complex.
    grouped={}
    for w in witnesses:
        k=tuple(w['completion']['cells'])
        grouped.setdefault(k,[]).append(w)
    return table,[{'cell_chain':list(k),'witnesses':v} for k,v in grouped.items()]


def main():
    source=ROOT/'examples/realization-lattice/helium-carriers.json'
    raw=json.loads(source.read_text(encoding='utf-8'))
    # Algorithms see geometry and opaque source IDs; species/labels are used
    # only afterward to report which prior carriers were recovered.
    cells=[{'id':str(i),'vertices':tuple(tuple(p) for p in c['indices'])} for i,c in enumerate(raw['items'])]
    labels={str(i):c['label'] for i,c in enumerate(raw['items'])}
    all_pairs=[];selected=[];comparisons=0
    for a,b in permutations(cells,2):
        table,completions=search(a,b,cells);comparisons+=len(table)
        all_pairs.append({'entry':labels[a['id']],'exit':labels[b['id']],
                          'comparisons':len(table),'matches':sum(m['match'] for m in table),
                          'completions':[[labels[i] for i in c['cell_chain']] for c in completions]})
        if (labels[a['id']],labels[b['id']]) in [('P1','E1'),('P2','E2')]:
            assert sum(m['match'] for m in table)==2
            assert len(completions)==1 and labels[completions[0]['cell_chain'][1]]=='N1'
            selected.append({'entry':labels[a['id']],'exit':labels[b['id']],
                             'all_144_comparisons':table,'completion_records':completions})
    assert comparisons==30*144==4320
    # Relabelling/translation does not change incidence decisions.
    shifted=[{'id':c['id'],'vertices':tuple((p[2]+2,-p[0],p[1]) for p in c['vertices'])} for c in cells]
    for i,j in permutations(range(6),2):
        old,oc=search(cells[i],cells[j],cells);new,nc=search(shifted[i],shifted[j],shifted)
        assert [m['match'] for m in old]==[m['match'] for m in new]
        assert [c['cell_chain'] for c in oc]==[c['cell_chain'] for c in nc]
    a,b=cells[0],cells[2];table,complete=search(a,b,cells);m=next(m for m in table if m['match'])
    rejected=[]
    def reject(name,fn):
        try:fn()
        except AssertionError:rejected.append(name)
        else:raise AssertionError('accepted hostile '+name)
    reject('false_match',lambda:validate(a,b,{**m,'right_image':((99,0,0),(100,0,0))},[a,cells[1],b]))
    reject('edge_only_union_is_not_face_completion',lambda:validate(a,b,m,[a,b]))
    reject('wrong_bridge',lambda:validate(a,b,m,[a,cells[5],b]))
    reject('repeat_entry_as_bridge',lambda:validate(a,b,m,[a,a,b]))
    report={'status':'pass','scope':'Finite six-carrier geometric incidence pilot, no global completeness or WG filler claim',
      'codomain':'Shared FCC vertex/edge/face incidence; each carrier has its explicit affine inclusion',
      'match_rule':'Exact equality of ordered edge endpoints; no tolerance or role labels',
      'completion_rule':'At most one additional retained carrier; face-connected chain through the matched edge',
      'comparisons':comparisons,'pair_count':30,'source_id_to_label':labels,
      'pair_summaries':all_pairs,'selected_cases':selected,'rejected_controls':rejected,
      'limits':['Pool already contains six constructed helium carriers; recovery is not particle generation.',
                'Match cell here is a 1-cell (directed edge), not a generated tetrahedron.',
                'No phase/coefficient equivalence or full higher-coherence closure checked.',
                'Two-component/full helium assembly and arbitrary lattice cell pairs are not settled.']}
    out=Path(__file__).with_name('results')/'codomain-match-search-v1.json'
    out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','comparisons':comparisons,'selected':[p for p in all_pairs if (p['entry'],p['exit']) in [('P1','E1'),('P2','E2')]],'rejected_controls':rejected}))


if __name__=='__main__':main()
