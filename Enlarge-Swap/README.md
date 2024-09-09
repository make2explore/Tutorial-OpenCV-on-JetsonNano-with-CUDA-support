# Tutorial : Resize and Enlarge/Increase Swap memory of Jetson Nano
  
In this Tutorial we will see how to resize and enlarge size of swap memory of Jetson Nano  
  
**Follow the Instructions given below**
- All steps are given with screenshot of each stage.
- Please follow instruction stepwise carefully   
  
## Resize the Swap Memory
Starting with L4T 32.2.1/JetPack 4.2.2, the Jetson Nano by default has 2GB of swap memory.  
  
<img src="/Enlarge-Swap/screenshots/swap18.png" width="650"> 
</br>
  
<img src="/Enlarge-Swap/screenshots/swap5.png" width="450" height="350"> 
</br>
  
- The swap memory allows for "extra memory" when there is memory pressure on main (physical) memory by swapping portions of memory to disk. 
- Because the Jetson Nano has a relatively small amount of memory (4GB) this can be very useful, especially when, say, compiling large projects.  
- The swap memory method in use is Zram. You can examine the swap memory information by using following command:  
  
<blockquote>
$ zramctl</blockquote>
  
<img src="/Enlarge-Swap/screenshots/swap19.png" width="650"> 
  
- You will notice that there are four entries (one for each CPU of the Jetson Nano) /dev/zram0 - /dev/zram3. Each entry has an allocated amount of swap memory associated with it, by default 495.5M, for a total of around 2GB. This is half the size of the main memory. You will find this to be adequate for most tasks.  
- However, there are times you may want to adjust the size of swap memory ... (Like for Installation of OpneCV)

- The configuration for the Zram allocation is done on startup. The file that controls this is 
/etc/systemd/nvzramconfig.sh

- The size of the Zram for each CPU is calculated by the line:  
  
<blockquote>
mem=$((("${totalmem}" / 2 / "${NRDEVICES}") * 1024))
</blockquote>
  
- where totalmem is the total amount of memory, and NRDEVICES is the number of CPUs.

- Basically it divides the amount of physical memory by the number of CPU's with a divisor, in this case 2 to get the 2GB total.  

- You can simply edit this equation using a text editor. You should probably make a backup of the file first, just in case. You will need sudo permissions to change the file.
  
- Install lightweight 'nano' editor  
  ```
  sudo apt-get install nano
  
  ```
  
<img src="/Enlarge-Swap/screenshots/swap7.png" width="450" height="350"> 
  
</br>
  
- Now lets edit the nvzramconfig.sh file using Nano editor
<blockquote>
sudo nano /etc/systemd/nvzramconfig.sh
</blockquote>
  
<img src="/Enlarge-Swap/screenshots/swap21.png" width="450" height="350"> 
  
</br>
  
- For example, you may remove the divisor to get a full 4GB.  
  
<img src="/Enlarge-Swap/screenshots/swap22.png" width="450" height="350"> 
  
</br>
  
- Now reboot the machine for changes to take effect  
<blockquote>
sudo reboot now
</blockquote>
  
- After reboot check the Swap memory using free command of jtop command. You will see Swap=4GB
  
<img src="/Enlarge-Swap/screenshots/swap23.png" width="450" height="350"> 
  
</br>  
<img src="/Enlarge-Swap/screenshots/swap24.png" width="450" height="350"> 
  
</br>
## Enlarge the Swap Memory
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
  

5. Install dphys-swapfile package 
  ```
  sudo apt-get install dphys-swapfile
  
  ```
  
<img src="/Enlarge-Swap/screenshots/swap8.png" width="450" height="350"> 

</br>

<img src="/Enlarge-Swap/screenshots/swap9.png" width="450" height="350"> 

</br>

6. Edit the file to enlarge the boundary 
  ```
  sudo nano /sbin/dphys-swapfile
  
  ```
  
<img src="/Enlarge-Swap/screenshots/swap10.png" width="450" height="350"> 
  
</br>

<img src="/Enlarge-Swap/screenshots/swap11.png" width="450" height="350"> 
  
</br>

<img src="/Enlarge-Swap/screenshots/swap12.png" width="450" height="350"> 
  
</br>

7. Edit another file -  give the required memory size
  ```
  sudo nano /etc/dphys-swapfile
  
  ```
  
<img src="/Enlarge-Swap/screenshots/swap13.png" width="450" height="350"> 
  
</br>

<img src="/Enlarge-Swap/screenshots/swap14.png" width="450" height="350"> 
  
</br>

<img src="/Enlarge-Swap/screenshots/swap15.png" width="450" height="350"> 
  
</br>
  
8. Reboot the board for changes to take effect
  ```
  sudo reboot now
  
  ```
  
<img src="/Enlarge-Swap/screenshots/swap16.png" width="450" height="350"> 
  
</br>
  
9. After Reboot check the swap size using jtop command
  ```
  jtop
  
  ```
  
<img src="/Enlarge-Swap/screenshots/swap17.png" width="450" height="350"> 
  
</br>