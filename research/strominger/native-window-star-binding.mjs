import {windowProtocol} from './demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {bindSourceFibers,restoreSourceFibers} from '../realization-tower/belt-source-fiber-binding.mjs';
import {validateNativeFixture} from './retained-diagram-audit.mjs';
import {boundary,composeEvidence} from './fibration-evidence.mjs';
import {isDeepStrictEqual as equal} from 'node:util';
const sameSet=(a,b)=>a.length===b.length&&new Set(a).size===a.length&&a.every(x=>b.includes(x));
// A source-bound presentation annotation. No field coordinate is identified with
// a vertex, star arm, particle role or geometric context merely by equal count.
export function nativeWindowStarView(fixture,packetId,layer,{markOrder=null}={}){
 const packet=fixture.packets.find(p=>p.id===packetId);if(!packet)throw Error('Unknown native packet');
 const chart=fixture.charts.find(c=>c.index===packet.chart),protocol=windowProtocol.find(p=>p.species===chart?.species),cell=fixture.cells.find(c=>c.id===chart?.cell);
 if(!protocol||!cell)throw Error('Missing native chart/carrier');
 const marks=markOrder??[...protocol.nodes];if(!sameSet(marks,protocol.nodes))throw Error('Mark order must retain the actual four protocol nodes');
 const vertices=marks.map(mark=>chart.aliases[mark]);if(!sameSet(vertices,cell.vertices))throw Error('Marked window nodes do not cover the actual native carrier');
 const window=protocol.window.map(mark=>({mark,vertex:chart.aliases[mark]})),context={mark:protocol.continuation,vertex:chart.aliases[protocol.continuation]};
 if(window.length!==3||window.some(w=>w.vertex===context.vertex)||!sameSet([...window.map(w=>w.vertex),context.vertex],vertices))throw Error('Invalid native three-plus-one window');
 if(!cell.faces.some(face=>sameSet(face,window.map(w=>w.vertex))))throw Error('Selected native window is not an actual carrier face');
 const packetRef={packet:packet.id,chart:chart.index,cell:cell.id,origin:packet.origin,permutation:[...packet.permutation]};
 const historyPositions=fixture.histories.flatMap(h=>h.packets.flatMap((id,after)=>id===packet.id?[{history:h.id,after}]:[]));
 const rows=vertices.flatMap((source,s)=>vertices.flatMap((target,t)=>s===t?[]:[{label:4*s+t,source,target,payload:{packetRef,sourceMark:marks[s],targetMark:marks[t],historyPositions}}]));
 const binding=bindSourceFibers(rows,layer,{marking:vertices,history:historyPositions}),stars=binding.centres.map(centre=>{
  const mark=marks[vertices.indexOf(centre.endpoint)],selected=mark===context.mark;
  const face=vertices.filter(v=>v!==centre.endpoint),nativeFace=cell.faces.find(f=>sameSet(f,face));if(!nativeFace)throw Error('Formal context complement is not a tetrahedral face');
  const satellites=binding.satellites.filter(s=>s.star===vertices.indexOf(centre.endpoint));
  return {node:centre.node,contextMark:mark,contextVertex:centre.endpoint,selectedByProtocol:selected,admission:selected?'existing-native-window':'alternative-geometric-context-only',face:[...nativeFace],satellites:satellites.map(s=>({node:s.node,arm:s.arm,rowLabel:s.row.label,targetMark:s.row.payload.targetMark,targetVertex:s.row.target})),orderedNativeWindow:selected?window.map(w=>satellites.find(s=>s.row.target===w.vertex).node):null};
 });
 return {packetRef,marks,vertices,protocol:{species:protocol.species,window:[...protocol.window],continuation:protocol.continuation},window,context,historyPositions,rows,binding,stars,scope:'One actual native packet viewed through four marked geometric contexts. Only the supplied protocol window is selected; other faces are not new certified native operations. Full coefficients remain in the referenced packet, not split among satellites.'};
}
export function auditNativeWindowStarViews(fixture,layer){
 const errors=validateNativeFixture(fixture);if(errors.length)throw Error(`Malformed native fixture: ${JSON.stringify(errors)}`);
 const views=fixture.packets.map(p=>nativeWindowStarView(fixture,p.id,layer));
 const perCarrierContexts=[...new Set(views.map(v=>v.packetRef.cell))].map(cell=>{const members=views.filter(v=>v.packetRef.cell===cell),anchorVertices=members[0].vertices;return {cell,anchorVertices,observedContextIndices:[...new Set(members.map(v=>anchorVertices.indexOf(v.context.vertex)))].sort(),packets:members.map(v=>({packet:v.packetRef.packet,contextVertex:v.context.vertex,contextIndex:anchorVertices.indexOf(v.context.vertex),origin:v.packetRef.origin,historyPositions:v.historyPositions}))};});
 const checks=[{id:'all-packets-covered',passed:views.length===fixture.packets.length},{id:'one-source-selected-context-per-packet',passed:views.every(v=>v.stars.filter(s=>s.selectedByProtocol).length===1)},{id:'all-sector-rows-recover',passed:views.every(v=>equal(restoreSourceFibers(v.binding),v.rows))},{id:'full-five-coefficient-references-retained',passed:views.every(v=>equal(v.packetRef.permutation,fixture.packets.find(p=>p.id===v.packetRef.packet).permutation))}];
 const record={id:'native:window-stars',adapter:'native-window-stars',input:boundary('native-diagram',fixture),output:boundary('native-window-star-views',views),dependsOn:[],premises:[{id:'window-stars:layout-convention',status:'assumed',statement:'Map ordered local protocol marks to the four displayed star indices and XOR-difference arms. This is a declared presentation adapter, not a derived spatial or field coupling.'}],claim:'Each native packet supplies a witnessed ordered three-plus-context face, retained exactly within its four-context star presentation.',checks};
 return {status:checks.every(c=>c.passed)?'native-selected-window-bound':'rejected',views,perCarrierContexts,record,composition:composeEvidence([record]),counts:{packets:views.length,selectedWindows:views.length,alternativeGeometricContexts:views.length*3},unresolved:['No native operation or full-field readout is assigned to the three unselected contexts of a packet.','No independent scalar amplitude is assigned to the context vertex or to a satellite.','A common fixed four-star frame across changing native carriers is not supplied by reindexing each local protocol.','Actual ESD7 parent-to-belt attachment remains unbound.']};
}
