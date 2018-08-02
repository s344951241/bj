
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

local function sum()
	return 1
end
file = io.open("name.txt","a")
print(file)

local info = debug.getinfo(sum)
for k,v in pairs(info) do
	print(k,':',info[k])
end

tab_df_f={[111] = {id= 111,name="111"},["2222"] ={}}
print((tab_df_f)["2222"])

print("ssss"=="ssss")


for i=1,9,1 do
	print(i)
end


function argsTest(...)
	for a,v in ipairs(arg) do
		print(v)
	end
end

function argsTest2(...)
	
	argsTest(...)
end

argsTest2(1,2,3,4)