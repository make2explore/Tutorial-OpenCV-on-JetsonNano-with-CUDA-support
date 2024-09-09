# Tutorial : Resize and Enlarge/Increase Swap memory of Jetson Nano
  
In this Tutorial we will see how to resize and enlarge size of swap memory of Jetson Nano  
  
**Follow the Instructions given below**
- All steps are given with screenshot of each stage.
- Please follow instruction stepwise carefully   
  
Starting with L4T 32.2.1/JetPack 4.2.2, the Jetson Nano by default has 2GB of swap memory.  
  
</br>
<img src="/Enlarge-Swap/screenshots/swap18.png" width="650"> 
</br>
  
<img src="/Enlarge-Swap/screenshots/swap5.png" width="450" height="350"> 
</br>
  
- The swap memory allows for "extra memory" when there is memory pressure on main (physical) memory by swapping portions of memory to disk. 
- Because the Jetson Nano has a relatively small amount of memory (4GB) this can be very useful, especially when, say, compiling large projects.  
  
1. Lets Login into our Jetson Nano. We will use PuTTY software to remotely login into Nano via SSH  
  
<img src="/Enlarge-Swap/screenshots/swap1.png" width="450" height="350">  
  
</br>
  
2. Enter Your credentials - Username and Password  
  
<img src="/Enlarge-Swap/screenshots/swap2.png" width="450" height="350">  
  

<img src="/Enlarge-Swap/screenshots/swap3.png" width="450" height="350"> 

</br>
  
3. Check for any updates available 
  ```
  sudo apt-get update
    
  sudo apt-get upgrade
  
  ```
  
<img src="/Enlarge-Swap/screenshots/swap4.png" width="450" height="350">  
  
</br>
  
<img src="/Enlarge-Swap/screenshots/swap6.png" width="450" height="350">  
  
</br>
  
4. Run jtop command to get information about avalable RAM, ZRAM and Swap memory
  
<img src="/Enlarge-Swap/screenshots/swap5.png" width="450" height="350"> 
  
</br>
  
5. Install lightweight 'nano' editor  
  ```
  sudo apt-get install nano
  
  ```
  
<img src="/Enlarge-Swap/screenshots/swap7.png" width="450" height="350"> 
  
</br>

6. Install dphys-swapfile package 
  ```
  sudo apt-get install dphys-swapfile
  
  ```
  
<img src="/Enlarge-Swap/screenshots/swap8.png" width="450" height="350"> 

</br>

<img src="/Enlarge-Swap/screenshots/swap9.png" width="450" height="350"> 

</br>

7. Edit the file to enlarge the boundary 
  ```
  sudo nano /sbin/dphys-swapfile
  
  ```
  
<img src="/Enlarge-Swap/screenshots/swap10.png" width="450" height="350"> 
  
</br>

<img src="/Enlarge-Swap/screenshots/swap11.png" width="450" height="350"> 
  
</br>

<img src="/Enlarge-Swap/screenshots/swap12.png" width="450" height="350"> 
  
</br>

8. Edit another file -  give the required memory size
  ```
  sudo nano /etc/dphys-swapfile
  
  ```
  
<img src="/Enlarge-Swap/screenshots/swap13.png" width="450" height="350"> 
  
</br>

<img src="/Enlarge-Swap/screenshots/swap14.png" width="450" height="350"> 
  
</br>

<img src="/Enlarge-Swap/screenshots/swap15.png" width="450" height="350"> 
  
</br>
  
9. Reboot the board for changes to take effect
  ```
  sudo reboot now
  
  ```
  
<img src="/Enlarge-Swap/screenshots/swap16.png" width="450" height="350"> 
  
</br>
  
10. After Reboot check the swap size using jtop command
  ```
  jtop
  
  ```
  
<img src="/Enlarge-Swap/screenshots/swap17.png" width="450" height="350"> 
  
</br>