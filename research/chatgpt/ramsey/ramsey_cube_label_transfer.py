"""Natural-hypercube net: distinguish a component ID from a cube coordinate and test literal domain of the (3,7) label. Full fixed-table automorphism action at 3,8 and 3,9. Group edges by orbit and by endpoint signature sizes; compare independent saved states. For old templates use ALL compared images, not just their representatives."""
from itertools import permutations,combinations
from collections import Counter
from ramsey_address_to_cube import S as nine,D,json
load=lambda n:json.loads((D/(n+'.json')).read_text());six=list(combinations(range(6),2));old=list((a,b) for a,b in combinations(range(15),2) if set(six[a]).isdisjoint(six[b]));masks=[m for t in load('ramsey_six_component_label')['greedy_counts'] for m in t['masks']];links={i for m in masks for i in range(45) if m>>i&1};used=sorted({six[j] for i in links for j in old[i]});
def audit(S,W):
    E=[(a,b) for a,b in combinations(range(len(S)),2) if not S[a]&S[b]];ei={e:i for i,e in enumerate(E)};n=max(S).bit_length();subs=[tuple(i for i in range(n) if m>>i&1) for m in S];si={v:i for i,v in enumerate(S)};G=[]
    for p in permutations(range(n)):
        try:g=[si[sum(1<<p[i] for i in t)] for t in subs]
        except KeyError:continue
        G.append([ei[tuple(sorted((g[a],g[b])))] for a,b in E])
    orbit={sum((W[0]>>i&1)<<j for i,j in enumerate(g)) for g in G};assert orbit==set(W);left=set(range(len(E)));desc=[];classes=Counter();red=Counter()
    while left:
        k=min(left);o={g[k] for g in G};left-=o;counts={sum(w>>j&1 for j in o) for w in W};assert len(counts)==1;num=counts.pop();a,b=E[k];desc.append(dict(rep=[subs[a],subs[b]],links=len(o),red=num));shape=str(tuple(sorted([len(subs[a]),len(subs[b])])));classes[shape]+=len(o);red[shape]+=num
    # Test any injection of the old six primitive labels into the new primitive labels, not arbitrary retyping.
    duads={tuple(t) for t in subs if len(t)==2};best=max(sum(tuple(sorted((p[i],p[j]))) in duads for i,j in used) for p in permutations(range(n),6));return dict(actions=len(G),state_orbit=len(orbit),red_by_type=red,possible_by_type=classes,orbit_counts=desc,best_duads_transferred=best)
a=load('ramsey_seven_all_wirings');r=dict(needed_old_duads=len(used),old_duads=used,k8=audit(a['address_masks'],a['wirings']),k9=audit(nine,load('ramsey_nine_frame_readout')['coordinate_ordered_wirings']));print([(k,r[k]['red_by_type'],r[k]['possible_by_type'],r[k]['best_duads_transferred'],[v['red'] for v in r[k]['orbit_counts']]) for k in ('k8','k9')],len(used));(D/'ramsey_cube_label_transfer.json').write_text(json.dumps(r,indent=2)+'\n')
