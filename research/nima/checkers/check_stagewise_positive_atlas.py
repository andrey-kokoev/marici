"""Stagewise positive atlas witnesses for the registered tetrahedral family.

Geometry domain: positive homothetic copies of the reference labelled surface.
Phase domain: all 36 complex coefficient inputs, with exact target projector N.
Every intermediate state includes the declared immutable twelve-patch atlas.
Arrow counts count nonzero coefficient transfers, not static chart descriptions.
These conventions are shared by the original and compressed implementations.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json
from check_twelve_triangle_positive_geometry import (
    POINTS, LABELS, ONE, ZERO, OMEGA, mean, compose, rotation,
    transpose, mm, det, dot, sub, cross, zadd, zmul, zconj, zscale,
    znorm, zmv, zmm, zreal, projector,
)


def main():
    generators=((1,2,0,3),(3,0,2,1))
    group={(0,1,2,3)};front=list(group)
    while front:
        p=front.pop()
        for g in generators:
            q=compose(g,p)
            if q not in group: group.add(q);front.append(q)
    rotations=[rotation(p) for p in sorted(group)]
    triangles=[];points=dict(POINTS)
    for p in sorted(group):
        a,b,c=[LABELS[p[i]] for i in range(3)]
        centre='F_'+''.join(sorted((a,b,c)))
        points[centre]=mean([POINTS[k] for k in (a,b,c)])
        triangles.append((centre,a,b))
    Xs=[transpose(tuple(points[k] for k in t)) for t in triangles]
    X=tuple(r for block in Xs for r in block)
    vs=[zmv(block,(ONE,OMEGA,zmul(OMEGA,OMEGA))) for block in Xs]
    Ps=[projector(v) for v in vs]
    u=tuple(z for v in vs for z in v);assert sum(znorm(z) for z in u)==80
    L=tuple(tuple(Ps[i//3][i%3][j%3] if i//3==j//3 else ZERO
                  for j in range(36)) for i in range(36))
    blocks=[[mm(R,transpose(S)) for S in rotations] for R in rotations]
    G=zreal(tuple(tuple(blocks[i//3][j//3][i%3][j%3]/12 for j in range(36)) for i in range(36)))
    N=projector(u)
    Id=tuple(tuple(ONE if i==j else ZERO for j in range(36)) for i in range(36))
    A=tuple((z,) for z in u);B=(tuple(zscale(zconj(z),F(1,80)) for z in u),)
    unit=((ONE,),)
    assert zmm(G,L)==N and zmm(A,B)==N
    # Static chart data is explicitly part of EVERY intermediate state, including
    # a compressed stage. No original spatial vertex array is used by decode().
    patches=[]
    for t,v in zip(triangles,vs):
        r=tuple(z[0] for z in v);s=tuple(z[1] for z in v)
        # The reference face offset is recoverable from the mode frame itself;
        # it is not read back from a discarded vertex buffer by the decoder.
        f=tuple(x/2 for x in cross(r,s));assert f==points[t[0]]
        norm=sum(znorm(z) for z in v)
        assert dot(r,s)==0 and dot(r,f)==0 and dot(s,f)==0
        assert dot(r,r)==F(2,3) and dot(s,s)==2 and norm==F(20,3)
        assert dot(cross(r,s),f)>0
        patches.append({'labels':t,'f':f,'r':r,'s':s,'norm':norm})
    ref=(ZERO,(F(-1,10),F(-3,10)),(F(-1,10),F(3,10)))

    def inner(v,w):
        total=ZERO
        for a,b in zip(v,w): total=zadd(total,zmul(zconj(a),b))
        return total

    def local_charts(Y):
        assert len(Y)==36
        charts=[]
        for g,v in enumerate(vs):
            norm=patches[g]['norm'];chart=[]
            for j in range(3):
                q=tuple(Y[3*g+i][j] for i in range(3))
                alpha=zscale(inner(v,q),1/norm)
                assert q==tuple(zmul(alpha,z) for z in v)
                chart.append(alpha)
            charts.append(tuple(chart))
        return charts

    def decode(charts):
        # Real chart coordinates are (t,w)=(Re(alpha),-Im_sqrt3(alpha)).
        # Their orientation is explicitly fixed; it is not inferred from PSD.
        assert len(charts)==12
        copies={};boundary=Counter();spatial=[];scales=[];areas=[]
        for chart,patch in zip(charts,patches):
            xy=[(z[0],-z[1]) for z in chart]
            e1=sub(xy[1],xy[0]);e2=sub(xy[2],xy[0])
            area=(e1[0]*e2[1]-e1[1]*e2[0])/2
            assert area>0, 'nonpositive oriented chart area'
            scale=-10*chart[1][0]
            assert scale>0, 'nonpositive registered geometric scale'
            assert chart==tuple(zscale(z,scale) for z in ref), 'outside declared registered family'
            f,r,s,n=patch['f'],patch['r'],patch['s'],patch['norm']
            verts=[]
            for label,(t,w) in zip(patch['labels'],xy):
                p=tuple(scale*f[i]+n*(r[i]*t/dot(r,r)+s[i]*w/dot(s,s)) for i in range(3))
                if label in copies: assert copies[label]==p, 'shared-vertex seam mismatch'
                copies[label]=p;verts.append(p)
            spatial.append(tuple(verts));scales.append(scale);areas.append(area)
            labels=patch['labels']
            for a,b in zip(labels,labels[1:]+labels[:1]):
                boundary[tuple(sorted((a,b)))]+=1 if a<b else -1
        assert len(copies)==8 and len(boundary)==18 and all(v==0 for v in boundary.values())
        assert len(set(scales))==1
        scale=scales[0];volume=F(0)
        for p,q,r in spatial:
            normal=cross(sub(q,p),sub(r,p))
            assert dot(normal,p)>0
            assert all(dot(normal,sub(v,p))<=0 for v in copies.values())
            cell=det(transpose((p,q,r)))/6
            assert cell>0 and cell==F(2,9)*scale**3
            volume+=cell
        assert volume==F(8,3)*scale**3
        # Oracle comparison follows validation; decoder itself used only its atlas.
        assert copies=={k:tuple(scale*x for x in p) for k,p in points.items()}
        return {'scale':str(scale),'triangles':12,'shared_vertices':8,
                'boundary_zero':True,'supporting_halfspaces':True,
                'minimum_oriented_chart_area':str(min(areas)),
                'positive_volume':str(volume),'atlas_geometry_admissible':True}

    # Each transition applies its specified coefficient map columnwise to the
    # geometric chart samples as well as to an arbitrary phase input.
    candidates={
        'original_1836':((L,'local'),(G,'local'),(N,'local')),
        'wire_feedback_576':((L,'local'),(G,'local'),(Id,'local')),
        'compressed_73':((B,'shared'),(unit,'shared'),(A,'local')),
        'compressed_72':((B,'shared'),(A,'local')),
    }
    reports={}
    for name,steps in candidates.items():
        composite=Id
        for M,_ in steps: composite=zmm(M,composite)
        assert composite==N
        count=sum(sum(z!=ZERO for row in M for z in row) for M,_ in steps)
        expected=int(name.rsplit('_',1)[1]);assert count==expected
        scale_reports=[]
        for scale in (F(1,10),F(1),F(2),F(7,3)):
            state=zreal(tuple(tuple(scale*x for x in row) for row in X))
            stage_reports=[]
            for i,(M,kind) in enumerate(steps):
                state=zmm(M,state)
                if kind=='local': charts=local_charts(state)
                else:
                    assert len(state)==1
                    charts=[tuple(state[0])]*12
                checked=decode(charts)
                assert checked['scale']==str(scale)
                checked['stage']=i+1;checked['chart_storage']=kind
                stage_reports.append(checked)
            scale_reports.append(stage_reports)
        reports[name]={'arrows':count,'exact_target_on_all_phase_inputs':True,
                       'all_tested_stages_geometrically_positive':True,
                       'scale_checks':scale_reports}
    # Hostile controls are judged by the same decoder, not by preset verdicts.
    def rejects(charts):
        try: decode(charts)
        except AssertionError as exc: return str(exc)
        raise AssertionError('invalid atlas was accepted')
    zero=rejects([tuple(ZERO for _ in ref)]*12)
    flipped=rejects([(ref[0],ref[2],ref[1])]*12)
    cracked=[ref]*12;cracked[0]=tuple(zscale(z,2) for z in ref)
    seam=rejects(cracked)
    assert zero=='nonpositive oriented chart area'
    assert flipped=='nonpositive oriented chart area'
    assert seam=='shared-vertex seam mismatch'
    # Lower bounds for the same declared class: all 36 input columns and output
    # rows of N are nonzero. Separate linear stages need 36 + 1 + 36 transfers,
    # or 36 + 36 for two passes. The positive atlas constructions attain them.
    assert all(any(N[j][i]!=ZERO for j in range(36)) for i in range(36))
    assert all(any(z!=ZERO for z in row) for row in N)
    serial_patches=[{k:([str(x) for x in v] if isinstance(v,tuple) and k!='labels'
                        else list(v) if k=='labels' else str(v)) for k,v in p.items()} for p in patches]
    report={'audit_assertions_passed':True,
            'model':'registered positive-homothetic tetrahedral family with explicit shared immutable atlas at every stage',
            'phase_input_domain':'all C^36; exact target N',
            'geometry_input_domain':'scale * reference labelled mesh, scale > 0; arbitrary poses/deformations not claimed',
            'atlas':{'patches':serial_patches,'reference_chart':[[str(x) for x in z] for z in ref],
                     'reference_offset_from_mode_frame':'f=cross(r,s)/2',
                     'coordinate_orientation':'t=Re(alpha), w=-Im_sqrt3(alpha)',
                     'scale_decode':'scale=-10*Re(alpha_corner_1)',
                     'embedding':'scale*f + norm*(r*t/dot(r,r) + s*w/dot(s,s))',
                     'sharing':'shared stages retain all twelve patch embeddings and incidence labels, not only a scalar'},
            'candidates':reports,
            'negative_controls':{'zero_area':zero,'reversed_orientation':flipped,'positive_cells_with_broken_seam':seam},
            'analytic_scale_extension':'Linear operators scale chart samples by scale; decoded vertices scale by scale, chart areas by scale^2 and oriented volumes by scale^3. Thus checks extend to all scale>0.',
            'conditional_minima':{'three_stage':73,'two_pass':72,
                                  'accounting':'Nonzero scalar coefficient transfers between disjoint stage ports; static atlas descriptions are declared model data, not additional interaction arrows.',
                                  'limitations':'Does not minimize atlas storage or geometric reconstruction circuitry; not a derivation of the spatial carrier or a theorem for arbitrary positive geometries.'}}
    dest=Path(__file__).resolve().parents[1]/'results'/'stagewise-positive-atlas.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: explicit atlas witnesses preserve positive geometry at every stage for 1836, 576, 73 and 72 arrows. Zero-area, reversed and cracked atlases rejected. Registered-family minima: 73 (three stages), 72 (two passes), with shared atlas data declared.')

if __name__=='__main__': main()
