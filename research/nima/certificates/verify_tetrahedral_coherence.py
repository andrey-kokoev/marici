"""Finite filtered-module chain tetrahedra, including their chosen higher witnesses.

Homological convention: delta(H)=dH+Hd, delta(K)=dK-Kd.
The trusted structural verifier is supplied as a code path, not certificate data.
"""
from pathlib import Path
import importlib.util
import json
import sys
from itertools import combinations


def load_verifier(path):
    spec=importlib.util.spec_from_file_location('structural_checker',Path(path))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


class Checker:
    names=('00','10','01','11')
    edges=tuple(''.join(map(str,x)) for x in combinations(range(4),2))
    faces=tuple(''.join(map(str,x)) for x in combinations(range(4),3))

    def __init__(self,structural_verifier):self.s=load_verifier(structural_verifier)

    def add(self,*matrices):
        return [[sum(m[i][j] for m in matrices) for j in range(5)] for i in range(5)]

    def typed(self,m,a,b):
        s=self.s
        for action in ('left','right'):
            s.need(s.mul(m,a[action])==s.mul(b[action],m),'map fails module intertwining')
        for flag in ('K','M','N','L'):
            image=s.mul(m,a[flag])
            s.need(s.rank(s.join(b[flag],image))==s.rank(b[flag]),'map fails filtration containment')

    def stage(self,stage):
        s=self.s;s.keys(stage,('structural','edges','faces','tetrahedron'))
        s.verify(stage['structural'])
        nodes=[]
        for name in self.names:
            raw=stage['structural']['nodes'][name]
            shapes={'D':(5,5),'left':(5,5),'right':(5,5),'K':(5,3),'M':(5,3),'N':(5,2),'L':(5,1)}
            nodes.append({k:s.matrix(raw[k],*shape) for k,shape in shapes.items()})
        # At each vertex C_2=C_1=C_0=E, d_2=d_1=left_t.
        # The structural checker proves d^2=0 and stability of all four flags.
        s.keys(stage['edges'],self.edges);edges={}
        for key,raw in stage['edges'].items():
            i,j=map(int,key);f=s.matrix(raw,5,5);self.typed(f,nodes[i],nodes[j])
            s.need(s.mul(f,nodes[i]['D'])==nodes[j]['D'],'edge loses common source identification')
            edges[key]=f
        s.keys(stage['faces'],self.faces);faces={}
        for key,raw in stage['faces'].items():
            s.keys(raw,('h0','h1'));i,j,k=map(int,key)
            h0=s.matrix(raw['h0'],5,5);h1=s.matrix(raw['h1'],5,5)
            for h in (h0,h1):self.typed(h,nodes[i],nodes[k])
            defect=self.add(s.mul(edges[f'{j}{k}'],edges[f'{i}{j}']),s.neg(edges[f'{i}{k}']))
            d0,dk=nodes[i]['left'],nodes[k]['left']
            s.need(s.mul(dk,h0)==defect,'face degree-zero homotopy equation')
            s.need(self.add(s.mul(dk,h1),s.mul(h0,d0))==defect,'face degree-one homotopy equation')
            s.need(s.mul(h1,d0)==defect,'face degree-two homotopy equation')
            faces[key]=(h0,h1)
        # Two pastings from F23 F12 F01 to F03.
        omega=tuple(self.add(s.mul(edges['23'],faces['012'][r]),faces['023'][r],
                  s.neg(s.mul(faces['123'][r],edges['01'])),s.neg(faces['013'][r])) for r in (0,1))
        d0,d3=nodes[0]['left'],nodes[3]['left'];zero=s.zero(5,5)
        s.need(s.mul(d3,omega[0])==zero and s.mul(omega[1],d0)==zero and
               self.add(s.mul(d3,omega[1]),s.mul(omega[0],d0))==zero,'tetrahedral boundary is not closed')
        cell=stage['tetrahedron'];s.need(type(cell) is dict and 'status' in cell,'missing tetrahedral status')
        filler=None
        if cell['status']=='FILLED':
            s.keys(cell,('status','k0'));filler=s.matrix(cell['k0'],5,5)
            self.typed(filler,nodes[0],nodes[3])
            s.need(s.mul(d3,filler)==omega[0] and s.neg(s.mul(filler,d0))==omega[1],
                   'tetrahedral filler does not match the chosen faces')
        elif cell['status']=='OBSTRUCTED':
            s.keys(cell,('status','entry'));entry=cell['entry']
            s.need(type(entry) is list and len(entry)==2 and all(type(x) is int and 0<=x<5 for x in entry),'bad obstruction entry')
            # Every admitted K intertwines left_t: d3 K=K d0.
            # Hence every boundary (d3 K,-K d0) has component sum zero.
            total=self.add(*omega);s.need(total[entry[0]][entry[1]]!=0,'no certified obstruction at this entry')
        else:raise ValueError('unsupported tetrahedral status')
        return {'nodes':nodes,'edges':edges,'faces':faces,'omega':omega,'filler':filler,'status':cell['status']}

    def verify(self,bundle):
        s=self.s;s.keys(bundle,('schema','scope','stages','transitions'))
        s.need(bundle['schema']=='filtered-module-tetrahedral-tower-fixture-v1','wrong schema')
        s.need(bundle['scope']=='finite-fixture-not-an-identification-of-the-four-physical-towers','unsupported scope')
        s.need(type(bundle['stages']) is list and 1<=len(bundle['stages'])<=8,'bad stage count')
        s.need(type(bundle['transitions']) is list and len(bundle['transitions'])==len(bundle['stages'])-1,'missing stage transitions')
        stages=[self.stage(stage) for stage in bundle['stages']]
        for index,raw in enumerate(bundle['transitions']):
            s.keys(raw,('vertex_maps',));s.keys(raw['vertex_maps'],('0','1','2','3'))
            old,new=stages[index:index+2];maps={}
            for i in range(4):
                m=s.matrix(raw['vertex_maps'][str(i)],5,5);maps[i]=m
                self.typed(m,old['nodes'][i],new['nodes'][i])
                s.need(s.mul(m,old['nodes'][i]['D'])==new['nodes'][i]['D'],'stage source identification')
            for key in self.edges:
                i,j=map(int,key)
                s.need(s.mul(maps[j],old['edges'][key])==s.mul(new['edges'][key],maps[i]),'stage edge transport')
            for key in self.faces:
                i,_,k=map(int,key)
                for r in (0,1):
                    s.need(s.mul(maps[k],old['faces'][key][r])==s.mul(new['faces'][key][r],maps[i]),'stage face-witness transport')
            s.need(old['status']==new['status'],'stage changes certified filler status')
            for r in (0,1):
                s.need(s.mul(maps[3],old['omega'][r])==s.mul(new['omega'][r],maps[0]),'stage boundary transport')
            if old['filler'] is not None:
                s.need(s.mul(maps[3],old['filler'])==s.mul(new['filler'],maps[0]),'stage filler-witness transport')
        return {'verified':True,'stages':len(stages),'edges_per_stage':6,'faces_per_stage':4,
                'tetrahedral_statuses':[x['status'] for x in stages],
                'scope':bundle['scope'],'transport':'strict transport of the chosen face and filler witnesses'}


if __name__=='__main__':
    checker=Checker(sys.argv[2])
    print(json.dumps(checker.verify(checker.s.load(sys.argv[1])),indent=2))
