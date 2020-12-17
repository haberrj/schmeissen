const io = require('socket.io-client');


document.addEventListener('DOMContentLoaded', () => {
  const socket = io('http://' + document.domain + ':' + location.port + '/game');

  socket.on('connect', () => {
    socket.emit('joined', '');
  });

  socket.on('status', (data) => {
    document.getElementById('chat').value = document.getElementById('chat').value + '<' + data.msg + '>\n';
    document.getElementById('chat').scrollBy(document.getElementById('chat').scrollHeight, 0);
  });

  socket.on('message', (data) => {
    document.getElementById('chat').value = document.getElementById('chat').value + data.msg + '\n';
    document.getElementById('chat').scrollBy(document.getElementById('chat').scrollHeight, 0);
  });

  document.getElementById('text').addEventListener('keydown', (e) => {
    if (e.code === 'Enter') {
      let text = document.getElementById('text').value;
      document.getElementById('text').value = '';
      socket.emit('text', {msg: text});
    }
  });

  document.getElementById('exit').onclick = () => {
    socket.emit('left', {}, () => {
      socket.disconnect();
      window.location.href = "/dashboard";
    });
  };
});
