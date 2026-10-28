import fs from 'node:fs/promises';
import {buildBeltLayers} from '../research/realization-tower/belt-layer-model.mjs';
import {deriveBeltFlux,measureBeltFlux,reflectedStarWiringControl} from '../research/realization-tower/belt-flux-audit.mjs';
const model=buildBeltLayers({origin:[0,0,0],x:[1,0,0],y:[0,1,0],normal:[0,0,1]}),flow=deriveBeltFlux(model),baseline=measureBeltFlux(model,flow),control=reflectedStarWiringControl(model),controlFlow=deriveBeltFlux(control),reflectedControl=measureBeltFlux(control,controlFlow);
const receipt={scope:'steady geometric balance audit; no mechanical stability or native field law claimed',tolerance:1e-10,baseline,perNodeRates:model.layers.map(l=>({label:l.label,rates:Object.fromEntries(['P','E'].map(d=>[d,[...new Set(l.nodes.filter(n=>n.direction===d).map(n=>flow.nodeRates[n.id]))]]))})),edgeRates:flow.edgeRates,reflectedControl:{diagnosticOnly:true,changedEdges:model.links.filter((e,i)=>e.from!==control.links[i].from||e.to!==control.links[i].to).map(e=>({id:e.id,before:e,after:control.links.find(x=>x.id===e.id)})),audit:reflectedControl}};
const path='research/strominger/results/belt-flux-audit.json';await fs.mkdir('research/strominger/results',{recursive:true});await fs.writeFile(path,JSON.stringify(receipt,null,2)+'\n');
for(const [name,a] of [['Current wiring',baseline],['Arm-alignment control (should match production)',reflectedControl]]){
 console.log(name);console.table(a.cuts.map(c=>({gap:c.between.join(' ↔ '),P:c.directionalFlux.P,E:c.directionalFlux.E,transverse:c.transverseFlux,twist:c.axialAngularTransport,tilt:c.transverseAngularTransport,anisotropy:c.tangentAnisotropy.relativeEigenvalueGap})));
 console.log('max conservation residual:',a.maxConservationResidual,'global turning moment:',a.globalTurningMoment);
}
console.log('Control changes',receipt.reflectedControl.changedEdges.length,'edge endpoints. Receipt:',path);
