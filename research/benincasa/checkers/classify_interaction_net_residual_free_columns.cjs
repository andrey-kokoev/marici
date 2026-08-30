#!/usr/bin/env node
"use strict";
const fs=require("fs");
const labels=JSON.parse(fs.readFileSync(process.argv[2],"utf8")).labels;
const ns=JSON.parse(fs.readFileSync(process.argv[3],"utf8"));
const count=new Map();
for(const column of ns.free_columns){
 const l=labels[column], k=l[0], levels=l.slice(1,6), exp=l[6], degree=exp[0]+exp[1];
 const keys=[
  ["k",String(k)],
  ["levels",levels.join("")],
  ["block",k+":"+levels.join("")],
  ["degree",String(degree)],
  ["block_degree",k+":"+levels.join("")+":"+degree],
  ["label",JSON.stringify(l)]
 ];
 for(const [group,key] of keys){
  const mapKey=group+"|"+key;
  count.set(mapKey,(count.get(mapKey)||0)+1);
 }
}
const groups={};
for(const [mapKey,value] of count){
 const split=mapKey.indexOf("|"), group=mapKey.slice(0,split), key=mapKey.slice(split+1);
 (groups[group]??=[]).push([key,value]);
}
for(const group of Object.keys(groups)) groups[group].sort((a,b)=>b[1]-a[1]||a[0].localeCompare(b[0]));
process.stdout.write(JSON.stringify({free_count:ns.free_columns.length,groups},null,2)+"\n");
