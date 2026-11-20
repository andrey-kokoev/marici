"""All maximal twin choices on the 35-circle up to translations/reflection. Count arbitrary legal next borders."""
from ramsey_clique_power_blowup import layers
S={1,7,11,16,19,24,28,34}
for d in [1,7,11,16]:
    parent=[*range(35),0,d];adj=[sum(1<<i for i,y in enumerate(parent) if (y-x)%35 in S) for x in parent];ss=layers(adj);nine=[s for s in ss if s.bit_count()==9];assert max(map(int.bit_count,ss))==9 and all(row in ss for row in adj)
    legal=[s for s in ss if all(s&t for t in nine)];print('distance',d,'blue nines',len(nine),'arbitrary borders',len(legal),flush=True)
