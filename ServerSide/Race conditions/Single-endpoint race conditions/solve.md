## Solution

That was easy trick, we just need to intercept the request to change email. Send to repeater, dublicate the request and change the email in the second request to carlos@ginandjuice.shop in the first request to my initial email. Then send the requests in parallel(single packet). Check email for verification link. Remove carlos in admin panel.