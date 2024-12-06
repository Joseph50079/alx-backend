import { createClient } from 'redis';

function redisConnect() {
    const client = createClient({
        url: 'redis://127.0.0.1:6379',
    });

  client.on('connect', function () {
    console.log('Redis client connected to the server');
  }).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

  (async () => {
    await client.connect();
  })();

};

redisConnect();