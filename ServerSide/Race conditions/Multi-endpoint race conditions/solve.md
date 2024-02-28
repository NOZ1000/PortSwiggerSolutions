## First Attempt

My first mistake, i thought that the challenge was in abbusing gift cards. And u successfully added 4000$ to my account. But i was wrong. And i couldnt use this money. So my second try was the next day after i rereaded the topic infomation.

## Second Attempt

After rereading the topic information, i realized that the delay between payment and adding item to the cart was different. And i would be able to fit in the time between the payment and adding the item to the cart `after adding some garbage requests` after payment and before adding the item to the cart.

![image](./Screenshot%20from%202024-02-28%2020-24-31.png)

## Solution

1. Sended to repeater the request to add the target item(1337$) to the cart, garbage requests(get request to the main page) and the payment request.
2. Also in my cart was 1 item for 20$.
3. In repeater added requsets to group: `Payment`, `Garbage`, `Garbage`, `Add to cart 1337% item`.
4. Then sended the group using signle packet request(in parallel).
5. Also to find the gap between payment and adding the item to the cart, i just attempeted several times to find the right time.

## The main idea

The main idea is to fill the gap between payment and adding the item to the cart with garbage requests and then add the target item to the cart.