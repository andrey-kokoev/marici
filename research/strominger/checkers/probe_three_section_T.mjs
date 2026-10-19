// Incidence-level test of P/N/E as three coordinate sections of one object.
// Distinct geometric vertices are not silently identified.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {windowProtocol} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';
const bodies=Object.fromEntries(windowProtocol.map(p=>[p.species,[...p.nodes]])),species=['proton','neutron','electron'],common=species.reduce((a,s)=>a.filter(n=>bodies[s].includes(n)),bodies.proton);
assert.deepEqual([...common].sort(),['C1','M1']);
const residual=Object.fromEntries(species.map(s=>[s,bodies[s].filter(n=>!common.includes(n))]));assert.deepEqual(residual,{proton:['C0','M0'],neutron:['M0','C2'],electron:['C2','M2']});
const labels=[...new Set(Object.values(residual).flat())],candidates=[];
for(let i=0;i<labels.length;i++)for(let j=i+1;j<labels.length;j++){
 const [a,b]=[labels[i],labels[j]],q=n=>n===b?a:n,axes=[...new Set(labels.map(q))],sections=Object.fromEntries(species.map(s=>[s,[...new Set(residual[s].map(q))]])),valid=axes.length===3&&Object.values(sections).every(x=>x.length===2)&&new Set(Object.values(sections).map(x=>[...x].sort().join('|'))).size===3;
 candidates.push({identify:[a,b],sections,validThreeCoordinateSections:valid});
}
const passing=candidates.filter(c=>c.validThreeCoordinateSections);assert.equal(passing.length,1);assert.deepEqual(passing[0].identify,['C0','M2']);
const abstractAxes={C0:'a',M2:'a',M0:'b',C2:'c'},sectionData=Object.fromEntries(species.map(s=>{const varies=residual[s].map(n=>abstractAxes[n]);return [s,{varies,holdsFixed:['a','b','c'].find(x=>!varies.includes(x))}];}));
// Glue coefficient-reference charts by their existing full permutations.
// E->P is the explicitly inferred inverse composite, not a native outgoing E.
const PN=[3,1,2,0,4],NE=[0,4,2,3,1],compose=(a,b)=>b.map(i=>a[i]),inv=p=>p.map((_,i)=>p.indexOf(i)),PE=compose(PN,NE),EP=inv(PE);assert.deepEqual(compose(PE,EP),[0,1,2,3,4]);
const reverse={C0:'M2',M2:'C0',M0:'C2',C2:'M0',C1:'M1',M1:'C1'},q=n=>abstractAxes[n]??n;
assert.equal(q(reverse.C0),q(reverse.M2)); // seam is invariant under reversal
const axisReversal={a:q(reverse.C0),b:q(reverse.M0),c:q(reverse.C2)};assert.deepEqual(axisReversal,{a:'a',b:'c',c:'b'});
const input='research/strominger/results/hydrogen-edge-attachment/verification.json',bytes=await readFile(input),h=JSON.parse(bytes);assert.ok(h.rows.every(r=>{const a=r.bodies[2].aliases;return a.C0!==a.M2;}));
const out='research/strominger/results/three-section-T';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'three-section-incidence-model-with-explicit-seam',bodies,commonCore:common,residual,onePairGluingTests:candidates,uniqueSeam:['C0','M2'],sectionData,axisReversal,coefficientChartMaps:{PN,NE,inferredEP:EP,compositeLoop:[0,1,2,3,4]},geometricC0M2DistinctAllMarkings:true,sourceSha256:createHash('sha256').update(bytes).digest('hex'),checkerSha256:createHash('sha256').update(await readFile(new URL('./probe_three_section_T.mjs',import.meta.url))).digest('hex'),scope:'Combinatorial section-incidence model after retaining the shared C1/M1 core and identifying C0/M2 as an abstract cycle seam. This is a new boundary/reference gluing, not equality of occupied spatial vertices or coefficient amplitudes. a/b/c not yet identified with physical M/C/R. The coefficient triangle closes by chosen inverse composite; it does not independently derive the seam, native E->P dynamics, metric compatibility or 12/3 channel equivalence.'},null,2)+'\n');console.log(JSON.stringify({commonCore:common,residual,uniqueSeam:passing[0].identify,sectionData,axisReversal,inferredEP:EP},null,2));
