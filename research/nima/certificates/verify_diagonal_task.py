"""Independent certificate verifier. Does not import or execute the solver."""
from fractions import Fraction
import hashlib
import json
import sys


def require(condition,message):
    if not condition:raise ValueError(message)


def fields(value,required,optional=()):
    require(type(value) is dict,'Expected object')
    require(set(required)<=set(value)<=set(required)|set(optional),'Missing or unknown fields')


def array(value,length=None):
    require(type(value) is list,'Expected array')
    if length is not None:require(len(value)==length,'Wrong array length')


def strict_load(path):
    def pairs(items):
        out={}
        for key,value in items:
            require(key not in out,'Duplicate JSON key')
            out[key]=value
        return out
    def reject(value):raise ValueError('Floating-point or nonfinite JSON number forbidden')
    with open(path,encoding='utf-8') as stream:
        return json.load(stream,object_pairs_hook=pairs,parse_float=reject,parse_constant=reject)


def validate_shape(problem,certificate):
    fields(problem,('model','rows','budget','target'),('metadata',))
    array(problem['rows'])
    for row in problem['rows']:
        fields(row,('data','calibration','weight'))
        array(row['data'],2);array(row['calibration'],2)
    fields(problem['target'],('coefficients','threshold'));array(problem['target']['coefficients'])
    if 'metadata' in problem:
        m=problem['metadata'];fields(m,(),('coordinate_roles','last_row','auxiliary_row_4'))
        for key,value in m.items():
            if key=='coordinate_roles':
                array(value,len(problem['rows']));require(all(type(x) is str for x in value),'Bad coordinate labels')
            else:require(type(value) is str,'Bad annotation')
    fields(certificate,('version','problem_sha256','status'),
           ('witness_semantics','witness','dual','minimum_cost_lower_bound','true_witness','false_witness'))
    extra={
        'UNRESOLVED':set(), 'INFEASIBLE':{'minimum_cost_lower_bound'},
        'TARGET_TRUE':{'witness','dual'},'TARGET_FALSE':{'witness','dual'},
        'AMBIGUOUS':{'true_witness','false_witness'}}
    require(type(certificate['status']) is str and certificate['status'] in extra,'Unknown status')
    expected={'version','problem_sha256','status'}|extra[certificate['status']]
    if certificate['version']==2:expected.add('witness_semantics')
    require(set(certificate)==expected,'Unexpected evidence fields')
    if 'dual' in certificate:fields(certificate['dual'],('lambda','bound'))
    for key in ('witness','true_witness','false_witness'):
        if key not in certificate:continue
        value=certificate[key]
        if type(value) is dict:
            fields(value,('kind','numerators'));array(value['numerators'])
        else:array(value)


def q(x):
    require(isinstance(x,str),'Non-string rational')
    return Fraction(x)


