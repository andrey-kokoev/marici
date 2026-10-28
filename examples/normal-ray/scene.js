// Owned imperative renderer following examples/threejs-reference/scene.js.
// Uses the matched, bundled r180/TrackballControls pair as in tetrahedral-planes.
import * as T from 'three';
import {buildSulfur32Handlebody} from '../../research/realization-tower/sulfur-32-handlebody.mjs';
import {createSulfurHandlebody} from './sulfur-handlebody-renderer.js';
import {removeSulfurTubesTips} from '../../research/realization-tower/sulfur-32-tubes-view.mjs';
import {buildFiveSideOctWiring} from '../../research/realization-tower/five-side-oct-wiring.mjs';
import {createDenseOctWiring} from './dense-oct-wiring-renderer.js';
import {buildSulfurIncomingBundle} from '../../research/realization-tower/sulfur-32-incoming-bundle.mjs';
import {createSulfurIncomingBundle} from './sulfur-incoming-bundle-renderer.js';
import {createSulfurNTubeMarkers} from './sulfur-n-tube-markers.js';
import {setSulfurWiringOpacity} from './sulfur-wiring-opacity.js';
import {createSulfurChannelCutaway} from './sulfur-channel-cutaway.js';
import {singleOctahedralEnvelope} from '../../research/realization-tower/single-octahedral-process.mjs';
import {nativeBridgeEnvelope} from '../../research/realization-tower/native-bridge-process.mjs';
import {signedOctahedralEnvelope} from '../../research/realization-tower/signed-octahedral-process.mjs';
import {protonRotationLine,locksAllowAxialRotation} from './axial-rotation.js';
import {createBeltNodeArrow,createBeltTerminal,createBeltTransportLines,createBeltSurface,insideNBorderStyle} from './belt-renderer.js';
import {layoutVertexLabels} from './vertex-label-layout.js';
import {geometryParentPoint} from './belt-geometry-layout.js';
import {wiringParentPoint} from './belt-wiring-layout.js';
import {centralBeltEnvelope,buildCentralBeltLayout} from '../../research/realization-tower/central-belt-layout.mjs';
import {filterComplexVisibility,filterBeltView} from './complex-visibility.js';
import {applyCellFibrationCut,geometricCellLayer} from '../../research/realization-tower/cell-fibration-cut.mjs';
import { createFaceCompositor } from './face-compositor.js';
import {createCellHover} from './cell-hover.js';
import {esd7CellId} from '../../research/realization-tower/esd7-cell-ids.mjs';
import { palette } from '../threejs-reference/palette.js';
import { TrackballControls } from 'three/addons/controls/TrackballControls.js';
import { LineSegments2 } from 'three/addons/lines/LineSegments2.js';
import { LineSegmentsGeometry } from 'three/addons/lines/LineSegmentsGeometry.js';
import { LineMaterial } from 'three/addons/lines/LineMaterial.js';
import { lattice, worldPoint, apex, cells, seed } from '../../research/realization-tower/normal-ray-model.mjs';
import { processState } from '../../research/realization-tower/normal-ray-processes.mjs';
import {neutronBeltEnvelope} from '../../research/realization-tower/neutron-belt-process.mjs';
import {cellDualGraph} from '../../research/realization-tower/cell-dual-graph.mjs';
import {doubleEsd7Envelope,doubleEsd7VertexLabels} from '../../research/realization-tower/double-esd7-process.mjs';
import {pairContextEnvelope} from '../../research/realization-tower/pair-context-process.mjs';
import {foldedFibrationEnvelope} from '../../research/realization-tower/fibration-folded-process.mjs';
import {fibrationClonePoint,fibrationDisplayEnvelope} from '../../research/realization-tower/fibration12-process.mjs';

import { edgeProbe } from '../../research/realization-tower/edge-ray-model.mjs';
const cache = Array.from({ length: 7 }, (_, i) => edgeProbe(i + 1));
const edgeIds = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]], faceIds = [0,2,1,0,1,3,0,3,2,1,2,3];
const envelopeAt = k => [0,1,2,3].map(i => apex.map((x,j)=>x+(i===0?0:j===0?k:j===i?-k:0)));
const vec = p => new T.Vector3(...worldPoint(p));
const direction = vec(cache[6].point).sub(vec(apex)).normalize();
const roleColors={proton:0x1265a8,electron:0xa82664,neutron:0xe5eaf0};
const roleEdgeColors={proton:0x94a3b8,electron:0x94a3b8,neutron:0x64748b};
const roleOpacity={proton:.78,electron:.78,neutron:.16};
const roleLabelColors={proton:0x70d5ff,electron:0xff91c8,neutron:0xf1f5fa};
const roleLetters={proton:'P',electron:'E',neutron:'N'};

