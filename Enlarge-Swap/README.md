# Tutorial : Enlarge/Increase Swap memory of Jetson Nano
  
In this Tutorial we will see how to enlarge size of swap memory of Jetson Nano  
  
**Follow the Instructions given below**
- All steps are given with screenshot of each stage.
- Please follow instruction stepwise carefully   
  
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
  
4. Install lightweight 'nano' editor  
  ```
  sudo apt-get install nano
    
  ```
  
  
<img src="/Enlarge-Swap/screenshots/swap7.png" width="450" height="350"> 
  
</br>

