--[[require "module"

print(module.constant)

module.func3()--]]


local m = require"module"

print(m.constant)

m.func3()

print(_G.module.func3())