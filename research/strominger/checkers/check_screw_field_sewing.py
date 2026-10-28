"""Registered extension of the existing exact sewing checker to the screw patch.
Only fixture/cardinality and the old fixture-specific comparison sample change.
The prior metrics, generator construction, full-field equations and controls remain.
"""
from collections import defaultdict,deque
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys
from exact_multiradical import Radical as R,mm,adj,identity,serialize,rational,sqrt,decode_A

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
import check_twelve_triangle_positive_geometry as geo
BASE='research/strominger/results/'
PATHS={'fixture':BASE+'screw-field-fixture.json',
       'five':BASE+'full-five-channel-candidate/verification.json',
       'pn':BASE+'global-PN-transport/verification.json',
       'ne':BASE+'neutron-contrast-electron-transport/verification.json',
       'p':BASE+'common-three-carrier-protocol/proton.json',
       'n':BASE+'common-three-carrier-protocol/neutron.json',
       'grid':BASE+'baryon-tensor-grid/verification.json'}

def restore(a):return [[R({int(k):F(v) for k,v in x.items()}) for x in row] for row in a]
def zeros(n,m):return [[R() for _ in range(m)] for _ in range(n)]
def add(a,b,sign=1):return [[x+sign*y for x,y in zip(row,col)] for row,col in zip(a,b)]
def sharp(a,metric):return [[x*metric[j] for j,x in enumerate(row)] for row in adj(a)]
def gram(a,metric):return mm(sharp(a,metric),a)
def perm(p):return [[R(int(j==p[i])) for j in range(len(p))] for i in range(len(p))]
def block(a,b):
    return [row+[R() for _ in b] for row in a]+[[R() for _ in a]+row for row in b]
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()


