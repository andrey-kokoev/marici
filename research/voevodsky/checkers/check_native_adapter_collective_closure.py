"""Exact 48-coordinate embedding and minimal invariant-subspace audit.
Belt L/G/N are read from the native coefficient store, not replaced by toy edges.
Carrier coordinates are local geometric port characters, not full spinor states.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json

BASE=Path(__file__).resolve().parents[1]

class F:
    """Exact real quadratic field Q(sqrt(151))."""
    __slots__=('a','b')
    def __init__(self,a=0,b=0):self.a=Q(a);self.b=Q(b)
    @staticmethod
    def cast(x):return x if isinstance(x,F) else F(x)
    def __bool__(self):return bool(self.a or self.b)
    def __add__(self,o):
        o=F.cast(o);return F(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return F(-self.a,-self.b)
    def __sub__(self,o):return self+-F.cast(o)
    def __rsub__(self,o):return F.cast(o)+-self
    def __mul__(self,o):
        o=F.cast(o)
        if not self or not o:return F()
        return F(self.a*o.a+151*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inverse(self):
        denominator=self.a*self.a-151*self.b*self.b
        if not denominator:raise ZeroDivisionError
        return F(self.a/denominator,-self.b/denominator)
    def __truediv__(self,o):return self*F.cast(o).inverse()
    def __eq__(self,o):
        o=F.cast(o);return self.a==o.a and self.b==o.b
    def positive(self):
        if not self:return False
        if self.a>=0 and self.b>=0:return True
        if self.a<=0 and self.b<=0:return False
        return self.a*self.a>151*self.b*self.b if self.a>0 else 151*self.b*self.b>self.a*self.a
    def encoded(self):return [str(self.a),str(self.b)]


def cmul(x,y):return (x[0]*y[0]-3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def cdiv(x,y):
    n=y[0]*y[0]+3*y[1]*y[1]
    a,b=cmul(x,(y[0],-y[1]));return a/n,b/n

def apply(A,v):
    return [sum((a*v[j] for j,a in row.items() if v[j]),F()) for row in A]
def inner(x,y,metric):return sum((a*g*b for a,b,g in zip(x,y,metric) if a and b),F())
def unit(n,i):return [F(int(i==j)) for j in range(n)]
def indicator(n,indices):
    indices=set(indices);return [F(int(j in indices)) for j in range(n)]
def same(a,b):return all(x==y for x,y in zip(a,b))

class Span:
    def __init__(self,n):self.n=n;self.rows=[];self.pivots=[];self.certificates=[]
    def reduce(self,v):
        v=list(v);coefficients=[]
        for row,pivot in zip(self.rows,self.pivots):
            coefficient=v[pivot];coefficients.append(coefficient)
            if coefficient:
                v=[a-coefficient*b if b else a for a,b in zip(v,row)]
        return v,coefficients
    def add(self,v,origin):
        residual,coefficients=self.reduce(v)
        pivot=next((i for i,x in enumerate(residual) if x),None)
        if pivot is None:return False
        normalizer=residual[pivot];inverse=normalizer.inverse()
        self.rows.append([x*inverse for x in residual]);self.pivots.append(pivot)
        self.certificates.append({'origin':origin,'normalizer':normalizer.encoded(),
            'subtractions':[{'basis':i,'coefficient':x.encoded()} for i,x in enumerate(coefficients) if x]})
        return True


def closure(seeds,operators,n):
    span=Span(n)
    for i,v in enumerate(seeds):span.add(v,{'seed':i})
    cursor=0
    while cursor<len(span.rows):
        for name,A in operators.items():span.add(apply(A,span.rows[cursor]),{'operator':name,'parent':cursor})
        cursor+=1
    assert all(not any(span.reduce(v)[0]) for v in seeds)
    assert all(not any(span.reduce(apply(A,v))[0]) for A in operators.values() for v in span.rows)
    return span


def orthogonalize(rows,metric):
    output=[];norms=[]
    for row in rows:
        v=list(row)
        for w,h in zip(output,norms):
            q=inner(w,v,metric)/h
            if q:v=[a-q*b for a,b in zip(v,w)]
        h=inner(v,v,metric);assert h.positive()
        output.append(v);norms.append(h)
    assert all(inner(a,b,metric)==(norms[i] if i==j else 0) for i,a in enumerate(output) for j,b in enumerate(output))
    return output,norms


def restricted(A,basis,metric,norms):
    images=[apply(A,v) for v in basis]
    out=[[inner(v,w,metric)/norms[i] for w in images] for i,v in enumerate(basis)]
    for j,image in enumerate(images):
        reconstructed=[sum((out[i][j]*basis[i][k] for i in range(len(basis))),F()) for k in range(len(metric))]
        assert same(reconstructed,image)
    return out


def main():
    store_path=BASE/'results/belt_three_by_twelve_store.json';ambient_path=BASE/'results/coupled_six_piece_belt_store.json';adapter_path=BASE/'results/native_rim_phase_adapter.json'
    store=json.loads(store_path.read_text(encoding='utf-8'));ambient=json.loads(ambient_path.read_text(encoding='utf-8'));adapter=json.loads(adapter_path.read_text(encoding='utf-8'))
    assert adapter['verification_passed']
    for name,digest in adapter['source_hashes'].items():assert sha256((BASE/name).read_bytes()).hexdigest()==digest
    assert store['source_root']==ambient['root']==adapter['source_packet_root']
    record=ambient['record'];assert sha256(json.dumps(record,sort_keys=True,separators=(',',':')).encode()).hexdigest()==ambient['root']
    coordinates=store['coordinates'];assert len(coordinates)==36
    d=[Q(c['d']) for c in coordinates];z=[]
    for c in coordinates:
        a,b,r,s=map(Q,c['selected_numerator']);assert b==s==0
        assert a or r;z.append((a,r))
    # x_i is the unnormalized native plane coordinate; w_i=z_i/d_i is its
    # selected native value. y_i=x_i/w_i retains that phase in the gauge record.
    w=[(a/di,b/di) for (a,b),di in zip(z,d)]
    metric=[F((a*a+3*b*b)/di) for (a,b),di in zip(z,d)]
    metric += [F(v) for _ in range(6) for v in (Q(6),Q(2,3))]
    n=48;operators={s:[{} for _ in range(n)] for s in ('L','G','N')}
    for arrow in store['arrows']:
        i,j=arrow['target'],arrow['source'];a,b,c,e=map(Q,arrow['numerator']);assert b==e==0
        # Gauge conjugation of the actual stored operator, not a new projector.
        value=cdiv(cmul((a,c),z[j]),(z[i][0]*d[j],z[i][1]*d[j]))
        assert value[1]==0
        assert j not in operators[arrow['stage']][i]
        operators[arrow['stage']][i][j]=F(value[0])
    for A in operators.values():
        for i in range(36,48):A[i][i]=F(1)
    total=sum(metric[:36],F());sector=sum(metric[:12],F())
    assert total==3*sector
    checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    check('all_native_arrows_gauge_conjugated',sum(len(row) for A in operators.values() for row in A[:36])==1836)
    check('native_L_matches_sector_projector',all(operators['L'][i].get(j,F())==(metric[j]/sector if i//12==j//12 else F()) for i in range(36) for j in range(36)))
    check('native_G_matches_sector_average',all(operators['G'][i].get(j,F())==F(Q(1,3) if i%12==j%12 else 0) for i in range(36) for j in range(36)))
    check('native_N_matches_collective_projector',all(operators['N'][i].get(j,F())==metric[j]/total for i in range(36) for j in range(36)))
    # Six initial rim triangles; all other native belt coordinates remain present.
    indices={(c['triangle'],c['axis']):i for i,c in enumerate(coordinates)}
    triangles={tuple(t):i for i,t in enumerate(record['triangles'])}
    ports=[]
    for prefix in ('L','U'):
        for k in range(3):
            a=prefix+str(k);b=prefix+str((k+1)%3)
            triangle=next(t for t in triangles if t[1:]==(a,b))
            tri=triangles[triangle];slots=[indices[tri,axis] for axis in (0,1)]
            assert w[slots[0]]==(Q(0),Q(1)) and w[slots[1]]==(Q(1),Q(0))
            assert metric[slots[0]]==6 and metric[slots[1]]==Q(148,675)
            ports.append({'rim':prefix,'edge':[a,b],'triangle':tri,'belt_slots':slots,'carrier_slots':[36+2*len(ports),37+2*len(ports)]})
    local=[]
    for row in adapter['adapter_matrix']:
        values=[]
        for raw in row:
            a,b,c,e=map(Q,raw);assert c==e==0;values.append(F(a,b))
        local.append(values)
    U=[{i:F(1)} for i in range(n)]
    for p in ports:
        slots=p['carrier_slots']+p['belt_slots']
        for i,slot in enumerate(slots):U[slot]={slots[j]:x for j,x in enumerate(local[i]) if x}
    operators={'U':U,**operators}
    rim_slots={i for p in ports for i in p['belt_slots']};untouched=set(range(36))-rim_slots
    check('all_24_nonrim_belt_coordinates_retained',len(untouched)==24 and all(U[i]=={i:F(1)} for i in untouched))
    check('full_metric_positive',all(g.positive() for g in metric))
    check('all_embedded_generators_metric_self_adjoint',all(metric[i]*A[i].get(j,F())==metric[j]*A[j].get(i,F()) for A in operators.values() for i in range(n) for j in range(n)))
    units=[unit(n,i) for i in range(n)]
    check('full_48_coordinate_adapter_involution',all(same(apply(U,apply(U,v)),v) for v in units))
    check('native_projectors_and_GL_N_survive_embedding',all(same(apply(A,apply(A,v)),apply(A,v)) for key,A in operators.items() if key!='U' for v in units) and all(same(apply(operators['G'],apply(operators['L'],v)),apply(operators['N'],v)) and same(apply(operators['L'],apply(operators['G'],v)),apply(operators['N'],v)) for v in units))
    check('co_moving_native_matrices_C3_covariant',all(A[(i+12)%36].get((j+12)%36,F())==A[i].get(j,F()) for key,A in operators.items() if key!='U' for i in range(36) for j in range(36)))
    visible_seeds=[indicator(n,range(36)),indicator(n,range(36,42)),indicator(n,range(42,48))]
    small=closure(visible_seeds,operators,n)
    local_seed_slots=sorted(rim_slots|set(range(36,48)))
    broad=closure([unit(n,i) for i in local_seed_slots],operators,n)
    # Use geometry-defined disjoint collective coordinates, rather than a
    # complicated generator-dependent Gram-Schmidt basis. No modes are removed.
    natural_names=['nonrim_belt_collective'];natural_groups=[sorted(untouched)]
    for side in ('belt','carrier'):
        for rim in ('L','U'):
            for axis,axis_name in enumerate(('edge','transverse')):
                natural_names.append(side+'_'+rim+'_'+axis_name)
                natural_groups.append([p[side+'_slots'][axis] for p in ports if p['rim']==rim])
    natural=[indicator(n,slots) for slots in natural_groups]
    natural_norms=[inner(v,v,metric) for v in natural]
    simple=Span(n)
    for i,v in enumerate(visible_seeds+natural):simple.add(v,{'geometric_seed':i})
    check('nine_geometric_collectives_equal_generated_closure',len(small.rows)==len(simple.rows)==9 and all(not any(small.reduce(v)[0]) for v in natural) and all(not any(simple.reduce(v)[0]) for v in small.rows))
    check('arbitrary_local_inputs_generate_27_dimensions',len(broad.rows)==27)
    broad_geometric=Span(n)
    for i in local_seed_slots:broad_geometric.add(unit(n,i),{'local_slot':i})
    for sector_index in range(3):
        broad_geometric.add(indicator(n,[i for i in untouched if i//12==sector_index]),{'nonrim_sector':sector_index})
    check('broad_closure_is_local_ports_plus_three_nonrim_collectives',len(broad_geometric.rows)==27 and all(not any(broad.reduce(v)[0]) for v in broad_geometric.rows) and all(not any(broad_geometric.reduce(v)[0]) for v in broad.rows))
    check('generic_nonrim_input_is_not_silently_covered_by_reduction',any(broad.reduce(unit(n,min(untouched)))[0]))
    basis,norms=orthogonalize(simple.rows,metric)
    reduced={name:restricted(A,basis,metric,norms) for name,A in operators.items()}
    natural_reduced={name:restricted(A,natural,metric,natural_norms) for name,A in operators.items()}
    check('collective_G_is_identity_and_L_equals_N',all(reduced['G'][i][j]==int(i==j) for i in range(9) for j in range(9)) and all(reduced['L'][i][j]==reduced['N'][i][j] for i in range(9) for j in range(9)))
    visible=Span(n)
    for i,v in enumerate(visible_seeds):visible.add(v,{'seed':i})
    check('three_proposed_collectives_do_not_close',any(any(visible.reduce(apply(U,v))[0]) for v in visible_seeds))
    check('all_independent_port_inputs_require_nonrim_modes',len(broad.rows)>len(local_seed_slots))
    check('collective_closure_is_contained_in_broad_closure',all(not any(broad.reduce(v)[0]) for v in small.rows))
    # Orthogonalization starts with precisely the three disjoint visible seeds.
    leakage=Span(len(basis)-3)
    for j in range(3):leakage.add([reduced['U'][i][j] for i in range(3,len(basis))],{'visible_column':j})
    check('one_extra_hidden_state_is_insufficient',len(small.rows)>4 and len(leakage.rows)>1)
    # Compare the restricted metric-adjoint identities with the full embedding.
    check('restricted_generators_metric_self_adjoint',all(norms[i]*A[i][j]==norms[j]*A[j][i] for A in reduced.values() for i in range(len(basis)) for j in range(len(basis))))
    # Each generated basis has an exact certificate: elimination of previous
    # vectors from either a seed or a generator image. Replay it independently.
    def replay(span,seeds):
        rows=[]
        for expected,certificate in zip(span.rows,span.certificates):
            origin=certificate['origin']
            v=list(seeds[origin['seed']]) if 'seed' in origin else apply(operators[origin['operator']],rows[origin['parent']])
            for entry in certificate['subtractions']:
                coefficient=F(*entry['coefficient']);v=[a-coefficient*b for a,b in zip(v,rows[entry['basis']])]
            inv=F(*certificate['normalizer']).inverse();v=[a*inv for a in v]
            assert same(v,expected);rows.append(v)
        return True
    check('both_minimal_closure_generation_certificates_replay',replay(small,visible_seeds) and replay(broad,[unit(n,i) for i in local_seed_slots]))
    check('all_48_coordinates_remain_in_model',len(metric)==48 and len(U)==48)
    # No empirical probability enters any closure calculation.
    result={'verification_passed':all(checks.values()),'checks':checks,'scalar_field':'Q(sqrt(151)); complex-linear extension implicit',
        'gauge':'x_i = (selected_numerator_i/d_i) y_i; native phase retained in gauge, not erased',
        'belt_gauge':[{'triangle':c['triangle'],'axis':c['axis'],'real':str(wi[0]),'i_sqrt3':str(wi[1])} for c,wi in zip(coordinates,w)],
        'full_dimension':n,'native_belt_dimension':36,'carrier_port_dimension':12,'ports':ports,
        'visible_seed_names':['native_belt_return','proton_ABC_port_character','electron_current_ABC_port_character'],
        'visible_dimension':3,'collective_minimal_closure_dimension':len(small.rows),'hidden_complement_dimension':len(small.rows)-3,
        'one_step_adapter_leakage_rank':len(leakage.rows),'independent_local_input_dimension':len(local_seed_slots),
        'independent_local_input_closure_dimension':len(broad.rows),
        'metric':[v.encoded() for v in metric],'collective_orthogonal_basis':[[v.encoded() for v in row] for row in basis],
        'collective_gram_diagonal':[v.encoded() for v in norms],
        'geometric_collective_names':natural_names,'geometric_collective_supports':natural_groups,
        'geometric_collective_gram_diagonal':[v.encoded() for v in natural_norms],
        'geometric_restricted_generators':{name:[[v.encoded() for v in row] for row in A] for name,A in natural_reduced.items()},
        'collective_restricted_generators':{name:[[v.encoded() for v in row] for row in A] for name,A in reduced.items()},
        'collective_generation_certificate':small.certificates,'broad_generation_certificate':broad.certificates,
        'scope':['Exact smallest invariant space for the named seeds and embedded U,L,G,N only.',
            'Native projectors act as identity on appended carrier ports; no full proton or electron operator is supplied by that extension.',
            'Co-moving charts use the iteration-2 schedule; no new clock or fixed electron port is assumed.',
            'All untouched modes remain in the full model; invariance is not a deletion of provenance.',
            'No Hamiltonian coupling strengths, physical energy law, full spinor coupling or scattering probabilities derived.'],
        'source_hashes':{str(p.relative_to(BASE)).replace('\\','/'):sha256(p.read_bytes()).hexdigest() for p in (store_path,ambient_path,adapter_path,Path(__file__))}}
    output=BASE/'results/native_adapter_collective_closure.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('verification_passed','checks','full_dimension','visible_dimension','collective_minimal_closure_dimension','hidden_complement_dimension','one_step_adapter_leakage_rank','independent_local_input_dimension','independent_local_input_closure_dimension')},indent=2))

if __name__=='__main__':main()
