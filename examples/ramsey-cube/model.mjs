// Catalogue record 1 (r38_27.g6.gz); one-based labels match the spreadsheet.
export const seven=new URLSearchParams(globalThis.location?.search).get('case')==='3-7'
export const graphCode=seven?'U???GOOGIGPB`SQgg[cEoKaagg@iI@w@`ROCrGA?':String.raw`ZGoXI_J?Ec@JScg@sa@o_OG\CP?IOd?KCQ?LA?WlH_@AC?i?@Ab?Ql?oY?AO`
export const root=seven?5:1
export const vertices=Array.from({length:graphCode.charCodeAt(0)-63},(_,i)=>i+1)
export function relation(a,b){
  if(a===b)return 'N'
  const hi=Math.max(a,b)-1, lo=Math.min(a,b)-1, bit=hi*(hi-1)/2+lo
  return ((graphCode.charCodeAt(1+Math.floor(bit/6))-63)>>(5-bit%6))&1?'R':'B'
}
export const anchors=[root,...vertices.filter(v=>relation(root,v)==='R')]
export const row=v=>anchors.map(a=>relation(v,a))
export const position=v=>[(v-1)%3-1,1-Math.floor((v-1)%9/3),1-Math.floor((v-1)/9)]
export const redEdges=vertices.flatMap(b=>vertices.filter(a=>a<b&&relation(a,b)==='R').map(a=>[a,b]))
