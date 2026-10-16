# R7-16 PowerShell (Windows admins): self-signed RSA cert + ECDSA cert in the machine store.
$rsa = New-SelfSignedCertificate -DnsName "svc.qx.example.com" -CertStoreLocation "Cert:\LocalMachine\My" `
        -KeyAlgorithm RSA -KeyLength 2048 -HashAlgorithm SHA256 -NotAfter (Get-Date).AddYears(5)
$ec  = New-SelfSignedCertificate -DnsName "api.qx.example.com" -CertStoreLocation "Cert:\LocalMachine\My" `
        -KeyAlgorithm ECDSA_nistP256 -CurveExport CurveName
Export-PfxCertificate -Cert $rsa -FilePath C:\certs\svc.pfx -Password (ConvertTo-SecureString "changeit" -AsPlainText -Force)
