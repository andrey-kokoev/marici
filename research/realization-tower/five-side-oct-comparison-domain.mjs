import {buildPESymmetricSector} from '../strominger/pe-symmetric-sector.mjs';
import {buildFiveSideOctRoutingObligations} from './five-side-oct-routing-obligations.mjs';
const centre=vs=>[0,1,2,3].map(i=>vs.reduce((s,p)=>s+p[i]/vs.length,0));
const pairKey=(a,b)=>JSON.stringify([a,b]);
const pathKey=nodes=>JSON.stringify(nodes);
const sort=xs=>[...xs].sort((a,b)=>a.id.localeCompare(b.id));
const normal=f=>[0,1,2,3].find(i=>f.vertices.every(p=>p[i]===f.vertices[0][i]));

// Enumerate the whole finite incidence object first. This is a comparison
// DOMAIN, not a selected route, nor a claim that every parallel pair must be
// identified. Only the sourced entry-prefix comparisons are marked required.
export function buildFiveSideOctComparisonDomain(sector=buildPESymmetricSector(2),{readingIds=null,maxLength=4}={}){
 if(![3,4].includes(maxLength))throw Error('Diagnostic path lengths supported: 3 or 4');
 const sites=buildFiveSideOctRoutingObligations(sector),cells=sort(sector.cells),byCell=new Map(cells.map(c=>[c.id,c])),byFace=new Map(sector.faces.map(f=>[f.id,f]));
 const readings=sites.readings.filter(r=>!readingIds||readingIds.includes(r.id)).map(reading=>{
  const height=id=>reading.sign*reading.axis.reduce((s,x,i)=>s+x*(centre(byCell.get(id).vertices)[i]-sector.centre[i]),0)/2;
  const arrows=sort(sector.faces.filter(f=>f.owners.length===2).map(f=>{
   const [a,b]=[...f.owners].sort((a,b)=>height(b)-height(a));
   if(Math.abs(height(a)-height(b)-.5)>1e-9)throw Error('Shared interface is not between consecutive cell-centre layers');
   return {id:f.id,from:a,to:b,axis:normal(f)};
  }));
  const outgoing=new Map(cells.map(c=>[c.id,[]]));for(const a of arrows)outgoing.get(a.from).push(a);
  const twoPaths=new Map(),threePaths=new Map();
  for(const a of arrows)for(const b of outgoing.get(a.to)){
   const k=pairKey(a.from,b.to);if(!twoPaths.has(k))twoPaths.set(k,[]);
   twoPaths.get(k).push({id:pathKey([a.from,a.to,b.to]),cells:[a.from,a.to,b.to],arrows:[a.id,b.id],axes:[a.axis,b.axis]});
   for(const c of outgoing.get(b.to)){
    const k3=pairKey(a.from,c.to);if(!threePaths.has(k3))threePaths.set(k3,[]);
    threePaths.get(k3).push({id:pathKey([a.from,a.to,b.to,c.to]),cells:[a.from,a.to,b.to,c.to],arrows:[a.id,b.id,c.id]});
    if(maxLength===4)for(const d of outgoing.get(c.to)){
     const k4=pairKey(a.from,d.to);if(!threePaths.has(k4))threePaths.set(k4,[]);
     threePaths.get(k4).push({id:pathKey([a.from,a.to,b.to,c.to,d.to]),cells:[a.from,a.to,b.to,c.to,d.to],arrows:[a.id,b.id,c.id,d.id]});
    }
   }
  }
  const required=new Map(reading.comparisons.map(c=>[pairKey(c.sharedReference,c.cell),c]));
  const comparisons=sort([...twoPaths].filter(([,ps])=>ps.length>1).map(([id,paths])=>{
   const [source,target]=JSON.parse(id),binding=required.get(id),ordered=sort(paths);
   if(binding&&[...binding.inputs].sort().join('|')!==ordered.map(p=>p.cells[1]).sort().join('|'))throw Error('Prefix comparison lost an operand');
   return {id,source,target,sourceRole:byCell.get(source).role,targetRole:byCell.get(target).role,alternatives:ordered,
    status:binding?'source-required-prefix-incidence; map-unbound':'potential-comparison; authorization-unbound',sourceRequirement:binding?.id??null,comparisonMap:null,fillingWitness:null};
  }));
  if(required.size!==comparisons.filter(c=>c.sourceRequirement).length)throw Error('Prefix comparison absent from global domain');
  const byComparison=new Map(comparisons.map(c=>[c.id,c]));
  const overlaps=sort([...threePaths].filter(([,ps])=>ps.length>1).map(([id,ps])=>{
   const paths=sort(ps),moves=[];
   for(let i=0;i<paths.length;i++)for(let j=i+1;j<paths.length;j++){
    const a=paths[i],b=paths[j];
    // Change exactly one intermediate presentation, retaining both contexts.
    // This names a comparison boundary, without inventing its comparison map.
    for(let position=1;position<a.cells.length-1;position++)if(a.cells[position]!==b.cells[position]&&a.cells.every((c,k)=>k===position||c===b.cells[k])){
     const comparison=pairKey(a.cells[position-1],a.cells[position+1]);
     if(!byComparison.has(comparison))throw Error('Unretained comparison boundary');
     moves.push({from:a.id,to:b.id,comparison,position,contextBefore:a.arrows.slice(0,position-1),contextAfter:a.arrows.slice(position+1),witness:null});
    }
   }
   const adj=new Map(paths.map(p=>[p.id,[]]));for(let i=0;i<moves.length;i++){adj.get(moves[i].from).push({to:moves[i].to,edge:i});adj.get(moves[i].to).push({to:moves[i].from,edge:i});}
   const seen=new Set(),treeEdges=new Set(),treeAdj=new Map(paths.map(p=>[p.id,[]]));let components=0;
   for(const p of paths)if(!seen.has(p.id)){
    components++;const queue=[p.id];seen.add(p.id);
    for(let i=0;i<queue.length;i++)for(const {to,edge} of adj.get(queue[i]))if(!seen.has(to)){
     seen.add(to);queue.push(to);treeEdges.add(edge);treeAdj.get(queue[i]).push({to,edge});treeAdj.get(to).push({to:queue[i],edge});
    }
   }
   const cycles=[];
   for(let i=0;i<moves.length;i++)if(!treeEdges.has(i)){
    const move=moves[i],queue=[move.to],prior=new Map([[move.to,null]]);
    for(let j=0;j<queue.length&&!prior.has(move.from);j++)for(const n of treeAdj.get(queue[j]))if(!prior.has(n.to)){prior.set(n.to,{at:queue[j],edge:n.edge});queue.push(n.to);}
    const tail=[];let at=move.from;while(at!==move.to){const p=prior.get(at);tail.push({edge:p.edge,from:p.at,to:at});at=p.at;}
    cycles.push({steps:[{edge:i,from:move.from,to:move.to},...tail.reverse()],status:'formal-closed-boundary; filling-not-authorized',fillingWitness:null});
   }
   if(cycles.length!==moves.length-paths.length+components)throw Error('Bad cycle bookkeeping');
   // Separate squares of disjoint substitutions from other formal cycles.
   // GF(2) ranks are diagnostics of this finite graph, NOT nonabelian holonomy
   // checks, physical mode counts, or authorization to fill these boundaries.
   const squares=new Map();
   for(const start of paths)for(const a of adj.get(start.id))for(const b of adj.get(start.id)){
    if(moves[a.edge].position>=moves[b.edge].position-1)continue;
    for(const c of adj.get(a.to))if(moves[c.edge].position===moves[b.edge].position){
     const d=adj.get(b.to).find(d=>d.to===c.to&&moves[d.edge].position===moves[a.edge].position);
     if(!d)continue;
     const es=[a.edge,c.edge,d.edge,b.edge];squares.set([...es].sort((a,b)=>a-b).join(','),es);
    }
   }
   const basis=new Map();
   for(const es of squares.values()){
    let bits=es.reduce((n,e)=>n^(1n<<BigInt(e)),0n);
    while(bits){const pivot=bits.toString(2).length-1;if(basis.has(pivot))bits^=basis.get(pivot);else{basis.set(pivot,bits);break;}}
   }
   return {id,source:paths[0].cells[0],target:paths[0].cells.at(-1),length:paths[0].arrows.length,paths,moves,components,cycleRank:cycles.length,cycleBasis:cycles,disjointSquares:[...squares.values()],disjointSquareRank:basis.size,residualCycleRank:cycles.length-basis.size,
    scope:'Complete presentation graph at this fixed interface-path length. The cycle basis is diagnostic only; no identity holonomy, invertibility or sufficient higher-filling set is inferred.'};
  }));
  const prefixChecks=reading.comparisons.map(c=>{
   const boundary=byComparison.get(pairKey(c.sharedReference,c.cell));
   const turns=boundary.alternatives.map(p=>({NCell:p.cells[1],entryAxis:p.axes[0],exitAxis:p.axes[1],sameAxis:p.axes[0]===p.axes[1],nativeFaces:p.arrows,commonEdgeVertices:byFace.get(p.arrows[0]).vertices.filter(v=>byFace.get(p.arrows[1]).vertices.some(w=>String(w)===String(v)))}));
   return {requirement:c.id,boundary:boundary.id,kind:c.kind,turns,representableBySameAxisNPassages:turns.every(t=>t.sameAxis),scope:'Obstruction to representing this comparison boundary using the old same-axis passage grammar; not proof that a comparison path is an individual wire trajectory.'};
  });
  return {id:reading.id,arrows,comparisons,overlaps,prefixChecks,summary:{cells:cells.length,nativeInterfaces:arrows.length,twoInterfacePaths:[...twoPaths.values()].reduce((n,ps)=>n+ps.length,0),parallelTwoStepBoundaries:comparisons.length,sourceRequiredPrefixBoundaries:required.size,threeInterfacePaths:[...threePaths.values()].filter(ps=>ps[0].arrows.length===3).reduce((n,ps)=>n+ps.length,0),fourInterfacePaths:[...threePaths.values()].filter(ps=>ps[0].arrows.length===4).reduce((n,ps)=>n+ps.length,0),parallelThreeStepPresentations:overlaps.filter(o=>o.length===3).length,parallelFourStepPresentations:overlaps.filter(o=>o.length===4).length,comparisonContextMoves:overlaps.reduce((n,o)=>n+o.moves.length,0),formalCycleRank:overlaps.reduce((n,o)=>n+o.cycleRank,0),disjointSquareRank:overlaps.reduce((n,o)=>n+o.disjointSquareRank,0),residualCycleRank:overlaps.reduce((n,o)=>n+o.residualCycleRank,0),disconnectedParallelPresentations:overlaps.filter(o=>o.components>1).length,prefixBoundariesExcludedByOldAxisGrammar:prefixChecks.filter(c=>!c.representableBySameAxisNPassages).length}};
 });
 return {schema:'five-side-oct.comparison-domain.v1',status:'incidence-domain-not-a-coherent-solution',constructionAdmitted:false,edgeUnits:sector.edgeUnits,maximumDiagnosticPathLength:maxLength,readings,
  unresolved:['signed-pair and port binding','authorization and maps for whole-depth comparisons','composition and filling laws','native realization including boundary','coherence-obligation completeness beyond enumerated path lengths'],selectedGroups:[],selectedWireRoutes:[]};
}
