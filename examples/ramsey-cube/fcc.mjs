// Conventional FCC coordinates: even x+y+z. One nearest-neighbour step
// changes two coordinates by one. Cube-frame strides (2,0,0) are not NN bonds.
import {anchors,vertices} from './model.mjs'
export const world=p=>p.map(x=>(x-4)/4)
const sites=new Map(),key=p=>p.join(',');for(let x=0;x<=8;x++)for(let y=0;y<=8;y++)for(let z=0;z<=8;z++)if((x+y+z)%2===0)sites.set(key([x,y,z]),[x,y,z])
const interior=p=>p.every(x=>x>0&&x<8),steps=[];for(let i=-1;i<=1;i++)for(let j=-1;j<=1;j++)for(let k=-1;k<=1;k++)if(i*i+j*j+k*k===2)steps.push([i,j,k])
const corners=Array.from({length:8},(_,i)=>[i&1?8:0,i&2?8:0,i&4?8:0]);const body=[[4,4,4],...steps.map(s=>s.map(x=>4+2*x)),...[0,1,2].flatMap(i=>[-2,2].map(d=>[4,4,4].map((x,j)=>x+(i===j?d:0))))];const free=vertices.filter(v=>!anchors.includes(v));export const site=v=>anchors.includes(v)?corners[anchors.indexOf(v)]:body[free.indexOf(v)]
export const frame=[];for(const p of corners)for(let axis=0;axis<3;axis++)if(!p[axis])for(let n=0;n<8;n+=2)frame.push([n,n+2].map(t=>p.map((x,i)=>i===axis?t:x)))
const occupied=new Set(vertices.map(v=>key(site(v))))
export function route(a,b){const start=site(a),end=site(b),q=[start],parent=new Map([[key(start),null]]);for(let h=0;h<q.length;h++){const p=q[h];if(key(p)===key(end)){const path=[];for(let u=p;u;u=parent.get(key(u)))path.push(u);return path.reverse()}
 for(const s of steps){const u=sites.get(key(s.map((x,i)=>x+p[i])));if(!u||parent.has(key(u)))continue;const last=key(u)===key(end);if(!last&&occupied.has(key(u)))continue;
 // A cube corner needs one face-diagonal hop before it can enter the bulk.
 if(!interior(u)&&!last&&![start,end].some(t=>t.every(x=>x===0||x===8)&&t.reduce((d,x,i)=>d+(x-u[i])**2,0)===2))continue;
 parent.set(key(u),p);q.push(u)}}throw Error(`No FCC path ${a}-${b}`)}
