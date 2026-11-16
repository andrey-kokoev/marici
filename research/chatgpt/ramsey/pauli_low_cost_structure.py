#!/usr/bin/env python3
"""Explore exact parity structure of the low-cost Ramsey(3,7;22) graphs."""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
from pauli_realization_audit import decode_graph6, binary_rank, factor_paulis, EXPECTED_SHA256
from hashlib import sha256
HERE=Path(__file__).resolve().parent

def kernel_basis(rows):
    a=rows[:];pivots=[];rank=0;n=len(rows)
    for col in range(n):
        p=next((i for i in range(rank,n) if a[i]>>col&1),None)
        if p is None:continue
        a[p],a[rank]=a[rank],a[p]
        for i in range(n):
            if i!=rank and a[i]>>col&1:a[i]^=a[rank]
        pivots.append(col);rank+=1
    basis=[]
    for free in range(n):
        if free in pivots:continue
        vector=1<<free
        for i,p in enumerate(pivots):
            if a[i]>>free&1:vector|=1<<p
        assert all((row&vector).bit_count()%2==0 for row in rows)
        basis.append(vector)
    assert len(basis)==n-binary_rank(rows)
    return basis

def span(basis):
    result=[0]
    for b in basis:result += [x^b for x in result]
    return result

def parity_closed_heptagons(rows):
    """Direct induced-cycle search; no matrix ranks or kernels are used."""
    n=len(rows);found={};cycle_count=0
    def visit(path,used):
        nonlocal cycle_count
        first,last=path[0],path[-1]
        candidates=rows[last]&~used&~((1<<(first+1))-1)
        closing=len(path)==6
        while candidates:
            bit=candidates&-candidates;candidates^=bit;v=bit.bit_length()-1
            expected=(1<<last)|((1<<first) if closing else 0)
            if rows[v]&used!=expected:continue
            if closing:
                if path[1]>v:continue
                cycle_count+=1;mask=used|bit
                if all((r&mask).bit_count()%2==0 for r in rows):found[mask]=path+[v]
            else:visit(path+[v],used|bit)
    for first in range(n):visit([first],1<<first)
    return found,cycle_count

def relation_certificate(rows,heptagons):
    """Six independent even-neighborhood supports + an invertible principal minor."""
    n=len(rows);code=span(kernel_basis(rows));relations=[]
    for word in [(1<<n)-1]+list(heptagons)+sorted(code,key=lambda w:(w.bit_count(),w)):
        if binary_rank(relations+[word])>len(relations):relations.append(word)
    assert len(relations)==6
    realization=factor_paulis(rows)
    details=[]
    for word in relations:
        vertices=[i for i in range(n) if word>>i&1]
        degrees=sorted((rows[i]&word).bit_count() for i in vertices)
        if word==(1<<n)-1:kind='all vertices (even 6-regular degree)'
        elif word in heptagons:kind='parity-closed induced C7'
        elif len(vertices)==7 and degrees==[0,0,2,2,2,2,2]:kind='induced C5 plus two isolated vertices'
        else:kind=f'{len(vertices)}-vertex even-neighborhood support'
        x=z=phase=0
        for i in vertices:
            phase^=(z&realization['x_masks'][i]).bit_count()%2
            x^=realization['x_masks'][i];z^=realization['z_masks'][i]
        assert x==z==0
        details.append({'vertices_1based':[i+1 for i in vertices],'kind':kind,'induced_degrees':degrees,
                        'neighborhood_intersections':[(r&word).bit_count()for r in rows],
                        'ordered_pauli_product': '-I' if phase else '+I'})
    residual=rows[:];pivots=[]
    while any(residual):
        a=next(i for i,r in enumerate(residual)if r);b=(residual[a]&-residual[a]).bit_length()-1
        x=sum(((r>>b)&1)<<i for i,r in enumerate(residual));z=sum(((r>>a)&1)<<i for i,r in enumerate(residual))
        residual=[r^(z if r>>b&1 else 0)^(x if r>>a&1 else 0) for r in residual]
        pivots.extend([a,b])
    principal=[sum(((rows[i]>>j)&1)<<k for k,j in enumerate(pivots))for i in pivots]
    assert len(set(pivots))==16 and binary_rank(principal)==16
    return {'independent_relations':details,'relation_rank':binary_rank(relations),
            'nonsingular_principal_vertices_1based':[i+1 for i in pivots],
            'principal_binary_rank':16,'minimum_qubits':8,'pauli_realization':realization}

