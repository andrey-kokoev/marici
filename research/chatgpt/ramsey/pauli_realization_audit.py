#!/usr/bin/env python3
"""Exact GF(2) rank and constructive Pauli audit of declared Ramsey catalogues.
Standard library only. Catalogue completeness is external, not proved here.
"""
import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import urllib.request

HERE=Path(__file__).resolve().parent
SOURCE='https://users.cecs.anu.edu.au/~bdm/data/'
EXPECTED_SHA256={
    'r34_8.g6':'3068e421da9548f92c0c16196d8dc8f032eb83401716b01d96de8025a9614798',
    'r35_13.g6':'eb4d3f787f07ed14c0a82a83bee170ed096c24b6a7e971fded185ca1a760798f',
    'r36_17.g6':'3286c5366ddc70f349c3f7e798d7acbc79dc026c7abe0c8f406cad41ca990361',
    'r37_22.g6':'228d886ee01b3003d90c768af57804954f7adccbca901a3eeb3c69ccc020e8c5',
}
CATALOGUES=[('r34_8.g6',4,8,3,'all'),('r35_13.g6',5,13,1,'all'),
            ('r36_17.g6',6,17,7,'all'),('r37_22.g6',7,22,191,'source-listed extremal catalogue')]

def decode_graph6(line):
    line=line.removeprefix('>>graph6<<').strip()
    n=ord(line[0])-63
    if not 0<=n<=62:raise ValueError('Only small graph6 records supported')
    values=[ord(c)-63 for c in line[1:]]
    if len(values)!=(n*(n-1)//2+5)//6 or any(not 0<=v<64 for v in values):raise ValueError('Invalid graph6')
    rows=[0]*n;k=0
    for j in range(1,n):
        for i in range(j):
            if values[k//6]>>(5-k%6)&1:rows[i]|=1<<j;rows[j]|=1<<i
            k+=1
    return rows

def encode_graph6(rows):
    bits=[(rows[i]>>j)&1 for j in range(1,len(rows)) for i in range(j)]
    bits.extend([0]*((-len(bits))%6))
    return chr(len(rows)+63)+''.join(chr(63+sum(bits[i+k]<<(5-k) for k in range(6))) for i in range(0,len(bits),6))

def binary_rank(rows):
    pivots={}
    for value in rows:
        while value:
            p=value.bit_length()-1
            if p not in pivots:pivots[p]=value;break
            value^=pivots[p]
    return len(pivots)

def independent_witness(rows,size,candidates=None):
    def visit(available,needed,chosen):
        if needed==0:return chosen
        while available.bit_count()>=needed:
            bit=available&-available;available^=bit;v=bit.bit_length()-1
            result=visit(available&~rows[v],needed-1,chosen+[v])
            if result is not None:return result
        return None
    return visit((1<<len(rows))-1 if candidates is None else candidates,size,[])

def triangle_free(rows):
    return all(not(rows[i]&rows[j]) for j in range(len(rows)) for i in range(j) if rows[i]>>j&1)

def complement(rows):
    mask=(1<<len(rows))-1
    return [mask^row^(1<<i) for i,row in enumerate(rows)]

def factor_paulis(rows):
    """Peel rank-two alternating blocks C=x z^T+z x^T+C'.
    Returns X/Z exponent masks, and strings using W=XZ (not a phase convention for Y).
    """
    n=len(rows);residual=rows[:];xs=[0]*n;zs=[0]*n;q=0
    while any(residual):
        a=next(i for i,r in enumerate(residual) if r)
        b=(residual[a]&-residual[a]).bit_length()-1
        x=[r>>b&1 for r in residual];z=[r>>a&1 for r in residual]
        xmask=sum(v<<i for i,v in enumerate(x));zmask=sum(v<<i for i,v in enumerate(z))
        for i in range(n):
            xs[i]|=x[i]<<q;zs[i]|=z[i]<<q
            residual[i]^=(zmask if x[i] else 0)^(xmask if z[i] else 0)
        q+=1
    assert q*2==binary_rank(rows)
    for i in range(n):
        for j in range(n):
            assert (((xs[i]&zs[j]).bit_count()+(zs[i]&xs[j]).bit_count())%2)==(rows[i]>>j&1)
    letters={(0,0):'I',(1,0):'X',(0,1):'Z',(1,1):'W'}
    strings=[''.join(letters[(xs[i]>>k&1,zs[i]>>k&1)] for k in range(q)) for i in range(n)]
    return {'qubits':q,'x_masks':xs,'z_masks':zs,'paulis':strings}

def verify_record(line,s):
    rows=decode_graph6(line)
    assert triangle_free(rows)
    assert independent_witness(rows,s) is None
    witness=independent_witness(rows,s-1)
    assert witness is not None
    factor=factor_paulis(rows)
    inverse=factor_paulis(complement(rows))
    return {'graph6':line,'vertices':len(rows),'edges':sum(r.bit_count() for r in rows)//2,
            'degrees':sorted(r.bit_count() for r in rows),'binary_rank':2*factor['qubits'],
            'minimum_qubits':factor['qubits'],'complement_minimum_qubits':inverse['qubits'],
            'maximum_commuting_witness_1based':[v+1 for v in witness],
            'edge_saturated_triangle_free':all(rows[i]&rows[j] for j in range(len(rows)) for i in range(j) if not(rows[i]>>j&1)),
            'pauli_realization':factor,'complement_pauli_realization':inverse,
            'verified':{'triangle_free':True,'no_independent_s':True,'factorization_all_pairs':True}}

def audit_catalogues(cache):
    results=[]
    for filename,s,n,count,scope in CATALOGUES:
        path=cache/filename
        if not path.exists():
            data=urllib.request.urlopen(SOURCE+filename,timeout=40).read()
            # Validate prior to caching; do not save an HTTP landing page as graph data.
            lines=[line.strip() for line in data.decode('ascii').splitlines() if line.strip()]
            assert len(lines)==count
            assert all(len(decode_graph6(line))==n for line in lines)
            path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data)
        data=path.read_bytes();lines=[line.strip() for line in data.decode('ascii').splitlines() if line.strip()]
        assert sha256(data).hexdigest()==EXPECTED_SHA256[filename], 'Catalogue checksum mismatch'
        assert len(lines)==count and len(set(lines))==count
        records=[verify_record(line,s) for line in lines]
        assert all(r['vertices']==n for r in records)
        histogram=Counter(r['minimum_qubits'] for r in records)
        grouped=defaultdict(Counter)
        for r in records:grouped[r['edges']][r['minimum_qubits']]+=1
        result={'file':filename,'url':SOURCE+filename,'sha256':sha256(data).hexdigest(),
                's':s,'vertices':n,'scope':scope,'count':count,
                'edge_saturated_count':sum(r['edge_saturated_triangle_free'] for r in records),'qubit_histogram':dict(sorted(histogram.items())),
                'complement_qubit_histogram':dict(sorted(Counter(r['complement_minimum_qubits'] for r in records).items())),
                'edge_count_vs_qubits':{str(e):dict(sorted(h.items())) for e,h in sorted(grouped.items())},'records':records}
        results.append(result)
        print(filename,'qubits',result['qubit_histogram'],'complement',result['complement_qubit_histogram'],flush=True)
    return results

def deletion_audit(catalogue):
    histogram=Counter();rank_changes=Counter();checked=valid=0;seen=set();best=None;examples={}
    minimum_cost=min(r['minimum_qubits'] for r in catalogue['records']);minimum_records=[]
    for record in catalogue['records']:
        rows=decode_graph6(record['graph6']);n=len(rows);mask=(1<<n)-1
        low_cost={'graph6':record['graph6'],'qubits':record['minimum_qubits'],'degrees':record['degrees'],
                  'valid_deletions':0,'forbidden_commuting_sevens_by_deleted_edge':{}} if record['minimum_qubits']==minimum_cost else None
        for j in range(n):
            for i in range(j):
                if not(rows[i]>>j&1):continue
                checked+=1
                # Any newly independent seven must include both deleted endpoints.
                available=mask&~(rows[i]|rows[j]|(1<<i)|(1<<j))
                five=independent_witness(rows,5,available)
                if five is not None:
                    if low_cost is not None:
                        witness=[i,j]+five
                        assert all(not(rows[a]>>b&1) for a in witness for b in witness if a!=b and {a,b}!={i,j})
                        low_cost['forbidden_commuting_sevens_by_deleted_edge'][f'{i+1},{j+1}']=[v+1 for v in witness]
                    continue
                if low_cost is not None:low_cost['valid_deletions']+=1
                modified=rows[:];modified[i]^=1<<j;modified[j]^=1<<i
                valid+=1;line=encode_graph6(modified)
                if line in seen:continue
                seen.add(line)
                assert triangle_free(modified) and independent_witness(modified,7) is None
                factor=factor_paulis(modified);qubits=factor['qubits'];histogram[qubits]+=1
                change=qubits-record['minimum_qubits'];rank_changes[change]+=1
                example={'parent_graph6':record['graph6'],'deleted_edge_1based':[i+1,j+1],
                         'graph6':line,'parent_qubits':record['minimum_qubits'],'minimum_qubits':qubits,
                         'pauli_realization':factor}
                if best is None or qubits<best['minimum_qubits']:best=example
                examples.setdefault(str(change),example)
        if low_cost is not None:minimum_records.append(low_cost)
    return {'attempted_parent_edge_pairs':checked,'valid_parent_edge_pairs':valid,
            'distinct_labelled_valid_graphs':len(seen),'qubit_histogram':dict(sorted(histogram.items())),
            'qubit_change_histogram':dict(sorted(rank_changes.items())),
            'deduplication':'identical graph6 only, not graph isomorphism',
            'scope':'Exactly one deletion from the supplied 22-vertex catalogue; no isomorphism classification of the results.',
            'minimum_witness':best,'change_witnesses':examples,'minimum_catalogue_records':minimum_records}

def make_report(result):
    lines=['# Ramsey–Pauli realization-cost audit','',
           'Exact arithmetic over F₂. Anticommutation is adjacency; commutation is nonadjacency. Each graph is checked for triangle-freeness and absence of an independent s-set. Every Pauli realization is checked against every matrix entry. W denotes XZ.','',
           'By Sarkar–Yoder, arXiv:2302.07966v2, Theorem 5.4, the minimum qubits for a **fixed** commutation matrix C are rank_F₂(C)/2. Rank is computed independently of the constructive factorization.','',
           '## Catalogue results','', '| Constraints | Vertices | Catalogue scope | Records | Minimum-qubit histogram | Swapped-relation histogram |',
           '|---|---:|---|---:|---|---|']
    for c in result['catalogues']:
        lines.append(f"| (3,{c['s']}) | {c['vertices']} | {c['scope']} | {c['count']} | {c['qubit_histogram']} | {c['complement_qubit_histogram']} |")
    c=result['catalogues'][-1]
    lines+=['','## R(3,7): edge counts versus register cost','', '| Edges | Qubits: number of records |','|---:|---|']
    for edges,hist in c['edge_count_vs_qubits'].items():lines.append(f'| {edges} | {hist} |')
    d=result['single_edge_deletions']
    lines+=['','## One-edge deletions', '',
            f"Tried {d['attempted_parent_edge_pairs']} parent/edge pairs; {d['valid_parent_edge_pairs']} preserve (3,7) avoidance, yielding {d['distinct_labelled_valid_graphs']} distinct labelled graph6 records.",
            f"Minimum-qubit histogram: **{d['qubit_histogram']}**.",
            f"Qubit-cost changes relative to the first encountered parent: **{d['qubit_change_histogram']}**.",
            'Identical graph6 records are deduplicated; isomorphic relabellings are not. These are perturbations of the supplied catalogue, not a claim of new isomorphism classes.','',
            '## Lowest-cost catalogue records','',
            *[f"- A {r['qubits']}-qubit record with degree range {min(r['degrees'])}–{max(r['degrees'])}: {r['valid_deletions']} valid edge deletions; {len(r['forbidden_commuting_sevens_by_deleted_edge'])} deletions create a commuting seven-set. Explicit witnesses are stored in the JSON." for r in d['minimum_catalogue_records']], '',
            '## Scope and interpretation','',
            '- Vertex count, graph edge count, and minimum qubit count are different invariants.',
            '- Complementing the graph swaps the meanings of the two binary outcomes. It preserves the Ramsey avoidance statement with parameters swapped, but need not preserve realization cost.',
            '- Deleting an edge removes an anticommutation requirement **and adds a commutation requirement**. It is not merely dropping a constraint; rank need not be monotone.',
            f"- Catalogue completeness/isomorphism classification is attributed to the source, not independently proved here. The source heading says ‘maximal’, but this must not be read as edge-maximal: {c['edge_saturated_count']} of {c['count']} records are triangle-free edge-saturated; {c['count']-c['edge_saturated_count']} are not. These are largest-order (22-vertex) examples.",
            '- No new Ramsey upper bound, unrestricted minimum-dimension theorem, or connection to ESD7 geometry is established.', '',
            '## Reproduce','', '```sh','python research/chatgpt/ramsey/pauli_realization_audit.py','python -m unittest discover -s tests -p "test_pauli_realization_audit.py"','```','',
            'Input graph6 files are cached under `pauli-realization-catalogues/`. Source URLs, SHA-256 hashes, per-record ranks, and explicit minimum-register Pauli strings are in `pauli-realization-audit.json`.','',
            'Source catalogue: https://users.cecs.anu.edu.au/~bdm/data/ramsey.html','']
    return '\n'.join(lines)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--cache',type=Path,default=HERE/'pauli-realization-catalogues');args=parser.parse_args()
    catalogues=audit_catalogues(args.cache)
    deletion=deletion_audit(catalogues[-1]);print('single-edge deletion audit', {k:v for k,v in deletion.items() if 'witness' not in k and k!='minimum_catalogue_records'},flush=True)
    result={'schema':'marici.ramsey-pauli-realization-audit.v1','catalogues':catalogues,'single_edge_deletions':deletion}
    (HERE/'pauli-realization-audit.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    (HERE/'pauli-realization-audit.md').write_text(make_report(result),encoding='utf-8')

if __name__=='__main__':main()
