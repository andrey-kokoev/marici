import {buildOctahedralBeltSurface,nativeOctahedralBeltMetrics} from './belt-octahedral-surface.mjs';
import {buildNCapDocking} from './belt-N-cap-docking.mjs';
import {buildBeltTerminalWiring} from './belt-terminal-wiring.mjs';
import {buildBeltLayers,transportColors} from './belt-layer-model.mjs';
import {buildFoldedFibration} from './fibration-folded-process.mjs';
import {analyzeSeamLattice} from './seam-lattice.mjs';
import {fibrationDisplayEnvelope} from './fibration12-process.mjs';
import {worldPoint} from './normal-ray-model.mjs';
import {beltViewerPoint} from './neutron-belt-process.mjs';
const add=(a,b)=>a.map((v,i)=>v+b[i]),sub=(a,b)=>a.map((v,i)=>v-b[i]),mul=(a,s)=>a.map(v=>v*s),dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],unit=a=>mul(a,1/Math.hypot(...a));
const center=ps=>mul(ps.reduce(add,[0,0,0]),1/ps.length),same=(a,b)=>Math.hypot(...sub(a,b))<1e-8;
const parentModel=buildFoldedFibration(),seam=analyzeSeamLattice(parentModel.occurrences),original=fibrationDisplayEnvelope.slice(0,4),clone=fibrationDisplayEnvelope.slice(4),shared=original.filter(p=>clone.some(q=>same(p,q))).map(worldPoint);
const origin=center(shared),x=unit(sub(shared[1],shared[0]));let normal=unit(cross(x,sub(shared[2],shared[0])));
const apex=worldPoint(original.find(p=>!clone.some(q=>same(p,q))));if(dot(sub(apex,origin),normal)<0)normal=mul(normal,-1);
const y=cross(normal,x),parentOffset=3.2;
function baseParentPoint(p,copy){
 const sign=copy==='original'?1:-1,offset=sub(worldPoint(p),origin),angle=-sign*2*Math.PI/3;
 const rotated=add(add(mul(offset,Math.cos(angle)),mul(cross(normal,offset),Math.sin(angle))),mul(normal,dot(normal,offset)*(1-Math.cos(angle))));
 return add(add(origin,rotated),mul(normal,sign*parentOffset));
}
const terminalPivots=Object.fromEntries([['original','+N'],['clone','−N']].map(([copy,label])=>[copy,baseParentPoint(parentModel.bindings.find(b=>b.text===label&&b.copies.includes(copy)).point,copy)]));
const terminalAxis=unit(sub(terminalPivots.original,terminalPivots.clone));
export const centralParentAlignments=Object.fromEntries([['original',original,-1],['clone',clone,1]].map(([copy,vertices,sign])=>{
 const pivot=terminalPivots[copy],before=unit(sub(pivot,center(vertices.map(p=>baseParentPoint(p,copy))))),after=mul(terminalAxis,sign),turn=cross(before,after),sine=Math.hypot(...turn),cosine=Math.max(-1,Math.min(1,dot(before,after)));
 const seed=Math.abs(before[0])<.8?[1,0,0]:[0,1,0],axis=sine>1e-12?mul(turn,1/sine):unit(cross(before,seed)),angle=Math.atan2(sine,cosine);
 return [copy,{pivot,axis,angle,before,after}];
}));
function rotateOffset(v,{axis,angle}){return add(add(mul(v,Math.cos(angle)),mul(cross(axis,v),Math.sin(angle))),mul(axis,dot(axis,v)*(1-Math.cos(angle))));}
function unattachedParentPoint(p,copy){
 copy=copy??(dot(sub(worldPoint(p),origin),normal)>=0?'original':'clone');const alignment=centralParentAlignments[copy];
 return beltViewerPoint(add(alignment.pivot,rotateOffset(sub(baseParentPoint(p,copy),alignment.pivot),alignment)));
}
const docking=buildNCapDocking(parentModel,buildOctahedralBeltSurface(buildCentralBeltLayout()),unattachedParentPoint);
export function centralParentPoint(p,copy){copy=copy??(dot(sub(worldPoint(p),origin),normal)>=0?'original':'clone');return beltViewerPoint(docking.transform(p,copy));}
export const centralBeltEnvelope=[...original.map(p=>centralParentPoint(p,'original')),...clone.map(p=>centralParentPoint(p,'clone'))];

