"""Run all four diagram conjectures through shared exact gates at all four faces.

The released-loop case is an explicit six-agent regional rewrite introducing one
six-port identity junction. It is a candidate macro rule, not an assumed particle
law or a compilation into elementary principal-pair rewrites.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter
from itertools import combinations
from math import hypot
from html import escape
import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from interaction_conjecture_harness import *
from draw_canonical_proton_net import tutte,check_planar
from check_twenty_four_triangle_shared_seed import proper,SWAP

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results'/'interaction-conjectures'
REQUIRED=('linear_ownership','stagewise_geometry','seed_sector_response','collective_identity','full_retained_port_response',
          'distinct_companion_geometry','compact_companion_mode','opposite_inherited_currents')


def positive_baseline(points,triangles): return geometry(points,list(triangles.values()))
def zplus(a,b): return tuple(tuple(zadd(x,y) for x,y in zip(r,s)) for r,s in zip(a,b))
def ztimes(a,c): return tuple(tuple(zscale(z,c) for z in r) for r in a)
def conjmat(a): return tuple(tuple(zconj(z) for z in r) for r in a)

def render(net,triangles,face,cap,names,L,mode,path):
    selected=set(face_cycle(triangles,face)[0]);a,b,c=cap;d=next(x for x in LABELS if x not in cap)
    adjacency={name:set() for name in names}
    for i,x in enumerate(names):
        for j,y in enumerate(names):
            if i!=j and L[i][j]: adjacency[x].add(y)
    body={x:{y for y in ys if y not in selected} for x,ys in adjacency.items() if x not in selected}
    fixed={'J':(730,490),b+a:(535,130),a+d:(130,190),d+a:(130,790),a+c:(535,850)}
    pos=tutte(body,fixed)
    pos.update({a+b:(F(1220),F(180)),b+c:(F(1220),F(800)),c+a:(F(1057),F(490))})
    edges=[(x,y) for i,x in enumerate(names) for y in names[i+1:] if y in adjacency[x]]
    check_planar(pos,edges)
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1390" height="1020" viewBox="0 0 1390 1020">',
           '<defs><marker id="head" viewBox="0 0 6 6" refX="5.5" refY="3" markerWidth="7" markerHeight="7" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0 L6 3 L0 6 Z" fill="#704473"/></marker></defs>',
           '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#233449}</style>',
           '<rect width="1390" height="1020" fill="#fcfdff"/>',
           f'<text x="35" y="40" font-size="25" font-weight="650">Released-loop candidate — {face.replace("F_", "face ")}</text>',
           '<text x="35" y="70" font-size="15">Original triangle records retained · one shared junction · exact eigenvalue 5 on both circulating components</text>']
    for x,y in edges:
        i,j=names.index(x),names.index(y);w=-L[i][j]
        current=w*zmul(zconj(mode[i]),mode[j])[1]
        if current<0:x,y=y,x;current=-current
        px,py=map(float,pos[x]);qx,qy=map(float,pos[y]);length=hypot(qx-px,qy-py)
        dx,dy=(qx-px)/length,(qy-py)/length
        r1=29 if x=='J' else 22;r2=29 if y=='J' else 22
        px,py=px+r1*dx,py+r1*dy;qx,qy=qx-r2*dx,qy-r2*dy
        col='#aaaeb7' if current==0 else '#704473'
        width=1.6 if current==0 else float(current)*2+1
        marker='' if current==0 else ' marker-end="url(#head)"'
        parts.append(f'<path d="M{px:.3f} {py:.3f} L{qx:.3f} {qy:.3f}" stroke="{col}" stroke-width="{width}" fill="none"{marker}><title>{x} to {y}; conductance {w}; oriented current magnitude {current} sqrt(3)</title></path>')
        if 'J' in (x,y):parts.append(f'<text x="{(px+qx)/2+5:.3f}" y="{(py+qy)/2-6:.3f}" font-size="11" fill="#858b97">2</text>')
    for name in names:
        x,y=map(float,pos[name]);junction=name=='J'
        col='#f7e9bd' if junction else '#fff0dd' if name in selected else '#e9f2fb'
        parts.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{26 if junction else 19}" fill="{col}" stroke="#355069" stroke-width="2"/>')
        parts.append(f'<text x="{x:.3f}" y="{y+5:.3f}" text-anchor="middle" font-size="14" font-weight="650">{"I" if junction else name}</text>')
    parts+=['<text x="365" y="935" text-anchor="middle" font-size="17">Body: three loops × +1 current unit</text>',
            '<text x="1060" y="935" text-anchor="middle" font-size="17">Companion: one loop × −3 units</text>',
            '<text x="35" y="975" font-size="13">Current unit = sqrt(3)/2 in the inherited seed normalization. Grey connections carry zero current in this state.</text>',
            '<text x="35" y="998" font-size="13">The junction has zero amplitude in the circulating modes; the constant identity mode remains shared. Charge identification is not assumed.</text>',
            '</svg>']
    path.write_text('\n'.join(parts)+'\n',encoding='utf-8');ET.parse(path)


def released_case(net,points,triangles,face):
    case=Case('released_loop',face)
    candidate,selected,cap=release(net,triangles,face)
    case.check('linear_ownership',lambda: set(owners(candidate))==set(owners(net)) and len(owners(candidate))==12)
    # Atomic stellar expansion of the already present face-centre record.
    # At t=0 the released patch is a positive 2D face; for t>0 it is a positive
    # 3D tetrahedron. The full carrier has positive volume throughout.
    geom=[]
    def check_geometry():
        geom.append({'stage':'source','carrier':positive_baseline(points,triangles)})
        for t in (F(1,4),F(1,2),F(3,4),F(1)):
            new,body,comp,g=release_geometry(points,triangles,face,cap,1+2*t)
            geom.append({'stage':'stellar expansion','parameter':str(t),**g})
        certificate=geometry_path_certificate(points,new,
            (('body',body,False),('companion',comp,True),('union',list(triangles.values()),False)))
        return {'stages':geom,'whole_path_certificate':certificate}
    case.check('stagewise_geometry',check_geometry)
    case.check('seed_sector_response',lambda:seed_response(candidate))
    new,body,comp,g=release_geometry(points,triangles,face,cap)
    case.check('distinct_companion_geometry',lambda:set(map(frozenset,body))!=set(map(frozenset,comp)) and F(g['companion']['volume'])>0)
    names,L=laplacian(candidate);v=chiral_mode(names,cap)
    oldnames,oldL=laplacian(net)
    T=tuple(tuple(F(1,12) if name=='J' else F(name==old) for old in oldnames) for name in names)
    R=tuple(tuple(F(name==old) for name in names) for old in oldnames)
    Qold=tuple(tuple(F(1,12) for _ in oldnames) for _ in oldnames)
    Qnew=tuple(tuple(F(1,13) for _ in names) for _ in names)
    assert mm(T,seed_embedding(oldnames))==seed_embedding(names)
    case.check('collective_identity',lambda:mm(mm(R,Qnew),T)==Qold)
    oldv=chiral_mode(oldnames,cap)
    assert zmm(zreal(T),tuple((z,) for z in oldv))==tuple((z,) for z in v)
    # Select chirality with the seed face cycle before performing the rewrite.
    pa,pb,pc=cap;perm={k:k for k in LABELS};perm.update({pa:pb,pb:pc,pc:pa})
    U=tuple(tuple(F(target==perm[source[0]]+perm[source[1]]) for source in oldnames) for target in oldnames)
    assert zmm(zreal(U),tuple((z,) for z in oldv))==tuple((zmul(OMEGA,z),) for z in oldv)
    inside=tuple(z if name in selected else ZERO for name,z in zip(names,v))
    outside=tuple(z if name not in selected else ZERO for name,z in zip(names,v))
    assert is_eigen(L,v,5)
    def localized():
        assert is_eigen(L,inside,5) and is_eigen(L,outside,5)
        assert sum(z!=ZERO for z in inside)==3 and sum(z!=ZERO for z in outside)==9
        assert inside[names.index('J')]==outside[names.index('J')]==ZERO
        return {'companion_support':3,'body_support':9,'eigenvalue':5,'junction_amplitude':'0'}
    case.check('compact_companion_mode',localized)
    common=projector((ONE,)*len(names));bodyP=projector(outside);compP=projector(inside)
    body_sector=zplus(common,bodyP);comp_sector=zplus(common,compP)
    assert zmm(body_sector,body_sector)==body_sector and zmm(comp_sector,comp_sector)==comp_sector
    assert zmm(body_sector,comp_sector)==common
    jc=currents(names,L,inside,triangles);jb=currents(names,L,outside,triangles)
    def balance():
        assert jc[face]==F(-3,2)
        assert sum(jb.values())==F(3,2) and sum(jc.values())==F(-3,2)
        assert all(jb[f]==F(1,2) for f in jb if f!=face)
        return {'body_total_imag_sqrt3':'3/2','companion_total_imag_sqrt3':'-3/2',
                'normalization':'inherited common seed amplitude; not independently normalized modes'}
    case.check('opposite_inherited_currents',balance)
    oldnames,oldL=laplacian(net)
    retained=[k for k in oldnames if k not in selected]
    old_response=boundary_response(oldL,oldnames,retained,F(1))
    new_response=boundary_response(L,names,retained,F(1))
    residual=add(new_response,scale(old_response,-1))
    full_changed=old_response!=new_response
    assert full_changed and rank(residual)==3
    old_order=hidden_realization_order(oldL,oldnames,retained)
    new_order=hidden_realization_order(L,names,retained)
    assert old_order=={'hidden_states':3,'observable_order':3,'dark_states':0}
    assert new_order=={'hidden_states':4,'observable_order':2,'dark_states':2}
    first=next((i,j) for i in range(len(retained)) for j in range(len(retained)) if residual[i][j])
    def full_response():
        i,j=first
        assert not full_changed,f'{retained[i]},{retained[j]}: {old_response[i][j]} -> {new_response[i][j]}; residual {residual[i][j]}, rank 3'
    case.check('full_retained_port_response',full_response)
    before=port_edges(net);after=port_edges(candidate)
    assert len(before)==36 and len(after)==42 and len(before|after)==48
    assert len(after-before)==12 and len(before-after)==6
    nc=sum(znorm(z) for z in inside);nb=sum(znorm(z) for z in outside)
    assert nc==9 and nb==15
    filename='released-loop-'+face[2:]+'.svg'
    render(candidate,triangles,face,cap,names,L,v,OUT/filename)
    trace={'source_face':face,'retained_handles':sorted(owners(candidate)),
           'before_directed_ports':sorted(before),'after_directed_ports':sorted(after),
           'new_directed_ports':sorted(after-before),'removed_directed_ports':sorted(before-after),
           'points_before':points,'points_after':new,'body_faces':body,'companion_faces':comp,
           'agent_order':names,'laplacian':L,'seed_initialization':T,
           'mode_full':v,'mode_body':outside,'mode_companion':inside,
           'retained_response_ports':retained,'response_before':old_response,'response_after':new_response,
           'response_residual':residual,'response_residual_rank':3}
    (OUT/('released-loop-'+face[2:]+'-trace.json')).write_text(json.dumps(trace,indent=2,default=str)+'\n')
    case.details={'rule':'Replace three principal bridges by six conductance-2 links to one shared junction; keep all triangle agents and payloads.',
                  'why_weight_2':'A unit bridge acts as 2 on its antisymmetric endpoint mode. A junction link to amplitude zero must match that coefficient.',
                  'geometry_rule':'Move existing face centre F to 3F, the antipode of the opposite seed vertex; add opposite cap views of the existing base face.',
                  'geometry_domain':'registered tetrahedral fixture; dimension-changing stellar expansion is declared',
                  'positive_interpolation_proof':'Body volume 8/3; companion volume (4/3)t for t>0; union 8/3+(4/3)t. All boundary cones of the union stay positive for 0<=t<=1.',
                  'source_operator_domain':'All four retained seed states: L W = W (5H), with H=I-J4/4. Verified before and after.',
                  'collective_identity_domain':'All twelve transported triangle amplitudes: R Q13 T = Q12. T retains old amplitudes and initializes the junction to their mean; R reads back old ports.',
                  'initialization':'The new field is exactly T times the existing seed field; no independent companion amplitude is supplied.',
                  'shared_identity_sectors':'(P0+Pbody)(P0+Pcomp)=P0; both sectors are idempotent.',
                  'full_boundary_response_at_z1':'changed; residual rank 3',
                  'hidden_realization_before':old_order,'hidden_realization_after':new_order,
                  'minimum_hidden_state_budget_for_full_response_plus_two_dark_modes':5,
                  'state_budget_scope':'Symmetric linear realizations with the same nine retained ports. Three observable source states plus two independent dark modes require at least five internal scalar states; this rule supplies four.',
                  'agents_before_after':[12,13],
                  'arrow_ledger':{'before':36,'after':42,'retained_union':48,'new':12,'removed':6},
                  'mode_squared_norms':{'body':str(nb),'companion':str(nc)},
                  'separately_normalized_current_totals':{'body':str(sum(jb.values())/nb),'companion':str(sum(jc.values())/nc)},
                  'charge_status':'Opposite inherited currents checked. Quantized equal physical charge is not established.',
                  'diagram':filename}
    return case.record(REQUIRED)


def split_case(net,points,triangles,face):
    case=Case('shared_seed_split',face)
    v=(ONE,OMEGA,zmul(OMEGA,OMEGA));E0=projector((ONE,)*3)
    Ep=projector(v);Em=projector(tuple(zconj(z) for z in v))
    Pa=zplus(E0,Ep);Pb=zplus(E0,Em)
    assert zmm(Pa,Pa)==Pa and zmm(Pb,Pb)==Pb and zmm(Pa,Pb)==E0
    distinct=False
    for t in triangles.values():
        X=zreal(transpose(tuple(points[k] for k in t)))
        centre=zmm(X,E0);a=zmm(X,Pa);b=zmm(X,Pb)
        xa=zplus(zplus(a,conjmat(a)),ztimes(centre,-1))
        xb=zplus(zplus(b,conjmat(b)),ztimes(centre,-1))
        assert xa==X and xb==X
        distinct=distinct or xa!=xb
    case.check('linear_ownership',lambda:len(owners(net))==12)
    case.check('stagewise_geometry',lambda:positive_baseline(points,triangles))
    case.check('seed_sector_response',lambda:seed_response(net))
    case.check('collective_identity',lambda:all(sum(row)==0 for row in laplacian(net)[1]))
    case.check('full_retained_port_response',lambda:laplacian(clone(net))==laplacian(net))
    case.check('distinct_companion_geometry',lambda:distinct)
    case.check('compact_companion_mode',lambda:False)
    names,L=laplacian(net);_,cap=face_cycle(triangles,face);mode=chiral_mode(names,cap)
    j=currents(names,L,mode,triangles);k=currents(names,L,tuple(zconj(z) for z in mode),triangles)
    case.check('opposite_inherited_currents',lambda:all(j[f]==-k[f] for f in j))
    case.details={'shared_identity':'(E0+Eomega)(E0+Eomega_bar)=E0',
                  'geometry_result':'Both conjugate sectors reconstruct exactly the same twelve triangles.',
                  'rule_type':'spectral view decomposition, no new geometric agent'}
    return case.record(REQUIRED)


def boundary_case(net,points,triangles,face):
    case=Case('boundary_mode',face)
    names,L=laplacian(net);selected,cap=face_cycle(triangles,face)
    d=next(k for k in LABELS if k not in cap)
    standing=tuple((F(name[0]==d)-F(name[1]==d),F(0)) for name in names)
    assert sum(z!=ZERO for z in standing)==6 and is_eigen(L,standing,5)
    mode=chiral_mode(names,cap)
    confined=tuple(z if name in selected else ZERO for name,z in zip(names,mode))
    assert not is_eigen(L,confined,5)
    outer=[i for i,name in enumerate(names) if name not in selected]
    inner=[names.index(name) for name in selected]
    leakage=tuple(tuple(L[i][j] for j in inner) for i in outer)
    assert rank(leakage)==3
    case.check('linear_ownership',lambda:len(owners(net))==12)
    case.check('stagewise_geometry',lambda:positive_baseline(points,triangles))
    case.check('seed_sector_response',lambda:seed_response(net))
    case.check('collective_identity',lambda:all(sum(row)==0 for row in L))
    case.check('full_retained_port_response',lambda:laplacian(clone(net))==laplacian(net))
    case.check('distinct_companion_geometry',lambda:False)
    case.check('compact_companion_mode',lambda:{'standing_mode_support':6,'eigenvalue':5})
    j=currents(names,L,standing,triangles)
    assert all(v==0 for v in j.values())
    case.check('opposite_inherited_currents',lambda:any(v!=0 for v in j.values()))
    case.details={'standing_mode':f'psi_ab=delta({d},a)-delta({d},b)',
                  'three_agent_boundary_leakage_rank':3,
                  'geometry_result':'A compact six-agent standing mode exists on the unchanged carrier; separate companion geometry has not been generated.'}
    return case.record(REQUIRED)


def conjugation_case(net,points,triangles,face):
    case=Case('whole_body_conjugation',face)
    R=proper(SWAP);reflected={k:mv(R,p) for k,p in points.items()}
    case.check('linear_ownership',lambda:len(owners(net))==12)
    case.check('stagewise_geometry',lambda:geometry(reflected,list(triangles.values())))
    case.check('seed_sector_response',lambda:seed_response(net))
    case.check('collective_identity',lambda:all(sum(row)==0 for row in laplacian(net)[1]))
    case.check('full_retained_port_response',lambda:laplacian(clone(net))==laplacian(net)) # real operator
    case.check('distinct_companion_geometry',lambda:False)
    case.check('compact_companion_mode',lambda:False)
    names,L=laplacian(net);_,cap=face_cycle(triangles,face);v=chiral_mode(names,cap)
    opposite=tuple(zconj(z) for z in v)
    assert is_eigen(L,opposite,5)
    j=currents(names,L,v,triangles);k=currents(names,L,opposite,triangles)
    case.check('opposite_inherited_currents',lambda:all(j[f]==-k[f] for f in j))
    case.details={'geometry_result':'One congruent whole-body image; node count and volume unchanged.',
                  'simultaneously_constructed_bodies':1}
    return case.record(REQUIRED)


def controls(net,points,triangles):
    face='F_ABC';recipe=release_recipe(net,triangles,face);region,reps,internal,boundary=recipe[:4]
    results=[]
    def refusal(name,operation):
        try:operation()
        except (ValueError,AssertionError):results.append({'control':name,'rejected':True});return
        raise AssertionError('negative control accepted: '+name)
    for name,newreps,newboundary,newinternal in (
        ('duplicated payload',reps[:-1]+(Agent('JUNCTION',reps[0].handles),),boundary,internal),
        ('omitted boundary',reps,dict(list(boundary.items())[1:]),internal),
        ('late invalid port',reps,boundary,internal[:-1]+((internal[-1][0],(6,'absent')),)),
    ):
        trial=clone(net);before=snapshot(trial)
        refusal(name,lambda:trial.replace_region(region,newreps,newinternal,newboundary))
        assert snapshot(trial)==before
    out,selected,cap=release(net,triangles,face)
    refusal('flattened companion',lambda:release_geometry(points,triangles,face,cap,F(1)))
    bad=list(triangles.values());t=bad[0];bad[0]=(t[0],t[2],t[1])
    refusal('inverted source face',lambda:geometry(points,bad))
    def wrong_weight(): assert seed_response(out,F(1)),'seed response changed'
    refusal('unmatched junction weight',wrong_weight)
    names,L=laplacian(out);v=chiral_mode(names,cap)
    confined=tuple(z if name in selected else ZERO for name,z in zip(names,v))
    badL=[list(row) for row in L];i=names.index('J');j=names.index(selected[0])
    badL[i][i]+=1;badL[j][j]+=1;badL[i][j]-=1;badL[j][i]-=1
    def broken_balance(): assert is_eigen(badL,confined,5),'localized mode leaks'
    refusal('one unbalanced junction arm',broken_balance)
    oldnames,_=laplacian(net)
    R=tuple(tuple(F(name==old) for name in names) for old in oldnames)
    wrongT=tuple(tuple(F(name==old) for old in oldnames) for name in names)
    Qnew=tuple(tuple(F(1,len(names)) for _ in names) for _ in names)
    Qold=tuple(tuple(F(1,len(oldnames)) for _ in oldnames) for _ in oldnames)
    def lost_identity(): assert mm(mm(R,Qnew),wrongT)==Qold,'collective identity rescaled'
    refusal('omitted junction initialization',lost_identity)
    return results


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--conjecture',default='all',choices=('all','shared_seed_split','released_loop','boundary_mode','whole_body_conjugation'))
    parser.add_argument('--face',default='all',choices=('all','ABC','ABD','ACD','BCD'))
    args=parser.parse_args(argv)
    suffix='' if args.conjecture==args.face=='all' else '-'+args.conjecture+'-'+args.face
    OUT.mkdir(parents=True,exist_ok=True)
    net,points,triangles=fixture()
    assert positive_baseline(points,triangles)['volume']=='8/3' and seed_response(net)
    names,L=laplacian(net)
    assert rank(L)==11 and rank(seed_embedding(names))==4
    # The exact three-dimensional eigenvalue-5 space comes from the four seed
    # vertices, rather than an eigenspace chosen after observing a candidate.
    D=tuple(tuple(F(name[0]==p)-F(name[1]==p) for p in LABELS) for name in names)
    assert rank(D)==3 and mm(L,D)==scale(D,5)
    assert rank(add(L,scale(eye(12),-5)))==9
    negative=controls(net,points,triangles)
    registry={'shared_seed_split':split_case,'released_loop':released_case,
              'boundary_mode':boundary_case,'whole_body_conjugation':conjugation_case}
    chosen=registry if args.conjecture=='all' else {args.conjecture:registry[args.conjecture]}
    faces=sorted({t[0] for t in triangles.values()}) if args.face=='all' else ['F_'+args.face]
    results=[]
    for run in chosen.values():
        for face in faces:
            before=(snapshot(net),dict(points),dict(triangles))
            results.append(run(net,points,triangles,face))
            assert (snapshot(net),points,triangles)==before,'candidate mutated the common source fixture'
    assert len(results)==len(chosen)*len(faces)
    released=[r for r in results if r['conjecture']=='released_loop']
    assert all(r['result']=='candidate_not_established' for r in results)
    for r in released:
        assert r['checks']['full_retained_port_response']['status']=='fail'
        assert all(v['status']=='pass' for k,v in r['checks'].items() if k!='full_retained_port_response')
    # Symmetry control: no outer face is privileged by the planar drawing.
    if released: assert len({json.dumps(r['details']['arrow_ledger'],sort_keys=True) for r in released})==1
    report={'audit_assertions_passed':True,'case_count':len(results),'anchor_count':len(faces),
            'selection':vars(args),
            'model_inputs':['existing twelve-triangle carrier','unit conductance on original agent wires',
                            'oriented loop current as a trial readout','explicit conjecture-specific macro rules'],
            'protected_domain':'Laplacian intertwining on the four-state seed image W has induced operator 5*(I-J4/4). Collective-projector comparison covers all twelve transported amplitudes. The full retained-port Laplacian response fails its acceptance gate.',
            'summary':dict(Counter(r['conjecture']+': '+r['result'] for r in results)),
            'negative_controls':negative,'cases':results,
            'limitations':['No electron or electromagnetic-charge identification is certified.',
                           'The released-loop macro changes the full boundary transfer function; only the stated seed sector is protected.',
                           'Current balance uses inherited normalization; independent unit-norm normalization changes its magnitudes.',
                           'Regional rewrites are not compiled into elementary principal-pair steps.',
                           'No primitive mass count or physical binding dynamics is inferred.']}
    source_paths=[Path(__file__),Path(__file__).with_name('interaction_conjecture_harness.py'),Path(__file__).with_name('abstract_port_net.py')]
    report['source_sha256']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in source_paths}
    report_name='report'+suffix+'.json'
    (OUT/report_name).write_text(json.dumps(report,indent=2,default=str)+'\n')
    rows=[]
    for r in results:
        checks='; '.join(k+': '+v['status'] for k,v in r['checks'].items())
        diagram=r['details'].get('diagram')
        link=f'<a href="{diagram}">diagram</a>' if diagram else ''
        rows.append(f'<tr><td>{escape(r["conjecture"])}</td><td>{escape(r["anchor"])}</td><td>{escape(r["result"])}</td><td>{escape(checks)}</td><td>{link}</td></tr>')
    html='''<!doctype html><meta charset="utf-8"><title>Interaction conjecture tests</title>
<style>body{font:15px system-ui;max-width:1350px;margin:35px auto;padding:20px;color:#24364b}table{border-collapse:collapse;width:100%}td,th{padding:12px;border:1px solid #d3dce6;text-align:left}img{max-width:100%}small{color:#51667d}</style>
<h1>Four conjectures × four equivalent faces</h1>
<p>Exact gates: payload ownership, geometric positivity, four-state response, collective identity, companion geometry, mode localization, and inherited oriented-current balance.</p>
<p>The released-loop fixture constructs a positive compact companion and preserves the four-state response and collective identity. It fails the stronger full retained-port response gate. None of these concrete variants establishes the full conjecture.</p>
<table><tr><th>Conjecture</th><th>Face</th><th>Result</th><th>Gates</th><th>View</th></tr>'''+''.join(rows)+'''</table>
<h2>Released loop, face ABC</h2><img src="released-loop-ABC.svg" alt="Body and companion joined through one identity junction">
<p><a href="report.json">Full exact report and controls</a></p>'''
    html=html.replace('Four conjectures × four equivalent faces',f'{len(chosen)} conjectures × {len(faces)} faces').replace('href="report.json"','href="'+report_name+'"')
    (OUT/('index'+suffix+'.html')).write_text(html,encoding='utf-8')
    assert len(negative)==8
    print(f'PASS infrastructure: {len(results)} cases, {len(faces)} anchors, eight rejected negative controls.')
    if released: print(f'Released-loop macro: {len(released)}/{len(released)} construct a positive 3-agent circulating companion and preserve the seed response; all fail the full retained-port response gate.')
    if len(chosen)>1: print('Other cases: conjugate views give the same body; a six-agent standing boundary mode exists; whole-body conjugation retains full size.')
    print('Limits recorded: full boundary response changes; current magnitudes depend on normalization; macro is not a primitive-step compilation.')

if __name__=='__main__': main()
