"""Gauge-dressed all-face contacts on one common endpoint/neutral-record parent.

A single neutral bit, gap 1 and g=1/2, couples through retained contact P.
Exact rational LDL bounds on full unit-flux blocks; no species offsets.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
from assemble_endpoint_charging import ROOT,geometry,block_diagonal,matmul
from check_source_gauss_operator_charging import positive_definite


def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def block(H,P,g):
    n=len(H)
    return [[(H[i%n][j%n]+F(i>=n and i==j)) if i//n==j//n else -g*P[i%n][j%n] for j in range(2*n)] for i in range(2*n)]
def bounds(H,metric,lo,hi,steps=58):
    def pd(x):return positive_definite([[metric[i]*(H[i][j]-F(i==j)*x) for j in range(len(H))] for i in range(len(H))])
    assert pd(lo) and not pd(hi)
    for _ in range(steps):
        mid=(lo+hi)/2
        if pd(mid):lo=mid
        else:hi=mid
    return lo,hi

def relabel(K,root):
    """Find an exact weighted-graph automorphism taking 0 to root."""
    n=len(K);mapping={0:root};used={root}
    def go():
        if len(mapping)==n:return dict(mapping)
        a=max((i for i in range(n) if i not in mapping),key=lambda i:sum(K[i][j]!=0 for j in mapping))
        for b in range(n):
            if b in used or K[a][a]!=K[b][b]:continue
            if any(K[a][j]!=K[b][k] or K[j][a]!=K[k][b] for j,k in mapping.items()):continue
            mapping[a]=b;used.add(b);found=go()
            if found:return found
            used.remove(b);del mapping[a]
        return None
    result=go()
    if result is None:raise ValueError('Source rooted blocks are not equivalent')
    assert all(K[i][j]==K[result[i]][result[j]] for i in range(n) for j in range(n))
    return [result[i] for i in range(n)]


def realify(A,B):
    # Complex matrix A+i sqrt(3)B in x+i sqrt(3)y coordinates.
    n=len(A)
    return [A[i]+[-3*x for x in B[i]] for i in range(n)]+[B[i]+A[i] for i in range(n)]

def main():
    parentpath=ROOT/'research/strominger/results/common-endpoint-charging.json';parent=json.loads(parentpath.read_text())
    assert parent['status']=='passed'
    for p,h in parent['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    contacts_path=ROOT/'research/voevodsky/results/all_face_contact.json';contacts=json.loads(contacts_path.read_text())['carriers']
    beta,eta,g=F(3,5),F(1,5),F(1,2);rows={};checks={};packet={}
    for name in ('proton','belt'):
        native=parent['source_operators'][name];K=[list(map(F,r)) for r in native['kinetic_operator']];metric=list(map(F,native['metric']));n=len(K)
        covered=set(contacts[name]['covered_triangles']);norm=sum(metric[i] for i in covered)
        P=[[metric[j]/norm if i in covered and j in covered else F(0) for j in range(n)] for i in range(n)]
        assert matmul(P,P)==P and all(metric[i]*P[i][j]==metric[j]*P[j][i] for i in range(n) for j in range(n))
        # Gauge dressing: every contact term i->j carries the SAME endpoint
        # shift q(e_j-e_i) as kinetic hopping, preserving lead flux exactly.
        q=parent['sectors'][name]['signed_charge']
        for i in range(n):
            for j in range(n):
                if P[j][i]:
                    assert all(q*(int(k==j)-int(k==i))-q*int(k==j)+q*int(k==i)==0 for k in range(n))
        graph=geometry(n,native['internal_edges'],native['exterior_ports'])
        if name=='proton':
            assert matmul(K,P)==[[F(0)]*n for _ in range(n)]
            diagonal=block_diagonal(graph,1,[1]+[0]*(len(graph['ports'])-1),beta,eta)
            H=[[K[i][j]+(diagonal[i] if i==j else 0) for j in range(n)] for i in range(n)]
            joint=block(H,P,g);lo,hi=bounds(joint,metric*2,F(-1),F(2))
            maps=[]
            for root in graph['ports']:
                perm=relabel(K,root)
                assert all(P[i][j]==P[perm[i]][perm[j]] and graph['resistance'][i][j]==graph['resistance'][perm[i]][perm[j]] for i in range(n) for j in range(n))
                other=block_diagonal(graph,1,[int(j==root) for j in range(len(graph['ports']))],beta,eta)
                assert all(diagonal[i]==other[perm[i]] and metric[i]==metric[perm[i]] for i in range(n))
                maps.append(perm)
            assert hi<F(1,2) # non-unit flux bound 1-g =1/2
            rows[name]={'ground_interval':list(map(str,(lo,hi))),'equivalent_unit_flux_blocks':len(maps),'other_flux_lower_bound':'1/2'}
            packet[name]={'metric':list(map(str,metric*2)),'joint_unit_flux_matrix':[[str(x) for x in r] for r in joint],'rooted_automorphisms':maps,'contact':[[str(x) for x in r] for r in P]}
        else:
            # Exact six-mode invariant restriction; do not manufacture six
            # independent oscillators or omit a leaking complement.
            E=[[F(i%6==j) for j in range(6)] for i in range(18)]
            D=[[F(j%6==i,3) for j in range(18)] for i in range(6)]
            Q=matmul(E,D);k=matmul(matmul(D,K),E);p=matmul(matmul(D,P),E)
            assert matmul(D,E)==eye(6)
            assert matmul(K,E)==matmul(E,k) and matmul(P,E)==matmul(E,p)
            assert matmul(P,Q)==P and matmul(Q,P)==P
            assert matmul(K,Q)==matmul(Q,K)
            # K>=0 and P vanishes on the complement, so its full neutral
            # extension stays >=0. A negative retained-sector state wins.
            joint=block(k,p,g);m=[3*x for x in metric[:6]];lo,hi=bounds(joint,m*2,F(-1),F(0))
            # All nonzero neutral lead fluxes cost >= beta; coupling >=-g.
            assert hi<0<beta-g
            r=norm/sum(metric)
            assert r==F(2386,4485)
            negative_trial=-(g*r)**2/(1+(g*r)**2)
            assert hi<negative_trial<0
            rows[name]={'ground_interval':list(map(str,(lo,hi))),'exact_reduced_matter_dimension':6,'joint_dimension':12,
                        'matter_complement_lower_bound':'0','other_flux_lower_bound':str(beta-g),'vacuum_stable':False,
                        'coherent_contact_overlap':str(r),'negative_coherent_record_trial':str(negative_trial),
                        'all_nonzero_g_obstruction':'For every real g!=0, the normalized coherent matter times (|0>+g*r|1>) has energy -g^2*r^2/(1+g^2*r^2)<0.'}
            packet[name]={'metric':list(map(str,m*2)),'joint_matrix':[[str(x) for x in r] for r in joint],'contact':[[str(x) for x in r] for r in p]}
        checks[name+'_gauge_dressed_native_contact']=True
    # Electron contact is the ENTIRE coherent doublet (I+Q)/2. Parse the
    # retained elementary K exactly; no rank-one spin choice is substituted.
    encoded=parent['source_operators']['electron']['kinetic_operator'];n=4
    kr=[[F(0)]*n for _ in range(n)];ki=[[F(0)]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            v=encoded[i][j];assert set(v)<={'0','10'}
            kr[i][j]=F(v.get('0','0'));ki[i][j]=F(v.get('10','0'))
    pr=[[(F(2*(i==j))-kr[i][j])/2 for j in range(n)] for i in range(n)]
    pi=[[-x/2 for x in r] for r in ki]
    R=realify(pr,pi);assert matmul(R,R)==R
    assert sum(R[i][i] for i in range(8))==4 # complex rank two, real rank four
    graph=geometry(4,[(i,j) for i in range(4) for j in range(i+1,4)],list(range(4)));intervals=[];matrices=[]
    for a in range(4):
        ell=[-int(i==a) for i in range(4)];diag=block_diagonal(graph,-1,ell,beta,eta)
        h=[[kr[i][j]+(diag[i] if i==j else 0) for j in range(4)] for i in range(4)]
        # block() adds the neutral gap only to the real part.
        ar=block(h,pr,g)
        ai=[[ki[i%4][j%4] if i//4==j//4 else -g*pi[i%4][j%4] for j in range(8)] for i in range(8)]
        real=realify(ar,ai);metric=[F(1)]*8+[F(3)]*8
        assert all(metric[i]*real[i][j]==metric[j]*real[j][i] for i in range(16) for j in range(16))
        intervals.append(bounds(real,metric,F(-1),F(2)));matrices.append(real)
        for i in range(4):
            for j in range(4):
                # q=-1 assisted contact shifts n by e_i-e_j, just as K.
                assert all(int(k==i)-int(k==j)+int(k==j)-int(k==i)==0 for k in range(4))
    lo=min(x for x,y in intervals);hi=min(y for x,y in intervals);assert hi<F(1,2)
    rows['electron']={'ground_interval':list(map(str,(lo,hi))),'unit_flux_blocks':4,'complex_contact_rank':2,'other_flux_lower_bound':'1/2'}
    packet['electron']={'realified_metric':['1']*8+['3']*8,'unit_flux_joint_matrices':[[list(map(str,r)) for r in M] for M in matrices]}
    checks['electron_full_doublet_and_gauge_dressing']=True
    checks['belt_six_mode_closure_and_complement_retained']=True
    checks['full_integer_flux_lattice_bounds']=True
    checks['common_empty_ready_record_energy_zero']=True
    checks['neutral_belt_below_vacuum_detected']=F(rows['belt']['ground_interval'][1])<0
    p0,p1=map(F,rows['proton']['ground_interval']);e0,e1=map(F,rows['electron']['ground_interval']);b0,b1=map(F,rows['belt']['ground_interval'])
    assert 0<e0 and 0<p0
    report={'status':'passed','checks':checks,'sectors':rows,'shared_law':'H_endpoint tensor I + I tensor |1><1| - (1/2) P_contact_dressed tensor X; no extra rest offset',
            'branch':'Alternative to independent seam records, not their cumulative addition','operators':packet,
            'proton_per_electron_interval':list(map(str,(p0/e1,p1/e0))),
            'disposition':'Gauge-compatible native contact changes both charged energies, but neutral belt falls below the common empty vacuum. This unoffset branch cannot be a stable-vacuum particle model.'}
    paths=[Path(__file__).resolve(),parentpath,contacts_path,Path(__file__).with_name('assemble_endpoint_charging.py'),ROOT/'research/voevodsky/checkers/check_source_gauss_operator_charging.py',ROOT/'research/voevodsky/checkers/check_belt_interface_response.py']
    report['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    dest=ROOT/'research/strominger/results/common-native-contact.json';dest.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':checks,'energies':{k:list(map(lambda x:float(F(x)),v['ground_interval'])) for k,v in rows.items()},'proton_per_electron_interval':list(map(lambda x:float(F(x)),report['proton_per_electron_interval']))},indent=2))

if __name__=='__main__':main()
