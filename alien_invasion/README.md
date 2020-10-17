# alien_invasion
### Python编程从入门到实践--项目一--武装飞船
---------

## 环境配置（OS：Ubuntu 20.04）

1. 安装pip
   - *检查是否安装了pip*  `pip -version`
   - *安装pip*
      - *下载get-pip.py*  `wget https://bootstrap.pypa.io/get-pip.py` 
      - *安装pip*  `sudo python3 get-pip.py`

2. 安装Pygame
   ```
   #书上的方法，可能安装不成功，
   #我就没有安装成功，遇到了一个问题，于是找到了下面那个帖子的方法
   sudo apt-get install python3-dev mercurial
   sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev
   sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
   sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcodec-dev
   sudo apt-get install python-numpy

   参考 https://stackoverflow.com/questions/61893077/cannot-install-pygame
   很多Linux发行版有自己的Pygame包
   sudo apt-get install python3-pygame
   ```
