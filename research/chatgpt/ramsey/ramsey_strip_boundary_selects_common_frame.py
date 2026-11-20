"""Select from common-frame single-component matchings using only directed boundary flags; do not impose a precomputed short route or shared residue."""
from ramsey_common_frame_components import out,frame,turn,GS
from ramsey_strip_distance_layer_split import matching as crossing,active
from collections import Counter
family0=[m for m in out if len(m&turn(m))==10];assert len(family0)==16
for label,flags in [('none',set()),('entry',{(0,16)}),('entry and opposite-row exit',{(0,16),(7,29)}),('entry and same-row exit',{(0,16),(4,29)})]:
 selected=[m for m in family0 if flags<=m];print(label,'matchings',len(selected),'cyclic frames',len({frame[m] for m in selected}));
 if label=='entry and opposite-row exit':
  m,=selected;assert m&turn(m)==crossing;assert {v for e in m^turn(m) for v in e}==active;print('selected residue agrees with geometric crossing completion',True)
print('row-compatible cyclic frame fixed ground labels',Counter(next(x for x in range(6) if all(p[x]==x for p in GS[k])) for k in {frame[m] for m in family0}))
