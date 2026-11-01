// Appended to the supplied viewer by scripts/build-reference-port-routing.mjs.
(() => {
  const viewer=window.auditViewer;
  const router=createPortRouter(viewer.data);
  const byRequest=new Map();
  const labels=['O','A','B','D','E'];
  function payloadFor(id) {
    if(!byRequest.has(id)) byRequest.set(id,Object.fromEntries(labels.map(label=>[label,`request-${id+1}:${label}`])));
    return byRequest.get(id);
  }
  function getPacket() {
    const state=viewer.getState();
    return router.packet({requestId:state.id,routeIndex:state.choice,reverse:state.reversed,
      position:state.position,lift:document.getElementById('lift').value,payload:payloadFor(state.id)});
  }
  const form=document.getElementById('packet-inputs');
  for(const label of labels) {
    const field=document.createElement('label');field.textContent=label;
    const input=document.createElement('input');input.id=`payload-${label}`;input.type='text';
    input.setAttribute('aria-label',`Payload for ${label}`);
    input.addEventListener('input',()=>{payloadFor(viewer.getState().id)[label]=input.value;refreshPacket();});
    field.append(input);form.append(field);
  }
  function refreshPacket() {
    const packet=getPacket();
    for(const slot of packet.slots) document.getElementById(`payload-${slot.label}`).value=slot.value;
    document.getElementById('packet-summary').textContent=
      `${packet.historyFrom} → ${packet.historyTo} · C${packet.currentCell}\n`+
      `Ingress: ${packet.ingress?.id??'source'}\nEgress: ${packet.egress?.id??'delivered'}`+
      (packet.pairedEgress?` → ${packet.pairedEgress.id}`:'')+
      `\nTraversed: ${packet.visitedRoute.map(c=>`C${c}`).join(' → ')}`;
    const tbody=document.getElementById('values');tbody.replaceChildren();
    for(const slot of packet.slots) {
      const row=document.createElement('tr');
      for(const text of [slot.label,slot.value,`(${slot.coordinates.join(', ')})`]) {
        const td=document.createElement('td');td.textContent=text;row.append(td);
      }
      tbody.append(row);
    }
    document.getElementById('transform').textContent=
      'Composed transport from route source to current cell (exact):\n'+JSON.stringify(packet.transport)+
      '\n\nEndpoint transport in the selected direction:\n'+JSON.stringify(packet.endpointTransport)+
      '\nHidden coordinates and inherited payload labels are retained.';
    document.getElementById('packet-record').textContent=JSON.stringify(packet,null,2);
    document.getElementById('packet-audit').textContent=
      `${router.audit.requests} requests · ${router.audit.simpleRoutes} simple routes · ${router.audit.seams} seam maps checked with exact arithmetic on load.`;
  }
  // The original viewer remains the owner of navigation and drawing.
  const baseRender=render;
  render=function(){baseRender();refreshPacket();};
  window.referenceRouting={router,getPacket,refresh:refreshPacket};
  refreshPacket();
})();
