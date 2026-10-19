import {lattice} from './simplex-model.mjs';
import {makeLatticeItem,itemKey} from './lattice-items.mjs';
import {nativePhaseFrame,auditPhaseCombination} from './phase-discipline-model.mjs';
import {createWindowConstruction,windowProtocol} from './window-construction-model.mjs';
import {transportCarrierCoefficients,referenceCarrierMarks} from './deuterium-tunnel-model.mjs';
import {auditStateCoverage} from './fiber-coverage-model.mjs';
import {assemblyDomain,lithiumNNHypothesis} from './lithium6-assembly-model.mjs';
const copy=x=>structuredClone(x),equal=(a,b)=>JSON.stringify(a)===JSON.stringify(b),sort=a=>[...a].sort((a,b)=>a-b),idPermutation=[0,1,2,3,4];
const active={proton:[0,1,2],neutron:[1,2,3],electron:[3,2,4]};
export function applyLithiumReferenceEdge(coefficients,edge,direction=1){
 if(![1,-1].includes(direction)||!Array.isArray(coefficients)||coefficients.length!==5||coefficients.some(z=>!Array.isArray(z)||z.length!==2||z.some(x=>!Number.isFinite(x)))||!equal(sort(edge.permutation),idPermutation))throw Error('Finite five-slot carrier, bijective reference edge and signed direction required');
 const p=direction===1?edge.permutation:edge.permutation.map((_,i)=>edge.permutation.indexOf(i));return p.map(i=>[...coefficients[i]]);
}
function nativePermutation(event){return transportCarrierCoefficients(idPermutation.map(i=>[i,0]),event).map(z=>z[0]);}
function validate(candidate,domain){
 const {nucleus,electrons,types,interfaces}=candidate,all=[...nucleus,...electrons];
 if(nucleus.length!==6||electrons.length!==3||new Set(all).size!==9||!nucleus.includes(0)||all.some(i=>!Number.isInteger(i)||!lattice.cells[i])||nucleus.filter(i=>domain.species[i]==='proton').length!==3||electrons.some(i=>domain.species[i]!=='neutron'))throw Error('Expected a whole 3P/3N/3e assembly in the bounded domain');
 for(const i of all)if(lattice.cells[i].some(v=>!['M','C'].includes(types[v]))||lattice.cells[i].filter(v=>types[v]==='M').length!==2)throw Error('Globally consistent MMCC types required');
 const actual=[];for(const i of all)for(const e of domain.adjacency[i])if(i<e.to&&all.includes(e.to)){
  const a=electrons.includes(i)?'electron':domain.species[i],b=electrons.includes(e.to)?'electron':domain.species[e.to];
  if(a===b&&a!=='neutron'||[a,b].includes('electron')&&[a,b].includes('proton'))throw Error('Unadmitted assembly face contact');
  const kind=[a,b].includes('electron')?'NE':a===b?'NN':'PN',m=e.face.filter(v=>types[v]==='M').length;if(m!==(kind==='PN'?2:1))throw Error('Wrong interface C/M type');
  actual.push([i,e.to,kind,sort(e.face)]);
 }
 const normalized=interfaces.map(e=>[Math.min(e.from,e.to),Math.max(e.from,e.to),e.kind,sort(e.face)]);
 if(!equal(actual.sort(),normalized.sort()))throw Error('Interface ledger does not match actual face contacts');
 const seen=new Set([0]),queue=[0];for(let i=0;i<queue.length;i++)for(const e of domain.adjacency[queue[i]])if(nucleus.includes(e.to)&&!seen.has(e.to)){seen.add(e.to);queue.push(e.to);}
 if(seen.size!==6||electrons.some(i=>!domain.adjacency[i].some(e=>nucleus.includes(e.to))))throw Error('Disconnected assembly');
}
export function compileLithium6Reference(candidate,{nnRule,orientations=0}={}){
 if(nnRule!==lithiumNNHypothesis)throw Error('Explicit NN reference hypothesis required');
 const domain=assemblyDomain();validate(candidate,domain);
 const pn=candidate.interfaces.filter(e=>e.kind==='PN');if(!Number.isInteger(orientations)||orientations<0||orientations>=2**pn.length)throw Error('Invalid reader orientation mask');
 const charts=[],edges=[],packets=[];
 function edge(from,to,permutation,kind,conditional=false){edges.push({from,to,permutation:[...permutation],kind,conditional});}
 for(const [index,link] of pn.entries()){
  const p=domain.species[link.from]==='proton'?link.from:link.to,n=p===link.from?link.to:link.from,component=lattice.assembly.components[p];
  const seed=makeLatticeItem('tetrahedron',component.origin,component.transform.kind==='inversion'),ms=sort(link.face.filter(v=>candidate.types[v]==='M'));if(orientations&(1<<index))ms.reverse();
  const local={C0:lattice.cells[p].find(v=>!link.face.includes(v)),M0:ms[0],C1:link.face.find(v=>candidate.types[v]==='C'),M1:ms[1]};
  const model=createWindowConstruction({seed,bindings:Object.fromEntries(Object.entries(local).map(([k,v])=>[k,lattice.nodes[v].address]))});model.step();const packet=model.step();
  if(packet.status!=='complete'||packet.items[1].key!==itemKey(lattice.cells[n].map(v=>lattice.nodes[v].address)))throw Error('PN reference packet disagrees with the assembly');
  const aliases=Object.fromEntries(referenceCarrierMarks.map(name=>[name,lattice.nodes.findIndex(v=>equal(v.address,packet.bindings[name]))]));
  const e=lattice.cells.findIndex(cell=>itemKey(cell.map(v=>lattice.nodes[v].address))===packet.items[2].key);
  const pChart=charts.length;charts.push({id:pChart,cell:p,species:'proton',aliases:copy(aliases),window:['C0','M0','C1'].map(k=>aliases[k])});
  const nChart=charts.length;charts.push({id:nChart,cell:n,species:'neutron',aliases:copy(aliases),window:['M0','C1','M1'].map(k=>aliases[k])});
  edge(pChart,nChart,nativePermutation(packet.events[0]),'PN');
  if(candidate.electrons.includes(e)){const eChart=charts.length;charts.push({id:eChart,cell:e,species:'electron',aliases:copy(aliases),window:['M1','C1','C2'].map(k=>aliases[k])});edge(nChart,eChart,nativePermutation(packet.events[1]),'NE');}
  packets.push({p,n,e,pChart,nChart,packet});
 }
 for(let i=0;i<charts.length;i++)for(let j=i+1;j<charts.length;j++)if(charts[i].cell===charts[j].cell&&charts[i].species!=='electron'){
  const a=charts[i],b=charts[j];
  if(a.species==='proton')edge(i,j,[2,1,0,3,4],'proton-reader-reference',true);
  else edge(i,j,a.aliases.M0===b.aliases.M0?idPermutation:[0,3,2,1,4],'shared-neutron-reference',true);
 }
 for(const link of candidate.interfaces.filter(e=>e.kind==='NN')){
  let admitted=0;
  for(const a of charts.filter(c=>c.cell===link.from&&c.species==='neutron'))for(const b of charts.filter(c=>c.cell===link.to&&c.species==='neutron')){
   if(a.aliases.C1!==b.aliases.C1||a.aliases.C2!==b.aliases.C2)continue;
   const m=link.face.find(v=>candidate.types[v]==='M');if(!((a.aliases.M1===m&&b.aliases.M0===m)||(a.aliases.M0===m&&b.aliases.M1===m)))continue;
   const source=a.aliases.M1===m?a:b,target=source===a?b:a,packet=packets.find(p=>p.nChart===source.id);
   if(packet.e!==target.cell)throw Error('NN does not cross the native MCC continuation face');
   // Fix ALL THREE shared-face coefficients: M (3 -> 1), C1 (2), C2 (4).
   // The departing M coefficient enters the new M slot. The outside C0 slot
   // is identified by reference hypothesis, not by geometric coincidence.
   edge(source.id,target.id,[0,3,2,1,4],'NN-reference',true);admitted++;
  }
  if(!admitted)return {status:'rejected-reader-choice',reason:'no-reversed-edge-NN-reader',orientations};
 }
 if(candidate.electrons.some(e=>!charts.some(c=>c.cell===e)))return {status:'rejected-reader-choice',reason:'selected-electron-without-native-NE-reader',orientations};
 const root=charts.find(c=>c.cell===0&&c.species==='proton').id,adj=charts.map(()=>[]);
 edges.forEach((e,i)=>{adj[e.from].push({edge:i,direction:1,to:e.to});if(e.kind!=='NE')adj[e.to].push({edge:i,direction:-1,to:e.from});});
 const states=[],transitions=[],byId=new Map(),stateId=(chart,p)=>chart+':'+p.join('');
 function admit(chart,permutation){const id=stateId(chart,permutation);if(!byId.has(id)){const s={id,chart,cell:itemKey(lattice.cells[charts[chart].cell].map(v=>lattice.nodes[v].address)),permutation:[...permutation]};byId.set(id,s);states.push(s);}return id;}
 const entry=admit(root,idPermutation);
 for(let i=0;i<states.length;i++){
  if(states.length>120*charts.length)throw Error('Reference permutation cover failed to close');
  const s=states[i];for(const hop of adj[s.chart]){const e=edges[hop.edge],p=applyLithiumReferenceEdge(s.permutation.map(x=>[x,0]),e,hop.direction).map(z=>z[0]);transitions.push([s.id,admit(hop.to,p)]);}
 }
 const exitStates=states.filter(s=>charts[s.chart].species==='electron').map(s=>s.id),requiredCells=[...candidate.nucleus,...candidate.electrons].map(i=>itemKey(lattice.cells[i].map(v=>lattice.nodes[v].address)));
 const coverage=auditStateCoverage({states,transitions,entryStates:[entry],exitStates,requiredCells});
 if(coverage.status!=='covered'||!coverage.allEnteredStatesReachExit)return {status:'rejected-reader-choice',reason:'full-state-coverage-failed',orientations};
 const rootHolonomies=states.filter(s=>s.chart===root).map(s=>s.permutation);
 // Extract a closed root-based walk from a non-tree edge. This is reader
 // navigation on a completed assembly, never a carrier construction history.
 const paths=new Map([[root,[]]]),treeEdges=new Set(),queue=[root];
 for(let i=0;i<queue.length;i++)for(const h of adj[queue[i]])if(charts[h.to].species!=='electron'&&!paths.has(h.to)){paths.set(h.to,[...paths.get(queue[i]),h]);treeEdges.add(h.edge);queue.push(h.to);}
 const chord=edges.findIndex((e,i)=>e.kind!=='NE'&&!treeEdges.has(i));let tour=[];
 if(chord>=0){const e=edges[chord];tour=[...paths.get(e.from),{edge:chord,direction:1,to:e.to},...[...paths.get(e.to)].reverse().map(h=>({edge:h.edge,direction:-h.direction,to:edges[h.edge][h.direction===1?'from':'to']}))];}
 const covered=new Set([root,...tour.map(h=>h.to)]);
 for(const [node,path] of paths)if(!covered.has(node)){
  // Visit off-cycle branches by a path and its exact inverse. This adds no
  // holonomy, but keeps whole-assembly navigation from hiding a dangling arm.
  tour.push(...path,...[...path].reverse().map(h=>({edge:h.edge,direction:-h.direction,to:edges[h.edge][h.direction===1?'from':'to']})));
  path.forEach(h=>covered.add(h.to));
 }
 if(covered.size!==charts.filter(c=>c.species!=='electron').length)throw Error('Unvisited nuclear reader');
 let holonomy=[...idPermutation];for(const h of tour)holonomy=applyLithiumReferenceEdge(holonomy.map(x=>[x,0]),edges[h.edge],h.direction).map(z=>z[0]);
 let value=[...idPermutation],order=0;do{value=holonomy.map(i=>value[i]);order++;}while(!equal(value,idPermutation)&&order<=120);
 const phaseFrames=charts.map(c=>{const spec=windowProtocol.find(p=>p.species===c.species),vertices=[...c.window,lattice.cells[c.cell].find(v=>!c.window.includes(v))];return nativePhaseFrame(String(c.id),c.species,Object.fromEntries([...spec.window,spec.continuation].map((name,i)=>[name,'vertex-'+vertices[i]])));});
 const phaseInterfaces=edges.map(e=>({from:String(e.from),to:String(e.to),kind:e.kind,identification:charts[e.from].cell===charts[e.to].cell?'unproved-reader-comparison':'same-occurrence',vertices:lattice.cells[charts[e.from].cell].filter(v=>lattice.cells[charts[e.to].cell].includes(v)).map(v=>'vertex-'+v)}));
 const phaseAudit=auditPhaseCombination(phaseFrames,phaseInterfaces);
 return {status:'reference-algebra-only',phaseAudit,viewerAdmitted:false,orientations,nnRule,charts,edges,root,states,transitions,entryStates:[entry],exitStates,coverage,rootHolonomies,tour,holonomy,operatorOrder:order,
  scope:'WITHDRAWN: phase admission failed. Geometry and reference coefficient algebra only, not a valid Li-6 realization. Not a He-4 growth prefix. Native PN/NE operators plus the existing conditional P/shared-N comparisons and an additional NN MCC interface hypothesis. NN fixes the three shared-face coefficients and carries all five slots; its outside context identification remains assumed. Finite holonomy is retained, not forced to identity. Neither physical stability nor a unique grammar is derived.'};
}
