// Browser readout/diagram adapter. No scientific supplier is run here.
const $ = id => document.getElementById(id)
const rational = x => { const [a,b=1] = String(x).split('/').map(Number); return a/b }
const real6 = x => rational(x.rational) + Math.sqrt(6)*rational(x.sqrt6)
const real3 = x => rational(x[0]) + Math.sqrt(3)*rational(x[1])
const complex = z => z.map(real3)
const cmul = ([a,b],[c,d]) => [a*c-b*d,a*d+b*c]
const cadd = ([a,b],[c,d]) => [a+c,b+d]
const dot = (row,state) => row.reduce((sum,z,i)=>cadd(sum,cmul(z,state[i])),[0,0])
const apply = (matrix,state) => matrix.map(row=>dot(row,state))
const norm = state => state.reduce((n,[r,i])=>n+r*r+i*i,0)
const fmt = x => Math.abs(x)<1e-14?'0':Number(x).toPrecision(8)
const cf = ([r,i]) => `${fmt(r)} ${i<0?'−':'+'} ${fmt(Math.abs(i))}i`
const esc = x => String(x).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;')
function bars(id,labels,values,unit='') {
 const max=Math.max(...values.map(Math.abs),1e-20), height=240/values.length
 $(id).innerHTML=labels.map((label,i)=>{const y=15+i*height,w=Math.abs(values[i])/max*205;return `<text x="10" y="${y+19}" fill="#dfeaff" font-size="12">${esc(label)}</text><rect x="${values[i]<0?250-w:250}" y="${y}" width="${w}" height="${Math.min(height-6,26)}" fill="${values[i]<0?'#e9a3cf':'#83d5ee'}"/><text x="${values[i]<0?250-w:250}" y="${y+Math.min(height-6,26)+13}" fill="#dfeaff" font-size="11">${esc(fmt(values[i])+unit)}</text>`}).join('')
}
const events = (ids,fn) => ids.forEach(id=>$(id).addEventListener('change',fn))
const audit = {}; window.researchLabAudit=audit
try {
 const response=await fetch('/experiments/research-lab/data.json');if(!response.ok)throw new Error(`Source data HTTP ${response.status}`)
 const data=await response.json()
 function arrow() {
  const geometry=$('hinge').value,branch=$('response-branch').value,c=data.arrow.branches[branch].cases[+$('response-probe').value],configuration=c.configurations[geometry]
  const packet=configuration.all_edge_response.map(real6),curvatures=configuration.all_face_curvature.map(real6),local=real6(c.local_response)
  $('response-disposition').textContent=branch==='source_face_metric'?'Falsifier: the complete symmetric AB packet is shielded.':'Declared unequal-weight control: remote sensitivity is visible.'
  $('response-readout').textContent=`Clamped local AB response: ${fmt(local)}\nCollective AB response: ${fmt(packet[0])}\nHinged − original AB: ${fmt(c.anchored_response_hinged_approx-c.anchored_response_source_approx)}\nComplete local row stays fixed; full resolvent difference rank: ${c.full_response_difference_rank}\nAll face curvatures: ${curvatures.map(fmt).join(', ')}\nAll twelve occurrence readouts: ${configuration.all_twelve_occurrence_readout.map(real6).map(fmt).join(', ')}`
  bars('response-chart',data.arrow.field_coordinate_order,packet)
  const points=Object.fromEntries(Object.entries(data.arrow.geometries[geometry]).map(([k,p])=>{const [x,y,z]=p.map(rational);return[k,[235+78*(x-.35*z),145-65*(y-.25*z)]]}))
  const primitive=data.arrow.primitive_registry
  $('hinge-geometry').innerHTML='<defs><marker id="direction" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0L6 3L0 6" fill="#82d8f0"/></marker></defs>'+primitive.map(({tail,head})=>{const a=points[tail],b=points[head],dx=b[0]-a[0],dy=b[1]-a[1],length=Math.hypot(dx,dy),ox=-3*dy/length,oy=3*dx/length;return `<line x1="${a[0]+ox+dx*.09}" y1="${a[1]+oy+dy*.09}" x2="${b[0]+ox-dx*.09}" y2="${b[1]+oy-dy*.09}" stroke="#82d8f0" stroke-width="1.6" marker-end="url(#direction)"/>`}).join('')+Object.entries(points).map(([k,[x,y]])=>`<circle cx="${x}" cy="${y}" r="6" fill="#ffd08b"/><text x="${x+10}" y="${y-8}" fill="#ffffff">${k}</text>`).join('')+'<text x="12" y="286" fill="#b7c6d8" font-size="12">Projection for display; metric calculations use the 3D source.</text>'
  audit.arrow={geometry,branch,packet,local,curvatures,primitiveCount:primitive.length,points:data.arrow.geometries[geometry],sourceAB:c.anchored_response_source_approx,hingedAB:c.anchored_response_hinged_approx}
 }
 events(['hinge','response-branch','response-probe'],arrow);arrow()
 function link() {
  const record=data.link,states=[record.pair_x,record.pair_y].map(s=>s.map(complex)),decoder=record.two_source_rotation_reading_decoders[+$('link-rotation').value],observation=decoder.observation.map(row=>row.map(complex)),inverse=decoder.inverse.map(row=>row.map(complex))
  const readings=states.map(s=>apply(observation,s)),allowed=$('second-reading').checked,recovered=allowed?readings.map(s=>apply(inverse,s)):null
  $('link-rotation').disabled=!allowed
  $('link-readout').textContent=states.map((state,i)=>`Input ${i?'y':'x'}: (${state.map(cf).join('; ')})\nSquared norm: ${fmt(norm(state))}\nFirst link reading: ${cf(readings[i][0])}${allowed?`\nSecond permitted reading: ${cf(readings[i][1])}\nReconstructed: (${recovered[i].map(cf).join('; ')})`:''}`).join('\n\n')+`\n\nObservation rank: ${allowed?2:1} of 2 complex directions.`
  const labels=['x first Re','y first Re'],values=[readings[0][0][0],readings[1][0][0]]
  if(allowed){labels.push('x second Re','x second Im','y second Re','y second Im');values.push(...readings[0][1],...readings[1][1])}
  bars('link-chart',labels,values);audit.link={states,readings:readings.map(r=>allowed?r:[r[0]]),norms:states.map(norm),rank:allowed?2:1,recovered}
 }
 events(['second-reading','link-rotation'],link);link()
 const task=data.tasks,p=task.proton_comparison
 $('task-table').innerHTML=[['L / G / N transfer supports',p.supports,task.stage_supports],['L / G / N ranks',p.ranks,task.projector_ranks],['Raw rejection / local disagreement / collective',p.diagnostics,task.diagnostic_dimensions],['Minimum reconstruction addresses',p.minimum_addresses,task.minimum_addresses]].map(([name,a,b])=>`<tr><th>${name}</th><td>${Array.isArray(a)?a.join(' / '):a}</td><td>${Array.isArray(b)?b.join(' / '):b}</td></tr>`).join('')
 let selected=new Set()
 function tasks() {
  const focused=document.activeElement?.dataset?.address
  const neutron=$('task-carrier').value==='neutron',size=neutron?12:3,groups=neutron?3:12,counts=Array.from({length:groups},(_,g)=>Array.from(selected).filter(i=>Math.floor(i/size)===g).length),empty=counts.filter(k=>!k).length
  const rank=counts.reduce((n,k)=>n+(k?Math.min(size,k+1):0),0)+(empty>0&&empty<groups?1:0)
  $('addresses').innerHTML=Array.from({length:36},(_,i)=>`<label><input type="checkbox" data-address="${i}" ${selected.has(i)?'checked':''}>${neutron?'S':'T'}${Math.floor(i/size)+1}:${i%size+1}</label>`).join('')
  $('addresses').querySelectorAll('input').forEach(input=>input.addEventListener('change',()=>{const i=+input.dataset.address;input.checked?selected.add(i):selected.delete(i);tasks()}))
  if(focused!==undefined)$('addresses').querySelector(`[data-address="${focused}"]`)?.focus()
  $('task-readout').textContent=`${selected.size} addresses selected · observation rank ${rank}/36 · ${36-rank} hidden complex directions. ${rank===36?'Complete mathematical reconstruction.':'Not a complete decoder.'}`
  audit.tasks={carrier:neutron?'neutron':'proton',counts,addresses:[...selected].sort((a,b)=>a-b),rank,hidden:36-rank}
 }
 $('task-carrier').addEventListener('change',()=>{selected=new Set();tasks()})
 $('addresses-none').addEventListener('click',()=>{selected=new Set();tasks()})
 $('addresses-all').addEventListener('click',()=>{selected=new Set(Array.from({length:36},(_,i)=>i));tasks()})
 $('addresses-minimum').addEventListener('click',()=>{const size=$('task-carrier').value==='neutron'?12:3;selected=new Set(Array.from({length:36},(_,i)=>i).filter(i=>i%size<size-1));tasks()});tasks()
 let resource=2,depth=0,history=[]
 function reference() {
  const active=depth===1||depth===2,mode=['empty input','stored','delayed','depleted bank'][depth],operator=active?resource:0,valid=active&&resource===2
  $('reference-advance').disabled=depth===3
  $('reference-readout').textContent=`Declared preparation: ${resource} Clifford units, initially empty bank\nExchange depth: ${depth}/3 · mode: ${mode}\nCarrier scalar: ${depth===0||depth===3?resource:0}\nActive bank operator: ${operator}I\nActive inverse: ${operator?fmt(1/operator)+'I':'rejected: singular/empty reference'}\nPinned 2I boundary binding: ${valid?'eligible under supplied identifications':'REJECTED (wrong resource or inactive bank)'}\nSource coefficient budget: ${resource**2}; represented Frobenius norm²: ${2*resource**2}\nRetained parent history: ${history.length?history.join(' → '):'empty'}`
  $('reference-chart').innerHTML=Array.from({length:4},(_,i)=>`<rect x="${12+i*118}" y="70" width="102" height="70" rx="8" fill="${i===depth?'#40627f':'#23364c'}"/><text x="${20+i*118}" y="96" fill="#fff" font-size="12">${['Prepare','Stored','Delayed','Returned'][i]}</text><text x="${20+i*118}" y="118" fill="#ffd08b" font-size="12">bank ${i===1||i===2?resource:0}I</text>`).join('')+'<text x="12" y="190" fill="#b7c6d8" font-size="12">Depth labels are source steps, not physical elapsed time.</text>'
  audit.reference={resource,depth,operator,eligible:valid,history:[...history],coefficientBudget:resource**2,representedNorm:2*resource**2}
 }
 $('reference-prepare').addEventListener('click',()=>{resource=+$('reference-units').value;depth=0;history=[];$('recovery-readout').textContent='New declared input; no physical reset cost is inferred.';reference()})
 $('reference-advance').addEventListener('click',()=>{if(depth>=3)return;history.push(`parent ${depth}`);depth++;$('recovery-readout').textContent='';reference()})
 $('reference-recover').addEventListener('click',()=>{$('recovery-readout').textContent=`Inverse recovery along ${history.length} retained parents returns ${resource} units and the empty initial bank. Current depth and active bank are unchanged; this is a read-only recovery statement.`});reference()
 // Exact endpoint enumeration from check_rung_transport_diagram.py, not graph reachability.
 const E=[];for(let a=0;a<4;a++)for(let b=0;b<4;b++)if(a!==b&&!(a===0&&b===1))E.push([a,b])
 const leaves=[];for(const [tag,size] of [['a',11],['s',4]])for(let i=0;i<size;i++)for(let j=0;j<size;j++)leaves.push({id:leaves.length,source:tag==='a'?[tag,E[i][0],E[j][0]]:[tag,i,j],target:tag==='a'?[tag,E[i][1],E[j][1]]:[tag,i,j]})
 const fibres=new Map();for(const leaf of leaves){const key=leaf.target.join(':');if(!fibres.has(key))fibres.set(key,[]);fibres.get(key).push(leaf.id)}
 const pairCount=[...fibres.values()].reduce((n,v)=>n+v.length**2,0)
 if(leaves.length!==data.t9.end_to_end.original_rows||fibres.size!==data.t9.end_to_end.final_families||pairCount!==data.t9.end_to_end.exact_admitted_leaf_pairs)throw new Error('Endpoint fixture differs from pinned T9')
 for(const id of ['context-a','context-b'])$(id).innerHTML=leaves.map(l=>`<option value="${l.id}">leaf ${l.id} · target ${l.target.join(':')}</option>`).join('')
 $('context-b').value='1'
 $('context-fibres').innerHTML=[...fibres].map(([key,ids])=>`<tr><th>${key}</th><td>${ids.join(', ')}</td></tr>`).join('')
 function contexts(){const a=leaves[+$('context-a').value],b=leaves[+$('context-b').value],admitted=a.target.join(':')===b.target.join(':');$('context-readout').textContent=`leaf ${a.id} (${a.target.join(':')}) and leaf ${b.id} (${b.target.join(':')}): ${admitted?'ADMITTED original common-target composition':'REJECTED: no matching target and no declared connector'}. ${leaves.length} leaves remain retained in ${fibres.size} inherited target fibres; ${pairCount} original ordered pairs.`;audit.context={a,b,admitted,pairCount,leafCount:leaves.length,familyCount:fibres.size}}
 events(['context-a','context-b'],contexts);contexts()
 function branches(){const {masses,J4,contrast}=data.branches.original_outer_interface,j=J4.map(row=>row.map(rational)),d=contrast.map(row=>row.map(rational)),M=masses[0]+masses[1],retained=$('retain-contrast').checked,arrow=j.map((row,i)=>row.map((x,k)=>x+masses[1]/M*d[i][k])),state=j.map((row,i)=>row.map((x,k)=>x-masses[0]/M*d[i][k]));$('branch-readout').textContent=`Original branch masses: ${masses.join(', ')}\nUnchanged J4: ${j.map(row=>row.map(fmt).join(', ')).join(' ; ')}\n${retained?`Retained contrast: ${d.map(row=>row.map(fmt).join(', ')).join(' ; ')}\nArrow branch residual: ${arrow.map(row=>row.map(fmt).join(', ')).join(' ; ')}\nState branch residual: ${state.map(row=>row.map(fmt).join(', ')).join(' ; ')}\nRank 8: full two-matrix branch readout.`:'Contrast discarded: rank 4. Branch means cannot be reconstructed from J4 alone.'}\nResiduals are relative to supplied reference 2I, not physical energies. All three tested endpoint policies support this extended observation; it does not select the pinned wiring.`;audit.branches={J4:j,masses,contrast:retained?d:null,arrow:retained?arrow:null,state:retained?state:null,rank:retained?8:4}}
 events(['retain-contrast'],branches);branches()
 $('clock-reading').innerHTML=data.clock.cases.map((c,i)=>`<option value="${i}">${fmt(c.state_read_clock)}</option>`).join('')
 function clock(){const enabled=$('clock-matching').checked,rate=+$('clock-rate').value,c=data.clock.cases[+$('clock-reading').value],populations=enabled?c.all_forty_populations:data.clock.actual_initial_density,reading=enabled?c.state_read_clock:0,occupation=enabled?c.connected_record_occupation:0
  $('clock-reading').disabled=!enabled
  $('clock-readout').textContent=enabled?`χ=${fmt(reading)} · connected occupation=${fmt(occupation)}\nInitial clock slope: ${fmt(rate*data.clock.initial_phase_slope_model_units)} (model generator units)\nAt this reading, denominator: ${fmt(rate*c.clock_direction_denominator_model_units)}\nH and 3H: same relational state; audited state discrepancy ${fmt(c.residuals.rate_independent_state)}\nTrace from all forty populations: ${fmt(populations.reduce((a,b)=>a+b,0))}`:'Matching disabled: free input is stationary, initial slope is zero. χ=0; local clock chart REJECTED (zero derivative). No relational continuation is fabricated.'
  bars('clock-chart',data.clock.cases.map(c=>'χ '+fmt(c.state_read_clock)),data.clock.cases.map(c=>enabled?c.connected_record_occupation:0))
  $('clock-populations').innerHTML=populations.map((p,i)=>`<span>${i<20?'O':'C'}${i%20}: ${fmt(p)}</span>`).join('')
  audit.clock={enabled,rate,reading,occupation,populations:[...populations],chartValid:enabled}
 }
 events(['clock-matching','clock-reading','clock-rate'],clock);clock()
 function spatial(){const metric=$('spatial-metric').value,scale=metric==='product_probability'?100:1000,rows=data.spatial.rows,values=rows.map(row=>row[metric]*scale),baseline=rows[0][metric],delta=(rows[3][metric]/baseline-1)*100
  bars('spatial-chart',rows.map(r=>r.case),values)
  $('spatial-readout').textContent=`Combined versus supplied baseline: ${delta.toFixed(3)}% relative change for this observable. ${rows.every(r=>r.transport_peak>0&&r.rate_per_residence>0)?'Both signed transport readouts remain positive in all four fixtures.':''}`
  $('spatial-table').innerHTML=rows.map((r,i)=>`<tr><th>${r.case}${i===0?' (supplied)':''}</th><td>${r.nlam} / ${r.nD}</td><td>${r.nm}</td><td>${fmt(r.first_omitted_full)}</td><td>${fmt(r[metric]*scale)}</td></tr>`).join('')
  $('spatial-audits').innerHTML=data.spatial.checks.map(c=>`<tr><th>${c.case}</th><td>${c.full_S_checks}</td><td>${c.prepared_column_checks}</td><td>${fmt(c.max_GMRES_equation_residual)}</td><td>${fmt(c.max_raw_audit_residual)}</td></tr>`).join('')
  audit.spatial={metric,values,relativeChange:delta,fullSTests:data.spatial.checks.map(c=>c.full_S_checks),preparedTests:data.spatial.checks.map(c=>c.prepared_column_checks),continuumCertified:false}
 }
 events(['spatial-metric'],spatial);spatial()
 audit.ready=true;$('load-status').textContent='Pinned source data loaded. Explore the six comparisons below.'
} catch(error){$('load-status').textContent='Research snapshot could not load: '+error.message;$('load-status').classList.add('error');throw error}
