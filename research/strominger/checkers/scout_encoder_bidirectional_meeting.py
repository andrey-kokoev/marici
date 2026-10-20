"""Bounded numerical meet-in-the-middle scout with exact gate descriptors.

Compares full whitened bright embeddings, not scalar endpoints. The shortlist
still needs the independent rational verifier. The known-word split is a
convention/regression control, not a newly discovered solution.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import numpy as np
from scipy.spatial import cKDTree

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[1]


def main(max_depth,epsilon):
    assert 0<=max_depth<=2, 'This exhaustive prototype caps each side at depth 2; deeper search needs a separate budget.'
    paths={'source':BASE/'results/neutron-seam-control-transport.json',
           'memory':BASE/'results/neutron-comparison-memory.json',
           'scattering':BASE/'results/neutron-autonomous-rim-scattering.json',
           'orbit':BASE/'results/encoder-conjugated-bank-controls.json',
           'known':BASE/'results/encoder-control-word-scout-refined.json'}
    raw={k:p.read_bytes() for k,p in paths.items()}
    data={k:json.loads(v) for k,v in raw.items()}
    for key in ('orbit','known'):
        for p,h in data[key]['source_hashes'].items():
            assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    def array(x):return np.array([[float(F(v)) for v in row] for row in x])
    M=array(data['source']['metric']);G=array(data['memory']['memory_metric'])
    B=array(data['memory']['residual_incidence']);E=array(data['scattering']['exact_bright_basis'])
    C=np.linalg.cholesky(M).T;Cm=np.linalg.cholesky(G).T
    Cg=np.linalg.cholesky(E.T@M@E).T
    Eorth=C@E@np.linalg.inv(Cg)
    D=Cm@B@np.linalg.inv(C)
    left,s,right=np.linalg.svd(D,full_matrices=False)
    assert s[14]>1e-6 and s[15]<1e-10
    W=left[:,:15]@right[:15,:]
    target=np.vstack(((np.eye(24)-W.T@W)@Eorth,W@Eorth)).astype(complex)
    initial=np.vstack((Eorth,np.zeros((21,5)))).astype(complex)
    Cfull=np.zeros((45,45));Cfull[:24,:24]=C;Cfull[24:,24:]=Cm
    directions=array(data['orbit']['directions'])@Cfull.T
    directions/=np.linalg.norm(directions,axis=1)[:,None]
    def apply(state,control):
        t=float(F(int(control['t_numerator']),int(control['t_denominator'])))
        z=(1-3*t*t+2j*np.sqrt(3)*t)/(1+3*t*t)
        d=directions[control['conjugate_direction']]
        return state+(z-1)*d[:,None]*(d@state)[None,:]
    def inverse(word):
        return [dict(c,t_numerator=str(-int(c['t_numerator']))) for c in reversed(word)]
    def execute(state,word):
        for control in word:state=apply(state,control)
        return state
    # Existing accepted word: a middle meeting must have the same error as the
    # complete forward execution. Wrong inverse order must be detected.
    known=data['known']['controls'];split=len(known)//2
    known_f=known[:split];known_b=inverse(known[split:])
    middle=np.linalg.norm(execute(initial,known_f)-execute(target,known_b))
    final=np.linalg.norm(execute(initial,known)-target)
    assert abs(middle-final)<1e-10
    assert middle<1e-6
    bad_b=[dict(c,t_numerator=str(-int(c['t_numerator']))) for c in known[split:]]
    wrong_order=np.linalg.norm(execute(initial,known_f)-execute(target,bad_b))
    assert wrong_order>1e-3
    assert inverse(inverse(known_b))==known_b
    # Fixed finite vocabulary: t=+/-1 yields inverse cube-root phases. Two
    # consecutive gates on the same direction always shorten (cancel or merge).
    alphabet=[{'conjugate_direction':i,'t_numerator':str(t),'t_denominator':'1'}
              for i in range(39) for t in (1,-1)]
    def expand(states,words):
        blocks=[];out_words=[]
        for control in alphabet:
            direction=control['conjugate_direction']
            indices=[i for i,w in enumerate(words) if not w or w[-1]['conjugate_direction']!=direction]
            if not indices:continue
            subset=states[indices]
            d=directions[direction]
            t=int(control['t_numerator']);z=complex(-.5,t*np.sqrt(3)/2)
            coefficients=np.einsum('i,nij->nj',d,subset)
            blocks.append(subset+(z-1)*d[None,:,None]*coefficients[:,None,:])
            out_words.extend([words[i]+[control] for i in indices])
        return np.concatenate(blocks,axis=0),out_words
    def features(states):
        flat=states.reshape(len(states),-1)
        return np.concatenate((flat.real,flat.imag),axis=1)
    forward=np.array([initial]);backward=np.array([target]);fw=[[]];bw=[[]]
    cumulative_f=forward;cumulative_b=backward;all_fw=fw[:];all_bw=bw[:]
    layers=[];best=None
    for depth in range(max_depth+1):
        if depth:
            forward,fw=expand(forward,fw);backward,bw=expand(backward,bw)
            cumulative_f=np.concatenate((cumulative_f,forward));cumulative_b=np.concatenate((cumulative_b,backward))
            all_fw+=fw;all_bw+=bw
        tree=cKDTree(features(cumulative_b))
        distances,indices=tree.query(features(cumulative_f),k=1,workers=1)
        fi=int(np.argmin(distances));bi=int(indices[fi])
        fword,bword=all_fw[fi],all_bw[bi]
        joined=fword+inverse(bword)
        meeting=float(np.linalg.norm(cumulative_f[fi]-cumulative_b[bi]))
        joined_state=execute(initial,joined)
        joined_error=float(np.linalg.norm(joined_state-target))
        assert abs(meeting-joined_error)<1e-10
        assert np.linalg.norm(cumulative_f[fi].conj().T@cumulative_f[fi]-np.eye(5))<1e-10
        record={'depth_per_side':depth,'maximum_joined_length':2*depth,
                'forward_boundary_count':len(cumulative_f),'backward_boundary_count':len(cumulative_b),
                'minimum_numerical_meeting_Frobenius_error':meeting,
                'best_forward_length':len(fword),'best_backward_length':len(bword),
                'numerical_match_at_requested_tolerance':meeting<float(epsilon)}
        layers.append(record)
        print(json.dumps(record),flush=True)
        best={'forward_controls':fword,'backward_controls':bword,'controls':joined,
              'numerical_frobenius_error':joined_error,
              'numerical_operator_error':float(np.linalg.norm(joined_state-target,ord=2))}
        if meeting<float(epsilon):break
    hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(raw[k]).hexdigest() for k,p in paths.items()}
    own=Path(__file__).resolve();hashes[own.relative_to(ROOT).as_posix()]=hashlib.sha256(own.read_bytes()).hexdigest()
    for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    report={'status':'scout_only','requested_epsilon':str(epsilon),
        'alphabet':'39 source-derived conjugated bank directions, t=+1 or -1; 78 exact phase gates',
        'layers':layers,'known_word_split_control':{'split':split,'total_gates':len(known),
            'meeting_error':float(middle),'full_word_error':float(final),'wrong_inverse_order_error':float(wrong_order)},
        **best,'source_hashes':hashes,
        'scope':'Bounded exhaustive numerical boundary enumeration in a fixed finite vocabulary, with adjacent same-direction shortening. Includes odd lengths via cumulative frontiers. No certified global depth obstruction, complete dense search, or new accepted solution without exact verification.'}
    (BASE/'results/encoder-bidirectional-meeting-scout.json').write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--max-depth',type=int,default=2)
    parser.add_argument('--epsilon',default='1/100')
    args=parser.parse_args();main(args.max_depth,F(args.epsilon))
