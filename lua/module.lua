module = {}

module.constant = "����һ������"

function module.func1()
	print("����һ�����к���")
end

local function func2()
	print("����һ��˽�к���")
end

function module.func3()
	func2()
end

return module