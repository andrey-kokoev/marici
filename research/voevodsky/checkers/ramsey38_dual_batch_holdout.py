"""Time the query pipeline from graph, move script and target rows, not precomputed ends/pools."""
from ramsey38_endpoint_holdout import P as prior,past,old,previous,suffix,freeze,prev,json,sys
from ramsey38_middle_choice_holdout import setup,graph,prepare,extend,face_assignments,shelling,boundary,add
from ramsey38_surface_filler_dual import geometry,make_search,Counter,permutations,median,perf_counter_ns,lru_cache
from ramsey38_release_census import templates
from ramsey38_cone_partial_veto_trial import prior as screened
from itertools import combinations
import gc
P=prev.out/'ramsey38_dual_batch_cases.json';R=prev.out/'ramsey38_dual_batch_times.json'
protocol='First three novel eligible broader middle-choice arrays after 256258 (all requests), no filtering on success. Three balanced methods from decoded graph inputs to 1/2-attachment solutions. Rebuild pools once per distinct query prefix in each batch; rebuild geometry and target sets. Universal labelled-sphere template library warm; exclude sample selection, disk I/O and validation. Forward tests candidate end surface directly, no target-family enumeration.'
class Ends:
    def __init__(self,test):self.test=test
    def __contains__(self,b):return self.test(b)
def run(data,mode):
    geometry.cache_clear();cells,enc,delta,spheres,blocks=geometry();search=make_search(delta,spheres,blocks);ans=[];pool_sizes=[];work=Counter();tri=sorted(sum(1<<i for i in f) for f in combinations(range(7),3));car=lambda s:sum(1<<i for i,t in enumerate(cells) if s&t==s);contact=lambda s:sum(1<<i for i,t in enumerate(tri) if s&t==s)
    for e in data['cases']:
        g=graph(e['word']);u=e['u'];L,rows,ts,dec,stage,_=prepare(g,u);mask=lambda f:sum(1<<L.index(v) for v in f)
        @lru_cache(None)
        def balls(req,bd):return [frozenset(t) for t in face_assignments(L,req,set(map(dec,bd))) if shelling(t)]
        @lru_cache(None)
        def starts(a,b,j,k):
            req,S=stage((a,));r2,T=stage(tuple(sorted((a,b))));A=[t for bd in S[frozenset([j])] for t in balls(req,bd)];Bs={t for bd in T[frozenset([j,k])] for t in balls(r2,bd) if any(extend(s,t) is not None for s in A)};return [(sum(1<<cells.index(mask(c)) for c in t),enc(map(mask,boundary(t)))) for t in sorted(Bs,key=lambda t:sorted(sorted(c) for c in t))]
        for d in e['requests']:
            a,b,c=map(tuple,d['moves']);j,k,l=d['goal'];pool=starts(a,b,j,k);pool_sizes.append(len(pool));h=g;buried=[]
            for x,v in (a,b,c):
                _,rs,_=setup(h,u);buried.append(rs[x]);h=add(h,(x,v))
            _,rs,_=setup(h,u);goal={j,k,l};needs=[contact(s) for r,s in rs.items() if r not in goal and s.bit_count()<4];ban=0
            for s in buried+[rs[r] for r in goal]:ban|=contact(s)
            pred=lambda B:not B&ban and all(B&m for m in needs);ends=Ends(pred) if mode=='forward' else {B for B in spheres if pred(B)};r,n=search((pool,ends,[car(s) for s in set(rs.values())],None),mode);ans.append(sorted(r));work.update(n)
    return ans,pool_sizes,dict(work)
def controls():
    from ramsey38_mesh_equivariance_audit import P as pin
    from ramsey38_append_holdout import P as append
    from ramsey38_preserve_first_ball import faces
    results=[];cells,enc,delta,spheres,blocks=geometry();search=make_search(delta,spheres,blocks)
    for file,record,j,l in [(pin,606,3,18),(append,531,12,11)]:
        e=next(e for e in json.loads(file.read_text())['cases'] if e['record']==record);d=next(d for d in e['requests'] if (d['j'],d['l'])==(j,l));p=d.get('commit') or d['pick'];g=graph(e['word']);L,rs,_=setup(g,e['u']);mask=lambda f:sum(1<<L.index(v) for v in f);dec=lambda s:frozenset(v for i,v in enumerate(L) if s>>i&1);x,v=p['first'];S=rs[x];h=add(g,p['first']);r=setup(h,e['u'])[1];end=setup(add(h,p['second']),e['u'])[1];tips=[p['tip']] if record==606 else [4,18]
        for tip in tips:
            rr=set(r.values())|{S|1<<L.index(tip)};A=[sum(1<<cells.index(mask(t)) for t in ts) for ts in face_assignments(L,set(map(dec,rr)),set(map(dec,p['bd']))) if shelling(ts)];case=([(m,enc(p['bd'])) for m in A],{enc(p['end'])},[sum(1<<i for i,t in enumerate(cells) if t&s==s) for s in set(end.values())],None);sol=[search(case,k)[0] for k in ('forward','back','join')];assert sol[0]==sol[1]==sol[2];n=len({x[0] for x in sol[0]});assert n==({(606,4):3,(531,4):0,(531,18):1}[record,tip]);results.append(dict(record=record,tip=tip,starts=len(A),extendible=n,orders=len(sol[0])))
    return results
def bench():
    data=json.loads(P.read_text());ctrl=controls();templates();gold=None;times=[];nodes={};modes=('forward','back','join')
    for order in permutations(modes):
        rnd={}
        for k in order:
            gc.collect();t=perf_counter_ns();ans,pools,nodes[k]=run(data,k);rnd[k]=(perf_counter_ns()-t)/1e6
            if gold is None:gold=ans
            assert ans==gold and pools==[len(d['pool']) for e in data['cases'] for d in e['requests']]
        times.append(rnd);print(rnd,flush=True)
    med={k:median(r[k] for r in times) for k in modes};print(med,ctrl);prev.save(R,dict(sha=prev.sha(P.read_bytes()),timings_ms=times,median_ms=med,controls=ctrl,requests=len(gold),feasible=sum(bool(a) for a in gold),orders=sum(map(len,gold)),pairs=sum(len({x[:3] for x in a}) for a in gold),nodes=nodes))
if __name__=='__main__':
    if sys.argv[1]=='freeze':freeze(256258,477142,(prior,past,old,previous,suffix,screened),lambda *args:{},P,protocol,lambda es:len(es)==3,require_burial=False)
    elif sys.argv[1]=='bench':bench()
