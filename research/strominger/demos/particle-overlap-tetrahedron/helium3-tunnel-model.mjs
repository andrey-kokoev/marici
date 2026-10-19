import {createWindowConstruction,windowProtocol} from './window-construction-model.mjs';
import {makeLatticeItem,acrossFace,itemKey} from './lattice-items.mjs';
import {windowPrefixGraph,auditStateCoverage} from './fiber-coverage-model.mjs';
import {transportCarrierCoefficients,transportWindowMode,windowModeCoefficients,referenceCarrierMarks} from './deuterium-tunnel-model.mjs';
const copy=x=>structuredClone(x),equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b),mean=ps=>ps[0].map((_,i)=>ps.reduce((s,p)=>s+p[i],0)/ps.length);
const firstAliases=Object.fromEntries([...referenceCarrierMarks,'M2'].map(n=>[n,n]));
export function permuteCharacter(mode,permutation){
 if(!Array.isArray(permutation)||permutation.length!==3||[...permutation].sort((a,b)=>a-b).join(',')!=='0,1,2')throw Error('A three-slot permutation is required');
 const c=windowModeCoefficients(mode),target=permutation.map(i=>c[i]);
 for(const branch of ['common','positive','negative'])for(const phaseExponent of [0,1,2]){const candidate={branch,phaseExponent},v=windowModeCoefficients(candidate);if(v.every((z,i)=>z.every((x,j)=>Math.abs(x-target[i][j])<1e-12)))return candidate;}
 throw Error('Permutation does not preserve a window character');
}
export function sharedNeutronTransfer(c){
 if(!Array.isArray(c)||c.length!==5||c.some(z=>!Array.isArray(z)||z.length!==2||z.some(x=>!Number.isFinite(x))))throw Error('Full five-slot reference carrier required');
 return [0,3,2,1,4].map(i=>[...c[i]]);
}
// Complete the marked N tetrahedron's two MCM and two MCC face ports.
// Enumerate both orientations of the remaining incoming face; do not choose
// by distance or coordinates. Exactly one must use a new electron port.
export function deriveHelium3Branch(first){
 if(first.status!=='complete')throw Error('First packet must be complete');
 const b=first.bindings,seed=makeLatticeItem(first.seed.kind,first.seed.origin,first.seed.inverted),owner=acrossFace(seed,first.events[0].face),incoming=[b.M0,b.C2,b.M1];
 if(!owner.faces.some(f=>itemKey(f)===itemKey(incoming)))throw Error('This marking does not give a regular second proton seed');
 const nextSeed=acrossFace(owner,incoming);if(nextSeed.kind!=='tetrahedron')throw Error('Second proton requires a four-vertex seed');
 const apex=nextSeed.vertices.find(p=>!incoming.some(q=>equal(p,q)));
 if(!apex||Object.values(b).some(p=>equal(p,apex)))throw Error('Second proton context must be a new geometric identity');
 const initialMode=permuteCharacter(first.events[0].modeBefore,[1,0,2]),occupied=new Set(first.items.map(i=>i.key)),accepted=[],rejected=[];
 for(const [m0,m1] of [['M0','M1'],['M1','M0']]){
  const bindings={C0:apex,M0:b[m0],C1:b.C2,M1:b[m1]},run=createWindowConstruction({seed:nextSeed,bindings,...initialMode});run.step();const packet=run.step();
  if(packet.status!=='complete'||packet.items[1].key!==first.items[1].key||!equal(packet.bindings.C2,b.C1))throw Error('Second packet does not retain the same neutron');
  if(occupied.has(packet.items[2].key)){rejected.push({m0,m1,reason:'would reuse an occupied terminal carrier'});continue;}
  accepted.push({seed:nextSeed,bindings,initialMode,aliases:{C0:'C3',M0:m0,C1:'C2',M1:m1,C2:'C1',M2:'M3'},packet});
 }
 if(accepted.length!==1)throw Error('Remaining neutron ports do not select a unique disjoint branch');
 const result=accepted[0];if(result.aliases.M0!=='M1'||result.aliases.M1!=='M0')throw Error('Unexpected neutron port orientation');
 const ports=[...first.events,...result.packet.events].map(e=>itemKey(e.face));
 if(new Set(ports).size!==4||!first.items[1].faces.every(f=>ports.includes(itemKey(f))))throw Error('Neutron face cover is incomplete');
 if(occupied.has(result.packet.items[0].key))throw Error('Second proton would overlap an existing carrier');
 return {...result,rejected,ports};
}
export function createHelium3Tunnel({seed,bindings:initialBindings,branch='positive',phaseExponent=0,complementCoefficients=[[0,0],[0,0]],identity={id:'id'}}={}){
 if(!Array.isArray(complementCoefficients)||complementCoefficients.length!==2||complementCoefficients.some(z=>!Array.isArray(z)||z.length!==2||z.some(x=>!Number.isFinite(x))))throw Error('Two finite complement coefficients required');
 const models=[createWindowConstruction({seed,bindings:initialBindings,branch,phaseExponent,identity})],aliases=[firstAliases],initialMode={branch,phaseExponent},input=[...windowModeCoefficients(initialMode),...copy(complementCoefficients)];
 const carriedIdentity=models[0].snapshot().identity,items=[],bindings={},commits=[],reads=[],passages=[],boundaries=[],observed=new Set(['0:0']);
 let plan=null,cycle=0,localPosition=0,coefficients=copy(input),mode={...initialMode};const maps=[[0,1,2],[3,1,4]];
 function bind(packet,a){for(const [local,p] of Object.entries(packet.bindings)){const global=a[local];if(bindings[global]&&!equal(bindings[global],p))throw Error('Global mark moved');if(!bindings[global]){if(Object.values(bindings).some(q=>equal(p,q)))throw Error('Duplicate global identity name');bindings[global]=[...p];}}}
 function commit(packet,index,a){
  const body=packet.items[index];if(items.some(i=>i.key===body.key))throw Error('Construction cannot revisit a carrier');
  const mapped={...copy(body),nodes:body.nodes.map(n=>a[n]),window:body.window.map(n=>a[n]),continuation:a[body.continuation]};items.push(mapped);bind(packet,a);
 }
 commit(models[0].snapshot(),0,aliases[0]);
 function packetInput(c){return c===0?copy(input):[1,0,2,3,4].map(i=>[...input[i]]);}
 function fibers(c){
  const graph=windowPrefixGraph(models[c].snapshot(),'R'+c);let v=packetInput(c);
  return graph.states.map((s,i)=>{if(i)v=transportCarrierCoefficients(v,models[c].snapshot().events[i-1]);return {...s,cycle:c,localWindow:s.window,window:s.window.map(n=>aliases[c][n]),referenceCarrier:copy(v),identity:carriedIdentity};});
 }
 function assertReader(){const f=fibers(cycle)[localPosition];if(!equal(f.referenceCarrier,coefficients)||!equal(f.mode,mode))throw Error('Shared-neutron fiber mismatch');}
 function transferEvent(event,direction){coefficients=transportCarrierCoefficients(coefficients,event,direction);mode=transportWindowMode(mode,event,direction);}
 function shared(){coefficients=sharedNeutronTransfer(coefficients);mode=permuteCharacter(mode,[2,1,0]);}
 function boundary(direction){
  const e0=models[0].snapshot().events,e1=plan.packet.events;
  if(direction===1){transferEvent(e0[1],-1);shared();transferEvent(e1[0],-1);}
  else {transferEvent(e1[0],1);shared();transferEvent(e0[1],1);}
 }
 function graph(){
  const states=models.flatMap((_,c)=>fibers(c)),transitions=[];
  for(let c=0;c<models.length;c++)for(let i=1;i<models[c].snapshot().items.length;i++)transitions.push(['R'+c+':'+(i-1),'R'+c+':'+i]);
  if(models[1])transitions.push(['R0:2','R1:0']);
  if(models[1]?.snapshot().items.length>=2)transitions.push(['R0:1','R1:1']);
  return {states,transitions,entryStates:['R0:0'],exitStates:items.length===5?['R1:2']:[]};
 }
 function snapshot(){
  assertReader();const packet=models[cycle].snapshot(),terminal=items.length===5,active=packet.items[localPosition],a=aliases[cycle],last=packet.items.length-1;
  const histories=models.map((m,c)=>({cycle:c,word:m.snapshot().history.map(n=>aliases[c][n])}));
  const stateGraph=graph(),prefixCoverage=auditStateCoverage({...stateGraph,exitStates:[stateGraph.states.at(-1).id],requiredCells:items.map(i=>i.key)});
  const first=models[0].snapshot(),interfaces=first.events.map((e,i)=>({from:first.items[i].key,to:first.items[i+1].key,face:copy(e.face),window:[...e.orderedFace]}));
  if(plan)interfaces.push({from:items[3].key,to:items[1].key,face:copy(plan.packet.events[0].face),window:plan.packet.events[0].orderedFace.map(n=>aliases[1][n])});
  if(terminal)interfaces.push({from:items[1].key,to:items[4].key,face:copy(plan.packet.events[1].face),window:plan.packet.events[1].orderedFace.map(n=>aliases[1][n])});
  const guides=packet.events.flatMap((e,i)=>{const port=mean(e.face);return [[packet.items[i].center,port],[port,packet.items[i+1].center]];});
  return {atomTrial:'helium3',status:terminal?'complete':'ready',candidates:terminal?[]:[{kind:items.length<3?'next-window':items.length===3?'complete-neutron-input-ports':'complete-neutron-output-ports'}],identity:carriedIdentity,items:copy(items),bindings:copy(bindings),history:histories.flatMap(h=>h.word),histories,events:copy(commits),readEvents:copy(reads),added:items.length-1,
   entry:copy(models[0].snapshot().entry),exit:{kind:'next-center',target:'next-realization',reached:terminal,point:terminal?[...items[4].center]:null,identity:terminal?carriedIdentity:null},
   counts:Object.fromEntries(['proton','neutron','electron'].map(s=>[s,items.filter(i=>i.species===s).length])),
   tunnel:{position:maps[cycle][localPosition],localPosition,window:active.window.map(n=>a[n]),species:active.species,chartEntry:[...packet.entry.point],mode:{...mode},coefficients:active.window.map(n=>[...coefficients[referenceCarrierMarks.indexOf(n)]]),referenceCarrier:{marks:[...referenceCarrierMarks],aliases:copy(a),coefficients:copy(coefficients)},identity:carriedIdentity,
    frontier:{item:maps[cycle][last],center:[...packet.items[last].center],window:(packet.candidates[0]?.window??packet.items[last].window).map(n=>a[n]),terminal:packet.status==='complete'},
    coverage:{required:5,built:items.length,covered:prefixCoverage.coveredCells,complete:terminal&&prefixCoverage.coveredCells===5,boundaryKind:terminal?'terminal-electron':'construction-frontier'},
    canTowardEntry:terminal&&localPosition>0,canTowardExit:terminal&&localPosition<2,
    realizations:{cycle,count:2,boundaryIdentification:'shared-neutron-overlap-fixing-reference-map',assumed:true,observedStates:[...observed],requiredStates:6,canNextCycle:terminal&&cycle===0&&localPosition>0,canPreviousCycle:terminal&&cycle===1&&localPosition<2,boundaryPassages:copy(boundaries)},
    interfaces,fiberStates:stateGraph.states,guideEdges:copy(guides),passages:copy(passages),sharedNeutronItem:1,
    scope:'Four-port completion of one marked neutron. Five physical carriers, two realization-window paths, one constructed neutron. The overlap-fixing reference/context identification is conditional; a single five-cell spatial Hamiltonian path is not claimed.'}};
 }
 function step(){
  if(items.length===5)return {...snapshot(),committed:false};
  if(items.length<3){const packet=models[0].step();transferEvent(packet.events.at(-1),1);localPosition=packet.items.length-1;commit(packet,localPosition,aliases[0]);commits.push({kind:'new-carrier',item:items.length-1,cycle:0,face:copy(packet.events.at(-1).face)});}
  else if(items.length===3){
   plan=deriveHelium3Branch(models[0].snapshot());boundary(1);models.push(createWindowConstruction({seed:plan.seed,bindings:plan.bindings,identity:carriedIdentity,...plan.initialMode}));aliases.push(plan.aliases);cycle=1;localPosition=0;commit(models[1].snapshot(),0,aliases[1]);commits.push({kind:'new-proton-at-realization-entry',item:3,cycle:1,ordinarySpatialEdge:false});
  }else {
   const n=models[1].step();if(n.items[1].key!==items[1].key)throw Error('Shared neutron changed');transferEvent(n.events[0],1);bind(n,aliases[1]);observed.add('1:1');reads.push({kind:'read-existing-carrier',item:1,cycle:1,newGeometry:false});
   const e=models[1].step();transferEvent(e.events[1],1);localPosition=2;commit(e,2,aliases[1]);commits.push({kind:'new-carrier',item:4,cycle:1,viaExisting:[1],face:copy(e.events[1].face)});
  }
  observed.add(cycle+':'+localPosition);return {...snapshot(),committed:true};
 }
 function pass(direction){
  if(![1,-1].includes(direction))throw RangeError('Direction must be +1 or -1');
  const next=localPosition+direction;if(items.length!==5||next<0||next>2)return {...snapshot(),moved:false};
  const packet=models[cycle].snapshot(),event=packet.events[direction===1?localPosition:next];transferEvent(event,direction);passages.push({cycle,from:localPosition,to:next,direction,face:copy(event.face)});localPosition=next;observed.add(cycle+':'+localPosition);return {...snapshot(),moved:true};
 }
 function crossCycle(direction){
  if(![1,-1].includes(direction))throw RangeError('Direction must be +1 or -1');
  if(items.length!==5||!(direction===1?cycle===0&&localPosition>0:cycle===1&&localPosition<2))return {...snapshot(),crossed:false};
  const from={cycle,localPosition},atNeutron=localPosition===1;
  if(atNeutron)shared();else boundary(direction);
  cycle+=direction;localPosition=atNeutron?1:direction===1?0:2;observed.add(cycle+':'+localPosition);
  boundaries.push({from,to:{cycle,localPosition},kind:atNeutron?'shared-neutron-chart':'cycle-boundary',ordinarySpatialEdge:false,referenceRule:'fix shared M0/M1 identities; exchange C1/C2; retain the full context slot'});
  return {...snapshot(),crossed:true};
 }
 return {snapshot,step,pass,crossCycle,ambientCoverage:requiredCells=>auditStateCoverage({...graph(),requiredCells})};
}
