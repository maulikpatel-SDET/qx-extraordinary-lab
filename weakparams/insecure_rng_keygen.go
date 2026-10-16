// R7-13 Go: RSA key from math/rand (deterministic) instead of crypto/rand.
package weakparams

import (
	"crypto/rsa"
	mathrand "math/rand"
)

func PredictableKey() (*rsa.PrivateKey, error) {
	src := mathrand.New(mathrand.NewSource(42))
	return rsa.GenerateKey(src, 2048)
}
