"""Exact, reusable gates for conjectures on the twelve-triangle carrier.

A case supplies a concrete macro rewrite, geometry, and observable domain.
No absent certificate is interpreted as a successful physical conjecture.
"""
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from fractions import Fraction as F
from itertools import combinations
from abstract_port_net import PortNet, Signature, Agent
from check_twenty_four_triangle_shared_seed import A,B,closure
from check_twelve_triangle_positive_geometry import (
    POINTS,LABELS,I,ONE,ZERO,OMEGA,mean,transpose,mm,mv,det,dot,sub,cross,
    zadd,zmul,zconj,zscale,zmm,zreal,projector,znorm,
)
from check_collective_four_state_identity import rank

SIG={'TRI':Signature('p',('l','r')),
     'JUNCTION':Signature('p',('a1','a2','b0','b1','b2'))}
JP=('p','a1','a2','b0','b1','b2')


def eye(n): return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def add(a,b): return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def scale(a,c): return tuple(tuple(c*x for x in r) for r in a)
def inverse(m):
    n=len(m);a=[list(row)+list(eye(n)[i]) for i,row in enumerate(m)]
    for j in range(n):
        p=next(i for i in range(j,n) if a[i][j])
        a[j],a[p]=a[p],a[j];v=a[j][j];a[j]=[x/v for x in a[j]]
        for i in range(n):
            if i!=j:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[j])]
    return tuple(tuple(row[n:]) for row in a)

def snapshot(net): return (dict(net.nodes),dict(net.wires),net.serial)
def clone(net):
    out=PortNet(net.signatures)
    out.nodes=dict(net.nodes);out.wires=dict(net.wires);out.serial=net.serial
    return out

def owners(net): return {h:n for n,a in net.nodes.items() for h in a.handles}
def label(net,n): return net.nodes[n].handles[0] if net.nodes[n].handles else 'J'
def port_edges(net):
    return {((label(net,n),p),(label(net,m),q)) for (n,p),(m,q) in net.wires.items()}

def fixture():
    points=dict(POINTS);triangles={}
    for p in closure((A,B)):
        a,b,c=[LABELS[p[i]] for i in range(3)]
        centre='F_'+''.join(sorted((a,b,c)))
        points[centre]=mean([POINTS[k] for k in (a,b,c)])
        triangles[a+b]=(centre,a,b)
    net=PortNet(SIG);ids={k:net.add('TRI',(k,)) for k in sorted(triangles)}
    interfaces=defaultdict(list)
    for name,(f,a,b) in triangles.items():
        for port,edge in (('p',(a,b)),('l',(f,a)),('r',(b,f))):
            interfaces[tuple(sorted(edge))].append((ids[name],port))
    for ends in interfaces.values():
        assert len(ends)==2;net.link(*ends)
    net.validate()
    return net,points,triangles

def face_cycle(triangles,face):
    selected=sorted(k for k,t in triangles.items() if t[0]==face)
    nxt={triangles[k][1]:triangles[k][2] for k in selected}
    a=min(nxt);b=nxt[a];c=nxt[b];assert nxt[c]==a
    return selected,(a,b,c)

def laplacian(net,junction_weight=F(2)):
    names=sorted(label(net,n) for n in net.nodes);index={k:i for i,k in enumerate(names)}
    n=len(names);L=[[F(0)]*n for _ in names]
    edges={tuple(sorted((label(net,a),label(net,b)))) for (a,p),(b,q) in net.wires.items()}
    assert len(edges)==len(net.wires)//2 # this fixture has no parallel agent wires
    for a,b in edges:
        w=junction_weight if 'J' in (a,b) else F(1)
        i,j=index[a],index[b]
        L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    return names,tuple(tuple(r) for r in L)

def seed_embedding(names):
    # Four retained state records: common identity plus oriented endpoint contrasts.
    return tuple(tuple(F(1,4)+(F(name[0]==k)-F(name[1]==k) if name!='J' else 0)
                       for k in LABELS) for name in names)

def seed_response(net,junction_weight=F(2)):
    names,L=laplacian(net,junction_weight)
    W=seed_embedding(names)
    H=tuple(tuple(F(i==j)-F(1,4) for j in range(4)) for i in range(4))
    return mm(L,W)==mm(W,scale(H,5))

def boundary_response(L,names,terminals,z):
    keep=[names.index(k) for k in terminals];inside=[i for i in range(len(names)) if i not in keep]
    M=add(L,scale(eye(len(names)),z))
    bb=tuple(tuple(M[i][j] for j in keep) for i in keep)
    bi=tuple(tuple(M[i][j] for j in inside) for i in keep)
    ii=tuple(tuple(M[i][j] for j in inside) for i in inside)
    return add(bb,scale(mm(mm(bi,inverse(ii)),transpose(bi)),-1))