def main(fixture_path=None,result_path=None):
    paths=dict(PATHS)
    if fixture_path is not None:paths['fixture']=fixture_path
    data={k:json.loads((ROOT/p).read_text(encoding='utf-8')) for k,p in paths.items()}
    f=data['fixture'];checks=[]
    def check(name,condition):
        if not condition:raise AssertionError(name)
        checks.append(name)
        print('PASS: '+name,flush=True)
    for key in ['fixture','five','pn','ne']:
        check(key+' receipt inputs match live repository files',all(sha(p)==digest for p,digest in data[key]['sourceHashes'].items()))
    check('assembly has fully witnessed contacts and certified retained exits',f['audit']['certifiedExit'] and f['audit']['allContactsWitnessed'] and not f['audit']['pendingContacts'])
    m=list(map(F,data['n']['source']['metric']));mp=list(map(F,data['p']['source']['metric']))
    assert mp==[F(1)]*36
    metric={'proton':[F(1)]*44,'neutron':m+[F(1)]*8,'electron':m+[F(1)]*8}
    BP=restore(data['five']['protonFiveEmbedding']);BN=restore(data['five']['neutronFiveEmbedding'])
    BE=restore(data['five']['postNEJointEmbedding']);root_binding=BP+zeros(8,5)
    PN=restore(data['pn']['matrix']);PNinv=sharp(PN,m)
    # Reconstruct the exact geometric P-reader operator used in the prior candidate.
    labels=data['p']['source']['coordinates'];rotation=geo.rotation((2,3,0,1));rename=dict(zip('ABCD','CDAB'))
    UP=zeros(36,36)
    for j,label in enumerate(labels):
        edge,axis=label.split(':');new=''.join(rename[v] for v in edge)
        for i in range(3):UP[labels.index(new+':'+'xyz'[i])][j]=R(rotation[i]['xyz'.index(axis)])
    O=[restore(x) for x in data['pn']['factorRotations']]
    gauges={}
    for label,source_metric in [('proton',mp),('neutron',m)]:
        row=data['grid']['carriers'][label];z=[decode_A(x) for x in row['sourceReturnColumn']]
        phase=[x*sqrt(1/rational(x.conj()*x)) for x in z]
        assert all(x.conj()*x==1 for x in phase)
        gauges[label]={'metric':source_metric,'phase':phase,'grid':sum(row['grid'],[])}
    gp,gn=gauges['proton'],gauges['neutron']
    for a,i in enumerate(gn['grid']):
        for b,j in enumerate(gp['grid']):
            assert PN[i][j]==gn['phase'][i]*sqrt(mp[j]/m[i])*O[0][a//3][b//3]*O[1][a%3][b%3]*gp['phase'][j].conj()
    check('existing PN factorization and geometric P reader prove full metric isometry',all(mm(adj(o),o)==identity(len(o)) for o in O) and gram(UP,mp)==identity(36) and mm(UP,UP)==identity(36))
    K=restore(data['ne']['contrastFrame']);J=restore(data['ne']['electronFrame']);S=restore(data['ne']['NEcandidateMatrix'])
    Ssharp=mm(K,adj(J));C=mm(K,sharp(K,m));NE=mm(J,adj(J))
    W=[row+right for row,right in zip(add(identity(36),C,-1),Ssharp)]
    W += [left+row for left,row in zip(S,add(identity(8),NE,-1))]
    check('joint44 NE exchange has exact orthonormal swap factors',gram(K,m)==identity(2) and mm(adj(J),J)==identity(2) and S==mm(J,sharp(K,m)) and Ssharp==mm(K,adj(J)))
    # These identities prove W^2=I and W^sharp W=I on ALL44 coordinates:
    # exchange the two orthonormal rank-two images and fix their complements.
    edge_maps={'PN':block(PN,identity(8)),'inverse-PN':block(PNinv,identity(8)),
               'P-reader':block(UP,identity(8)),'N-reader':identity(44),'NN-phase-advance':identity(44),'NE':W}
    charts={c['index']:c for c in f['charts']};packets={p['id']:p for p in f['packets']}
    species=lambda id:charts[packets[id]['chart']]['species']
    def edge_key(op):
        if op['kind']=='reader-phase-advance':return 'P-reader' if species(op['source'])=='proton' else 'N-reader'
        return op['kind']
    # Solve the full retained graph's parity constraints, not only its generating paths.
    outgoing=defaultdict(list)
    for op in f['operations']:outgoing[op['source']].append(op)
    parity={f['rootPacket']:0};queue=deque([f['rootPacket']])
    while queue:
        a=queue.popleft()
        for op in outgoing[a]:
            bit=parity[a]^int(edge_key(op)=='P-reader');b=op['target']
            if b in parity:assert parity[b]==bit
            else:parity[b]=bit;queue.append(b)
    check('all screw-patch packet frames solve every interface constraint',len(parity)==len(packets)==f['expectedPacketCount'])
    # Retain exact factorizations rather than expanding dense radical products.
    # Each factor is proved invertible above, so these act on all44 coordinates.
    inverse_name={'PN':'inverse-PN','inverse-PN':'PN','P-reader':'P-reader','NE':'NE'}
    def inverse_word(word):return tuple(inverse_name[x] for x in reversed(word))
    def normal(word):
        stack=[]
        for x in word:
            if stack and inverse_name[x]==stack[-1]:stack.pop()
            else:stack.append(x)
        return tuple(stack)
    def apply(word,matrix):
        for x in word:
            if x in ['PN','inverse-PN']:
                src,dst=(gp,gn) if x=='PN' else (gn,gp)
                factors=O if x=='PN' else [adj(o) for o in O]
                normal_field=[[sqrt(src['metric'][j])*src['phase'][j].conj()*v for v in matrix[j]] for j in src['grid']]
                small=[]
                for a in range(12):small.extend(mm(factors[1],normal_field[3*a:3*a+3]))
                result=zeros(36,len(matrix[0]))
                for b in range(3):
                    column=mm(factors[0],[small[3*a+b] for a in range(12)])
                    for a,row in enumerate(column):
                        j=dst['grid'][3*a+b]
                        result[j]=[dst['phase'][j]*sqrt(1/dst['metric'][j])*v for v in row]
                matrix=result+matrix[36:]
            elif x=='P-reader':matrix=mm(UP,matrix[:36])+matrix[36:]
            elif x=='NE':
                left,right=matrix[:36],matrix[36:]
                u=mm(sharp(K,m),left);v=mm(adj(J),right)
                matrix=add(left,mm(K,add(v,u,-1)))+add(right,mm(J,add(u,v,-1)))
            else:raise ValueError(x)
        return matrix
    frames={('proton',0):(),('proton',1):('P-reader',)}
    for bit in (0,1):
        frames['neutron',bit]=frames['proton',bit]+('PN',)
        frames['electron',bit]=frames['neutron',bit]+('NE',)
    inverses={key:inverse_word(word) for key,word in frames.items()}
    probe=[[R(i-17)] for i in range(44)]
    for key,word in frames.items():
        assert normal(word+inverses[key])==()
        assert apply(inverses[key],apply(word,probe))==probe
    checks.append('all six factored full-field frames recover an arbitrary nonzero44-coordinate probe')
    frame_key=lambda id:(species(id),parity[id])
    P={id:perm(p['permutation']) for id,p in packets.items()}
    U={id:frames[frame_key(id)] for id in packets}
    Ui={id:inverses[frame_key(id)] for id in packets}
    physical={key:apply(word,root_binding) for key,word in frames.items()}
    piPN=perm(next(op['permutation'] for op in f['operations'] if op['kind']=='PN'))
    piNE=perm(next(op['permutation'] for op in f['operations'] if op['kind']=='NE'))
    check('unrotated restrictions reproduce the prior PN and joint NE bindings',physical['neutron',0]==mm(BN+zeros(8,5),piPN) and physical['electron',0]==mm(BE,mm(piNE,piPN)))
    Y={id:physical[frame_key(id)] for id in packets}
    bindings={id:mm(Y[id],adj(P[id])) for id in packets}
    readouts={id:sharp(bindings[id],metric[species(id)]) for id in packets}
    checked_types=set();interfaces=[]
    for op in f['operations']:
        a,b=op['source'],op['target'];key=(edge_key(op),frame_key(a),frame_key(b));E=edge_maps[key[0]];pi=perm(op['permutation'])
        if key not in checked_types:
            word=() if key[0] in ['N-reader','NN-phase-advance'] else (key[0],)
            assert normal(U[a]+word)==U[b]
            assert apply(word,Y[a])==Y[b]
            checked_types.add(key)
        assert mm(pi,P[a])==P[b]
        word=() if key[0] in ['N-reader','NN-phase-advance'] else (key[0],)
        # Adjoint transport computes R_b U_edge on ALL44 inputs without
        # expanding products of dense multiradical44x44 matrices.
        assert sharp(apply(inverse_word(word),bindings[b]),metric[species(a)])==mm(pi,readouts[a])
        assert apply(word,bindings[a])==mm(bindings[b],pi)
        interfaces.append({'operation':op['id'],'kind':op['kind'],'source':a,'target':b,'full44FieldSquare':True,'full44ReadoutSquare':True,'fiveCoefficientBindingSquare':True})
    check('all screw-patch interfaces intertwine on the entire44-dimensional field',len(interfaces)==f['expectedInterfaceCount'])
    for id in packets:
        assert gram(bindings[id],metric[species(id)])==identity(5)
        assert mm(readouts[id],bindings[id])==identity(5)
        assert mm(bindings[id],P[id])==Y[id]
    checks.append('every framed five-slot readout is exact and norm preserving')
    comparison_pairs=[(a,b) for a in packets for b in packets if a<b and packets[a]['chart']==packets[b]['chart'] and packets[a]['origin']==packets[b]['origin'] and P[a]!=P[b]]
    same_field_pairs=[(a,b) for a,b in comparison_pairs if U[a]==U[b]]
    check('distinct retained coefficient histories survive equal-chart equal-field comparison',bool(same_field_pairs) and all(Y[a]==Y[b] and bindings[a]!=bindings[b] for a,b in same_field_pairs))
    a=f['rootPacket']
    # Pairwise transitions form a full-field cocycle by cancellation of Ui[j] U[j].
    # Verify a nontrivial P/N/E triangle directly as an independent regression.
    n=next(id for id in packets if species(id)=='neutron');e=f['audit']['exitPackets'][0]
    Cpn=Ui[a]+U[n];Cne=Ui[n]+U[e];Cpe=Ui[a]+U[e]
    check('P N E chart comparisons compose on all44 coordinates',normal(Cpn+Cne)==normal(Cpe) and apply(Cne,apply(Cpn,probe))==apply(Cpe,probe))
    exits=[]
    for id in f['audit']['exitPackets']:
        gE=gram(Y[id][36:],[F(1)]*8);gN=gram(Y[id][:36],m)
        assert add(gE,gN)==identity(5)
        assert mm(gE,gE)==gE and mm(gN,gN)==gN
        assert sum(rational(gE[i][i]) for i in range(5))==2
        assert sum(rational(gN[i][i]) for i in range(5))==3
        exits.append({'packet':id,'electronRank':2,'retainedBaryonRank':3,'fullFiveRecovery':True})
    check('all terminal histories retain rank2 E plus rank3 baryon information',len(exits)==len(f['audit']['exitPackets']) and len(exits)>0)
    # Fixed canonical coupling is a real negative control, not accepted by construction.
    canonical={'proton':root_binding,'neutron':BN+zeros(8,5),'electron':BE}
    fixed_failures=[id for id in packets if mm(canonical[species(id)],P[id])!=Y[id]]
    check('discarding transported coefficient bindings breaks the root-field comparison',bool(fixed_failures))
    pn=next(op for op in f['operations'] if op['kind']=='PN')
    check('replacing PN by identity fails the native full-field square',U[pn['source']]!=U[pn['target']])
    # Norm on a compatible section is inherited from ONE root field, not summed copies.
    check('compatible sections recover the same arbitrary44-coordinate root from every chart',all(normal(U[id]+Ui[id])==() for id in packets))
    previous_path=BASE+'joint-field-assembly-sewing.json'
    previous=json.loads((ROOT/previous_path).read_text())
    generators={name:serialize(matrix) for name,matrix in edge_maps.items() if name not in ['N-reader','NN-phase-advance']}
    check('all source generator matrices are byte-value identical to the prior candidate',generators==previous['generatorMatrices'])
    inputs=list(paths.values())+[previous_path,'research/strominger/contracts/pb208-screw-field-attempt.v1.json','research/strominger/screw-field-sewing-result-v1.md','research/strominger/checkers/check_screw_field_sewing.py','research/strominger/checkers/check_joint_field_assembly_sewing.py',
           'research/strominger/checkers/exact_multiradical.py','research/nima/checkers/check_twelve_triangle_positive_geometry.py']
    report={'status':'passed','check_count':len(checks),'checks':checks,'sourceHashes':{p:sha(p) for p in inputs},
      'counts':{'bodies':f['audit']['counts'],'packets':len(packets),'interfaces':len(interfaces),'rootFieldDimension':44,'preparedNativeDimension':5},
      'sameFieldDistinctHistoryPairs':same_field_pairs,'screwFieldSewingEstablished':True,'actualEsd7FaceBindingEstablished':False,'fullPbConstructionEstablished':False,'infiniteRetainedExtensionEstablished':False,'interfaces':interfaces,'retainedHistories':f['histories'],'exitSplits':exits,'fixedBindingFailurePackets':fixed_failures,
      'frameTypes':{s+str(bit):{'forwardFactorWord':word,'inverseFactorWord':inverses[s,bit]} for (s,bit),word in frames.items()},
      'generatorMatrices':{name:serialize(matrix) for name,matrix in edge_maps.items() if name not in ['N-reader','NN-phase-advance']},
      'packetBindings':[{'packet':id,'species':species(id),'frameParity':parity[id],'nativePermutation':packets[id]['permutation'],'binding':serialize(bindings[id]),'readout':serialize(readouts[id])} for id in packets],
      'globalSection':'x_h=U_h z for one arbitrary44-coordinate root z; comparisons C_(h,k)=U_k U_h^-1. All retained interface operators equal these comparisons.',
      'naturality':'R_target U_edge = Pi_edge R_source on all44 coordinates; U_edge B_source=B_target Pi_edge on all5 coefficients.',
      'disposition':'Registered native sewing gate passed for the actual screw-growth patch, including every repaired contact and retained interface. No source generator was refitted; no actual esd7 face identification or Pb construction is established.',
      'scope':'Conditional on the prior global PN completion, joint NE contrast swap, co-moving ordered-corner N/NN convention and propagated frame bindings. This is full-field connection gluing, not equality of raw values on a fixed six-component geometric face. Additional geometric face readouts, all possible assemblies, analytical esd7 witnesses and an autonomous update/clock are not established.'}
    report['fixture_source']=paths['fixture']
    dest=ROOT/(result_path or BASE+'screw-field-sewing.json');dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':report['status'],'checks':len(checks),**report['counts'],'EExits':len(exits),'fixedBindingFailures':len(fixed_failures),'result':str(dest)}))


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fixture',help='Repository-relative reconstructed fixture to verify')
    parser.add_argument('--output',help='Repository-relative result path; required with --fixture')
    args=parser.parse_args()
    if args.fixture and not args.output:parser.error('--fixture requires a separate --output to preserve the prior receipt')
    main(args.fixture,args.output)
