# OpenCV Installation using script
  
Please note that, Installing OpenCV on your Jetson Nano is bit hectic. With its around 70 command lines, it is more of an lengthy procedure. That's why we created an installation script that executes all commands in this guide at once. Use it if you want, it should not cause any problems. The whole installation will take two-three hours to complete. You may have to give authorization to some commands in between installation.
  
- Please use or update version of OpenCV in following commands according to your choice
- Which means you just have to replace the name of the particular script into following commands  
  
</br>

  ```
  
# check your memory first
$ free -m  
  
# you need at least a total of 8.5 GB!  
# if not, enlarge your swap space as explained in the guide  
  
$ wget https://github.com/make2explore/Tutorial-OpenCV-on-JetsonNano-with-CUDA-support/blob/main/scripts/OpenCV-4-10-0.sh  
  
$ sudo chmod 755 ./OpenCV-4-10-0.sh  
  
$ ./OpenCV-4-10-0.sh  
  
# once the installation is done...  
  
$ rm OpenCV-4-10-0.sh  
  
# remove the dphys-swapfile now  
  
$ sudo /etc/init.d/dphys-swapfile stop  
  
$ sudo apt-get remove --purge dphys-swapfile  
  
# just a tip to save an additional 275 MB  
  
$ sudo rm -rf ~/opencv  
  
$ sudo rm -rf ~/opencv_contrib  
  
  ```