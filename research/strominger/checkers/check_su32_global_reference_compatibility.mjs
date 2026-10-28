// Global reference identity audit; no routing, cyclic order or payload transport inferred.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas,cellSignConstraintGraphs,encodeSignedReferences} from '../su32-signed-reference-encoder.mjs';
const path='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const fixture=JSON.parse(await fs.readFile(path,'utf8'));
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(createHash('sha256').update(await fs.readFile(p)).digest('hex'),h);
const atlas=buildSu32SignedReferenceAtlas(fixture);
// Solve the COMPLETE constraint graph first; only then restrict to charts.
function solve(graph){
 const neighbors=new Map(graph.vertices.map(v=>[v,[]]));
 for(const {vertices:[a,b]} of graph.edges){neighbors.get(a).push(b);neighbors.get(b).push(a);}
 const assignment={};let components=0;
 for(const root of graph.vertices)if(assignment[root]===undefined){
  components++;assignment[root]=0;const queue=[root];
  for(let i=0;i<queue.length;i++)for(const v of neighbors.get(queue[i])){
   const required=1-assignment[queue[i]];
   if(assignment[v]===undefined){assignment[v]=required;queue.push(v);}
   else if(assignment[v]!==required)return {satisfiable:false};
  }
 }
 for(const {vertices:[a,b]} of graph.edges)assert.notEqual(assignment[a],assignment[b]);
 return {satisfiable:true,components,numberOfAssignments:String(2n**BigInt(components)),assignment};
}
function auditScope(name,charts){
 const graphs=cellSignConstraintGraphs({charts}),roles={};
 for(const role of ['P','E']){
  const g=graphs[role],solution=solve(g);
  roles[role]={vertices:g.vertices.length,edges:g.edges.length,...solution};
  if(solution.satisfiable)for(const c of charts)assert.notEqual(solution.assignment[c[role][0]],solution.assignment[c[role][1]]);
  else{
   const triangle=g.triangles[0];assert(triangle);
   // Independently verify the minimal odd-cycle certificate in source charts.
   for(const edge of triangle.edges)for(const id of edge.occurrences){
    const c=charts.find(c=>c.id===id);assert(c);
    assert.deepEqual([...c[role]].sort(),edge.vertices);
   }
   let solutions=0;
   for(let bits=0;bits<8;bits++)if(triangle.edges.every(e=>
    ((bits>>triangle.vertices.indexOf(e.vertices[0]))&1)!==((bits>>triangle.vertices.indexOf(e.vertices[1]))&1)))solutions++;
   assert.equal(solutions,0);roles[role].obstruction=triangle;
  }
 }
 return {name,charts:charts.length,roles};
}
const scopes=fixture.readings.map(r=>auditScope(r.id,atlas.charts.filter(c=>c.reading===r.id)));
scopes.push(auditScope('all six incoming charts',atlas.charts.filter(c=>c.source===fixture.readings.find(r=>r.id===c.reading).incomingN)));
scopes.push(auditScope('all 36 charts',atlas.charts));
assert(scopes.slice(0,-1).every(s=>['P','E'].every(r=>s.roles[r].satisfiable)));
assert(['P','E'].every(r=>!scopes.at(-1).roles[r].satisfiable));
// Globally retain all native cell identities. Pick arbitrary chart frames all
// at once; restrictions below verify them, rather than generating new wiring.
const globalCells=Object.fromEntries(fixture.cells.map(c=>[c.id,{id:c.id,role:c.role}]));
const frames=atlas.charts.map(c=>{
 for(const cell of c.starCells)assert(globalCells[cell]);
 const p=encodeSignedReferences(atlas,c.id,[0,0],{'P+':null,'P-':null,'E+':null,'E-':null});
 return {chart:c.id,byCell:p.referenceBinding};
});
function overlap(a,b){return Object.keys(a.byCell).filter(cell=>Object.hasOwn(b.byCell,cell)).map(cell=>({cell,from:a.byCell[cell],to:b.byCell[cell]}));}
const overlaps=[];let full=0,partial=0,empty=0,tripleChecks=0;
for(let i=0;i<frames.length;i++)for(let j=i+1;j<frames.length;j++){
 const map=overlap(frames[i],frames[j]);
 if(map.length===4)full++;else if(map.length)partial++;else empty++;
 if(map.length)overlaps.push({from:frames[i].chart,to:frames[j].chart,map});
 for(const edge of map){assert.equal(edge.from[0],edge.to[0]);assert(globalCells[edge.cell]);}
}
for(let i=0;i<frames.length;i++)for(let j=i+1;j<frames.length;j++)for(let k=j+1;k<frames.length;k++){
 const ab=overlap(frames[i],frames[j]),bc=overlap(frames[j],frames[k]),ac=overlap(frames[i],frames[k]);
 for(const x of ab){const y=bc.find(y=>y.cell===x.cell);if(!y)continue;
  const z=ac.find(z=>z.cell===x.cell);assert(z);assert.equal(x.to,y.from);
  assert.equal(x.from,z.from);assert.equal(y.to,z.to);tripleChecks++;
 }
}
assert(partial>0);assert(tripleChecks>0);
// Independent P/E sign changes are coordinate changes of the reference frame.
// Check every alternative binding at each chart without changing shared cells.
let relabelChecks=0;
const flip=(label,binding)=>label[0]+((label[1]==='+')!==Boolean(binding[label[0]==='P'?0:1])?'+':'-');
for(let i=0;i<frames.length;i++)for(const p of [0,1])for(const e of [0,1]){
 const binding=[p,e],packet=encodeSignedReferences(atlas,frames[i].chart,binding,{'P+':null,'P-':null,'E+':null,'E-':null});
 const changed={chart:frames[i].chart,byCell:packet.referenceBinding};
 for(let j=0;j<frames.length;j++)if(j!==i){
  const before=overlap(frames[i],frames[j]),after=overlap(changed,frames[j]);
  assert.deepEqual(after,before.map(x=>({...x,from:flip(x.from,binding)})));relabelChecks++;
 }
}
const sourcePaths=[path,'research/strominger/su32-signed-reference-encoder.mjs','research/strominger/checkers/check_su32_global_reference_compatibility.mjs'];
const hashes={};for(const p of sourcePaths)hashes[p]=createHash('sha256').update(await fs.readFile(p)).digest('hex');
const report={schema:'su32.global-reference-compatibility.v1',passed:true,
 scope:'Native cell identity restrictions; static opposite-sign constraints are an explicitly tested extra hypothesis, not a native transport law.',
 globalIdentityCarrier:{cells:Object.keys(globalCells).length,charts:frames.length,fullOverlaps:full,partialOverlaps:partial,emptyOverlaps:empty,tripleChecks,relabelChecks},
 scopes,frames,overlaps,
 conclusions:['Native shared cell identities admit consistent partial reference maps, with triple agreement on their actual common domains.',
 'Fixed cell signs exist in each tested reading separately and across the six incoming charts; they do not extend to all 36 charts.',
 'Odd triangles refute simultaneous fixed-cell signs under the uniform all-cone extension hypothesis, not the native construction.',
 'Proper partial overlaps do not authorize identification or transport of the missing records. No full four-record transition maps were derived.',
 'No circular order, circle bundle, global signal routing, physical phase or Chern class is inferred.'],sourceHashes:hashes};
const dir='research/strominger/results/su32-global-reference-compatibility-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,frames:undefined,overlaps:undefined,sourceHashes:undefined,scopes:scopes.map(s=>({...s,roles:Object.fromEntries(Object.entries(s.roles).map(([r,x])=>[r,{...x,assignment:undefined,obstruction:x.obstruction?.vertices}]))}))},null,2));