def structure(rows):
    n=len(rows);basis=kernel_basis(rows);code=span(basis)
    common=Counter((rows[i]&rows[j]).bit_count() for i,j in combinations(range(n),2) if not(rows[i]>>j&1))
    squares=sum(((rows[i]&rows[j]).bit_count()*((rows[i]&rows[j]).bit_count()-1))//2 for i,j in combinations(range(n),2))//2
    columns=[sum(((b>>i)&1)<<j for j,b in enumerate(basis)) for i in range(n)]
    minimum=min((x.bit_count() for x in code if x),default=0)
    minimal=[x for x in code if x and x.bit_count()==minimum]
    heptagons,cycle_count=parity_closed_heptagons(rows)
    from_kernel={w for w in code if w.bit_count()==7 and all((rows[i]&w).bit_count()==2 for i in range(n)if w>>i&1)}
    assert set(heptagons)==from_kernel
    heptagon_details=[]
    for mask,cycle in heptagons.items():
        heptagon_details.append({'cycle_1based':[i+1 for i in cycle],
            'outside_neighbor_count_histogram':dict(sorted(Counter((r&mask).bit_count()for i,r in enumerate(rows)if not(mask>>i&1)).items())),
            'intersection_sizes_with_others':sorted((mask&other).bit_count()for other in heptagons if other!=mask)})
    return {'parity_closed_heptagons':heptagon_details,'heptagon_relation_rank':binary_rank(list(heptagons)),
            'induced_heptagon_count':cycle_count,
            'compression_certificate':relation_certificate(rows,heptagons) if n-len(basis)==16 else None,
            'rank':n-len(basis),'nullity':len(basis),'degrees':sorted(row.bit_count() for row in rows),
            'kernel_basis':basis,'kernel_weight_enumerator':dict(sorted(Counter(x.bit_count() for x in code).items())),
            'kernel_column_multiplicities':dict(sorted(Counter(Counter(columns).values()).items())),
            'minimum_kernel_weight':minimum,'minimum_weight_word_count':len(minimal),
            'minimum_weight_words_rank':binary_rank(minimal),
            'nonadjacent_common_neighbors':dict(sorted(common.items())), 'four_cycles':squares,
            'minimum_word_supports_1based':[[i+1 for i in range(n) if word>>i&1]for word in minimal]}

def make_report(result):
    lines=['# Why the two low-cost Ramsey patterns fit in eight qubits','',
           'Status: exact certificates for two graphs; a motif discriminator verified on the supplied 191-record catalogue. Not an unrestricted classification theorem or a new Ramsey bound.','',
           '## A structural discriminator: parity-closed heptagons','',
           'Call an induced seven-cycle S **parity-closed** when every vertex of the whole graph has an even number of neighbors in S. This is a graph-only test: find a chordless seven-cycle, then count its incidences with all vertices. It does not require computing a matrix rank.','',
           '| Minimum qubits | Parity-closed induced C7s per graph | Catalogue records |','|---:|---:|---:|']
    for row in result['feature_table']:lines.append(f"| {row['qubits']} | {row['parity_closed_heptagons']} | {row['records']} |")
    lines+=['','Both low-cost graphs have four such heptagons; no other catalogue graph has one. For each of these heptagons, fourteen outside vertices have two neighbors on the cycle and one outside vertex has none. The four cycle supports have binary span dimension three; their XOR is zero. Their pairwise intersections have sizes 1 or 3.','',
            'The heptagons alone do **not** explain all six dependencies. Their three independent relations plus the all-vertices relation account for four. Two further even-neighborhood relations complete the certificate.','',
            '## Why even-neighborhood relations save qubits','',
            'Let A be the binary anticommutation adjacency matrix and let 1_S be the incidence vector of a vertex subset. The parity condition is exactly A 1_S = 0. Graphically, each operator anticommutes with an even number of operators in S, so the ordered product over S commutes with every listed operator.','',
            'In a minimum-register realization spanning the full nondegenerate symplectic space, this product is a scalar ±I. In a nonminimal realization it need only be central relative to the chosen family; the scalar conclusion must not be assumed there.','',
            'Six independent parity relations give nullity(A) ≥ 6, hence rank(A) ≤ 22−6 = 16. A separately exhibited nonsingular 16×16 principal submatrix gives rank(A) ≥ 16. Together these certify **exactly eight qubits**, without relying on a single full-matrix rank assertion.','']
    for record in result['records']:
        certificate=record['compression_certificate']
        if certificate is None:continue
        lines += [f"## Catalogue record {record['catalogue_record_1based']}",'',
                  'Graph6:', '```text', record['graph6'], '```','',
                  'Independent parity relations (vertex labels are 1-based; products use increasing label order):','',
                  '| Support | Graph structure | Product in the saved minimal realization |','|---|---|---|']
        for relation in certificate['independent_relations']:
            lines.append(f"| {', '.join(map(str,relation['vertices_1based']))} | {relation['kind']} | {relation['ordered_pauli_product']} |")
        lines += ['', 'A nonsingular principal submatrix is supported on: '+', '.join(map(str,certificate['nonsingular_principal_vertices_1based']))+'.','']
    lines += ['## What this does and does not explain','',
              '- The low cost comes from six independent global even-neighborhood relations; the certificates exhibit those relations explicitly.',
              '- Parity-closed heptagons supply a non-rank structural signature distinguishing the two examples within this catalogue.',
              '- Both examples have degree six, but eight other catalogue graphs are also 6-regular and require nine or ten qubits. Regularity alone is insufficient.',
              '- The four heptagons account for only three independent relations. The additional supports are essential to the eight-qubit certificate.',
              '- This report itself is catalogue-relative. The subsequent `heptagon-normal-form-theorem.md` gives a separate, catalogue-independent computer-assisted proof that the exact 22-vertex hypotheses force rank 16. It includes independently checked UNSAT proofs and completion certificates; it is not a short human-only derivation.',
              '- Follow-up: `heptagon-forcing-investigation.md` gives a 21-vertex, 6-regular counterexample to the unrestricted-size implication (nine qubits) and a graph-only boundary lemma. The exact 22-vertex claim is subsequently settled by the normal-form computation.',
              '- No identification with ESD7, physical braid carriers, or an unrestricted qudit-dimension minimum follows.','',
              '## Verification','',
              'The heptagons are found by a direct induced-cycle search and independently matched against weight-seven kernel vectors. Certificate verification checks every neighborhood parity, independence of all six supports, the 16×16 minor, and each stated Pauli product.','',
              '```sh','python research/chatgpt/ramsey/pauli_low_cost_structure.py','python -m unittest discover -s tests -p "test_pauli_low_cost_structure.py"','```','',
              'Full per-graph features and certificates: `pauli-low-cost-structure.json`. Input catalogue and its SHA-256 are pinned by `pauli_realization_audit.py`.','']
    return '\n'.join(lines)

def main():
    data=(HERE/'pauli-realization-catalogues/r37_22.g6').read_bytes()
    assert sha256(data).hexdigest()==EXPECTED_SHA256['r37_22.g6']
    lines=data.decode().splitlines()
    all_records=[]
    for i,line in enumerate(lines,1):
        result=structure(decode_graph6(line));result.update(catalogue_record_1based=i,graph6=line)
        all_records.append(result)
        if result['rank']==16:
            print('record',i,'qubits',result['rank']//2,'closed heptagons',len(result['parity_closed_heptagons']),
                  'relations',[r['kind']for r in result['compression_certificate']['independent_relations']],flush=True)
    feature_table=Counter((r['rank']//2,len(r['parity_closed_heptagons']))for r in all_records)
    print('qubits, parity-closed C7 count -> records',dict(feature_table),flush=True)
    result={'schema':'marici.ramsey-pauli-low-cost-structure.v1','catalogue_sha256':sha256(data).hexdigest(),
            'scope':'191 source-listed 22-vertex graphs; motif characterization is catalogue-relative, not an unrestricted theorem.',
            'feature_table':[{'qubits':q,'parity_closed_heptagons':h,'records':count}for(q,h),count in sorted(feature_table.items())],
            'records':all_records}
    (HERE/'pauli-low-cost-structure.json').write_text(json.dumps(result,indent=2)+'\n')
    (HERE/'pauli-low-cost-structure.md').write_text(make_report(result),encoding='utf-8')

if __name__=='__main__':main()
