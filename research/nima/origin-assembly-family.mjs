import {phaseUniverse} from './origin-bounded-assemblies.mjs';

// Exact reduced ordered Boolean diagrams; models are selected packet sets.
// This represents the complete configuration family without mistaking an
// explicit-list resource stop for phase completeness.
export class BooleanDiagram {
 constructor(variables,{maxNodes=1000000}={}){this.variables=variables;this.maxNodes=maxNodes;this.nodes=[[variables,0,0],[variables,1,1]];this.unique=new Map();this.cache=new Map();this.notCache=new Map([[0,1],[1,0]]);}
 node(v,lo,hi){if(lo===hi)return lo;const k=v+','+lo+','+hi;if(this.unique.has(k))return this.unique.get(k);if(this.nodes.length>=this.maxNodes)throw Error('explicit-symbolic-node-resource-limit');const id=this.nodes.length;this.nodes.push([v,lo,hi]);this.unique.set(k,id);return id;}
 variable(v){return this.node(v,0,1);}
 not(a){if(this.notCache.has(a))return this.notCache.get(a);const [v,l,h]=this.nodes[a],r=this.node(v,this.not(l),this.not(h));this.notCache.set(a,r);return r;}
 binary(kind,a,b){
  if(a>b)[a,b]=[b,a];
  if(kind==='and'){if(!a)return 0;if(a===1)return b;if(a===b)return a;}
  else{if(b===1||a===1)return 1;if(!a)return b;if(a===b)return a;}
  const key=kind+':'+a+':'+b;if(this.cache.has(key))return this.cache.get(key);
  const v=Math.min(this.nodes[a][0],this.nodes[b][0]),[al,ah]=this.nodes[a][0]===v?this.nodes[a].slice(1):[a,a],[bl,bh]=this.nodes[b][0]===v?this.nodes[b].slice(1):[b,b];
  const r=this.node(v,this.binary(kind,al,bl),this.binary(kind,ah,bh));this.cache.set(key,r);return r;
 }
 and(...xs){return xs.reduce((a,b)=>this.binary('and',a,b),1);}
 or(...xs){return xs.reduce((a,b)=>this.binary('or',a,b),0);}
 implies(a,b){return this.or(this.not(a),b);}
 count(root){const memo=new Map(),go=(id,level)=>{if(id<2)return id?1n<<BigInt(this.variables-level):0n;const [v,l,h]=this.nodes[id];if(!memo.has(id))memo.set(id,go(l,v+1)+go(h,v+1));return (1n<<BigInt(v-level))*memo.get(id);};return go(root,0);}
 accepts(root,selectedVariables){const s=new Set(selectedVariables);let n=root;while(n>1){const [v,l,h]=this.nodes[n];n=s.has(v)?h:l;}return n===1;}
 models(root,limit=1000){const out=[],chosen=[];const visit=(id,level)=>{if(!id||out.length>=limit)return;if(level===this.variables){if(id===1)out.push([...chosen]);return;}const v=this.nodes[id][0];if(id===1||v>level){visit(id,level+1);chosen.push(level);visit(id,level+1);chosen.pop();}else{visit(this.nodes[id][1],level+1);chosen.push(level);visit(this.nodes[id][2],level+1);chosen.pop();}};visit(root,0);return out;}
 maximumSelection(root){const memo=new Map(),go=(id,level)=>{if(id===0)return null;if(id===1)return Array.from({length:this.variables-level},(_,i)=>i+level);const [v,l,h]=this.nodes[id];if(!memo.has(id)){const a=go(l,v+1),b=go(h,v+1),hi=b===null?null:[v,...b];memo.set(id,a===null?hi:hi===null?a:hi.length>a.length?hi:a);}const best=memo.get(id);return best===null?null:[...Array.from({length:v-level},(_,i)=>i+level),...best];};return go(root,0);}
}

