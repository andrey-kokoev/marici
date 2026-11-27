"""Conditional semantics test: Boolean observations occur only in terminal continuations."""
from itertools import product
from pathlib import Path
import json

# An address is not a truth value. Requesters, responders, conditions and sensor
# produce continuations. Only a test driver holding the full net may resolve them.
def requester(address):
    return lambda responder: lambda: responder(address)()

def neutral(address):
    return lambda: lambda full: False

def addressed(side, slot):
    return lambda sender: lambda: lambda full: full.permits(side, slot, sender)

def no_response(replies):
    def stage():
        fs=[r() for r in replies]
        return lambda full: not any([f(full) for f in fs])
    return stage

def sensor(red,blue):
    def stage():
        r,b=red(),blue()
        def resolve(full):
            rv,bv=r(full),b(full)
            return rv or bv
        return resolve
    return stage

all_links=list(product(range(3),range(7)));cover=[(j%3,j) for j in range(7)]

def wire(links,role):
    rs=[requester(i) for i in range(3)];bs=[requester(j) for j in range(7)]
    red=no_response([bs[j](role('R',i)) for i,j in links]);blue=no_response([rs[i](role('B',j)) for i,j in links]);return red,blue,sensor(red,blue)

class FullNet:
    def __init__(self,net,permits):self.net=net;self.permits=permits
    def observe(self):return tuple(f()(self) for f in self.net)

def run():
    omitted=sorted(set(all_links)-set(cover));counts=dict(blind_cases=0,distinguished_conditions=0,distinguished_final=0,neutral_controls=0);example={}
    def compare(rule,role=addressed):return [FullNet(wire(L,role),rule).observe() for L in (all_links,cover)]
    # If replies ignore sender and the condition tests presence, multiplicity is immaterial.
    for mask in range(1<<10):
        def blind(side,slot,sender):return bool(mask & (1<<(slot+(3 if side=='B' else 0))))
        a,b=compare(blind);assert a==b;counts['blind_cases']+=1
    for i,j in omitted:
        for side in ('R','B'):
            target=(side,i,j) if side=='R' else (side,j,i)
            # Same retained (0,0) link in the opposite direction in both nets.
            other=('B' if side=='R' else 'R',0,0)
            for active_other in range(2):
                def rule(s,k,t):return (s,k,t)==target or (active_other==1 and (s,k,t)==other)
                a,b=compare(rule);assert a[:2]!=b[:2] and (a[2]!=b[2])==(active_other==1);counts['distinguished_conditions']+=1;counts['distinguished_final']+=int(a[2]!=b[2]);
                n,m=compare(rule,lambda s,k: neutral if (s,k)==target[:2] else addressed(s,k));assert n==m;counts['neutral_controls']+=1
                if not example or (i,j,side)==(1,0,'R'):
                    example[str(active_other)]=dict(all=a,cover=b)
    out=dict(scope='Terminal true reply counted against corresponding absence; synthetic permitted responder functions, not inferred source semantics.',counts=counts,example_B1_to_RorN2=example);dst=Path(__file__).resolve().parents[1]/'results/ramsey_reactive_requests.json';dst.write_text(json.dumps(out,indent=2)+'\n');print(out)
if __name__=='__main__':run()
