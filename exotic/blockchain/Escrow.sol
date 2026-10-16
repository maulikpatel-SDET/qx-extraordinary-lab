// SPDX-License-Identifier: MIT
// R7-20 Smart contract: ecrecover = ECDSA over secp256k1 (quantum-vulnerable), keccak256 hash.
pragma solidity ^0.8.24;

contract Escrow {
    address public signer;

    constructor(address _signer) { signer = _signer; }

    function release(bytes32 orderHash, uint8 v, bytes32 r, bytes32 s) external view returns (bool) {
        bytes32 digest = keccak256(abi.encodePacked("\x19Ethereum Signed Message:\n32", orderHash));
        return ecrecover(digest, v, r, s) == signer;
    }
}
