"""Exact source-constrained affine formula synthesis for SCC."""
from __future__ import annotations
from fractions import Fraction

def F(x): return x if isinstance(x,Fraction) else Fraction(str(x))
def show(x): return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"

def _rref(matrix,nvars):
    a=[list(map(F,row)) for row in matrix];pivot_cols=[];row=0
    for col in range(nvars):
        pivot=next((i for i in range(row,len(a)) if a[i][col]),None)
        if pivot is None:continue
        a[row],a[pivot]=a[pivot],a[row];q=a[row][col];a[row]=[x/q for x in a[row]]
        for i in range(len(a)):
            if i!=row and a[i][col]:
                q=a[i][col];a[i]=[x-q*y for x,y in zip(a[i],a[row])]
        pivot_cols.append(col);row+=1
        if row==len(a):break
    return a,pivot_cols

def synthesize_stage(stage):
    unknowns=stage.get("unknowns",[]);parameters=stage.get("parameters",[]);all_vars=unknowns+parameters
    if stage.get("observer_fitted") is not False:return {"id":stage["id"],"status":"rejected","first_failed_gate":"observer_fitting","formulas":{}}
    if stage.get("authority") not in ("source_authorized","explicit_assumption"):
        return {"id":stage["id"],"status":"rejected","first_failed_gate":"authority","formulas":{}}
    matrix=[]
    for eq in stage.get("equations",[]):
        coeff=eq.get("coefficients",{});matrix.append([F(coeff.get(v,0)) for v in all_vars]+[F(eq.get("rhs",0))])
    rref,pivots=_rref(matrix,len(unknowns)) if matrix else ([],[])
    inconsistent=any(all(x==0 for x in row[:len(all_vars)]) and row[-1]!=0 for row in rref)
    if inconsistent:return {"id":stage["id"],"status":"inconsistent","first_failed_gate":"source_equations","formulas":{}}
    pivot_row={c:i for i,c in enumerate(pivots)};formulas={};underdetermined=[]
    for out in stage.get("outputs",unknowns):
        j=all_vars.index(out)
        if j not in pivot_row:underdetermined.append(out);continue
        row=rref[pivot_row[j]];free_unknown=[unknowns[k] for k in range(len(unknowns)) if k not in pivots and row[k]!=0]
        if free_unknown:underdetermined.append(out);continue
        terms={p:show(-row[len(unknowns)+k]) for k,p in enumerate(parameters) if row[len(unknowns)+k]!=0}
        formulas[out]={"constant":show(row[-1]),"parameter_coefficients":terms,"source_derived":stage["authority"]=="source_authorized"}
    status="derived" if not underdetermined else ("partially_derived" if formulas else "underdetermined")
    return {"id":stage["id"],"status":status,"first_failed_gate":None if status=="derived" else "formula_rank","rank":len(pivots),"unknown_count":len(unknowns),"formulas":formulas,"underdetermined":underdetermined,"free_unknowns":[unknowns[k] for k in range(len(unknowns)) if k not in pivots]}

def synthesize_bridges(contract):
    stages=[synthesize_stage(s) for s in contract.get("stages",[])]
    derived={f"{s['id']}.{name}":formula for s in stages for name,formula in s["formulas"].items()}
    required=contract.get("required_source_outputs",[]);missing=[x for x in required if x not in derived or not derived[x]["source_derived"]]
    return {"schema":"marici.scc.formula-synthesis.v1","contract":contract.get("id"),"stages":stages,"derived_formulas":derived,"required_source_outputs":required,"missing_source_formulas":missing,"bridge_status":"source_derived" if not missing else "underdetermined","certifies_physical_realization":False}