def hidden_realization_order(L,names,terminals):
    keep=[names.index(k) for k in terminals];inside=[i for i in range(len(names)) if i not in keep]
    A=tuple(tuple(L[i][j] for j in inside) for i in inside)
    B=tuple(tuple(L[i][j] for j in inside) for i in keep)
    observable=[];power=eye(len(inside))
    for _ in inside:
        observable.extend(mm(B,power));power=mm(power,A)
    order=rank(tuple(observable))
    # For a real symmetric A, observability and controllability are adjoint.
    return {'hidden_states':len(inside),'observable_order':order,'dark_states':len(inside)-order}


def coplanar_overlap(a,b,normal):
    drop=max(range(3),key=lambda i:abs(normal[i]));axes=[i for i in range(3) if i!=drop]
    aa=[tuple(p[i] for i in axes) for p in a];bb=[tuple(p[i] for i in axes) for p in b]
    for tri in (aa,bb):
        for p,q in zip(tri,tri[1:]+tri[:1]):
            axis=(-(q[1]-p[1]),q[0]-p[0])
            x=[dot(axis,v) for v in aa];y=[dot(axis,v) for v in bb]
            if max(x)<=min(y) or max(y)<=min(x): return False
    return True

def geometry(points,triangles):
    used={v for t in triangles for v in t}
    assert len({points[v] for v in used})==len(used),'coincident differently named vertices'
    interior=mean([points[v] for v in sorted(used)])
    boundary=Counter();degrees=Counter();volume=F(0);faces=[]
    for t in triangles:
        p,q,r=[points[k] for k in t]
        n=cross(sub(q,p),sub(r,p))
        assert dot(n,n)>0,'degenerate face'
        assert dot(n,sub(p,interior))>0,'inverted or flat cell'
        assert all(dot(n,sub(points[k],p))<=0 for k in used),'nonconvex support or overlap'
        vol=det(transpose((sub(p,interior),sub(q,interior),sub(r,interior))))/6
        assert vol>0,'nonpositive interior cone'
        volume+=vol;faces.append(((p,q,r),n))
        for a,b in zip(t,t[1:]+t[:1]):
            e=tuple(sorted((a,b)));boundary[e]+=1 if a<b else -1;degrees[e]+=1
    assert all(n==0 for n in boundary.values()),'open seam'
    assert all(n==2 for n in degrees.values()),'nonmanifold boundary edge'
    assert len(used)-len(degrees)+len(triangles)==2,'incorrect boundary Euler characteristic'
    for (a,n),(b,m) in combinations(faces,2):
        if all(dot(n,sub(v,a[0]))==0 for v in b):
            assert not coplanar_overlap(a,b,n),'overlapping coplanar face interiors'
    return {'vertices':len(used),'faces':len(triangles),'volume':str(volume),
            'positive_cones':True,'seams_closed':True,'interiors_compatible':True}

def release_recipe(net,triangles,face):
    selected,cap=face_cycle(triangles,face);own=owners(net)
    region_names=sorted(set(selected)|{k[::-1] for k in selected})
    region=tuple(own[k] for k in region_names);loc={n:i for i,n in enumerate(region)}
    replacements=tuple(net.nodes[n] for n in region)+(Agent('JUNCTION'),)
    boundary={};internal=[];seen=set()
    for ep,peer in net.wires.items():
        if ep[0] not in loc: continue
        if peer[0] not in loc:
            boundary[ep]=(loc[ep[0]],ep[1]);continue
        pair=tuple(sorted((ep,peer)))
        if pair in seen: continue
        seen.add(pair)
        if ep[1]==peer[1]=='p': continue # the three cross-face links are split
        internal.append(((loc[ep[0]],ep[1]),(loc[peer[0]],peer[1])))
    for k,jp,jq in zip(selected,JP[:3],JP[3:]):
        internal.append(((loc[own[k]],'p'),(6,jp)))
        internal.append(((loc[own[k[::-1]]],'p'),(6,jq)))
    assert len(region)==6 and len(boundary)==6
    return region,replacements,tuple(internal),boundary,selected,cap

def release(net,triangles,face):
    recipe=release_recipe(net,triangles,face)
    out=clone(net);out.replace_region(*recipe[:4]);out.validate()
    assert set(owners(out))==set(owners(net))
    return out,recipe[4],recipe[5]

