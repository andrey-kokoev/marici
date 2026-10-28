// Candidate identity/port domains and a finite placement domain, not routes.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildFiveSideOctRoutingObligations} from '../../realization-tower/five-side-oct-routing-obligations.mjs';
const contractPath='research/strominger/contracts/su32-edge5-fibre-placement-binding-v1.json';
const previousPath='research/strominger/results/su32-edge5-extension-contract-v1/verification.json';
const hash=x=>createHash('sha256').update(x).digest('hex');
const bytes=await fs.readFile(contractPath),contract=JSON.parse(bytes);
const previous=JSON.parse(await fs.readFile(previousPath,'utf8'));
for(const [p,h] of Object.entries(previous.sourceHashes))assert.equal(hash(await fs.readFile(p)),h,`Stale source: ${p}`);
assert.equal(contract.extends,previous.contractPath);
const sector=buildPESymmetricSector(2),obligations=buildFiveSideOctRoutingObligations(sector);
const reading=obligations.readings.find(r=>r.id===contract.reading);assert(reading);
const centre=c=>[0,1,2,3].map(i=>c.vertices.reduce((s,v)=>s+v[i],0)/c.vertices.length);
const shape=vs=>vs.map(v=>v.join(',')).sort().join('|');
const point=p=>p.join(','),edgeKey=(a,b)=>[point(a),point(b)].sort().join('|');
const byId=new Map(sector.cells.map(c=>[c.id,c])),byShape=new Map(sector.cells.map(c=>[shape(c.vertices),c]));
const faces=new Map(sector.faces.map(f=>[f.id,f]));
const height=c=>reading.sign*reading.axis.reduce((s,a,i)=>s+a*(centre(c)[i]-sector.centre[i]),0)/2;
const reflect=v=>{const h=reading.axis.reduce((s,a,i)=>s+a*(v[i]-sector.centre[i]),0)/2;return v.map((x,i)=>x-h*reading.axis[i]);};
const mirror=Object.fromEntries(sector.cells.map(c=>[c.id,byShape.get(shape(c.vertices.map(reflect)))?.id]));
for(const c of sector.cells){assert(mirror[c.id]);assert.equal(mirror[mirror[c.id]],c.id);
 assert.equal(byId.get(mirror[c.id]).role,({proton:'electron',electron:'proton',neutron:'neutron'})[c.role]);}
const incoming=reading.incomingN,outgoing=mirror[incoming];
const axis=vertices=>{const axes=[0,1,2,3].filter(i=>vertices.every(v=>v[i]===vertices[0][i]));assert.equal(axes.length,1);return axes[0];};
const fibres=sector.cells.filter(c=>c.role==='proton').sort((a,b)=>a.id.localeCompare(b.id)).map(source=>{
 const target=byId.get(mirror[source.id]);
 const ports=source.faces.map(vertices=>{
  const a=faces.get(shape(vertices)),b=faces.get(shape(vertices.map(reflect)));assert(a&&b);
  assert(a.owners.includes(source.id));assert(b.owners.includes(target.id));
  return {sourceAxis:axis(a.vertices),targetAxis:axis(b.vertices),
   source:{cell:source.id,face:a.id,occurrence:source.id+'@'+a.id,owners:[...a.owners]},
   target:{cell:target.id,face:b.id,occurrence:target.id+'@'+b.id,owners:[...b.owners]}};
 }).sort((a,b)=>a.sourceAxis-b.sourceAxis);
 assert.deepEqual(ports.map(p=>p.sourceAxis),[0,1,2,3]);assert.deepEqual(ports.map(p=>p.targetAxis).sort(),[0,1,2,3]);
 return {id:'edge5-fibre:'+source.id,sourcePresentation:source.id,targetPresentation:target.id,ports,
  payloadMeaning:null,path:null};
});
assert.equal(fibres.length,80);assert.equal(new Set(fibres.map(f=>f.id)).size,80);
assert.equal(new Set(fibres.map(f=>f.targetPresentation)).size,80);
for(const side of ['source','target'])assert.equal(new Set(fibres.flatMap(f=>f.ports.map(p=>p[side].occurrence))).size,320);
function boundaryDomain(cell,forward){
 return sector.faces.filter(f=>f.owners.length===2&&f.owners.includes(cell)).flatMap(f=>{
  const neighbour=f.owners.find(id=>id!==cell),delta=height(byId.get(neighbour))-height(byId.get(cell));
  return (forward?delta<0:delta>0)?[{face:f.id,bodyPort:cell+'@'+f.id,neighbour,neighbourPort:neighbour+'@'+f.id}]:[];
 });
}
const entryFaces=boundaryDomain(incoming,true),exitFaces=boundaryDomain(outgoing,false);
assert.equal(entryFaces.length,4);assert.equal(exitFaces.length,4);
for(const face of entryFaces){const reflected=shape(faces.get(face.face).vertices.map(reflect));
 assert(exitFaces.some(f=>f.face===reflected&&f.neighbour===mirror[face.neighbour]));}
