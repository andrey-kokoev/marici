"""Exact four-event, degree-zero slice of the raw-to-minimal loss.

All retained windows lie in the fixed external context in this slice,
so each contextual row has a single common nonzero window-pair factor.
No independent artificial window variables or midpoint ranks are used.
"""
from pathlib import Path
from itertools import combinations,permutations
from collections import defaultdict
import runpy,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
v=runpy.run_path(str(ROOT/'research/voevodsky/certificates/verify_minimal_matched_retention.py'))
m=json.loads((ROOT/'research/grothendieck/results/finite-cubic-observer.json').read_text())
rows={v['frozen'](r['shape']):(r['sign'],r['coefficient']) for r in m['rows']}
others=v['other_shapes']();selected=v['SHAPE'];profile=v['profile']
results=[]
for inside in combinations(range(6),4):
    outside=tuple(k for k in range(6) if k not in inside)
    words=list(permutations(inside));I=s.Matrix(24,23,lambda i,j:int(i==j+1)-int(i==0))
    # Complete minimal forgotten I^2 basis at these endpoints.
    pairs=sorted({tuple(tuple(sorted(w[k:k+2])) for k in (0,2)) for w in words})
    products=[v['multiply'](v['forgotten'](p[0]),v['forgotten'](p[1])) for p in pairs]
    I2=s.Matrix([[col.get((w,(0,)*4),0) for col in products] for w in words])
    for prefix_size in range(3):
        for pre_set in combinations(outside,prefix_size):
            post_set=tuple(k for k in outside if k not in pre_set)
            raw={};minimal={}
            for pre in permutations(pre_set):
                for post in permutations(post_set):
                    ctx=(pre,post)
                    for idx,w in enumerate(words):
                        col={(pre+w+post,(1,)*len(pre)+(0,)*4+(1,)*len(post)):1}
                        image=profile(col)
                        assert not any(shape in others for shape,windows in image)
                        for (shape,windows),value in image.items():
                            if shape not in rows:continue
                            sign,label=rows[shape]
                            assert label=='crossed' # reserved positive block is absent
                            raw.setdefault((ctx,shape),[0]*24)[idx]+=value
                            minimal.setdefault((ctx,'combined'),[0]*24)[idx]+=sign*value
                            if shape==selected:minimal.setdefault((ctx,'selected'),[0]*24)[idx]+=value
            R=s.Matrix(list(raw.values())) if raw else s.zeros(0,24)
            M=s.Matrix(list(minimal.values())) if minimal else s.zeros(0,24)
            rank=lambda A:A.rank()
            rr,mr=rank(R*I),rank(M*I)
            rr2,mr2=rank(R*I2),rank(M*I2)
            if rr==mr:continue
            null=(M*I).nullspace()
            basis=[];images=s.zeros(R.rows,0)
            for n in null:
                source=I*n;image=R*source
                enlarged=images.row_join(image)
                if enlarged.rank()>images.cols:
                    basis.append([{'word':list(w),'coefficient':str(c)} for w,c in zip(words,source) if c])
                    images=enlarged
            assert len(basis)==rr-mr
            witness=basis[0]
            results.append({'start_mask':sum(1<<p for p in pre_set),
                'end_mask':sum(1<<p for p in pre_set+inside),
                'event_indices':inside,'raw_rank':rr,'minimal_rank':mr,
                'loss_dimension':rr-mr,'inherited_second_level_loss':rr2-mr2,
                'witness':witness,'source_basis':basis})
# Close the five source generators under all possible retained left paths.
# A forgotten left edge kills their observation; no right extension fits.
# For each fixed two-retained prefix, all rows share one physical factor,
# so rescaling each column by that nonzero factor preserves its rank.
levels={};branches={};action_columns=[]
for r in results:
    initial=tuple(p for p in range(6) if r['start_mask']&(1<<p))
    for generator_index,generator in enumerate(r['source_basis']):
        h={(tuple(t['word']),(0,)*4):s.Rational(t['coefficient']) for t in generator}
        for prefix in permutations(initial):
            full=v['multiply']({(prefix,(1,1)):1},h)
            image=profile(full)
            assert not any(shape in others or shape==selected for shape,w in image)
            assert sum(rows[shape][0]*c for (shape,w),c in image.items() if shape in rows)==0
            vector=[sum(c for (shape,w),c in image.items() if shape==sh) for sh in rows]
            action_columns.append({'origin_start_mask':r['start_mask'],'generator_index':generator_index,
                'retained_prefix':prefix,'common_window_masks':[[0,1<<prefix[0]],[1<<prefix[0],r['start_mask']]],
                'raw_row_coefficients':[[index,str(c)] for index,c in enumerate(vector) if c]})
            branches.setdefault((r['start_mask'],prefix),[]).append(vector)
            for degree,start in ((1,1<<prefix[0]),(2,0)):
                levels.setdefault((degree,start),[]).append(vector)
closure=[{'retained_degree':q,'start_mask':start,'end_mask':63,
          'dimension':s.Matrix(columns).rank()} for (q,start),columns in sorted(levels.items())]
branch_ranks=[{'origin_start_mask':origin,'retained_prefix':prefix,'rank':s.Matrix(cols).rank()}
              for (origin,prefix),cols in sorted(branches.items())]
assert sum(b['rank'] for b in branch_ranks)==7
assert sum(c['dimension'] for c in closure if c['retained_degree']==2)==5
result={'passed':True,'retained_prefix_branch_ranks':branch_ranks,'source_action_columns':action_columns,'slice':'retained degree zero, exactly four source events',
 'nonzero_loss_corners':results,'slice_loss_dimension':sum(r['loss_dimension'] for r in results),
 'slice_second_level_dimension':sum(r['inherited_second_level_loss'] for r in results),
 'generated_submodule_additional_corners':closure,
 'generated_submodule_dimension':sum(r['loss_dimension'] for r in results)+sum(c['dimension'] for c in closure),
 'scope':'Exact slice only, not the complete loss module. Rank identification assumes the owning common filter is nonzero on the external retained windows. Source witnesses and row cancellations are exact independently of response magnitudes.'}
(ROOT/'research/voevodsky/results/four-event-raw-retention-loss.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
