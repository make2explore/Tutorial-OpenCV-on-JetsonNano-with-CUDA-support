# OpenCV Installation using script
  
Please note that, Installing OpenCV on your Jetson Nano is bit hectic. With its around 70 command lines, it is more of an lengthy procedure. That's why we created an installation script that executes all commands in this guide at once. Use it if you want, it should not cause any problems. The whole installation will take two-three hours to complete. You may have to give authorization to some commands in between installation.
  
- Please use or update version of OpenCV in following commands according to your choice
- Which means you just have to replace the name of the particular script into following commands  
  
</br>


**1. First, Check your available memory**  
  ```
free -m
  ```
</br>
  
<img src="/Enlarge-Swap/screenshots/swap27.png" width="650"> 
  
</br>

**You need at least 8.5GB of total memory(RAM+Swap) for fast build which utilizes all 4 cores of Jetson Nano**  
If you still have not enough memory, enlarge your swap space as explained in the [Enlarge Swap memory section](https://github.com/make2explore/Tutorial-OpenCV-on-JetsonNano-with-CUDA-support/tree/main/Enlarge-Swap)  
</br>
  
**2. Then download the script from GiHub Repo, please use OpenCV-4-X-X.sh (version) as per your choice** 
  
  ```
wget https://github.com/make2explore/Tutorial-OpenCV-on-JetsonNano-with-CUDA-support/raw/main/OpenCV-Install-Scripts/OpenCV-Latest.sh
  ```
  
**3. Change persmissions of file**
  
  ```
sudo chmod 755 ./OpenCV-Latest.sh
  ```
  
**4. Execute the Script - Please note it will take 2-3 hours to complete**
  
  ```
./OpenCV-Latest.sh
  ```
  
**5. Once the installation is done remove script file**  
  
  ```
rm OpenCV-Latest.sh
  ```

**6. Now lets edit the *nvzramconfig.sh* file using Nano editor, to restore zram to default settings**
  
  ```
sudo nano /etc/systemd/nvzramconfig.sh
  ```
<img src="/Enlarge-Swap/screenshots/swap22.png" width="450" height="350"> 
  
</br>
  
- So in order restore zram to its original default state, you have to add the divisor to get a 2GB. 
- You have to add */2*, refer following screenshot  
  
<img src="/Enlarge-Swap/screenshots/swap21.png" width="450" height="350"> 
  
</br>
  
**7. Remove the (Swap) dphys-swapfile and Free the SD memory**  
  
  ```
sudo /etc/init.d/dphys-swapfile stop
  ```
  
**8. Remove the (Swap) dphys-swapfile package also**  
  
  ```
sudo apt-get remove --purge dphys-swapfile
  ```
  
**9. Save an additional 275 MB by removing installation files**  
  
  ```
sudo rm -rf ~/opencv
  ```

  

  ```
sudo rm -rf ~/opencv_contrib
  ```
</br>
  
**10. Reboot the System for changes to take effect**
  
  ```
sudo reboot now
  ```