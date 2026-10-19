/* D3 force layout; reachability is computed over port rules, not force links. */
function createPortView({onNode,onPort,onRule,onClear}) {
  const svg=d3.select('#port-graph');
  let simulation=null,net=null,rules=[],records=[],links=[],selection=null,paused=false;
  let nodeGroups,portGroups,edgeGroups,gateGroups,layer;
  const gravityControl=document.getElementById('port-gravity');
  const linkStrength=d=>Math.min(.8,.12*Math.sqrt(d.rule.weight));
  // Keep node bodies apart; heavier links shorten the gap, not the labels.
  const linkDistance=d=>(Math.hypot(d.source.w,d.source.h)+Math.hypot(d.target.w,d.target.h))/2+120/Math.sqrt(d.rule.weight);
  const zoomer=d3.zoom().scaleExtent([.08,4]).on('zoom',event=>layer?.attr('transform',event.transform));
  svg.call(zoomer).on('dblclick.zoom',null);
  const activate=(selection,fn)=>selection.on('click',(event,d)=>{event.stopPropagation();fn(d);}).on('keydown',(event,d)=>{if(event.key==='Enter'||event.key===' '){event.preventDefault();event.stopPropagation();fn(d);}});
  function dims(){return {w:document.getElementById('port-canvas').clientWidth || 1000,h:document.getElementById('port-canvas').clientHeight || 700};}
  function fit(){
    if(!records.length)return;
    const {w,h}=dims();
    const minX=Math.min(...records.map(n=>n.x-n.w/2-28)),maxX=Math.max(...records.map(n=>n.x+n.w/2+28));
    const minY=Math.min(...records.map(n=>n.y-n.h/2-28)),maxY=Math.max(...records.map(n=>n.y+n.h/2+28));
    const k=Math.min(1.3,(w-40)/(maxX-minX),(h-40)/(maxY-minY));
    svg.call(zoomer.transform,d3.zoomIdentity.translate(w/2-k*(minX+maxX)/2,h/2-k*(minY+maxY)/2).scale(k));
  }
  function offset(n,port){
    if(!port)return {x:n.x,y:n.y};
    const i=PORTS.indexOf(port);
    return {x:n.x+(i%2?1:-1)*(n.w/2),y:n.y+(i<2?-1:1)*(n.h/2-17)};
  }
  function boundary(n,toward){
    const dx=toward.x-n.x,dy=toward.y-n.y;
    const scale=n.type==='gate'?22/(Math.abs(dx)+Math.abs(dy)||1):Math.min((n.w/2+3)/(Math.abs(dx)||.001),(n.h/2+3)/(Math.abs(dy)||.001));
    return {x:n.x+dx*scale,y:n.y+dy*scale};
  }
  function tick(){
    nodeGroups?.attr('transform',d=>`translate(${d.x},${d.y})`);
    gateGroups?.attr('transform',d=>`translate(${d.x},${d.y})`);
    edgeGroups?.each(function(d){
      const a=d.fromPort?offset(d.source,d.fromPort):boundary(d.source,d.target);
      const b=d.toPort?offset(d.target,d.toPort):boundary(d.target,d.source);
      const dx=b.x-a.x,dy=b.y-a.y,len=Math.hypot(dx,dy)||1,pad=d.toPort?17:2;
      const end={x:b.x-pad*dx/len,y:b.y-pad*dy/len};
      const bend=d.rule.kind==='dependency'?0:d.source===d.target?100:20*(d.index%3-1);
      const control={x:(a.x+end.x)/2-dy/len*bend,y:(a.y+end.y)/2+dx/len*bend};
      const path=d.source===d.target?`M${a.x},${a.y} C${a.x+100},${a.y-100} ${b.x+100},${b.y+100} ${end.x},${end.y}`:`M${a.x},${a.y} Q${control.x},${control.y} ${end.x},${end.y}`;
      d3.select(this).selectAll('path').attr('d',path);
      d3.select(this).select('.edge-weight').attr('x',d.source===d.target?a.x+75:(a.x+2*control.x+end.x)/4).attr('y',d.source===d.target?(a.y+b.y)/2:(a.y+2*control.y+end.y)/4-7);
    });
  }
  function highlight(){
    if(!nodeGroups)return;
    let reach=null;
    if(selection?.kind==='port')reach=reachablePorts(rules,[selection.key]);
    if(selection?.kind==='rule')reach=reachablePorts(rules,selection.rule.inputs.map(p=>p.key));
    let dependencyNodes=null;
    if(selection?.kind==='dependency'){
      dependencyNodes=new Set([selection.rule.output.node]);
      let changed=true;
      while(changed){changed=false;for(const n of net.nodes)if(!dependencyNodes.has(n.id)&&n.depends_on.some(id=>dependencyNodes.has(id))){dependencyNodes.add(n.id);changed=true;}}
    }
    const dependencyVisible=d=>d.rule.kind==='dependency'&&(d.rule===selection?.rule||dependencyNodes?.has(d.rule.inputs[0].node));
    nodeGroups.classed('dim',n=>dependencyNodes?!dependencyNodes.has(n.node.id)&&n.node.id!==selection.rule.inputs[0].node:reach && !PORTS.some(p=>reach.ports.has(portKey(n.node.id,p))))
      .classed('selected',n=>selection?.kind==='node' && selection.id===n.node.id);
    portGroups.classed('dim',d=>dependencyNodes?true:reach && !reach.ports.has(d.key))
      .classed('selected',d=>selection?.kind==='port' && d.key===selection.key);
    edgeGroups.classed('dim',d=>dependencyNodes?!dependencyVisible(d):reach && (d.rule.kind==='dependency'||!reach.rules.has(d.rule.id)))
      .classed('selected',d=>['rule','dependency'].includes(selection?.kind) && selection.rule===d.rule);
    gateGroups.classed('dim',d=>dependencyNodes?true:reach && !reach.rules.has(d.rule.id));
    if(dependencyNodes)document.getElementById('port-notice').textContent='Dependency path preview: selected prerequisite → dependent and downstream dependents. No outcome ports are implied.';
    else if(reach)document.getElementById('port-notice').textContent=`${reach.ports.size} reachable ports; ${reach.rules.size} enabled implication rules. ${selection.kind==='rule'?'Selected rule premises are assumed together for this preview. ':''}No outcome is assigned by clicking. Other ports of a reached node remain independent.`;
    else notice();
  }
  function notice(){
    if(!net)return;
    const {omitted}=normalizeImplications(net);
    const dependencies=links.filter(d=>d.rule.kind==='dependency').length;
    document.getElementById('port-notice').textContent=rules.length?`${rules.length} declared implications. ${omitted.length} non-outcome relations omitted. AND gates require every premise; source witness conditions still apply.`:`${dependencies} dependency arrows (dashed). No explicit outcome implications in this net; dependencies do not connect outcome ports.`;
  }
  function selectPort(d){selection={kind:'port',key:d.key};highlight();onPort(d.node,d.port);}
  function selectRule(rule){selection={kind:rule.kind==='dependency'?'dependency':'rule',rule};highlight();onRule(rule);}
  function clear(){selection=null;highlight();}
  function selectNode(id){selection=id?{kind:'node',id}:null;highlight();}
  function draw(next){
    simulation?.stop();net=next;rules=normalizeImplications(net).rules;selection=null;paused=false;
    document.getElementById('port-pause').textContent='Pause layout';
    svg.selectAll('*').remove();
    svg.append('defs').append('marker').attr('id','port-arrow').attr('viewBox','0 0 10 10').attr('refX',9).attr('refY',5).attr('markerWidth',6).attr('markerHeight',6).attr('orient','auto').append('path').attr('d','M0,0 L10,5 L0,10 Z').attr('fill','var(--accent)');
    layer=svg.append('g');
    const columns=Math.max(2,Math.ceil(Math.sqrt(net.nodes.length)));
    records=net.nodes.map((n,i)=>{
      const lines=wrapLabel(n.title,'12px system-ui',185);
      return {id:'node:'+n.id,node:n,type:'node',w:240,h:Math.max(110,lines.length*16+50),lines,x:(i%columns)*330,y:Math.floor(i/columns)*240};
    });
    links=[];
    for(const n of net.nodes)for(const parent of n.depends_on){
      const rule={id:`${parent} → ${n.id}`,kind:'dependency',weight:1,weightDeclared:false,inputs:[{node:parent}],output:{node:n.id},raw:{relation:'Research prerequisite, not a port implication',prerequisite:parent,dependent:n.id}};
      links.push({source:'node:'+parent,target:'node:'+n.id,fromPort:null,toPort:null,rule,id:'dependency:'+JSON.stringify([parent,n.id])});
    }
    rules.forEach((r,i)=>{
      if(r.inputs.length===1){links.push({source:'node:'+r.inputs[0].node,target:'node:'+r.output.node,fromPort:r.inputs[0].port,toPort:r.output.port,rule:r,id:r.id+':out'});}
      else {
        const gate={id:'gate:'+r.id,rule:r,type:'gate',w:44,h:44,x:(i%columns)*330+160,y:Math.floor(i/columns)*240+100};records.push(gate);
        r.inputs.forEach((p,j)=>links.push({source:'node:'+p.node,target:gate.id,fromPort:p.port,toPort:null,rule:r,id:r.id+':in'+j}));
        links.push({source:gate.id,target:'node:'+r.output.node,fromPort:null,toPort:r.output.port,rule:r,id:r.id+':out'});
      }
    });
    edgeGroups=layer.append('g').selectAll('g').data(links).join('g').attr('class',d=>d.rule.kind==='dependency'?'implication-edge dependency-edge':'implication-edge').attr('role','button').attr('tabindex',0).attr('data-rule',d=>d.rule.id).attr('aria-label',d=>`${d.rule.kind==='dependency'?'Research dependency: ':''}${d.rule.id}; weight ${d.rule.weight}${d.rule.inputs.length>1?'; AND, all premises required':''}`);
    edgeGroups.append('title').text(d=>`${d.rule.id}\nWeight ${d.rule.weight}${d.rule.weightDeclared?' (declared)':' (default layout weight)'}\n${d.rule.raw.relation || ''}`);
    edgeGroups.append('path').attr('class','ink').attr('stroke-width',d=>1+Math.min(8,Math.sqrt(d.rule.weight)*1.7)).attr('stroke-dasharray',d=>d.rule.kind==='dependency'?'7 5':null).attr('marker-end','url(#port-arrow)');
    edgeGroups.append('path').attr('class','hit');
    edgeGroups.append('text').attr('class','edge-weight').attr('text-anchor','middle').text(d=>d.rule.weight);
    activate(edgeGroups,d=>selectRule(d.rule));
    gateGroups=layer.append('g').selectAll('g').data(records.filter(n=>n.type==='gate')).join('g').attr('class','and-gate').attr('tabindex',0).attr('role','button').attr('aria-label',d=>'AND: '+d.rule.id);
    gateGroups.append('path').attr('d','M0,-23 L23,0 L0,23 L-23,0 Z');gateGroups.append('text').attr('text-anchor','middle').attr('y',4).text('AND');activate(gateGroups,d=>selectRule(d.rule));
    nodeGroups=layer.append('g').selectAll('g').data(records.filter(n=>n.type==='node')).join('g').attr('class','force-node').attr('data-id',d=>d.node.id);
    const bodies=nodeGroups.append('g').attr('class','node-body').attr('role','button').attr('tabindex',0).attr('aria-label',d=>d.node.title);
    bodies.append('rect').attr('x',d=>-d.w/2).attr('y',d=>-d.h/2).attr('width',d=>d.w).attr('height',d=>d.h).attr('rx',6);
    bodies.each(function(d){d3.select(this).selectAll('text').data(d.lines).join('text').attr('class','node-label').attr('text-anchor','middle').attr('y',(_,i)=>-((d.lines.length-1)*16)/2+i*16+4).text(line=>line);});
    activate(bodies,d=>{selectNode(d.node.id);onNode(d.node.id);});
    nodeGroups.each(function(n){
      const ports=d3.select(this).selectAll('.port').data(PORTS.map(port=>({node:n.node.id,port,key:portKey(n.node.id,port),record:n}))).join('g').attr('class','port').attr('role','button').attr('tabindex',0).attr('data-key',d=>d.key).attr('data-node',d=>d.node).attr('data-port',d=>d.port).attr('aria-label',d=>`${n.node.title}: ${d.port} ${PORT_LABELS[d.port]}`).classed('recorded',d=>n.node.outcome===d.port).attr('transform',d=>{const p=offset({...n,x:0,y:0},d.port);return `translate(${p.x},${p.y})`;});
      ports.append('circle').attr('r',16);ports.append('text').attr('text-anchor','middle').attr('y',4).text(d=>d.port);ports.append('title').text(d=>`${d.port}: ${PORT_LABELS[d.port]}${n.node.outcome===d.port?' (recorded outcome)':''}`);activate(ports,selectPort);
    });
    portGroups=layer.selectAll('.port');
    const drag=d3.drag().on('start',(event,d)=>{event.sourceEvent.stopPropagation();if(!event.active&&!paused)simulation.alphaTarget(.15).restart();d.fx=d.x;d.fy=d.y;}).on('drag',(event,d)=>{d.fx=event.x;d.fy=event.y;d.x=event.x;d.y=event.y;tick();}).on('end',(event,d)=>{if(!event.active)simulation.alphaTarget(0);d.fx=null;d.fy=null;});
    bodies.call(drag);gateGroups.call(drag);
    simulation=d3.forceSimulation(records).velocityDecay(.35)
      .force('link',d3.forceLink(links).id(d=>d.id).distance(linkDistance).strength(linkStrength))
      .force('charge',d3.forceManyBody().strength(-600))
      .force('collision',d3.forceCollide().radius(n=>Math.hypot(n.w,n.h)/2+20).iterations(2))
      .force('gravity',d3.forceRadial(0,450,350).strength(Number(gravityControl.value))).on('tick',tick);
    const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
    simulation.stop();simulation.tick(reduced?150:20);tick();fit();
    if(!reduced)simulation.restart();else{paused=true;document.getElementById('port-pause').textContent='Resume layout';}
    svg.on('click.clear',event=>{if(event.target===svg.node()){clear();onClear();}});
    highlight();
  }
  gravityControl.oninput=()=>{
    document.getElementById('port-gravity-value').value=Number(gravityControl.value).toFixed(2);
    if(!simulation)return;
    simulation.force('gravity').strength(Number(gravityControl.value));
    simulation.alpha(.7);
    if(paused){simulation.tick(150);tick();}else simulation.restart();
  };
  document.getElementById('port-fit').onclick=fit;
  document.getElementById('port-clear').onclick=()=>{clear();onClear();};
  document.getElementById('port-pause').onclick=()=>{paused=!paused;if(paused)simulation?.stop();else simulation?.alpha(.25).restart();document.getElementById('port-pause').textContent=paused?'Resume layout':'Pause layout';};
  return {draw,clear,selectNode,fit,stop:()=>simulation?.stop(),resume:()=>{if(!paused)simulation?.alpha(.12).restart();},getRules:()=>rules};
}
