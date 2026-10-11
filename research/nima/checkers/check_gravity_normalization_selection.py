"""Normalization identifiability audit; do not execute old claim generators.

Exact current dynamics checks plus fixed-unit alternative gravitational
readout assignments. The assignments are not solutions of a gravitational
field equation: no such equation/coupling is present in this record model.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
from check_four_packet_cycle import UNIT,E2,tensor
from check_four_packet_record_feedback import (
    basis,matrix_of,mm,transpose,cycle,budget,scale,
)
ROOT=Path(__file__).resolve().parents[1]


def main():
    U=matrix_of(lambda v:sum(cycle(v[:4],v[4:]),()),20)
    I=tuple(basis(20));assert mm(transpose(U),U)==I
    for lam in (F(1,3),F(2),F(7)):
        dilation=tuple(tuple(lam*x for x in row) for row in I)
        assert mm(U,dilation)==mm(dilation,U)
    # Overall positive budget calibration cannot be selected by preservation.
    calibrations=[]
    for kappa,tau in ((F(1),F(1)),(F(7),F(3,2)),(F(1,5),F(11))):
        metric=tuple(tuple(kappa*x for x in row) for row in I)
        assert mm(mm(transpose(U),metric),U)==metric
        for t in ((F(0),)*16,tensor(UNIT,UNIT),tensor(E2,E2)):
            out=cycle(UNIT,t)
            assert kappa*budget(*out)==kappa*budget(UNIT,t)
        calibrations.append(dict(budget_multiplier=str(kappa),step_duration=str(tau),
                                 labelled_period_duration=str(6*tau),same_update_matrix=True))
    # Freeze all external units and weak-scale calibration. Vary the missing
    # DIMENSIONLESS Planck/weak readout, not the chosen unit system.
    weak_scale=F(246);reference_mass=F(1)
    old_hierarchy=F(12*11**15)/(1+F(1,90)-F(1,5280))
    assignments=[]
    for multiplier in (F(1),F(2)):
        hierarchy=multiplier*old_hierarchy
        planck=weak_scale*hierarchy
        G=1/(planck*planck)
        alpha=G*reference_mass**2 # hbar=c=1, same fixed reference mass
        assignments.append(dict(hierarchy=str(hierarchy),planck_mass_fixed_units=str(planck),
                                G_fixed_units=str(G),dimensionless_alpha_G=str(alpha)))
    assert F(assignments[1]['G_fixed_units'])==F(assignments[0]['G_fixed_units'])/4
    assert F(assignments[1]['dimensionless_alpha_G'])!=F(assignments[0]['dimensionless_alpha_G'])
    result=dict(schema='marici.nima.gravity-normalization-selection.v1',status='pass',
        exact_symmetries=['U commutes with scalar amplitude dilations',
                          'U^T (kappa I) U=kappa I for every positive kappa',
                          'The discrete update contains no duration fixing tau'],
        calibration_controls=calibrations,
        fixed_external_convention={'weak_scale':'246','reference_mass':'1','hbar':'1','c':'1'},
        alternative_readout_assignments=assignments,
        interpretation='The alternative hierarchy labels demonstrate the missing physical readout constraint; they are not claimed derived predictions or gravitational solutions. Current U, source paths and conservation tests do not depend on either label.',
        source_audit={'check_gravitational_constant.py':'Assigns 246 GeV and Planck hierarchy, states carrier spacing as fundamental input.',
                      'agda/PhysicsConstants.agda':'Proves Nat arithmetic (including 11+4=15), not identification with physical masses or coupling.',
                      'newton-law-from-poisson.md':'Explicitly supplies G and the matter/acceleration coupling.'},
        disposition='Gravitational normalization is not identifiable from the current selected record dynamics. Even fixing external units leaves an unconstrained dimensionless mass/coupling readout.',
        required_new_source='A justified matter/geometry coupling and calibrated observable, or an independently selected dimensionless mass-ratio law. None is supplied by the inspected normalization sources.',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in (
            'checkers/check_four_packet_record_feedback.py','checkers/check_gravitational_constant.py',
            'checkers/check_constant_table.py','agda/PhysicsConstants.agda',
            'newton-law-from-poisson.md','checkers/check_gravity_normalization_selection.py')})
    (ROOT/'results/gravity-normalization-selection.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('alternative_readout_assignments','source_sha256')},indent=2))


if __name__=='__main__':main()
