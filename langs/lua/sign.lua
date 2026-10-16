-- R7-22 Lua (OpenResty): lua-resty-rsa
local rsa = require "resty.rsa"
local pub, priv, err = rsa:generate_rsa_keys(2048)
local signer = rsa:new({ private_key = priv, algorithm = "SHA256" })
local sig = signer:sign("invoice")
