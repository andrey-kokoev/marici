#!/usr/bin/env python3
"""Natural directed-system/Fock decomposition of NNMHV history spaces."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/nima'));from nnmhv_coherence_paths import compile_nnmhv_histories
def key(h):return (h.outer_pair,h.inner_pair,h.branch)
rows=[]
for n in range(6,12):
 old=compile_nnmhv_histories(n);new=compile_nnmhv_histories(n+1);lookup={key(h):i for i,h in enumerate(new)};image=[lookup.get(key(h)) for h in old];created=[i for i in range(len(new)) if i not in set(image)];m=n-4;expected=sum(r*r for r in range(1,m+1))
 rows.append({'map':f'V_{n}->V_{n+1}','source_dimension':len(old),'target_dimension':len(new),'embedded_indices':image,'created_shell_dimension':len(created),'created_indices':created,'sum_of_squares_shell_dimension':expected})
checks={'all_endpoint_branch_embeddings_exist':all(all(i is not None for i in r['embedded_indices']) for r in rows),'all_embeddings_injective':all(len(set(r['embedded_indices']))==r['source_dimension'] for r in rows),'orthogonal_counting_decomposition':all(r['source_dimension']+r['created_shell_dimension']==r['target_dimension'] for r in rows),'created_shell_is_sum_of_squares':all(r['created_shell_dimension']==r['sum_of_squares_shell_dimension'] for r in rows)}
out={'schema':'marici.nima.nnmhv-history-fock-refinement.v1','decomposition':'V_(n+1) = iota_n(V_n) direct_sum W_(n+1)','metric':'history basis orthonormal counting metric','rows':rows,'checks':checks,'passed':all(checks.values()),'interpretation':{'iota_n':'isometric retention of endpoint-pair/branch histories','W_(n+1)':'newly created history shell','creation_dimension':'dim W_(n+1) = sum_(r=1)^(n-4) r^2','reflow':'change of canonical weights on the retained subspace, not creation of basis states'}};p=ROOT/'research/nima/results/nnmhv-history-fock-refinement.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
