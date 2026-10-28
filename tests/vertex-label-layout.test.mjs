import test from 'node:test';import assert from 'node:assert/strict';
import {layoutVertexLabels,vertexLabelMetrics} from '../examples/normal-ray/vertex-label-layout.js';
const viewport={width:800,height:600},anchor=(key,x,y,cx=400,cy=300)=>({key,text:'V₁',anchorX:x,anchorY:y,centerX:cx,centerY:cy,visible:true});
test('equal-height anchors receive equal-height labels, independent of vertex index',()=>{
 const a=[anchor('v1',200,200,200,300),anchor('v6',600,200,600,300)],r=layoutVertexLabels(a,viewport);
 assert.equal(r[0].y,r[1].y);assert.equal(r[0].y,164);assert.equal(r[0].x,200);assert.equal(r[1].x,600);
});
test('clearance is constant in CSS pixels at different zooms and parent translations',()=>{
 for(const scale of [.2,1,4]){const a=anchor('v1',400+30*scale,300+20*scale),[r]=layoutVertexLabels([a],viewport);assert.ok(Math.abs(Math.hypot(r.x-a.anchorX,r.y-a.anchorY)-vertexLabelMetrics.clearance)<1e-10);}
 const a=anchor('v1',200,200,200,300),b=anchor('v1',300,250,300,350),[ra]=layoutVertexLabels([a],viewport),[rb]=layoutVertexLabels([b],viewport);assert.equal(rb.x-ra.x,100);assert.equal(rb.y-ra.y,50);
});
test('coincident anchors get deterministic nonoverlapping labels without moving anchors',()=>{
 const a=Array.from({length:8},(_,i)=>anchor(`v${i+1}`,400,300)),snapshot=JSON.stringify(a),r=layoutVertexLabels(a,viewport);
 assert.deepEqual(r,layoutVertexLabels(a,viewport));assert.equal(JSON.stringify(a),snapshot);
 for(let i=0;i<r.length;i++){assert.equal(r[i].anchorX,400);assert.equal(r[i].anchorY,300);assert.ok(Number.isFinite(r[i].leaderX));for(let j=0;j<i;j++)assert.ok(Math.abs(r[i].x-r[j].x)>=44-1e-9||Math.abs(r[i].y-r[j].y)>=44-1e-9);}
});
test('edge labels stay within viewport and hidden anchors do not displace visible labels',()=>{
 const a=[anchor('v1',0,0),anchor('v2',800,600)],r=layoutVertexLabels(a,viewport);
 for(const p of r){assert.ok(p.x>=26&&p.x<=774);assert.ok(p.y>=26&&p.y<=574);}
 assert.deepEqual(layoutVertexLabels([{...a[0],visible:false},a[1]],viewport)[1],layoutVertexLabels([a[1]],viewport)[0]);
});
