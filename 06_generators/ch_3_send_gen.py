def chai_cust():
    print("Welcome! What chai would you like?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_cust()

next(stall)     # start the gen

# stall.send("Masala Chai") # when commented then yield waits for the send message to come in order
# stall.send("Lemon Chai")