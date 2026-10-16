// R7-18 PQC KEMs other than ML-KEM: HQC (NIST pick 2025), Classic McEliece, FrodoKEM, BIKE. Quantum-safe.
package com.qx.exotic;

import java.security.KeyPairGenerator;
import java.security.SecureRandom;
import java.security.Security;

import org.bouncycastle.pqc.jcajce.provider.BouncyCastlePQCProvider;
import org.bouncycastle.pqc.jcajce.spec.BIKEParameterSpec;
import org.bouncycastle.pqc.jcajce.spec.CMCEParameterSpec;
import org.bouncycastle.pqc.jcajce.spec.FrodoParameterSpec;
import org.bouncycastle.pqc.jcajce.spec.HQCParameterSpec;

public class OtherPqcKems {
    public static void main(String[] args) throws Exception {
        Security.addProvider(new BouncyCastlePQCProvider());
        SecureRandom rnd = new SecureRandom();
        KeyPairGenerator hqc = KeyPairGenerator.getInstance("HQC", "BCPQC");
        hqc.initialize(HQCParameterSpec.hqc128, rnd);
        KeyPairGenerator cmce = KeyPairGenerator.getInstance("CMCE", "BCPQC");
        cmce.initialize(CMCEParameterSpec.mceliece348864, rnd);
        KeyPairGenerator frodo = KeyPairGenerator.getInstance("Frodo", "BCPQC");
        frodo.initialize(FrodoParameterSpec.frodokem640aes, rnd);
        KeyPairGenerator bike = KeyPairGenerator.getInstance("BIKE", "BCPQC");
        bike.initialize(BIKEParameterSpec.bike128, rnd);
        for (KeyPairGenerator g : new KeyPairGenerator[]{hqc, cmce, frodo, bike}) {
            System.out.println(g.generateKeyPair().getPublic().getAlgorithm());
        }
    }
}
