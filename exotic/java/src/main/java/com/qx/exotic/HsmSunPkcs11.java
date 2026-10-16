// R7-21 Java SunPKCS11 provider: RSA key pair generated in the HSM.
package com.qx.exotic;

import java.security.KeyPairGenerator;
import java.security.Provider;
import java.security.Security;

public class HsmSunPkcs11 {
    public static void main(String[] args) throws Exception {
        Provider p = Security.getProvider("SunPKCS11").configure("/etc/qx/pkcs11.cfg");
        Security.addProvider(p);
        KeyPairGenerator g = KeyPairGenerator.getInstance("RSA", p);
        g.initialize(3072);
        System.out.println(g.generateKeyPair().getPublic().getAlgorithm());
    }
}
