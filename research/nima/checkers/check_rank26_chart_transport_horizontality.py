#!/usr/bin/env python3
"""Certify the differential coherence of the physical G12 -> G31 chart map.

The quotient transition is parameter dependent.  We reconstruct its first
derivative on each external axis over the finite field, validate the rational
interpolants on held-out points, and test dT + A_target T - T A_source.
"""
from __future__ import annotations
import contextlib,importlib,io,json,os,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
BEN=ROOT/"research"/"benincasa";NCHK=ROOT/"research"/"nima"/"checkers"
sys.path[:0]=[str(BEN),str(NCHK)]
with contextlib.redirect_stdout(io.StringIO()):
    base=importlib.import_module("physical_four_mark_residue_twisted_derham")
    charts=importlib.import_module("g12_g31_residue_chart_transition")
    prior=importlib.import_module("check_rank26_physical_annihilator_chart_transport")
P=base.PRIME
OUT=ROOT/"research"/"nima"/"results"/f"rank26_chart_transport_horizontality_p{P}.json"
base.reduce_row=prior.reduce_complete
HALF=(-pow(2,P-2,P))%P
charts.GAMMA=HALF;charts.AMBIENT=14;charts.CUTOFF=7

def solve_linear(rows,width):
    """Return the unique solution of an augmented linear system, or None."""
    a=[[x%P for x in row] for row in rows];r=0;piv=[]
    for c in range(width):
      k=next((i for i in range(r,len(a)) if a[i][c]),None)
      if k is None:continue
      a[r],a[k]=a[k],a[r];iv=pow(a[r][c],P-2,P);a[r]=[x*iv%P for x in a[r]]
      for i in range(len(a)):
       if i!=r and a[i][c]:
        q=a[i][c];a[i]=[(x-q*y)%P for x,y in zip(a[i],a[r])]
      piv.append(c);r+=1
    if any(not any(row[:width]) and row[width] for row in a):return None
    if len(piv)<width:return None
    out=[0]*width
    for i,c in enumerate(piv):out[c]=a[i][width]
    return out

def rational_fit(samples,heldout,max_total=5):
    """Fit y=N/D with D(0)=1; return derivative and minimal bidegree."""
    if all(y==0 for _,y in samples+heldout):return 0,(0,0)
    for total in range(max_total+1):
      for nd in range(total+1):
       dd=total-nd;width=nd+1+dd
       if len(samples)<width:continue
       rows=[]
       for x,y in samples:
        row=[pow(x,i,P) for i in range(nd+1)]
        row += [(-y*pow(x,j,P))%P for j in range(1,dd+1)]
        row += [y]
        rows.append(row)
       sol=solve_linear(rows,width)
       if sol is None:continue
       num=sol[:nd+1];den=[1]+sol[nd+1:]
       ok=True
       for x,y in heldout:
        nv=sum(c*pow(x,i,P) for i,c in enumerate(num))%P
        dv=sum(c*pow(x,i,P) for i,c in enumerate(den))%P
        if not dv or nv!=y*dv%P:ok=False;break
       if ok:
        a0=num[0];a1=num[1] if len(num)>1 else 0;b1=den[1] if len(den)>1 else 0
        return (a1-a0*b1)%P,(nd,dd)
    return None,None

def transition_at(point,source_free_labels,target_free_labels):
    target_point=(point[0],point[2],point[1])
    source=charts.presentation(base.fiber_data,point,charts.SOURCE_NAMES)
    target=charts.presentation(charts.g31_fiber_data,target_point,charts.TARGET_NAMES)
    sf_current=source["free_low"];tf_current=target["free_low"]
    spos={c:i for i,c in enumerate(sf_current)};tpos={c:i for i,c in enumerate(tf_current)}
    def coordinates(label,pres,pos):
      red=prior.reduce_complete({pres["columns"][label]:1},pres["pivots"])
      return [red.get(c,0) for c in pos]
    # The reducer's pivot chart may jump.  Require instead that the fixed
    # labelled Pluecker coordinates from the center remain a basis.
    Bs=list(map(list,zip(*[coordinates(label,source,sf_current) for label in source_free_labels])))
    Bt=list(map(list,zip(*[coordinates(label,target,tf_current) for label in target_free_labels])))
    try:
      prior.inverse(Bs);Bti=prior.inverse(Bt)
    except StopIteration:return None
    mapped=[]
    for label in source_free_labels:
      red=prior.reduce_complete({target["columns"][charts.map_label(label)]:P-1},target["pivots"])
      mapped.append([red.get(c,0) for c in tf_current])
    M=list(map(list,zip(*mapped)))
    return prior.matmul(Bti,M)

