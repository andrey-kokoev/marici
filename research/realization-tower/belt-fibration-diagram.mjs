import {buildCentralBeltLayout,buildCentralTerminalWiring} from './central-belt-layout.mjs';
import {worldPoint} from './normal-ray-model.mjs';
// Extract actual topology. No gap is replaced by a single fictitious field map.
export function extractBeltFibrationDiagram(){
 const layout=buildCentralBeltLayout(),terminal=buildCentralTerminalWiring(layout),rules=new Map(layout.wiring.flatMap(w=>w.branches.map(e=>[e.id,w.rule])));
 const nodes=layout.layers.flatMap(l=>l.nodes.map(n=>({...structuredClone(n),label:l.label,geometricKind:l.kind,nativePacketType:null})));
 nodes.push(...terminal.bundles.map(({body})=>({id:body.id,label:body.beltTerminal.vertexLabel,geometricKind:'terminal-bundle',position:worldPoint(body.point),terminal:body.beltTerminal,nativePacketType:null})));
 const interfaces=[...layout.links,...terminal.links].map(e=>({...structuredClone(e),wiringRule:rules.get(e.id)??e.rule,nativeAdapter:null}));
 const boundaryRequirements=terminal.links.map(e=>({copy:e.parent,beltNode:e.from===e.terminal?e.to:e.from,terminal:e.terminal,wiring:e.id,direction:e.direction,requiredFlux:e.flux,flow:e.from===e.terminal?'parent-to-belt':'belt-to-parent'}));
 return {kind:'extracted-belt-topology',nodes,interfaces,parentPorts:terminal.bundles.map(b=>b.body),terminalFibers:terminal.bundles.map(b=>({id:b.body.id,...b.retainedFiber,nativeMap:null})),boundaryRequirements,scope:'Actual belt and same-sign N terminal wiring. Retained parent grouping is explicit; native field fibration remains unbound.'};
}
export function inspectExtractedBelt(diagram){
 const ids=new Set(diagram.nodes.map(n=>n.id)),errors=[];if(ids.size!==diagram.nodes.length)errors.push({category:'duplicate-node'});
 const edgeIds=new Set();for(const e of diagram.interfaces){if(edgeIds.has(e.id))errors.push({category:'duplicate-interface',at:e.id});edgeIds.add(e.id);for(const end of ['from','to'])if(!ids.has(e[end]))errors.push({category:'unknown-endpoint',at:e.id,endpoint:e[end]});}
 const obligations=[...diagram.nodes.filter(n=>!n.nativePacketType).map(n=>({category:'unbound-packet-type',at:n.id,layer:n.label})),...diagram.interfaces.map(e=>({category:e.nativeAdapter?'unsupported-adapter':'missing-interface-map',at:e.id,from:e.from,to:e.to,wiringRule:e.wiringRule})),...diagram.boundaryRequirements.filter(r=>!r.wiring).map(r=>({category:'missing-parent-attachment',at:r.beltNode,copy:r.copy,direction:r.flow,requiredFlux:r.requiredFlux}))];
 for(const fiber of diagram.terminalFibers??[])if(!fiber.nativeMap)obligations.push({category:'missing-terminal-field-fibration',at:fiber.id});
 for(const r of diagram.boundaryRequirements)if(!ids.has(r.beltNode))errors.push({category:'unknown-boundary-node',at:r.beltNode});
 return {status:errors.length?'rejected':'incomplete',counts:{nodes:diagram.nodes.length,interfaces:diagram.interfaces.length,parentTerminals:diagram.parentPorts.length,boundaryRequirements:diagram.boundaryRequirements.length},errors,obligations,equationFailures:[],scope:'Obligations extracted from actual incidence. No numerical or full-field equation is evaluated for an interface without a native adapter.'};
}
