const express = require('express');
const socketio = require('socket.io');
const http = require('http');

const PORT = process.env.PORT || 5000;

const router = require('./router');

const app = express();
const server = http.createServer(app);
const io = socketio(server);

io.on('connection', () => {
    console.log('We have a new connection!!');

    socket.on('disconnect', () => {
        console.log('User has left the chat!')
    });
});

app.use(router);

server.listen(PORT, () => console.log(`Server is running on ${PORT}`));