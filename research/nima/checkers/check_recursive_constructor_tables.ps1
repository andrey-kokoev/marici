$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Sources = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Receipt = Join-Path $Results 'recursive-constructor-formal-audit.json'
if (Test-Path $Receipt) { Remove-Item $Receipt }
Push-Location $Root
try {
  & (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module RecursiveTableRegression -Fresh
  if ($LASTEXITCODE -ne 0) { throw 'Positive compilation failed' }
  $PositivePath = Join-Path $Results 'agda-RecursiveTableRegression.json'
  $Positive = Get-Content $PositivePath -Raw | ConvertFrom-Json
  if (!$Positive.passed -or !$Positive.ignore_interfaces) { throw 'Fresh receipt absent' }
  $Controls = @()
  $Specs = @(
    @{ Name='RecursiveTablesBadCoverage'; Markers=@('maps', 'atom-supported') },
    @{ Name='RecursiveTablesBadCertificateErasure'; Markers=@('false', 'true', 'refl') },
    @{ Name='RecursiveTablesBadRetentionErasure'; Markers=@('retain', 'atom', 'refl') }
  )
  foreach ($Spec in $Specs) {
    $Name = $Spec.Name
    $File = Join-Path $Sources "negative/$Name.agda"
    $Output = & (Join-Path $Tools 'agda-2.8.0/agda.exe') --transliterate -i $Sources -i (Join-Path $Tools 'cubical-0.9') $File 2>&1
    $Code = $LASTEXITCODE
    $Text = $Output | Out-String
    $Text | Set-Content -Encoding utf8 (Join-Path $Results "agda-$Name.log")
    if ($Code -eq 0 -or !$Text.Contains('[UnequalTerms]')) { throw "Wrong rejection: $Name`n$Text" }
    foreach ($Marker in $Spec.Markers) {
      if (!$Text.Contains($Marker)) { throw "Wrong rejection marker: $Name / $Marker`n$Text" }
    }
    $Controls += @{ module=$Name; exit_code=$Code; expected_markers=$Spec.Markers;
      correctly_rejected=$true; source_sha256=(Get-FileHash -Algorithm SHA256 $File).Hash }
  }
  @{ status='independent-recursive-EP-tables-checked'; finished_at=[DateTime]::UtcNow.ToString('o');
     positive_receipt_sha256=(Get-FileHash -Algorithm SHA256 $PositivePath).Hash; controls=$Controls;
     checker_sha256=(Get-FileHash -Algorithm SHA256 $PSCommandPath).Hash;
     scope='Independent typed recursive tables for atom/E/P codes; retained E/P runtime equivalent to the actual seed/E/P-only Resolve closure, for every supplied native admission family. Other five code forms and ten rules are not independently implemented.'
  } | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Receipt
} finally { Pop-Location }
