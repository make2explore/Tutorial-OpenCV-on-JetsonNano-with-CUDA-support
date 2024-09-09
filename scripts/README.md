# OpenCV Installation using script
  
Please note that, Installing OpenCV on your Jetson Nano is bit hectic. With its around 70 command lines, it is more of an lengthy procedure. That's why we created an installation script that executes all commands in this guide at once. Use it if you want, it should not cause any problems. The whole installation will take two-three hours to complete. You may have to give authorization to some commands in between installation.
  
- Please use or update version of OpenCV in following commands according to your choice
- Which means you just have to replace the name of the particular script into following commands  
  
</br>


**1. Check your memory first**  
  ```
  
free -m  

  ```
**You need at least 6GB**  
If not, enlarge your swap space as explained in the [Enlarge Swap memory section](https://github.com/make2explore/Tutorial-OpenCV-on-JetsonNano-with-CUDA-support/tree/main/Enlarge-Swap)  
  
**2. Then download the script from GiHub Repo, please use OpenCV-4-X-X.sh (version) as per your choice** 
  
  ```
wget https://github.com/make2explore/Tutorial-OpenCV-on-JetsonNano-with-CUDA-support/blob/main/scripts/OpenCV-4-10-0.sh  
  
  ```
  
**3. Change persmissions of file**
  
  ```
sudo chmod 755 ./OpenCV-4-10-0.sh  
  
  ```
  
**4. Execute the Script - Please note it will take 2-3 hours to complete**
  
  ```
./OpenCV-4-10-0.sh  
  
  ```
  
**5. Once the installation is done remove script file**  
  
  ```
rm OpenCV-4-10-0.sh  
  
  ```
  
**6. Remove the (Swap) dphys-swapfile and Free the SD memory**  
  
  ```
sudo /etc/init.d/dphys-swapfile stop  
  
  ```
  
**7. Remove the (Swap) dphys-swapfile package also**  
  
  ```
sudo apt-get remove --purge dphys-swapfile  
  
  ```
  
**8. Save an additional 275 MB by removing installation files**  
  
  ```
  
sudo rm -rf ~/opencv  
  
  ```

  

  ```
  
$ sudo rm -rf ~/opencv_contrib  
  
  ```