#!/usr/bin/perl
# R7-22 Perl: Crypt::OpenSSL::RSA
use strict; use warnings;
use Crypt::OpenSSL::RSA;
my $rsa = Crypt::OpenSSL::RSA->generate_key(2048);
$rsa->use_sha256_hash();
my $sig = $rsa->sign("invoice");
