$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Sources = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Receipt = Join-Path $Results 'native-table-formal-audit.json'
if (Test-Path $Receipt) { Remove-Item $Receipt }
Push-Location $Root
try {
  & (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module NativeTableRegression -Fresh
  if ($LASTEXITCODE -ne 0) { throw 'Positive compilation failed' }
  $PositivePath = Join-Path $Results 'agda-NativeTableRegression.json'
  $Positive = Get-Content $PositivePath -Raw | ConvertFrom-Json
  if (!$Positive.passed -or !$Positive.ignore_interfaces) { throw 'Fresh receipt absent' }
  $Specs = @(
    @{ Name='NativeTableBadAttachment'; Markers=@('Bool', 'Unit') },
    @{ Name='NativeTableBadConstructorErasure'; Markers=@('atom-header', 'maps-header', 'refl') },
    @{ Name='NativeTableBadFillerErasure'; Diagnostic='[MismatchedProjectionsError]'; Markers=@('fst', 'snd', 'refl') },
    @{ Name='NativeTableBadCertificateErasure'; Markers=@('false', 'true', 'refl') },
    @{ Name='NativeTableBadRetentionErasure'; Markers=@('retain-header', 'atom-header', 'refl') },
    @{ Name='NativeTableBadFirstJetReadout'; Markers=@('0 != 1', 'zero-jet', 'bump-jet', 'refl') }
  )
  $Controls = @()
  foreach ($Spec in $Specs) {
    $Name = $Spec.Name
    $File = Join-Path $Sources "negative/$Name.agda"
    $Output = & (Join-Path $Tools 'agda-2.8.0/agda.exe') --transliterate -i $Sources -i (Join-Path $Tools 'cubical-0.9') $File 2>&1
    $Code = $LASTEXITCODE
    $Text = $Output | Out-String
    $Text | Set-Content -Encoding utf8 (Join-Path $Results "agda-$Name.log")
    $Diagnostic = if ($Spec.Diagnostic) { $Spec.Diagnostic } else { '[UnequalTerms]' }
    if ($Code -eq 0 -or !$Text.Contains($Diagnostic)) { throw "Wrong rejection: $Name`n$Text" }
    foreach ($Marker in $Spec.Markers) {
      if (!$Text.Contains($Marker)) { throw "Wrong rejection marker: $Name / $Marker`n$Text" }
    }
    $Controls += @{ module=$Name; exit_code=$Code; expected_diagnostic=$Diagnostic; expected_markers=$Spec.Markers;
      correctly_rejected=$true; source_sha256=(Get-FileHash -Algorithm SHA256 $File).Hash }
  }
  @{ status='full-typed-native-table-equivalence-checked'; finished_at=[DateTime]::UtcNow.ToString('o');
     positive_receipt_sha256=(Get-FileHash -Algorithm SHA256 $PositivePath).Hash;
     checker_sha256=(Get-FileHash -Algorithm SHA256 $PSCommandPath).Hash; controls=$Controls;
     scope='All eight original Code forms, complete packages, all twelve independently implemented native rule schemas and their marked ports/boundaries, and actual retained Resolve closures for arbitrary original seed families. Intrinsic typed recursive tables, not arbitrary malformed raw tables or unmarked regrouping alone. Independent exact finite second-jet readout agrees with both existing tidal routes; no continuum topology/completion or new physical realization is asserted.'
  } | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Receipt
} finally { Pop-Location }
