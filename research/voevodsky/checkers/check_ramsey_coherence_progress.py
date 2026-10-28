"""Revision32 scoped progress gates; no implicit native/parent promotion."""
import json
from hashlib import sha256

RESULT_IDS = {
 'result-marked-port-full-field-lift', 'result-ordered-outgoing-E-readout',
 'result-joint44-E-frame-comparison', 'result-complete-directional-reversal',
 'result-canonical-joint44-dual-carriers', 'result-finite-reversed-assembly-descent',
 'theorem-candidate-arbitrary-assembly-coherence'}
OPEN_IDS = {'joint44-native-source-selection','negative-direction-policy-native-descent'}
THEOREM='theorem-candidate-arbitrary-assembly-coherence'
GUARDS={'unbounded_source_graph_coherence':True,'fixed_candidate_assumptions':True,
 'exact_integer_semantics':True,'finite_complete_boundary_reversal':True,
 'formal_kernel_certificate':False,'independent_source_selection':False,
 'unchanged_forward_native_admission':False,'parent_resolved':False}
DEPENDENCIES={
 'result-marked-port-full-field-lift':['prior-geometric-five-column-seed','prior-completed-twelve-port-metric-route'],
 'result-ordered-outgoing-E-readout':['result-marked-port-full-field-lift'],
 'result-joint44-E-frame-comparison':['result-ordered-outgoing-E-readout','prior-joint-field-readout-sewing'],
 'result-complete-directional-reversal':['result-ordered-outgoing-E-readout','prior-direction-indexed-reverse-validator'],
 'result-canonical-joint44-dual-carriers':['result-marked-port-full-field-lift','result-complete-directional-reversal','prior-joint-field-readout-sewing'],
 'result-finite-reversed-assembly-descent':['result-canonical-joint44-dual-carriers','result-complete-directional-reversal'],
 THEOREM:['result-canonical-joint44-dual-carriers'],
 'joint44-native-source-selection':[THEOREM,'result-canonical-joint44-dual-carriers'],
 'negative-direction-policy-native-descent':[THEOREM,'result-complete-directional-reversal']}
PARENTS={
 'result-marked-port-full-field-lift':'T-seam-based-port-readout-binding',
 'result-ordered-outgoing-E-readout':'T-seam-based-port-readout-binding',
 'result-joint44-E-frame-comparison':'T-seam-joint-field-readout-binding',
 'result-complete-directional-reversal':'dual-field-reverse-policy-compatibility',
 'result-canonical-joint44-dual-carriers':'T-seam-joint-field-readout-binding',
 'result-finite-reversed-assembly-descent':'admitted-reversal-overlap-coherence',
 THEOREM:'admitted-reversal-overlap-coherence',
 'joint44-native-source-selection':'T-seam-based-port-readout-binding',
 'negative-direction-policy-native-descent':'reversed-boundary-source-admission'}

