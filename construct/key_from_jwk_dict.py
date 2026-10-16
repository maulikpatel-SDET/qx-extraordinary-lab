"""R7-10 Private key written as a JWK dict literal inside code, loaded with PyJWT."""
import json

from jwt.algorithms import ECAlgorithm

PARTNER_JWK = {
    "kty": "EC",
    "crv": "P-256",
    "x": "7UVhx_XVu9OuazKm599sCzrtiaOAppy99pYasa3WSw4",
    "y": "ROnxZY4ENLwQAf_MjrbZaC9h_Y7UgvLoxjWa1UgxhZY",
    "d": "ucR50oKsfS5x2zNa0XMUECrGfesZ8z8aZzbwsQFkKNg"
}

key = ECAlgorithm.from_jwk(json.dumps(PARTNER_JWK))
