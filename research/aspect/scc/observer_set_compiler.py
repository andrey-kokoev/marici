"""First-class graded observer sets for SCC."""
from fractions import Fraction

def F(x):return Fraction(str(x))
def S(x):
    if isinstance(x,Fraction):return x.numerator if x.denominator==1 else f"{x.numerator}/{x.denominator}"
    if isinstance(x,list):return [S(y) for y in x]
    return x
def mm(a,b):return [[sum(F(x)*F(y) for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def rank(a):
    a=[[F(x) for x in row] for row in a];r=0
    for c in range(len(a[0]) if a else 0):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r];q=a[r][c];a[r]=[x/q for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][c]:q=a[i][c];a[i]=[x-q*y for x,y in zip(a[i],a[r])]
        r+=1
    return r
def sym2(t):
    a,b=t[0];c,d=t[1]
    return [[a*a,2*a*b,b*b],[a*c,a*d+b*c,b*d],[c*c,2*c*d,d*d]]
def eq(a,b):return [[F(x) for x in row] for row in a]==[[F(x) for x in row] for row in b]

def compile_observer_set(c):
    errors=[];base=c.get("base_dimension");transport=c.get("base_transport")
    if not isinstance(base,int) or base<1:errors.append("invalid base_dimension")
    if not transport or len(transport)!=base or any(len(r)!=base for r in transport):errors.append("invalid base_transport")
    members=[]
    for m in c.get("members",[]):
        arity=m.get("arity");induced=transport if arity==1 else sym2(transport) if arity==2 and base==2 else None
        if induced is None:members.append({"id":m.get("id"),"status":"unsupported_arity"});continue
        matrix=m.get("matrix",[]);transported=m.get("transported_matrix",[]);expected=mm(matrix,induced)
        width=len(induced);shape_ok=bool(matrix) and all(len(row)==width for row in matrix)
        members.append({"id":m["id"],"tower":m.get("tower","default"),"arity":arity,"domain":m.get("domain"),"shape_ok":shape_ok,"induced_transport":S(induced),"transported_observer":S(expected),"transport_natural":shape_ok and eq(expected,transported),"rank":rank(matrix) if shape_ok else 0,"domain_dimension":width})
    by_arity={}
    for n in sorted({x.get("arity") for x in members if x.get("arity")}):
        matrices=[m["matrix"] for m in c["members"] if m["arity"]==n]
        stacked=[row for matrix in matrices for row in matrix];dim=len(stacked[0]) if stacked else 0
        by_arity[str(n)]={"joint_rank":rank(stacked),"domain_dimension":dim,"joint_kernel_dimension":dim-rank(stacked),"faithful":rank(stacked)==dim}
    by_tower_arity={}
    for tower in sorted({m.get("tower","default") for m in c["members"]}):
        by_tower_arity[tower]={}
        for n in sorted({m["arity"] for m in c["members"] if m.get("tower","default")==tower}):
            matrices=[m["matrix"] for m in c["members"] if m.get("tower","default")==tower and m["arity"]==n];stacked=[row for matrix in matrices for row in matrix];dim=len(stacked[0]) if stacked else 0;rnk=rank(stacked)
            by_tower_arity[tower][str(n)]={"joint_rank":rnk,"domain_dimension":dim,"joint_kernel_dimension":dim-rnk,"faithful":rnk==dim}
    pol=[]
    for p in c.get("polarization",[]):
        M=[[F(x) for x in row] for row in p["gramian"]];x=list(map(F,p["x"]));y=list(map(F,p["y"]));
        q=lambda v:sum(v[i]*M[i][j]*v[j] for i in range(len(v)) for j in range(len(v)))
        mixed=q([u+v for u,v in zip(x,y)])-q(x)-q(y);bilinear=2*sum(x[i]*M[i][j]*y[j] for i in range(len(x)) for j in range(len(y)))
        pol.append({"id":p["id"],"mixed":str(mixed),"twice_bilinear":str(bilinear),"passed":mixed==bilinear})
    comparisons=[]
    required={"named_constructor_actions","observers","viewing_forms","authority","completion_topology","instrument_backaction"}
    for x in c.get("realization_comparisons",[]):
        slots=x.get("slots",{});complete=set(slots)==required;passed=complete and all(slots.values()) and x.get("invertible") is True
        comparisons.append({"id":x["id"],"slot_complete":complete,"verified_equivalent":passed,"first_failed_slot":next((k for k in required if not slots.get(k,False)),None)})
    member_index={m["id"]:m for m in c.get("members",[])};intertower=[]
    for x in c.get("intertower_comparisons",[]):
        source=member_index[x["source_member"]];target=member_index[x["target_member"]];induced=transport if source["arity"]==1 else sym2(transport);expected=mm(source["matrix"],induced)
        intertower.append({"id":x["id"],"arity":source["arity"],"different_towers":source.get("tower")!=target.get("tower"),"passed":source["arity"]==target["arity"] and eq(expected,target["matrix"])})
    pushouts=[]
    for x in c.get("pushout_completion",[]):
        finite=[{"cutoff":row["cutoff"],"minimum_singular_value":str(min(map(F,row["singular_values"]))),"invertible":all(F(v)>0 for v in row["singular_values"])} for row in x["finite_cutoffs"]]
        uniform=F(x["declared_uniform_lower_bound"]);closed=x.get("completion_closed_range") is True and uniform>0
        pushouts.append({"id":x["id"],"finite_exact":all(r["invertible"] for r in finite),"finite_cutoffs":finite,"declared_uniform_lower_bound":str(uniform),"completion_exact":closed,"first_failed_gate":None if closed else "completion_closed_range"})
    higher=[{"degree":x["degree"],"state":x["state"],"admitted":x["state"]=="verified" and bool(x.get("witness"))} for x in c.get("higher_coherence",[])]
    passed=not errors and all(x.get("shape_ok") and x.get("transport_natural") for x in members) and all(x["passed"] for x in pol) and all(x["passed"] for x in intertower) and all(x["state"]!="falsified" for x in higher)
    return {"schema":"marici.scc.observer-set-compilation.v1","observer_set":c.get("id"),"errors":errors,"members":members,"joint_faithfulness_by_arity":by_arity,"joint_faithfulness_by_tower_and_arity":by_tower_arity,"polarization":pol,"intertower_comparisons":intertower,"pushout_completion":pushouts,"realization_comparisons":comparisons,"higher_coherence":higher,"passed":passed,"claim":"finite observer-set coherence passes independently of any failed completion gate"}
