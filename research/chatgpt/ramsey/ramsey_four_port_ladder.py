"""Construct a four-level nested ladder from just the 17-vertex source. Test capacity on the late cores."""
from ramsey_port_chain_from_17 import read_seed,D,search,json
from ramsey_hall_center_conjecture import independent
A=read_seed((D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines()[4]);assert not independent(A,(1<<17)-1,6);out=[]
for k in (7,8,9,10):
    possible_five=None
    if k>=9:possible_five='graph' in search(A,k,5)
    r=search(A,k,4);A=r['graph'];I=[0]
    for i,row in enumerate(A):I += [s|1<<i for s in I if not s&row]
    top=[s for s in I if s.bit_count()==k-1];single=sum(all(s&t for t in top) for s in I);result={'k':k,'supports':r['supports'],'graph':A,'top_set_count':len(top),'same_level_single_extensions':single,'five_ports_possible_on_input':possible_five};out.append(result);print(k,len(A),[s.bit_count() for s in r['supports']],len(top),single,possible_five)
(D/'ramsey_four_port_ladder.json').write_text(json.dumps(out,indent=2)+'\n')
