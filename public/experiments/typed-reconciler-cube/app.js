import * as THREE from "three"
import { CSS3DRenderer, CSS3DObject } from "three/addons/renderers/CSS3DRenderer.js"
import { OrbitControls } from "three/addons/controls/OrbitControls.js"

const host=document.querySelector("#scene"),detail=document.querySelector("#detail"),status=document.querySelector("#validation")
const text=await fetch("./coherence-lattice.toml?v=11").then(r=>{if(!r.ok)throw new Error(`TOML fetch ${r.status}`);return r.text()})

function value(raw){const s=raw.trim();if(s.startsWith('"'))return JSON.parse(s);if(s==="true"||s==="false")return s==="true";if(/^[-+]?\d+$/.test(s))return Number(s);return s}
function parseToml(source){const root=Object.create(null),arrays=Object.create(null);let target=root;for(const original of source.split(/\r?\n/)){const line=original.replace(/\s+#.*$/,"").trim();if(!line)continue;let m;if((m=line.match(/^\[\[([^\]]+)\]\]$/))){const key=m[1];arrays[key]??=[];target=Object.create(null);arrays[key].push(target);root[key]=arrays[key]}else if((m=line.match(/^\[([^\]]+)\]$/))){const key=m[1];if(!Object.hasOwn(root,key))root[key]=Object.create(null);target=root[key]}else{const at=line.indexOf("=");if(at<1)throw new Error(`Unsupported TOML line: ${line}`);target[line.slice(0,at).trim()]=value(line.slice(at+1))}}return root}
const model=parseToml(text),rungs=[...model.rung].sort((a,b)=>a.index-b.index),n=model.lattice.object_count
const reconcilerLabels=new Map((model.reconciler??[]).map(item=>[item.id,item]))
const edgeTypes=new Map((model.edge_type??[]).map(item=>[item.id,item]))
const lenses=model.coefficient_lens??[], boundaryWord=(model.boundary_word??[])[0]
const thetaTate=new Map((model.theta_tate_cell??[]).map(item=>[item.id,item]))
const errors=[];if(!["marici.coherence-lattice.v1","marici.coherence-lattice.v2"].includes(model.schema))errors.push("unknown schema");if(rungs.length!==n)errors.push("rung count mismatch");if(new Set(rungs.map(r=>r.id)).size!==n)errors.push("duplicate rung id");if(model.lattice.formation!=="contiguous_interval")errors.push("unsupported formation")
if(reconcilerLabels.size!==n-1)errors.push("first reconciler label count mismatch")
if(edgeTypes.size!==2||!edgeTypes.has("L")||!edgeTypes.has("R"))errors.push("expected L and R edge types")
if(boundaryWord?.route_a!=="L > R"||boundaryWord?.route_b!=="R > L")errors.push("boundary word mismatch")
if(lenses.length!==3)errors.push("coefficient lens count mismatch")
if(thetaTate.size!==n*(n+1)/2)errors.push("theta/Tate overlay cell count mismatch")
if(errors.length)throw new Error(errors.join("\n"))
const cells=[];for(let p=0;p<n;p++)for(let i=0;i<n-p;i++){const id=`C${p}_${i}`;cells.push({id,p,i,span:[i,i+p],status:p<=model.lattice.max_witnessed_column?(p===0?"pinned":"partial"):"required",label:p===0?rungs[i].label:p===1?reconcilerLabels.get(id)?.label:`required coherence over A${i}…A${i+p}`,authority:p===0?"pinned tower vocabulary":p===1?reconcilerLabels.get(id)?.authority:"unconstructed formal slot",sector:thetaTate.get(id)})}
status.textContent=`valid TOML · ${cells.length} cells · ${n},${n-1},${n-2},${n-3},${n-4},${n-5},${n-6}`

const scene=new THREE.Scene(),camera=new THREE.PerspectiveCamera(42,1,1,6000)
camera.position.set(850,0,2700)
const renderer=new CSS3DRenderer();renderer.domElement.className="css3d-root";host.replaceChildren(renderer.domElement)
const controls=new OrbitControls(camera,renderer.domElement);controls.enableDamping=true;controls.target.set(850,0,0);controls.minDistance=900;controls.maxDistance=5200
const objects=new Map(),positions=new Map(),columnGap=320,rowGap=150
const color=["#63b3ff","#f3b35d","#50d890","#b68cff","#e96b78","#d68cff","#ffffff"]
function describe(cell){const left=cell.p?`C${cell.p-1}_${cell.i}`:"none",right=cell.p?`C${cell.p-1}_${cell.i+1}`:"none",shared=cell.p>1?`C${cell.p-2}_${cell.i+1}`:"tower adjacency";const routes=cell.p>1?`<span>route A: ${cell.id} -L→ ${left} -R→ ${shared}</span><span>route B: ${cell.id} -R→ ${right} -L→ ${shared}</span><hr>${lenses.map(l=>`<span class="formula"><b>${l.id}</b>: ${l.formula} = ${l.flat_identity}</span>`).join("")}`:"<span>boundary formula begins in column 2</span>";detail.innerHTML=`<strong>${cell.id} · ${cell.label}</strong><span>theta/Tate overlay: ${cell.sector.label}</span><span>column: ${cell.p} · span: A${cell.span[0]}…A${cell.span[1]}</span><span>status: ${cell.status}</span><span>overlay authority: ${cell.sector.authority}</span><span>L face: ${left}</span><span>R face: ${right}</span><span>shared face: ${shared}</span>${routes}`}
for(const cell of cells){const x=cell.p*columnGap,y=(cell.i+cell.p/2-(n-1)/2)*rowGap,z=cell.p*12;positions.set(cell.id,new THREE.Vector3(x,y,z));const box=document.createElement("button");box.className=`lattice-box ${cell.status} ${cell.p>1?"diamond":""}`;let body=`<b>${cell.id} · ${cell.label}</b><small class="sector-label">${cell.sector.label}</small>`;if(cell.p>1){const left=`C${cell.p-1}_${cell.i}`,right=`C${cell.p-1}_${cell.i+1}`,shared=`C${cell.p-2}_${cell.i+1}`;body+=`<code>${cell.id} → ${left} → ${shared}</code><code>${cell.id} → ${right} → ${shared}</code><span class="equations">${lenses.map(l=>`<em><i>${l.id}</i> ${l.formula} = ${l.flat_identity}</em>`).join("")}</span>`};box.innerHTML=body;box.style.setProperty("--cell-color",color[cell.p]);box.addEventListener("click",()=>{document.querySelectorAll(".lattice-box.selected").forEach(e=>e.classList.remove("selected"));box.classList.add("selected");describe(cell)});const object=new CSS3DObject(box);object.position.copy(positions.get(cell.id));scene.add(object);objects.set(cell.id,object)}
function addLink(from,to,kind){const a=positions.get(from),b=positions.get(to),delta=new THREE.Vector3().subVectors(b,a),length=delta.length(),mid=a.clone().add(b).multiplyScalar(.5);const line=document.createElement("div");line.className=`lattice-link ${kind}`;line.title=edgeTypes.get(kind).label;line.style.width=`${length}px`;const object=new CSS3DObject(line);object.position.copy(mid);object.rotation.z=Math.atan2(delta.y,delta.x);scene.add(object)}
for(const cell of cells.filter(c=>c.p>0)){addLink(`C${cell.p-1}_${cell.i}`,cell.id,"L");addLink(`C${cell.p-1}_${cell.i+1}`,cell.id,"R")}
for(const button of document.querySelectorAll("[data-view]"))button.addEventListener("click",()=>{const mode=button.dataset.view;document.querySelectorAll("[data-view]").forEach(b=>b.classList.toggle("active",b===button));for(const cell of cells)objects.get(cell.id).element.classList.toggle("muted",mode!=="all"&&(mode==="tower"?cell.p!==0:cell.p===0))})
document.querySelector('[data-view="all"]').click();describe(cells.at(-1))
function resize(){const w=Math.max(1,host.clientWidth),h=Math.max(1,host.clientHeight);renderer.setSize(w,h);camera.aspect=w/h;camera.updateProjectionMatrix()}
new ResizeObserver(resize).observe(host);resize();function animate(){requestAnimationFrame(animate);controls.update();renderer.render(scene,camera)}animate()
