import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas,encodeSignedReferences,decodeSignedReferences,mapReferencePayloads,cellSignConstraintGraphs} from '../su32-signed-reference-encoder.mjs';
const input='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const fixture=JSON.parse(await fs.readFile(input,'utf8'));
for(const [path,digest] of Object.entries(fixture.sourceHashes))assert.equal(createHash('sha256').update(await fs.readFile(path)).digest('hex'),digest,`Stale fixture: ${path}`);
const atlas=buildSu32SignedReferenceAtlas(fixture);assert.equal(atlas.charts.length,36);
const slots=['P+','P-','E+','E-'];
const records={ 'P+':{source:'p-forward',value:[1,2]},'P-':{source:'p-reverse',value:null},'E+':'electron-forward','E-':{source:'electron-reverse',value:false}};
const equalPayloads=Object.fromEntries(slots.map(s=>[s,'same-value']));
const amplitudes={'P+':[1,0],'P-':[0,1],'E+':[2,1],'E-':[1,-1]};
const rotate=([x,y],k)=>[[x,y],[-y,x],[-x,-y],[y,-x]][k%4].map(x=>x===0?0:x);
const norm=z=>z[0]*z[0]+z[1]*z[1];
const relative=(a,b)=>[a[0]*b[0]+a[1]*b[1],a[0]*b[1]-a[1]*b[0]];
const skeleton=p=>{const {records,...rest}=p;return rest;};
let roundTrips=0,actionChecks=0;
for(const chart of atlas.charts)for(const p of [0,1])for(const e of [0,1]){
 for(const source of [records,equalPayloads,amplitudes]){
  const packet=encodeSignedReferences(atlas,chart.id,[p,e],source);
  assert.deepEqual(decodeSignedReferences(atlas,JSON.parse(JSON.stringify(packet))),source);roundTrips++;
  assert.equal(Object.keys(packet.records).length,4);
  const used=packet.channels.flatMap(c=>[c.P.record,c.E.record]);
  for(const s of slots)assert.equal(used.filter(x=>x===s).length,2);
 }
 const packet=encodeSignedReferences(atlas,chart.id,[p,e],amplitudes);
 for(let a=0;a<4;a++)for(let b=0;b<4;b++){
  const act=(pkt,k)=>mapReferencePayloads(atlas,pkt,z=>rotate(z,k));
  assert.deepEqual(act(act(packet,a),b),act(packet,(a+b)%4));actionChecks++;
 }
 const common=mapReferencePayloads(atlas,packet,z=>rotate(z,1));
 const independent=mapReferencePayloads(atlas,packet,(z,s)=>rotate(z,s==='E+'?1:0));
 assert.deepEqual(skeleton(common),skeleton(independent));
 assert.deepEqual(relative(common.records['P+'],common.records['E+']),relative(amplitudes['P+'],amplitudes['E+']));
 assert.notDeepEqual(relative(independent.records['P+'],independent.records['E+']),relative(amplitudes['P+'],amplitudes['E+']));
 for(const s of slots){assert.equal(norm(common.records[s]),norm(amplitudes[s]));assert.equal(norm(independent.records[s]),norm(amplitudes[s]));}
}
const original=encodeSignedReferences(atlas,atlas.charts[0].id,[0,0],records);
const mutations={
 missingRecord:p=>{delete p.records['P+'];},
 wrongChannelReference:p=>{p.channels[0].P.record=p.channels[0].P.record==='P+'?'P-':'P+';},
 missingComparison:p=>{p.comparisons.pop();},
 inventedReconciliation:p=>{p.boundary.reconciliation='identity';},
 duplicatedPayloadInChannel:p=>{p.channels[0].payload=p.records['P+'];},
 wrongOccurrence:p=>{p.chartId=atlas.charts[1].id;}
};
for(const mutate of Object.values(mutations)){const bad=structuredClone(original);mutate(bad);assert.throws(()=>decodeSignedReferences(atlas,bad));}
const graphs=cellSignConstraintGraphs(atlas);
function binaryAssignment(graph){
 const adjacency=new Map(graph.vertices.map(v=>[v,[]]));
 for(const {vertices:[a,b]} of graph.edges){adjacency.get(a).push(b);adjacency.get(b).push(a);}
 const labels={};
 for(const root of graph.vertices)if(labels[root]===undefined){
  labels[root]=0;const queue=[root];
  for(let i=0;i<queue.length;i++)for(const v of adjacency.get(queue[i])){
   const required=1-labels[queue[i]];
   if(labels[v]===undefined){labels[v]=required;queue.push(v);}else if(labels[v]!==required)return {satisfiable:false};
  }
 }
 assert(graph.edges.every(e=>labels[e.vertices[0]]!==labels[e.vertices[1]]));return {satisfiable:true,labels};
}
const entryAtlas={charts:atlas.charts.filter(c=>c.source===fixture.readings.find(r=>r.id===c.reading).incomingN)};
assert.equal(entryAtlas.charts.length,6);
const entryOnly=Object.fromEntries(Object.entries(cellSignConstraintGraphs(entryAtlas)).map(([role,g])=>[role,binaryAssignment(g)]));
const byReading=fixture.readings.map(r=>({reading:r.id,roles:Object.fromEntries(Object.entries(cellSignConstraintGraphs({charts:atlas.charts.filter(c=>c.reading===r.id)})).map(([role,g])=>[role,binaryAssignment(g)]))}));
const stars=new Map();
for(const c of atlas.charts){const key=JSON.stringify(c.starCells);if(!stars.has(key))stars.set(key,[]);stars.get(key).push(c);}
assert.equal(stars.size,6);
const starReports=[];
for(const [star,charts] of stars){
 assert.equal(charts.length,6);
 const roles={};
 for(const role of ['P','E']){
  const vertices=[...new Set(charts.flatMap(c=>c[role]))].sort();assert.equal(vertices.length,4);
  const edges=[...new Set(charts.map(c=>JSON.stringify([...c[role]].sort())))].map(JSON.parse);assert.equal(edges.length,6);
  for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)assert(edges.some(e=>e.includes(vertices[i])&&e.includes(vertices[j])));
  let valid=0;for(let bits=0;bits<16;bits++)if(edges.every(([a,b])=>((bits>>vertices.indexOf(a))&1)!==((bits>>vertices.indexOf(b))&1)))valid++;
  assert.equal(valid,0);
  roles[role]={vertices,edges,validBinaryAssignments:valid,assignmentsTested:16};
 }
 starReports.push({cells:JSON.parse(star),roles});
}
for(const role of ['P','E'])assert(graphs[role].triangles.length>0);
const sources=[input,'research/strominger/sulfur-32-reversible-channel-specification.md','research/strominger/su32-signed-reference-encoder.mjs','research/strominger/checkers/check_su32_signed_reference_encoder.mjs'];
const sourceHashes={};for(const path of sources)sourceHashes[path]=createHash('sha256').update(await fs.readFile(path)).digest('hex');
const report={schema:'su32.signed-reference-encoder-test.v1',status:'passed',classification:'lossless occurrence-reference encoding; static cell signs refuted; phase law underdetermined',charts:atlas.charts.length,bindingsPerChart:4,roundTrips,actionChecks,
 phaseTest:{amplitudeInterpretation:'explicit test fixture only',commonPhasePreservesIncidence:true,independentPhasePreservesIncidence:true,relativeReadingCommon:[2,1],relativeReadingIndependent:[-1,2],sourceSelectedAction:null,scope:'Four exact phase samples test executable arithmetic; general equivariance follows because reference lookup commutes with any per-record payload map. This does not derive native U(1).'},
 negativeControls:Object.keys(mutations),staticCellSignTest:{constraint:'opposite labels on each same-role pair at every cone entrance in all readings; uniform-cone extension hypothesis, not an extra operator requirement',stars:starReports,graphs,entryOnly,byReading},atlas,sourceHashes,
 globalSignedRecordAssignment:null,fiveSlotEncoder:null,nativeHopfBinding:false,
 next:'Construct source-authorized occurrence transition maps and signed-record-to-coefficient encoding; do not promote the 144 alternative chart bindings to simultaneous assignments.'};
if(process.argv.includes('--record')){const dir='research/strominger/results/su32-signed-reference-encoder-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(`${dir}/verification.json`,JSON.stringify(report,null,2)+'\n');}
console.log(JSON.stringify({status:report.status,classification:report.classification,charts:report.charts,bindingsPerChart:4,roundTrips,actionChecks,stars:starReports.length,staticCellSignAssignmentsPerStar:{P:0,E:0},entryOnly:Object.fromEntries(Object.entries(entryOnly).map(([r,x])=>[r,x.satisfiable])),byReading:byReading.map(r=>({reading:r.reading,P:r.roles.P.satisfiable,E:r.roles.E.satisfiable})),negativeControls:report.negativeControls,phaseTest:report.phaseTest,nativeHopfBinding:false},null,2));
