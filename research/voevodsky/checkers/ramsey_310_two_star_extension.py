"""Can any two legal stars over the fixed 38-prefix coexist? Include twins."""
import json
from itertools import combinations_with_replacement
from ramsey_310_attachment_index import got, sets, HOME

eights=[m for m in sets if m.bit_count()==8]; pairs=list(combinations_with_replacement(sorted(got),2)); reasons={};legal=[]
for a,b in pairs:
    common=a&b;miss=next((e for e in eights if not e&(a|b)),0)
    if not common:legal.append([a,b,'+'])
    if not miss:legal.append([a,b,'-'])
    reasons[str((a,b))]={'shared_plus_vertex':(common&-common).bit_length()-1 if common else None,'unmet_minus_eight':miss or None}
r=dict(prefix_vertices=38,stars=len(got),unordered_pairs_including_twins=len(pairs),sign_assignments=2*len(pairs),legal=legal,blocking_witnesses=reasons)
(HOME/'results/ramsey_310_two_star_extension.json').write_text(json.dumps(r,indent=2)+'\n');print(len(pairs),len(legal))
