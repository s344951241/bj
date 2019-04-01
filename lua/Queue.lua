local Queue = {}

function Queue:ctor(capacity)
    self.capacity = capacity or 5
    self.queue = {}
    self.size = 0
    self.head = -1
    self.rear = -1
end

function Queue:EnQueue(element)
    if self.size == 0 then
        self.head = 0 
        self.rear = 1
        self.size =1
        self.queue[self.rear] = element
    else
        local temp = (self.rear+1)%self.capacity
        if temp==self.head then
            return
        else
            self.rear = temp
        end
        self.queue[self.rear] = element
        self.size = self.size+1
    end
end

function Queue:DeQueue()
    if self:IsEmpty() then
        return
    end
    self.size = self.size-1
    self.head = (self.head+1)%self.capacity
    local value = self.queue[self.head]
    return value
end
function Queue:IsEmpty()
    if self:Size()==0 then
        return true    
    end
    return false
end
function Queue:Size()
    return self.size    
end
Queue:ctor(5)
Queue:EnQueue(1)
Queue:EnQueue(2)
print(Queue:DeQueue())
print(Queue:DeQueue())
