import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildOctahedralCoherentRouting} from '../../realization-tower/octahedral-coherent-routing.mjs';
import {buildFiveSideOctComparisonDomain} from '../../realization-tower/five-side-oct-comparison-domain.mjs';
import {nativeVertexLinks,comparisonSphereSweep,sampledFrameTransitionDegree,nativeToOrthogonal,octahedronToSpinor,spinorToOctahedron,hopfProjection,commonPhase,hopfSection,sampledTransitionDegree,carrierHomologyMod2} from '../five-side-oct-hopf-probe.mjs';
const distance=(a,b)=>Math.hypot(...a.map((x,i)=>x-b[i]));
const sector=buildPESymmetricSector(2),R=sector.edgeUnits,topology=carrierHomologyMod2(sector);
assert.deepEqual(topology.carrier.betti,[1,0,0,0]);assert.deepEqual(topology.boundary.betti,[1,0,1]);assert.deepEqual(topology.relativeToBoundary.betti,[0,0,0,1]);
let maximumOrbitDrift=0,maximumChartRoundTripError=0,maximumSectionError=0;
for(let i=0;i<80;i++){
 const z=1-2*(i+.5)/80,phi=i*Math.PI*(3-Math.sqrt(5)),n=[Math.sqrt(1-z*z)*Math.cos(phi),Math.sqrt(1-z*z)*Math.sin(phi),z],q=hopfSection(n,'north');
 maximumSectionError=Math.max(maximumSectionError,distance(hopfProjection(q),n));
 for(let j=0;j<=64;j++){
  const point=commonPhase(q,2*Math.PI*j/64),x=spinorToOctahedron(point,R);assert(x);assert(x.reduce((s,x)=>s+Math.abs(x),0)<R);
  maximumOrbitDrift=Math.max(maximumOrbitDrift,distance(hopfProjection(point),n));maximumChartRoundTripError=Math.max(maximumChartRoundTripError,distance(octahedronToSpinor(x,R),point));
 }
}
assert(maximumOrbitDrift<1e-10&&maximumChartRoundTripError<1e-10&&maximumSectionError<1e-10);
const transitionDegree=sampledTransitionDegree();assert(Math.abs(transitionDegree-1)<1e-10);
const pole=[0,0,0,1],movedBoundaryClass=spinorToOctahedron(commonPhase(pole,Math.PI/2),R);assert(movedBoundaryClass);assert(movedBoundaryClass.reduce((s,x)=>s+Math.abs(x),0)<R);
const generic=[Math.SQRT1_2,0,Math.SQRT1_2,0],signClasses=new Map();
for(const a of [1,-1])for(const b of [1,-1]){
 const n=hopfProjection([a*generic[0],a*generic[1],b*generic[2],b*generic[3]]),key=n.map(x=>Math.round(x*1e12)/1e12).join(',');
 if(!signClasses.has(key))signClasses.set(key,[]);signClasses.get(key).push(`${a===1?'+':'-'}${b===1?'+':'-'}`);
}
assert.equal(signClasses.size,2);
// Test only the named reference projection against the existing UNVALIDATED
// candidate. Failure here does not exclude every possible Hopf discretization.
const candidate=buildOctahedralCoherentRouting(2),projection=q=>hopfProjection(octahedronToSpinor(nativeToOrthogonal(q,sector.centre),R));
const drifts=candidate.slots.map(slot=>{
 const base=projection(slot.points[0]);let drift=0;
 for(let k=1;k<slot.points.length;k++)for(let j=0;j<=8;j++){const p=slot.points[k-1].map((x,i)=>x+j/8*(slot.points[k][i]-x));drift=Math.max(drift,distance(projection(p),base));}
 return {slot:slot.id,maximumSampledBaseDrift:drift};
});
const nonconstant=drifts.filter(d=>d.maximumSampledBaseDrift>1e-8);
// A local Hopf lift has a different total space from the physical 3-ball.
// Identify the actual native link spheres before considering such a lift.
const vertexLinks=nativeVertexLinks(sector),interiorLinks=vertexLinks.filter(l=>!l.boundary),interiorIds=new Set(interiorLinks.map(l=>l.id)),localReadings=[];let representativeSphereSweep;
assert.equal(interiorLinks.length,44);
for(const l of interiorLinks){assert.deepEqual(l.homology.cellCounts,[12,24,14]);assert.deepEqual(l.homology.betti,[1,0,1]);assert.deepEqual(l.roles,{P:4,N:6,E:4});}
for(let axis=0;axis<3;axis++)for(const sign of [-1,1]){
 const id=`reading:${axis}:${sign}`,domain=buildFiveSideOctComparisonDomain(sector,{readingIds:[id]}).readings[0],sweeps=domain.overlaps.filter(o=>o.residualCycleRank).map(o=>comparisonSphereSweep(sector,o));
 assert.deepEqual(new Set(sweeps.map(s=>s.vertex)),interiorIds);
 for(const s of sweeps){assert(s.sweeps.some(c=>Math.abs(c.degreeRelativeToFirstSweep)===1));assert(s.sweeps.every(c=>c.steps!==4||c.degreeRelativeToFirstSweep===0));}
 representativeSphereSweep??=sweeps[0];localReadings.push({id,vertices:sweeps.map(s=>s.vertex),sphereSweepsVerified:sweeps.length});
}
const frameTransitionDegree=sampledFrameTransitionDegree();assert(Math.abs(Math.abs(frameTransitionDegree)-2)<1e-10);
const paths=['research/strominger/five-side-oct-hopf-hypothesis-v1.md','tests/five-side-oct-hopf-probe.test.mjs','research/realization-tower/five-side-oct-comparison-domain.mjs','research/strominger/five-side-oct-hopf-probe.mjs','research/strominger/checkers/check_five_side_oct_hopf_hypothesis.mjs','research/strominger/pe-symmetric-sector.mjs','research/realization-tower/octahedral-coherent-routing.mjs','research/realization-tower/octahedral-full-fibration.mjs','research/strominger/sulfur-32-reversible-channel-specification.md'];
const evidence=[];for(const path of paths)evidence.push({path,sha256:createHash('sha256').update(await fs.readFile(path)).digest('hex')});
const report={schema:'five-side-oct.hopf-hypothesis.v1',constructionAdmitted:false,nativeHopfBinding:'not established',topology,
 reference:{extraAssumptions:['collapse the entire octahedral boundary to a single point','choose the stated radial/stereographic chart','interpret its four real coordinates as two complex coordinates; not a native P/E binding','supply common-phase circle action'],sampledFibres:80,samplesPerFibre:65,maximumOrbitDrift,maximumChartRoundTripError,maximumSectionError,transitionDegree,transitionConvention:'south section = exp(i*phi) times north section on the equator; degree +1',boundaryClassMovesIntoInterior:movedBoundaryClass,scope:'A standard Hopf reference on the ADDED boundary quotient. Eighty is an arbitrary number of sampled circle fibres, not a cardinality selected by Hopf topology.'},
 localLinkHypothesis:{interiorSites:interiorLinks.length,linkShape:'cuboctahedral direction sphere: 12 vertices, 24 edges, 8 triangular and 6 square faces',starCells:{P:4,N:6,E:4},readings:localReadings,representativeSphereSweep,spinorTransitionDegree:transitionDegree,ordinaryFrameTransitionDegree:frameTransitionDegree,scope:'The residual diagrams are full native vertex stars; their comparison cycles sweep the link sphere over integer chains. A Hopf spinor lift over these spheres is a concrete conditional hypothesis. The native records have not selected that lift rather than ordinary frames or supplied its phase transport.'},
 literalComplexSignHypothesis:{assumption:'Interpret the four native direction labels as multiplication of two complex coordinates by +/-1',baseClasses:[...signClasses.values()],distinctBasePoints:signClasses.size,scope:'Conditional diagnostic only. Native direction signs have not been identified with complex amplitudes. Four such sign choices do not give four distinct Hopf base fibres.'},
 currentCandidate:{status:'unvalidated candidate, not the intended completed wiring',sourceFibres:candidate.fibration.sourceFibers.length,slotPaths:candidate.routes.length,closedSlotPaths:candidate.routes.filter(r=>r.ports[0]===r.ports.at(-1)).length,testedNChannels:drifts.length,nonconstantUnderReferenceProjection:nonconstant.length,minDrift:Math.min(...drifts.map(d=>d.maximumSampledBaseDrift)),maxDrift:Math.max(...drifts.map(d=>d.maximumSampledBaseDrift)),sampleCounterexamples:nonconstant.slice(0,4),scope:'Rejects this explicit reference projection as an identification of the current N paths with Hopf fibres. Does not reject other, source-justified maps or completions.'},
 remaining:['source-defined packet, spinor-sign and common-phase binding','distinguish a global boundary quotient from local direction-frame lifts','native comparison transport realizing the measured sphere sweep with degree one or two','compatible transition/filling witnesses across overlapping vertex stars and the boundary','binding to the 80 retained fibres without count-based identification'],evidence};
if(process.argv.includes('--record')){const dir='research/strominger/results/five-side-oct-hopf-hypothesis-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(`${dir}/verification.json`,JSON.stringify(report,null,2)+'\n');}
console.log(JSON.stringify({...report,localLinkHypothesis:{...report.localLinkHypothesis,readings:localReadings.map(r=>({id:r.id,sphereSweepsVerified:r.sphereSweepsVerified})),representativeSphereSweep:{vertex:representativeSphereSweep.vertex,link:representativeSphereSweep.link,roles:representativeSphereSweep.roles,sweepDegrees:representativeSphereSweep.sweeps.map(s=>s.degreeRelativeToFirstSweep)}},evidence:report.evidence.map(e=>e.path)},null,2));
