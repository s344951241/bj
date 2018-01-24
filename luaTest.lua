Person= {}

function Person:init(o)
	o = o or {}
	setmetatable(o,self)
	self.__index  = self
	return o
end

function Person:print()
	print("this is a person")
end

Man = Person:init()

Man:print()