"""Search for a small permutation-invariant support rule separating the four excluded cones."""
import json
from pathlib import Path

census=json.loads(Path("research/flavor/results/orbit_census.json").read_text())
excluded={1,3,8,12}


def slots(mask):
    return [(i,j) for i in range(3) for j in range(3) if mask & (1<<(3*i+j))]


def sector_features(mask,prefix):
    ss=slots(mask)
    rd=sorted([sum(i==r for i,j in ss) for r in range(3)])
    cd=sorted([sum(j==c for i,j in ss) for c in range(3)])
    forced=sum(1 for i in range(3) for k in range(i+1,3)
               if not ({j for r,j in ss if r==i}&{j for r,j in ss if r==k}))
    return {f"{prefix}_row_{k}":v for k,v in enumerate(rd)} | {
            f"{prefix}_col_{k}":v for k,v in enumerate(cd)} | {
            f"{prefix}_forced_gram_zeros":forced}


rows=[]
for o in census["orbits"]:
    su,sd=set(slots(o["mask_u"])),set(slots(o["mask_d"]))
    f={"cycle_length":o["cycle_length"],"sector_overlap":len(su&sd)}
    f.update(sector_features(o["mask_u"],"u"))
    f.update(sector_features(o["mask_d"],"d"))
    rows.append((o["orbit_index"],f,int(o["orbit_index"] in excluded)))

names=sorted(rows[0][1])
X=[[f[n] for n in names] for _,f,_ in rows]
y=[v for _,_,v in rows]

def solve(indices,depth):
    labels={y[i] for i in indices}
    if len(labels)==1:
        return {"leaf":labels.pop()}
    if depth==0:
        return None
    for j,name in enumerate(names):
        vals=sorted({X[i][j] for i in indices})
        for threshold in vals[:-1]:
            left=[i for i in indices if X[i][j]<=threshold]
            right=[i for i in indices if X[i][j]>threshold]
            if not left or not right:
                continue
            lt,rt=solve(left,depth-1),solve(right,depth-1)
            if lt is not None and rt is not None:
                return {"feature":name,"le":threshold,"left":lt,"right":rt}
    return None

def predict(tree,row):
    if "leaf" in tree:
        return tree["leaf"]
    branch="left" if row[names.index(tree["feature"])]<=tree["le"] else "right"
    return predict(tree[branch],row)

model=None
for depth in range(1,6):
    model=solve(list(range(len(y))),depth)
    if model is not None:
        break

out={"schema":"marici.flavor.support_combinatorial_discriminator.v1",
     "exact_low_depth_rule_found":model is not None,
     "features":names,
     "rows":[{"orbit":i,"excluded":bool(v),**f} for i,f,v in rows]}
if model is not None:
    out["minimum_tested_depth"]=depth
    out["rule"]=model
    # Leave-one-out stability: refit at same depth, demand held-out correctness.
    loo=[]
    loo_rows=[]
    for k in range(len(y)):
        m=solve([i for i in range(len(y)) if i!=k],depth)
        ok=m is not None and predict(m,X[k])==y[k]
        loo.append(ok)
        loo_rows.append({"held_out_orbit":rows[k][0],"correct":ok,
                         "prediction":None if m is None else bool(predict(m,X[k]))})
    out["leave_one_out_correct"]=sum(loo)
    out["leave_one_out_total"]=len(loo)
    out["leave_one_out_failures"]=[r for r in loo_rows if not r["correct"]]
Path("research/flavor/results/wp10_support_combinatorial_discriminator.json").write_text(
    json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in out.items() if k!="rows" and k!="features"},indent=2))
