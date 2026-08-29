"""Exact runtime semantics for recursive globular SCC observer towers."""
from __future__ import annotations
from fractions import Fraction

TERMINAL_KINDS={"zero_residual","contraction","closed_equivalence","well_founded_decrease"}
RESIDUAL_KINDS={"kernel","cokernel","topological","authority"}
GLOBAL_LENSES={"completion","authority","coefficients","parent_child"}

def F(x): return Fraction(str(x))
def rank(matrix):
    a=[[F(x) for x in row] for row in matrix]
    if not a:return 0
    width=len(a[0])
    if any(len(row)!=width for row in a):raise ValueError("ragged matrix")
    r=0
    for col in range(width):
        pivot=next((i for i in range(r,len(a)) if a[i][col]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r];p=a[r][col];a[r]=[x/p for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][col]:q=a[i][col];a[i]=[x-q*y for x,y in zip(a[i],a[r])]
        r+=1
    return r
def mm(left,right):
    if not left or not right:return []
    if len(left[0])!=len(right):raise ValueError("noncomposable matrices")
    return [[sum(F(x)*F(y) for x,y in zip(row,col)) for col in zip(*right)] for row in left]
def mpow(matrix,power):
    size=len(matrix);out=[[int(i==j) for j in range(size)] for i in range(size)]
    for _ in range(power):out=mm(out,matrix)
    return out
def fail(gate,reason,**evidence):return {"passed":False,"first_failed_gate":gate,"reason":reason,"evidence":evidence}

def levels(c):
    cells=c.get("cells",[]);index={x.get("id"):x for x in cells}
    if len(index)!=len(cells) or None in index:return fail("globular_typing","cell identifiers must be present and unique")
    for cell in cells:
        level=cell.get("level")
        if not isinstance(level,int) or level<0:return fail("globular_typing","invalid coherence level",cell=cell.get("id"))
        for field in ("domain","codomain","arity"):
            if field not in cell:return fail("globular_typing","incomplete signature",cell=cell["id"],missing=field)
        if level==0:
            if cell.get("source_boundary") is not None or cell.get("target_boundary") is not None:return fail("globular_typing","level-zero cell has higher boundaries",cell=cell["id"])
            continue
        source=index.get(cell.get("source_boundary"));target=index.get(cell.get("target_boundary"))
        if source is None or target is None:return fail("globular_boundary","higher cell lacks two constructed boundaries",cell=cell["id"])
        if source["level"]!=level-1 or target["level"]!=level-1:return fail("globular_boundary","boundaries are not immediately lower",cell=cell["id"])
        if source.get("parallel_signature")!=target.get("parallel_signature"):return fail("globular_parallelism","boundaries are not parallel",cell=cell["id"])
        if level>1 and (source.get("source_boundary"),source.get("target_boundary"))!=(target.get("source_boundary"),target.get("target_boundary")):return fail("globular_parallelism","higher boundaries do not share lower boundary",cell=cell["id"])
    return {"passed":True,"levels":sorted({x["level"] for x in cells}),"cell_count":len(cells)}

def incidence(c):
    packet=c.get("source_incidence",{});directions=packet.get("declared_directions",[]);matrix=packet.get("matrix",[])
    try:
        base_rank=rank(matrix);effective=matrix;action=c.get("source_action_observability");action_rank=None
        if action:
            J=action.get("observer",[]);A=action.get("action",[]);powers=action.get("powers",[]);labels=action.get("diagonal_labels",[])
            if action.get("source_authorized") is True and J and powers:
                if A:
                    effective=[row for power in powers for row in mm(J,mpow(A,power))];action_rank=rank(effective)
                elif labels and action.get("distinct_labels_source_derived") is True and len(set(labels))==len(labels) and powers==list(range(len(labels))) and len(J)==1 and len(J[0])==len(labels) and all(F(x)!=0 for x in J[0]):
                    action_rank=len(labels);effective=[[int(i==j) for j in range(len(labels))] for i in range(len(labels))]
        ranks=[rank(effective)];current=effective
        for stage in c.get("rank_shadow",[]):current=mm(stage["matrix"],current);ranks.append(rank(current))
    except (KeyError,TypeError,ValueError) as exc:return fail("finite_source_incidence_realization",str(exc))
    if not directions or not matrix or len(matrix[0])!=len(directions):return fail("finite_source_incidence_realization","incidence columns must realize every declared direction")
    required=packet.get("required_rank",len(directions));action_required=action.get("required_rank",required) if action else required
    if base_rank<required:return fail("finite_source_incidence_realization","static source incidence rank is deficient",rank=base_rank,required_rank=required,directions=len(directions))
    if action and action_rank is not None and action_rank<action_required:return fail("action_observability","authorized action stack is rank deficient",rank=action_rank,required_rank=action_required)
    if any(b>a for a,b in zip(ranks,ranks[1:])):return fail("rank_monotonicity","higher observer increased lower incidence rank",ranks=ranks)
    return {"passed":True,"base_rank":base_rank,"authorized_action_stack_rank":action_rank,"ranks":ranks,"directions":len(directions)}

def residuals(c):
    ids=set()
    for residual in c.get("residuals",[]):
        rid=residual.get("id")
        if not rid or rid in ids or residual.get("kind") not in RESIDUAL_KINDS:return fail("typed_residual","invalid residual identity or kind",residual=rid)
        ids.add(rid);seed=residual.get("seed_map",{});expected="inclusion" if residual["kind"]=="kernel" else "projection" if residual["kind"]=="cokernel" else "typed_map"
        if seed.get("kind")!=expected or not seed.get("source") or not seed.get("target"):return fail("typed_residual","wrong seed variance or signature",residual=rid,expected=expected)
    return {"passed":True,"ids":sorted(ids),"count":len(ids)}

def children(c,res):
    ids=set()
    for child in c.get("child_towers",[]):
        cid=child.get("id")
        if not cid or cid in ids or child.get("parent")!=c.get("id"):return fail("boxed_child_tower","child lacks unique identity or explicit parent",child=cid)
        ids.add(cid)
        if child.get("seed_residual") not in res["ids"] or child.get("boxed") is not True:return fail("boxed_child_tower","child lacks typed boxed seed",child=cid)
    return {"passed":True,"ids":sorted(ids),"count":len(ids)}

def promotions(c,ch):
    required={"source_authorized","signature_compatible","incidence_independent","support_preserving","coherent_with_existing_cells"}
    for p in c.get("promotions",[]):
        if p.get("child") not in ch["ids"]:return fail("promotion_authority","promotion names absent child",promotion=p.get("id"))
        cert=p.get("certificates",{})
        if set(cert)!=required or not all(cert.values()):return fail("promotion_authority","incomplete promotion certificate",promotion=p.get("id"),missing=sorted(k for k in required if not cert.get(k)))
    return {"passed":True,"count":len(c.get("promotions",[]))}

def termination(c,ch):
    witnesses={x.get("child"):x for x in c.get("termination",[])}
    for child in ch["ids"]:
        w=witnesses.get(child)
        if not w or w.get("kind") not in TERMINAL_KINDS:return fail("termination","missing admitted termination witness",child=child)
        kind=w["kind"]
        if kind=="zero_residual" and w.get("residual")!=0:return fail("termination","nonzero zero-residual witness",child=child)
        if kind=="contraction" and not w.get("source_authorized_contraction"):return fail("termination","unauthorized contraction",child=child)
        if kind=="closed_equivalence" and not w.get("source_authorized_equivalence"):return fail("termination","unauthorized closed equivalence",child=child)
        if kind=="well_founded_decrease" and (not w.get("measure") or not w.get("after",0)<w.get("before",0)):return fail("termination","measure does not strictly decrease",child=child)
    return {"passed":True,"count":len(ch["ids"])}

def completion(c):
    x=c.get("completion",{});cells=x.get("incompatibility_cells",[])
    triad=next((z for z in cells if z.get("id")=="separation-continuity-margin"),None)
    if not triad or triad.get("log_crowded_sequence") is not True or triad.get("all_three_admitted") is not False or set(triad.get("properties",[]))!={"source_separation","observer_norm_continuity","uniform_lower_margin"}:
        return fail("completion_incompatibility","separation-continuity-margin incompatibility cell is absent or violated")
    branch=next((z for z in x.get("constructor_branches",[]) if z.get("id")=="fourier-bohr-invariant-mean"),None)
    missing_incidence={"prime_power","endpoint","archimedean","green_determinant"}
    rigging=branch.get("rigging",{}) if branch else {}
    if not branch or branch.get("branch")!="discrete_valuation_port" or branch.get("source_authorized") is not True or branch.get("kernel")!="Kronecker_character" or branch.get("frequency_norm_continuous") is not False or str(branch.get("lower_frame_bound"))!="1" or not missing_incidence.issubset(set(branch.get("does_not_supply",[]))) or not all(rigging.get(k) for k in ("dense_test_algebra","coefficient_hilbert_completion","boundary_dual")) or rigging.get("bounded_port_evaluation") is not False or rigging.get("constructor_multiplication_l2_closed") is not False:
        return fail("constructor_branch_typing","Fourier-Bohr invariant mean is mistyped or overpromoted")
    strict=x.get("strictness",{})
    if not(strict.get("closed_complemented_range") and strict.get("continuous_generalized_inverse") and strict.get("uniform_over_completion")):return fail("completion_strictness","range, generalized inverse, or completion-uniform margin is not strict")
    defect=x.get("supported_finite_defect",{})
    if not defect.get("finite") or defect.get("support") not in {"seam","right","left","none"} or not defect.get("fourier_character"):return fail("supported_finite_defect","defect lacks finite support or Fourier character")
    acyclic=x.get("acyclicity",{})
    if not(acyclic.get("source_authorized") and acyclic.get("contracting_homotopy")):return fail("acyclicity","no source-authorized contracting homotopy")
    return {"passed":True,"stages":["strictness","supported_finite_defect","acyclicity"]}

def confluence(c):
    rewrites={x.get("id"):x for x in c.get("rewrites",[])}
    if None in rewrites or len(rewrites)!=len(c.get("rewrites",[])):return fail("rewrite_confluence","rewrites need unique identities")
    for pair in c.get("critical_pairs",[]):
        if pair.get("left") not in rewrites or pair.get("right") not in rewrites:return fail("rewrite_confluence","critical pair names absent rewrite",pair=pair.get("id"))
        if not pair.get("join_witness") or not pair.get("higher_coherence_witness"):return fail("rewrite_confluence","critical pair lacks coherent join",pair=pair.get("id"))
    return {"passed":True,"critical_pair_count":len(c.get("critical_pairs",[]))}

def global_coherence(c):
    cells={x.get("lens"):x for x in c.get("global_coherence",[])};missing=sorted(GLOBAL_LENSES-set(cells));invalid=sorted(k for k,v in cells.items() if k in GLOBAL_LENSES and not(v.get("witness") and v.get("source_authorized")))
    if missing or invalid:return fail("global_coherence","global lens coherence incomplete",missing=missing,invalid=invalid)
    return {"passed":True,"lenses":sorted(GLOBAL_LENSES)}

def compile_globular_tower(c):
    gates=[]
    for name,fn in (("globular_typing",levels),("finite_source_incidence_realization",incidence),("typed_residual",residuals)):
        result=fn(c);gates.append({"gate":name,**result})
        if not result["passed"]:return {"schema":"marici.scc.globular-tower-compilation.v1","tower":c.get("id"),"gates":gates,**result}
    res=gates[-1];ch=children(c,res)
    stages=[("boxed_child_tower",lambda:ch),("promotion_authority",lambda:promotions(c,ch)),("termination",lambda:termination(c,ch)),("completion",lambda:completion(c)),("rewrite_confluence",lambda:confluence(c)),("global_coherence",lambda:global_coherence(c))]
    for name,build in stages:
        result=build()
        gates.append({"gate":name,**result})
        if not result["passed"]:return {"schema":"marici.scc.globular-tower-compilation.v1","tower":c.get("id"),"gates":gates,**result}
    return {"schema":"marici.scc.globular-tower-compilation.v1","tower":c.get("id"),"gates":gates,"passed":True,"first_failed_gate":None,"claim":"globular recursive observer semantics compiled"}
