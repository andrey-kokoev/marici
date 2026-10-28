"""Execute existing retained-family promotion twice on the oscillator source.
Loads only named pure definitions from the owner checker, not its fixture/IO.
"""
import ast
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sympy as s
from check_oscillator_fibration_cut import transfer

ROOT = Path(__file__).resolve().parents[3]
OWNER = 'research/nima/checkers/check_rung_transport_diagram.py'


def promotion_api():
    tree = ast.parse((ROOT/OWNER).read_text(encoding='utf-8'))
    names = {'Row', 'mean', 'indexed', 'unindex', 'incoming_promotion', 'leaves'}
    definitions = [n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.ClassDef)) and n.name in names]
    assert {n.name for n in definitions} == names
    # The original linear aggregate helpers specialized to scalar coefficients.
    env = {'dataclass':dataclass,'defaultdict':defaultdict,'F':F,
           'scale':lambda q,x:q*x,'add':lambda x,y:x+y}
    exec(compile(ast.Module(body=definitions,type_ignores=[]),OWNER,'exec'),env)
    return env


def main():
    api=promotion_api()
    Row, promote, leaves, indexed, unindex = (api[k] for k in ('Row','incoming_promotion','leaves','indexed','unindex'))
    g,h=s.symbols('g h', positive=True,real=True)
    d=s.symbols('delta',real=True)
    chi=1/((g*g+h*h)/2-s.I*d)
    source=tuple(Row(('leaf',i),(a,),(b,),v) for i,(v,a,b) in enumerate(((g*chi,0,2),(h*chi,1,2),(-g,2,3),(s.Integer(1),0,3))))
    def read(rows):
        primitive=tuple((r.value,r.source[0],r.target[0]) for r in leaves(rows))
        return (transfer(primitive,0,3),transfer(primitive,1,3))
    expected=read(source)
    fixture={g:1,h:2,d:0}
    reports={}
    for policy in ('inherited','common'):
        stage1=promote(source,1,policy)
        stage2=promote(stage1,2,policy)
        assert leaves(stage1)==source and leaves(stage2)==source
        assert tuple(c for r in stage2 for c in r.members)==stage1
        assert {r.label for r in source}.isdisjoint(r.label for r in stage1)
        assert {r.label for r in stage1}.isdisjoint(r.label for r in stage2)
        assert sum(r.mass for r in stage2)==4
        presentations=[]
        for depth,rows in enumerate((source,stage1,stage2)):
            by_from=indexed(rows,'source')
            by_to=indexed(rows,'target')
            assert unindex(by_from)==unindex(by_to)==rows
            # Actual three presentations and their comparison routes.
            assert indexed(unindex(by_from),'target')==by_to
            for view in (rows,unindex(by_from),unindex(by_to)):
                got=read(view)
                assert all(s.simplify(a-b)==0 for a,b in zip(got,expected))
            presentations.append({'depth':depth,'records':len(rows),
                                  'from_fibers':len(by_from),'to_fibers':len(by_to)})
        rr,qq=read(stage2)
        assert s.simplify(rr*s.conjugate(rr)+qq*s.conjugate(qq)-1)==0
        # Poisoning a nested bath coefficient must not be hidden by reconstruction
        # from a separately saved input: recursively copy records with that leaf zero.
        def erase_bath(row):
            if row.members:
                return Row(row.label,row.source,row.target,row.value,row.mass,tuple(erase_bath(c) for c in row.members))
            return Row(row.label,row.source,row.target,s.Integer(0) if row.label==('leaf',1) else row.value,row.mass,row.members)
        bad=tuple(erase_bath(r) for r in stage2)
        br,bq=read(bad)
        assert bq==0 and br==rr
        assert s.simplify((br*s.conjugate(br)+bq*s.conjugate(bq)).subs(fixture))==s.Rational(9,25)
        reports[policy]={
            'record_counts':[len(source),len(stage1),len(stage2)],
            'fresh_labels':[[list(r.label) for r in rows] for rows in (stage1,stage2)],
            'presentations':presentations,
            'intermediate_records_recovered':True,'original_coefficient_rows_recovered':True,
            'resonant_r':str(rr.subs(fixture)),'resonant_q':str(qq.subs(fixture)),
            'resonant_commutator_weight':'1',
            'nested_bath_erasure_commutator_weight':'9/25',
            'source_leaf_ids':[list(r.label) for r in leaves(stage2)],
        }
    assert reports['inherited']['record_counts']==[4,2,2]
    assert reports['common']['record_counts']==[4,2,1]
    sources=[OWNER,'research/aspect/markov-oscillator-loss-noise-identity.md',str(Path(__file__).relative_to(ROOT)).replace('\\','/'),'research/strominger/checkers/check_oscillator_fibration_cut.py']
    result={'status':'pass','operation':'actual incoming_promotion definition; scalar specialization of linear aggregate helpers',
            'policies':reports,
            'scope':'Two retained generative family promotions, not endpoint transposition. The triangle is raw/from-indexed/to-indexed presentations, not three physical ports. No FCC or universal law-domain equivalence follows from the presentation triangle alone.',
            'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources}}
    out=ROOT/'research/strominger/results/oscillator-family-promotion/verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
