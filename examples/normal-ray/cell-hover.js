import * as T from 'three';
import {LineSegments2} from 'three/addons/lines/LineSegments2.js';
import {LineSegmentsGeometry} from 'three/addons/lines/LineSegmentsGeometry.js';
import {LineMaterial} from 'three/addons/lines/LineMaterial.js';
import {simplexCellPath} from '../../research/realization-tower/simplex-cell-movement.mjs';

// Picking owns separate, never-rendered face meshes. Wire mode picks actual edges.
export function createCellHover({scene,camera,canvas,host,signal,requestRender,onHover}){
 const raycaster=new T.Raycaster(),pointer=new T.Vector2();raycaster.params.Line2={threshold:3};raycaster.layers.enable(1);
 const pickMaterial=new T.MeshBasicMaterial({side:T.DoubleSide}),emptyEdgeMaterial=new LineMaterial({linewidth:3,worldUnits:false});
 let enabled=false,edgesOnly=false,entries=[],targets=[],cursor=null,press=null,pendingClick=null,pressCtrl=false,pinned=false,hovered=null,hoverHighlight=null,lastMessage='',disposed=false;
 let selection=[],selectionHighlights=new Map(),selectionPosition=null;
 const listen=(target,event,fn)=>target.addEventListener(event,fn,{signal});
 const pointKey=p=>p.toArray().map(x=>x.toFixed(8)).join(',');
 function disposeHighlight(obj){if(obj){scene.remove(obj);obj.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});}}
 function showTubeShape(outline,entry){
  const r=canvas.getBoundingClientRect();outline.material.resolution.set(r.width,r.height);
  if(entry.info.kind!=='tube'||!entry.target?.isMesh)return;
  entry.target.updateMatrixWorld(true);
  const fill=new T.Mesh(entry.target.geometry.clone(),new T.MeshBasicMaterial({color:0xffce66,transparent:true,opacity:.3,side:T.DoubleSide,depthTest:false,depthWrite:false}));
  fill.matrixAutoUpdate=false;fill.matrix.copy(entry.target.matrixWorld);fill.layers.set(1);fill.renderOrder=outline.renderOrder-1;outline.add(fill);
 }
 function clearSelection(){for(const obj of selectionHighlights.values())disposeHighlight(obj);selectionHighlights.clear();selection=[];selectionPosition=null;}
 function hoverEntry(entry){
  if(hovered!==entry){hovered=entry;disposeHighlight(hoverHighlight);hoverHighlight=null;
   if(entry){hoverHighlight=new LineSegments2(new LineSegmentsGeometry().setPositions(entry.segments.flatMap(p=>p.toArray())),new LineMaterial({color:0xffce66,linewidth:4,worldUnits:false,depthTest:false,depthWrite:false}));hoverHighlight.renderOrder=20;hoverHighlight.layers.set(1);showTubeShape(hoverHighlight,entry);scene.add(hoverHighlight);}
  }
 }
 function constraints(){
  const result=[];
  for(let i=0;i<selection.length;i++)for(let j=i+1;j<selection.length;j++){
   const a=selection[i],b=selection[j];if(a.info.kind==='tube'||b.info.kind==='tube')continue;
   const sharedFacets=[...a.facetKeys].filter(k=>b.facetKeys.has(k)).length;
   const commonLayers=(a.info.layers??[]).flatMap((v,n)=>v===b.info.layers?.[n]?[n+1]:[]);
   result.push({from:a.info.id,to:b.info.id,sharedFacets,commonLayers,roles:[a.info.role,b.info.role],roleCompatible:a.info.role===b.info.role,
    forward:simplexCellPath(a.info.geometryId,b.info.geometryId),reverse:simplexCellPath(b.info.geometryId,a.info.geometryId)});
  }
  return result;
 }
 function publish(){
  let message=null;
  if(selection.length){
   const r=host.getBoundingClientRect(),pos=selectionPosition??cursor??{x:r.left+r.width/2,y:r.top+r.height/2},width=Math.min(360,r.width-16);
   message={selection:selection.map(e=>e.info),sharedConstraints:constraints(),pinned:true,x:Math.max(8,Math.min(pos.x-r.left+16,r.width-width-8)),y:Math.max(8,Math.min(pos.y-r.top+16,r.height-330))};
  }else if(hovered&&cursor){
   const r=host.getBoundingClientRect(),width=Math.min(310,r.width-16);
   message={...hovered.info,pinned,x:Math.max(8,Math.min(cursor.x-r.left+16,r.width-width-8)),y:Math.max(8,Math.min(cursor.y-r.top+16,r.height-330))};
  }
  const text=JSON.stringify(message);if(text!==lastMessage){lastMessage=text;onHover(message);}
 }
 function clear(){cursor=null;press=null;pendingClick=null;pinned=false;clearSelection();hoverEntry(null);publish();requestRender();}
 function reset(){clear();for(const e of entries)e.proxy?.geometry.dispose();entries=[];targets=[];}
 function addToSelection(entry,point){
  if(!entry||selection.includes(entry))return;
  selection.push(entry);selectionPosition=point;
  const outline=new LineSegments2(new LineSegmentsGeometry().setPositions(entry.segments.flatMap(p=>p.toArray())),new LineMaterial({color:0xffce66,linewidth:5,worldUnits:false,depthTest:false,depthWrite:false}));
  outline.renderOrder=21;outline.layers.set(1);showTubeShape(outline,entry);scene.add(outline);selectionHighlights.set(entry,outline);
 }
 listen(canvas,'pointermove',e=>{if(!enabled)return;if(press)press.moved ||= Math.hypot(e.clientX-press.x,e.clientY-press.y)>4;if(pinned&&!selection.length)return;cursor={x:e.clientX,y:e.clientY};requestRender();});
 listen(canvas,'pointerdown',e=>{if(!enabled)return;press={x:e.clientX,y:e.clientY,moved:false};pressCtrl=e.ctrlKey||e.metaKey;});
 listen(canvas,'pointerup',e=>{if(enabled&&press&&!press.moved&&e.button===0){pendingClick={ctrl:e.ctrlKey||e.metaKey||pressCtrl,point:{x:e.clientX,y:e.clientY}};cursor=pendingClick.point;}press=null;pressCtrl=false;requestRender();});
 listen(canvas,'pointercancel',()=>{press=null;if(!selection.length&&!pinned)hoverEntry(null);});
 listen(canvas,'pointerleave',()=>{press=null;if(!selection.length&&!pinned){hoverEntry(null);publish();}});
 listen(window,'pointerdown',e=>{
  if(!enabled||e.target.closest?.('#cell-hover-info'))return;
  // Release a pinned tooltip before the next canvas pick, even on empty space.
  pinned=false;hoverEntry(null);
  if(!e.ctrlKey&&!e.metaKey)clearSelection();
  if(!canvas.contains(e.target)){cursor=null;press=null;pendingClick=null;}
  publish();requestRender();
 });
 listen(window,'keydown',e=>{if(e.key==='Escape'&&enabled)clear();});
 return {
  begin(nextEnabled,nextEdgesOnly){reset();enabled=Boolean(nextEnabled);edgesOnly=Boolean(nextEdgesOnly);if(!enabled)cursor=null;},
  add(info,faces,segments,edgeObject,pickObject=null){
   if(!enabled)return;
   const entry={info,segments,facetKeys:new Set(faces.map(face=>face.map(pointKey).sort().join('|'))),proxy:null};let target=pickObject??edgeObject;
   if(!pickObject&&!edgesOnly){const positions=[];for(const f of faces)for(let i=1;i<f.length-1;i++)for(const p of [f[0],f[i],f[i+1]])positions.push(...p.toArray());target=new T.Mesh(new T.BufferGeometry().setAttribute('position',new T.Float32BufferAttribute(positions,3)),pickMaterial);target.updateMatrixWorld(true);entry.proxy=target;}
   if(edgesOnly&&!target&&info.unfilled){target=new LineSegments2(new LineSegmentsGeometry().setPositions(segments.flatMap(p=>p.toArray())),emptyEdgeMaterial);entry.proxy=target;}
   if(!target)return;const pickTargets=Array.isArray(target)?target:[target];entry.target=pickTargets[0];for(const object of pickTargets)object.userData.hoverEntry=entry;entries.push(entry);targets.push(...pickTargets);
  },
  update(){
   if(!enabled)return;
   if(hovered?.info.kind==='tube'&&hovered.target.material.opacity===0){pinned=false;hoverEntry(null);}
   if(pinned&&!selection.length){publish();return;}
   if(!cursor||press){if(!selection.length)hoverEntry(null);publish();return;}
   const r=canvas.getBoundingClientRect();if(!r.width||!r.height)return;
   pointer.set((cursor.x-r.left)/r.width*2-1,-(cursor.y-r.top)/r.height*2+1);camera.updateMatrixWorld();
   for(const target of targets){target.updateMatrixWorld(true);if(target.isLineSegments2)target.material.resolution.set(r.width,r.height);}
   for(const obj of selectionHighlights.values())obj.material.resolution.set(r.width,r.height);
   if(hoverHighlight)hoverHighlight.material.resolution.set(r.width,r.height);
   raycaster.setFromCamera(pointer,camera);const hits=raycaster.intersectObjects(targets.filter(t=>t.userData.hoverEntry.info.kind!=='tube'||t.material.opacity>0),false);
   // Tube shells are an overlay: pick the visible overlay before underlying cells.
   let hit=hits.find(h=>h.object.userData.hoverEntry.info.kind==='tube')??hits[0];
   if(edgesOnly&&hit)hit=hits.find(h=>Math.abs(h.distance-hit.distance)<1e-6&&(h.object.userData.hoverEntry.info.unfilled||h.object.userData.hoverEntry.info.conflicts?.length))??hit;
   if(pendingClick){
    const click=pendingClick;pendingClick=null;
    if(click.ctrl){if(hit)addToSelection(hit.object.userData.hoverEntry,click.point);}
    else{clearSelection();pinned=Boolean(hit);hoverEntry(hit?.object.userData.hoverEntry??null);cursor=click.point;}
   }
   if(!selection.length&&!pinned)hoverEntry(hit?.object.userData.hoverEntry??null);
   publish();
  },
  clear,
  snapshot:()=>({enabled,edgesOnly,targetCount:entries.length,pinned,highlighted:Boolean(hoverHighlight),highlightOverlay:Boolean(hoverHighlight?.layers.isEnabled(1)),selectedHighlights:selectionHighlights.size,cell:hovered?.info??null,selection:selection.map(e=>e.info)}),
  dispose(){if(disposed)return;disposed=true;reset();pickMaterial.dispose();emptyEdgeMaterial.dispose();enabled=false;},
 };
}
