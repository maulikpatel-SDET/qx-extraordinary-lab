// R7-17 Stateful hash-based PQC signatures: LMS / HSS and XMSS (NIST SP 800-208). Quantum-safe.
package com.qx.exotic;

import java.security.KeyPairGenerator;
import java.security.SecureRandom;
import java.security.Security;

import org.bouncycastle.pqc.crypto.lms.LMOtsParameters;
import org.bouncycastle.pqc.crypto.lms.LMSigParameters;
import org.bouncycastle.pqc.jcajce.provider.BouncyCastlePQCProvider;
import org.bouncycastle.pqc.jcajce.spec.LMSKeyGenParameterSpec;
import org.bouncycastle.pqc.jcajce.spec.XMSSParameterSpec;

public class StatefulHashSignatures {
    public static void main(String[] args) throws Exception {
        Security.addProvider(new BouncyCastlePQCProvider());
        KeyPairGenerator lms = KeyPairGenerator.getInstance("LMS", "BCPQC");
        lms.initialize(new LMSKeyGenParameterSpec(LMSigParameters.lms_sha256_n32_h10, LMOtsParameters.sha256_n32_w4), new SecureRandom());
        KeyPairGenerator xmss = KeyPairGenerator.getInstance("XMSS", "BCPQC");
        xmss.initialize(new XMSSParameterSpec(10, XMSSParameterSpec.SHA256), new SecureRandom());
        System.out.println(lms.generateKeyPair().getPublic().getAlgorithm());
        System.out.println(xmss.generateKeyPair().getPublic().getAlgorithm());
    }
}
