import {lattice,faces} from './simplex-model.mjs';
import {nitrogen15Reference} from './nitrogen15-reference.mjs';
import {assemblyDomain,searchLithiumAssemblies,searchBeryllium9Assemblies,searchBoronAssemblies,searchCarbonAssemblies} from './lithium6-assembly-model.mjs';
import {makeLatticeItem,itemKey} from './lattice-items.mjs';
import {createWindowConstruction,windowProtocol} from './window-construction-model.mjs';
import {transportCarrierCoefficients,referenceCarrierMarks,windowModeCoefficients} from './deuterium-tunnel-model.mjs';
import {createHelium3Tunnel} from './helium3-tunnel-model.mjs';
import {deriveHelium4Core} from './helium4-core-probe.mjs';
import {auditPhaseCombination} from './phase-discipline-model.mjs';
import {auditStateCoverage} from './fiber-coverage-model.mjs';
import {phaseFrame,phaseAdvanceWitness,applyPhasePermutation,spectralReadout} from './phase-advance-model.mjs';
const copy=x=>structuredClone(x),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b),identityPermutation=[0,1,2,3,4];
const domain=assemblyDomain(),keys=lattice.cells.map(c=>itemKey(c.map(v=>lattice.nodes[v].address))),cellByKey=new Map(keys.map((k,i)=>[k,i]));
const pointByKey=new Map(lattice.nodes.map((n,i)=>[JSON.stringify(n.address),'vertex-'+i]));
const rootBindings=Object.fromEntries(Object.entries(createWindowConstruction().snapshot().bindings).map(([name,p])=>[name,pointByKey.get(JSON.stringify(p))]));
function nativePermutation(event){return transportCarrierCoefficients(identityPermutation.map(i=>[i,0]),event).map(z=>z[0]);}
export function geometryCandidate(snapshot){
 const ids=snapshot.items.map(i=>cellByKey.get(i.key));if(ids.some(i=>i===undefined))throw Error('Assembly outside the current primitive domain');
 const types={};for(const [mark,p] of Object.entries(snapshot.bindings)){const node=lattice.nodes.findIndex(n=>same(n.address,p));if(node>=0)types[node]=mark[0];}
 const nucleus=ids.filter((_,i)=>snapshot.items[i].species!=='electron'),electrons=ids.filter((_,i)=>snapshot.items[i].species==='electron');
 const interfaces=ids.flatMap(i=>domain.adjacency[i].filter(e=>i<e.to&&ids.includes(e.to)).map(e=>({from:i,to:e.to,face:[...e.face],kind:electrons.includes(i)||electrons.includes(e.to)?'NE':domain.species[i]===domain.species[e.to]?'NN':'PN'})));
 return {nucleus,electrons,types,interfaces,displayOrder:ids};
}
// Carrier reachability is not sufficient: every actual full-face contact
// needs a typed transport edge. Reconstruct the ledger independently so an
// edited certificate cannot hide a contact by deleting its declaration.
export function auditAssemblyContacts({candidate,charts,edges}){
 const {nucleus,electrons,types}=candidate,all=[...nucleus,...electrons],occupied=new Set(all);
 if(occupied.size!==all.length||all.some(i=>!lattice.cells[i]))throw Error('Invalid physical carrier set');
 const species=i=>electrons.includes(i)?'electron':domain.species[i];
 for(const i of all)if(lattice.cells[i].some(v=>!['M','C'].includes(types[v]))||lattice.cells[i].filter(v=>types[v]==='M').length!==2)throw Error('Each carrier needs explicit MMCC roles');
 const key=(a,b,kind,face)=>JSON.stringify([Math.min(a,b),Math.max(a,b),kind,[...face].sort((x,y)=>x-y)]),actual=new Map();
 for(const i of all)for(const e of domain.adjacency[i])if(i<e.to&&occupied.has(e.to)){
  const a=species(i),b=species(e.to);if(a===b&&a!=='neutron'||[a,b].includes('electron')&&[a,b].includes('proton'))throw Error('Unsupported physical face contact');
  const kind=[a,b].includes('electron')?'NE':a===b?'NN':'PN';
  if(e.face.filter(v=>types[v]==='M').length!==(kind==='PN'?2:1))throw Error('Physical contact role mismatch');
  actual.set(key(i,e.to,kind,e.face),{from:i,to:e.to,kind,face:[...e.face]});
 }
 const declared=candidate.interfaces.map(e=>key(e.from,e.to,e.kind,e.face));
 if(declared.length!==actual.size||new Set(declared).size!==declared.length||declared.some(k=>!actual.has(k)))throw Error('Assembly interface ledger mismatch');
 for(const c of charts)if(!occupied.has(c.cell)||c.species!==species(c.cell))throw Error('Chart does not represent an occupied carrier');
 const witnessed=new Set();
 for(const e of edges){
  const a=charts[e.from],b=charts[e.to];if(!a||!b)throw Error('Unknown contact chart');
  if(e.kind==='reader-phase-advance'){if(a.cell!==b.cell)throw Error('Reader advance changes carrier');continue;}
  const kind=({'PN':'PN','inverse-PN':'PN','NE':'NE','NN-phase-advance':'NN'})[e.kind];if(!kind)throw Error('Unknown physical transport kind');
  const face=lattice.cells[a.cell].filter(v=>lattice.cells[b.cell].includes(v)),k=key(a.cell,b.cell,kind,face);
  if(face.length!==3||!actual.has(k))throw Error('Transport does not witness an actual contact');witnessed.add(k);
 }
 const missing=[...actual].filter(([k])=>!witnessed.has(k)).map(([,e])=>e);
 return {status:missing.length?'unwitnessed-physical-contact':'all-physical-contacts-witnessed',requiredContacts:actual.size,witnessedContacts:witnessed.size,missing};
}
export function compilePhaseAssembly(candidate,orientations=0){
 const {nucleus,electrons,types}=candidate,all=[...nucleus,...electrons],pn=candidate.interfaces.filter(e=>e.kind==='PN');
 if(new Set(all).size!==all.length||!nucleus.includes(0)||all.some(i=>!lattice.cells[i]))throw Error('Distinct in-domain carriers and a root proton required');
 if(!Number.isInteger(orientations)||orientations<0||orientations>=2**pn.length)throw Error('Invalid reader assignment');
 for(const i of all)if(lattice.cells[i].some(v=>!['M','C'].includes(types[v]))||lattice.cells[i].filter(v=>types[v]==='M').length!==2)throw Error('Each carrier needs explicit MMCC roles');
 if(Object.entries(rootBindings).some(([name,vertex])=>types[Number(vertex.slice(7))]!==name[0]))return {status:'rejected',reason:'root-phase-boundary-mismatch'};
 const actual=[];
 for(const i of all)for(const e of domain.adjacency[i])if(i<e.to&&all.includes(e.to)){
  const a=electrons.includes(i)?'electron':domain.species[i],b=electrons.includes(e.to)?'electron':domain.species[e.to];
  if(a===b&&a!=='neutron'||[a,b].includes('electron')&&[a,b].includes('proton'))throw Error('Unsupported physical face contact');
  const kind=[a,b].includes('electron')?'NE':a===b?'NN':'PN';
  if(e.face.filter(v=>types[v]==='M').length!==(kind==='PN'?2:1))return {status:'rejected',reason:'interface-role-mismatch'};
  actual.push([i,e.to,kind,[...e.face].sort((a,b)=>a-b)]);
 }
 const declared=candidate.interfaces.map(e=>[Math.min(e.from,e.to),Math.max(e.from,e.to),e.kind,[...e.face].sort((a,b)=>a-b)]);
 if(!same(actual.sort(),declared.sort()))throw Error('Assembly interface ledger mismatch');
 const charts=[],edges=[],packets=[];
 function add(from,to,permutation,kind,phaseDelta=0,witness=null){edges.push({from,to,permutation:[...permutation],kind,phaseDelta,witness});}
 for(const [i,link] of pn.entries()){
  const p=domain.species[link.from]==='proton'?link.from:link.to,n=p===link.from?link.to:link.from,component=lattice.assembly.components[p];
  const ms=link.face.filter(v=>types[v]==='M').sort((a,b)=>a-b);if(ms.length!==2||domain.species[n]!=='neutron')return {status:'rejected',reason:'invalid-PN-face'};
  if(orientations&(1<<i))ms.reverse();
  const local={C0:lattice.cells[p].find(v=>!link.face.includes(v)),M0:ms[0],C1:link.face.find(v=>types[v]==='C'),M1:ms[1]};
  const seed=makeLatticeItem('tetrahedron',component.origin,component.transform.kind==='inversion'),model=createWindowConstruction({seed,bindings:Object.fromEntries(Object.entries(local).map(([k,v])=>[k,lattice.nodes[v].address]))});model.step();const packet=model.step();
  if(packet.status!=='complete'||packet.items[1].key!==keys[n])return {status:'rejected',reason:'native-packet-mismatch'};
  const aliases=Object.fromEntries(Object.entries(packet.bindings).map(([name,point])=>[name,pointByKey.get(JSON.stringify(point))]));
  const e=cellByKey.get(packet.items[2].key),pChart=charts.length;
  charts.push({id:String(pChart),cell:p,species:'proton',aliases:copy(aliases)});
  const nChart=charts.length;charts.push({id:String(nChart),cell:n,species:'neutron',aliases:copy(aliases)});
  const map=nativePermutation(packet.events[0]);add(pChart,nChart,map,'PN');add(nChart,pChart,map,'inverse-PN');
  if(electrons.includes(e)){const eChart=charts.length;charts.push({id:String(eChart),cell:e,species:'electron',aliases:copy(aliases)});add(nChart,eChart,nativePermutation(packet.events[1]),'NE');}
  packets.push({p,n,e,pChart,nChart});
 }
 for(let i=0;i<charts.length;i++)for(let j=i+1;j<charts.length;j++)if(charts[i].cell===charts[j].cell&&charts[i].species!=='electron'){
  try{const forward=phaseAdvanceWitness(charts[i],charts[j]),back=phaseAdvanceWitness(charts[j],charts[i]);add(i,j,forward.permutation,'reader-phase-advance',1,forward);add(j,i,back.permutation,'reader-phase-advance',1,back);}
  catch{return {status:'rejected',reason:'incompatible-local-phase-readers'};}
 }
 for(const link of candidate.interfaces.filter(e=>e.kind==='NN')){
  let count=0;
  for(const from of charts.filter(c=>c.cell===link.from&&c.species==='neutron'))for(const to of charts.filter(c=>c.cell===link.to&&c.species==='neutron'))for(const [a,b] of [[from,to],[to,from]]){
   try{const witness=phaseAdvanceWitness(a,b),packet=packets.find(p=>p.nChart===Number(a.id));if(packet.e!==b.cell)continue;
    const shared=link.face.map(v=>'vertex-'+v);if(shared.length!==3||!shared.every(v=>lattice.cells[b.cell].some(n=>'vertex-'+n===v)))continue;
    add(Number(a.id),Number(b.id),witness.permutation,'NN-phase-advance',1,witness);count++;
   }catch{/* This assignment does not have the required retained phase edge. */}
  }
  if(!count)return {status:'rejected',reason:'no-phase-consistent-NN-interface'};
 }
 if(all.some(cell=>!charts.some(c=>c.cell===cell)))return {status:'rejected',reason:'missing-carrier-reader'};
 for(const e of edges)if(e.phaseDelta===0){
  const inverse=e.kind==='inverse-PN',a=charts[inverse?e.to:e.from],b=charts[inverse?e.from:e.to],from=phaseFrame(a),to=phaseFrame(b),vertices=to.window.map(o=>o.vertex);
  const result=auditPhaseCombination([from,to],[{from:from.id,to:to.id,kind:inverse?'PN':e.kind,identification:'same-occurrence',vertices}]);if(result.status!=='native-phase-compatible')throw Error('Native interface failed its phase check');e.witness={phaseDelta:0,from,to,phaseAudit:result};
 }
 const contacts=auditAssemblyContacts({candidate,charts,edges});
 if(contacts.missing.length)return {status:'rejected',reason:'unwitnessed-physical-contact',contacts};
 const root=charts.findIndex(c=>c.cell===0&&c.species==='proton'&&Object.entries(rootBindings).every(([name,vertex])=>c.aliases[name]===vertex));
 if(root<0)return {status:'rejected',reason:'root-phase-boundary-mismatch'};
 const adj=charts.map(()=>[]);edges.forEach((e,i)=>adj[e.from].push(i));
 const paths=new Map([[root,[]]]),queue=[root];for(let i=0;i<queue.length;i++)for(const index of adj[queue[i]]){const e=edges[index];if(!paths.has(e.to)){paths.set(e.to,[...paths.get(queue[i]),index]);queue.push(e.to);}}
 if(paths.size!==charts.length)return {status:'rejected',reason:'phase-directed-carrier-unreachable'};
 const exitPaths=new Map();for(const start of queue){const q=[start],p=new Map([[start,[]]]);for(let i=0;i<q.length;i++){const c=q[i];if(charts[c].species==='electron'){exitPaths.set(start,p.get(c));break;}for(const index of adj[c]){const e=edges[index];if(!p.has(e.to)){p.set(e.to,[...p.get(c),index]);q.push(e.to);}}}if(!exitPaths.has(start))return {status:'rejected',reason:'phase-directed-dead-end'};}
 // Finite, concrete entry-to-exit witnesses. Absolute origin is part of the
 // state; a returning coefficient permutation NEVER resets that origin.
 const certificateStates=new Map(),certificateEdges=[],exitStateIds=new Set();
 const stateId=s=>s.chart+'@'+s.origin+':'+s.permutation.join('')+'|'+s.history.join('.');
 function keep(s){const id=stateId(s);if(!certificateStates.has(id))certificateStates.set(id,{id,...copy(s),frame:phaseFrame(charts[s.chart],s.origin),cell:keys[charts[s.chart].cell]});return id;}
 const entry={chart:root,origin:0,permutation:[...identityPermutation],history:[]},entryId=keep(entry);
 for(const chart of queue){let state=copy(entry);for(const index of [...paths.get(chart),...exitPaths.get(chart)]){const e=edges[index],before=keep(state);if(state.chart!==e.from)throw Error('Bad witness path');
   if(e.phaseDelta===1)phaseAdvanceWitness(charts[e.from],charts[e.to],state.origin);
   state={chart:e.to,origin:state.origin+e.phaseDelta,permutation:e.permutation.map(i=>state.permutation[i]),history:[...state.history,index]};certificateEdges.push([before,keep(state)]);
  }exitStateIds.add(keep(state));}
 const certificate={states:[...certificateStates.values()],transitions:certificateEdges,entryStates:[entryId],exitStates:[...exitStateIds],requiredCells:all.map(i=>keys[i])};
 return {status:'phase-coherent-reference',candidate:copy(candidate),orientations,charts,edges,root,paths:Object.fromEntries(paths),exitPaths:Object.fromEntries(exitPaths),certificate,
  scope:'Phase-first local readers and explicit ordered realization advances. Geometry IDs and phase occurrences are separate; all five coefficients and all face spectral components are retained. Phase origins are unbounded and are not quotiented by coefficient holonomy. Outside-context coefficient retention is still a declared reference law, not a physical binding or stability derivation.'};
}
const cache=new Map();
export function selectPhaseAssembly(isotope){
 if(cache.has(isotope))return copy(cache.get(isotope));let candidates,retained=null;
 if(isotope==='nitrogen14')throw Error('No N-14 reference admitted in the current bounded isotope ansatz');
 if(isotope==='nitrogen15'){
  const r=compilePhaseAssembly(nitrogen15Reference.candidate,nitrogen15Reference.orientations);
  if(r.status!=='phase-coherent-reference'||r.candidate.electrons.length!==7||r.candidate.nucleus.filter(i=>domain.species[i]==='proton').length!==7||r.candidate.nucleus.filter(i=>domain.species[i]==='neutron').length!==8)throw Error('Invalid frozen N-15 reference');
  const old=selectPhaseAssembly('carbon13');
  if(!old.candidate.nucleus.every(i=>r.candidate.nucleus.includes(i))||!old.candidate.electrons.every(i=>r.candidate.electrons.includes(i))||Object.entries(old.candidate.types).some(([v,t])=>r.candidate.types[v]!==t)||!old.charts.every(a=>r.charts.some(b=>a.cell===b.cell&&a.species===b.species&&same(a.aliases,b.aliases))))throw Error('N-15 reference no longer retains selected C-13');
  r.retainedAssembly={isotope:'carbon13',nucleus:[...old.candidate.nucleus],electrons:[...old.candidate.electrons],addedProtons:r.candidate.nucleus.filter(i=>!old.candidate.nucleus.includes(i)&&domain.species[i]==='proton'),addedNeutrons:r.candidate.nucleus.filter(i=>!old.candidate.nucleus.includes(i)&&domain.species[i]==='neutron'),addedElectrons:r.candidate.electrons.filter(i=>!old.candidate.electrons.includes(i)),scope:'Retained C-13 geometry, roles and readers; no physical growth or stability law derived.'};
  auditPhaseAssembly(r);cache.set(isotope,r);return copy(r);
 }
 if(['lithium6','lithium7'].includes(isotope))candidates=searchLithiumAssemblies({allowNN:true,neutronCount:isotope==='lithium7'?4:3}).candidates;
 else if(isotope==='beryllium9')candidates=searchBeryllium9Assemblies().candidates;
 else if(isotope==='boron10')candidates=searchBoronAssemblies({neutronCount:5}).candidates;
 else if(isotope==='boron11')candidates=searchBoronAssemblies({neutronCount:6,retained:selectPhaseAssembly('boron10').candidate}).candidates;
 else if(['carbon12','carbon13'].includes(isotope))candidates=searchCarbonAssemblies({neutronCount:isotope==='carbon12'?6:7,retained:selectPhaseAssembly('boron11').candidate}).candidates;
 else if(['helium3','helium4'].includes(isotope)){
  const m=createHelium3Tunnel();for(let i=0;i<4;i++)m.step();const h=m.snapshot(),s=isotope==='helium3'?h:deriveHelium4Core(h);candidates=[geometryCandidate(s)];
 }else throw Error('Unknown phase assembly');
 const previousIsotope=({lithium7:'lithium6',beryllium9:'lithium7',boron11:'boron10',carbon12:'boron11',carbon13:'boron11'})[isotope];
 if(previousIsotope){
  retained=selectPhaseAssembly(previousIsotope);const old=retained.candidate;
  candidates=candidates.filter(c=>old.nucleus.every(i=>c.nucleus.includes(i))&&old.electrons.every(i=>c.electrons.includes(i))&&Object.entries(old.types).every(([v,t])=>c.types[v]===t));
 }
 for(const candidate of candidates)for(let orientations=0;orientations<2**candidate.interfaces.filter(e=>e.kind==='PN').length;orientations++){
  const r=compilePhaseAssembly(candidate,orientations);if(r.status==='phase-coherent-reference'){
   if(retained&&!retained.charts.every(a=>r.charts.some(b=>a.cell===b.cell&&a.species===b.species&&same(a.aliases,b.aliases))))continue;
   if(retained)r.retainedAssembly={isotope:previousIsotope,nucleus:[...retained.candidate.nucleus],electrons:[...retained.candidate.electrons],addedNeutrons:r.candidate.nucleus.filter(i=>!retained.candidate.nucleus.includes(i)&&domain.species[i]==='neutron'),addedProtons:r.candidate.nucleus.filter(i=>!retained.candidate.nucleus.includes(i)&&domain.species[i]==='proton'),addedElectrons:r.candidate.electrons.filter(i=>!retained.candidate.electrons.includes(i)),scope:'Retained geometry, roles and native readers; full phase certificate recompiled, not a claimed physical growth process.'};
   cache.set(isotope,r);return copy(r);
  }
 }
 throw Error('No phase-coherent reference assembly in the tested domain');
}
export function auditPhaseAssembly(reference){
 const r=reference,boundary=r.charts[r.root],contacts=auditAssemblyContacts(r);
 if(contacts.missing.length)throw Error('Unwitnessed physical contact');
 if(boundary?.cell!==0||boundary.species!=='proton'||Object.entries(rootBindings).some(([name,vertex])=>boundary.aliases[name]!==vertex))throw Error('Changed native root marking');
 for(const e of r.edges){
  const a=r.charts[e.from],b=r.charts[e.to];
  for(const c of [a,b]){const frame=phaseFrame(c),vertices=[...frame.window,frame.context].map(o=>o.vertex).sort();if(!same(vertices,lattice.cells[c.cell].map(v=>'vertex-'+v).sort()))throw Error('Phase frame does not bind its actual tetrahedron');}
  if(e.phaseDelta===1){if(!['reader-phase-advance','NN-phase-advance'].includes(e.kind)||(e.kind==='reader-phase-advance')!==(a.cell===b.cell))throw Error('Wrong phase interface kind');const w=phaseAdvanceWitness(a,b);if(!same(w.permutation,e.permutation)||!same(w,e.witness))throw Error('Phase advance witness or full-carrier map was changed');}
  else {
   if(e.phaseDelta!==0||!['PN','inverse-PN','NE'].includes(e.kind))throw Error('Unwitnessed phase transition');
   const expected=e.kind==='NE'?[0,4,2,3,1]:[3,1,2,0,4];if(!same(e.permutation,expected))throw Error('Changed native full-carrier map');
   if(referenceCarrierMarks.some(name=>a.aliases[name]!==b.aliases[name]))throw Error('Native transport lost a retained reference mark');
   const inverse=e.kind==='inverse-PN',from=phaseFrame(inverse?b:a),to=phaseFrame(inverse?a:b);
   if(auditPhaseCombination([from,to],[{from:from.id,to:to.id,kind:inverse?'PN':e.kind,identification:'same-occurrence',vertices:to.window.map(o=>o.vertex)}]).status!=='native-phase-compatible')throw Error('Invalid native phase interface');
  }
 }
 const states=new Map(r.certificate.states.map(s=>[s.id,s]));
 const entry=states.get(r.certificate.entryStates[0]);if(r.certificate.entryStates.length!==1||!entry||entry.chart!==r.root||entry.origin!==0||entry.history.length||!same(entry.permutation,identityPermutation))throw Error('Changed entry boundary');
 if(!same([...r.certificate.requiredCells].sort(),[...r.candidate.nucleus,...r.candidate.electrons].map(i=>keys[i]).sort()))throw Error('A required carrier was omitted');
 for(const id of r.certificate.exitStates)if(r.charts[states.get(id)?.chart]?.species!=='electron')throw Error('Non-electron terminal boundary');
 for(const s of states.values())if(s.cell!==keys[r.charts[s.chart].cell]||!same(s.frame,phaseFrame(r.charts[s.chart],s.origin)))throw Error('Phase indices or geometric bindings changed in the combination');
 for(const [from,to] of r.certificate.transitions){const a=states.get(from),b=states.get(to),index=b.history.at(-1),e=r.edges[index];
  if(!e||a.chart!==e.from||b.chart!==e.to||!same(b.history,[...a.history,index])||b.origin!==a.origin+e.phaseDelta||!same(b.permutation,e.permutation.map(i=>a.permutation[i])))throw Error('Combination skipped a phase or lost its history/carrier');
  if(e.phaseDelta)phaseAdvanceWitness(r.charts[e.from],r.charts[e.to],a.origin);
 }
 const coverage=auditStateCoverage(r.certificate);if(coverage.fromEntryStateIds.length!==states.size)throw Error('Unrooted phase-history state');if(coverage.status!=='covered'||!coverage.allEnteredStatesReachExit)throw Error('Incomplete phase-bearing entry/exit witnesses');
 return {status:'phase-coherent-reference',coverage,contacts,phaseStateCount:states.size,absoluteOriginsRetained:true,allFiveSlotsRetained:true,physicalBindingLawDerived:false};
}
export function createPhaseAssembly(isotope,{coefficients=null}={}){
 const r=selectPhaseAssembly(isotope),audit=auditPhaseAssembly(r),input=coefficients??[...windowModeCoefficients({branch:'positive',phaseExponent:0}),[0,0],[0,0]];
 applyPhasePermutation(input,identityPermutation);
 const ids=[...(r.candidate.displayOrder??[...r.candidate.nucleus,...r.candidate.electrons])],identity=Object.freeze({id:'id'});
 const views=ids.map(cell=>{const chart=r.charts.map((c,i)=>({c,i,path:r.paths[i]})).filter(x=>x.c.cell===cell).sort((a,b)=>a.path.reduce((s,i)=>s+r.edges[i].phaseDelta,0)-b.path.reduce((s,i)=>s+r.edges[i].phaseDelta,0)||a.path.length-b.path.length)[0].i,path=r.paths[chart];let origin=0,value=copy(input);for(const i of path){const e=r.edges[i];origin+=e.phaseDelta;value=applyPhasePermutation(value,e.permutation);}return {chart,origin,history:[...path],frame:phaseFrame(r.charts[chart],origin),coefficients:value,spectrum:spectralReadout(r.charts[chart].species,value)};});
 const ordered=ids.map((cell,i)=>({cell,view:views[i]})).sort((a,b)=>a.view.origin-b.view.origin||a.view.history.length-b.view.history.length||['proton','neutron','electron'].indexOf(a.view.frame.species)-['proton','neutron','electron'].indexOf(b.view.frame.species)||a.cell-b.cell);
 ids.splice(0,ids.length,...ordered.map(x=>x.cell));views.splice(0,views.length,...ordered.map(x=>x.view));
 const items=ids.map((cell,i)=>{const frame=views[i].frame,vertices=lattice.cells[cell].map(v=>[...lattice.nodes[v].address]);return {key:keys[cell],kind:'tetrahedron',species:frame.species,vertices,components:[copy(vertices)],faces:faces.map(f=>f.map(j=>[...vertices[j]])),center:vertices[0].map((_,j)=>vertices.reduce((s,p)=>s+p[j]/4,0)),nodes:lattice.cells[cell].map(v=>'vertex-'+v),window:frame.window.map(o=>o.vertex),continuation:frame.context.vertex};});
 const bindings=Object.fromEntries([...new Set(ids.flatMap(i=>lattice.cells[i]))].map(v=>['vertex-'+v,[...lattice.nodes[v].address]]));
 function snapshot(){return {atomTrial:isotope,status:'complete',identity,items:copy(items),bindings:copy(bindings),history:[],events:[],added:0,candidates:[],counts:Object.fromEntries(['proton','neutron','electron'].map(s=>[s,items.filter(i=>i.species===s).length])),construction:{kind:'phase-first-whole-assembly',betweenElementPrefixRequired:false},phaseAudit:{...copy(audit),scope:r.scope},phaseViews:copy(views),phaseCertificate:copy(r.certificate),phaseEdges:copy(r.edges),entry:{point:[...items[0].center]},exit:{point:null,reached:false},tunnel:{position:0,scope:r.scope}};}
 return {snapshot,reference:()=>copy(r),step:()=>({...snapshot(),committed:false})};
}