def connection_matrix(pres,fiber,point,names,axis):
    free=pres["free_low"];pos={c:i for i,c in enumerate(free)};n=len(free)
    A=[[0]*n for _ in range(n)]
    for j,c in enumerate(free):
      label=pres["ordered_columns"][c]
      raw=prior.connection_image(label,names,HALF,axis,pres,fiber,point)
      red=prior.reduce_complete(raw,pres["pivots"])
      for tc,v in red.items():
       if tc in pos:A[pos[tc]][j]=v
    return A

def add3(dT,At,T,As):
    AtT=prior.matmul(At,T);TAs=prior.matmul(T,As)
    return [[(dT[i][j]+AtT[i][j]-TAs[i][j])%P for j in range(len(T[0]))] for i in range(len(T))]

def main():
    center=charts.SOURCE_POINT
    source=charts.presentation(base.fiber_data,center,charts.SOURCE_NAMES)
    target_point=(center[0],center[2],center[1])
    target=charts.presentation(charts.g31_fiber_data,target_point,charts.TARGET_NAMES)
    sf=[source["ordered_columns"][c] for c in source["free_low"]]
    tf=[target["ordered_columns"][c] for c in target["free_low"]]
    T0=transition_at(center,sf,tf);assert T0 is not None
    axis_reports=[];all_pass=True
    target_axes=(0,2,1)
    # Start with the smallest useful certified window.  If this fails, widen
    # adaptively in a later run rather than rebuilding 69 presentations.
    train_offsets=[0,1,2,3,4,6,8];held_offsets=[9,10]
    selected_axes=[int(x) for x in os.environ.get("MARICI_AXES","0,1,2").split(",")]
    for axis in selected_axes:
      target_axis=target_axes[axis]
      values=[]
      for h in train_offsets+held_offsets:
       point=list(center);point[axis]=(point[axis]+h)%P
       try:T=transition_at(tuple(point),sf,tf)
       except (KeyError,ValueError,StopIteration):T=None
       if T is not None:values.append((h%P,T))
      train=[x for x in values if (x[0] if x[0]<=P//2 else x[0]-P) in train_offsets]
      held=[x for x in values if (x[0] if x[0]<=P//2 else x[0]-P) in held_offsets]
      accepted={x if x<=P//2 else x-P for x,_ in values}
      rejected=[h for h in train_offsets+held_offsets if h not in accepted]
      dT=[[0]*26 for _ in range(26)];degrees=[];fit_failures=0
      for i in range(26):
       for j in range(26):
        deriv,degree=rational_fit([(x,M[i][j]) for x,M in train],[(x,M[i][j]) for x,M in held])
        if deriv is None:fit_failures+=1
        else:dT[i][j]=deriv;degrees.append(degree)
      As=connection_matrix(source,base.fiber_data,center,charts.SOURCE_NAMES,axis)
      At=connection_matrix(target,charts.g31_fiber_data,target_point,charts.TARGET_NAMES,target_axis)
      theta=add3(dT,At,T0,As);nonzero=sum(x!=0 for row in theta for x in row)
      passed=fit_failures==0 and nonzero==0;all_pass &= passed
      axis_reports.append({"source_axis":axis,"target_axis":target_axis,"usable_training_points":len(train),"usable_heldout_points":len(held),"rejected_offsets":rejected,"fit_failures":fit_failures,"max_numerator_degree":max((d[0] for d in degrees),default=None),"max_denominator_degree":max((d[1] for d in degrees),default=None),"mixed_curvature_nonzero_entries":nonzero,"passed":passed})
      print(json.dumps(axis_reports[-1]),flush=True)
    payload={"schema":"marici.rank26-chart-transport-horizontality.v1","prime":P,"gamma":"-1/2","transition":"G12_to_G31","identity":"dT + A_target T - T A_source = 0","selected_axes":selected_axes,"complete_axis_census":selected_axes==[0,1,2],"axes":axis_reports,"passed":all_pass}
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(payload,indent=2))
    if not all_pass:raise SystemExit(1)
if __name__=="__main__":main()
