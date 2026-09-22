"""Identification audit for the actual labelled P_y source, not the gain fixture.

Rechecks saved numerical and finite structural evidence. Does not rerun Arb,
assert an acquired measurement, or manufacture physical tetrahedral witnesses.
"""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import hashlib
import json
import copy

ROOT=Path(__file__).resolve().parents[1]
OTHER=ROOT.parent/'voevodsky'


def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module


t=load_module('transition',ROOT/'certificates/verify_diagonal_transition.py');v=t.v
s=load_module('source_obstruction',OTHER/'certificates/verify_filtered_obstruction.py')


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def identify(problem,certificate,manifest):
    """Decode structural Boolean-corner labels into actual arithmetic endpoints."""
    primes=problem['event_primes'];background=problem['background']
    def endpoint(mask):
        result=background
        for i,p in enumerate(primes):
            if mask&(1<<i):result*=p
        return result
    seams=[[endpoint(a),endpoint(b),'retained' if kind==1 else 'forgotten']
           for tag,a,b,kind in problem['private_seams']]
    v.require(seams==manifest['seams'],'Actual source seam identification fails')
    v.require([endpoint(x) for x in problem['cubic_outer']]==manifest['outer_corner'],'Actual outer corner identification fails')
    witness=certificate['witness']
    prefix=next(p for p in certificate['prefixes'] if p['id']==witness['prefix_id'])
    pairs=prefix['pairs']+[[i for i in range(len(primes)) if not prefix['end']&(1<<i)]]
    kinds=prefix['kinds']+[witness['suffix_kind']]
    v.require(pairs==[[0,1],[2,3],[4,5]] and kinds==[1,0,1],'Source witness is not declared v_y')
    expanded=s.parse_terms(prefix['terms'])
    expanded=s.multiply(expanded,s.relation(tuple(pairs[-1]),kinds[-1]))
    norm=sum(abs(a) for a in expanded.values())
    target=tuple(tuple(e) for e in problem['private_seams'])
    coefficient=s.vacuum_rows(0,63,expanded,3).get(target,F(0))
    v.require(norm==32 and coefficient==1,'Source norm or normalized coefficient mismatch')
    return {'seams':seams,'outer_corner':manifest['outer_corner'],
            'source_pairs':[[primes[i] for i in pair] for pair in pairs],
            'source_kinds':kinds,'expanded_path_terms':len(expanded),
            'path_l1_cost':str(norm),'P_y_of_v_y':str(coefficient)}