function components(universe){
 const {rules,packets,operations}=universe,adj=new Map(packets.map(p=>[p,[]]));
 for(const i of operations){const o=rules.operations[i];if(o.phaseDelta===0)adj.get(o.source).push(o.target);}
 const number=new Map(),low=new Map(),stack=[],on=new Set(),groups=[];let next=0;
 const visit=p=>{number.set(p,next);low.set(p,next++);stack.push(p);on.add(p);for(const q of adj.get(p)){if(!number.has(q)){visit(q);low.set(p,Math.min(low.get(p),low.get(q)));}else if(on.has(q))low.set(p,Math.min(low.get(p),number.get(q)));}if(low.get(p)===number.get(p)){const c=[];let q;do{q=stack.pop();on.delete(q);c.push(q);}while(q!==p);groups.push(c.sort((a,b)=>a-b));}};
 for(const p of packets)if(!number.has(p))visit(p);
 const which=new Map();groups.forEach((g,i)=>g.forEach(p=>which.set(p,i)));
 for(const g of groups){if(g.length>2)throw Error('New zero-grade component requires selected-subset connectivity proof');if(g.length===2&&(!adj.get(g[0]).includes(g[1])||!adj.get(g[1]).includes(g[0])))throw Error('Zero-grade pair not mutually connected');}
 const successors=groups.map(()=>new Set()),indegree=groups.map(()=>0);
 for(const i of operations){const e=rules.operations[i],a=which.get(e.source),b=which.get(e.target);if(a!==b&&!successors[a].has(b)){successors[a].add(b);indegree[b]++;}}
 const q=indegree.flatMap((n,i)=>n?[]:[i]);for(let k=0;k<q.length;k++)for(const t of successors[q[k]])if(--indegree[t]===0)q.push(t);
 if(q.length!==groups.length)throw Error('Phase/NE condensation is not acyclic');
 return {groups,which,topological:q};
}

