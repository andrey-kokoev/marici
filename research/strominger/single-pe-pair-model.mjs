// A single marked P/E boundary fixture. No growth words or stage count inputs.
import {GenerativeAssemblyRules} from '../nima/generative-phase-assembly.mjs';
import {applyPhasePermutation} from './demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const copy=x=>structuredClone(x),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
export function makeSinglePEPair({seedBindings=null}={}){
 const rules=new GenerativeAssemblyRules({seedBindings});
 const pn=rules.outgoing(rules.root).map(i=>rules.operations[i]).find(o=>o.kind==='PN');
 const ne=rules.outgoing(pn.target).map(i=>rules.operations[i]).find(o=>o.kind==='NE');
 rules.validateTransfer(pn);rules.validateTransfer(ne);
 const pChart=rules.charts[rules.packets[pn.source].chart],eChart=rules.charts[rules.packets[ne.target].chart];
 function reconstruct(pValue,eValue,orientation=1){
  if(![1,-1].includes(orientation))throw Error('Explicit flow orientation required');
  // Reconstruct geometrically from the two endpoints, not from a supplied N ID.
  const neighbors=c=>rules.geometry.cells[c.cell].faces.map(face=>rules.geometry.neighbor(c.cell,face));
  const pNeighbors=neighbors(pChart),eNeighbors=neighbors(eChart),common=[...new Set(pNeighbors.filter(c=>eNeighbors.includes(c)))];
  if(common.length!==1)throw Error('Endpoint geometry does not select a unique common face neighbor');
  const cell=common[0],chartId=rules.completeN(cell,pChart.aliases);
  if(chartId===null)throw Error('Common neighbor is not a native neutron reader');
  const nChart=rules.charts[chartId];
  for(const mark of ['C0','M0','C1','M1','C2'])if(nChart.aliases[mark]!==eChart.aliases[mark])throw Error('P/E retained reference mismatch');
  const fromP=applyPhasePermutation(pValue,pn.permutation),fromE=applyPhasePermutation(eValue,ne.permutation,-1);
  // Reverse reading changes which endpoint supplies the candidate; it does
  // not turn inverse-NE coefficient reconstruction into a native growth arrow.
  const candidate=orientation===1?fromP:fromE,comparison=orientation===1?fromE:fromP;
  if(!same(candidate,comparison))throw Error('P/E endpoints disagree on the full neutron state');
  return {cell,cellKey:rules.geometry.cells[cell].key,chart:copy(nChart),coefficients:copy(candidate),origin:rules.packets[pn.source].origin,
   orientation,readFrom:orientation===1?'P':'E',readToward:orientation===1?'E':'P',nativeReverseGrowth:false,
   witness:{commonFaceNeighbors:common,pnFace:copy(pn.face),neFace:copy(ne.face),pnPermutation:[...pn.permutation],nePermutation:[...ne.permutation]}};
 }
 function prepare(pValue){
  const eValue=applyPhasePermutation(applyPhasePermutation(pValue,pn.permutation),ne.permutation);
  return {endpoints:{P:copy(pValue),E:eValue},neutron:reconstruct(pValue,eValue),orientation:1,confirmation:'not-requested',history:[]};
 }
 function reverseInPlace(state){
  state.orientation=-state.orientation;state.confirmation='pending';
  state.history.push({action:'reverse-flow-in-place',orientation:state.orientation});return state;
 }
 function confirm(state){
  if(state.confirmation!=='pending')throw Error('No pending reversal to confirm');
  const checked=reconstruct(state.endpoints.P,state.endpoints.E,state.orientation);
  if(checked.cellKey!==state.neutron.cellKey||checked.origin!==state.neutron.origin||!same(checked.coefficients,state.neutron.coefficients))throw Error('Reversal failed retained-state agreement');
  state.neutron=checked;state.confirmation='confirmed';
  state.history.push({action:'positive-confirmation',orientation:state.orientation,cellKey:checked.cellKey,allFiveCoefficients:true});return state;
 }
 return {rules,pn,ne,pChart,eChart,reconstruct,prepare,reverseInPlace,confirm};
}
