import * as M from './model.mjs';
import proof from './identity-data.mjs';
import * as Carrier from './carrier.mjs?v=face-centers';

const rational=x=>{const [a,b='1']=String(x).split('/');return Number(a)/Number(b);};
const multiply=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]];
const complex=z=>[rational(z.real),Math.sqrt(3)*rational(z.imaginary_sqrt3_coefficient)];
const average=points=>points[0].map((_,i)=>points.reduce((sum,p)=>sum+p[i],0)/points.length);
const delta=(a,b)=>a.map((v,i)=>v-b[i]);
const modeLambda={common:[1,0],positive:[-.5,Math.sqrt(3)/2],negative:[-.5,-Math.sqrt(3)/2]};
export const identityProof=proof;

export function identityState({view='lattice',geometry='chart',electronTrial=false,angle=0,progress=0,route='all',mode='positive',phase=0}={}) {
  if(!Object.hasOwn(modeLambda,mode))throw new RangeError('Unknown spectral mode');
  const carrier=electronTrial?Carrier.trial:Carrier;
  const routes=geometry==='carrier'?M.routes.filter(r=>carrier.bodies.some(b=>b.id===r.id)):M.routes;
  const coords=geometry==='carrier'?carrier.points:M.coordinatesFor(view),stage=route==='all'?Math.min(routes.length-1,progress<1?0:progress<3?1:2):routes.findIndex(r=>r.id===route);
  if(stage<0)throw new RangeError('Unknown identity window');
  const anchors=routes.map(r=>average(r.nodes.map(n=>coords[n])));
  let branch=mode,transport=[1,0];const branchPath=[branch];
  for(let k=0;k<stage;k++) {const next=proof.transitions[k].mode_transport[branch];branch=next.target_mode;transport=multiply(transport,complex(next.phase));branchPath.push(branch);}
  const probe=[Math.cos(phase*Math.PI/180),Math.sin(phase*Math.PI/180)],total=multiply(transport,probe);
  const lambda=modeLambda[branch],weights=[[1,0],lambda,multiply(lambda,lambda)].map(z=>multiply(total,z));
  const r=routes[stage],anchor=anchors[stage];
  const re=anchor.map((_,axis)=>r.nodes.reduce((sum,n,i)=>sum+(coords[n][axis]-anchor[axis])*weights[i][0],0));
  const im=anchor.map((_,axis)=>r.nodes.reduce((sum,n,i)=>sum+(coords[n][axis]-anchor[axis])*weights[i][1],0));
  // First-seen assembly and chronological occurrence averaging are deliberately distinct.
  const occurrence=Math.min(5,Math.max(0,Math.floor(progress+1e-7))),visited=M.walk.slice(0,occurrence+1),unique=[...new Set(visited)];
  const assemblyTrail=[];const encountered=[];
  for(const n of visited) {if(!encountered.includes(n))encountered.push(n);assemblyTrail.push(average(encountered.map(k=>coords[k])));}
  return {stage,role:r.id,word:r.nodes.map(n=>n[0]).join(''),nodes:r.nodes,branch,seedMode:mode,branchPath,
    transportPhaseDegrees:Math.abs(Math.atan2(transport[1],transport[0]))<1e-12?0:Math.atan2(transport[1],transport[0])*180/Math.PI,
    probePhaseDegrees:phase,weights,anchor,anchors,displayDisplacement:stage?delta(anchor,anchors[stage-1]):anchor.map(()=>0),realVector:re,imaginaryVector:im,
    sourceAnchorExact:proof.windows[stage].anchor,sourceDisplacementExact:stage?proof.transitions[stage-1].anchor_displacement:null,
    modeRecord:proof.windows[stage].modes[branch],closure:proof.windows[stage].explicit_extra_closure,
    sourceOccurrences:proof.windows[stage].walk_occurrence_ids,operation:stage?proof.transitions[stage-1].cyclic_target_convention:'source cyclic frame',
    occurrence,uniqueVertices:unique,assemblyAnchor:assemblyTrail.at(-1),assemblyTrail,occurrenceMean:average(visited.map(n=>coords[n])),
    repeatedVertex:visited.length!==unique.length,walk:M.walk,proofChecks:proof.verified_checks,proofHash:proof.receipt_sha256,
    sourceMetricScope:'Verified regular pentachoron. Other views show coordinate images of the same labeled coefficients, not an isometric identification.',
  };
}

