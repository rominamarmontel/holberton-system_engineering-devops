-   [](https://students-support.hbtn.io/hc)
    
      
    

----------

----------

# 0x13. Firewall

-   By:  Sylvain Kalache, co-founder at Holberton School
-   Weight:  1
-   Project will start  Sep 5, 2022 12:00 AM, must end by  Sep 6, 2022 12:00 AM
-   will be  released at  Sep 5, 2022 3:36 PM
-   An auto review will be launched at the deadline

### Concepts

_For this project, we expect you to look at this concept:_

-   [Web stack debugging](https://intranet.hbtn.io/concepts/68)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png)

## Background Context

### Your servers without a firewall…

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif)

## Resources

**Read or watch**:

-   [What is a firewall](https://intranet.hbtn.io/rltoken/QS5iHSDU_woydPRIb68sOw "What is a firewall")

## More Info

As explained in the  **web stack debugging guide**  concept page,  `telnet`  is a very good tool to check if sockets are open with  `telnet IP PORT`. For example, if you want to check if port 22 is open on  `web-02`:

```
sylvain@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is '^]'.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.
sylvain@ubuntu$

```

We can see for this example that the connection is successful:  `Connected to web-02.holberton.online.`

Now let’s try connecting to port 2222:

```
sylvain@ubuntu$ telnet web-02.holberton.online 2222
Trying 54.89.38.100...
^C
sylvain@ubuntu$

```

We can see that the connection never succeeds, so after some time I just use  `ctrl+c`  to kill the process.

This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.

Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on  `web-01`, please perform the test from outside of the school network, like from your  `web-02`  server. If you SSH into your  `web-02`  server, the traffic will be originating from  `web-02`  and not from the school’s network, bypassing the firewall.

## Warning!

**Containers on demand cannot be used for this project (Docker container limitation)**

**Be very careful with firewall rules! For instance, if you ever deny port  `22/TCP`  and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.**

### Quiz questions

**Great!**  You've completed the quiz successfully! Keep going!  (Show quiz)

## Your servers

Name

Username

IP

State

4336-web-01

`ubuntu`

`50.19.193.215`

running

Actions  Toggle Dropdown

4336-web-02

`ubuntu`

`54.227.31.122`

running

Actions  Toggle Dropdown

4336-lb-01

`ubuntu`

`18.212.229.8`

running

Actions  Toggle Dropdown

## Tasks

### 0. Block all incoming traffic but

mandatory

Let’s install the  `ufw`  firewall and setup a few rules on  `web-01`.

Requirements:

-   The requirements below must be applied to  `web-01`  (feel free to do it on  `lb-01`  and  `web-02`, but it won’t be checked)
-   Configure  `ufw`  so that it blocks all incoming traffic, except the following TCP ports:
    -   `22`  (SSH)
    -   `443`  (HTTPS SSL)
    -   `80`  (HTTP)
-   Share the  `ufw`  commands that you used in your answer file

**Repo:**

-   GitHub repository:  `holbertonschool-system_engineering-devops`
-   Directory:  `0x13-firewall`
-   File:  `0-block_all_incoming_traffic_but`
