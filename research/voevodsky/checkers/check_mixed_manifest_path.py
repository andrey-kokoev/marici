"""Individually scoped weakening edges do not compose across row generations."""
from pathlib import Path
import json
A={'src':'start','dst':'middle','rule':'weakening','manifest':'rows-A','generation':1,'src_target':(1,0,1),'dst_target':(1,0,2)}
B={'src':'middle','dst':'end','rule':'weakening','manifest':'rows-B','generation':2,'src_target':(1,0,2),'dst_target':(1,0,3)}
C=dict(B,manifest='rows-A',generation=1)
def local(edge):return edge['rule']=='weakening' and edge['src_target'][:2]==edge['dst_target'][:2] and edge['src_target'][2]<=edge['dst_target'][2]
def compose(left,right):
 assert local(left) and local(right)
 if left['dst']!=right['src'] or left['dst_target']!=right['src_target']:return 'MIDDLE_OCCURRENCE_OR_TARGET_MISMATCH'
 if (left['manifest'],left['generation'])!=(right['manifest'],right['generation']):return 'SOURCE_GENERATION_MISMATCH_NEEDS_TYPED_MIGRATION'
 return 'LOCAL_COMPOSABLE_SAME_SOURCE'
assert local(A) and local(B)
assert compose(A,B)=='SOURCE_GENERATION_MISMATCH_NEEDS_TYPED_MIGRATION'
assert compose(A,C)=='LOCAL_COMPOSABLE_SAME_SOURCE'
assert compose(A,dict(C,src_target=(1,0,1)))=='MIDDLE_OCCURRENCE_OR_TARGET_MISMATCH'
report={'passed':True,'two_individually_valid_scopes':'rows-A generation1 then rows-B generation2','mixed_path':'SOURCE_GENERATION_MISMATCH_NEEDS_TYPED_MIGRATION','same_source_control':'LOCAL_COMPOSABLE_SAME_SOURCE','middle_target_mismatch':'rejected even on same manifest','scope':'Synthetic scope checks, not actual proofs, migrations, owner grants or analytic roles.'}
out=Path(__file__).resolve().parents[1]/'results/mixed-manifest-path.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
