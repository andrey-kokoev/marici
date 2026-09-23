"""Exact full-domain triangular sections for rank-two retired migrations.

Only two-dimensional public coordinates (no surviving audits) are admitted.
The owning migration verifier remains the source/context authority.
"""
from pathlib import Path
from fractions import Fraction as Q
from uuid import uuid4
import sys,json
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from migration_section_checkpoint import SectionSession,check_section
from full_segment_checkpoint import coverage_rows
from checked_retirement_interface import freeze
from verify_scalar_envelope_band import cross,area,intersection
if not __debug__:raise RuntimeError('Assertions required')

def polygon_targets(polygon):
    return [((b[1]-a[1],a[0]-b[0]),(b[1]-a[1])*a[0]+(a[0]-b[0])*a[1])
            for a,b in zip(polygon,polygon[1:]+polygon[:1])]
def weights(triangle,p):
    a,b,c=triangle;d=cross(a,b,c);assert d>0
    return (cross(p,b,c)/d,cross(a,p,c)/d,cross(a,b,p)/d)
def interpolate(triangle,lifts,p):
    w=weights(triangle,p)
    return tuple(sum(t*v[j] for t,v in zip(w,lifts)) for j in range(len(lifts[0])))

def verify_full_polygon(state,expected_polygon,packet):
    assert set(packet)=={'migration_binding','polygon','vertices','source_lifts','triangles','coverage_weights'}
    assert packet['migration_binding']==state.migration_binding and packet['polygon']==expected_polygon
    assert json.loads(state.runtime_json)['audits']==[]
    polygon=[tuple(map(Q,v)) for v in expected_polygon]
    assert len(polygon)>=3 and all(len(v)==2 for v in polygon) and len(set(polygon))==len(polygon)
    assert area(polygon)>0
    assert all(cross(polygon[i-1],polygon[i],polygon[(i+1)%len(polygon)])>0 for i in range(len(polygon)))
    assert all(cross(a,b,p)>=0 for a,b in zip(polygon,polygon[1:]+polygon[:1]) for p in polygon)
    targets=polygon_targets(polygon);rows=coverage_rows(state)
    assert len(packet['coverage_weights'])==len(targets)
    for raw,(normal,bound) in zip(packet['coverage_weights'],targets):
        w=list(map(Q,raw));assert len(w)==len(rows) and all(x>=0 for x in w)
        assert tuple(sum(x*a[j] for x,(a,h) in zip(w,rows)) for j in range(2))==normal
        assert sum(x*h for x,(a,h) in zip(w,rows))<=bound
    vertices=[tuple(map(Q,v)) for v in packet['vertices']]
    assert vertices and all(len(v)==2 for v in vertices) and len(set(vertices))==len(vertices)
    assert all(cross(a,b,p)>=0 for a,b in zip(polygon,polygon[1:]+polygon[:1]) for p in vertices)
    assert len(packet['source_lifts'])==len(vertices)
    for v,t in zip(packet['vertices'],packet['source_lifts']):
        check_section(state,[v],{'migration_binding':state.migration_binding,'vertices':[v],'source_lifts':[t]})
    lifts=[tuple(map(Q,t)) for t in packet['source_lifts']];cells=[];used=set()
    for ids in packet['triangles']:
        assert len(ids)==3 and len(set(ids))==3 and all(type(i) is int and 0<=i<len(vertices) for i in ids)
        used.update(ids);p=[vertices[i] for i in ids];t=[lifts[i] for i in ids]
        assert area(p)>0;cells.append((p,t))
    assert cells and used==set(range(len(vertices)))
    comparisons=0
    for i,(p,t) in enumerate(cells):
        for q,u in cells[i+1:]:
            common=intersection(p,q);assert area(common)==0
            # Shared indices alone do NOT establish continuity at T-junctions.
            for v in common:
                assert interpolate(p,t,v)==interpolate(q,u,v);comparisons+=1
    assert sum(area(p) for p,t in cells)==area(polygon)
    return {'vertex_checks':len(vertices),'coverage_implications':len(targets),
            'cells':len(cells),'face_point_comparisons':comparisons}

class FullPolygonSession(SectionSession):
    def __init__(self):super().__init__();self._polygon_covers={}
    def _receipt(self):
        result=super()._receipt()
        result['bytes']['full_polygon_encodings']=sum(len(s.encode()) for s in self._polygon_covers.values())
        return result
    def attach_full_polygon(self,handle,expected_before,expected_polygon,packet):
        with self._lock:
            self._current(handle);assert expected_before==self._state.descriptor()
            proof=json.loads(freeze(packet));polygon=json.loads(freeze(expected_polygon))
            work=verify_full_polygon(self._state,polygon,proof)
            sid=uuid4().hex;self._polygon_covers[sid]=freeze(proof);self._handle=uuid4().hex
            self._section_work['vertex_checks']+=work['vertex_checks']
            result=self._receipt();result.update(section_id=sid,coverage='full-current-domain',attachment_work=work)
            return result
    def covered_lift(self,handle,section_id,point):
        with self._lock:
            self._current(handle)
            if section_id not in self._polygon_covers:raise ValueError('UNKNOWN_COVER')
            p=tuple(map(Q,point))
            if len(p)!=2:raise ValueError('NONPUBLIC_POINT')
            proof=json.loads(self._polygon_covers[section_id]);assert proof['migration_binding']==self._state.migration_binding
            if not all(sum(a*x for a,x in zip(n,p))<=h for n,h in coverage_rows(self._state)):raise ValueError('EXCLUDED_POINT')
            vertices=[tuple(map(Q,v)) for v in proof['vertices']];lifts=[tuple(map(Q,t)) for t in proof['source_lifts']]
            for ids in proof['triangles']:
                triangle=[vertices[i] for i in ids]
                if all(w>=0 for w in weights(triangle,p)):
                    result=interpolate(triangle,[lifts[i] for i in ids],p)
                    self._section_work['interpolated_lifts']+=1
                    return list(map(str,result))
            raise ValueError('OUTSIDE_CERTIFIED_COVER')
