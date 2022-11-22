if Error Message occured "illegal instructions (core dumped)",     

add ~/.bashrc

```bash
export OPENBLAS_CORETYPE=ARMV8 
```



the UDP server is ROS Node 
```bash
rosrun udp_hear udp_pub.py
```


udp Client is 
```bash
python client.py
```