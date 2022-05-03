# discord_anime_bot_V2.0

<p align="center">

<img src="https://img.shields.io/badge/made%20by-Alone-blue.svg" >

<img src="https://img.shields.io/badge/python-3.10.2-green.svg">
  
<img src="https://img.shields.io/badge/discord-1.7.3-green.svg">
 
<img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" >

<img src="https://img.shields.io/github/languages/top/Alone0506/discord_anime_bot_V2.0.svg">

</p>

### 功能介紹
主要功能為到巴哈姆特動畫瘋抓取網頁中的本季新番與週期表的動畫資訊並透過對discord bot 輸入指令的方式獲得動畫資訊, 用戶如果對該動畫有興趣, 也有提供連結可以直接前往觀看.

除此之外, 提供"訂閱"的功能, 每3到5分鐘會根據用戶的訂閱名單上網比對資料, 如果動畫有更新, 便會發出discord 的私人訊息告知用戶動畫已更新.
如果訂閱名單上的新番沒有出現在動畫瘋的新番列表內，也會自動將該動畫移出用戶的訂閱名單.

### 2.0版本支持多伺服器同時使用
在1.0中, 只要用戶輸入指令便會上網抓取檔案, 在單一或少量伺服器的情況下或許可行, 但如果同時有多個伺服器輸入指令, 會導致巴哈認為我的機器人在攻擊伺服器而鎖住機器人的ip.
所以2.0的作法為每3到5分鐘上網抓取檔案後儲存在伺服器內, 因為用戶通常對於動畫更新並不要求要馬上看到, 所以採取延遲3到5分鐘的做法來保護機器人不被鎖ip.\
~(其實可以用代理ip, 但是我是懶得持續上網更新免費的ip)~

### 使用$help的範例
![help](https://user-images.githubusercontent.com/90964498/166421108-dcec8838-60a1-40e0-a832-0a10d9d54e9d.gif)