"""Exact controls for the written whole-record external-return proof."""
from pathlib import Path
from fractions import Fraction as F
import contextlib
import hashlib
import io
import json

# Re-run the local-core algebraic checks and reuse exactly that constructor.
with contextlib.redirect_stdout(io.StringIO()):
    import check_uniform_local_core as M
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,condition):
    if not condition: raise AssertionError(name)
    checks.append(name)

def path_operator(tag,segment,c,s):
    first,second=(M.right,M.left) if tag==0 else (M.left,M.right)
    if segment==0:
        return M.phase(M.projector(first),c,s)
    return M.cmul(M.phase(M.projector(second),c,s),(first,M.Z))

def state(operator,label):
    return tuple(tuple(part[i][label] for i in range(4)) for part in operator)
def basis(label):
    return tuple(F(i==label) for i in range(4)),tuple(F(0) for _ in range(4))
def norm(v): return sum(x*x for part in v for x in part)
def swap_state(v):
    return tuple(tuple(part[((i&1)<<1)|(i>>1)] for i in range(4)) for part in v)

for source in range(4):
    target=source^3
    seams=[]
    for tag in (0,1):
        check(f'start/{source}/{tag}',state(path_operator(tag,0,F(1),F(0)),target)==basis(target))
        end_first=path_operator(tag,0,F(-1),F(0))
        start_second=path_operator(tag,1,F(1),F(0))
        check(f'seam-operator/{source}/{tag}',end_first==start_second)
        seam=state(end_first,target); seams.append(seam)
        check(f'seam-native-corner/{source}/{tag}',seam==basis(source^(2 if tag==0 else 1)))
        check(f'finish/{source}/{tag}',state(path_operator(tag,1,F(-1),F(0)),target)==basis(source))
        for segment in (0,1):
            for k,(c,s) in enumerate(M.phases):
                op=path_operator(tag,segment,c,s)
                check(f'unitary/{source}/{tag}/{segment}/{k}',M.cmul(M.adj(op),op)==(M.I,M.Z))
                check(f'norm/{source}/{tag}/{segment}/{k}',norm(state(op,target))==1)
                swapped_source=((source&1)<<1)|(source>>1)
                swapped=state(path_operator(1-tag,segment,c,s),swapped_source^3)
                check(f'factor-exchange/{source}/{tag}/{segment}/{k}',swap_state(state(op,target))==swapped)
    check(f'schedule-distinguished-at-seam/{source}',seams[0]!=seams[1])
    encoded_pairs={(seams[r],seams[q]) for r in (0,1) for q in (0,1)}
    check(f'all-four-tag-pairs-distinguished/{source}',len(encoded_pairs)==4)
    for r in (0,1):
        for q in (0,1):
            pair=(seams[r],seams[q])
            check(f'schedule-pair-swap/{source}/{r}/{q}',(seams[q],seams[r])==tuple(reversed(pair)))

classification=json.loads((ROOT/'results/agda-TickRetainedStructure.json').read_text(encoding='utf-8-sig'))
check('source-classification-receipt-current',classification['passed']
      and classification['source_sha256']==hashlib.sha256((ROOT/'agda/TickRetainedStructure.agda').read_bytes()).hexdigest())
fresh=json.loads((ROOT/'results/spectral-return-source-classification.json').read_text(encoding='utf-8'))
check('fresh-source-classification-closure',fresh['status']=='pass' and fresh['fresh_dependency_check']
      and fresh['source_sha256']==classification['source_sha256'])
core=json.loads((ROOT/'results/uniform-local-core.json').read_text(encoding='utf-8'))
contract=json.loads((ROOT/'contracts/spectral-whole-return-test.v1.json').read_text(encoding='utf-8'))
check('same-witness-as-local-core',contract['witness']==core['witness'] and core['outcome']=='++')
paths=[Path(__file__).resolve(),ROOT/'contracts/spectral-whole-return-test.v1.json',ROOT/'spectral-whole-return-proof.md',
       ROOT/'checkers/check_uniform_local_core.py',ROOT/'results/uniform-local-core.json',
       ROOT/'agda/TickRetainedStructure.agda',ROOT/'results/agda-TickRetainedStructure.json',
       ROOT/'results/spectral-return-source-classification.json']
r={'status':'pass','outcome':'++','claim':contract['claim_id'],'witness':contract['witness'],
   'semantic_backend':contract['semantic_backend'],'return_meaning':contract['return_meaning'],
   'checks_passed':len(checks),'checks':checks,
   'proof_kind':'written_all_time_analytic_and_whole_record_argument_with_exact_checks',
   'kernel_verified_analytic_theorem':False,
   'completion_backend_verified':False,'cubical_pointwise_decoder_constructed':False,'C1_at_seam_claimed':False,
   'source_sha256':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(ROOT/'results/spectral-whole-return.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in r.items() if k!='checks'},indent=2))
