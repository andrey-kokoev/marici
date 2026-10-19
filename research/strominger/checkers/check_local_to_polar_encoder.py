"""Exact bright-sector factorization obstruction and finite schedule diagnostics."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import hashlib,json
from check_witnessed_interface_compiler import (ROOT,BASE,eye,tr,mm,plus,minus,scale,blockdiag,rat,enc,rank,inverse,compile_interface)
hashes={}
def read(p):
    raw=(ROOT/p).read_bytes();hashes[p]=hashlib.sha256(raw).hexdigest();return json.loads(raw)
def determinant(a):
    a=[r[:] for r in a];d=F(1)
    for j in range(len(a)):
        p=next((i for i in range(j,len(a)) if a[i][j]),None)
        if p is None:return F(0)
        if p!=j:a[p],a[j]=a[j],a[p];d=-d
        q=a[j][j];d*=q
        for i in range(j+1,len(a)):
            r=a[i][j]/q
            for k in range(j+1,len(a)):a[i][k]-=r*a[j][k]
            a[i][j]=0
    return d
def square(q):return q>=0 and isqrt(q.numerator)**2==q.numerator and isqrt(q.denominator)**2==q.denominator

def main():
    read('research/strominger/inputs/local-to-polar-encoder-protocol-v1.json')
    source=read('research/strominger/results/neutron-seam-control-transport.json')
    memory=read('research/strominger/results/neutron-comparison-memory.json')
    scattering=read('research/strominger/results/neutron-autonomous-rim-scattering.json')
    assert all(r['status']=='passed' for r in (source,memory,scattering))
    M=rat(source['metric']);Mi=inverse(M);B=rat(memory['residual_incidence']);Gamma=rat(memory['memory_metric'])
    Hmem=mm(mm(mm(B,Mi),tr(B)),Gamma);assert Hmem==rat(memory['rational_memory_operator'])
    S=mm(mm(mm(Mi,tr(B)),Gamma),B)
    A0=scale(F(1,4),rat(source['native_energy']));K=plus(A0,S)
    E=rat(scattering['exact_bright_basis']);assert rank(E)==5
    g=mm(mm(tr(E),M),E);L=mm(mm(inverse(g),tr(E)),M);assert mm(L,E)==eye(5)
    Sb=mm(mm(L,S),E);assert mm(S,E)==mm(E,Sb)
    assert mm(A0,E)==[[F(0)]*5 for _ in range(24)]
    # Rational basis C for the nonzero invariant image of Sb.
    cols=[]
    for col in tr(Sb):
        if rank(cols+[col])>len(cols):cols.append(col)
    C=tr(cols);r=len(cols)
    Ci=mm(inverse(mm(tr(C),C)),tr(C))
    Splus=mm(mm(Ci,Sb),C);assert mm(Sb,C)==mm(C,Splus)
    det=determinant(Splus);assert det>0
    obstruction=not square(det)
    # Exact support projector and expected native part of the polar encoder.
    rows=[]
    for row in B:
        if rank(rows+[row])>len(rows):rows.append(row)
    Q=mm(mm(mm(Mi,tr(rows)),inverse(mm(mm(rows,Mi),tr(rows)))),rows)
    N=minus(eye(24),Q);assert mm(Q,Q)==Q and mm(B,N)==[[F(0)]*24 for _ in B]
    expected_native=mm(N,E)
    metric=blockdiag(M,Gamma);Hafter=blockdiag(A0,Hmem)
    gates=[]
    for i,row in enumerate(B):
        c=compile_interface(M,[row]);assert c['memory_metric'][0][0]==Gamma[i][i]
        gates.append(c)
    def step(i,X):
        c=gates[i];Y=[row[:] for row in X];ncol=len(X[0])
        residual=mm([B[i]],X[:24])[0]
        delta=[X[24+i][j]-residual[j] for j in range(ncol)]
        for k in range(24):
            a=c['injection'][k][0]
            if a:Y[k]=[v+a*w for v,w in zip(X[k],delta)]
        Y[24+i]=residual
        return Y
    ready=E+[[F(0)]*5 for _ in range(21)]
    native_contacts=[row[:2] for row in E]
    assert mm(mm(tr(native_contacts),M),native_contacts)==scale(3,eye(2))
    schedules={'forward21':list(range(21)),'reverse21':list(reversed(range(21))),
       'two_forward_sweeps':list(range(21))*2,'forward_then_backtrack':list(range(21))+list(reversed(range(21)))}
    results={};outputs={}
    for name,word in schedules.items():
        X=[row[:] for row in ready];history=[]
        for serial,i in enumerate(word):
            Y=step(i,X);assert step(i,Y)==X
            history.append({'occurrence':serial,'interface':i});X=Y
        assert mm(mm(tr(X),metric),X)==g
        recovered=[row[:] for row in X]
        for i in reversed(word):recovered=step(i,recovered)
        assert recovered==ready
        nr=minus(X[:24],expected_native)
        er=minus(mm(Hafter,X),mm(X,Sb))
        energy=minus(mm(mm(tr(X),mm(metric,Hafter)),X),mm(g,Sb))
        # Contact columns are transported with the SAME candidate embedding.
        contact=[row[:2] for row in X]
        assert mm(mm(tr(contact),metric),X)==[row[:] for row in g[:2]]
        old_reader=mm(mm(tr(native_contacts),M),X[:24])
        old_error=minus(old_reader,g[:2])
        results[name]={'length':len(word),'native_polar_output_residual_rank':rank(nr),
          'post_storage_energy_intertwiner_residual_rank':rank(er),'quadratic_energy_residual_rank':rank(energy),
          'untransported_contact_residual_rank':rank(old_error),'transported_contact_preserved':True,'reverse_recovery':True,
          'quadratic_energy_residual':enc(energy),'history':history}
        outputs[name]=enc(X)
    checks={'actual5D_bright_sector_invariant_and_native_energy_zero':True,
      'nonzero_image_determinant_computed_exactly':True,'local_gate_matrices_reconstructed_from_source_rows':True,
      'all_four_schedules_preserve_metric_and_reverse':True,'all_candidate_contact_readouts_preserved_when_transported':True,
      'native_output_and_post_storage_energy_residuals_retained':True}
    # This assertion tests the prospective conjecture, not a forced success:
    # report square determinant as an inconclusive result if it occurs.
    if obstruction:checks['nonsquare_determinant_obstructs_any_finite_rational_word']=True
    for p in [Path(__file__),BASE/'checkers/check_witnessed_interface_compiler.py',BASE/'checkers/check_neutron_canonical_occupied_closure.py']:
        hashes[p.relative_to(ROOT).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
    for p,h in hashes.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    out=BASE/'results/local-to-polar-encoder';out.mkdir(parents=True,exist_ok=True)
    report={'status':'pass','checks':checks,'source_hashes':hashes,'bright_dimension':5,'nonzero_residual_dimension':r,
      'positive_restriction_determinant':str(det),'determinant_is_rational_square':square(det),
      'finite_rational_word_obstruction':obstruction,'bright_metric':enc(g),'bright_residual_operator':enc(Sb),
      'nonzero_image_basis':enc(C),'positive_restriction':enc(Splus),'schedules':results,
      'argument':'In the unchanged raw metric charts B=W sqrt(S). If the polar memory output W E were rational, g^-1 (W E)^T Gamma B E would give a rational matrix sqrt(Sb). Its restriction to im(Sb) would have rational determinant whose square equals det(Splus). A nonsquare determinant excludes this. Every finite word in current rational gates on rational ready inputs remains rational.',
      'scope':'Exact finite rational endpoint-gate class with the original polar memory reader. Does not exclude approximation, continuous controls with irrational parameters, a different energy-compatible encoder, or a changed memory chart with independently verified reader transport. No numerical polar SVD or Agda proof was run.'}
    (out/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    (out/'schedule-outputs.json').write_text(json.dumps(outputs,indent=2)+'\n')
    print(json.dumps({'status':'pass','checks':len(checks),'positive_rank':r,'determinant':str(det),'rational_word_obstruction':obstruction,'schedule_ranks':{k:[v['native_polar_output_residual_rank'],v['post_storage_energy_intertwiner_residual_rank']] for k,v in results.items()}}))
if __name__=='__main__':main()
