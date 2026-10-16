# R7-22 Elixir / Erlang :public_key
defmodule Qx.Signer do
  def rsa_key, do: :public_key.generate_key({:rsa, 2048, 65537})
  def ec_key, do: :public_key.generate_key({:namedCurve, :secp256r1})
  def sign(msg, key), do: :public_key.sign(msg, :sha256, key)
end
