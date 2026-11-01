// A dictionary for actual five-cell presentations. The free path nerve is an
// explicitly declared interpretation, not an admitted native operation law.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildFiveSideOctComparisonDomain} from '../../realization-tower/five-side-oct-comparison-domain.mjs';
const root='research/strominger',sector=buildPESymmetricSector(1),cells=new Map(sector.cells.map(c=>[c.id,c]));
const full=buildFiveSideOctComparisonDomain(sector,{readingIds:['reading:0:-1'],maxLength:4});
const reading=full.readings[0],cones=reading.overlaps.filter(o=>o.length===4&&o.source==='neutron:0,0,2,1'&&o.residualCycleRank>0);
assert.equal(cones.length,1);const cone=cones[0];assert.equal(cone.paths.length,16);
const move=cone.moves.find(m=>m.position===2);assert(move);
const A=cone.paths.find(p=>p.id===move.from),B=cone.paths.find(p=>p.id===move.to);assert(A&&B);
const arrows=new Map(reading.arrows.map(a=>[a.id,a]));
function faces(path){
 const result=[];for(let mask=1;mask<32;mask++){
  const indices=[0,1,2,3,4].filter(i=>mask&(1<<i)),vertices=indices.map(i=>path.cells[i]);
  const edgeWords=indices.slice(1).map((j,k)=>path.arrows.slice(indices[k],j));
  result.push({dimension:indices.length-1,indices,vertices,edgeWords});
 }return result;
}
const faceKey=f=>JSON.stringify([f.vertices,f.edgeWords]),vertexKey=f=>JSON.stringify(f.vertices);
const counts=fs=>[0,1,2,3,4].map(d=>fs.filter(f=>f.dimension===d).length);
function intervalEdges(path){
 const out=[];for(let i=0;i<5;i++)for(let j=i+1;j<5;j++){
  const word=path.arrows.slice(i,j),steps=word.map(a=>arrows.get(a));
  assert.equal(steps[0].from,path.cells[i]);assert.equal(steps.at(-1).to,path.cells[j]);
  for(let k=0;k<steps.length-1;k++)assert.equal(steps[k].to,steps[k+1].from);
  const direct=reading.arrows.filter(a=>a.from===path.cells[i]&&a.to===path.cells[j]);assert.equal(direct.length,j===i+1?1:0);
  out.push({fromIndex:i,toIndex:j,from:path.cells[i],to:path.cells[j],word,
   sourceKind:j===i+1?'native-oriented-face-incidence':'formal-retained-path-composite',nativeOperation:null});
 }
 for(let i=0;i<5;i++)for(let j=i+1;j<5;j++)for(let k=j+1;k<5;k++)
  assert.deepEqual([...path.arrows.slice(i,j),...path.arrows.slice(j,k)],path.arrows.slice(i,k));
 return out;
}
const fa=faces(A),fb=faces(B),keysB=new Set(fb.map(faceKey)),verticesB=new Set(fb.map(vertexKey));
const actualIntersection=fa.filter(f=>keysB.has(faceKey(f))),vertexOnlyIntersection=fa.filter(f=>verticesB.has(vertexKey(f)));
assert.deepEqual(counts(fa),[5,10,10,5,1]);assert.deepEqual(counts(actualIntersection),[4,2,0,0,0]);
assert.deepEqual(counts(vertexOnlyIntersection),[4,6,4,1,0]);
const commonCells=A.cells.filter(c=>B.cells.includes(c));assert.equal(commonCells.length,4);
const comparison=reading.comparisons.find(c=>c.id===move.comparison);assert(comparison?.sourceRequirement);
assert.equal(comparison.comparisonMap,null);assert.equal(comparison.fillingWitness,null);assert.equal(move.witness,null);
const leftWord=A.arrows.slice(1,3),rightWord=B.arrows.slice(1,3);assert.notDeepEqual(leftWord,rightWord);
assert.equal(A.cells[1],B.cells[1]);assert.equal(A.cells[3],B.cells[3]);
// Endpoint-only edge identity would silently assert precisely this absent comparison.
const forcedIdentification={endpoints:[A.cells[1],A.cells[3]],leftWord,rightWord,
 sourceComparison:comparison.id,nativeComparisonMap:comparison.comparisonMap};
