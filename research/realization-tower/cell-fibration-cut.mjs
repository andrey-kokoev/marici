import {buildFoldedFibration,foldedFibrationEnvelope} from './fibration-folded-process.mjs';
const center=vs=>vs[0].map((_,i)=>vs.reduce((s,v)=>s+v[i]/vs.length,0));
const signature=vs=>{const c=center(vs);return vs.map(v=>v.map((x,i)=>x-c[i]).join(',')).sort().join('|');};
const geometry=buildFoldedFibration().geometry;
const cornerCells=foldedFibrationEnvelope.map(p=>geometry.find(g=>g.kind==='tetrahedron'&&g.vertices.some(v=>v.every((x,i)=>x===p[i]))));
const slots=geometry.filter(g=>g.kind==='tetrahedron'&&signature(g.vertices)===signature(cornerCells[0].vertices));
const slotIds=new Set(slots.map(g=>g.id));
export function geometricCellDepth(body,vertex){
 if(!Number.isInteger(vertex)||vertex<1||vertex>4)throw Error('Cut vertex must be 1–4');
 const origin=foldedFibrationEnvelope[vertex-1],others=foldedFibrationEnvelope.filter((_,i)=>i!==vertex-1);
 const axis=origin.findIndex((x,i)=>others.every(p=>p[i]!==x&&p[i]===others[0][i]));
 const unit=(others[0][axis]-origin[axis])/7;
 return (center(body.vertices)[axis]-center(cornerCells[vertex-1].vertices)[axis])/unit;
}
// The three native cell families have different centroid offsets. Align their
// discrete vertex layers by their axial spans: the first octahedron lies in
// layer 1; the inverted tetrahedron beyond it lies in layer 2.
export function geometricCellLayer(body,vertex){
 const depth=geometricCellDepth(body,vertex);
 const offset=body.kind==='octahedron'?0.25:slotIds.has(body.id)?0:0.5;
 const layer=depth+offset;
 if(Math.abs(layer-Math.round(layer))>1e-8)throw Error('Cell does not belong to a native vertex layer');
 return Math.round(layer);
}
export function applyCellFibrationCut(proc,cut){
 if(!proc.cellFibrationAudit||!cut?.enabled)return proc;
 if(!Number.isInteger(cut.layer)||cut.layer<0||cut.layer>6)throw Error('Cut layer must be 0–6');
 const startLayer=cut.startLayer??0;
 if(!Number.isInteger(startLayer)||startLayer<0||startLayer>cut.layer)throw Error('Cut start layer must be 0–end layer');
 const vertices=cut.vertex==='all'?[1,2,3,4]:[cut.vertex];
 const admittedComplement=proc.retainedBodies.filter(g=>!slotIds.has(g.id));
 const occupiedIds=new Set(proc.retainedBodies.map(g=>g.id));
 const unresolved=(proc.conflictBodies??[]).filter(g=>!slotIds.has(g.id)&&!occupiedIds.has(g.id));
 const candidates=[...slots,...admittedComplement,...unresolved].filter(g=>vertices.some(vertex=>{
  const layer=geometricCellLayer(g,vertex);return layer>=startLayer&&layer<=cut.layer;
 })),ids=new Set(candidates.map(g=>g.id));
 const retainedBodies=proc.retainedBodies.filter(g=>ids.has(g.id)),occupied=new Set([...proc.retainedBodies,...(proc.conflictBodies??[])].map(g=>g.id)),empty=candidates.filter(g=>!occupied.has(g.id));
 const counts={proton:0,neutron:0,electron:0,total:retainedBodies.length};for(const g of retainedBodies)counts[g.role]++;
 const wires=cut.showEmpty?empty:[];
 // Retain all admitted corner cells as orientation context, outside slice counts.
 const cornerIds=new Set(proc.cellFibrationAudit.corners.map(c=>c.cell));
 const contextBodies=proc.retainedBodies.filter(g=>cornerIds.has(g.id)&&!ids.has(g.id));
 const labelIds=new Set([...ids,...contextBodies.map(g=>g.id)]);
 const conflictBodies=(proc.conflictBodies??[]).filter(g=>ids.has(g.id));
 const emptyBodies=(proc.emptyBodies??[]).filter(g=>vertices.some(vertex=>{const layer=geometricCellLayer(g,vertex);return layer>=startLayer&&layer<=cut.layer;}));
 return {...proc,retainedBodies,conflictBodies,emptyBodies,contextBodies,interfaceGuides:[],presentationPoints:[],presentationDot:null,
  presentationLabels:[...proc.presentationLabels.filter(p=>labelIds.has(p.cell)),...wires.map(g=>({cell:g.id,point:center(g.vertices),role:'neutron',text:'∅'}))],
  presentationWireframes:wires,
  cutAudit:{vertex:cut.vertex,vertices,combination:'union',startLayer,layer:cut.layer,counts,conflictBodyCount:conflictBodies.length,slotCount:candidates.length,emptyCount:empty.length,emptyIds:empty.map(g=>g.id),visibleIds:retainedBodies.map(g=>g.id),wireframeCount:wires.length,fullBodyCount:proc.retainedBodies.length,geometricDepth:true,shapeAwareLayers:true,includesVertexComplex:startLayer===0,inclusiveDepthRange:true,contextIds:contextBodies.map(g=>g.id),contextBodyCount:contextBodies.length,keepEnvelope:true},
 };
}
