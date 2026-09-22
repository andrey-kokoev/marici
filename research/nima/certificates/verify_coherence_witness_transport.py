"""Corrected transport of tetrahedral witnesses, with composition across three stages.

The fixture complexes occupy degrees 0..2. There is no degree-three correction:
K_new U_0 - U_3 K_old must equal the alternating sum of supplied face rehomotopies.
"""
from pathlib import Path
import importlib.util
import json
import sys

spec=importlib.util.spec_from_file_location('tetrahedra',Path(__file__).with_name('verify_tetrahedral_coherence.py'))
t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)


class Checker(t.Checker):
    def comparison(self,old,new,raw):
        s=self.s;s.keys(raw,('vertex_maps','face_rehomotopies'))
        s.keys(raw['vertex_maps'],('0','1','2','3'));s.keys(raw['face_rehomotopies'],self.faces)
        maps={};corrections={}
        for i in range(4):
            m=s.matrix(raw['vertex_maps'][str(i)],5,5);maps[i]=m
            self.typed(m,old['nodes'][i],new['nodes'][i])
            s.need(s.mul(m,old['nodes'][i]['D'])==new['nodes'][i]['D'],'stage source identification')
        for key in self.edges:
            i,j=map(int,key)
            s.need(s.mul(maps[j],old['edges'][key])==s.mul(new['edges'][key],maps[i]),'stage edge transport')
        for key in self.faces:
            i,_,k=map(int,key)
            j=s.matrix(raw['face_rehomotopies'][key],5,5)
            self.typed(j,old['nodes'][i],new['nodes'][k]);corrections[key]=j
            change=tuple(self.add(s.mul(new['faces'][key][r],maps[i]),
                                 s.neg(s.mul(maps[k],old['faces'][key][r]))) for r in (0,1))
            s.need(change[0]==s.mul(new['nodes'][k]['left'],j) and
                   change[1]==s.neg(s.mul(j,old['nodes'][i]['left'])),'face rehomotopy does not witness the change')
        boundary=self.add(s.mul(new['edges']['23'],corrections['012']),corrections['023'],
                          s.neg(s.mul(corrections['123'],old['edges']['01'])),s.neg(corrections['013']))
        delta=(s.mul(new['nodes'][3]['left'],boundary),s.neg(s.mul(boundary,old['nodes'][0]['left'])))
        for r in (0,1):
            change=self.add(s.mul(new['omega'][r],maps[0]),s.neg(s.mul(maps[3],old['omega'][r])))
            s.need(change==delta[r],'tetrahedral boundary correction fails')
        s.need(old['status']==new['status'],'certified obstruction status changes')
        if old['filler'] is not None:
            change=self.add(s.mul(new['filler'],maps[0]),s.neg(s.mul(maps[3],old['filler'])))
            s.need(change==boundary,'filler change is not the supplied face correction')
        return {'maps':maps,'corrections':corrections}

    def verify(self,bundle):
        s=self.s;s.keys(bundle,('schema','scope','stages','comparisons'))
        s.need(bundle['schema']=='corrected-tetrahedral-witness-transport-v1','wrong schema')
        s.need(bundle['scope']=='finite-fixture-not-an-identification-of-the-four-physical-towers','unsupported scope')
        s.need(type(bundle['stages']) is list and len(bundle['stages'])==3,'exactly three stages required')
        s.keys(bundle['comparisons'],('01','12','02'))
        stages=[self.stage(st) for st in bundle['stages']]
        comparisons={}
        for key,raw in bundle['comparisons'].items():
            i,j=map(int,key);comparisons[key]=self.comparison(stages[i],stages[j],raw)
        first,second,direct=(comparisons[k] for k in ('01','12','02'))
        for i in range(4):
            s.need(s.mul(second['maps'][i],first['maps'][i])==direct['maps'][i],'composed stage map disagrees')
        for key in self.faces:
            i,_,k=map(int,key)
            composed=self.add(s.mul(second['maps'][k],first['corrections'][key]),
                              s.mul(second['corrections'][key],first['maps'][i]))
            s.need(composed==direct['corrections'][key],'rehomotopy routes disagree despite valid individual comparisons')
        return {'verified':True,'stages':3,'comparisons':3,
                'tetrahedral_statuses':[x['status'] for x in stages],
                'composed_vertex_maps_checked':4,'composed_face_rehomotopies_checked':4,
                'scope':bundle['scope'],
                'limitation':'The declared three-term complexes have no degree-three correction; this is not an all-level coherence theorem.'}


if __name__=='__main__':
    checker=Checker(sys.argv[2])
    print(json.dumps(checker.verify(checker.s.load(sys.argv[1])),indent=2))