def main():
    paths={key:ROOT/'results'/('py-bridge-'+key+'.json') for key in ('problem','certificate','manifest','calibration')}
    sp=OTHER/'results/filtered-obstruction-problem.json'
    sc=OTHER/'results/filtered-obstruction-certificate.json'
    p,cert,manifest,cal=[v.strict_load(paths[key]) for key in ('problem','certificate','manifest','calibration')]
    problem,certificate=s.load(sp),s.load(sc)
    v.verify(p,cert);v.verify_py_manifest(p,manifest)
    structural=s.verify(problem,certificate)
    for key,path in (('calibration',paths['calibration']),('structural_problem',sp),('structural_certificate',sc)):
        v.require(sha(path)==manifest['evidence_sha256'][key],'Referenced evidence bytes changed: '+key)
    v.require(cal['certified_positive_E_y_enclosure']==manifest['calibration'],'Calibration artifact and manifest disagree')
    identification=identify(problem,certificate,manifest)
    v.require(p['rows'][0]['weight']==identification['path_l1_cost'],'Numerical source cost is not the reconstructed path cost')
    # Exact scientific notation avoids expanding hundreds of thousands of digits.
    gained=copy.deepcopy(p)
    for field in ('data','calibration'):
        gained['rows'][0][field]=['2e-240665','2e-240664']
        v.require(all(v.q(new)==2*v.q(old) for old,new in zip(p['rows'][0][field],gained['rows'][0][field])),'Gain is not exactly two')
    gained_cert=copy.deepcopy(cert);gained_cert['problem_sha256']=t.digest(gained)
    v.verify(gained,gained_cert)
    edge={'version':1,'kind':'positive-diagonal-refinement-v1',
          'old_sha256':t.digest(p),'new_sha256':t.digest(gained),
          'source_scale':['1'],'observation_scale':['2'],'target_scale':'1'}
    t.verify_transition(p,gained,edge)
    # Raw center and absolute radius double, while normalized uncertainty does not.
    lo,hi=map(v.q,p['rows'][0]['data']);elo=v.q(p['rows'][0]['calibration'][0])
    a,b=map(v.q,gained['rows'][0]['data']);enew=v.q(gained['rows'][0]['calibration'][0])
    v.require((b-a)/2==2*(hi-lo)/2 and (b-a)/(2*enew)==(hi-lo)/(2*elo),'Error budget failed to transport')
    rejected=0
    for alteration in ('seam','outer'):
        bad=copy.deepcopy(manifest)
        if alteration=='seam':bad['seams'][1][0]=10
        else:bad['outer_corner'][1]=6006
        try:identify(problem,certificate,bad)
        except ValueError:rejected+=1
        else:raise AssertionError('Source misidentification accepted')
    bad=copy.deepcopy(gained);bad['rows'][0]['calibration']=p['rows'][0]['calibration'][:]
    bad_edge=copy.deepcopy(edge);bad_edge['new_sha256']=t.digest(bad)
    try:t.verify_transition(p,bad,bad_edge)
    except ValueError:rejected+=1
    else:raise AssertionError('Reading gain without calibration gain accepted')
    theorem=OTHER/'whole-row-calibration-gains-transport-the-filtered-attachment-but-internal-reweighting-need-not.md'
    report={'audit_passed':True,'actual_source_identification':identification,
        'numerical_status_before':cert['status'],'numerical_status_after':gained_cert['status'],
        'task':'P_y > 1/20','universal_lower_bound':'1/10',
        'raw_gain':'2','source_comparison':'identity','path_budget':'32',
        'conservative_normalized_raw_radius_bound':str((hi-lo)/(2*elo)),
        'structural_reverification':structural,
        'operation_definition':{'selected_family':'the complete saturation of the private raw seed whose normalized coordinate is P_y',
            'new_raw_functional':'lambda_new(x)=2*lambda_old(x) for every source x and every admitted context',
            'other_seed_families':'unchanged','lower_observer':'unchanged',
            'not_inferred_from':'agreement on the selected witness or the 270 cubic columns'},
        'identification_ledger':[
            {'link':'actual source labels, private coefficient and numerical line prior','status':'machine-checked'},
            {'link':'numerical raw gain, normalized task and raw-error transport','status':'machine-checked'},
            {'link':'finite source obstruction on the original packet','status':'machine-checked conditional on owning hypotheses'},
            {'link':'whole-source gain identity','status':'definition of the admitted coordinate operation, not a detector-redesign inference'},
            {'link':'actual saturated kernels, flags and filtered pushout under this operation','status':'owning theorem applies conditionally; not instantiated as a physical matrix certificate'},
            {'link':'chosen face witnesses and tetrahedral fillers for the four actual towers','status':'not supplied or identified'}],
        'next_missing_artifact':{'required':'source-compatible presentation of the actual saturated evaluation and its retained source lift',
            'must_bind':['source actions and evaluation maps','inherited ideal filtration',
                         'chosen nullhomotopy/source lift','six typed comparisons and four face witnesses'],
            'must_not_substitute':'the five-dimensional dual-number fixture or its artificially truncated chain complex'},
        'external_assumptions':manifest['external_assumptions'],
        'calibration_reintegrated':False,'physical_measurement_performed':False,
        'full_four_tower_identification_verified':False,'corruptions_rejected':rejected,
        'evidence_sha256':{**manifest['evidence_sha256'],'gain_transport_theorem_text':sha(theorem)}}
    for name,obj in [('actual-py-gain-problem',gained),('actual-py-gain-certificate',gained_cert),
                     ('actual-py-gain-transition',edge),('actual-py-gain-identification-audit',report)]:
        (ROOT/'results'/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
