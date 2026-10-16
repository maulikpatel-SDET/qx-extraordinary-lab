// R7-22 Scala on the JVM: JCA EC key + SHA256withECDSA.
import java.security.{KeyPairGenerator, Signature}
import java.security.spec.ECGenParameterSpec

object Signer {
  def sign(data: Array[Byte]): Array[Byte] = {
    val g = KeyPairGenerator.getInstance("EC")
    g.initialize(new ECGenParameterSpec("secp384r1"))
    val kp = g.generateKeyPair()
    val s = Signature.getInstance("SHA384withECDSA")
    s.initSign(kp.getPrivate)
    s.update(data)
    s.sign()
  }
}
