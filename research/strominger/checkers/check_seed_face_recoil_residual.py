"""Exact endpoint comparison for the EXISTING six-port/generalized-body adapter.
Tests a candidate equality, not the existence of a native face witness.
Reads the registry and pure operator expressions without executing owner IO.
"""
import ast
import hashlib
import json
from pathlib import Path
import sympy as S

ROOT=Path(__file__).resolve().parents[3]
REGISTRY='research/nima/checkers/check_natural_tower_return.py'
ADAPTER='research/nima/checkers/check_seed_port_exchange_binding.py'


def main():
    registry_tree=ast.parse((ROOT/REGISTRY).read_text(encoding='utf-8'))
    packets=next(ast.literal_eval(n.value) for n in registry_tree.body
                 if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PACKETS' for t in n.targets))
    registry={name:(a,b) for name,a,b in packets}
    labels=tuple(registry)
    env={'S':S,'registry':registry,'labels':labels,'vertices':{v:i for i,v in enumerate('ABCD')}}
    tree=ast.parse((ROOT/ADAPTER).read_text(encoding='utf-8'))
    assignments=[n for n in tree.body if isinstance(n,ast.Assign)
                 and len(n.targets)==1 and isinstance(n.targets[0],ast.Name)
                 and n.targets[0].id in {'G','H','features','metric','operators'}]
    assert {n.targets[0].id for n in assignments}=={'G','H','features','metric','operators'}
    exec(compile(ast.Module(body=assignments,type_ignores=[]),ADAPTER,'exec'),env)
    # Use the actual first loop's pure exchange expressions, not its numerical
    # comparison/imported fixtures or any receipt-writing code.
    loop=next(n for n in tree.body if isinstance(n,ast.For))
    body=[]
    for n in loop.body:
        if not isinstance(n,ast.Assign) or len(n.targets)!=1:
            continue
        t=n.targets[0]
        if (isinstance(t,ast.Name) and t.id in {'f','mismatch','direction','E'}) or (
                isinstance(t,ast.Subscript) and isinstance(t.value,ast.Name) and t.value.id=='operators'):
            body.append(n)
    assert len(body)==5
    selected=ast.For(target=loop.target,iter=loop.iter,body=body,orelse=[])
    exec(compile(ast.fix_missing_locations(ast.Module(body=[selected],type_ignores=[])),ADAPTER,'exec'),env)
    F,H,ops,metric=(env[k] for k in ('features','H','operators','metric'))
    D=F.T*H*F
    assert D.rank()==6
    # At the real, zero-configuration endpoints the shared cotangent map is
    # P0=F^T H y, pi=r. It is injective on y in span(F), inverse y=F D^-1 P0.
    body_map=S.diag(F.T*H,S.eye(6))
    lift=S.diag(F,S.eye(6))
    assert body_map*lift==S.diag(D,S.eye(6))
    assert (body_map*lift).rank()==12
    kinetic=S.diag(D.inv(),S.eye(6))
    body_ops={}
    for i,label in enumerate(labels):
        ei=S.eye(6)[:,i]
        direction=(D*ei).col_join(-ei)
        mismatch=(-ei.T).row_join(ei.T)
        B=S.eye(12)+direction*mismatch
        body_ops[label]=B
        assert body_map*ops[label]*lift==B*body_map*lift
        assert B.T*kinetic*B==kinetic
        assert S.eye(6).row_join(D)*B==S.eye(6).row_join(D)
    def run(word):
        assert all(registry[a][1]==registry[b][0] for a,b in zip(word,word[1:]))
        E=S.eye(22)
        for label in word:
            E=ops[label]*E
        return E
    e=S.eye(6)[:,labels.index('AB')]
    initial=S.zeros(16,1).col_join(e)
    direct=run(('AB',))*initial
    indirect=run(('AD','DB'))*initial
    assert registry['AB']==(registry['AD'][0],registry['DB'][1])
    # Explicitly compare the full carrier/record outputs.
    assert indirect==initial
    assert direct==(F*e).col_join(S.zeros(6,1))
    md,mi=body_map*direct,body_map*indirect
    assert md==(D*e).col_join(S.zeros(6,1))
    assert mi==S.zeros(6,1).col_join(e)
    assert md!=mi
    total=S.eye(6).row_join(D)
    assert total*md==total*mi==D*e
    assert (md.T*kinetic*md)[0]/2==(mi.T*kinetic*mi)[0]/2==S.Rational(1,2)
    assert md[6+labels.index('AB')]==0 and mi[6+labels.index('AB')]==1
    # Repeat the old honest control: AB-only preparation does NOT distinguish
    # the return protocols, although their full operators differ.
    assert run(('BA',))*initial==run(('BC','CA'))*initial
    assert run(('BA',))!=run(('BC','CA'))
    # Matrix involution is not a claim that AB;AB is a directed seed path.
    assert ops['AB']*ops['AB']==S.eye(22)
    paths=[REGISTRY,ADAPTER,'research/nima/shared-recoil-cotangent-binding.md',
           'research/nima/checkers/check_shared_recoil_cotangent_binding.py',
           str(Path(__file__).relative_to(ROOT)).replace('\\','/')]
    result={'status':'pass','disposition':'endpoint_flattening_rejected_in_shared_recoil_readout',
            'direct':['AB'],'indirect':['AD','DB'],'preparation':'existing unit AB record; zero carrier',
            'mechanical_difference':[str(x) for x in md-mi],
            'record_AB_momenta':['0','1'],'equal_total_generalized_momentum':True,
            'endpoint_kinetic_energy_each':'1/2','all_six_endpoint_intertwining_equations':True,
            'return_protocol_AB_preparation_control':'same output; different operators',
            'boundary':'No native face between these free routes is asserted. No no-go for a nontrivial witness action. Endpoint-only regression, not a fresh full cotangent/intermediate-pulse check.',
            'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    out=ROOT/'research/strominger/results/seed-face-recoil-residual/verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
