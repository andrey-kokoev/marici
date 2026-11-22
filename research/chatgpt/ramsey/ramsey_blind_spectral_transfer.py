"""Transfer unchanged trial to the prior held-out record list, cyclic 35 and Exoo39. Symmetry-equivalent deletions counted once within each parent."""
from ramsey_blind_spectral_attachment import *
from exoo39_symbolic_relations import edges

def run():
    ix=json.loads((D/'ramsey_template_transfer_records.json').read_text());ls=gzip.decompress((D/'pauli-realization-catalogues/r38_27.g6.gz').read_bytes()).splitlines();gs=[(8,i,nx.from_graph6_bytes(ls[i-1])) for i in ix];G=nx.Graph();G.add_nodes_from(range(35));G.add_edges_from((v,(v+x)%35) for v in G for x in (1,7,11,16));F=nx.Graph();F.add_nodes_from(range(39));F.add_edges_from(edges());gs.extend([(9,1,G),(10,1,F)]);rows=[]
    for k,i,g in gs:
        A=nx.to_numpy_array(g,nodelist=range(len(g)));assert max(s.bit_count() for s in independent(A))==k-1
        for o in orbit_reps(g):
            v=o[0];keep=np.arange(len(A))!=v;rows.append(dict(k=k,record=i,root=v,multiplicity=len(o),size=g.degree(v),**trial(A[keep][:,keep],g.degree(v),k-1,100*i+v)))
    with (D/'ramsey_blind_spectral_transfer.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    for k in (8,9,10):
        rs=[r for r in rows if r['k']==k];parents={r['record'] for r in rs};print(k,len(rs),[round(np.mean([np.mean([r[key] for r in rs if r['record']==i]) for i in parents]),2) for key in ['spectral','common','degree','random_xy','uniform']])
if __name__=='__main__':run()
