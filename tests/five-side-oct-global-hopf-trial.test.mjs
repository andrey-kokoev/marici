import test from 'node:test';
import assert from 'node:assert/strict';
import {buildPESymmetricSector} from '../research/strominger/pe-symmetric-sector.mjs';
import {buildGlobalHopfTrial,connectionMap,pathPhase} from '../research/strominger/five-side-oct-global-hopf-trial.mjs';
import {wrapPhase} from '../research/strominger/five-side-oct-local-hopf-trial.mjs';
import {nativeToOrthogonal} from '../research/strominger/five-side-oct-hopf-probe.mjs';
const s=buildPESymmetricSector(2),t=buildGlobalHopfTrial(s),near=(a,b,tol=1e-9)=>assert(Math.abs(a-b)<tol,`${a} != ${b}`);
test('global trial covers the full native interface graph and all interior native edges',()=>{
 const edges=new Set(s.faces.filter(f=>f.owners.length===2).map(f=>[...f.owners].sort().join('|')));
 assert.deepEqual(new Set(t.edgePhases.map(e=>e.endpoints.join('|'))),edges);assert.equal(edges.size,560);
 assert.deepEqual(new Set(t.edgePhases.flatMap(e=>e.endpoints)),new Set(s.cells.map(c=>c.id)));
 const all=new Set(),boundary=new Set();for(const f of s.faces)for(const [i,j]of [[0,1],[0,2],[1,2]]){const key=[f.vertices[i].join(','),f.vertices[j].join(',')].sort().join('|');all.add(key);if(f.owners.length===1)boundary.add(key);}
 assert.deepEqual(new Set(t.faces.map(f=>f.nativeEdge.join('|'))),new Set([...all].filter(k=>!boundary.has(k))));
});
test('shared-star direction changes are actual geometric reflections, not scalar gauge changes',()=>{
 const by=new Map(t.local.stars.map(star=>[star.vertex,star]));
 for(const o of t.local.overlaps){const [a,b]=o.vertices.map(id=>by.get(id)),v=nativeToOrthogonal(b.point,a.point),e=v.map(x=>x/Math.hypot(...v));
  for(const id of o.ring){const x=a.directions.get(id),y=b.directions.get(id),dot=x.reduce((s,x,i)=>s+x*e[i],0);near(Math.hypot(...x.map((x,i)=>x-2*dot*e[i]-y[i])),0);}
 }
});
test('each dual cell retains exactly its own unit charge; background terms have zero total flux',()=>{
 assert.equal(t.starFlux.length,44);
 for(const star of t.starFlux){near(star.flux,-2*Math.PI);for(const [source,flux]of Object.entries(star.fluxBySource))near(flux,source===star.vertex?-2*Math.PI:0);}
 for(const f of t.faces)for(const o of f.occurrences)near(o.phaseAgreementError,0);
});
test('shared faces cancel and the dual boundary carries the retained total charge',()=>{
 assert.equal(t.shared.length,168);assert.equal(t.boundary.length,192);
 for(const f of t.shared){const [a,b]=f.occurrences;near(a.flux+b.flux,0);near(wrapPhase(a.loop+b.loop),0);}
 near(t.boundaryFlux,-44*2*Math.PI);near(t.boundaryFlux,t.starFlux.reduce((s,c)=>s+c.flux,0));
 // Reducing the boundary total modulo 2*pi would erase all 44 units.
 near(wrapPhase(t.boundaryFlux),0);assert(Math.abs(t.boundaryFlux)>270);
});
test('factor gauge changes preserve flux and transform the single global connection consistently',()=>{
 const gauge=(v,c)=>[...v+'|'+c].reduce((s,x)=>s+x.charCodeAt(0)*.017,0),changed=buildGlobalHopfTrial(s,{gauge}),map=connectionMap(changed);
 for(const edge of t.edgePhases){const [a,b]=edge.endpoints,delta=t.factors.reduce((sum,f)=>sum+gauge(f.source,b)-gauge(f.source,a),0);near(wrapPhase(map.get(edge.endpoints.join('|'))-edge.phase-delta),0);}
 near(changed.boundaryFlux,t.boundaryFlux);
 const connection=connectionMap(t),edge=t.edgePhases[0].endpoints;near(pathPhase(connection,edge)+pathPhase(connection,[...edge].reverse()),0);
 assert.throws(()=>pathPhase(connection,['missing','cell']),/leaves/);
});
test('ordinary chart gauges obey triple cocycles at the actual shared cells',()=>{
 const by=new Map(t.local.stars.map(s=>[s.vertex,s])),g=(v,c)=>[...v+c].reduce((s,x)=>s+.013*x.charCodeAt(0),0);
 for(const [a,b,c]of t.local.triangles)for(const id of by.get(a).cells.filter(id=>by.get(b).cells.includes(id)&&by.get(c).cells.includes(id))){
  const ab=g(b,id)-g(a,id),bc=g(c,id)-g(b,id),ca=g(a,id)-g(c,id);near(wrapPhase(ab+bc+ca),0);assert(Math.abs(wrapPhase(ab+bc+ca+.2))>.1);
 }
});
