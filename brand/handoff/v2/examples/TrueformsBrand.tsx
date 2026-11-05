import type { CSSProperties } from "react";

type Layout = "A" | "B";
type Mode = "color" | "dark" | "mono" | "black" | "white" | "auto";
type LogoProps = { layout?: Layout; mode?: Mode; width?: number;
  assetBase?: string; decorative?: boolean; className?: string; style?: CSSProperties; };
const ratio = 619.5523611111112 / 100.895;
export function TrueformsLogo({layout="B",mode="color",width=240,assetBase="/brand",
  decorative=false,className,style}: LogoProps) {
  const base=assetBase.replace(/\/$/, "");
  const src=(m: Exclude<Mode,"auto">)=>`${base}/trueforms-logo-${layout.toLowerCase()}-${m}.svg`;
  const image=<img src={src(mode==="auto"?"color":mode)} alt={decorative?"":"Trueforms"}
    width={width} height={width/ratio}
    style={{display:"block",width:"100%",height:"auto"}} />;
  return <span className={className} style={{display:"inline-block",width,maxWidth:"100%",...style}}>
    {mode==="auto"?<picture><source media="(prefers-color-scheme: dark)" srcSet={src("dark")}/>{image}</picture>:image}
  </span>;
}
type IconProps={size?:number;label?:string;className?:string;style?:CSSProperties};
export function TrueformsIcon({size=32,label,className,style}:IconProps){return (
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="14.75 12.75 102.5 134.5"
    width={size*102.5/134.5} height={size} className={className}
    role={label?"img":undefined} aria-label={label} aria-hidden={label?undefined:true}
    focusable="false" style={{display:"block",color:"#16765C",...style}}>
    <g transform="translate(4 4)" fill="none" stroke="currentColor" strokeWidth="6.5"
       strokeLinecap="round" strokeLinejoin="round">
      <path d="M60 140H24Q14 140 14 130V22Q14 12 24 12H78L110 44V90"/>
      <path d="M78 12V36Q78 44 86 44H110"/>
      <path d="M34 44H60M34 64H90M34 84H90M34 104H60"/>
      <path d="M70 126L84 140L110 114"/>
    </g>
  </svg>);
}