def validate(nodes,artifact,require):
 receipts={};digests={}
 for key in RESULT_IDS|OPEN_IDS:
  n=nodes[key]
  require(n['status']==('confirmed_scoped_result' if key in RESULT_IDS else 'open_candidate'),'fresh result/open selection conflated')
  require(n['outcome'] is None and n['attempts']==[],'scoped research promoted to formal outcome')
  require(n['depends_on']==DEPENDENCIES[key] and n['candidate_for']==PARENTS[key],'fresh progress disconnected')
  require(bool(n['evidence']) and bool(n['provenance']),'fresh progress provenance missing')
  if key in RESULT_IDS:
   level='written_mathematical_proof_with_fresh_exact_certificate' if key==THEOREM else 'fresh_exact_scoped_checks'
   require(n['evidence_status']==level and bool(n['verification_level']),'fresh verification level drift')
  else:require(n['protocol']['intent']=='prove' and bool(n['protocol']['stop_condition']),'remaining gate protocol missing')
  for path in n['evidence']:
   p=artifact(path)
   if path.endswith('.json'):
    data=json.loads(p.read_text());receipts[path.rsplit('/',1)[-1]]=data
    for source,digest in data.get('source_sha256',data.get('sourceHashes',{})).items():
     if source not in digests:digests[source]=sha256(artifact(source).read_bytes()).hexdigest()
     require(digests[source]==digest,'stale fresh coherence input: '+source)
 require(nodes[THEOREM]['scope_guards']==GUARDS,'unbounded candidate theorem scope promoted or weakened')
 require(nodes[THEOREM]['motivated_by']==['result-finite-reversed-assembly-descent'],'finite-to-unbounded provenance missing')
 require(nodes['T-seam-based-port-readout-binding']['protocol'].get('recommended_child')=='joint44-native-source-selection','next source-selection gate missing')
 require(nodes['admitted-reversal-overlap-coherence']['protocol'].get('recommended_child')=='negative-direction-policy-native-descent','next native-policy gate missing')
 require(nodes['admitted-reversal-overlap-coherence'].get('conditional_results')==['result-finite-reversed-assembly-descent',THEOREM],'conditional theorem not connected to parent')
 e=receipts['ramsey-outgoing-E-readout-v1.json']
 require(e['scientificStatus']=='ordered_outgoing_E_readout_and_full_complement_pass' and e['orderedWindow']==['M1','C1','C2'] and e['outgoingWindowSlots']==[2,1,3] and e['complementMarks']==['M0','M2'],'corrected E reader lost')
 require(e['exactFull36ActiveReadoutSquare'] and e['exactFull36ComplementReadoutSquare'] and e['exactFiveCoefficientRecovery'],'E recovery/readout weakened')
 carrier=receipts['ramsey-dual-carrier-identification-v1.json']
 require(carrier['middleCarrierMapIsActualPriorPortMap'] and carrier['allCanonicalBindingSquares'] and carrier['allFull44ReadoutSquares'],'canonical carrier scope drift')
 require(carrier['rawEightDecomposition']=={'oldBaryonContrast':2,'retainedOldElectronComplement':6} and carrier['geometryCasesOutsideUnchangedForwardPGuard']==16,'carrier complement or forward guard erased')
 complete=receipts['ramsey-complete-reversed-reference-v1.json']
 require(complete['freshMarkings']==24 and len(complete['rows'])==24 and all(r['dualEWindowReferenceSlots']==[2,1,3] for r in complete['rows']),'whole-certificate coverage drift')
 for filename,packets,edges,triangles in [('ramsey-reversed-assembly-fields-v1.json',14,18,2744),('ramsey-reversed-screw-fields-v1.json',66,95,287496)]:
  r=receipts[filename]
  require((r['packets'],r['interfaces'],r['fullFieldComparisonTriangles'])==(packets,edges,triangles) and r['allPacketFiveCoefficientRecovery'],'finite descent coverage drift')
 q=receipts['ramsey-native-chart-quotient-v1.json'];r=receipts['ramsey-arbitrary-assembly-coherence-v1.json']
 require(q['queueExhausted'] and len(q['states'])==96 and len(q['edges'])==160 and len(q['roots'])==24,'quotient not closed')
 require(r['scientificStatus']=='unbounded_exact_source_graph_coherence_within_declared_field_candidate' and r['allEdgePotentialEquations'],'unbounded theorem missing')
 c,k=r['chartConstants'],r['translationCharacter']
 require(len(c)==96 and all(v in [0,1] for v in c) and k==[0,1,1,0],'parity witness malformed')
 for edge in q['edges']:
  require(c[edge['target']]^c[edge['source']]^(sum(a*b for a,b in zip(k,edge['displacement']))%2)==edge['fieldParity'],'parity edge equation failed')
 require(r['forwardAndReverseFieldTemplateCases']==320 and r['allFivePermutationFrameCases']==19200,'unbounded algebra coverage drift')
 require(receipts['ramsey-forward-generators-replay-v1.json']['status']=='passed','fresh full-field generator replay missing')
 return {'confirmed_scoped_results':sorted(RESULT_IDS),'remaining_open_gates':sorted(OPEN_IDS),
         'receipt_count':len(receipts),'direct_source_files_checked':len(digests),
         'unbounded_coherence':'fixed_candidate_exact_source_graph','formal_kernel_certificate':False}
