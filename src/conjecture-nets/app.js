const payload = JSON.parse(document.getElementById('net-data').textContent);
const nets = payload.nets.map(entry => ({ ...normalizeNet(entry.contract, entry.source, entry.title), sha256: entry.sha256 }));
const $ = id => document.getElementById(id);
const local = location.protocol === 'file:';
let current = nets[0], selected = '', zoom = 1, width = 1000, height = 600;
let activeTab = 'dependencies', portView, portNet = null, returnFocus = null;
const el = (tag, text, cls) => { const x = document.createElement(tag); if (text !== undefined) x.textContent = text; if (cls) x.className = cls; return x; };
const svgEl = (tag, attrs = {}) => { const x = document.createElementNS('http://www.w3.org/2000/svg', tag); for (const [k,v] of Object.entries(attrs)) x.setAttribute(k, v); return x; };
function category(n) {
  if (/deferred|blocked/.test(n.status)) return 'blocked';
  if (/evidence|candidate/.test(n.kind) || /source.*located|candidate_recorded/.test(n.status)) return 'evidence';
  if (n.status === 'open') return 'open';
  return 'resolved';
}
function link(path) {
  const href = sourceURL(path, local);
  if (!href) return el('span', typeof path === 'string' ? path : JSON.stringify(path));
  const a = el('a', path); a.href = href; a.target = '_blank'; a.rel = 'noopener noreferrer'; return a;
}
function field(parent, heading, value) {
  if (value === undefined || value === null || value === '') return;
  parent.append(el('h3', heading));
  parent.append(el(typeof value === 'string' ? 'p' : 'pre', typeof value === 'string' ? value : JSON.stringify(value, null, 2)));
}
function hash() {
  const p = new URLSearchParams({net: current.id, tab: activeTab});
  if (selected) p.set('node', selected);
  // file: can reject history API changes; assigning a fragment works offline too.
  const fragment = '#' + p;
  if (location.hash !== fragment) location.hash = fragment;
}
function nodeButton(id) {
  const n = current.nodes.find(n => n.id === id);
  const b = el('button', n?.title || id, 'link-button'); b.onclick = () => choose(id, true); return b;
}
function openDetails(focus = false) {
  if (!$('drawer').contains(document.activeElement)) returnFocus = document.activeElement;
  $('drawer').inert = false; $('drawer').setAttribute('aria-hidden','false'); $('drawer').classList.add('open');
  if (focus) $('close-details').focus({preventScroll:true});
}
function closeDetails(restoreFocus = true) {
  $('drawer').classList.remove('open'); $('drawer').setAttribute('aria-hidden','true'); $('drawer').inert = true;
  selected = ''; portView?.clear(); hash(); renderList();
  $('graph').querySelectorAll('.selected,.related').forEach(n=>n.classList.remove('selected','related'));
  if (restoreFocus && returnFocus?.isConnected) returnFocus.focus({preventScroll:true});
}
function choose(id, focus = false) {
  if (!current.nodes.some(n => n.id === id)) return;
  selected = id; hash(); renderList(); renderDetails(); portView?.selectNode(id);
  for (const group of $('graph').querySelectorAll('.graph-node')) group.classList.toggle('selected', group.dataset.id === id);
  for (const edge of $('graph').querySelectorAll('.edge')) edge.classList.toggle('related', edge.dataset.from === id || edge.dataset.to === id);
  openDetails(focus);
}
function showPort(node, port) {
  selected=node; hash(); renderList(); renderDetails();
  $('details').prepend(el('h2', `${port} · ${PORT_LABELS[port]}`));
  $('details').append(el('p','Highlighted routes are directed reachability from this one port, not proof admission. No transition between a node’s other outcome ports is assumed.'));
  openDetails();
}
function showRule(rule) {
  selected=''; hash(); renderList(); const out=$('details'); out.replaceChildren();
  out.append(el('h2',rule.id));
  if(rule.kind==='dependency'){
    field(out,'Edge type','Research dependency (dashed), not an outcome implication');
    field(out,'Prerequisite',rule.inputs[0].node);field(out,'Dependent',rule.output.node);
    out.append(el('p','Highlighting follows downstream research dependencies. This edge does not connect outcome ports or establish a proof.'));
    openDetails();return;
  }
  field(out,'Weight',`${rule.weight} (${rule.weightDeclared?'declared source weight':'default layout weight'}; not a probability)`);
  field(out,rule.inputs.length>1?'ALL premises required':'Premise',rule.inputs.map(p=>`${p.node} [${p.port}]`).join('\n'));
  field(out,'Conclusion',`${rule.output.node} [${rule.output.port}]`);
  field(out,'Relation',rule.raw.relation);field(out,'Scope',rule.raw.scope_id);
  field(out,'Witness condition',rule.raw.witness_identity_check);
  out.append(el('p','Reachability preview assumes this rule’s premises together. Other source conditions remain requirements; clicking assigns no outcome.'));
  field(out,'Complete source implication',rule.raw);openDetails();
}
function setTab(tab, updateHash = true) {
  activeTab=tab==='ports'?'ports':'dependencies';
  for(const id of ['dependencies','ports']) {
    const button=$('tab-'+id);button.setAttribute('aria-selected',String(activeTab===id));button.tabIndex=activeTab===id?0:-1;
  }
  $('dependency-panel').hidden=activeTab!=='dependencies';$('ports-panel').hidden=activeTab!=='ports';
  if(activeTab==='ports') {
    if(portNet!==current){portView.draw(current);portNet=current;if(selected)portView.selectNode(selected);}else portView.resume();
  } else {portView?.stop();fit();}
  if(updateHash)hash();
}
function renderDetails() {
  const n = current.nodes.find(n => n.id === selected), out = $('details'); out.replaceChildren();
  out.append(el('h2', n.title), el('div', n.id, 'field'));
  out.append(el('span', n.status, 'badge'), el('span', n.kind, 'badge'));
  out.append(el('p', 'Formal outcome: ' + (n.outcome === null ? 'none recorded' : JSON.stringify(n.outcome))));
  if (current.frontier.includes(n.id)) out.append(el('strong', 'Declared frontier'));
  field(out, 'Statement', n.statement);
  for (const [key,label] of [['verdict','Scoped verdict'],['scope','Scope'],['next_action','Next action'],['acceptance','Acceptance'],['blocker','Blocker'],['reopening','Reopening'],['prerequisite_use','Prerequisite use']]) field(out, label, n.raw[key]);
  out.append(el('h3', 'Prerequisites'));
  if (!n.depends_on.length) out.append(el('p', 'No local prerequisites.', 'empty'));
  n.depends_on.forEach(id => { const p = el('div'); p.append(nodeButton(id)); out.append(p); });
  const children = current.nodes.filter(x => x.depends_on.includes(n.id));
  out.append(el('h3', 'Dependents'));
  if (!children.length) out.append(el('p', 'No local dependents.', 'empty'));
  children.forEach(x => { const p = el('div'); p.append(nodeButton(x.id)); out.append(p); });
  if (Array.isArray(n.raw.evidence)) { out.append(el('h3', 'Evidence / source references')); const ul = el('ul'); n.raw.evidence.forEach(p => { const li = el('li'); li.append(link(p)); ul.append(li); }); out.append(ul); }
  if (n.raw.candidate) { out.append(el('h3', 'Candidate record'), link(n.raw.candidate)); }
  const external = n.raw.external_dependency;
  if (external) {
    out.append(el('h3', 'External prerequisite'));
    field(out, 'Relation', external.relation);
    const target = nets.find(net => net.source === external.contract);
    if (target && target.nodes.some(node => node.id === external.node)) {
      const b = el('button', `Open ${target.title}: ${external.node}`, 'link-button');
      b.onclick = () => switchNet(target.id, external.node); out.append(b);
    } else out.append(el('p', 'Not included in this snapshot; open the source contract.'));
    out.append(el('div')); out.append(link(external.contract));
  }
  const raw = el('details'); raw.append(el('summary', 'Complete source node'), el('pre', JSON.stringify(n.raw, null, 2))); out.append(raw);
}
function renderList() {
  const q = $('search').value.toLowerCase().trim(), f = $('filter').value;
  const rows = current.nodes.filter(n => (!q || JSON.stringify(n.raw).toLowerCase().includes(q) || n.title.toLowerCase().includes(q)) && (f === 'all' || (f === 'frontier' ? current.frontier.includes(n.id) : category(n) === f)));
  const list = $('node-list'); list.replaceChildren();
  $('results').hidden = !q && f === 'all';
  if (!rows.length) list.append(el('p', 'No matching nodes. Clear search or change the filter.', 'empty'));
  rows.forEach(n => { const b = el('button', n.title, 'node-item'); b.dataset.id = n.id; b.setAttribute('aria-pressed', String(selected === n.id)); b.append(el('small', n.status + (current.frontier.includes(n.id) ? ' · frontier' : ''))); b.onclick = () => choose(n.id, true); list.append(b); });
  $('summary').textContent = `${current.nodes.length} nodes · ${current.frontier.length} frontier${q || f !== 'all' ? ` · ${rows.length} matches` : ''}${current.source ? '' : ' · local import'}`;
}
function applyZoom() { $('graph').style.width = width * zoom + 'px'; $('graph').style.height = height * zoom + 'px'; $('zoom-label').textContent = Math.round(zoom * 100) + '%'; }
function fit() { zoom = Math.min(1, Math.max(.75, ($('graph-scroll').clientWidth - 24) / width)); applyZoom(); }
function wrapLabel(text, font, maxWidth = 210) {
  const ctx = document.createElement('canvas').getContext('2d'); ctx.font = font;
  const lines = []; let line = '';
  for (const word of text.split(/\s+/)) {
    const joined = line ? line + ' ' + word : word;
    if (ctx.measureText(joined).width <= maxWidth) { line = joined; continue; }
    if (line) lines.push(line);
    line = '';
    for (const char of word) {
      if (line && ctx.measureText(line + char).width > maxWidth) { lines.push(line); line = ''; }
      line += char;
    }
  }
  if (line) lines.push(line);
  return lines;
}
function drawGraph() {
  const svg = $('graph'); svg.replaceChildren();
  const defs = svgEl('defs'), marker = svgEl('marker', {id:'arrow', viewBox:'0 0 10 10', refX:9, refY:5, markerWidth:7, markerHeight:7, orient:'auto-start-reverse'});
  marker.append(svgEl('path', {d:'M 0 0 L 10 5 L 0 10 z', fill:'currentColor'})); defs.append(marker); svg.append(defs);
  const levels = new Map(), coords = new Map();
  current.nodes.forEach(n => { if (!levels.has(n.level)) levels.set(n.level, []); levels.get(n.level).push(n); });
  width = Math.max(300, Math.max(...[...levels.values()].map(a => a.length)) * 275 + 20);
  let y = 20;
  for (const [,nodes] of [...levels].sort((a,b) => a[0]-b[0])) {
    let rowHeight = 0;
    nodes.forEach((n,i) => {
      const lines = wrapLabel(n.title, '13px system-ui');
      const status = wrapLabel((current.frontier.includes(n.id) ? '◆ ' : '') + n.status.replaceAll('_',' '), '11px system-ui');
      const h = 28 + lines.length*17 + status.length*15;
      coords.set(n.id, {x:(width-nodes.length*275)/2 + i*275, y, h, lines, status});
      rowHeight = Math.max(rowHeight,h);
    });
    y += rowHeight + 50;
  }
  height = y;
  svg.setAttribute('viewBox', `0 0 ${width} ${height}`);
  current.nodes.forEach(n => n.depends_on.forEach(dep => {
    const a = coords.get(dep), b = coords.get(n.id), mid = (a.y+a.h+b.y)/2;
    const p = svgEl('path', {d:`M${a.x+115},${a.y+a.h} C${a.x+115},${mid} ${b.x+115},${mid} ${b.x+115},${b.y}`, class:'edge', 'marker-end':'url(#arrow)'});
    p.dataset.from = dep; p.dataset.to = n.id; svg.append(p);
  }));
  current.nodes.forEach(n => {
    const {x,y,h,lines,status} = coords.get(n.id), g = svgEl('g', {transform:`translate(${x},${y})`, class:'graph-node', tabindex:'0', role:'button', 'aria-label':`${n.title}; ${n.status}`});
    g.dataset.id = n.id; g.dataset.category = category(n);
    const title = svgEl('title'); title.textContent = `${n.id}\n${n.statement}`; g.append(title, svgEl('rect',{width:230,height:h,rx:4}));
    lines.forEach((s,i) => { const t = svgEl('text',{x:10,y:20+i*17,class:'label'}); t.textContent = s; g.append(t); });
    status.forEach((s,i) => { const t = svgEl('text',{x:10,y:28+lines.length*17+i*15,class:'status'}); t.textContent = s; g.append(t); });
    g.onclick = () => choose(n.id, true); g.onkeydown = e => { if (e.key==='Enter' || e.key===' ') { e.preventDefault(); choose(n.id, true); } }; svg.append(g);
  });
  fit();
}
function switchNet(id, node) {
  current = nets.find(n => n.id === id) || nets[0]; selected = current.nodes.some(n => n.id===node) ? node : '';
  portView?.stop(); portNet=null;
  $('drawer').classList.remove('open'); $('drawer').setAttribute('aria-hidden','true'); $('drawer').inert=true;
  $('net-select').value = current.id; $('search').value = ''; $('filter').value = 'all'; $('error').textContent = '';
  const info = $('net-info'); info.replaceChildren();
  if (current.source) { info.append(link(current.source)); field(info, 'Contract SHA-256 at generation', current.sha256); }
  field(info, 'Semantics / registration', current.raw.semantics || current.raw.registration || current.raw.coherence_obligation);
  field(info, 'Regime', current.raw.regime); field(info, 'Objective', current.raw.objective); field(info, 'Declared boundaries', current.raw.boundary);
  field(info, 'Outcome ports', current.raw.outcome_ports); field(info, 'Logical boundaries', current.raw.logic_boundary);
  drawGraph(); setTab(activeTab,false); renderList();
  if(selected)choose(selected);else hash();
}
function options() { $('net-select').replaceChildren(); nets.forEach(n => { const o = el('option', n.title); o.value=n.id; $('net-select').append(o); }); }
$('net-select').onchange = e => switchNet(e.target.value);
$('search').oninput = renderList; $('filter').onchange = renderList;
$('zoom-in').onclick = () => { zoom=Math.min(2,zoom*1.25); applyZoom(); };
$('zoom-out').onclick = () => { zoom=Math.max(.1,zoom/1.25); applyZoom(); };
$('fit').onclick = fit;
$('download').onclick = () => { const url = URL.createObjectURL(new Blob([JSON.stringify(current.raw,null,2)+'\n'],{type:'application/json'})); const a=el('a'); a.href=url; a.download=current.id.replace(/[^a-z0-9.-]/gi,'_')+'.json'; a.click(); setTimeout(()=>URL.revokeObjectURL(url),1000); };
$('import-file').onchange = async e => {
  const file=e.target.files[0]; if (!file) return;
  try {
    if (file.size>2_000_000) throw Error('Local import limit is 2 MB.');
    const net=normalizeNet(JSON.parse(await file.text()),'',file.name);
    normalizeImplications(net);
    if (nets.some(n=>n.id===net.id)) throw Error('This net ID is already loaded. Use a distinct version ID.');
    nets.push(net); options(); switchNet(net.id);
  } catch(error) { $('error').textContent='Cannot import net: '+error.message; }
  e.target.value='';
};
function restore() {
  const p=new URLSearchParams(location.hash.slice(1)); const net=nets.find(n=>n.id===p.get('net'));
  if (!net) return;
  const tab=p.get('tab')==='ports'?'ports':'dependencies';
  if (net.id!==current.id || (p.get('node') || '')!==selected) {activeTab=tab;switchNet(net.id,p.get('node'));}
  else if(activeTab!==tab)setTab(tab,false);
}
window.addEventListener('hashchange',restore);
if (local) { $('site-home').href='https://marici.andrei-kokoev.workers.dev/'; $('gallery').href='https://marici.andrei-kokoev.workers.dev/experiments/'; }
portView=createPortView({onNode:id=>choose(id),onPort:showPort,onRule:showRule,onClear:()=>closeDetails(false)});
$('close-details').onclick=()=>closeDetails();
document.addEventListener('keydown',event=>{if(event.key==='Escape' && $('drawer').classList.contains('open'))closeDetails();});
for(const tab of ['dependencies','ports']) {
  $('tab-'+tab).onclick=()=>setTab(tab);
  $('tab-'+tab).onkeydown=event=>{if(['ArrowLeft','ArrowRight','Home','End'].includes(event.key)){event.preventDefault();const next=event.key==='Home'?'dependencies':event.key==='End'?'ports':activeTab==='ports'?'dependencies':'ports';setTab(next);$('tab-'+next).focus();}};
}
options();
const initial=new URLSearchParams(location.hash.slice(1));activeTab=initial.get('tab')==='ports'?'ports':'dependencies';switchNet(initial.get('net') || nets[0].id,initial.get('node'));