// Presentation adapter: only this boundary converts world positions into the
// viewer's coordinates. Both render modes receive exactly the same node data.
export function buildCentralBeltLayout(){
 const terminal=(label,copy)=>worldPoint(unattachedParentPoint(parentModel.bindings.find(b=>b.text===label&&b.copies.includes(copy)).point,copy));
 const plus=terminal('+N','original'),minus=terminal('−N','clone'),beltOrigin=center([plus,minus]),beltNormal=unit(sub(plus,minus));
 // Preserve the transverse reference as closely as possible, without moving parents.
 let projected=sub(x,mul(beltNormal,dot(x,beltNormal)));if(Math.hypot(...projected)<1e-10)projected=sub(y,mul(beltNormal,dot(y,beltNormal)));
 const beltX=unit(projected),beltY=cross(beltNormal,beltX);
 return buildBeltLayers({origin:beltOrigin,x:beltX,y:beltY,normal:beltNormal,spacing:nativeOctahedralBeltMetrics.spacing,pitch:nativeOctahedralBeltMetrics.pitch});
}
export function buildCentralTerminalWiring(layout=buildCentralBeltLayout()){
 const wiring=buildBeltTerminalWiring(layout,parentModel,centralParentPoint),surface=buildOctahedralBeltSurface(layout);
 for(const {body} of wiring.bundles){const cap=docking.caps.find(c=>c.copy===body.beltTerminal.copy);body.point=beltViewerPoint(cap.targetCentre);body.vertices=[body.point];body.beltTerminal.anchor='exposed-N-cut-face-centre';body.beltTerminal.removedTip=cap.cellId;const patch=surface.patches.find(p=>p.copy===body.beltTerminal.copy);for(const tube of body.beltTerminal.tubes)tube.faceBinding={surface:surface.id,patch:patch.id,face:patch.faces[tube.slot],status:'declared-geometric-role'};}
 surface.cellulation.parentLatticeAttachment={status:'central-unit-face-docked',caps:docking.audit.caps.map(c=>({copy:c.copy,parentCell:c.neighborId,beltFace:c.targetFace,faceError:c.faceError})),scope:'Rigid face matching and half-space non-overlap checked; global lattice phase registration not separately certified.'};
 return {...wiring,surface,scope:'N terminal wiring with declared tube roles on opposite planar octahedral patches. Native field maps remain unbound.'};
}
export function presentCentralBelt(proc){
 const layout=buildCentralBeltLayout(),terminalWiring=buildCentralTerminalWiring(layout);
 const bodies=layout.layers.flatMap(layer=>layer.nodes.map(node=>{
  const point=beltViewerPoint(node.position);
  return {id:node.id,kind:'face-port',vertices:[point],faces:[],components:[],role:null,color:transportColors[node.direction],point,
   beltPort:{structure:`belt:layer:${layer.layer}`,layer:layer.layer,label:layer.label,kind:layer.kind,slot:node.slot,row:node.row,column:node.column,group:node.group,vertex:node.vertex,arm:node.arm,star:node.star,starCentre:node.starCentre,tubeSlot:node.tubeSlot,tubeLane:node.tubeLane,transportDirection:node.direction,normal:[...layout.normal],scope:'Sector-space transport direction, not a particle assignment.'}};
 }));
 const remap=b=>({...b,vertices:b.vertices.map(p=>centralParentPoint(p,b.id.split(':')[0])),faces:b.faces.map(f=>f.map(p=>centralParentPoint(p,b.id.split(':')[0])))});
 const key=p=>p.map(v=>v.toFixed(7)).join(','),guidePoints=new Map(proc.retainedBodies.map(b=>[key(center(b.vertices)),b.id.split(':')[0]]));
 const parentRotation=(copy,sign)=>({copy,degrees:120,signedRadians:-sign*2*Math.PI/3,axis:normal,pivot:beltViewerPoint(add(origin,mul(normal,sign*parentOffset))),terminalAlignment:{...centralParentAlignments[copy],pivot:beltViewerPoint(centralParentAlignments[copy].pivot)}});
 return {...proc,retainedBodies:proc.retainedBodies.map(remap),emptyBodies:proc.emptyBodies.map(remap),presentationWireframes:proc.presentationWireframes.map(remap),attachmentBodies:bodies,parentCutAudit:docking.audit,parentTipReplacementAudit:{cellIds:[...docking.audit.removedCellIds],role:'electron',scope:'Operator-assigned E replacements at the two cut N-tip cells; original N records retained separately.'},beltSurface:terminalWiring.surface,terminalBundles:terminalWiring.bundles.map(b=>b.body),beltGraphLinks:[...layout.links,...terminalWiring.links],replacedFaceLinks:seam.pairs.map(p=>p.cells),
  presentationLabels:proc.presentationLabels.map(p=>({...p,point:centralParentPoint(p.point,p.cell.split(':')[0])})),
  interfaceGuides:proc.interfaceGuides.filter(g=>!g.seamFlow).filter(g=>{const owners=g.points.map(p=>guidePoints.get(key(p)));return owners[0]&&owners[0]===owners[1];}).map(g=>({...g,points:g.points.map(p=>centralParentPoint(p,guidePoints.get(key(p))))})),
  centralBeltAudit:{surface:{id:terminalWiring.surface.id,counts:terminalWiring.surface.counts,cellulation:terminalWiring.surface.cellulation.counts,unitEdge:terminalWiring.surface.cellulation.unitEdge,parentLatticeAttachment:terminalWiring.surface.cellulation.parentLatticeAttachment,patches:terminalWiring.surface.patches,embedding:terminalWiring.surface.embedding},version:layout.version,nodeCount:layout.nodeCount,layerSpacing:layout.spacing,pitch:layout.pitch,normal:layout.normal,origin:beltViewerPoint(layout.origin),parentOffset,parentRotation:parentRotation('original',1),secondParentRotation:parentRotation('clone',-1),epRouting:null,parentCountsUnchanged:true,terminalWiring:{bundleCount:2,linkCount:terminalWiring.links.length,links:terminalWiring.links,bundles:terminalWiring.bundles,scope:terminalWiring.scope},wiring:layout.wiring,fiberJunctions:layout.fiberJunctions,
   layers:layout.layers.map(({nodes,...layer})=>({...layer,center:beltViewerPoint(layer.center),nodeIds:nodes.map(n=>n.id)})),
   attachmentStatus:'Each parent retains its occurrence records in one same-sign N terminal bundle: original +N, clone −N. Each bundle supplies the twelve outer majority satellites and receives the four minority centres, with normalized rates 1 and 3 respectively. All three central stars connect to all opposite stars in both directions. Terminal wiring is explicit; native field fibration and full bus maps remain unbound. One unit N-tip tetrahedron per parent is excluded from display and retained in the audit. Exposed octahedral neighbor faces are rigidly docked to the central triangles of the belt patches. Belt borders mark the declared inside-N sector.'},
  doubleEsd7Audit:{...proc.doubleEsd7Audit,seamLattice:{...proc.doubleEsd7Audit.seamLattice,flows:[],sharedPairs:[]}}};
}
