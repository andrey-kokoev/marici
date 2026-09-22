"""Independent exact verifier. Standard library only; imports no project code.

Checks the finite source obstruction, conditional on the explicitly listed
owning analytical/module hypotheses. Does not run the certificate producer.
"""
from fractions import Fraction
from itertools import combinations,permutations,product
from collections import defaultdict
import hashlib,json,sys

def require(ok,message):
    if not ok:raise ValueError(message)
def fields(obj,keys):require(isinstance(obj,dict) and set(obj)==set(keys),'unexpected fields')
def integer(x):require(type(x) is int,'expected integer');return x
def rational(x):
    require(type(x) is str,'coefficients must be rational strings')
    return Fraction(x)
def no_duplicates(items):
    d={}
    for k,v in items:
        require(k not in d,'duplicate JSON key');d[k]=v
    return d
def load(path):
    with open(path,encoding='utf-8') as stream:
        return json.load(stream,object_pairs_hook=no_duplicates,
            parse_float=lambda _:(_ for _ in ()).throw(ValueError('JSON floats forbidden')))
def digest(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def clean(d):return {k:v for k,v in d.items() if v}
def relation(pair,kind):
    a,b=pair;out={}
    for marks in (((0,0),) if kind==0 else ((1,0),(0,1))):
        out[((a,b),marks)]=Fraction(1);out[((b,a),marks)]=Fraction(-1)
    return out
def multiply(a,b):
    out=defaultdict(Fraction)
    for (w,m),c in a.items():
        for (v,n),d in b.items():out[w+v,m+n]+=c*d
    return clean(out)
def parse_terms(items):
    require(isinstance(items,list),'terms must be a list');out={}
    for term in items:
        fields(term,('word','marks','coefficient'))
        w=tuple(integer(x) for x in term['word']);m=tuple(integer(x) for x in term['marks'])
        require(len(w)==len(m) and len(set(w))==len(w),'invalid path')
        require(all(0<=x<6 for x in w) and all(x in (0,1) for x in m),'invalid label')
        key=(w,m);require(key not in out,'duplicate path term')
        c=rational(term['coefficient']);require(c!=0,'zero source term');out[key]=c
    return out
# Independently evaluate noncommutative potential words, not seam derivatives.
def record(start,w,m):
    state=start;out={():Fraction(1)}
    for event,keep in zip(w,m):
        require(not state&(1<<event),'event repeated from initial state')
        end=state|(1<<event)
        if keep:
            nxt=defaultdict(Fraction)
            for word,c in out.items():
                nxt[word+(end,)]+=c
                if state:nxt[word+(state,)]-=c
            out=clean(nxt)
        state=end
    return out
def rank(columns):
    basis={}
    for col in columns:
        v=dict(col)
        while v:
            p=min(v)
            if p not in basis:
                c=v[p];basis[p]={k:a/c for k,a in v.items()};break
            c=v[p]
            for k,a in basis[p].items():v[k]=v.get(k,Fraction(0))-c*a
            v=clean(v)
    return len(basis)
def rho_column(start,col):
    out=defaultdict(Fraction)
    for (w,m),c in col.items():
        for key,a in record(start,w,m).items():out[key]+=c*a
    return clean(out)
# Full ordered-cut vacuum projection. All non-cut marks must be forgotten;
# a homogeneous positive-degree potential word cannot contribute to vacuum.
def vacuum_rows(start,end,col,order):
    out=defaultdict(Fraction)
    for (w,m),c in col.items():
        states=[start]
        for e in w:
            require(not states[-1]&(1<<e),'invalid typed word')
            states.append(states[-1]|(1<<e))
        require(states[-1]==end,'outer endpoint mismatch')
        for cuts in combinations(range(len(w)),order):
            if any(keep and j not in cuts for j,keep in enumerate(m)):continue
            key=tuple(('e',states[j],states[j+1],m[j]) for j in cuts)
            out[key]+=c
    return clean(out)
def pairings(items):
    # Enumerate permutations and deduplicate pair orders; independent of the
    # producer's recursive choice-of-subset routine.
    return sorted({tuple(tuple(sorted(p[j:j+2])) for j in range(0,len(p),2)) for p in permutations(items)})
def expected_problem():
    return {'schema':'marici.filtered-cubic-obstruction.problem.v1',
     'background':2,'event_primes':[2,3,5,7,11,13],
     'source_record':'ordered vertex-potential differences; root potential zero',
     'old_outer':[0,15],'cubic_outer':[0,63],
     'old_seams':[[['e',0,1,1],['e',3,7,0]],[['e',1,3,1],['e',3,7,0]]],
     'private_seams':[['e',0,1,1],['e',3,7,0],['e',15,31,1]],
     'buffers':'vacuum','stage_two':'unchanged original saturated observer',
     'filtrations':{'B':['B','B','B','0'],'A':['A','A','B','0'],
       'G':['G','G','0','0'],'K':['K','N','L','0']},
     'definitions':{'M':'I E','N':'ker(pi) intersect M','L':'I^2 E',
       'f':'source evaluation restricted to G3','level_two_graph_signs':['1','-1']},
     'external_hypotheses':['old gap d2 is nonzero','private response factor Ey is positive',
       'surjective compatible source-bimodule evaluations','levelwise strict filtered category']}
def validate_tree(value):
    if type(value) in (str,int):return
    if type(value) is list:
        for x in value:validate_tree(x)
        return
    if type(value) is dict:
        require(all(type(k) is str for k in value),'non-string JSON key')
        for x in value.values():validate_tree(x)
        return
    raise ValueError('only strings, integer labels, lists and objects are admitted')
def verify(problem,cert):
    validate_tree(problem);validate_tree(cert)
    # Freeze the mathematical protocol; a digest alone would not do this.
    require(problem==expected_problem(),'unsupported or altered protocol')
    fields(cert,('schema','problem_sha256','local_kernels','prefixes','N_prefix_ids','witness'))
    require(cert['schema']=='marici.filtered-cubic-obstruction.certificate.v1','wrong certificate schema')
    require(cert['problem_sha256']==digest(problem),'problem digest mismatch')
    expected_local={(start,pair) for pair in combinations(range(6),2) for start in range(64)
                    if not any(start&(1<<e) for e in pair)}
    seen=set()
    for entry in cert['local_kernels']:
        fields(entry,('start','pair','record_rank','relations'))
        start=integer(entry['start']);pair=tuple(integer(x) for x in entry['pair']);key=(start,pair)
        require(key in expected_local and key not in seen,'missing/duplicate local corner');seen.add(key)
        paths=[(w,m) for w in permutations(pair) for m in product((0,1),repeat=2)]
        r=rank([record(start,*p) for p in paths])
        require(integer(entry['record_rank'])==r==6,'local recorder rank')
        require(len(entry['relations'])==2,'local relation count')
        for kind,terms in enumerate(entry['relations']):
            col=parse_terms(terms)
            require(col==relation(pair,kind),'wrong local relation vector')
            require(not rho_column(start,col),'relation not in recorder kernel')
        # Disjoint feature degrees give independence; rank 6 then proves they
        # span the entire two-event kernel, including the absence of a q=2 relation.
        require(rank([relation(pair,0),relation(pair,1)])==2,'dependent local relations')
    require(seen==expected_local,'local spanning audit incomplete')
    # There are no zero/one-event ideal elements: corner record maps inject.
    for start in range(64):
        require(rank([record(start,(),())])==1,'vertex kernel')
        for e in range(6):
            if not start&(1<<e):require(rank([record(start,(e,),(k,)) for k in (0,1)])==2,'one-event kernel')
    expected_prefix={(sum(1<<e for e in subset),pairs,kinds)
       for subset in combinations(range(6),4) for pairs in pairings(subset)
       for kinds in product((0,1),repeat=2)}
    seen=set();ids={};supports=defaultdict(set);actual_N=set();top=[];actions=0
    oldrows=[tuple(tuple(e) for e in row) for row in problem['old_seams']]
    target=tuple(tuple(e) for e in problem['private_seams'])
    for entry in cert['prefixes']:
        fields(entry,('id','end','pairs','kinds','terms','old_coefficients','right_action_values'))
        ident=integer(entry['id']);end=integer(entry['end'])
        pairs=tuple(tuple(integer(e) for e in pair) for pair in entry['pairs'])
        kinds=tuple(integer(k) for k in entry['kinds']);key=(end,pairs,kinds)
        require(key in expected_prefix and key not in seen,'prefix family incomplete/duplicated');seen.add(key)
        require(ident not in ids,'duplicate prefix id')
        col=parse_terms(entry['terms'])
        expected=multiply(relation(pairs[0],kinds[0]),relation(pairs[1],kinds[1]))
        require(col==expected,'wrong expanded prefix')
        require(not supports[end].intersection(col),'prefix generators not independent')
        supports[end].update(col)
        old=vacuum_rows(0,end,col,2) if end==15 else {}
        ov=[old.get(row,Fraction(0)) for row in oldrows]
        require(list(map(rational,entry['old_coefficients']))==ov,'old prefix values')
        require(ov[0]==ov[1],'old gap does not reduce to common prefix coefficient')
        if ov==[0,0]:actual_N.add(ident)
        rest=tuple(e for e in range(6) if not end&(1<<e))
        require(len(entry['right_action_values'])==2,'right action count')
        vals=[]
        for suffix_kind in (0,1):
            full=multiply(col,relation(rest,suffix_kind))
            im=vacuum_rows(0,63,full,3);val=im.get(target,Fraction(0));vals.append(val)
            require(rational(entry['right_action_values'][suffix_kind])==val,'right action value')
            require(val==ov[0]*suffix_kind,'private coordinate factorization fails')
            if ident in actual_N:require(val==0,'private row does not annihilate N-prefix action')
            allpairs=pairs+(rest,);allkinds=kinds+(suffix_kind,)
            if sum(allkinds)==2:
                state=0;pivot=[]
                for pair,keep in zip(allpairs,allkinds):
                    pivot.append(('e',state,state|(1<<min(pair)),keep))
                    state|=sum(1<<e for e in pair)
                top.append((tuple(pivot),im))
            actions+=1
        ids[ident]=(key,ov,vals)
    require(seen==expected_prefix and set(ids)==set(range(360)),'prefix spanning audit incomplete')
    ni=[integer(x) for x in cert['N_prefix_ids']]
    require(len(ni)==len(set(ni)) and set(ni)==actual_N and len(ni)==359,'incorrect N-prefix basis')
    require(len(top)==270 and len({p for p,im in top})==270,'private family size')
    for j,(pivot,im) in enumerate(top):
        require(all(im.get(p,0)==int(j==k) for k,(p,_) in enumerate(top)),'private matrix not identity')
    fields(cert['witness'],('prefix_id','suffix_kind','private_value'))
    witness=cert['witness'];ident=integer(witness['prefix_id'])
    require(ident in ids,'unknown witness')
    key,ov,vals=ids[ident]
    require(key==(15,((0,1),(2,3)),(1,0)),'wrong witness source')
    require(integer(witness['suffix_kind'])==1 and rational(witness['private_value'])==vals[1]==1,'witness not detected')
    return {'verified':True,'local_two_event_kernels':len(expected_local),
      'complete_prefix_generators':360,'complete_right_actions':actions,
      'N_prefix_generators':359,'private_matrix_size':270,
      'finite_obstruction':'P_y(N I)=0 and P_y(f(v_y))=1',
      'boundary':'Physical response nonvanishing, compatible observer evaluation, and the exact filtered-derived implication remain the explicitly declared owning hypotheses.'}
def main():
    if len(sys.argv)!=3:raise ValueError('usage: verify_filtered_obstruction.py PROBLEM.json CERTIFICATE.json')
    print(json.dumps(verify(load(sys.argv[1]),load(sys.argv[2])),indent=2))
if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,TypeError,ZeroDivisionError) as exc:
        print('REJECTED: '+str(exc),file=sys.stderr);sys.exit(1)
