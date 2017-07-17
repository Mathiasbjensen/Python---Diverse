import threading

# Example of simple threading

# parameter is the "parent" it inherit from.
class SomeMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

# One of the built in properties for thread is to give it a name.
x = SomeMessenger(name =  "Send out messages")
y = SomeMessenger(name= "Recieve messages")

#Start function goes to the class and looks for a function called 'run'.
x.start()
y.start()

# 