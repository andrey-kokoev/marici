"""Audit the new kernel minimum and separate, still-incomplete fresh prover.
The original benchmark and its receipts are not rewritten.
"""
from pathlib import Path
import hashlib
import io
import json
import unittest
from build_minimality_cover import BASE
from emit_minimum_kernel import emit, support
from emit_fresh_equations import emit as emit_equations
from check_fresh_equations import verify

if not __debug__:
    raise RuntimeError('audit assertions must remain enabled')

CERTIFICATE_SOURCE = '''{-# OPTIONS --safe --cubical --guardedness #-}
module SynthesisCertifiedMinimum where
open import Cubical.Foundations.Prelude
open import AlgebraSynthesisSpecification
open import DiscoveredWolframFormula using (found-formula; adequate)
open import GeneratedMinimumCoverage

module Certified (ℓ : Level) where
  minimum : Goal.Minimal ℓ found-formula
  minimum f cheaper = Coverage.no-cheaper ℓ f cheaper

  certificate : Goal.Result ℓ
  certificate = Goal.certify ℓ found-formula adequate minimum

-- Adequacy above is still the explicitly reused proof. This module closes
-- the minimum/Sigma gate, not the independent fresh-proof-search gate.
'''


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name):
    return json.loads((BASE/'results'/name).read_text(encoding='utf-8-sig'))


def receipt(name, module, expected_controls, old):
    packet=load(name)
    assert packet['schema']=='marici.synthesis.kernel-audit.v1'
    assert packet['module']==module and packet['passed'] is True
    assert packet['exit_code']==0 and packet['inputs_stable'] is True
    assert packet['ignore_interfaces'] is True and packet['no_new_window'] is True
    assert '--ignore-interfaces' in packet['args']
    assert {c['module']:c['expected_diagnostic'] for c in packet['controls']}==expected_controls
    assert all(c['correctly_rejected'] is True and c['exit_code']!=0 for c in packet['controls'])
    assert packet['compiler_sha256'].lower()==old['compiler_sha256'].lower()
    assert digest(packet['command'])==packet['compiler_sha256'].lower()
    assert digest(BASE/'checkers/check_synthesis_kernel.ps1')==packet['checker_sha256'].lower()
    owner={str(p.relative_to(BASE/'agda')).replace('\\','/'):digest(p) for p in (BASE/'agda').rglob('*.agda')}
    assert owner=={k:v.lower() for k,v in packet['owner_source_inventory_sha256'].items()}
    for path,sha in packet['library_source_inventory_sha256'].items():
        assert digest(Path(packet['library'])/path)==sha.lower()
    return {'receipt':name,'sha256':digest(BASE/'results'/name),'module':module,
            'fresh':True,'controls':list(expected_controls)}


def decode(t):
    if type(t) is int and t>=0: return f'x{t}'
    assert isinstance(t,list) and len(t)==2
    return tuple(decode(x) for x in t)


def main():
    old=load('algebra-synthesis-formal-audit.json')
    # Freeze the original goal and cached benchmark interface against its
    # pre-completion receipt: changing the grammar/meaning is not completion.
    frozen=['AlgebraSynthesisSpecification.agda','BooleanNandEquivalence.agda',
            'DiscoveredWolframFormula.agda','WolframBooleanAlgebra.agda','WolframConverse.agda']
    for name in frozen:
        assert digest(BASE/'agda'/name)==old['owner_source_inventory_sha256'][name].lower()
    assert (BASE/'agda/SynthesisCertifiedMinimum.agda').read_text(encoding='utf-8')==CERTIFICATE_SOURCE
    cover=load('minimality-prefix-cover.json')
    chunks,coverage=emit(cover)
    for name,text in chunks.items():
        assert (BASE/'agda'/name).read_text(encoding='utf-8')==text
    assert (BASE/'agda/GeneratedMinimumCoverage.agda').read_text(encoding='utf-8')==coverage
    assert (BASE/'agda/SynthesisMinimumSupport.agda').read_text(encoding='utf-8')==support(cover['models'])
    packet=load('fresh-equational-search-final.json')
    provenance=packet['provenance']
    assert provenance['prover_sha256']==digest(BASE/'checkers/fresh_equational_search.py')
    source_path=BASE/'results/algebra-formula-search.json'
    assert provenance['candidate_source_sha256']==digest(source_path)
    source=json.loads(source_path.read_text())
    candidate=next(x for x in source['survivors'] if (x['cost'],x['ordinal'])==(provenance['cost'],provenance['ordinal']))
    replay=verify(packet,(decode(candidate['left']),decode(candidate['right'])))
    assert (BASE/'agda/FreshEquationalConsequences.agda').read_text(encoding='utf-8')==emit_equations(packet)
    minimum=receipt('synthesis-kernel-formal-audit.json','SynthesisCertifiedMinimum',
        {'SynthesisMinimumMissingCase':'[CoverageIssue]','SynthesisMinimumBadRejection':'[UnequalTerms]'},old)
    fresh=receipt('fresh-equations-kernel-formal-audit.json','FreshEquationalConsequences',
        {'FreshWrongConclusion':'[UnequalTerms]'},old)
    stream=io.StringIO()
    suite=unittest.defaultTestLoader.discover(str(BASE/'checkers'),pattern='test_synthesis_completion.py')
    tests=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
    (BASE/'results/synthesis-completion-tests.log').write_text(stream.getvalue(),encoding='utf-8')
    assert tests.wasSuccessful(),stream.getvalue()
    result={'schema':'marici.synthesis-completion-audit.v1',
        'status':'kernel-minimum-closed-independent-adequacy-open',
        'kernel_checked_minimality':True,'agda_sigma_package_constructed':True,
        'sigma_adequacy_origin':'existing quantified proof, explicitly reused',
        'fresh_consequences_kernel_checked':replay['facts_checked'],
        'fresh_basis_complete':replay['basis_complete'],
        'independent_adequacy_constructed':False,'full_requested_completion':False,
        'autonomous_formula_selection_by_fresh_prover':False,
        'minimum':minimum,'fresh_consequences':fresh,'prefix_cover':cover['statistics'],
        'tests_run':tests.testsRun,'formula_cost':6,'symbol_length':15,
        'frozen_goal_reference':'algebra-synthesis-formal-audit.json',
        'boundary':'Total kernel coverage, not reliance on a Python enumeration count. Fresh conditional equations are not an Adequate witness.',
        'missing_typed_object':'A newly derived Adequate witness, including Boolean validity and reconstruction; fresh search has not derived the four basis goals.',
        'residuals':['fresh proof discovery and adequacy integration remain open',
                     'fixture selection is not an autonomous enumeration-to-proof pipeline',
                     'no runtime refinement theorem for the former Layer4 engine',
                     'Cubical indexed-match transport computation warnings remain; no executable extraction is claimed'],
        'sha256':{name:digest(BASE/name) for name in [
            'results/minimality-prefix-cover.json','results/fresh-equational-search-final.json',
            'checkers/build_minimality_cover.py','checkers/emit_minimum_kernel.py',
            'checkers/fresh_equational_search.py','checkers/check_fresh_equations.py',
            'checkers/emit_fresh_equations.py','checkers/check_synthesis_completion.py',
            'checkers/test_synthesis_completion.py','checkers/check_synthesis_kernel.ps1',
            'agda/AlgebraSynthesisSpecification.agda','agda/SynthesisCertifiedMinimum.agda']}}
    (BASE/'results/synthesis-completion-audit.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'tests':tests.testsRun,'fresh_facts':replay['facts_checked'],
                      'kernel_minimum':True,'fresh_adequacy':False}))


if __name__=='__main__': main()
