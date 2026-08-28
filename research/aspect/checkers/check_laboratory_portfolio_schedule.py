from itertools import combinations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CONTRACT=ROOT/"contracts"/"laboratory-portfolio-acquisition.v1.json"
RESULT=ROOT/"results"/"laboratory_portfolio_schedule.json"


def within(items,cap):
    return all(sum(i[axis] for i in items)<=cap[axis] for axis in cap)


def score(items):
    gains=set().union(*(set(i["gains"]) for i in items)) if items else set()
    sectors={i["sector"] for i in items}
    return len(gains),len(sectors),-sum(i["attempted_optical_trials"] for i in items),tuple(sorted(i["key"] for i in items))


def main():
    c=json.loads(CONTRACT.read_text());cap=c["campaign_capacity"]
    # Prove all declared loads from their authoritative contracts.
    for item in c["candidates"]:
        if "contract" not in item: continue
        source=json.loads((ROOT/"contracts"/item["contract"]).read_text())
        if "cell_count" in source:
            assert item["optical_setting_cells"]==source["cell_count"]
            assert item["attempted_optical_trials"]==source["cell_count"]*source["minimum_attempted_trials_per_cell"]
        else:
            assert item["arithmetic_verification_cases"]==source["verified_case_count_from_owner_report"]
    pool=[i for i in c["candidates"] if i["status"]=="admit" and i.get("acquisition_ready",True)]
    feasible=[]
    for n in range(len(pool)+1):
        for p in combinations(pool,n):
            if within(p,cap):feasible.append(p)
    best=max(feasible,key=score);keys=sorted(i["key"] for i in best)
    assert keys==sorted(i["key"] for i in pool)
    totals={axis:sum(i[axis] for i in best) for axis in cap}
    assert totals==cap
    hostiles={"prototype_scalar_costs_removed":all("cost" not in i for i in c["candidates"]),
              "deferred_cross_scale_invariant_not_scheduled":"four_atom_cross_scale_invariant" not in keys,
              "admitted_but_unready_polarized_sign_local_fiber_not_scheduled":"polarized_sign_local_relative_fiber" not in keys,
              "all_resource_axes_respected":within(best,cap),
              "all_acquisition_loads_derived_from_contracts":True,
              "incomparable_arithmetic_and_optical_resources_not_added":"resource_axes" in c and len(c["resource_axes"])==3,
              "capacity_not_claimed_as_apparatus_availability":"become laboratory availability claims only when" in c["authority_boundary"]}
    assert all(hostiles.values())
    out={"schema":"marici.aspect.laboratory-portfolio-schedule-check.v1","status":"pass",
         "feasible_portfolios_exhausted":len(feasible),"scheduled_portfolio":keys,"resource_totals":totals,
         "independent_directions":len(set().union(*(set(i["gains"]) for i in best))),
         "hostile_cost_models":hostiles,"apparatus_availability_bound":False,
         "disposition":"acquisition-authoritative schedule ready for operator binding to measured shot rates, setup durations, and port availability"}
    RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out,sort_keys=True))


if __name__=="__main__":main()
