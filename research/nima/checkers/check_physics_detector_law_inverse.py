"""Exact complete-word parameter inverse and conditioning controls; no estimates."""
import argparse
import copy
import itertools
import json
from fractions import Fraction as F
from pathlib import Path
import check_physics_geometric_candidate as G
import check_physics_observation_resource_interface as O

ROOT=G.ROOT
CONTRACT='research/nima/contracts/physics-detector-law-inverse.v1.json'


def probability(inputs,word,eta,gamma,r):
    G.require(len(inputs)==len(word),'word alignment')
    state=(r,1-r)
    for n,y in zip(inputs,word):state=O.step(n,y,state,eta,gamma)
    return sum(state)


def coordinates(eta,gamma,r):
    return tuple(probability(ns,word,eta,gamma,r) for ns,word in (
        ((1,),'C'),((0,1),'NC'),((1,1),'NC'),((1,0,1),'CNC')))


def inverse(x):
    a,b,v,w=x
    G.require(a>0,'zero initial click law')
    eta=(b-v)/a
    G.require(eta>0,'zero inferred efficiency')
    r=a/eta;gamma=w/(a*eta)
    G.require(0<eta<=1 and 0<r<=1 and 0<gamma<=1,'off-family coordinates')
    result=(eta,gamma,r)
    G.require(coordinates(*result)==tuple(x),'off-family residual')
    return result


def validate(c):
    G.require(c['decision']=='constructed_partial_complete_law_identifiability_witness'
              and c['full_node_closed'] is False and c['empirical_estimates'] is None,'scope promotion')
    G.require(c['inverse']=={'eta':'(b-v)/a','r':'a/eta','gamma':'w/(a*eta)'},'inverse changed')
    G.require(c['conditioning_box']=={'eta':['1/4','1/2'],'gamma':['1/4','1/2'],'r':['1/4','3/4']},'regime drift')


def main():
    p=argparse.ArgumentParser();p.add_argument('--pin',action='store_true');args=p.parse_args()
    c=G.load(CONTRACT);validate(c);paths={CONTRACT}|set(c['source_evidence']);pin=ROOT/c['source_pins']
    if args.pin:
        G.require(not pin.exists(),'refusing implicit re-pin')
        pin.write_text(json.dumps({'source_sha256':{p:G.sha(p) for p in sorted(paths)}},indent=2)+'\n',encoding='utf-8')
    pins=G.load(c['source_pins']);G.require(set(pins['source_sha256'])==paths,'pin coverage')
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source drift: '+path)
    def grid(lo,hi):return [lo+(hi-lo)*F(i,4) for i in range(5)]
    points=list(itertools.product(grid(F(1,4),F(1,2)),grid(F(1,4),F(1,2)),grid(F(1,4),F(3,4))))
    images=[];normalizations=0
    for eta,gamma,r in points:
        x=coordinates(eta,gamma,r);images.append(x)
        G.require(inverse(x)==(eta,gamma,r),'parameter inverse')
        a,b,v,w=x
        G.require(a==eta*r and b-v==a*eta and w==a*eta*gamma,'inverse polynomial identity')
        for inputs in ((1,), (0,1), (1,1), (1,0,1)):
            total=sum(probability(inputs,word,eta,gamma,r) for word in itertools.product('CN',repeat=len(inputs)))
            G.require(total==1,'complete word normalization');normalizations+=1
    pairs=0
    for p1,x1 in zip(points,images):
        for p2,x2 in zip(points,images):
            delta=max(abs(a-b) for a,b in zip(x1,x2))
            G.require(abs(p1[0]-p2[0])<=40*delta and abs(p1[2]-p2[2])<=124*delta
                      and abs(p1[1]-p2[1])<=560*delta,'pairwise inverse sensitivity')
            pairs+=1
    first=coordinates(F(1,2),F(1,4),F(1,4));second=coordinates(F(1,4),F(1,2),F(1,2))
    G.require((first[0],first[2],first[3])==(second[0],second[2],second[3])==(F(1,8),F(5,32),F(1,64)), 'three-coordinate alias')
    G.require(first[1]==F(7,32) and second[1]==F(3,16),'alias-breaking coordinate')
    failures=[]
    for name,x in (('zero-initial-readiness',coordinates(F(1,2),F(1,4),F(0))),
                   ('zero-efficiency',coordinates(F(0),F(1,4),F(1,2))),
                   ('postselected-coordinates',(F(1),F(1),F(1),F(1)))):
        try:inverse(x)
        except ValueError:failures.append(name)
        else:raise AssertionError('accepted '+name)
    # Different readiness per input word can defeat the shared family map.
    mixed=list(first);mixed[1]=coordinates(F(1,2),F(1,4),F(3,4))[1]
    try:inverse(mixed)
    except ValueError:failures.append('word-dependent-initialization')
    else:raise AssertionError('accepted this incompatible initialization control')
    rejected=[]
    for name in ('full-node-promotion','empirical-estimate','unproved-regime'):
        bad=copy.deepcopy(c)
        if name=='full-node-promotion':bad['full_node_closed']=True
        elif name=='empirical-estimate':bad['empirical_estimates']={'eta':'1/2'}
        else:bad['conditioning_box']['eta'][0]='0'
        try:validate(bad)
        except ValueError:rejected.append(name)
        else:raise AssertionError('accepted '+name)
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source changed during check')
    out={'schema':c['schema'],'status':'pass','reference_family_identifiable':True,
         'exact_parameter_inverse_cases':len(points),'complete_word_normalizations':normalizations,
         'pairwise_conditioning_controls':pairs,'inverse_lipschitz_bounds':{'eta':40,'r':124,'gamma':560},
         'three_coordinate_alias':{'first':list(map(str,first)),'second':list(map(str,second))},
         'rejected_inverse_controls':failures,'rejected_corruptions':rejected,'full_node_closed':False,
         'source_sha256':pins['source_sha256'],'checker_sha256':G.sha(Path(__file__))}
    (ROOT/c['result']).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='source_sha256'},indent=2))

if __name__=='__main__':main()