export function buildPhaseFamily({maxOrigin,maxDiagramNodes=1000000,sewingAssertions=null}={}){
 if(sewingAssertions!==null)throw Error('Additional sewing assertions require a family/key extension; unasserted global state sewing is not inferred');
 const universe=phaseUniverse({maxOrigin});if(!universe.complete)throw Error('Incomplete packet universe');const {rules}=universe,c=components(universe);
 const variablePackets=[...universe.packets].sort((a,b)=>rules.packets[a].origin-rules.packets[b].origin||a-b),variableOf=new Map(variablePackets.map((p,i)=>[p,i]));
 const diagram=new BooleanDiagram(variablePackets.length,{maxNodes:maxDiagramNodes}),x=new Map(variablePackets.map(p=>[p,diagram.variable(variableOf.get(p))]));
 let valid= x.get(rules.root);const conflicts=[];
 // Every compatibility guard is unary or pairwise: occupancy, role agreement,
 // and complete-face contact. Rootedness is supplied by the component clauses.
 for(let a=0;a<variablePackets.length;a++)for(let b=a+1;b<variablePackets.length;b++){
  const p=variablePackets[a],q=variablePackets[b],d=rules.describe([p,q]);if(!d.valid){conflicts.push({packets:[p,q],reason:d.reason});valid=diagram.and(valid,diagram.not(diagram.and(x.get(p),x.get(q))));}
 }
 const supports=[];
 for(let component=0;component<c.groups.length;component++){
  const group=c.groups[component],active=diagram.or(...group.map(p=>x.get(p)));
  if(group.includes(rules.root))continue;
  const incoming=universe.operations.filter(i=>{const e=rules.operations[i];return c.which.get(e.target)===component&&c.which.get(e.source)!==component;});
  const anchor=diagram.or(...incoming.map(i=>{const e=rules.operations[i];return diagram.and(x.get(e.source),x.get(e.target));}));
  valid=diagram.and(valid,diagram.implies(active,anchor));supports.push({component,incoming});
 }
 let exit=valid;
 const exitPackets=variablePackets.filter(p=>rules.charts[rules.packets[p].chart].species==='electron');
 exit=diagram.and(exit,diagram.or(...exitPackets.map(p=>x.get(p))));
 // Dual support on the same acyclic condensation gives every selected packet
 // a path to an E. Unselected cached possibilities are never obligations.
 for(let component=0;component<c.groups.length;component++){
  const group=c.groups[component];if(group.every(p=>exitPackets.includes(p)))continue;
  const outgoing=universe.operations.filter(i=>{const e=rules.operations[i];return c.which.get(e.source)===component&&c.which.get(e.target)!==component;});
  const escape=diagram.or(...outgoing.map(i=>{const e=rules.operations[i];return diagram.and(x.get(e.source),x.get(e.target));}));
  exit=diagram.and(exit,diagram.implies(diagram.or(...group.map(p=>x.get(p))),escape));
 }
 const bodies=new Map();for(const p of variablePackets){const ch=rules.charts[rules.packets[p].chart],key=ch.cell+':'+ch.species;if(!bodies.has(key))bodies.set(key,{cell:ch.cell,species:ch.species,packets:[]});bodies.get(key).packets.push(p);}
 const list=[...bodies.values()],contacts=[];
 for(let i=0;i<list.length;i++)for(let j=i+1;j<list.length;j++){
  const a=list[i],b=list[j];if(a.cell===b.cell)continue;
  if(rules.geometry.cells[a.cell].vertices.filter(v=>rules.geometry.cells[b.cell].vertices.includes(v)).length!==3)continue;
  const present=diagram.and(diagram.or(...a.packets.map(p=>x.get(p))),diagram.or(...b.packets.map(p=>x.get(p))));
  const links=universe.operations.filter(k=>{const op=rules.operations[k];return a.packets.includes(op.source)&&b.packets.includes(op.target)||b.packets.includes(op.source)&&a.packets.includes(op.target);});
  const witness=diagram.or(...links.map(k=>{const e=rules.operations[k];return diagram.and(x.get(e.source),x.get(e.target));}));
  exit=diagram.and(exit,diagram.implies(present,witness));contacts.push({bodies:[i,j],links});
 }
 const mapModel=vars=>vars.map(i=>variablePackets[i]).sort((a,b)=>a-b);
 return {schema:'marici.nima.origin-assembly-family.v1',complete:true,maxOrigin,universe,components:c,variablePackets,diagram,validRoot:valid,exitRoot:exit,
  conflicts,supports,bodies:list,contacts,
  summary:{maxOrigin,packetUniverse:variablePackets.length,allowedOperations:universe.operations.length,zeroGradeComponents:c.groups.length,
   compatibleConfigurations:diagram.count(valid).toString(),selectedRecordExitCertificates:diagram.count(exit).toString(),diagramNodes:diagram.nodes.length,
   potentialOccupiedCells:new Set(list.map(b=>b.cell)).size,potentialNuclearCells:new Set(list.filter(b=>b.species!=='electron').map(b=>b.cell)).size},
  accepts:(packets,{exits=false}={})=>packets.every(p=>variableOf.has(p))&&diagram.accepts(exits?exit:valid,packets.map(p=>variableOf.get(p))),
  models:({exits=false,limit=1000}={})=>diagram.models(exits?exit:valid,limit).map(mapModel),
  maximumRecordWitness:({exits=false}={})=>{const v=diagram.maximumSelection(exits?exit:valid);return v===null?null:mapModel(v);},
  representation:'Exact Boolean family plus allowed source-operation schemas. Assignments are compatible selected packet sets; all ordered construction/revisit histories remain paths, not a finite word list. Exit certificates are local transport/reachability only, not a global coupled-field sewing theorem.'};
}

export function reconstructPhaseSelection(family,packets){
 if(!family.accepts(packets))throw Error('Not an admitted phase-bounded construction selection');
 const {rules,operations}=family.universe,chosen=new Set(packets),reached=new Set([rules.root]),word=[],prefixes=[[rules.root]];
 for(let changed=true;changed;){changed=false;for(const i of operations){const e=rules.operations[i];if(reached.has(e.source)&&chosen.has(e.target)&&!reached.has(e.target)){
   reached.add(e.target);word.push(i);prefixes.push([...reached].sort((a,b)=>a-b));changed=true;
  }}}
 if(reached.size!==chosen.size)throw Error('Boolean root-support model failed actual reachability');
 for(const ids of prefixes)if(!rules.describe(ids).valid)throw Error('Symbolic model has no compatible construction prefix');
 return {word,prefixes,grade:Math.max(...packets.map(p=>rules.packets[p].origin)),minimumOperations:word.length,sourceOperationCountIsNotBudget:true};
}