const centre4=c=>[0,1,2,3].map(i=>4*c.vertices.reduce((s,v)=>s+v[i],0)/c.vertices.length);
const choose=(xs,n)=>n===0?[[]]:xs.flatMap((x,i)=>choose(xs.slice(i+1),n-1).map(t=>[x,...t]));
const det=m=>m.length===0?1:m[0].reduce((s,x,j)=>s+(j%2?-1:1)*x*det(m.slice(1).map(r=>r.filter((_,k)=>k!==j))),0);
const coordinates=A.cells.map(id=>centre4(cells.get(id)));assert(coordinates.flat().every(Number.isInteger));
const differences=coordinates.slice(1).map(v=>v.map((x,i)=>x-coordinates[0][i]));assert(differences.every(v=>v.reduce((a,b)=>a+b,0)===0));
let affineRank=0;for(let n=1;n<=4;n++)for(const rs of choose([0,1,2,3],n))for(const cs of choose([0,1,2,3],n))if(det(rs.map(i=>cs.map(j=>differences[i][j])))!==0)affineRank=n;
assert(affineRank<4);
let pairsAudited=0;const contactHistogram={};
for(let i=0;i<cone.paths.length;i++)for(let j=i+1;j<cone.paths.length;j++){
 const p=cone.paths[i],q=cone.paths[j],common=p.cells.filter(c=>q.cells.includes(c));assert(common.length>=2);
 assert(common.includes(cone.source)&&common.includes(cone.target));
 assert.notDeepEqual(p.arrows,q.arrows); // Same endpoints, different retained composite.
 contactHistogram[common.length]=(contactHistogram[common.length]??0)+1;pairsAudited++;
}
const describe=p=>({path:p,cells:p.cells.map((id,index)=>({index,id,role:cells.get(id).role,kind:cells.get(id).kind,
  geometricVertices:cells.get(id).vertices.length,centreTimesFour:centre4(cells.get(id))})),edges:intervalEdges(p),formalNerveFaces:faces(p)});
const sourceHashes={};for(const p of [root+'/checkers/check_su32_block_dictionary.mjs',root+'/pe-symmetric-sector.mjs',
 'research/realization-tower/five-side-oct-comparison-domain.mjs','research/realization-tower/five-side-oct-routing-obligations.mjs'])
 sourceHashes[p]=createHash('sha256').update(await fs.readFile(p)).digest('hex');
const result={schema:'su32.block-dictionary.v1',passed:true,nativeFilledFourSimplexAdmitted:false,
 reading:reading.id,cone:{source:cone.source,target:cone.target,paths:cone.paths.length},left:describe(A),right:describe(B),sourceMove:move,
 physicalCentreAffineRank:affineRank,formalNerveInterpretation:'Nerve of the free category on oriented cell-incidence arrows. Four composable arrows give a four-simplex; skipping a stage retains its arrows inside a composite word.',
 actualIntersection,vertexOnlyIntersection,forcedIdentification,
 coneContactAudit:{pairsAudited,sharedCellCounts:contactHistogram,singleVertexContacts:0},
 conclusion:'A five-cell presentation is a retained incidence path. It yields a four-simplex only under the declared free-path-nerve interpretation. Endpoint-only simplicial gluing would impose a native comparison that the source leaves unbound.',
 missingNativeBindings:['Interpretation of incidence arrows as operations on complete native records','Admission of the comparison between distinct retained composites','Realization of the three proposed contact blocks and their contact type'],
 limits:['The formal nerve construction is not a new physical four-dimensional cell or native filler.',
 'The 120-pair contact audit covers this one source cone, not all block candidates or all readings.'],sourceHashes};
const dir=root+'/results/su32-block-dictionary-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(dir+'/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({passed:true,leftCells:A.cells,rightCells:B.cells,physicalCentreAffineRank:affineRank,
 formalSimplexFaceCounts:counts(fa),historyAwareIntersection:counts(actualIntersection),vertexOnlyIntersection:counts(vertexOnlyIntersection),
 coneContactAudit:result.coneContactAudit,conclusion:result.conclusion,nativeFilledFourSimplexAdmitted:false},null,2));
