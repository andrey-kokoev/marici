"""Typed residual coproduct and comparison-square gates for SCC."""
KINDS=("presentation_residual","observer_invisible","pre_descent_anomaly",
       "cutoff_error","substantive_positive")


def fail(gate,reason,**evidence):
    return {"schema":"marici.scc.categorical-residual.v1","passed":False,
            "first_failed_gate":gate,"reason":reason,"evidence":evidence}


def compile_categorical_residual(c):
    r=c.get("residual",{});kind=r.get("kind")
    if kind not in KINDS:return fail("residual_coproduct","unknown residual modality",kind=kind)
    if not r.get("codomain"):return fail("residual_codomain","each modality requires its own codomain")
    if kind=="observer_invisible":
        if not r.get("gauge_in_observer_kernel_witness"):
            return fail("observer_quotient","observer quotient undefined without gauge-kernel inclusion")
        if r.get("literal_zero") and not r.get("presentation_representatives_removed"):
            return fail("zero_promotion","quotient-zero does not imply literal-zero")
    if kind=="pre_descent_anomaly" and r.get("global_descent_verified"):
        return fail("residual_retyping","after global descent use equality of global routes, not anomaly class")
    if kind=="cutoff_error" and not all(k in r for k in ("packet","cutoff","derivative_order","tail_bound")):
        return fail("cutoff_error","cutoff residual lacks quantified axes")
    squares=[]
    for square in c.get("comparison_squares",[]):
        st= square.get("type")
        if st=="completion_observation" and not square.get("tail_residual"):
            return fail("comparison_square","completion-observation square requires tail residual")
        if st=="coherence_positivity" and not any(k in square for k in ("surviving_equality","surviving_inequality","positivity_margin")):
            return fail("comparison_square","coherence-positivity square requires a surviving relation")
        if st not in ("completion_observation","coherence_positivity"):
            return fail("comparison_square","unknown square type",type=st)
        squares.append(square)
    return {"schema":"marici.scc.categorical-residual.v1","passed":True,"first_failed_gate":None,
            "residual":{"summand":kind,"codomain":r["codomain"],"data":r},
            "comparison_squares":squares,"literal_zero_admitted":bool(r.get("literal_zero")),
            "claim_boundary":"typed residual disposition; no automatic conversion between summands"}
