import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const setHolbertonSchools = () => {
  client.hset('HolbertonSchools', 'Portland', 50, redis.print);
  client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  client.hset('HolbertonSchools', 'New York', 20, redis.print);
  client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  client.hset('HolbertonSchools', 'Cali', 40, redis.print);
  client.hset('HolbertonSchools', 'Paris', 2, redis.print);
};

const displayHolbertonSchools = () => {
  client.hgetall('HolbertonSchools', (err, obj) => {
    if (err) {
      console.log(err);
    } else {
      console.log(obj);
    }
  });
};

setHolbertonSchools();
displayHolbertonSchools();

setTimeout(() => {
  client.quit();
}, 1000);
