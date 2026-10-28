import test from 'node:test';
import assert from 'node:assert/strict';
import {buildPESymmetricSector} from '../research/strominger/pe-symmetric-sector.mjs';
import {buildOctahedralCoherentRouting} from '../research/realization-tower/octahedral-coherent-routing.mjs';
import {buildFiveSideOctComparisonDomain} from '../research/realization-tower/five-side-oct-comparison-domain.mjs';
import {nativeVertexLinks,comparisonSphereSweep,spinorDirectionFrame,sampledFrameTransitionDegree,nativeToOrthogonal,orthogonalToNative,octahedronToSpinor,spinorToOctahedron,hopfProjection,commonPhase,hopfSection,sampledTransitionDegree,carrierHomologyMod2} from '../research/strominger/five-side-oct-hopf-probe.mjs';
const near=(a,b,tol=1e-10)=>assert(Math.hypot(...a.map((x,i)=>x-b[i]))<tol),norm2=q=>q.reduce((s,x)=>s+x*x,0);

test('the unmodified carrier is not a closed Hopf total space',()=>{
 const sector=buildPESymmetricSector(2),h=carrierHomologyMod2(sector);
 assert.deepEqual(h.carrier.cellCounts,[146,660,760,245]);assert.deepEqual(h.carrier.betti,[1,0,0,0]);assert.equal(h.carrier.euler,1);
 assert.deepEqual(h.boundary.betti,[1,0,1]);assert.equal(h.boundary.euler,2);
 assert.deepEqual(h.relativeToBoundary.betti,[0,0,0,1]);
 const broken=structuredClone(sector);broken.cells[0].faces.pop();assert.throws(()=>carrierHomologyMod2(broken),/Boundary squared/);
});
test('native coordinates round trip; the reference chart explicitly collapses the boundary',()=>{
 const s=buildPESymmetricSector(2);
 for(const cell of s.cells)for(const q of cell.vertices){const x=nativeToOrthogonal(q,s.centre);near(orthogonalToNative(x,s.centre),q);assert(x.reduce((s,x)=>s+Math.abs(x),0)<=5+1e-10);assert(Math.abs(norm2(octahedronToSpinor(x,5))-1)<1e-10);}
 for(const x of [[5,0,0],[-5,0,0],[0,5,0],[1,2,2]])near(octahedronToSpinor(x,5),[0,0,0,1]);
 assert.equal(spinorToOctahedron([0,0,0,1],5),null);
 for(const x of [[0,0,0],[1,2,1],[0,-1,.5]])near(spinorToOctahedron(octahedronToSpinor(x,5),5),x);
 near(spinorToOctahedron(commonPhase([0,0,0,1],Math.PI/2),5),[0,0,-2.5]);
 assert.throws(()=>octahedronToSpinor([6,0,0],5),/outside/);assert.throws(()=>octahedronToSpinor([0,0,0],Infinity),/radius/);
});
test('reference Hopf circles preserve projection and have free common phase',()=>{
 for(const raw of [[1,0,1,0],[1,2,3,4],[0,0,0,1]]){
  const q=raw.map(x=>x/Math.sqrt(norm2(raw))),base=hopfProjection(q);assert(Math.abs(norm2(base)-1)<1e-10);
  for(const theta of [0,.3,Math.PI/2,Math.PI,2*Math.PI]){const moved=commonPhase(q,theta);near(hopfProjection(moved),base);assert(Math.abs(norm2(moved.map((x,i)=>x-q[i]))-4*Math.sin(theta/2)**2)<1e-10);}
  near(commonPhase(q,2*Math.PI),q);
 }
 assert.throws(()=>hopfProjection([0,0,0,0]),/unit/);
});
test('two genuine local sections have a transition of degree one, not merely invariant labels',()=>{
 for(let i=0;i<=128;i++){
  const phi=2*Math.PI*i/128,n=[Math.cos(phi),Math.sin(phi),0],a=hopfSection(n,'north'),b=hopfSection(n,'south');
  near(hopfProjection(a),n);near(hopfProjection(b),n);near(commonPhase(a,phi),b);
 }
 assert(Math.abs(sampledTransitionDegree()-1)<1e-10);
 assert.throws(()=>hopfSection([0,0,-1],'north'),/singular/);assert.throws(()=>hopfSection([0,0,1],'south'),/singular/);
 // A constant map is phase-invariant but is not a bundle projection with
 // these sections. Invariance alone must not establish the Hopf hypothesis.
 const constant=()=>[0,0,1];assert.notDeepEqual(constant(hopfSection([1,0,0],'north')),[1,0,0]);
});
test('literal complex sign assignments collapse four pairings to two base values',()=>{
 const q=[Math.SQRT1_2,0,Math.SQRT1_2,0];
 near(hopfProjection(q),hopfProjection(q.map(x=>-x)));
 near(hopfProjection([-q[0],-q[1],q[2],q[3]]),hopfProjection([q[0],q[1],-q[2],-q[3]]));
 assert(Math.hypot(...hopfProjection(q).map((x,i)=>x-hopfProjection([-q[0],-q[1],q[2],q[3]])[i]))>1);
});
test('the local direction-frame bundle distinguishes a Hopf spin lift from ordinary frames',()=>{
 const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
 for(const n of [[1,0,0],[0,1,0],[0,0,1]]){
  const q=hopfSection(n,'north'),f=spinorDirectionFrame(q),opposite=spinorDirectionFrame(q.map(x=>-x));
  near(cross(f.x,f.y),f.normal);assert(Math.abs(dot(f.x,f.y))<1e-10);assert(Math.abs(norm2(f.x)-1)<1e-10);near(f.normal,n);near(f.x,opposite.x);near(f.y,opposite.y);
 }
 assert(Math.abs(sampledFrameTransitionDegree()-2)<1e-10);assert(Math.abs(sampledTransitionDegree()-1)<1e-10);
});
test('residual comparison cycles sweep actual native link spheres over integer chains',()=>{
 const s=buildPESymmetricSector(2),links=nativeVertexLinks(s),interior=links.filter(l=>!l.boundary),r=buildFiveSideOctComparisonDomain(s,{readingIds:['reading:0:-1']}).readings[0];
 assert.equal(interior.length,44);
 for(const l of interior){assert.deepEqual(l.homology.cellCounts,[12,24,14]);assert.deepEqual(l.homology.betti,[1,0,1]);assert.deepEqual(l.roles,{P:4,N:6,E:4});for(const ray of l.rays)assert.deepEqual(nativeToOrthogonal(ray,l.point).map(Math.abs).sort(),[0,1,1]);}
 const residual=r.overlaps.filter(o=>o.residualCycleRank),sweeps=residual.map(o=>comparisonSphereSweep(s,o));assert.deepEqual(new Set(sweeps.map(w=>w.vertex)),new Set(interior.map(l=>l.id)));
 for(const w of sweeps)for(const sweep of w.sweeps){
  const boundary=new Map();for(const [id,n] of Object.entries(sweep.coefficients)){const ring=w.dualFaces[id];for(let i=0;i<ring.length;i++){const a=ring[i],b=ring[(i+1)%ring.length],edge=[a,b].sort().join('|');boundary.set(edge,(boundary.get(edge)??0)+n*(a<b?1:-1));}}
  assert([...boundary.values()].every(n=>n===0));assert(sweep.degreeRelativeToFirstSweep===0?Object.values(sweep.coefficients).every(n=>n===0):Object.values(sweep.coefficients).every(n=>Math.abs(n)===1));
 }
 const broken=structuredClone(residual[0]);broken.cycleBasis.find(c=>c.steps.length===12).steps.pop();assert.throws(()=>comparisonSphereSweep(s,broken),/closed integer chain/);
});
test('current candidate channels are not fibres of the declared reference projection',()=>{
 const m=buildOctahedralCoherentRouting(2),s=m.fibration.sector,projection=q=>hopfProjection(octahedronToSpinor(nativeToOrthogonal(q,s.centre),5));
 assert.equal(m.routes.filter(r=>r.ports[0]===r.ports.at(-1)).length,0);
 for(const slot of m.slots){const first=projection(slot.points[0]);assert(slot.points.some(p=>Math.hypot(...projection(p).map((x,i)=>x-first[i]))>1e-6));}
});