export function mountIdentity({THREE,scene,host,getState,onRoute}) {
  const $=id=>document.getElementById(id),cfg={enabled:true,mode:'positive',phase:0,assembly:true};
  const group=new THREE.Group();group.name='retained-identity-development';scene.add(group);
  const label=document.createElement('span');label.className='identity-label';label.textContent='active-face center';label.title='Mean of the three active-face vertices, excluding the fourth continuation vertex.';host.append(label);
  const assemblyLabel=document.createElement('span');assemblyLabel.className='identity-label assembly-label';assemblyLabel.textContent='assembly center';assemblyLabel.title='Mean of the distinct vertices encountered along the path.';host.append(assemblyLabel);
  let key='',value=null,anchorPosition=null,assemblyPosition=null;
  const viewPoint=p=>new THREE.Vector3(...(getState().geometry==='carrier'?p:M.displayPoint(p,getState().view,getState().angle)));
  function clear() {group.traverse(o=>{o.geometry?.dispose();if(o.material)(Array.isArray(o.material)?o.material:[o.material]).forEach(m=>m.dispose());});group.clear();}
  function line(points,color,opacity=1,dashed=false) {
    const material=dashed?new THREE.LineDashedMaterial({color,transparent:true,opacity,dashSize:.045,gapSize:.035,depthTest:false}):new THREE.LineBasicMaterial({color,transparent:true,opacity,depthTest:false});
    const mesh=new THREE.Line(new THREE.BufferGeometry().setFromPoints(points),material);if(dashed)mesh.computeLineDistances();group.add(mesh);return mesh;
  }
  function marker(p,radius,color) {const mesh=new THREE.Mesh(new THREE.SphereGeometry(radius,18,12),new THREE.MeshBasicMaterial({color,depthTest:false}));mesh.position.copy(p);mesh.renderOrder=21;group.add(mesh);}
  function vector(p,v,color) {const length=v.length();if(length>1e-8){const a=new THREE.ArrowHelper(v.clone().normalize(),p,length,color,.045,.025);a.traverse(o=>{if(o.material){o.material.depthTest=false;o.renderOrder=22;}});group.add(a);}}
  const number=x=>Math.abs(x)<1e-8?'0':Number(x.toFixed(3)).toString();
  const tuple=p=>'('+p.map(number).join(', ')+')';
  const exact=p=>p?'('+p.join(', ')+')':'initial frame';
  function refresh() {
    const state=getState();const nextKey=JSON.stringify([state.view,state.geometry,state.electronTrial,state.angle,Math.floor(state.progress+1e-7),state.route,cfg]);
    if(nextKey===key)return;key=nextKey;value=identityState({...state,mode:cfg.mode,phase:cfg.phase});clear();group.visible=cfg.enabled;
    label.hidden=assemblyLabel.hidden=!cfg.enabled;
    const v=value;anchorPosition=viewPoint(v.anchor);assemblyPosition=viewPoint(v.assemblyAnchor);
    if(cfg.enabled) {
      line(v.anchors.map(viewPoint),0xa4efd0,.55,true);marker(anchorPosition,.038,0xa4efd0);
      if(v.branch!=='common') {
        const center=v.anchor,scale=.18;
        const endpoint=(a,b)=>viewPoint(center.map((x,i)=>x+scale*(a*v.realVector[i]+b*v.imaginaryVector[i])));
        line(Array.from({length:65},(_,i)=>endpoint(Math.cos(i*Math.PI/32),Math.sin(i*Math.PI/32))),0xa4efd0,.7);
        vector(anchorPosition,endpoint(1,0).sub(anchorPosition),0xffd28b);vector(anchorPosition,endpoint(0,1).sub(anchorPosition),0x95bbff);
      }
      if(cfg.assembly) {line(v.assemblyTrail.map(viewPoint),0xd1dbe9,.45,true);marker(assemblyPosition,.025,0xd1dbe9);}
    }
    assemblyLabel.hidden=!cfg.enabled||!cfg.assembly;
    document.querySelectorAll('[data-identity-route]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.identityRoute===state.route)));
    $('identity-window').textContent=M.routes[v.stage].name+' · '+v.word;
    $('identity-branch').textContent=v.branchPath.join(' → ');
    $('identity-phase-readout').textContent=number(v.transportPhaseDegrees)+'° transport + '+number(cfg.phase)+'° probe';
    $('identity-operation').textContent=v.operation;
    $('identity-anchor').textContent=tuple(v.anchor);
    $('identity-displacement').textContent=tuple(v.displayDisplacement);
    $('identity-source-anchor').textContent=exact(v.sourceAnchorExact);
    $('identity-source-delta').textContent=exact(v.sourceDisplacementExact);
    $('identity-assembly').textContent=v.uniqueVertices.length+' distinct vertices · '+(v.occurrence+1)+' retained occurrences';
    $('identity-assembly-anchor').textContent=tuple(v.assemblyAnchor);
    $('identity-occurrence-mean').textContent=tuple(v.occurrenceMean);
    $('identity-revisit').textContent=v.repeatedVertex?'C₁ revisited: same vertex; new occurrence. It is not inserted into the geometric mean twice.':'First-seen vertices assemble by bₙ₊₁ = bₙ + (xₙ₊₁ − bₙ)/(n + 1).';
    $('identity-record').textContent=v.nodes.map(n=>M.names[n]).join(' → ')+' · '+v.branch;
    $('identity-occurrences').textContent=v.sourceOccurrences.join(' · ');
    $('identity-closure').textContent=v.closure.source+' → '+v.closure.target+' (declared geometric closure, not a supplied native command)';
    $('identity-eigenvalue').textContent=v.branch==='common'?'1':v.branch==='positive'?'ω = exp(+2πi/3)':'ω̄ = exp(−2πi/3)';
    $('identity-proof').textContent='';
    $('identity-view-note').textContent=state.geometry==='carrier'&&state.electronTrial?'The active-face center averages M₁, C₁ and C₂ for the electron; it excludes M₂. Mode coefficients belong to the five-vertex geometry. M₂ has no spectral coefficient in this representation.':state.geometry==='carrier'?'The active-face center averages the three unbracketed vertices, not all four carrier vertices. The two tetrahedra preserve their individual geometry, not the complete pentachoron metric.':M.isLatticeView(state.view)?'The active-face center averages the three window vertices. The glyph shows their mode coefficients in lattice coordinates.':state.view==='pentachoron'?'The active-face center averages the three window vertices. C₂ remains the fifth pentachoron vertex even when its projection coincides with a center.':'In this view C₂ is the pentachoron barycenter, distinct from the fifth vertex V₄.';
    $('identity-phase-output').textContent=number(cfg.phase)+'°';
    $('identity-glyph-note').textContent=v.branch==='common'?'Common mode: the retained homogeneous identity line has no centered directional ellipse.':'Ellipse and gold/blue axes: real/imaginary coordinate images. Changing the phase probe leaves the eigenline projector unchanged.';
  }
  function positionLabels(camera) {
    const box=host.getBoundingClientRect(),occupied=[...host.querySelectorAll('.point-label,.carrier-label')].filter(el=>!el.hidden&&el.style.visibility!=='hidden').map(el=>{const r=el.getBoundingClientRect();return {x:r.x-box.x,y:r.y-box.y,w:r.width,h:r.height};});
    const intersects=(a,b)=>a.x<b.x+b.w+3&&b.x<a.x+a.w+3&&a.y<b.y+b.h+3&&b.y<a.y+a.h+3;
    for(const [el,p,preferred] of [[label,anchorPosition,[-10,20]],[assemblyLabel,assemblyPosition,[8,-19]]]) {
      if(el.hidden||!p)continue;const q=p.clone().project(camera),px=(q.x*.5+.5)*host.clientWidth,py=(-q.y*.5+.5)*host.clientHeight,w=el.offsetWidth,h=el.offsetHeight;
      const choices=[preferred,[0,-30],[65,4],[-65,4],[0,36],[65,-28],[-65,-28]];
      const candidates=choices.map(([dx,dy])=>({x:Math.max(7,Math.min(host.clientWidth-w-7,px+dx-w/2)),y:Math.max(52,Math.min(host.clientHeight-h-38,py+dy)),w,h}));
      const position=candidates.find(a=>!occupied.some(b=>intersects(a,b)))||candidates[0];occupied.push(position);
      el.style.left=position.x+w/2+'px';el.style.top=position.y+'px';el.style.visibility=Math.abs(q.z)<1?'visible':'hidden';
    }
  }
  document.querySelectorAll('[data-identity-route]').forEach(button=>button.addEventListener('click',()=>onRoute(button.dataset.identityRoute)));
  for(const [id,name] of [['identity-enabled','enabled'],['identity-assembly-toggle','assembly']])$(id).addEventListener('change',event=>{cfg[name]=event.target.checked;refresh();});
  $('identity-mode').addEventListener('change',event=>{cfg.mode=event.target.value;refresh();});
  $('identity-phase').addEventListener('input',event=>{cfg.phase=Number(event.target.value);refresh();});
  $('identity-phase-reset').addEventListener('click',()=>{cfg.phase=0;$('identity-phase').value=0;refresh();});
  return {refresh,positionLabels,snapshot:()=>({config:{...cfg},...value,visible:group.visible,sceneObjectCount:group.children.length})};
}
