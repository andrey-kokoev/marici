import {seed} from './normal-ray-model.mjs';
import {makeSevenContextFourDepth} from '../strominger/seven-context-four-depth-model.mjs';
const model=makeSevenContextFourDepth();
const trace=model.run([[2,1],[3,-2],[5,3],[7,-4],[11,5]]);
const point=p=>p.split(',').map(Number),aliases=trace.final.neutron.chart.aliases;
const face=names=>names.map(n=>point(aliases[n]));
const center=points=>points[0].map((_,i)=>points.reduce((sum,p)=>sum+p[i]/points.length,0));
export const pairContextStages=Object.freeze(trace.records.map(r=>`Depth ${r.depth}: ${r.local.vertices.join('–')} · ${r.orientation===1?'P → E':'E → P'} · confirmed`));
export const pairContextEnvelope=[0,1,2,3].map(i=>[0,1,2,3].map(j=>.25+3*(Number(i===j)-.25)));
export function pairContextProcess(k,step){
 if(!Number.isInteger(k)||k<1||k>7||!Number.isInteger(step)||step<0||step>=28)throw Error('Invalid pair-context step');
 const record=trace.records[step],snapshot=trace.states[record.depth],selected=face(record.local.vertices);
 const retainedBodies=[
  {id:'P-active-face',faces:[face(model.faces.P)],components:[],color:0x1265a8,opacity:.5},
  {id:'E-active-face',faces:[face(model.faces.E)],components:[],color:0xa82664,opacity:.5},
  {id:'N-mixed-witness',faces:[face(['M0','C1','M1'])],components:[],color:0xe5eaf0,opacity:.12},
 ];
 if(selected.length===3)retainedBodies.push({id:'selected-context',faces:[selected],components:[],color:0xffcb67,opacity:.7});
 const route=[center(face(model.faces.P)),center(face(['M0','C1','M1'])),center(face(model.faces.E))];
 if(record.orientation<0)route.reverse();
 const guides=route.slice(1).map((p,i)=>({id:`flow-${i}`,points:[route[i],p],color:0xffcb67}));
 if(selected.length===2)guides.push({id:'selected-edge',points:selected,color:0xffcb67});
 return {k:7,step,end:seed,assignments:[],firstRay:null,rays:[],faceNeighbors:[],faceVertexComparisons:[],neutronNeighbors:[],surfaceNeutronNeighbors:[],closureRounds:[],nextClosure:[],diamonds:[],conflicts:[],
 retainedBodies,presentationLabels:[],presentationPoints:selected.map(p=>({point:p,role:'proton',color:0xffcb67})),interfaceGuides:guides,
 presentationAudit:{nativeRealization:true,scope:'Native active faces, not new particle growth'},
 pairContextAudit:{position:step+1,depth:record.depth,context:record.local.vertices,orientation:record.orientation,confirmation:record.confirmation,bank:snapshot.bank,localValues:record.local.values,actionHistory:snapshot.history,contexts:model.contexts.map(c=>c.vertices),counts:{positions:28,contexts:7,depths:4,bankSlots:4,physicalBodies:3}},
 summary:`Position ${step+1}/28 — ${pairContextStages[step]}. Seven endpoint contexts × four retained reversals; N is the mixed interface witness.`,
 canAdvance:step<27,history:trace.records.slice(0,step+1).map((r,i)=>({round:i+1,rule:pairContextStages[i]}))};
}
