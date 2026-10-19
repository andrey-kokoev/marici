"""Disposition/registration audit; science is checked by separate registered scripts."""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json
from check_packet_handoff_naturality_net import audit as audit_naturality

ROOT=Path(__file__).resolve().parents[3]
NET=ROOT/'research/strominger/contracts/port-incidence-conjecture-net.v1.json'
OUT=ROOT/'research/strominger/results/port-incidence-net-audit-v1.json'


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def audit(net):
    assert net['owner']=='marici.Strominger'
    assert net['objective']['status']=='resolved'
    assert net['objective']['verdict']=='constructed_comparison'
    assert net['objective']['outcome'] is None
    assert net['objective']['physical_assignment_complete'] is False
    assert net['operator_stimulus_is_evidence'] is False
    assert all(v is False for v in net['semantics'].values())
    nodes={n['id']:n for n in net['conjectures']}
    assert len(nodes)==len(net['conjectures'])==9
    visiting=set();done=set()
    def visit(k):
        assert k in nodes and k not in visiting
        if k in done:return
        visiting.add(k)
        for d in nodes[k]['depends_on']:visit(d)
        visiting.remove(k);done.add(k)
    for k in nodes:visit(k)
    rejected={'electron-144-is-native-protocol','faithful-A-to-B-fold','same-codimension-rule'}
    assert {k for k,n in nodes.items() if n['disposition']=='rejected'}==rejected
    assert all(nodes[k]['residual'] for k in rejected)
    blocked=nodes['geometric-and-species-attachment']
    assert blocked['disposition']=='blocked_missing_source' and blocked['evidence'] is None
    assert blocked['first_missing_object'] and blocked['acceptance'] and blocked['actionable'] is False
    assert net['frontier']==[] and net['recommended_start'] is None
    assert net['neutrino']['tested'] is False and len(net['neutrino']['rivals'])==4
    assert net['neutrino']['preferred_candidate_id']=='B-MC'
    assert net['neutrino']['preferred_candidate']=={'incoming':['main-space',1],'outgoing':['codimension-sector',3],'candidate_pairs':3,'neutrino_source_tested':False}
    preferred_path=net['neutrino']['preferred_conjecture']
    preferred=json.loads((ROOT/preferred_path).read_text(encoding='utf-8'))
    assert preferred['id']=='neutrino-one-to-three-ports-v1'
    assert preferred['incoming']==['main-space',1] and preferred['outgoing']==['codimension-sector',3]
    assert preferred['candidate_pairs']==3 and preferred['status']=='uninstantiated'
    assert preferred['source_neutrino_tested'] is preferred['geometric_assignment_verified'] is False
    assert 'additional_candidate' not in net['neutrino']
    assert len(net['neutrino']['withdrawn_conjectures'])==1
    extra_path=net['neutrino']['withdrawn_conjectures'][0]
    extra=json.loads((ROOT/extra_path).read_text(encoding='utf-8'))
    assert extra['id']=='neutrino-one-to-four-ports-v1'
    assert extra['status']=='withdrawn' and extra['active'] is False
    assert extra['withdrawal']['scientifically_falsified'] is False
    assert extra['scientifically_tested'] is False
    assert extra['actionable'] is False and extra['formal_outcome'] is None
    p=extra['ports']
    assert (p['incoming_count'],p['outgoing_count'],p['candidate_pair_count'])==(1,4,4)
    assert p['incoming_role'] is p['outgoing_role'] is p['licensed_connections'] is None
    assert extra['test_contract']['first_missing_object'] and extra['test_contract']['falsifier']
    assert net['physical_validation'] is False and net['formal_outcome'] is None
    references=set(net['contracts']+net['scientific_receipts']+net['prospective_freezes'])
    references.update((net['parent_net'],net['packet'],extra_path,preferred_path,NET.relative_to(ROOT).as_posix()))
    for p in references:assert (ROOT/p).is_file(),p
    base,small=[json.loads((ROOT/p).read_text(encoding='utf-8')) for p in net['scientific_receipts']]
    for r in (base,small):
        assert r['status']=='pass' and all(r['checks'].values())
        assert all(digest(ROOT/p)==h for p,h in r['source_sha256'].items()),'stale science'
        references.update(r['source_sha256'])
    assert net['exact_check_groups']==len(base['checks'])+len(small['checks'])==22
    assert net['neutrino']['rivals'][:3]==base['neutrino']['rivals']
    contract=json.loads((ROOT/net['contracts'][0]).read_text(encoding='utf-8'))
    body={k:v for k,v in contract.items() if k not in ('status','disposition')}
    h=sha256(json.dumps(body,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert h==base['contract_semantic_sha256']==net['scientific_semantic_sha256']
    cells=net['candidate_interfaces']
    assert len(cells)==9 and len({c['id'] for c in cells})==9
    originals={c['id']:c for c in contract['interface_candidates']}
    for c in cells:
        assert c['incoming']==originals[c['id']]['incoming']
        assert c['outgoing']==originals[c['id']]['outgoing']
        assert c['pairs']==originals[c['id']]['candidate_pairs']==c['incoming'][1]*c['outgoing'][1]
        assert c['algebraic_witness']
        assert c['geometric_status']==c['physical_assignment']=='unverified'
    assert base['electron_sector_interface']['ordered_pairs']==144
    assert base['electron_sector_interface']['distinct_transfer_matrices']==8
    assert base['electron_literal144_comparison']['incidence_preserving_primitive_bijection'] is False
    for row in small['carriers'].values():
        assert [x['support'] for x in row['interfaces']]==[9,3,3,1]
        assert row['full_three_channel_recovery'] is False
        assert row['kernel_hostile']['rank_P3_minus_N']==2
    follow=net['neutrino_follow_up']
    assert follow['source_availability_correction']
    assert follow['source_relative_disk_boundary_and_cap_inclusion_constructed'] is True
    assert follow['original_triangle_to_cap_metric_ratio']=='3/8'
    assert follow['geometric_chain_coefficients_identified_with_spinor_coordinates'] is False
    assert follow['physical_neutrino_identified'] is follow['new_weak_attachment_admitted'] is False
    assert follow['formal_outcome'] is None
    assert preferred['existing_arrow_first_geometric_candidate_tested'] is True
    assert preferred['relative_geometric_boundary_and_neutron_cap_inclusion_constructed'] is True
    assert preferred['physical_neutrino_identified'] is False
    assert preferred['conditional_construction_receipts']==follow['scientific_receipts']
    assert preferred['conditional_construction_packet']==follow['packet']
    references.add(follow['packet'])
    counts=[];reports=[]
    for path in follow['scientific_receipts']:
        report=json.loads((ROOT/path).read_text(encoding='utf-8'))
        assert report['status']=='pass' and all(report['checks'].values())
        assert all(digest(ROOT/p)==h for p,h in report['source_sha256'].items()),'stale follow-up science'
        counts.append(len(report['checks']));reports.append(report)
        references.add(path);references.update(report['source_sha256'])
    assert counts==[14,6,13] and sum(counts)==follow['exact_check_groups']==33
    assert reports[0]['physical_neutrino_identified'] is reports[1]['physical_neutrino_identified'] is False
    geometric=reports[2]
    assert geometric['geometric_neutrino_candidate_preexisted'] is True
    assert geometric['source_relative_geometric_codimension_constructed'] is True
    assert geometric['physical_spacetime_embedding_or_neutrino_identification'] is False
    assert geometric['new_weak_attachment_admitted'] is False
    assert len(geometric['neutron_caps'])==2
    assert all(cap['old_metric_scale_ratio']=='3/8' and cap['original_fixed_scale_isometry'] is False for cap in geometric['neutron_caps'])
    attachment=net['neutrino_attachment_follow_up']
    assert attachment['packet']==preferred['attachment_follow_up_packet']
    references.add(attachment['packet']);references.update(attachment['prospective_freezes'])
    for key in ('geometric_boundary_attachment_constructed','actual_rim_edge_spinor_ports_constructed','spin_compatible_scalar_contact_constructed'):
        assert attachment[key] is True
    for key in ('spinor_fiber_derived_from_bare_arrows','species_unique_selector_constructed','physical_weak_vertex_constructed','physical_neutrino_identified'):
        assert attachment[key] is False
    assert attachment['formal_outcome'] is None and attachment['first_missing_object']
    assert preferred['geometric_boundary_attachment_constructed'] is True
    assert preferred['source_bound_rim_edge_spinor_ports_constructed'] is True
    assert preferred['spin_compatible_scalar_contact_constructed'] is True
    assert preferred['spinor_fiber_derived_from_bare_arrows'] is preferred['physical_weak_vertex_constructed'] is False
    attachment_reports=[]
    for path in attachment['scientific_receipts']:
        report=json.loads((ROOT/path).read_text(encoding='utf-8'))
        assert report['status']=='pass' and all(report['checks'].values())
        assert all(digest(ROOT/p)==h for p,h in report['source_sha256'].items()),'stale attachment science'
        assert report['physical_weak_vertex_constructed'] is report['physical_neutrino_identified'] is False
        attachment_reports.append(report);references.add(path);references.update(report['source_sha256'])
    assert [len(r['checks']) for r in attachment_reports]==[15,12]
    assert sum(len(r['checks']) for r in attachment_reports)==attachment['exact_check_groups']==27
    rim,contact=attachment_reports
    assert rim['geometric_boundary_attachment_constructed'] is True
    assert rim['species_unique_selector_constructed'] is False
    assert rim['spin_gate']['allowed_vertex_dimension']==0
    assert contact['actual_rim_edge_spinor_ports_constructed'] is contact['spin_compatible_scalar_contact_constructed'] is True
    assert contact['spinor_fiber_derived_from_bare_arrows'] is False
    assert contact['chart_count']==24 and contact['joint_transport_square_count']==144
    indexed=net['indexed_cycle_handoff']
    assert indexed['status']=='resolved_scoped_comparison'
    assert indexed['cycle_index_is_next_copy_not_exponent_or_physical_time'] is True
    for key in ('operator_instruction_is_evidence','sector_labels_physically_bound','observations_alone_force_electron_two_cycle','global_reversibility_forces_coarse_bijection','source_native_handoff_constructed','tag_extension_selects_particle_assignment','physical_spin_or_time_derived','physical_particle_assignment_verified'):
        assert indexed[key] is False
    assert indexed['explicit_tag_extension_constructed'] is True and indexed['formal_outcome'] is None
    assert indexed['retained_handoff_contexts']==2
    assert indexed['minimal_reversible_recurrence']=='F(s,b)=(s XOR b,b)'
    assert indexed['fitting_contextual_completions']==4 and indexed['minimal_bijective_completion_count']==1
    references.update(indexed[k] for k in ('contract','packet','scientific_receipt','prospective_freeze'))
    recurrence_contract=json.loads((ROOT/indexed['contract']).read_text(encoding='utf-8'))
    assert indexed['paths']==recurrence_contract['proposed_paths']
    indexed_nodes={n['id']:n for n in indexed['conjectures']}
    assert len(indexed_nodes)==len(indexed['conjectures'])==8
    todo=set();finished=set()
    def visit_indexed(k):
        assert k in indexed_nodes and k not in todo
        if k in finished:return
        todo.add(k)
        for d in indexed_nodes[k]['depends_on']:visit_indexed(d)
        todo.remove(k);finished.add(k)
    for k in indexed_nodes:visit_indexed(k)
    rejected_indexed={'sector-only-common-handoff','electron-two-cycle-unconditional','native-return-is-indexed-swap','sector-period-selects-spin'}
    assert {k for k,n in indexed_nodes.items() if n['disposition']=='rejected'}==rejected_indexed
    assert all(indexed_nodes[k]['residual'] for k in rejected_indexed)
    assert indexed_nodes['minimal-reversible-contextual-completion']['disposition']=='constructed_conditional'
    binding=indexed_nodes['physical-sector-handoff-binding']
    assert binding['disposition']=='blocked_missing_source' and binding['first_missing_object'] and binding['actionable'] is False
    recurrence=json.loads((ROOT/indexed['scientific_receipt']).read_text(encoding='utf-8'))
    assert recurrence['status']=='pass' and all(recurrence['checks'].values())
    assert len(recurrence['checks'])==indexed['exact_check_groups']==18
    assert all(digest(ROOT/p)==h for p,h in recurrence['source_sha256'].items()),'stale indexed-cycle science'
    references.update(recurrence['source_sha256'])
    finite=recurrence['finite_completion']
    assert finite['context_free_handoff_count']==0 and finite['minimum_handoff_contexts']==2
    assert finite['labelled_completions_examined']==32 and len(finite['fitting_completions'])==4
    assert finite['reversible_completion_count']==1
    assert recurrence['conditional_reversible_recurrence_constructed'] is recurrence['explicit_tag_extension_constructed'] is True
    for key in ('electron_two_cycle_follows_from_paths_alone','source_native_sector_handoff_constructed','tag_extension_selects_species_assignment','physical_particle_assignment_verified','physical_spin_or_time_derived'):
        assert recurrence[key] is False
    assert len(recurrence['compatible_supplied_mode_assignments'])==8
    assert all(row['native_active_payload_period']==1 and row['native_cycle_idempotent'] is True for row in recurrence['native_source_checks'].values())
    successor=net['naturality_successor']
    assert successor['status']=='blocked_not_complete' and successor['completed_iteration']==10 and successor['iteration_budget']==10
    assert successor['native_source_envelope_disposed'] is True
    assert successor['exact_check_groups']==258 and successor['latest_iteration_check_groups']==36
    assert successor['recommended_start'] is None
    assert successor['nonredundant_executable_continuation'] is False
    assert successor['source_native_handoff_constructed'] is successor['physical_assignment_verified'] is False
    child=json.loads((ROOT/successor['conjecture_net']).read_text(encoding='utf-8'))
    references.update(audit_naturality(child))
    for key in ('conjecture_net','iteration_packet','scientific_receipt','audit_receipt'):references.add(successor[key])
    child_audit=json.loads((ROOT/successor['audit_receipt']).read_text(encoding='utf-8'))
    assert child_audit['status']=='pass' and child_audit['objective_complete'] is False
    assert child_audit['scientific_check_groups']==258 and child_audit['iteration_check_groups']==[17,21,24,23,23,25,31,28,30,36]
    assert child_audit['objective_status']=='blocked_not_complete' and child_audit['native_source_envelope_disposed'] is True
    assert successor['iteration_packet']==child['iterations'][-1]['packet']
    assert successor['scientific_receipt']==child['iterations'][-1]['receipt']
    assert all(digest(ROOT/p)==h for p,h in child_audit['source_sha256'].items()),'stale naturality registration'
    for path in references:assert (ROOT/path).is_file(),path
    return references


def main():
    net=json.loads(NET.read_text(encoding='utf-8'))
    references=audit(net)
    hostiles={}
    cases=(('counts_promote_geometry',lambda n:n['candidate_interfaces'][0].update(geometric_status='constructed')),
           ('neutrino_promoted_without_source',lambda n:n['neutrino'].update(tested=True)),
           ('rejected_fold_silently_repaired',lambda n:n['conjectures'][4].update(disposition='constructed')),
           ('state_tangents_become_ports',lambda n:n['semantics'].update(state_tangents_are_ports=True)),
           ('fabricated_frontier',lambda n:n.update(frontier=['geometric-and-species-attachment'])),
           ('conditional_neutrino_physically_promoted',lambda n:n['neutrino_follow_up'].update(physical_neutrino_identified=True)),
           ('cap_inclusion_promoted_to_weak_attachment',lambda n:n['neutrino_follow_up'].update(new_weak_attachment_admitted=True)),
           ('chain_coefficients_promoted_to_spinor_coordinates',lambda n:n['neutrino_follow_up'].update(geometric_chain_coefficients_identified_with_spinor_coordinates=True)),
           ('contact_promoted_to_physical_weak_vertex',lambda n:n['neutrino_attachment_follow_up'].update(physical_weak_vertex_constructed=True)),
           ('borrowed_fiber_promoted_to_arrow_consequence',lambda n:n['neutrino_attachment_follow_up'].update(spinor_fiber_derived_from_bare_arrows=True)),
           ('boundary_context_promoted_to_species_selector',lambda n:n['neutrino_attachment_follow_up'].update(species_unique_selector_constructed=True)),
           ('contact_promoted_to_neutrino_identity',lambda n:n['neutrino_attachment_follow_up'].update(physical_neutrino_identified=True)),
           ('electron_two_cycle_promoted_to_unconditional',lambda n:n['indexed_cycle_handoff'].update(observations_alone_force_electron_two_cycle=True)),
           ('global_reversibility_promoted_to_coarse_bijection',lambda n:n['indexed_cycle_handoff'].update(global_reversibility_forces_coarse_bijection=True)),
           ('tagged_extension_promoted_to_native_handoff',lambda n:n['indexed_cycle_handoff'].update(source_native_handoff_constructed=True)),
           ('tag_compatibility_promoted_to_species_selection',lambda n:n['indexed_cycle_handoff'].update(tag_extension_selects_particle_assignment=True)),
           ('sector_period_promoted_to_spin_or_time',lambda n:n['indexed_cycle_handoff'].update(physical_spin_or_time_derived=True)),
           ('required_handoff_context_erased',lambda n:n['indexed_cycle_handoff'].update(retained_handoff_contexts=1)),
           ('naturality_successor_prematurely_closed',lambda n:n['naturality_successor'].update(status='complete')),
           ('naturality_source_handoff_promoted',lambda n:n['naturality_successor'].update(source_native_handoff_constructed=True)))
    for name,mutate in cases:
        bad=deepcopy(net);mutate(bad)
        try:audit(bad)
        except AssertionError:hostiles[name]=True
        else:raise AssertionError('accepted hostile '+name)
    report={'schema':'marici.port-incidence-net-audit.v1','status':'pass',
        'conjectures':9,'candidate_interfaces':9,'additional_uninstantiated_candidates':0,
        'withdrawn_candidates':1,'preferred_neutrino':'B-MC',
        'fresh_scientific_check_groups':22,'conditional_neutrino_follow_up_check_groups':33,
        'neutrino_attachment_follow_up_check_groups':27,
        'indexed_cycle_handoff_check_groups':18,'indexed_cycle_subconjectures':8,
        'naturality_iteration_check_groups':[17,21,24,23,23,25,31,28,30,36],'naturality_objective_complete':False,
        'neutrino_one_to_four_scientifically_tested':False,
        'negative_dispositions':3,'hostiles':hostiles,
        'source_sha256':{p:digest(ROOT/p) for p in sorted(references)},
        'registration_audit_only':True,'physical_validation':False}
    OUT.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='source_sha256'},indent=2))


if __name__=='__main__':main()