def verify(problem,certificate):
    validate_shape(problem,certificate)
    require(problem['model']=='positive-diagonal-real-l1-v1','Wrong model')
    require(type(certificate['version']) is int and certificate['version'] in (1,2),'Wrong version')
    if certificate['version']==2:
        require(certificate.get('witness_semantics')=='for-every-calibration-there-exists-source','Wrong witness quantifier')
    checksum=hashlib.sha256(json.dumps(problem,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    require(certificate['problem_sha256']==checksum,'Problem digest mismatch')
    rows=problem['rows'];require(1<=len(rows)<=64,'Invalid dimension')
    parsed=[];boxes=[]
    for row in rows:
        l,u=map(q,row['data']);e,f=map(q,row['calibration']);w=q(row['weight'])
        require(l<=u and 0<e<=f and w>0,'Invalid observation row')
        parsed.append((l,u,e,f,w))
        candidates=[l/e,l/f,u/e,u/f];boxes.append((min(candidates),max(candidates)))
    B=q(problem['budget']);coefs=list(map(q,problem['target']['coefficients']))
    threshold=q(problem['target']['threshold'])
    require(B>=0 and len(coefs)==len(rows),'Invalid budget/target')

    def witness(encoded):
        if isinstance(encoded,dict):
            require(certificate['version']==2,'Parametric witness requires version 2')
            require(encoded.get('kind')=='inverse-calibration','Unsupported witness formula')
            values=list(map(q,encoded['numerators']))
            require(len(values)==len(rows),'Wrong parametric witness dimension')
            cost=Fraction(0);low=Fraction(0);high=Fraction(0)
            for value,(l,u,e,f,w),a in zip(values,parsed,coefs):
                require(l<=value<=u,'Parametric prediction outside data')
                cost+=w*abs(value)/e
                ends=(a*value/e,a*value/f)
                low+=min(ends);high+=max(ends)
            require(cost<=B,'Parametric worst-case budget exceeded')
            return low,high
        require(certificate['version']==1,'Version 2 requires an explicit witness formula')
        require(len(encoded)==len(rows),'Wrong witness dimension')
        x=list(map(q,encoded));cost=Fraction(0)
        for value,(l,u,e,f,w) in zip(x,parsed):
            require(l<=e*value<=u and l<=f*value<=u,'Witness fails calibrated data')
            cost+=w*abs(value)
        require(cost<=B,'Witness exceeds budget')
        value=sum(a*v for a,v in zip(coefs,x))
        return value,value

    status=certificate['status']
    if status=='UNRESOLVED':return True # no substantive conclusion is asserted
    if status=='INFEASIBLE':
        cost=Fraction(0)
        for (lo,hi),row in zip(boxes,parsed):
            m=Fraction(0) if lo<=0<=hi else min(abs(lo),abs(hi))
            cost+=row[4]*m
        require(cost==q(certificate['minimum_cost_lower_bound']) and cost>B,'Invalid cost contradiction')
    elif status in ('TARGET_TRUE','TARGET_FALSE'):
        witness(certificate['witness']) # prevents vacuous task certification
        lam=q(certificate['dual']['lambda']);require(lam>=0,'Negative dual multiplier')
        value=-lam*B
        for (lo,hi),row,a in zip(boxes,parsed,coefs):
            if status=='TARGET_FALSE':a=-a
            candidates=[lo,hi]
            if lo<=0<=hi:candidates.append(Fraction(0))
            value+=min(a*x+lam*row[4]*abs(x) for x in candidates)
        require(value==q(certificate['dual']['bound']),'Incorrect dual value')
        require(value>threshold if status=='TARGET_TRUE' else value>=-threshold,'Target inequality not proved')
    elif status=='AMBIGUOUS':
        require(witness(certificate['false_witness'])[1]<=threshold,'False witness does not contradict strict target uniformly')
        require(witness(certificate['true_witness'])[0]>threshold,'True witness does not satisfy target uniformly')
    else:raise ValueError('Unknown status')
    return True


def verify_py_manifest(problem,manifest):
    fields(manifest,('version','protocol','problem_sha256','source_class','outer_corner','seams',
                     'normalized_coordinate','raw_coordinate','equation','calibration',
                     'spectral_point','receiver_gamma','forcing_beta','external_assumptions','evidence_sha256'))
    require(type(manifest['version']) is int and manifest['version']==1,'Wrong manifest version')
    require(manifest['protocol']=='cubic-P_y-raw-residual-v1','Unsupported bridge protocol')
    checksum=hashlib.sha256(json.dumps(problem,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    require(manifest['problem_sha256']==checksum,'Manifest problem mismatch')
    require(manifest['source_class']=='real line spanned by mixed(2,3) forgotten(5,7) mixed(11,13)','Wrong source class')
    array(manifest['outer_corner'],2)
    require(all(type(x) is int for x in manifest['outer_corner']) and manifest['outer_corner']==[2,60060],'Wrong endpoints')
    array(manifest['seams'],3)
    for row,expected in zip(manifest['seams'],[[2,4,'retained'],[12,60,'forgotten'],[420,4620,'retained']]):
        array(row,3);require(type(row[0]) is int and type(row[1]) is int and row==expected,'Wrong typed seam')
    require(manifest['normalized_coordinate']=='P_y' and manifest['raw_coordinate']=='z_y','Wrong coordinate labels')
    require(manifest['equation']=='z_y=E_y*P_y','Wrong normalization equation')
    require((manifest['spectral_point'],manifest['receiver_gamma'],manifest['forcing_beta'])==('3i','2','4'),'Wrong analytical parameters')
    require(len(problem['rows'])==1 and problem['rows'][0]['weight']=='32','Wrong source cost model')
    require(problem['target']['coefficients']==['1'],'Target is not P_y')
    array(manifest['calibration'],2)
    require(manifest['calibration']==problem['rows'][0]['calibration'],'Calibration binding mismatch')
    expected=['calibration_enclosure_contains_actual_E_y','acquisition_interval_contains_actual_z_y',
              'source_is_real_multiple_of_declared_v_y','declared_path_budget_is_valid',
              'structural_filtered_category_and_source_evaluation_hypotheses']
    require(manifest['external_assumptions']==expected,'Missing or changed assumption boundary')
    fields(manifest['evidence_sha256'],('calibration','structural_problem','structural_certificate'))
    for value in manifest['evidence_sha256'].values():
        require(type(value) is str and len(value)==64 and all(c in '0123456789abcdef' for c in value),'Invalid evidence digest')
    return True


if __name__=='__main__':
    problem=strict_load(sys.argv[1]);certificate=strict_load(sys.argv[2])
    verify(problem,certificate)
    if len(sys.argv)>3:verify_py_manifest(problem,strict_load(sys.argv[3]))
    print('VALID: conditional on declared input assumptions')
