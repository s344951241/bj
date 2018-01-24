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


tab1 = {xx="xxx"}
print(tab1.xx)
print(tab1.vv)
tab = {vv="vvv"}
tab.__index = tab
setmetatable(tab1,tab)
print(tab1.vv)