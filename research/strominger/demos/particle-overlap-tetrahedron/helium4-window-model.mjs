import {createHelium3Tunnel} from './helium3-tunnel-model.mjs';
import {deriveHelium4Core,applyHelium4CoreStep} from './helium4-core-probe.mjs';
import {referenceCarrierMarks,transportCarrierCoefficients,windowModeCoefficients} from './deuterium-tunnel-model.mjs';
import {auditStateCoverage} from './fiber-coverage-model.mjs';
const copy=x=>structuredClone(x),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
export const helium4ReaderHypothesis='retain-active-face/reference-context-hypothesis';
const activeSlots={proton:[0,1,2],neutron:[1,2,3],electron:[3,2,4]};
function character(species,coefficients){
 const active=activeSlots[species].map(i=>coefficients[i]);
 for(const branch of ['common','positive','negative'])for(const phaseExponent of [0,1,2]){const mode={branch,phaseExponent},v=windowModeCoefficients(mode);if(v.every((z,i)=>z.every((x,j)=>Math.abs(x-active[i][j])<1e-12)))return mode;}
 throw Error('Reader left its admitted character sector');
}
export function createHelium4Window({protonReaderRule,...options}={}){
 if(protonReaderRule!==helium4ReaderHypothesis)throw Error('Helium-4 requires the explicit retained-active-face/context hypothesis');
 const base=createHelium3Tunnel(options),initial=base.snapshot(),identity=initial.identity,input=copy(initial.tunnel.referenceCarrier.coefficients);
 let probe=null,variant=null,charts=null,graph=null,items=null,history=null,events=null,coefficients=null,chart=5,turn=0;
 const passages=[],loopPassages=[],observed=new Set();
 const key=(node,c)=>JSON.stringify([node,c]);
 function electronEvent(node){return probe.retainedPackets[node===1?0:1].events[1];}
 function prepare(){
  const prior=base.snapshot();probe=deriveHelium4Core(prior);
  const selected=probe.alternatives.map((choices,i)=>{
   const retained=prior.items[i===0?0:3].window,matches=choices.filter(c=>c.window.every(n=>retained.includes(n)));
   if(matches.length!==1)throw Error('Active-face retention is not unique');return matches[0];
  });
  variant=probe.variants.find(v=>same(v.choices,selected.map(c=>c.exchangeMiddleM)));
  if(!variant||variant.order!==3)throw Error('Expected the declared three-turn reference circuit');
  const first={C0:'C0',M0:'M0',C1:'C1',M1:'M1',C2:'C2'},second={C0:'C3',M0:'M1',C1:'C2',M1:'M0',C2:'C1'},left=selected[0].aliases,right=selected[1].aliases;
  const specs=[[0,'proton',first],[1,'neutron',first],[1,'neutron',second],[3,'proton',second],[3,'proton',right],[5,'neutron',right],[5,'neutron',left],[0,'proton',left],[2,'electron',first],[4,'electron',second]];
  charts=specs.map(([item,species,aliases],index)=>({index,item,species,aliases,window:activeSlots[species].map(i=>aliases[referenceCarrierMarks[i]])}));
  const source=selected[1].neutron,added={...copy(source),nodes:source.nodes.map(n=>right[n]),window:source.window.map(n=>right[n]),continuation:right[source.continuation]};
  items=[...copy(prior.items),added];history=[...prior.history,...selected[1].window,right.M1];
  // Read back from the existing second electron, then reframe the retained
  // proton before the ONE new PN construction. Never restore cached payloads.
  coefficients=transportCarrierCoefficients(prior.tunnel.referenceCarrier.coefficients,electronEvent(2),-1);
  coefficients=applyHelium4CoreStep(coefficients,variant.steps[2]);
  coefficients=applyHelium4CoreStep(coefficients,variant.steps[3]);
  const before=character('proton',coefficients);
  coefficients=applyHelium4CoreStep(coefficients,variant.steps[4]);
  events=[...copy(prior.events),{kind:'new-neutron',item:5,sourceProton:3,face:copy(selected[1].pn.face),window:[...charts[5].window],retainedContext:right.C2,modeBefore:before,modeAfter:character('neutron',coefficients),readerRule:protonReaderRule,viaExisting:[4,1,3]}];
  const states=[],transitions=[],byKey=new Map(),queue=[];
  function admit(node,c){
   const id=key(node,c);if(byKey.has(id))return id;
   if(states.length>=60)throw Error('Unexpected nonclosing He-4 reference orbit');
   const view=charts[node],state={id,chart:node,cell:items[view.item].key,species:view.species,window:[...view.window],aliases:copy(view.aliases),bindings:copy(prior.bindings),history:[...history],mode:character(view.species,c),referenceCarrier:copy(c),identity};
   states.push(state);byKey.set(id,state);queue.push(state);return id;
  }
  const entry=admit(0,input),exits=[];
  for(let i=0;i<queue.length;i++){
   const s=queue[i];if(s.chart>=8){exits.push(s.id);continue;}
   const next=(s.chart+1)%8,c=applyHelium4CoreStep(s.referenceCarrier,variant.steps[s.chart]);transitions.push([s.id,admit(next,c)]);
   if(s.chart===1||s.chart===2)transitions.push([s.id,admit(s.chart===1?8:9,transportCarrierCoefficients(s.referenceCarrier,electronEvent(s.chart)))]);
  }
  graph={states,transitions,entryStates:[entry],exitStates:exits,byKey};
  // These readers were traversed during the retained construction and final
  // neutron addition. The other clock sheets are not marked visited in advance.
  let c=copy(input);for(let i=0;i<=5;i++){
   observed.add(key(i,c));if(i===1||i===2)observed.add(key(i===1?8:9,transportCarrierCoefficients(c,electronEvent(i))));
   if(i<5)c=applyHelium4CoreStep(c,variant.steps[i]);
  }
  if(!same(c,coefficients))throw Error('New-neutron construction disagrees with the full-state reference circuit');
 }
 function current(){const s=graph.byKey.get(key(chart,coefficients));if(!s)throw Error('Unadmitted full reader state');return s;}
 function snapshot(){
  const prior=base.snapshot();
  if(!items){const t=prior.tunnel;return {...prior,atomTrial:'helium4',status:'ready',exit:{...prior.exit,reached:false},candidates:prior.items.length===5?[{kind:'second-neutron'}]:prior.candidates,
   tunnel:{...t,coverage:{...t.coverage,required:6,complete:false},canTowardEntry:false,canTowardExit:false,canReadElectron:false,realizations:{...t.realizations,cycle:0,count:3,clockLabel:'turn',requiredStates:initial.tunnel.mode.branch==='common'?10:30,boundaryIdentification:protonReaderRule,canNextCycle:false,canPreviousCycle:false},scope:'He-4 construction prefix; conditional proton-reader rule not yet exercised.'}};}
  const state=current(),view=charts[chart],atExit=chart>=8,coverage=auditStateCoverage({...graph,requiredCells:items.map(i=>i.key)});
  return {...prior,atomTrial:'helium4',status:'complete',identity,items:copy(items),history:[...history],histories:[...prior.histories,{kind:'new-neutron-reader',word:history.slice(prior.history.length)}],events:copy(events),readEvents:[...prior.readEvents,{kind:'read-existing-carrier',item:1,newGeometry:false,direction:-1},{kind:'read-existing-carrier',item:3,newGeometry:false,direction:-1},{kind:'proton-reader-hypothesis',item:3,newGeometry:false,readerRule:protonReaderRule}],added:5,candidates:[],counts:{proton:2,neutron:2,electron:2},
   exit:{kind:'retained-electron-centers',reached:atExit,point:atExit?[...items[view.item].center]:null,identity:atExit?identity:null},
   tunnel:{position:view.item,localPosition:view.item===0?0:1,chart,window:[...view.window],species:view.species,mode:{...state.mode},coefficients:activeSlots[view.species].map(i=>[...coefficients[i]]),referenceCarrier:{marks:[...referenceCarrierMarks],aliases:copy(view.aliases),coefficients:copy(coefficients)},identity,
    chartEntry:[...prior.entry.point],exitItems:[2,4],frontier:{item:atExit?view.item:2,center:[...items[atExit?view.item:2].center],terminal:true},
    coverage:{required:6,built:6,covered:coverage.coveredCells,complete:coverage.status==='covered',boundaryKind:'retained-electrons'},
    canTowardEntry:true,canTowardExit:!atExit,canReadElectron:chart===1||chart===2,
    realizations:{cycle:turn,count:3,clockLabel:'turn',boundaryIdentification:protonReaderRule,assumed:true,observedStates:[...observed],requiredStates:graph.states.length,canNextCycle:!atExit,canPreviousCycle:!atExit,boundaryPassages:copy(loopPassages)},
    fiberStates:graph.states.map(s=>({...copy(s),identity})),passages:copy(passages),interfaces:copy(probe.interfaces),guideEdges:[],
    scope:'Conditional He-4 reference trial: retain each proton active face, reverse its C order, and identify the outside context slot. Three-turn holonomy is retained on the full five-slot carrier. No tube, ordinary E-to-P step, or physical stability derivation.'}};
 }
 function step(){
  if(items)return {...snapshot(),committed:false};
  if(base.snapshot().items.length<5)base.step();else prepare();
  return {...snapshot(),committed:true};
 }
 function advance(direction){
  const from=chart,before=key(chart,coefficients),edge=direction===1?chart:(chart+7)%8;
  coefficients=applyHelium4CoreStep(coefficients,variant.steps[edge],direction);chart=(chart+direction+8)%8;
  if(from===7&&chart===0)turn=(turn+1)%3;if(from===0&&chart===7)turn=(turn+2)%3;
  current();observed.add(key(chart,coefficients));passages.push({kind:variant.steps[edge].kind,from,to:chart,direction,fromState:before,toState:key(chart,coefficients)});
 }
 function pass(direction){
  if(![1,-1].includes(direction))throw RangeError('Direction must be +1 or -1');
  if(!items||chart>=8&&direction===1)return {...snapshot(),moved:false};
  if(chart>=8){const from=chart,origin=chart===8?1:2;coefficients=transportCarrierCoefficients(coefficients,electronEvent(origin),-1);chart=origin;current();observed.add(key(chart,coefficients));passages.push({kind:'inverse-electron-read',from,to:chart});}
  else advance(direction);
  return {...snapshot(),moved:true};
 }
 function readElectron(){
  if(!items||![1,2].includes(chart))return {...snapshot(),moved:false};
  const from=chart;coefficients=transportCarrierCoefficients(coefficients,electronEvent(from));chart=from===1?8:9;current();observed.add(key(chart,coefficients));passages.push({kind:'terminal-electron-read',from,to:chart});return {...snapshot(),moved:true};
 }
 function crossCycle(direction){
  if(![1,-1].includes(direction))throw RangeError('Direction must be +1 or -1');
  if(!items||chart>=8)return {...snapshot(),crossed:false};
  const before=copy(coefficients),from=turn;for(let i=0;i<8;i++)advance(direction);
  loopPassages.push({kind:'full-nuclear-circuit',direction,chart,from,to:turn,coefficientsBefore:before,coefficientsAfter:copy(coefficients)});return {...snapshot(),crossed:true};
 }
 return {snapshot,step,pass,crossCycle,readElectron,ambientCoverage:requiredCells=>items?auditStateCoverage({...graph,requiredCells}):base.ambientCoverage(requiredCells)};
}
