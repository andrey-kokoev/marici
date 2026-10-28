import test from 'node:test';import assert from 'node:assert/strict';
import {buildBeltLayers} from '../research/realization-tower/belt-layer-model.mjs';
import {deriveBeltFlux,measureBeltFlux,reflectedStarWiringControl} from '../research/realization-tower/belt-flux-audit.mjs';
import {instantiateBlockWiring} from '../research/realization-tower/belt-wiring.mjs';
const frame={origin:[0,0,0],x:[1,0,0],y:[0,1,0],normal:[0,0,1]},run=m=>measureBeltFlux(m,deriveBeltFlux(m));
test('equal splitting conserves flux with threefold central weights on every layer',()=>{
 const m=buildBeltLayers(frame),snapshot=JSON.stringify(m),f=deriveBeltFlux(m),a=measureBeltFlux(m,f);assert.equal(a.totalInjection,24);assert.equal(a.totalExtraction,24);assert.ok(a.maxConservationResidual<1e-10);
 const expected=[[3,1],[12,4],[4,4/3],[4/3,4],[4,12],[1,3]];
 m.layers.forEach((l,i)=>l.nodes.forEach(n=>assert.ok(Math.abs(f.nodeRates[n.id]-expected[i][n.direction==='P'?0:1])<1e-10)));
 for(const l of a.layers){assert.equal(l.directionalFlux.P,12);assert.equal(l.directionalFlux.E,12);assert.ok(Math.hypot(...l.axialArrowMoment)<1e-10);assert.ok(l.positionAnisotropy.relativeEigenvalueGap<1e-10);}
 assert.equal(JSON.stringify(m),snapshot);
});
test('production wiring balances every gap and layer moment, not just the global resultant',()=>{
 const a=run(buildBeltLayers(frame));assert.ok(Math.hypot(...a.globalTurningReaction)<1e-10);assert.ok(Math.hypot(...a.globalTurningMoment)<1e-10);
 for(const cut of a.cuts){assert.ok(Math.hypot(...cut.angularTransport)<1e-10);assert.ok(cut.tangentAnisotropy.relativeEigenvalueGap<1e-10);}
 for(const layer of a.layers)assert.ok(Math.hypot(...layer.turningMoment)<1e-10);assert.ok(a.maxNodeTurningReaction>1,'balanced moments do not eliminate local turning loads');
});
test('legacy rotated-grid regression produces a local couple which arm alignment removes',()=>{
 const m=buildBeltLayers(frame);
 // Preserve the historical star-array geometry for this regression, independently
 // of the new tube-first production presentation.
 for(const index of [0,5]){const layer=m.layers[index],sign=index===0?1:-1;layer.kind='star-array';for(const n of layer.nodes){const theta=Math.PI/2+(n.arm??0)*2*Math.PI/3,r=n.starCentre?0:.4*m.pitch;n.local=[sign*((n.group%2-.5)*1.5*m.pitch+r*Math.cos(theta)),sign*((.5-Math.floor(n.group/2))*1.5*m.pitch+r*Math.sin(theta))];n.position=[...n.local,layer.plane];}}
 const legacy=instantiateBlockWiring({...m.layers[5],kind:'grid'},m.layers[4]),badLinks=new Map(legacy.branches.map(e=>[e.id,e]));
 m.links=m.links.map(e=>badLinks.get(e.id)??e);m.wiring=m.wiring.map(w=>w.outerLayer===6&&w.innerLayer===5?legacy:w);
 const bad=run(m);assert.ok(Math.hypot(...bad.globalTurningMoment)<1e-10);assert.ok(Math.abs(bad.cuts.at(-1).axialAngularTransport)>.02);assert.ok(bad.cuts.at(-1).transverseAngularTransport>.1);assert.ok(bad.cuts.at(-1).tangentAnisotropy.relativeEigenvalueGap>.01);
 const before=JSON.stringify(m),control=reflectedStarWiringControl(m),a=run(control);assert.deepEqual(control.layers,m.layers);assert.equal(control.links.length,m.links.length);assert.ok(control.links.some((e,i)=>e.to!==m.links[i].to||e.from!==m.links[i].from));
 assert.ok(a.maxConservationResidual<1e-10);for(const cut of a.cuts){assert.ok(cut.transverseFlux<1e-10);assert.ok(Math.hypot(...cut.angularTransport)<1e-10);assert.ok(cut.tangentAnisotropy.relativeEigenvalueGap<1e-10);}for(const l of a.layers)assert.ok(Math.hypot(...l.turningMoment)<1e-10);
 assert.equal(JSON.stringify(m),before);
});
test('audit detects corrupted rates and is invariant under rigid frame changes',()=>{
 const m=buildBeltLayers(frame),f=deriveBeltFlux(m);f.edgeRates[m.links[0].id]+=.25;assert.ok(measureBeltFlux(m,f).maxConservationResidual>.2);
 const a=run(m),b=run(buildBeltLayers({origin:[3,-7,2],x:[0,0,1],y:[1,0,0],normal:[0,1,0]}));a.cuts.forEach((c,i)=>{assert.ok(Math.abs(c.axialAngularTransport-b.cuts[i].axialAngularTransport)<1e-10);assert.ok(Math.abs(c.transverseAngularTransport-b.cuts[i].transverseAngularTransport)<1e-10);assert.ok(Math.abs(c.tangentAnisotropy.relativeEigenvalueGap-b.cuts[i].tangentAnisotropy.relativeEigenvalueGap)<1e-10);});
 const twice=measureBeltFlux(m,deriveBeltFlux(m,2));assert.ok(Math.abs(twice.cuts.at(-1).axialAngularTransport-2*a.cuts.at(-1).axialAngularTransport)<1e-10);
});
