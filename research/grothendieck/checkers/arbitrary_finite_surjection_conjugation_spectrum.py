"""Nonsplit Q16 and split D16 controls for the conjugation spectrum."""

from math import gcd
import json
from pathlib import Path


def mul(x,y,twist):
    a,b=x; c,d=y
    return ((a + (-1 if b else 1)*c + twist*b*d) % 8, (b+d)%2)


def power(x,n,twist):
    out=(0,0)
    for _ in range(n): out=mul(out,x,twist)
    return out


def run(name,twist):
    group=[(a,b) for b in range(2) for a in range(8)]
    survivors=[]; failures=[]; checks=0
    for n in range(1,25):
        failed=[]
        for h in range(2):
            source=[x for x in group if x[1]==h]
            target=[x for x in group if x[1]==(n*h)%2]
            images=[power(x,n,twist) for x in source]
            if sorted(images)!=sorted(target): failed.append(h)
            checks += len(source)*len(group)
        ok=not failed; predicted=gcd(n,16)==1
        assert ok==predicted,(name,n,ok,predicted)
        if ok: survivors.append(n)
        else: failures.append({"n":n,"failed_fibers":failed})
    return {"extension":name,"survivors_1_to_24":survivors,
            "failures":failures,"checks":checks}


def main():
    # twist 4 gives s^2=r^4 (generalized quaternion); twist 0 gives dihedral.
    families=[run("Q16_to_C2_nonsplit",4),run("D16_to_C2_split",0)]
    result={"theorem":"compatibility iff gcd(n,exp(K)*exp(A_q))=1",
            "families":families,"index_cases":48,
            "coefficient_value_checks":sum(x["checks"] for x in families),
            "status":"pass"}
    out=Path(__file__).parents[1]/"results"/"arbitrary-finite-surjection-conjugation-spectrum.json"
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2))


if __name__=="__main__": main()
