param(
  [Parameter(Mandatory=$true)][string]$Prime,
  [Parameter(Mandatory=$true)][string]$Chart
)
$ErrorActionPreference = 'Stop'
$UvPath = 'C:\Users\andrey\.local\bin\uv.exe'
if (-not (Test-Path -LiteralPath $UvPath -PathType Leaf)) { throw "uv executable not found: $UvPath" }
$argsList = @('run','--with','sympy','python','research/benincasa/checkers/check_repaired_low_A7_reconstruction.py',$Prime,$Chart)
$p = Start-Process -FilePath $UvPath -ArgumentList $argsList -WorkingDirectory (Get-Location).Path -WindowStyle Hidden -Wait -PassThru
exit $p.ExitCode