const bundle=cell=>({attachment:{kind:'shared-N-body',cell},occurrences:fibres.map(f=>({fibre:f.id,body:cell,selectedFace:null}))});
const boundaries={entry:bundle(incoming),exit:bundle(outgoing),entryFaceDomain:entryFaces,exitFaceDomain:exitFaces};
assert.deepEqual(boundaries.entry.occurrences.map(o=>o.fibre),boundaries.exit.occurrences.map(o=>o.fibre));
// Reverse this presentation association mechanically, retaining the fibre IDs.
const reversed=fibres.map(f=>({...f,sourcePresentation:f.targetPresentation,targetPresentation:f.sourcePresentation,
 ports:f.ports.map(p=>({sourceAxis:p.targetAxis,targetAxis:p.sourceAxis,source:p.target,target:p.source}))}));
const returned=reversed.map(f=>({...f,sourcePresentation:f.targetPresentation,targetPresentation:f.sourcePresentation,
 ports:f.ports.map(p=>({sourceAxis:p.targetAxis,targetAxis:p.sourceAxis,source:p.target,target:p.source}))}));
assert.deepEqual(returned,fibres);
const edgesOf=c=>new Set(c.faces.flatMap(face=>face.flatMap((a,i)=>face.slice(i+1).map(b=>edgeKey(a,b)))));
const edges=new Map(sector.cells.map(c=>[c.id,edgesOf(c)]));
const shared=(a,b)=>[...edges.get(a)].filter(e=>edges.get(b).has(e)).sort();
const middle=sector.cells.filter(c=>c.role==='neutron'&&Math.abs(height(c))<1e-9);assert.equal(middle.length,25);
const radiusSquared=c=>centre(c).reduce((s,x,i)=>s+(x-sector.centre[i])**2,0);
const tipRadius=Math.max(...sector.cells.filter(c=>c.role==='neutron').map(radiusSquared));
const tips=middle.filter(c=>radiusSquared(c)===tipRadius);assert.equal(tips.length,4);
const dual=id=>byShape.get(shape(byId.get(id).vertices.map(v=>v.map((x,i)=>2*sector.centre[i]-x)))).id;
const triples=[];
for(const T of tips){
 const neighbours=middle.filter(n=>n.id!==T.id&&shared(T.id,n.id).length);
 assert.equal(neighbours.length,2);
 for(const [U,V] of [neighbours,[...neighbours].reverse()])triples.push({id:JSON.stringify([T.id,U.id,V.id]),
  T:T.id,U:U.id,V:V.id,roles:{U:'P/P',V:'E/E'},tipGroup:[T.id,dual(T.id)].sort(),
  nativeEdges:{TU:shared(T.id,U.id),TV:shared(T.id,V.id)},
  requiredLater:{bothTipMembersActive:true,selectedRecordsAvailable:true,remainingCrossPairsAssigned:true},
  actualFibreAssignment:null});
}
assert.equal(triples.length,8);assert.equal(new Set(triples.map(t=>t.id)).size,8);
// Recover local entry-reference domains from native contexts, not fibre axes.
const P=[...new Set(reading.contexts.map(c=>c.P))].sort(),E=[...new Set(reading.contexts.map(c=>c.E))].sort();
assert.equal(P.length,2);assert.equal(E.length,2);
const refs={[P[0]]:'P+',[P[1]]:'P-',[E[0]]:'E+',[E[1]]:'E-'};
const entryReferences={binding:[0,0],referenceCells:refs,joints:reading.contexts.map(c=>({cell:c.channelOccurrence,
 pair:[refs[c.P],refs[c.E]],references:[c.P,c.E]})),signedToFibrePortMap:null};
assert.equal(new Set(entryReferences.joints.map(j=>j.pair.join('|'))).size,4);
const sourcePaths=[contractPath,previousPath,'research/strominger/pe-symmetric-sector.mjs',
 'research/realization-tower/five-side-oct-routing-obligations.mjs',
 'research/strominger/checkers/check_su32_edge5_fibre_placement_binding.mjs'];
const sourceHashes={};for(const p of sourcePaths)sourceHashes[p]=hash(await fs.readFile(p));
assert.equal(sourceHashes[contractPath],hash(bytes));
const report={schema:'su32.edge5-fibre-placement-binding.v1',passed:true,contractPath,
 status:'candidate naming, presentation and placement domains constructed; transport not supplied',
 counts:{fibres:fibres.length,sourceFaceOccurrences:320,targetFaceOccurrences:320,entryBundleOccurrences:80,exitBundleOccurrences:80,
 entryPhysicalFaceChoices:4,exitPhysicalFaceChoices:4,middleN:middle.length,transverseTips:tips.length,markedTriples:triples.length},
 fibres,boundaries,entryReferences,placementDomain:{scope:contract.placementScope,middleCells:middle.map(c=>c.id),triples},
 interpretation:{fibreIdentity:'A declared geometric indexing convention: one P anchor paired with its reflected E presentation. Not a proof of native fibre realization.',
 boundary:'All identities retained at each N-body boundary; eighty logical occurrences do not invent eighty physical faces. Actual face allocation remains a variable.',
 placement:'Eight geometric marked triples are eligible for the proposed global-middle scope. No activation or selected-payload assignment is certified.',
 reversal:'Exact reversal of the presentation/face association, not execution of a path between the paired cells.'},
 remaining:contract.notSupplied,routeAssignment:null,nativeExecution:null,sourceHashes};
assert.deepEqual(JSON.parse(JSON.stringify(report)),report);
const dir='research/strominger/results/su32-edge5-fibre-placement-binding-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,fibres:undefined,boundaries:undefined,placementDomain:{scope:report.placementDomain.scope,triples},sourceHashes:undefined},null,2));
