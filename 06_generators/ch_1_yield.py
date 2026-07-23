def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()

for cup in stall:
    print(cup)


#normal function
def get_chai_list():
    return ["Cup 1", "Cup2", "Cup3"]


#generator function
def get_chai_gen():
    yield "Chai 1"
    yield "Chai 2"
    yield "Chai 3"

chai = get_chai_gen()   # holds the reference only
print(next(chai))
print(next(chai))
print(next(chai))
print(next(chai)) # no more value to yield