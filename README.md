# Network Topology with Mininet

This repository is lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program which can generate a network topology using Mininet and use iPerf to measure the bandwidth of the topology.

---
## Objectives

1. Learn how to create a network topology with Mininet
2. Learn how to measure the bandwidth in your network topology with iPerf

---
## Execution

> * Program execution
>
>    First, I have to include some liberary from mininet that will be used in this lab and then define a class "class mytopo(Topo)" for my topology.  In this class, using "build" constructor to construct my own topology, if I want to add a switch, use "switch = self.addSwitch('switchname')", if I want to add a host, use "host = self.addHost('hostname')".
>
>    After adding switches and hosts, we can build connections and set bendwidth, delay and loss betweem each node by using "self.addLink(node1, node2, bw = bendwidth, delay = 'delay', loss = loss)".
>
>    Finally, we can create this topoloty by "topo = mytopo", and than create a network with a OVS controller and use TCLink by using mininet build in function "net = mininet = (topo = topo, controller = OVSController, link = TCLink)". So far, we have create a network with my own topology we can start it with the commend "net.start()", and we can dump the information of switches and hosts by those two command "dumpNodeConnections(net.switches)" and "dumpNodeConnections(net.hosts)". Finally, we want to enter CLI mode, so call the command "CLI(net)" at the end of the code.
> * Screenshot of using iPerf command in Mininet
>
>  ![alt text](https://github.com/nctucn/lab2-Hong-Ming/blob/master/Screen%20Shot%202018-11-29%20at%204.35.08%20PM.png)
>  ![alt text](https://github.com/nctucn/lab2-Hong-Ming/blob/master/Screen%20Shot%202018-11-29%20at%204.38.02%20PM.png)

---
## Description

### Mininet API in Python

- **CLI**

The simple command line interface to interact with nodes in network.

- **TCLink**

Link with symmetric TC interface configured via opts.

- **Mininet**

Network emulator.

- **Topo**

For network representation.

- **OVSController**

Open vSwitch controller.

- **dumpNodeConnections**

Display information of switches and hosts.


### iPerf Commands

- **h2 iperf -s -u -i 1 > ./out/result &**

-s mean run in server mode, -u mean use UDP connection instead of TCP connection, -i mean set interval, in this case, the interval is set to one. > ./out/result & mean write the output into result.

- **h6 iperf -c 10.0.0.2 -u –i 1**

-c mean run in client mode, in this case client h6 connect to server 10.0.0.2. -u and -i is same as above.

### Tasks

1. **Environment Setup**

First, login in the sever and then clone the repository from my GitHub account. Test the mininet see if it works, if not, try the command "service openvswitch-switch start".

2. **Example of Mininet**

Change the permission of example.py to highest permission and execute it, if it can't be executed, clean mininet up by using command "mn -c" and try again.

3. **Topology Generator**

Write the python code and execute it. If there are some bugs in the code, try to ping from host to host in mininet to identify if there are some misconnection in netword topology and remember to dump all the informations of switches and hosts so that you can see the detail of each node. 

4. **Measurement**

Measure the network by the commands provided in slide, compare the result with the one in expected folder, if the result is wrong, go back to identify the errors in program and try again.

---
## References

* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
    * [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
    * [GitHub/OSE-Lab - 熟悉如何使用 Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
    * [菸酒生的記事本 – Mininet 筆記](https://blog.laszlo.tw/?p=81)
    * [Hwchiu Learning Note – 手把手打造仿 mininet 網路](https://hwchiu.com/setup-mininet-like-environment.html)
    * [阿寬的實驗室 – Mininet 指令介紹](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
    * [Mininet 學習指南](https://www.sdnlab.com/11495.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)

---
## Contributors

* [Hong-Ming](https://github.com/Hong-Ming)
* [David Lu](https://github.com/yungshenglu)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3
