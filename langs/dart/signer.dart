// R7-22 Dart / Flutter: pointycastle RSA key generation.
import 'package:pointycastle/export.dart';

AsymmetricKeyPair<RSAPublicKey, RSAPrivateKey> makeRsa(SecureRandom rnd) {
  final gen = RSAKeyGenerator()
    ..init(ParametersWithRandom(RSAKeyGeneratorParameters(BigInt.parse('65537'), 2048, 64), rnd));
  final pair = gen.generateKeyPair();
  return AsymmetricKeyPair<RSAPublicKey, RSAPrivateKey>(pair.publicKey as RSAPublicKey, pair.privateKey as RSAPrivateKey);
}
