
# ASSIGNMENT 2 
## Socket Programming TCP Group Chat


### server.py

To begin, we must import the threading and socket modules into server.py.  

Within a program, a thread is a series of instructions. Using several threads is analogous to using multiple programs.

The host id and port number were then set. After that, we make a server object. After that, we must bind the server to the host and the port. Then, for any incoming connection to the server, we initiate listening mode.

To transmit a message from client A to client B, we must first send a message to the server, which acts as an intermediary between the two clients.

After that, we'll make an empty list for clients and the nickname.

Then we create a broadcast function that transmits a message from the server to all connected clients. It only accepts one parameter, i.e., the message.

Create a new function named function handle that manages each client's connection.

Client A connects to the server and sends a message to Client B, so we'll wrap our code in a try accept block to do this, which is used to handle exceptions.

To receive the client's connection, we must now write a function called receive.

On the server, the accept method is always active. It waits for any client to connect. This procedure creates a new socket with the client's connection and address.

Then a message is printed like connection is established and then we want to return the address.

Then invoke the broadcast function inorder to send the message to all the connected users, telling them that this user has joined the chat room.

Lastly, create and start the thread inorder to invoke the handle function.

### client.py

To begin, we must import the threading and socket modules into client.py.

Here, we took input from the client and stored the data to variable nickname.

Then we created a client object.  Instead of binding a client to host, we connect client to local host and our port.

Now we will create two functions for two threads, one for receiving message from other clients through the server and other for send messages to other clients through the server.

For that, first we create a receive function. Inside the function, run a while loop with a try and except block. 

Next, create the write function to run a while loop. Server is listening all time, the client choose nickname connected to server. Client input the message and send it to other clients.

Lastly, we create two threads, one for the receive and other for the write method.

