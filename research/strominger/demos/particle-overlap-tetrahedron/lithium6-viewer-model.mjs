import {lattice,faces} from './simplex-model.mjs';
import {itemKey} from './lattice-items.mjs';
import {windowModeCoefficients,referenceCarrierMarks} from './deuterium-tunnel-model.mjs';
import {auditStateCoverage} from './fiber-coverage-model.mjs';
import {searchLithium6Assemblies,lithiumNNHypothesis} from './lithium6-assembly-model.mjs';
import {compileLithium6Reference,applyLithiumReferenceEdge} from './lithium6-reference-model.mjs';
const copy=x=>structuredClone(x),equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b),active={proton:[0,1,2],neutron:[1,2,3],electron:[3,2,4]};
let defaultReference;
export function selectLithium6Reference(){
 if(!defaultReference){
  const search=searchLithium6Assemblies({allowNN:true});
  outer:for(const candidate of search.candidates)for(let orientations=0;orientations<2**candidate.interfaces.filter(e=>e.kind==='PN').length;orientations++){
   const reference=compileLithium6Reference(candidate,{nnRule:lithiumNNHypothesis,orientations});
   if(reference.status==='reference-algebra-only'){defaultReference={candidate,reference};break outer;}
  }
  if(!defaultReference)throw Error('No whole Li-6 reference assembly admitted in the bounded search');
 }
 return copy(defaultReference);
}
function character(species,coefficients){
 const v=active[species].map(i=>coefficients[i]);
 for(const branch of ['common','positive','negative'])for(const phaseExponent of [0,1,2]){const mode={branch,phaseExponent},test=windowModeCoefficients(mode);if(test.every((z,i)=>z.every((x,j)=>Math.abs(x-v[i][j])<1e-12)))return mode;}
 throw Error('Reference edge left the character sector');
}
export function createLithium6Assembly({researchOnly=false,nnRule,branch='positive',phaseExponent=0,complementCoefficients=[[0,0],[0,0]],identity={id:'id'}}={}){
 if(!researchOnly)throw Error('Li-6 withdrawn: phase discipline is not verified; research algebra only');
 if(nnRule!==lithiumNNHypothesis)throw Error('Li-6 requires an explicit NN reference hypothesis');
 if(!Array.isArray(complementCoefficients)||complementCoefficients.length!==2||complementCoefficients.some(z=>!Array.isArray(z)||z.length!==2||z.some(x=>!Number.isFinite(x))))throw Error('Two finite complement coefficients required');
 const {candidate,reference:r}=selectLithium6Reference(),input=[...windowModeCoefficients({branch,phaseExponent}),...copy(complementCoefficients)],carriedIdentity=Object.freeze({...identity});
 const names={},bindings={};for(const node of Object.keys(candidate.types).map(Number).sort((a,b)=>a-b)){const name='vertex-'+node;names[node]=name;bindings[name]=[...lattice.nodes[node].address];}
 const ids=[...candidate.nucleus,...candidate.electrons],items=ids.map(cell=>{
  const chart=r.charts.find(c=>c.cell===cell),vertices=lattice.cells[cell].map(v=>[...lattice.nodes[v].address]),nodes=lattice.cells[cell].map(v=>names[v]);
  return {key:itemKey(vertices),kind:'tetrahedron',species:chart.species,vertices,components:[copy(vertices)],faces:faces.map(f=>f.map(i=>[...vertices[i]])),center:vertices[0].map((_,j)=>vertices.reduce((sum,p)=>sum+p[j]/4,0)),nodes,window:chart.window.map(v=>names[v]),continuation:names[lattice.cells[cell].find(v=>!chart.window.includes(v))]};
 });
 let cursor=0,chart=r.root,turn=0,terminalEdge=null,coefficients=copy(input),permutation=[0,1,2,3,4];
 const passages=[],circuits=[],observed=new Set(),stateKey=()=>chart+':'+permutation.join(''),stateIds=new Set(r.states.map(s=>s.id));observed.add(stateKey());
 function execute(edgeIndex,direction){
  const e=r.edges[edgeIndex],from=direction===1?e.from:e.to,to=direction===1?e.to:e.from;if(chart!==from)throw Error('Wrong source reader');
  coefficients=applyLithiumReferenceEdge(coefficients,e,direction);permutation=applyLithiumReferenceEdge(permutation.map(x=>[x,0]),e,direction).map(z=>z[0]);chart=to;
  if(!stateIds.has(stateKey())||!equal(coefficients,permutation.map(i=>input[i])))throw Error('Full-state reference mismatch');
  observed.add(stateKey());passages.push({kind:e.kind,from,to,direction,permutation:[...permutation]});
 }
 function advance(direction){
  if(direction===1){const h=r.tour[cursor];execute(h.edge,h.direction);cursor=(cursor+1)%r.tour.length;if(cursor===0)turn=(turn+1)%r.operatorOrder;}
  else {if(cursor===0)turn=(turn+r.operatorOrder-1)%r.operatorOrder;cursor=(cursor+r.tour.length-1)%r.tour.length;const h=r.tour[cursor];execute(h.edge,-h.direction);}
 }
 function snapshot(){
  const c=r.charts[chart],position=ids.indexOf(c.cell),exits=candidate.electrons.map(i=>ids.indexOf(i)),atExit=terminalEdge!==null,ne=r.edges.findIndex(e=>e.kind==='NE'&&e.from===chart);
  const fiberStates=r.states.map(s=>{const reader=r.charts[s.chart],value=s.permutation.map(i=>[...input[i]]);return {...copy(s),window:reader.window.map(v=>names[v]),aliases:Object.fromEntries(referenceCarrierMarks.map(k=>[k,names[reader.aliases[k]]])),referenceCarrier:value,mode:character(reader.species,value),identity:carriedIdentity};});
  return {atomTrial:'lithium6',status:'unadmitted',phaseAudit:copy(r.phaseAudit),viewerAdmitted:false,identity:carriedIdentity,items:copy(items),bindings:copy(bindings),history:[],histories:[],events:[],readEvents:copy(passages),added:0,candidates:[],counts:{proton:3,neutron:3,electron:3},
   construction:{kind:'whole-assembly-constraint-solution',retainedHe4PrefixRequired:false,oneCarrierPerElementTransitionRequired:false},
   entry:{point:[...items[ids.indexOf(r.charts[r.root].cell)].center]},exit:{reached:atExit,point:atExit?[...items[position].center]:null,identity:atExit?carriedIdentity:null},
   tunnel:{position,localPosition:position===0?0:1,chart,window:c.window.map(v=>names[v]),species:c.species,mode:character(c.species,coefficients),coefficients:active[c.species].map(i=>[...coefficients[i]]),referenceCarrier:{marks:[...referenceCarrierMarks],aliases:Object.fromEntries(referenceCarrierMarks.map(k=>[k,names[c.aliases[k]]])),coefficients:copy(coefficients),permutation:[...permutation]},identity:carriedIdentity,
    chartEntry:[...items[0].center],exitItems:exits,frontier:{item:atExit?position:exits[0],center:[...items[atExit?position:exits[0]].center],terminal:true},
    coverage:{required:9,built:9,covered:r.coverage.coveredCells,complete:true,boundaryKind:'terminal-electrons'},canTowardEntry:true,canTowardExit:!atExit,canReadElectron:ne>=0,
    realizations:{cycle:turn,count:r.operatorOrder,clockLabel:'circuit',boundaryIdentification:nnRule,assumed:true,observedStates:[...observed],requiredStates:r.states.length,canNextCycle:!atExit,canPreviousCycle:!atExit,boundaryPassages:copy(circuits)},
    fiberStates,passages:copy(passages),interfaces:candidate.interfaces.map(e=>({kind:e.kind,from:items[ids.indexOf(e.from)].key,to:items[ids.indexOf(e.to)].key,face:e.face.map(v=>[...lattice.nodes[v].address])})),guideEdges:[],operatorOrder:r.operatorOrder,readerOrientationMask:r.orientations,scope:r.scope}};
 }
 function pass(direction){
  if(![1,-1].includes(direction))throw Error('Signed direction required');if(terminalEdge!==null){if(direction===1)return {...snapshot(),moved:false};execute(terminalEdge,-1);terminalEdge=null;}else advance(direction);return {...snapshot(),moved:true};
 }
 function readElectron(){const e=r.edges.findIndex(e=>e.kind==='NE'&&e.from===chart);if(e<0)return {...snapshot(),moved:false};execute(e,1);terminalEdge=e;return {...snapshot(),moved:true};}
 function crossCycle(direction){
  if(![1,-1].includes(direction))throw Error('Signed direction required');if(terminalEdge!==null)return {...snapshot(),crossed:false};
  const before=copy(coefficients);for(let i=0;i<r.tour.length;i++)advance(direction);circuits.push({direction,coefficientsBefore:before,coefficientsAfter:copy(coefficients)});return {...snapshot(),crossed:true};
 }
 return {snapshot,step:()=>({...snapshot(),committed:false}),pass,readElectron,crossCycle,ambientCoverage:requiredCells=>auditStateCoverage({...r,requiredCells})};
}