def release_geometry(points,triangles,face,cap,factor=F(3)):
    new=dict(points);new[face]=tuple(factor*x for x in points[face])
    body=[t for t in triangles.values() if t[0]!=face]+[cap]
    companion=[t for t in triangles.values() if t[0]==face]+[(cap[0],cap[2],cap[1])]
    union=list(triangles.values())
    result={'body':geometry(new,body),'companion':geometry(new,companion),'union':geometry(new,union)}
    assert F(result['body']['volume'])==F(8,3)
    assert F(result['companion']['volume'])==F(2,3)*(factor-1)
    assert F(result['union']['volume'])==F(8,3)+F(2,3)*(factor-1)
    return new,body,companion,result

def geometry_path_certificate(before,after,bodies):
    """Certify the whole affine geometry path, including a declared 2D birth.

    Expand determinants exactly as polynomials in t. No sampling stands in for
    strict positivity between stages. A 'born' body must be positive for every
    t>0; other cells must also be positive at t=0.
    """
    def polynomial(start,end):
        delta=tuple(sub(b,a) for a,b in zip(start,end));coeff=[]
        for degree in range(4):
            coeff.append(sum(det(transpose(tuple(delta[i] if i in chosen else start[i] for i in range(3))))
                             for chosen in combinations(range(3),degree)))
        assert coeff[2:]==[0,0],'non-affine determinant requires a stronger positivity certificate'
        return coeff[0],coeff[1]
    evidence={}
    for name,triangles,born in bodies:
        used=sorted({p for t in triangles for p in t})
        centres=[mean([frame[p] for p in used]) for frame in (before,after)]
        volume=[F(0),F(0)];cone_coefficients=[];support_count=0
        for face in triangles:
            start=tuple(sub(before[p],centres[0]) for p in face)
            end=tuple(sub(after[p],centres[1]) for p in face)
            a,b=polynomial(start,end);a/=6;b/=6
            if born: assert a==0 and b>0,'nonpositive newborn cone'
            else: assert a>0 and a+b>0,'nonpositive intermediate cone'
            volume[0]+=a;volume[1]+=b;cone_coefficients.append((str(a),str(b)))
            for p in used:
                vectors=[]
                for frame in (before,after):
                    origin=frame[face[0]]
                    vectors.append(tuple(sub(frame[v],origin) for v in (face[1],face[2],p)))
                x,y=polynomial(*vectors)
                assert x<=0 and x+y<=0,'intermediate support violation'
                support_count+=1
        evidence[name]={'volume_polynomial':[str(x) for x in volume],
                        'positive_cone_polynomials':cone_coefficients,
                        'affine_support_inequalities':support_count,
                        'positive_domain':'0<t<=1; positive 2D source patch at t=0' if born else '0<=t<=1'}
    return evidence


def zsub(a,b): return zadd(a,zscale(b,-1))
def chiral_mode(names,cap):
    a,b,c=cap
    potentials={k:ZERO for k in LABELS}
    potentials.update({a:ONE,b:zmul(OMEGA,OMEGA),c:OMEGA})
    return tuple(ZERO if name=='J' else zsub(potentials[name[0]],potentials[name[1]]) for name in names)

def is_eigen(L,v,eigenvalue):
    return zmm(zreal(L),tuple((z,) for z in v))==tuple((zscale(z,eigenvalue),) for z in v)

def currents(names,L,v,triangles):
    index={k:i for i,k in enumerate(names)};out={}
    for face in sorted({t[0] for t in triangles.values()}):
        _,(a,b,c)=face_cycle(triangles,face)
        cycle=(a+b,b+c,c+a)
        values=[]
        for x,y in zip(cycle,cycle[1:]+cycle[:1]):
            i,j=index[x],index[y]
            values.append(-L[i][j]*zmul(zconj(v[i]),v[j])[1])
        assert len(set(values))==1,'nonconserved loop current'
        out[face]=values[0]
    for i in range(len(names)):
        div=sum(-L[i][j]*zmul(zconj(v[i]),v[j])[1] for j in range(len(names)))
        assert div==0,'current divergence'
    return out


@dataclass
class Case:
    conjecture: str
    anchor: str
    checks: dict=field(default_factory=dict)
    details: dict=field(default_factory=dict)

    def check(self,name,operation):
        try:
            value=operation()
            assert value is not False,name
            self.checks[name]={'status':'pass'}
            if value is not None and value is not True: self.checks[name]['evidence']=value
            return True
        except (AssertionError,ValueError,ZeroDivisionError) as exc:
            self.checks[name]={'status':'fail','reason':str(exc) or name}
            return False

    def record(self,required):
        missing=[k for k in required if k not in self.checks]
        for k in missing:self.checks[k]={'status':'missing'}
        passed=all(self.checks[k]['status']=='pass' for k in required)
        return {'conjecture':self.conjecture,'anchor':self.anchor,
                'result':'passes_stated_fixture' if passed else 'candidate_not_established',
                'required_gates':list(required),'checks':self.checks,'details':self.details}
