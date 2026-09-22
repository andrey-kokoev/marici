"""Calibrate the actual P_y private row and export a conditional numerical bridge."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util
import hashlib
import json
from flint import arb

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj);return obj


def save(path,value):path.write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    c=load('calibration',HERE/'certify_joint_cubic_reconstruction.py')
    s=load('solver',ROOT/'certificates/diagonal_task_solver.py')
    v=load('verifier',ROOT/'certificates/verify_diagonal_task.py')
    # Actual first retained windows: [2,4] and [420,4620]. Middle seam is vacuum.
    logE=((c.scaled_residual(2)*c.scaled_residual(420)/5).log()
          -arb.pi()*(2**2+420**2))/arb(10).log()
    lo=F(str(logE.lower().fmpq()));hi=F(str(logE.upper().fmpq()))
    exponent_lo=lo.numerator//lo.denominator
    exponent_hi=-((-hi.numerator)//hi.denominator)
    assert exponent_lo<exponent_hi<0
    calibration=['1e'+str(exponent_lo),'1e'+str(exponent_hi)]
    ratio=F(1,10**(exponent_hi-exponent_lo))
    p={'model':s.MODEL,'rows':[{'data':calibration[:],'calibration':calibration[:],'weight':'32'}],
       'budget':'32','target':{'coefficients':['1'],'threshold':str(ratio/2)}}
    cert=s.solve(p);assert cert['status']=='TARGET_TRUE' and v.verify(p,cert)
    calpath=ROOT/'results/py-bridge-calibration.json'
    save(calpath,{'log10_E_y':str(logE),'certified_positive_E_y_enclosure':calibration,
        'formula':'E_y=K_[2,4]*K_[420,4620]/5',
        'method':'192-bit Arb completed-cell residual integration with theta and infinite integral tail bounds',
        'synthetic_acquisition':'Raw z_y interval is set equal to this broad calibration enclosure; it contains the prediction for source v_y. This is not an experimental measurement.'})
    structural=ROOT.parent/'voevodsky/results'
    manifest={'version':1,'protocol':'cubic-P_y-raw-residual-v1','problem_sha256':s.digest(p),
        'source_class':'real line spanned by mixed(2,3) forgotten(5,7) mixed(11,13)',
        'outer_corner':[2,60060],
        'seams':[[2,4,'retained'],[12,60,'forgotten'],[420,4620,'retained']],
        'normalized_coordinate':'P_y','raw_coordinate':'z_y','equation':'z_y=E_y*P_y',
        'calibration':calibration,'spectral_point':'3i','receiver_gamma':'2','forcing_beta':'4',
        'external_assumptions':['calibration_enclosure_contains_actual_E_y',
            'acquisition_interval_contains_actual_z_y','source_is_real_multiple_of_declared_v_y',
            'declared_path_budget_is_valid','structural_filtered_category_and_source_evaluation_hypotheses'],
        'evidence_sha256':{'calibration':sha(calpath),
            'structural_problem':sha(structural/'filtered-obstruction-problem.json'),
            'structural_certificate':sha(structural/'filtered-obstruction-certificate.json')}}
    assert v.verify_py_manifest(p,manifest)
    for name,value in [('problem',p),('certificate',cert),('manifest',manifest)]:
        save(ROOT/'results'/('py-bridge-'+name+'.json'),value)
    print(json.dumps({'passed':True,'E_y_enclosure':calibration,'log10_E_y':str(logE),
                     'certified_normalized_target':'P_y > '+str(ratio/2),
                     'source_witness':cert['witness'],'raw_reading_is_not_normalized_to_one':True},indent=2))


if __name__=='__main__':main()
