"""Exact flux-ground spinorial decomposition and observable selection boundary."""
from fractions import Fraction as F
import argparse
import json

from check_dressed_flux_projectors import audit as dressed_audit,Field
from check_five_cell_attachment_bridge import A,ZERO,ONE,mm,adj,rank,add,scale,decode,eye,record,load,digest,ROOT,BASE

DEST=BASE/'results/flux-ground-doublets.v1.json'


def trace(M):return sum((M[i][i] for i in range(len(M))),ZERO)
def zeros(n,m=None):return tuple(tuple(ZERO for _ in range(n if m is None else m)) for _ in range(n))


def audit():
    previous=dressed_audit();v=F(previous['field']['v']);f=Field(v)
    K=tuple(tuple(decode(x) for x in row) for row in load('research/strominger/results/common-endpoint-charging.json')['source_operators']['electron']['kinetic_operator'])
    Q=add(eye(4),scale(A(-1),K));plus=scale(A(F(1,2)),add(eye(4),Q));minus=add(eye(4),scale(A(-1),plus))
    assert mm(plus,minus)==zeros(4) and rank(plus)==rank(minus)==2
    rows=[];inner=[[ZERO,ZERO],[ZERO,ZERO]];commutant_norm=ZERO
    r=(ZERO,ONE);norm=f.add(f.one,f.mul(r,r));invnorm=f.inverse(norm)
    Fground=[list(row) for row in f.zeros(16,4)]
    for i in range(4):
        for j in range(4):Fground[4*i+j][i]=f.add((Q[j][i],ZERO),r if i==j else f.zero)
    Fground=tuple(tuple(row) for row in Fground)
    assert f.mm(f.adj(Fground),Fground)==f.scale(norm,f.matrix(eye(4)))
    for item in previous['joint_source_symmetry']['native_actions']:
        T=tuple(tuple(decode(x) for x in row) for row in item['line_transport'])
        perm=item['lead_permutation']
        assert mm(T,plus)==mm(plus,T) and mm(T,minus)==mm(minus,T)
        # T*g_i=t_i*g_pi(i). Keeping the distinct lead label produces the
        # same numerical T on ground labels, not the matter action alone.
        Joint=tuple(tuple(T[i%4][j%4] if i//4==perm[j//4] else ZERO for j in range(16)) for i in range(16))
        assert f.mm(f.matrix(Joint),Fground)==f.mm(Fground,f.matrix(T))
        chars=[trace(mm(T,P)) for P in (plus,minus)]
        assert chars[0]==A(2*F(item['quaternion'][0]))
        for i in range(2):
            for j in range(2):inner[i][j]+=chars[i].flip(8)*chars[j]/24
        full=trace(T);commutant_norm+=full.flip(8)*full/24
        rows.append({'quaternion':item['quaternion'],'lead_permutation':perm,
                     'plus_character':chars[0].record(),'minus_character':chars[1].record()})
    assert inner==[[ONE,ZERO],[ZERO,ONE]] and commutant_norm==A(2)
    # Finite-group character orthogonality implies two inequivalent irreducible
    # doublets, each once. Their commutant is span{I,Q}.
    minus_one=next(row for row in rows if row['quaternion']==['-1','0','0','0'])
    assert minus_one['plus_character']==minus_one['minus_character']==A(-2).record()
    lead_checks=[]
    for i in range(4):
        E=tuple(tuple(ONE if a==b==i else ZERO for b in range(4)) for a in range(4))
        comm=add(mm(E,plus),scale(A(-1),mm(plus,E)))
        assert rank(comm)==2
        branch=mm(minus,mm(E,plus));assert rank(branch)==1
        assert trace(mm(adj(branch),branch))==A(F(1,4))
        lead_checks.append({'lead':i,'projector_commutator_rank':2,'plus_to_minus_branch_rank':1,
                            'branch_Hilbert_Schmidt_squared':'1/4'})
    # Native Q acting only on matter, identity on lead labels, is a different
    # operator from Q on the four-dimensional ground label coordinates.
    matterQ=tuple(tuple(Q[i%4][j%4] if i//4==j//4 else ZERO for j in range(16)) for i in range(16))
    projection=lambda Y:f.scale(invnorm,f.mm(f.adj(Fground),Y))
    compressed=projection(f.mm(f.matrix(matterQ),Fground))
    c=f.mul((A(2),ZERO),f.mul(r,invnorm))
    assert compressed==f.scale(c,f.matrix(eye(4)))
    out=f.mm(f.matrix(matterQ),Fground)
    predicted=f.mm(Fground,compressed)
    leakage=f.madd(out,f.scale((-ONE,ZERO),predicted))
    assert f.rank(leakage)==4
    leak_fraction=f.add(f.one,f.neg(f.mul(c,c)))
    assert leak_fraction==(A(v*v/(v*v+4)),ZERO)
    assert f.scale(invnorm,f.mm(f.adj(leakage),leakage))==f.scale(leak_fraction,f.matrix(eye(4)))
    # Scalar assigned charge and degenerate ground energy cannot select one
    # summand. All fixed-label diagonal readers together destroy the split.
    assert all(plus[i][j]!=ZERO for i in range(4) for j in range(4))
    dependencies=set(previous['source_sha256'])|{'research/scattering/seed-composition/check_flux_ground_doublets.py'}
    return {
        'schema':'marici.scattering.flux-ground-doublets.v1',
        'status':'joint_ground_has_two_inequivalent_spinorial_doublets_but_charge_energy_and_matter_return_do_not_select_one',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'ground_representation':{'ground_coordinates':4,'full_matter_lead_coordinates':16,
                                  'intertwiner':'ground column i has (r*e_i+Qe_i) in lead block i',
                                  'ground_metric':'(r^2+1)*I4; normalized by one common scalar',
                                  'native_action_on_ground_labels':'same numerical T as line representation; lead is permuted jointly',
                                  'character_rows':rows},
        'decomposition':{'projector_plus':record(plus),'projector_minus':record(minus),
                          'ranks':[2,2],'character_inner_product_matrix':[['1','0'],['0','1']],
                          'commutant_dimension':2,'commutant':'span{I,Q_label}',
                          'inequivalent_irreducible_doublets':True,'plus_is_native_fundamental_character':True,
                          'central_minus_one_on_each':'-I2','spinorial_means':'binary-tetrahedral central action, not physical spin/statistics admission'},
        'observable_gate':{'assigned_charge_on_ground':'q*I4','ground_energy':'E_ground*I4',
                            'charge_or_ground_energy_selects_doublet':False,
                            'fixed_lead_readouts':lead_checks,
                            'lead_measurement_preserves_doublet':False,
                            'any_matrix_commuting_with_all_lead_readers_and_all_symmetries':'scalar I only',
                            'Q_label_requires_cross_lead_coherence':True},
        'native_matter_return':{'operator':'I_lead tensor Q_matter, not Q_label',
                                'compression_to_ground':'c*I4, c=2*r/(r^2+1)=2/sqrt(v^2+4)',
                                'native_P_compression':'(1+c)*I4/2',
                                'leakage_rank':4,'normalized_Q_leakage_squared':'v^2/(v^2+4)',
                                'normalized_fixture_leakage_squared':str(v*v/(v*v+4)),
                                'matter_return_selects_global_doublet':False},
        'selection_scope':{'symmetry_projectors_are_exactly_available_mathematically':True,
                           'symmetry_projectors_forced_to_one_choice':False,
                           'symmetry_transports_are_hamiltonian_flux_transfer':False,
                           'physical_spin_or_species_selected':False},
        'boundary':{'all_rank_two_joint_sectors_absent':False,'physical_preparation_or_charge_conjugation_derived':False,
                    'lead_records_erased':False,'formal_outcome_admitted':False},
        'next_gate':'Compare the cross-lead symmetry projectors with the owning endpoint/lead dynamics: test whether any admitted operator transfers lead flux coherently while preserving Gauss constraints and the dressed ground sector, or record the missing interaction and retained field-history requirements.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale flux-ground doublet receipt')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: exact character orthogonality decomposes the rank-four joint ground into two inequivalent spinorial doublets.')
    print('PASS: lead readers mix them; charge/energy are scalar and native matter return compresses to a scalar with leakage.')
    print('Boundary: cross-lead coherent sector selection remains a new operation, not physical spin preparation.')


if __name__=='__main__':main()
