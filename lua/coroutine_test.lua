
co = coroutine.create(
	function(i)
		print(i)
	end
)

coroutine.resume(co,1)
print(coroutine.status(co))

print("---------------------")

co=coroutine.wrap(
	function(i)
		print(i)
	end
)

co(1)
print("----------------------")

co2 = coroutine.create(
	function()
		for i=1,10 do
			print(i)
			if i==3 then
				print(coroutine.status(co2))
				print(coroutine.running())
			end
			coroutine.yield()
		end
	end
)

coroutine.resume(co2)
coroutine.resume(co2)
coroutine.resume(co2)

print(coroutine.status(co2))
print(coroutine.running())

print("------------------")

local newProductor

function productor()
	local i = 0
	while true do
		i = i+1
		send(i)
		if(i>=100) then
			return 
		end
	end
end

function consumer()
	
	while true do
		local i = receive()
		print(i)
		if(i>=100) then
			return 
		end
	end
end

function receive()
	local status,value = coroutine.resume(newProductor)
	return value;
end

function send(x)
	coroutine.yield(x)
end

newProductor = coroutine.create(productor)
consumer()