export function createViewer({ host, signal, onFailure, onView = () => {}, onCellHover = () => {} }) {
  signal.throwIfAborted();
  const lifetime = new AbortController();
  const listen = (target,event,fn) => target.addEventListener(event,fn,{signal:lifetime.signal});
  const fallback = host.querySelector('#fallback');
  const scene = new T.Scene(); scene.background = new T.Color(palette.background);
  const camera = new T.OrthographicCamera(-5,5,5,-5,.01,200);
  let renderer, controls, resizeObserver, intersectionObserver, densityQuery, faceCompositor, cellHover;
  let grid, marker, current = new T.Group(); scene.add(current);
  let disposed=false, frame=0, interacting=false, inView=true, previousTime=0, draws=0, rebuilds=0;
  let state={processId:'new-construction',k:1,step:0,branch:1,grid:true,opacity:.12,faceOpacity:1,edgesOnly:false,prior:false,bodies:true,spin:false,speed:1,locks:{v1:false,v2:false,v3:false,v4:false}};
  const wiringLabelLayout=buildCentralBeltLayout();
  let envelope=envelopeAt(state.k);
  let barycenter=envelope.map(vec).reduce((s,p)=>s.add(p),new T.Vector3()).multiplyScalar(.25);
  let halfSpan=Math.max(...envelope.map(p=>vec(p).distanceTo(barycenter)))*1.15;
  let buildKey='', audit=null, latestView=null,inspectionCell=null,lastCutVertex=null;
  let raySegments=[],dottedRaySegments=[],dottedArrowSegments=[],dottedRayIds=[],surfaceBatch=null,cellEdgeObjects=0;
  const sortDirection=new T.Vector3();
  function disposeTree(group) {
    const resources=new Set();
    group.traverse(o=>{if(o.isInstancedMesh)resources.add(o);if(o.geometry)resources.add(o.geometry);for(const m of (Array.isArray(o.material)?o.material:[o.material]))if(m){if(m.map)resources.add(m.map);resources.add(m);}});
    for(const r of resources)r.dispose(); group.clear();
  }
  function stopFrame(){cancelAnimationFrame(frame);frame=0;previousTime=0;}
  function requestRender(){if(!disposed&&!frame&&!document.hidden&&inView)frame=requestAnimationFrame(render);}
  function dispose(){
    if(disposed)return;disposed=true;state.spin=false;state.axialRotation=false;interacting=false;stopFrame();lifetime.abort();signal.removeEventListener('abort',dispose);
    resizeObserver?.disconnect();intersectionObserver?.disconnect();densityQuery?.removeEventListener('change',densityChanged);
    controls?.removeEventListener('change',requestRender);controls?.removeEventListener('start',start);controls?.removeEventListener('end',end);controls?.dispose();
    cellHover?.dispose();disposeTree(scene);faceCompositor?.dispose();renderer?.dispose();renderer?.domElement.remove();fallback.hidden=false;
  }
  function fail(error){dispose();onFailure(error);}
  signal.addEventListener('abort',dispose,{once:true});
  function line(points,color,opacity=1){return new T.LineSegments(new T.BufferGeometry().setFromPoints(points),new T.LineBasicMaterial({color,transparent:true,opacity,depthWrite:false}));}
  function cellOutline(points,color,opacity=1,wide=false){
    // In Wiring the geometry is a guide: reserve bright, thick strokes for wires.
    if((state.processId==='sulfur-32'&&state.sulfurWireBundle)||(state.processId==='ruthenium-98'&&state.rutheniumView==='wiring'))return line(points,0x64748b,.7);
    if(!state.edgesOnly&&!wide)return line(points,color,opacity);
    // Use screen-space wide lines, not unsupported WebGL LineBasicMaterial widths.
    // Each polygon contributes shared edges: draw each edge only once per body.
    const edges=new Map(),pointKey=p=>p.toArray().map(x=>x.toFixed(9)).join(',');
    for(let i=0;i<points.length;i+=2){const a=points[i],b=points[i+1];edges.set([pointKey(a),pointKey(b)].sort().join('|'),[a,b]);}
    cellEdgeObjects++;
    return new LineSegments2(new LineSegmentsGeometry().setPositions([...edges.values()].flatMap(pair=>pair.flatMap(p=>p.toArray()))),new LineMaterial({color,linewidth:wide?insideNBorderStyle.linewidth:3,worldUnits:false,transparent:false,depthTest:true,depthWrite:true}));
  }
  function dot(p,r,color){const o=new T.Mesh(new T.SphereGeometry(r,12,8),new T.MeshBasicMaterial({color}));o.position.copy(vec(p));return o;}
  function arrowLines(points,tip,direction,length,width){
    const side=new T.Vector3().crossVectors(direction,Math.abs(direction.y)<.9?new T.Vector3(0,1,0):new T.Vector3(1,0,0)).normalize().multiplyScalar(width);
    const base=tip.clone().addScaledVector(direction,-length);
    points.push(tip,base.clone().add(side),tip,base.clone().sub(side));
  }
  function rayLine(ray){
    const start=vec(ray.start),end=vec(ray.end),delta=end.clone().sub(start),length=delta.length();
    if(length<1e-9)return;
    const dotted=['meeting-to-V2','meeting-to-V4','ray24','ray42'].includes(ray.id);
    if(dotted){
      dottedRaySegments.push(start,end);dottedRayIds.push(ray.id);
      arrowLines(dottedArrowSegments,end,delta.divideScalar(length),Math.min(.08,length*.2),.015);
    }else {raySegments.push(start,end);arrowLines(raySegments,end,delta.divideScalar(length),Math.min(.14,length*.2),.025);}
  }
  function label(port){
    if(port.polarityRoles){const sheet=state.polaritySheet??'negative';port={...port,role:port.polarityRoles[sheet],text:port.polarityText?.[sheet]??port.text};}
    const canvas=document.createElement('canvas');canvas.width=96;canvas.height=96;
    const c=canvas.getContext('2d');c.fillStyle='rgba(11,17,32,.9)';c.beginPath();c.roundRect(12,12,72,74,12);c.fill();
    c.fillStyle='#'+(port.color??roleLabelColors[port.role]??0xffffff).toString(16).padStart(6,'0');c.font=port.text?'bold 48px sans-serif':'bold 64px sans-serif';c.textAlign='center';c.fillText(port.text??roleLetters[port.role],48,70);
    const texture=new T.CanvasTexture(canvas);texture.colorSpace=T.SRGBColorSpace;
    const sprite=new T.Sprite(new T.SpriteMaterial({map:texture,transparent:true,depthTest:false,depthWrite:false,toneMapped:false}));
    const size=port.role==='neutron'?.25:.32;sprite.scale.set(size,size,1);sprite.position.copy(vec(port.point));sprite.renderOrder=port.role==='neutron'?9:10;sprite.layers.set(1);current.add(sprite);
  }
  function rebuild(){
    const graphMode=state.processId==='ruthenium-98'?state.rutheniumView==='lattice':['sulfur-32','double-esd7','single-octahedral','signed-octahedral-belt','native-octahedral-bridge'].includes(state.processId)&&state.cellGraph&&!(state.processId==='sulfur-32'&&state.sulfurWireBundle);
    cellHover?.begin(state.showCellInfo,graphMode?false:state.edgesOnly);
    disposeTree(current);rebuilds++;surfaceBatch=null;cellEdgeObjects=0;raySegments=[];dottedRaySegments=[];dottedArrowSegments=[];dottedRayIds=[];grid=null;
    if(state.processId==='sulfur-32'&&state.sulfurChannels){
      const bundle=buildSulfurIncomingBundle(),carved=createSulfurChannelCutaway(bundle,{cut:state.sulfurChannelCut??.5,openExterior:state.sulfurChannelOpen??true,cutDirection:state.sulfurChannelNormal??[.35,-.85,.4]});
      if(state.bodies)current.add(carved);
      const wires=createSulfurIncomingBundle(bundle);wires.traverse(o=>{if(o.isMesh){o.layers.set(0);o.material.depthTest=true;o.userData.carvedWire=true;}});current.add(wires);
      audit={processId:state.processId,k:state.k,proceduralStep:state.step,channelCutawayAudit:carved.userData.audit,incomingBundleAudit:bundle.audit,graphMode:false,graphNodeCount:0,graphLinkCount:0,visibleLabels:[],shownCells:[],assignments:[],surfaceCount:state.bodies?1:0,constructionHistory:[]};
      if(!state.bodies){carved.geometry.dispose();carved.material.dispose();}
      return;
    }
    if(state.processId==='sulfur-32'&&state.sulfurHandlebody){
      renderer.localClippingEnabled=true;
      const model=buildSulfur32Handlebody();let handlebodyAudit={...model.audit,visible:false};
      if(state.bodies){const body=createSulfurHandlebody(model,{opacity:state.faceOpacity});current.add(body);handlebodyAudit={...body.userData.audit,visible:true};}
      audit={processId:state.processId,k:state.k,proceduralStep:state.step,handlebodyAudit,graphMode:false,graphNodeCount:0,graphLinkCount:0,visibleLabels:[],shownCells:[],assignments:[],surfaceCount:state.bodies?1:0,constructionHistory:[]};
      return;
    }
    const data=cache[state.k-1];let proc=applyCellFibrationCut(processState(state.processId,state.k,state.step,state.branch,{nTubeAxis:state.nTubeAxis,singleFaceColoring:state.singleFaceColoring,complexVisibility:state.complexVisibility,parentHalfStepTrim:state.parentHalfStepTrim,rimAssembly:state.rimAssembly,seamBelts:state.seamBelts,internalElectronSelf:state.internalElectronSelf,doubleRules:state.doubleRules,neutralValues:state.neutralValues,selectedNeutralMode:state.selectedNeutralMode}),state.cut);
    let incomingBundleAudit,rutheniumWiringAudit;
    if(state.processId==='ruthenium-98'&&state.rutheniumView==='wiring'){
      const wiring=buildFiveSideOctWiring(state.coherenceGroup??'all');const rendered=createDenseOctWiring(wiring);current.add(rendered);rutheniumWiringAudit={...wiring.audit,rendered:rendered.userData.audit};
    }
    if(state.processId==='sulfur-32'&&state.sulfurWireBundle){
      // Wiring retains the intact shape with one incoming bundle and a four-edge vertex split.
      // The previous graph, seam guides and fibration remain in Lattice.
      proc=processState('sulfur-32',state.k,0,state.branch);
      const bundle=buildSulfurIncomingBundle();current.add(createSulfurIncomingBundle(bundle));incomingBundleAudit=bundle.audit;
      incomingBundleAudit.nTubeMarkers={groups:0,pieces:0,schematic:true};
      if(state.sulfurNTubeMarkers){
        const markers=createSulfurNTubeMarkers(bundle,{selectedIdentity:state.sulfurNIdentity??'all'});current.add(markers);incomingBundleAudit.nTubeMarkers=markers.userData.audit;
        if(state.showCellInfo)for(const piece of markers.children){
          const shell=piece.children[0],outline=new T.EdgesGeometry(shell.geometry,25),positions=outline.attributes.position;
          const segments=Array.from({length:positions.count},(_,i)=>new T.Vector3().fromBufferAttribute(positions,i));outline.dispose();
          cellHover.add(piece.userData.hoverInfo,[],segments,null,piece.children.filter(o=>o.userData.tubePart));
          for(const hub of piece.children.filter(o=>o.userData.tubeJunction)){
            const boundary=new T.EdgesGeometry(hub.geometry,25),attribute=boundary.attributes.position;
            const lines=Array.from({length:attribute.count},(_,i)=>new T.Vector3().fromBufferAttribute(attribute,i));boundary.dispose();
            cellHover.add(hub.userData.hoverInfo,[],lines,null,hub);
          }
        }
      }
    }
    if(state.processId==='sulfur-32'&&state.sulfurTubes)proc=removeSulfurTubesTips(proc);
    if(state.processId==='double-esd7')proc=filterBeltView(filterComplexVisibility(proc,state.complexVisibility,state.beltLayers,state.esd7Planes),graphMode?'wiring':'geometry',{nativeBeltLayers:state.nativeBeltLayers});
    const previewCandidates=new Map((proc.doubleEsd7Audit?.rulePreview.candidates??[]).map(c=>[c.id,c]));
    const seamFlows=proc.doubleEsd7Audit?.seamLattice?.flows??[];
    const hoverInfo=(body,role,context=false)=>{
      const vertices=body.vertices??[...new Map((body.faces??body.components??[]).flat().map(v=>[v.join(','),v])).values()];
      const position=vertices[0].map((_,i)=>vertices.reduce((s,v)=>s+v[i],0)/vertices.length);
      const native=Boolean(proc.cellFibrationAudit||proc.fibrationAudit?.folded),cellId=id=>native?esd7CellId(id):id;
      const reflection=body.reflection?{...body.reflection,oppositeGeometryId:body.reflection.oppositeCell,oppositeCell:cellId(body.reflection.oppositeCell)}:null;
      const edgeSource=body.edgeSource?{...body.edgeSource,geometryId:body.edgeSource.cell,cell:cellId(body.edgeSource.cell)}:null;
      const coherence=body.coherence?{...body.coherence,neighbors:body.coherence.neighbors.map(n=>({...n,geometryId:n.cell,cell:cellId(n.cell)}))}:null;
      const translation=body.translation?{...body.translation,geometryId:body.translation.cell,cell:cellId(body.translation.cell)}:null;
      const interiorCopy=body.interiorCopy?{...body.interiorCopy,sources:body.interiorCopy.sources.map(s=>({...s,geometryId:s.cell,cell:cellId(s.cell)}))}:null;
      const conflicts=(body.conflicts??[]).map(w=>({...w,oppositeGeometryId:w.oppositeCell,oppositeCell:cellId(w.oppositeCell)}));
      return {id:cellId(body.id),geometryId:body.id,nativeWiring:body.nativeWiring??null,neutralWire:Boolean(body.neutralWire),insideNSector:Boolean(body.insideNSector),shape:body.kind??(vertices.length===4?'tetrahedron':'polyhedral cell'),role:role??null,position,worldPosition:vec(position).toArray(),layers:proc.cellFibrationAudit?[1,2,3,4].map(v=>geometricCellLayer(body,v)):null,constructionStep:body.layer??body.round??null,process:state.processId,processStep:state.step,seamFlows:seamFlows.filter(f=>f.cells.includes(body.id)).map(f=>({id:f.id,cycle:f.cycle,direction:f.direction})),beltPort:body.beltPort??null,beltTerminal:body.beltTerminal??null,internalSector:body.internalSector??null,refinement:body.refinement??null,attachment:body.attachment??null,front:body.front??null,arrow:body.arrow??null,arrivals:body.arrivals??[],ruleClosure:body.ruleClosure??null,rulePreview:state.highlightRulePreview?previewCandidates.get(body.id)??null:null,context,unfilled:Boolean(body.unfilled),reflection,edgeSource,coherence,translation,interiorCopy,nearestVertex:body.nearestVertex??null,conflicts};
    };
    if(!graphMode&&!proc.parentCutAudit&&(state.processId!=='double-esd7'||state.complexVisibility?.original!==false)&&(!proc.cutAudit||proc.cutAudit.keepEnvelope)&&!proc.signedOctahedralAudit&&!proc.octahedronAudit&&!proc.pairContextAudit&&!proc.neutronBeltAudit)current.add(line(edgeIds.flatMap(([a,b])=>[vec(envelope[a]),vec(envelope[b])]),palette.light,.5));
    if(!graphMode&&!proc.parentCutAudit&&(proc.rimAssemblyAudit||proc.centralBeltAudit)&&state.complexVisibility?.clone!==false)current.add(line(edgeIds.flatMap(([a,b])=>[vec(envelope[a+4]),vec(envelope[b+4])]),palette.light,.5));
    else if((!graphMode&&proc.doubleEsd7Audit&&!proc.centralBeltAudit&&state.complexVisibility?.clone!==false)||(proc.fibrationAudit&&!proc.fibrationAudit.folded))current.add(line(edgeIds.flatMap(([a,b])=>[vec(fibrationClonePoint(envelope[a])),vec(fibrationClonePoint(envelope[b]))]),palette.light,.5));
    if(state.grid&&(!proc.presentationAudit||proc.fibrationAudit)&&!proc.fibrationAudit?.folded){
      const litEdges=[];
      for(const [a,b] of lattice.edges){
        const start=lattice.nodes[a],end=lattice.nodes[b];
        const da=start.address[0]-(-5+state.k),db=end.address[0]-(-5+state.k);
        if(da>0&&db>0)continue;
        let from=new T.Vector3(...start.point),to=new T.Vector3(...end.point);
        if(da>0||db>0){const cut=from.clone().lerp(to,da/(da-db));if(da>0)from=cut;else to=cut;}
        if(from.distanceToSquared(to)>1e-12){litEdges.push(from,to);if(proc.fibrationAudit)litEdges.push(vec(fibrationClonePoint(start.address)),vec(fibrationClonePoint(end.address)));}
      }
      grid=line(litEdges,0xaaaaaa,Math.min(1,state.opacity*3.75));current.add(grid);
    }
    // One translucent triangle per geometric face. Cell fills replace coincident
    // support-plane tiles; shared cell faces get a stable blended color.
    const surfaces=new Map();
    function surface(polygon,color,opacity,priority,opacityScale=1){
      if(state.edgesOnly)return;
      const key=polygon.map(p=>p.map(x=>x.toFixed(9)).join(',')).sort().join('|'),previous=surfaces.get(key),tint=new T.Color(color);
      if(!previous||priority>previous.priority)surfaces.set(key,{polygon,color:tint,opacity,opacityScale,priority,count:1,weight:opacity});
      else if(priority===previous.priority){previous.color.multiplyScalar(previous.weight).add(tint.multiplyScalar(opacity)).multiplyScalar(1/(previous.weight+opacity));previous.weight+=opacity;previous.count++;previous.opacity=Math.max(previous.opacity,opacity);previous.opacityScale=Math.max(previous.opacityScale,opacityScale);}
    }
    marker.visible=Boolean(proc.firstRay);
    marker.scale.setScalar(proc.edgeMeeting?.25:1);
    marker.position.copy(vec(proc.edgeMeeting?.point??proc.rays.at(-1)?.end??data.point));
    for(const stop of cache.filter(s=>!proc.presentationAudit&&(s.k===state.k||(state.prior&&s.k<state.k)))){
      const active=stop.k===state.k,segments=[];
      for(const polygon of stop.polygons){const v=polygon.map(vec);for(let i=0;i<v.length;i++)segments.push(v[i],v[(i+1)%v.length]);}
      current.add(line(segments,0xaaaaaa,active?.8:.2));
    }
    const shown=new Map(proc.retainedBodies?[]:[[seed.id,seed]]);if(proc.firstRay&&state.bodies)for(const id of data.traversed)shown.set(id,cells[id]);
    if(state.step>=2&&!proc.retainedBodies){shown.set(seed.id,seed);shown.set(proc.end.id,proc.end);}
    for(const a of proc.assignments)shown.set(a.cell,cells[a.cell]);
    const continuations=proc.rays;
    for(const ray of continuations){
      if(state.bodies)for(const contact of ray.contacts){
        shown.set(contact.cell,cells[contact.cell]);
      }
      shown.set(ray.cell,cells[ray.cell]);
    }
    for(const neighbor of proc.faceNeighbors){
      shown.set(neighbor.cell,cells[neighbor.cell]);
      const assigned=proc.assignments.find(a=>a.cell===neighbor.cell),highlight=assigned?roleColors[assigned.role]:0xb0b0b0;
      for(const face of [neighbor.sharedFace,...neighbor.exteriorFaces.map(f=>f.vertices)]){
        const points=face.map(vec);
        current.add(line(points.flatMap((p,i)=>[p,points[(i+1)%points.length]]),highlight,.4));
      }
    }
    const filledCells=[],outlinePositions=[],outlineColors=[],assignedOutlinePositions=[];
    for(const [id,cell] of shown){
      const role=proc.assignments.find(a=>a.cell===id)?.role;
      const candidate=!role&&proc.faceNeighbors.find(n=>n.cell===id);
      const v=cell.vertices.map(vec),color=role?roleColors[role]:candidate?0xb0b0b0:id===seed.id?0xaaaaaa:palette.neutral;
      const filled=Boolean(role)||Boolean(candidate)||id===seed.id||id===proc.end.id||continuations.some(ray=>ray.cell===id);
      if(filled)filledCells.push(id);
      if(filled)for(let i=0;i<faceIds.length;i+=3)surface(faceIds.slice(i,i+3).map(j=>cell.vertices[j]),color,role?roleOpacity[role]:candidate?.1:.16,1);
      const hoverSegments=edgeIds.flatMap(([a,b])=>[v[a],v[b]]),hoverFaces=[];
      for(let i=0;i<faceIds.length;i+=3)hoverFaces.push(faceIds.slice(i,i+3).map(j=>v[j]));
      if(state.edgesOnly){const outline=cellOutline(hoverSegments,color);current.add(outline);cellHover.add(hoverInfo(cell,role),hoverFaces,hoverSegments,outline);continue;}
      cellHover.add(hoverInfo(cell,role),hoverFaces,hoverSegments,null);
      const tint=new T.Color(color),outlineOpacity=candidate?.4:.9;
      for(const [a,b] of edgeIds)for(const point of [v[a],v[b]]){
        if(role)assignedOutlinePositions.push(...point.toArray());
        else {outlinePositions.push(...point.toArray());outlineColors.push(tint.r,tint.g,tint.b,outlineOpacity);}
      }
    }
    current.add(new T.LineSegments(new T.BufferGeometry().setAttribute('position',new T.Float32BufferAttribute(outlinePositions,3)).setAttribute('color',new T.Float32BufferAttribute(outlineColors,4)),new T.LineBasicMaterial({vertexColors:true,transparent:true,depthWrite:false})));
    if(assignedOutlinePositions.length){
      const outlines=new LineSegments2(new LineSegmentsGeometry().setPositions(assignedOutlinePositions),new LineMaterial({color:0x000000,linewidth:2,worldUnits:false,transparent:true,depthWrite:false}));
      outlines.renderOrder=1;current.add(outlines);
    }
    // Seed-first Process 4: draw only admitted cells, at their original addresses.
    // Components are geometry, not particles. Cancel internal component faces.
    if(state.bodies)for(const body of [...(!graphMode?[...(proc.retainedBodies??[]),...(proc.conflictBodies??[]),...(proc.contextBodies??[]),...(proc.attachmentBodies??[]),...(proc.terminalBundles??[])]:[])]){
      if(body.beltTerminal){const orb=createBeltTerminal(body);current.add(orb);cellHover.add(hoverInfo(body,null),[],[],null,orb);continue;}
      if(body.beltPort?.transportDirection){const orb=createBeltNodeArrow(body);current.add(orb);cellHover.add(hoverInfo(body,null),[],[],null,orb);continue;}
      if(body.kind==='face-port'){current.add(dot(body.point,.09,body.color));continue;}
      const displayedRole=body.polarityRoles?.[state.polaritySheet??'negative']??body.role;
      const bodyColor=body.color??(displayedRole?roleColors[displayedRole]:body.round===0?0xffffff:0xadc4d4);
      const boundary=new Map();
      for(const component of body.components)for(let i=0;i<faceIds.length;i+=3){
        const polygon=faceIds.slice(i,i+3).map(j=>component[j]);
        const key=polygon.map(p=>p.join(',')).sort().join('|');
        const prior=boundary.get(key);boundary.set(key,{polygon,count:(prior?.count??0)+1});
      }
      for(const polygon of body.faces??[]){const key=polygon.map(p=>p.join(',')).sort().join('|');boundary.set(key,{polygon,count:1});}
      const segments=[];
      for(const {polygon,count} of boundary.values())if(count===1){
        const faceRole=body.faceRoles?.[polygon.map(v=>v.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|')];
        if(proc.parentCellulations||body.neutralWire){/* Native face meshes below own the parent fill. */}
        else if(body.polarityRoles){
          const role=body.polarityRoles[state.polaritySheet??'negative'];
          surface(polygon,roleColors[role],roleOpacity[role],2);
        }else surface(polygon,faceRole?roleColors[faceRole]:bodyColor,body.faceOpacity??(faceRole?roleOpacity[faceRole]:body.opacity??(body.role?roleOpacity[body.role]:.65)),faceRole?3:2,state.processId==='sulfur-32'&&state.sulfurTubes&&body.role==='neutron'?.05:1);
        const points=polygon.map(vec);for(let i=0;i<points.length;i++)segments.push(points[i],points[(i+1)%points.length]);
      }
      const outline=proc.parentCellulations||!segments.length?null:cellOutline(segments,body.insideNSector||body.tipReplacement?insideNBorderStyle.color:state.edgesOnly?bodyColor:body.edgeColor??(roleEdgeColors[displayedRole]??bodyColor),body.insideNSector||body.tipReplacement?1:.65,Boolean(body.insideNSector||body.tipReplacement));if(outline){if(state.processId==='sulfur-32'&&state.sulfurTubes&&body.role==='neutron'){outline.material.transparent=true;outline.material.opacity=.1;outline.material.depthWrite=false;}current.add(outline);}
      cellHover.add(hoverInfo(body,displayedRole,(proc.contextBodies??[]).some(b=>b.id===body.id)),[...boundary.values()].filter(f=>f.count===1).map(f=>f.polygon.map(vec)),segments,outline);
    }
    // Empty native positions have picking geometry only unless explicitly highlighted.
    if(!graphMode&&state.bodies)for(const body of proc.emptyBodies??[]){
      const faces=body.faces.map(f=>f.map(vec)),segments=faces.flatMap(f=>f.flatMap((p,i)=>[p,f[(i+1)%f.length]]));
      let outline=null;
      if((state.processId==='cell-fibration'&&state.cut?.highlightUnassigned)||(state.highlightRulePreview&&previewCandidates.has(body.id))){
        const edges=new Map(),key=p=>p.toArray().map(x=>x.toFixed(9)).join(',');
        for(let i=0;i<segments.length;i+=2){const a=segments[i],b=segments[i+1];edges.set([key(a),key(b)].sort().join('|'),[a,b]);}
        outline=new LineSegments2(new LineSegmentsGeometry().setPositions([...edges.values()].flatMap(pair=>pair.flatMap(p=>p.toArray()))),new LineMaterial({color:0xffce66,linewidth:4,worldUnits:false,depthTest:false,depthWrite:false}));outline.renderOrder=20;current.add(outline);
      }
      cellHover.add(hoverInfo(body,null),faces,segments,outline);
    }
    if(!graphMode&&state.bodies)for(const body of proc.presentationWireframes??[]){
      const segments=[];for(const face of body.faces){const points=face.map(vec);for(let i=0;i<points.length;i++)segments.push(points[i],points[(i+1)%points.length]);}
      current.add(line(segments,0xe5ae55,.6));
    }
    if(!graphMode&&state.bodies&&proc.parentEdgeRays?.length){
      const rays=new LineSegments2(new LineSegmentsGeometry().setPositions(proc.parentEdgeRays.flatMap(r=>r.points.flatMap(worldPoint))),new LineMaterial({color:0xffffff,linewidth:2.5,worldUnits:false,depthTest:true,depthWrite:true}));current.add(rays);
    }
    if(state.bodies)for(const parent of proc.parentCellulations??[])if(parent.cells.length)current.add(createBeltSurface(parent,{wireOnly:Boolean(state.edgesOnly)}));
    if(state.bodies&&proc.beltSurface)current.add(createBeltSurface(proc.beltSurface,{wireOnly:Boolean(graphMode||state.edgesOnly)}));
    let graphNodeCount=0,graphLinkCount=0;
    const beltLinks=proc.beltGraphLinks??[];
    if(state.bodies)current.add(createBeltTransportLines([...(proc.attachmentBodies??[]),...(proc.terminalBundles??[])],beltLinks));
    if(!graphMode&&state.bodies&&proc.attachmentBodies?.length&&beltLinks.length){const points=new Map(proc.attachmentBodies.map(b=>[b.id,vec(b.point)]));current.add(line(beltLinks.filter(e=>e.kind==='perimeter'&&points.has(e.from)&&points.has(e.to)).flatMap(e=>[points.get(e.from),points.get(e.to)]),0x70d5ff,.9));current.add(line(beltLinks.filter(e=>e.kind==='ep-coupling'&&points.has(e.from)&&points.has(e.to)).flatMap(e=>[points.get(e.from),points.get(e.to)]),0xffce66,.95));}
    if(graphMode&&state.bodies){
      let graph=proc.nativeWiringGraph??cellDualGraph([...proc.retainedBodies,...(proc.emptyBodies??[]),...(proc.attachmentBodies??[]),...(proc.terminalBundles??[])]);
      const points=new Map(graph.nodes.map(n=>[n.id,vec(n.position)])),key=(a,b)=>[a,b].sort().join('|'),replaced=new Set((proc.replacedFaceLinks??[]).map(([a,b])=>key(a,b)));
      if(!proc.nativeWiringGraph)graph={...graph,links:[...graph.links.filter(e=>!replaced.has(key(e.from,e.to))),...beltLinks.filter(e=>points.has(e.from)&&points.has(e.to))]};
      graphNodeCount=graph.nodes.length;graphLinkCount=graph.links.length;
      current.add(line(graph.links.filter(e=>e.kind==='native-tip-contact').flatMap(e=>[points.get(e.from),points.get(e.to)]),0xffffff,1));
      current.add(line(graph.links.filter(e=>e.kind!=='ep-coupling'&&e.kind!=='belt-transport'&&e.kind!=='native-tip-contact'&&e.kind!=='periodic-seam'&&e.kind!=='retained-tip-pair').flatMap(e=>[points.get(e.from),points.get(e.to)]),0x8595a8,.38));
      current.add(line(graph.links.filter(e=>e.kind==='ep-coupling').flatMap(e=>[points.get(e.from),points.get(e.to)]),0xffce66,.95));
      current.add(line(graph.links.filter(e=>e.kind==='periodic-seam').flatMap(e=>[points.get(e.from),points.get(e.to)]),0xe1bc65,.8));
      current.add(line(graph.links.filter(e=>e.kind==='retained-tip-pair').flatMap(e=>[points.get(e.from),points.get(e.to)]),0x42bfb3,.8));
      for(const node of graph.nodes){
        const body=node.body,orb=body.beltTerminal?createBeltTerminal(body):body.beltPort?.transportDirection?createBeltNodeArrow(body):new T.Mesh(new T.SphereGeometry(body.refinementParent?.012:(body.role||body.beltPort?.transportDirection)?.09:.055,12,8),new T.MeshBasicMaterial({color:body.color??(body.role?roleColors[body.role]:0x68788b),wireframe:Boolean(state.complexVisibility?.belt!==false&&proc.neutronRefinementAudit?.complexes.some(c=>c.parentId===body.id))}));
        orb.position.copy(points.get(node.id));orb.updateMatrixWorld(true);current.add(orb);
        for(const flow of seamFlows.filter(f=>f.cells.includes(body.id))){
          const ring=new T.Mesh(new T.SphereGeometry(.13,12,8),new T.MeshBasicMaterial({color:flow.color,wireframe:true,depthTest:false,depthWrite:false}));ring.position.copy(orb.position);ring.renderOrder=22;current.add(ring);
        }
        if(state.highlightRulePreview&&previewCandidates.has(body.id)){
          const halo=new T.Mesh(new T.SphereGeometry(.11,12,8),new T.MeshBasicMaterial({color:0xffce66,wireframe:true,depthWrite:false}));halo.position.copy(orb.position);current.add(halo);
        }
        const faces=body.faces.map(f=>f.map(vec)),segments=faces.flatMap(f=>f.flatMap((p,i)=>[p,f[(i+1)%f.length]]));
        cellHover.add(hoverInfo(body,body.role),faces,segments,null,orb);
      }
    }
    if(state.bodies)for(const pair of proc.tubesCutPrisms??[]){
      for(const wall of pair.walls)surface(wall,pair.color,1,3,1);
      const segments=pair.walls.flatMap(w=>w.flatMap((p,i)=>[vec(p),vec(w[(i+1)%w.length])]));
      current.add(cellOutline(segments,insideNBorderStyle.color,1,true));
    }
    const positions=[],colors=[],triangles=[];
    for(const entry of surfaces.values()){
      const points=entry.polygon.map(vec);
      for(let i=1;i<points.length-1;i++){
        const face=[points[0],points[i],points[i+1]],base=positions.length/3;
        for(const point of face){positions.push(...point.toArray());colors.push(entry.color.r,entry.color.g,entry.color.b,entry.opacity);}
        triangles.push({base,cellFace:entry.priority>=1,opacity:entry.opacity,opacityScale:entry.opacityScale,center:face.reduce((s,p)=>s.add(p),new T.Vector3()).multiplyScalar(1/3),depth:0});
      }
    }
    if(!state.edgesOnly){
    const geometry=new T.BufferGeometry().setAttribute('position',new T.Float32BufferAttribute(positions,3)).setAttribute('color',new T.Float32BufferAttribute(colors,4));
    geometry.setIndex(new T.BufferAttribute(Uint32Array.from({length:positions.length/3},(_,i)=>i),1));geometry.index.setUsage(T.DynamicDrawUsage);geometry.computeBoundingSphere();
    const surfaceMesh=new T.Mesh(geometry,new T.MeshBasicMaterial({vertexColors:true,side:T.DoubleSide,transparent:true,depthWrite:false,forceSinglePass:true}));
    surfaceBatch={geometry,triangles,mesh:surfaceMesh,hasTranslucentFaces:triangles.some(t=>t.opacityScale<1)};current.add(surfaceMesh);
    }else surfaceBatch=null;
    const visibleLabels=[...new Map((proc.presentationLabels??proc.assignments).map(a=>[`${a.cell}:${a.role}`,a])).values()].filter(()=>state.labels!==false);
    for(const port of visibleLabels)label(port);
    if(proc.presentationDot)current.add(dot(proc.presentationDot,.065,roleColors.electron));
    for(const site of proc.presentationPoints??[])current.add(dot(site.point,.045,site.color??roleColors[site.polarityRoles?.[state.polaritySheet??'negative']??site.role]));
    for(const guide of state.processId==='double-esd7'&&!graphMode?[]:proc.interfaceGuides??[]){
      const guidePoints=guide.points.map(vec),start=guidePoints[0],end=guidePoints.at(-1),delta=end.clone().sub(start),arrows=[];
      if(guide.inset){const offset=delta.clone().normalize().multiplyScalar(Math.min(guide.inset,delta.length()/3));start.add(offset);end.sub(offset);}
      if(!guide.connector)arrowLines(arrows,end,delta.clone().normalize(),Math.min(.06,delta.length()*.3),.015);
      const path=new T.Line(new T.BufferGeometry().setFromPoints(guidePoints),new T.LineDashedMaterial({color:guide.color,dashSize:.025,gapSize:.015,depthWrite:false}));
      path.computeLineDistances();const heads=line(arrows,guide.color);if(guide.seamFlow||guide.overlay){path.material.depthTest=false;heads.material.depthTest=false;path.renderOrder=22;heads.renderOrder=22;}current.add(path,heads);
    }
    for(const comparison of proc.faceVertexComparisons){
      const corners=comparison.corners.map(vec);
      const helper=new T.LineSegments(new T.BufferGeometry().setFromPoints(edgeIds.flatMap(([a,b])=>[corners[a],corners[b]])),new T.LineDashedMaterial({color:palette.light,transparent:true,opacity:.5,dashSize:.08,gapSize:.06,depthWrite:false}));
      helper.computeLineDistances();current.add(helper);
      const faceCenter=comparison.face.map(vec).reduce((s,p)=>s.add(p),new T.Vector3()).multiplyScalar(1/3);
      current.add(line([faceCenter,vec(comparison.oppositeVertex)],roleColors[comparison.ownerRole],.65));
      current.add(dot(comparison.oppositeVertex,.035,palette.light));
    }
    const signalConnections=[...new Map((proc.mediation?.witnesses??[]).flatMap(w=>w.faces).map(f=>[[f.from,f.to].sort((a,b)=>a-b).join(':'),f])).values()];
    if(proc.edgeFronts?.length)for(const ray of proc.edgeFronts)rayLine(ray);
    else if(proc.firstRay)rayLine(proc.firstRay);
    for(const ray of continuations)rayLine(ray);
    for(const ray of proc.baseEdgeRays??[])rayLine(ray);
    for(const guide of proc.connectionGuides??[]){
      const path=new T.Line(new T.BufferGeometry().setFromPoints(guide.points.map(vec)),new T.LineDashedMaterial({color:0xe6b35a,dashSize:.06,gapSize:.04,transparent:true,opacity:.65,depthWrite:false}));
      path.computeLineDistances();current.add(path);
    }
    if(raySegments.length)current.add(new LineSegments2(new LineSegmentsGeometry().setPositions(raySegments.flatMap(p=>p.toArray())),new LineMaterial({color:palette.edge,linewidth:2,worldUnits:false})));
    if(dottedRaySegments.length){
      const dotted=new T.LineSegments(new T.BufferGeometry().setFromPoints(dottedRaySegments),new T.LineDashedMaterial({color:palette.edge,dashSize:.012,gapSize:.05,linewidth:1,transparent:true,opacity:.85,depthWrite:false}));
      dotted.computeLineDistances();current.add(dotted);
      current.add(line(dottedArrowSegments,palette.edge,.85));
    }
    if(proc.firstRay)current.add(line(data.crossings.flatMap(edge=>edge.map(vec)),0xffffff));
    audit={incomingBundleAudit,rutheniumWiringAudit,ruthenium98Audit:proc.ruthenium98Audit,tubesViewAudit:proc.tubesViewAudit,peCoupledRoutingAudit:proc.peCoupledRoutingAudit,ambientNeutralAudit:proc.ambientNeutralAudit,nTubeAudit:proc.nTubeAudit,emptyRegionAudit:proc.emptyRegionAudit,interiorNPairingAudit:proc.interiorNPairingAudit,singleOctahedralAudit:proc.singleOctahedralAudit,nativeBridgeAudit:proc.nativeBridgeAudit,signedOctahedralAudit:proc.signedOctahedralAudit,parentTrimAudit:proc.parentTrimAudit,nativeWiringAudit:proc.nativeWiringAudit,parentCellulations:proc.parentCellulations?.map(p=>({copy:p.copy,counts:p.counts})),parentEdgeRays:proc.parentEdgeRays??[],geometryLayoutAudit:proc.geometryLayoutAudit,wiringLayoutAudit:proc.wiringLayoutAudit,parentCutAudit:proc.parentCutAudit,beltViewAudit:proc.beltViewAudit,centralBeltAudit:proc.centralBeltAudit,perimeterBeltAudit:proc.perimeterBeltAudit,complexVisibilityAudit:proc.complexVisibilityAudit,neutronRefinementAudit:proc.neutronRefinementAudit,rimAssemblyAudit:proc.rimAssemblyAudit,attachmentBodyCount:proc.attachmentBodies?.length??0,terminalBundleCount:proc.terminalBundles?.length??0,rulePreviewCount:previewCandidates.size,highlightedRulePreviewCount:state.highlightRulePreview&&state.bodies?previewCandidates.size:0,graphMode:Boolean(graphMode),graphNodeCount,graphLinkCount,edgesOnly:Boolean(state.edgesOnly),cellEdgeObjects,cellEdgeWidth:state.edgesOnly?3:null,faceRendering:state.edgesOnly?'none':'filled',wireframeBodyCount:proc.presentationWireframes?.length??0,highlightedUnassignedCount:state.processId==='cell-fibration'&&state.cut?.highlightUnassigned?(proc.emptyBodies?.length??0):0,cutAudit:proc.cutAudit??null,cellFibrationAudit:proc.cellFibrationAudit,doubleEsd7Audit:proc.doubleEsd7Audit,neutronBeltAudit:proc.neutronBeltAudit,collectiveCells:proc.collectiveCells??[],displayedPolaritySheet:state.polaritySheet??'negative',pairContextAudit:proc.pairContextAudit,octahedronAudit:proc.octahedronAudit,fibrationAudit:proc.fibrationAudit,presentationAudit:proc.presentationAudit,conflictBodyCount:proc.conflictBodies?.length??0,sourcePresentationBodyCount:proc.preCutRetainedCount,presentationBodyCount:proc.presentationAudit?proc.retainedBodies.length+(proc.conflictBodies?.length??0):undefined,retainedAudit:proc.retainedAudit,retainedHistory:proc.retainedBodies?proc.history:undefined,processId:state.processId,constructionHistory:proc.history,diamonds:proc.diamonds,conflicts:proc.conflicts,foundationComplete:proc.foundationComplete,radial:proc.radial,collectiveCore:proc.collectiveCore,connectionGuides:proc.connectionGuides,dottedRayIds,ray34Visible:proc.ray34Visible,ray34:proc.ray34,edge34Assignments:proc.edge34Assignments,edge34Predecessors:proc.edge34Predecessors,ray14Visible:proc.ray14Visible,ray14:proc.ray14,edge14Assignments:proc.edge14Assignments,edge14Predecessors:proc.edge14Predecessors,ray12Visible:proc.ray12Visible,ray12:proc.ray12,edge12Assignments:proc.edge12Assignments,edge12Predecessors:proc.edge12Predecessors,ray32PatternVisible:proc.ray32PatternVisible,ray32Pattern:proc.ray32Pattern,edge32Assignments:proc.edge32Assignments,edge32Predecessors:proc.edge32Predecessors,patternClosureRounds:proc.patternClosureRounds,nextPatternClosure:proc.nextPatternClosure,baseNeutronPassVisible:proc.baseNeutronPassVisible,baseNeutronPass:proc.baseNeutronPass,edgeVertexFillVisible:proc.edgeVertexFillVisible,edgeVertexNeutrons:proc.edgeVertexNeutrons,edgeClosureRounds:proc.edgeClosureRounds,nextEdgeClosure:proc.nextEdgeClosure,median3To24Visible:proc.median3To24Visible,median1To24Visible:proc.median1To24Visible,faceMedianRays:proc.faceMedianRays,faceMedianAssignments:proc.faceMedianAssignments,diamondGapVisible:proc.diamondGapVisible,diamondGapPlan:proc.diamondGapPlan,neutronBoundaryVisible:proc.neutronBoundaryVisible,neutronBoundaryPlan:proc.neutronBoundaryPlan,identifiedSurfacePlan:proc.identifiedSurfacePlan,identifiedSurfaceVisible:proc.identifiedSurfaceVisible,f134DiamondPlan:proc.f134DiamondPlan,f134DiamondVisible:proc.f134DiamondVisible,f123DiamondPlan:proc.f123DiamondPlan,f123DiamondVisible:proc.f123DiamondVisible,surfaceRemainderPlan:proc.surfaceRemainderPlan,surfaceRemainderVisible:proc.surfaceRemainderVisible,remainingFacePlan:proc.remainingFacePlan,remainingFaceVisible:proc.remainingFaceVisible,baseEdgeVisible:proc.baseEdgeVisible,baseEdgeRays:proc.baseEdgeRays,surfaceRays:proc.surfaceRays,surfacePropagationVisible:proc.surfacePropagationVisible,edgeMeeting:proc.edgeMeeting,edgeFronts:proc.edgeFronts,k:state.k,visibleLabels:visibleLabels.map(a=>({cell:a.cell,role:a.polarityRoles?.[state.polaritySheet??'negative']??a.role,text:a.polarityText?.[state.polaritySheet??'negative']??a.text})),surfaceCount:surfaces.size,sharedSurfaceCount:[...surfaces.values()].filter(f=>f.count>1).length,proceduralStep:state.step,firstRay:proc.firstRay,faceNeighbors:proc.faceNeighbors,neutronNeighbors:proc.neutronNeighbors,surfaceNeutronNeighbors:proc.surfaceNeutronNeighbors,closureRounds:proc.closureRounds,postMediationRounds:proc.postMediationRounds,surfaceContinuations:proc.surfaceContinuations,surfaceContinuationVisible:proc.surfaceContinuationVisible,nextClosure:proc.nextClosure,comparisonVisible:proc.comparisonVisible,faceVertexComparisons:proc.faceVertexComparisons,mediation:proc.mediation,mediationAvailable:proc.mediationAvailable,mediationVisible:proc.mediationVisible,signalConnections,partners:proc.partners,secondRay:proc.secondRay,thirdRay:proc.thirdRay,returnRay:proc.returnRay,closingRay:proc.closingRay,rays:proc.rays,shownCells:[...shown.keys()].sort((a,b)=>a-b),filledCells,emptySecondCells:[...new Set(continuations.flatMap(ray=>ray.contacts.map(c=>c.cell)))].filter(id=>shown.has(id)&&!filledCells.includes(id)),assignments:proc.assignments,endingCell:proc.end.id,endingCellOutsideEnvelope:false,seed:seed.id,sliceTiles:data.polygons.length,supportPlane:data.plane,rayEndpoint:data.point,rayCells:proc.firstRay?data.traversed.length:0,atStop:data.atStop.length,surfaceFace:data.surfaceFace,pathCells:proc.firstRay?data.traversed:[],edgeCrossings:data.crossings};
  }
  function updateFaceOpacity(){
    if(state.processId==='ruthenium-98'&&state.rutheniumView==='wiring'){
      const opacities=setSulfurWiringOpacity(current,{wireOpacity:state.rutheniumWireOpacity??1});if(audit.rutheniumWiringAudit)audit.rutheniumWiringAudit.wireOpacity=opacities.wireOpacity;
    }
    if(state.processId==='sulfur-32'&&(state.sulfurWireBundle||state.sulfurChannels)){
      const opacities=setSulfurWiringOpacity(current,{wireOpacity:state.sulfurWireOpacity,tubeOpacity:state.sulfurNTubeOpacity});
      if(audit.incomingBundleAudit)audit.incomingBundleAudit.opacities=opacities;
    }
    if(state.processId==='sulfur-32'&&state.sulfurChannels)current.traverse(o=>{if(o.userData.channelCutaway){o.material.opacity=state.faceOpacity;o.material.transparent=state.faceOpacity<1;o.material.depthWrite=state.faceOpacity===1;}});
    if(state.processId==='sulfur-32'&&state.sulfurHandlebody)current.traverse(o=>{if(o.userData.sulfurHandlebodySkin){o.material.opacity=state.faceOpacity;o.material.depthWrite=state.faceOpacity===1;}});
    if(!surfaceBatch||surfaceBatch.faceOpacity===state.faceOpacity)return;
    const colors=surfaceBatch.geometry.getAttribute('color');
    for(const triangle of surfaceBatch.triangles)if(triangle.cellFace){
      const opacity=state.faceOpacity*(['from-center-cell','unsplit-octahedron'].includes(state.processId)?triangle.opacity:1)*(triangle.opacityScale??1);
      for(let i=0;i<3;i++)colors.setW(triangle.base+i,opacity);
    }
    colors.needsUpdate=true;surfaceBatch.faceOpacity=state.faceOpacity;
  }
  function sortSurfaceTriangles(){
    if(!surfaceBatch)return;
    camera.getWorldDirection(sortDirection);
    for(const triangle of surfaceBatch.triangles)triangle.depth=triangle.center.dot(sortDirection);
    surfaceBatch.triangles.sort((a,b)=>b.depth-a.depth||a.base-b.base);
    const index=surfaceBatch.geometry.index.array;
    surfaceBatch.triangles.forEach((triangle,i)=>{index[3*i]=triangle.base;index[3*i+1]=triangle.base+1;index[3*i+2]=triangle.base+2;});
    surfaceBatch.geometry.index.needsUpdate=true;
  }
  function rotationVertices(){return state.processId==='double-esd7'&&state.rimAssembly?envelope.map((p,i)=>(state.cellGraph?wiringParentPoint:geometryParentPoint)(p,i<4?'original':'clone',wiringLabelLayout)):envelope;}
  function complexVertexVisible(p){
    if(state.processId!=='double-esd7')return true;
    const same=q=>q.every((x,i)=>Math.abs(x-p[i])<1e-8),v=state.complexVisibility??{};
    const vertices=state.rimAssembly?rotationVertices():fibrationDisplayEnvelope;
    return (v.original!==false&&vertices.slice(0,4).some(same))||(v.clone!==false&&vertices.slice(4).some(same));
  }
  function rotationConstraint(){
    const fixed=rotationVertices().filter((_,i)=>state.locks[`v${i+1}`]).map(vec);
    return {count:fixed.length,pivot:fixed.length===2?fixed[0]:barycenter,
      axis:fixed.length===2?fixed[1].clone().sub(fixed[0]).normalize():fixed.length===1?fixed[0].clone().sub(barycenter).normalize():null};
  }
  function constrained(q){
    q.normalize();if(q.w<0)q.set(-q.x,-q.y,-q.z,-q.w);
    const a=new T.Vector3(q.x,q.y,q.z),n=a.length();if(n<1e-12)return new T.Quaternion();
    a.multiplyScalar(2*Math.atan2(n,q.w)/n);
    const {count,axis}=rotationConstraint();
    if(count>=3)return new T.Quaternion();
    if(axis)a.copy(axis.clone().multiplyScalar(a.dot(axis)));
    const angle=a.length();return angle<1e-12?new T.Quaternion():new T.Quaternion().setFromAxisAngle(a.divideScalar(angle),angle);
  }
  function rotate(q,line=null){q=line?q:constrained(q);const constraint=rotationConstraint(),pivot=line?line.pivot:constraint.count?constraint.pivot:controls.target.clone();camera.position.sub(pivot).applyQuaternion(q).add(pivot);controls.target.sub(pivot).applyQuaternion(q).add(pivot);camera.up.applyQuaternion(q).normalize();camera.lookAt(controls.target);}
  function matchVertexView(from,to){
    const oldNormal=vec(rotationVertices()[from-1]).sub(barycenter).normalize();
    const newNormal=vec(rotationVertices()[to-1]).sub(barycenter).normalize();
    const q=new T.Quaternion().setFromUnitVectors(oldNormal,newNormal);
    // Keep the corresponding adjacent vertex in the same local frame, resolving
    // the otherwise ambiguous roll about the selected vertex normal.
    const vertexCycle=[2,1,4,3],nextInCycle=v=>vertexCycle[(vertexCycle.indexOf(v)+1)%vertexCycle.length];
    const symmetryPair=(from===1&&to===4)||(from===4&&to===1)||(from===2&&to===3)||(from===3&&to===2);
    const frameVertex=v=>symmetryPair?({1:4,4:1,2:3,3:2}[v]):nextInCycle(v);
    const oldDirection=vec(rotationVertices()[frameVertex(from)-1]).sub(barycenter).projectOnPlane(oldNormal).normalize().applyQuaternion(q);
    const newDirection=vec(rotationVertices()[frameVertex(to)-1]).sub(barycenter).projectOnPlane(newNormal).normalize();
    if(oldDirection.lengthSq()>1e-10&&newDirection.lengthSq()>1e-10){
      const roll=Math.atan2(newNormal.dot(oldDirection.clone().cross(newDirection)),oldDirection.dot(newDirection));
      q.premultiply(new T.Quaternion().setFromAxisAngle(newNormal,roll));
    }
    // P → N1 includes the requested one-third turn about the destination vertex normal.
    if((from===2&&to===1)||(from===1&&to===2))q.premultiply(new T.Quaternion().setFromAxisAngle(newNormal,(from===2?1:-1)*2*Math.PI/3));
    // Explicit view selection, like restoreView, is independent of drag locks.
    camera.position.sub(barycenter).applyQuaternion(q).add(barycenter);
    controls.target.sub(barycenter).applyQuaternion(q).add(barycenter);
    camera.up.applyQuaternion(q).normalize();camera.lookAt(controls.target);
    cellHover.clear();
  }
  function updateControls(){
    const before=camera.quaternion.clone(),oldTarget=controls.target.clone(),offset=camera.position.clone().sub(oldTarget),up=camera.up.clone();controls.update();
    if(Object.values(state.locks).some(Boolean)){
      const q=constrained(camera.quaternion.clone().multiply(before.invert())),r=camera.position.distanceTo(controls.target);
      const pan=controls.target.clone().sub(oldTarget),pivot=rotationConstraint().pivot;
      camera.position.copy(offset.normalize().multiplyScalar(r)).add(oldTarget).sub(pivot).applyQuaternion(q).add(pivot).add(pan);
      controls.target.copy(oldTarget).sub(pivot).applyQuaternion(q).add(pivot).add(pan);
      camera.up.copy(up).applyQuaternion(q).normalize();camera.lookAt(controls.target);
    }
    camera.zoom=T.MathUtils.clamp(camera.zoom,.2,20);camera.updateProjectionMatrix();
  }
  function orientation(){
    const s=new T.Spherical().setFromVector3(camera.position.clone().sub(controls.target));
    const azimuth=T.MathUtils.radToDeg(s.theta),elevation=90-T.MathUtils.radToDeg(s.phi);
    camera.updateMatrixWorld();
    const displayedVertices=rotationVertices(),doubleParent=state.processId==='double-esd7'&&displayedVertices.length===8;
    const vertexLabels=layoutVertexLabels(displayedVertices.map((p,i)=>{
      const anchor=vec(p).project(camera),owner=doubleParent?displayedVertices.slice(i<4?0:4,i<4?4:8):displayedVertices;
      const ownerCenter=owner.map(vec).reduce((s,p)=>s.add(p),new T.Vector3()).divideScalar(owner.length).project(camera);
      return {key:`v${i+1}`,index:i+1,text:`V${['₁','₂','₃','₄','₅','₆','₇','₈'][i]}${state.processId==='double-esd7'&&!state.rimAssembly?' '+doubleEsd7VertexLabels[i]:''}`,anchorX:(anchor.x+1)*width/2,anchorY:(1-anchor.y)*height/2,centerX:(ownerCenter.x+1)*width/2,centerY:(1-ownerCenter.y)*height/2,visible:!['sulfur-32','single-octahedral','signed-octahedral-belt','native-octahedral-bridge'].includes(state.processId)&&!(state.processId==='double-esd7'&&state.rimAssembly&&(state.parentHalfStepTrim||[0,1,6].includes(i)))&&complexVertexVisible(p)&&Math.abs(anchor.x)<=1&&Math.abs(anchor.y)<=1&&Math.abs(anchor.z)<=1};
    }),{width,height});
    const inspected=inspectionCell===null?null:vec(cells[inspectionCell].vertices[0].map((_,i)=>cells[inspectionCell].vertices.reduce((sum,p)=>sum+p[i]/4,0))).project(camera);
    latestView={inspection:inspected?{cell:inspectionCell,ndc:inspected.toArray()}:null,camera:{offset:camera.position.clone().sub(controls.target).toArray(),targetOffset:controls.target.clone().sub(barycenter).toArray(),up:camera.up.toArray(),zoom:camera.zoom},vertexLocks:{...state.locks},vertexLabels,quaternion:camera.quaternion.toArray(),cameraUp:camera.up.toArray(),projection:camera.type,zoom:camera.zoom,frustum:[camera.left,camera.right,camera.top,camera.bottom],azimuth,elevation,autoRotate:state.spin,axialRotate:!!state.axialRotation,target:controls.target.toArray(),constructionDirection:direction.toArray()};
    onView(latestView,audit);
  }
  function render(time){
    frame=0;if(disposed||document.hidden||!inView)return;
    try{
      const key=JSON.stringify([state.processId,state.k,state.step,state.branch,state.prior,state.bodies,state.esd7Planes,state.beltLayers,state.nativeBeltLayers,state.complexVisibility,state.rimAssembly,state.parentHalfStepTrim,state.seamBelts,state.internalElectronSelf,state.doubleRules,state.cellGraph,state.rutheniumView,state.coherenceGroup,state.sulfurWireBundle,state.sulfurChannels,state.sulfurChannelCut,state.sulfurChannelOpen,state.sulfurChannelNormal,state.sulfurNTubeMarkers,state.sulfurNIdentity,state.sulfurHandlebody,state.sulfurTubes,state.highlightRulePreview,state.edgesOnly,state.showCellInfo,state.labels,state.grid,state.polaritySheet,state.singleFaceColoring,state.nTubeAxis,state.cut,state.processId==='fibration-12x12'?[state.selectedNeutralMode,state.neutralValues]:null]);if(key!==buildKey){rebuild();buildKey=key;}
      updateControls();const dt=Math.min(previousTime?(time-previousTime)/1000:0,.05);previousTime=time;
      const constraint=rotationConstraint(),axial=state.axialRotation&&state.processId==='double-esd7'?protonRotationLine(state.rimAssembly,state.cellGraph):null;
      const normalSpinning=state.spin&&constraint.count<3&&state.speed!==0;
      const axialSpinning=axial&&state.speed!==0&&locksAllowAxialRotation(axial,rotationVertices().filter((_,i)=>state.locks[`v${i+1}`]).map(vec));
      const spinning=normalSpinning||axialSpinning;
      if(normalSpinning)rotate(new T.Quaternion().setFromAxisAngle(constraint.axis??new T.Vector3(0,1,0),dt*state.speed*.3));
      if(axialSpinning)rotate(new T.Quaternion().setFromAxisAngle(axial.axis,dt*state.speed*.3),axial);
      orientation();updateFaceOpacity();cellHover.update();renderer.info.reset();
      if(state.edgesOnly||(state.processId==='sulfur-32'&&(state.sulfurHandlebody||state.sulfurChannels)))renderer.render(scene,camera);
      else if(faceCompositor)faceCompositor.render(scene,camera,surfaceBatch.mesh,state.faceOpacity===1&&!surfaceBatch.hasTranslucentFaces);
      else {
        surfaceBatch.mesh.material.transparent=state.faceOpacity<1||surfaceBatch.hasTranslucentFaces;surfaceBatch.mesh.material.depthWrite=!surfaceBatch.mesh.material.transparent;
        if(surfaceBatch.mesh.material.transparent)sortSurfaceTriangles();renderer.render(scene,camera);
      }
      draws++;fallback.hidden=true;
      if(interacting||spinning)requestRender();else previousTime=0;
    }catch(e){fail(e);}
  }
  function start(){interacting=true;requestRender();}function end(){interacting=false;requestRender();}
  let width=0,height=0,ratio=0;
  function resize(force=false){
    if(disposed)return;const size=host.getBoundingClientRect(),dpr=Math.min(devicePixelRatio||1,2);
    if(size.width<=0||size.height<=0)return;
    if(!force&&size.width===width&&size.height===height&&ratio===dpr)return;
    width=size.width;height=size.height;ratio=dpr;renderer.setPixelRatio(ratio);renderer.setSize(width,height,false);faceCompositor?.resize();
    const aspect=width/height,h=halfSpan/Math.min(1,aspect);camera.left=-h*aspect;camera.right=h*aspect;camera.top=1.25*h;camera.bottom=-.75*h;camera.updateProjectionMatrix();controls.handleResize();requestRender();
  }
  function densityChanged(){densityQuery?.removeEventListener('change',densityChanged);densityQuery=matchMedia(`(resolution: ${devicePixelRatio}dppx)`);densityQuery.addEventListener('change',densityChanged);resize();}
  function reset(){camera.up.set(0,1,0);controls.target.copy(barycenter);camera.position.copy(barycenter).add(new T.Vector3().setFromSphericalCoords(10,T.MathUtils.degToRad(158),T.MathUtils.degToRad(67)));camera.zoom=1;camera.lookAt(controls.target);requestRender();}
  function aim(d){if(disposed)return;rotate(new T.Quaternion().setFromUnitVectors(camera.position.clone().sub(controls.target).normalize(),d.normalize()));requestRender();}
  try{
    renderer=new T.WebGLRenderer({antialias:true});renderer.domElement.setAttribute('role','img');renderer.domElement.setAttribute('aria-label','Lattice slice and normal-ray procedure; camera controls provide keyboard navigation.');renderer.domElement.setAttribute('aria-describedby','instructions');renderer.domElement.className='webgl-canvas';host.append(renderer.domElement);
    renderer.info.autoReset=false;faceCompositor=createFaceCompositor(renderer);camera.layers.enable(1);
    camera.position.set(4,3,5);controls=new TrackballControls(camera,renderer.domElement);controls.staticMoving=true;controls.rotateSpeed=2;controls.noPan=false;
    cellHover=createCellHover({scene,camera,canvas:renderer.domElement,host,signal:lifetime.signal,requestRender,onHover:onCellHover});
    marker=dot(cache[0].point,.065,0xffffff);scene.add(marker);
    controls.addEventListener('change',requestRender);controls.addEventListener('start',start);controls.addEventListener('end',end);
    listen(renderer.domElement,'webglcontextlost',e=>{e.preventDefault();fail(new Error('3D context lost. Reload to retry.'));});
    listen(document,'visibilitychange',()=>{stopFrame();requestRender();});
    listen(window,'pagehide',e=>{if(e.persisted)stopFrame();else dispose();});listen(window,'pageshow',e=>{if(e.persisted)requestRender();});
    resizeObserver=new ResizeObserver(resize);resizeObserver.observe(host);listen(window,'resize',resize);
    intersectionObserver=new IntersectionObserver(([entry])=>{inView=entry.isIntersecting;stopFrame();requestRender();});intersectionObserver.observe(host);
    reset();densityChanged();resize();signal.throwIfAborted();requestRender();
    return Object.freeze({
      update(next){
        if(disposed)return;
        const changedK=(next.processId==='ruthenium-98'&&(state.rutheniumView==='wiring')!==(next.rutheniumView==='wiring'))||(next.processId==='sulfur-32'&&(state.sulfurWireBundle!==next.sulfurWireBundle||state.sulfurChannels!==next.sulfurChannels))||(next.processId==='single-octahedral'&&(state.nTubeAxis==='coupled')!==(next.nTubeAxis==='coupled'))||(['single-octahedral','signed-octahedral-belt','native-octahedral-bridge'].includes(next.processId)&&state.step!==next.step)||state.k!==next.k||state.processId!==next.processId||(next.processId==='double-esd7'&&state.rimAssembly!==next.rimAssembly);
        const numericVertex=Number.isInteger(next.cut?.vertex)&&next.cut.vertex>=1&&next.cut.vertex<=4;
        const selectedVertex=!changedK&&next.processId==='cell-fibration'&&numericVertex&&next.cut.vertex!==state.cut?.vertex&&lastCutVertex!==null;
        state={...next,locks:{...next.locks},cut:next.cut?{...next.cut}:undefined};
        if(changedK){
          inspectionCell=null;
          const previousCenter=barycenter;
          envelope=state.processId==='ruthenium-98'?singleOctahedralEnvelope(2):state.processId==='sulfur-32'?singleOctahedralEnvelope(1):state.processId==='single-octahedral'?singleOctahedralEnvelope(state.step+(state.nTubeAxis==='coupled'?1:0)):state.processId==='native-octahedral-bridge'?nativeBridgeEnvelope(state.step):state.processId==='signed-octahedral-belt'?signedOctahedralEnvelope(state.step):state.processId==='neutron-belt'?neutronBeltEnvelope:state.processId==='double-esd7'?(state.rimAssembly?centralBeltEnvelope:doubleEsd7Envelope):state.processId==='pair-context-7x4'?pairContextEnvelope:['cell-fibration','fibration-12x12'].includes(state.processId)?foldedFibrationEnvelope:state.processId==='unsplit-octahedron'?[0,1,2,3].map(i=>[0,1,2,3].map(j=>.25+2*(Number(i===j)-.25))):envelopeAt(state.k);barycenter=rotationVertices().map(vec).reduce((s,p)=>s.add(p),new T.Vector3()).divideScalar(rotationVertices().length);
          const fitPoints=state.processId==='ruthenium-98'&&state.rutheniumView==='wiring'?[...envelope,...buildFiveSideOctWiring().strands.flatMap(s=>s.points)]:state.processId==='sulfur-32'&&state.sulfurWireBundle?[...envelope,...buildSulfurIncomingBundle().strands.flatMap(s=>s.points)]:envelope;
          halfSpan=Math.max(...fitPoints.map(p=>vec(p).distanceTo(barycenter)))*1.15;
          const delta=barycenter.clone().sub(previousCenter);controls.target.add(delta);camera.position.add(delta);
          resize(true);
        }
        if(selectedVertex)matchVertexView(lastCutVertex,state.cut.vertex);
        if(changedK)lastCutVertex=null;
        if(state.processId==='cell-fibration'&&numericVertex)lastCutVertex=state.cut.vertex;
        if(grid){grid.visible=state.grid;grid.material.opacity=Math.min(1,state.opacity*3.75);}requestRender();
      },
      focusCell(cell,zoom=3){
        if(disposed)return;
        if(!Number.isInteger(cell)||!cells[cell]||cells[cell].vertices.some(p=>p[0]>-5+state.k)||!Number.isFinite(zoom)||zoom<=0)throw Error('Invalid inspection cell or zoom');
        const point=cells[cell].vertices[0].map((_,i)=>cells[cell].vertices.reduce((sum,p)=>sum+p[i]/4,0));
        inspectionCell=cell;
        const offset=camera.position.clone().sub(controls.target);camera.zoom=T.MathUtils.clamp(zoom,.2,20);
        const up=new T.Vector3(0,1,0).applyQuaternion(camera.quaternion);
        controls.target.copy(vec(point)).addScaledVector(up,-(camera.top+camera.bottom)/2);
        camera.position.copy(controls.target).add(offset);camera.lookAt(controls.target);camera.updateProjectionMatrix();requestRender();
      },
      restoreView(saved){
        if(disposed||!saved)return;
        controls.target.copy(barycenter).add(new T.Vector3(...saved.targetOffset));
        camera.position.copy(controls.target).add(new T.Vector3(...saved.offset));camera.up.fromArray(saved.up).normalize();camera.zoom=saved.zoom;
        camera.lookAt(controls.target);camera.updateProjectionMatrix();requestRender();
      },
      angles(az,el){aim(new T.Vector3().setFromSphericalCoords(1,T.MathUtils.degToRad(90-el),T.MathUtils.degToRad(az)));},
      axis(name){aim(({x:new T.Vector3(1,0,0),y:new T.Vector3(0,1,0),z:new T.Vector3(0,0,1)})[name]);},
      ray(){aim(direction.clone().negate());},
      orbit(axis,angle){if(!disposed){rotate(new T.Quaternion().setFromAxisAngle(new T.Vector3(...({x:[1,0,0],y:[0,1,0],z:[0,0,1]})[axis]),angle));requestRender();}},
      zoom(factor){if(!disposed){camera.zoom=T.MathUtils.clamp(camera.zoom*factor,.2,20);camera.updateProjectionMatrix();requestRender();}},
      reset(){if(!disposed){state.locks={v1:false,v2:false,v3:false,v4:false,v5:false};state.spin=false;state.axialRotation=false;reset();}},
      dispose,
      clearCellHover:()=>cellHover.clear(),
      snapshot:()=>({faceAlphaValues:surfaceBatch?[...new Set(surfaceBatch.triangles.filter(t=>t.cellFace).map(t=>surfaceBatch.geometry.attributes.color.getW(t.base)))]:[],hover:cellHover.snapshot(),disposed,scheduled:Boolean(frame),draws,rebuilds,calls:renderer.info.render.calls,transparency:state.edgesOnly?'edges-only':faceCompositor?'weighted-oit':'sorted-fallback',edgesOnly:Boolean(state.edgesOnly),faceOpacity:state.faceOpacity,view:latestView,process:audit,
        vertices:rotationVertices().map((address,i)=>({label:`V_${i+1}`,address:[...address]}))}),
    });
  }catch(error){dispose();throw error;}
}
