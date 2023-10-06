# NASA - sonification of Hubble flyby videos

Requirements:

1. Install nginx

`brew install nginx`

2. Add the ngix configuration

`cp nasa.nginx.conf /opt/homebrew/etc/nginx/servers`

3. Restart nginx

`brew services restart nginx`

4. Open the browser: http://127.0.0.1:8082

5. Click the video

TODO:

- figure out a good way to create sounds out of motion detection canvas (shown on bottom right on the page)
- load some better samples in glicol. I've included some free sound samples I downloaded from the internet.
- have fun :)
