// R7-15 Node.js running openssl through child_process.
const { execSync, spawnSync } = require('child_process');

execSync('openssl req -x509 -newkey rsa:2048 -nodes -keyout k.pem -out c.pem -days 30 -subj "/CN=qx"');
spawnSync('openssl', ['genpkey', '-algorithm', 'EC', '-pkeyopt', 'ec_paramgen_curve:P-384', '-out', 'p384.key']);
