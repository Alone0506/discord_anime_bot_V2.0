# discord_anime_bot_V2.0

<p align="center">

<img src="https://img.shields.io/badge/made%20by-Alone-blue.svg" >

<img src="https://img.shields.io/badge/python-3.10.2-green.svg">
  
<img src="https://img.shields.io/badge/discord.py-1.7.3-green.svg">
 
<img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" >

</p>

### 功能介紹
主要功能為到巴哈姆特動畫瘋抓取網頁中的本季新番與週期表的動畫資訊並透過對discord bot 輸入指令的方式獲得動畫資訊, 用戶如果對該動畫有興趣, 也有提供連結可以直接前往觀看.

除此之外, 提供"訂閱"的功能, 每3到5分鐘會根據用戶的訂閱名單上網比對資料, 如果動畫有更新, 便會發出discord 的私人訊息告知用戶動畫已更新.
如果訂閱名單上的新番沒有出現在動畫瘋的新番列表內，也會自動將該動畫移出用戶的訂閱名單.

### 2.0版本支持多伺服器同時使用
在1.0中, 只要用戶輸入指令便會上網抓取檔案, 在單一或少量伺服器的情況下或許可行, 但如果同時有多個伺服器輸入指令, 會導致巴哈認為我的機器人在攻擊伺服器而鎖住機器人的ip.
所以在2.0中因為要避免被鎖iP而採取的作法為每3到5分鐘上網抓取檔案後儲存在伺服器內, 以這種做法來保護機器人.
~(其實可以用proxy, 但實測連到某些server的時候延遲會過高導致訂閱按鈕失效所以作罷 :) )~

### 如何讓這個機器人加到自己的伺服器
只要你有管理員的權限, 點擊 : https://discord.com/api/oauth2/authorize?client_id=965889341991825409&permissions=2147502160&scope=bot 即可讓機器人加入你的discord 群組!!
如果機器人要求的權限你都有給, 那麼在一開始加入的時候機器人會自動添加一個anime-channel的文字頻道到你的伺服器, 可以將此文字頻道設為無通知來避免在獲得新番資訊的時候
![螢幕擷取畫面 2022-05-05 151753](https://user-images.githubusercontent.com/90964498/166877800-56491f9f-0eb6-4a19-b0cf-9a62eb60414f.jpg)

### 使用$help的範例
![help](https://user-images.githubusercontent.com/90964498/166421108-dcec8838-60a1-40e0-a832-0a10d9d54e9d.gif)

### 訂閱與取消訂閱某動漫的範例
![sub](https://user-images.githubusercontent.com/90964498/166874343-0a1af364-e6be-4565-9267-168b1d9ef8a8.gif)

### 機器人會自動通知你
![alarm](https://user-images.githubusercontent.com/90964498/166874204-902ceadc-7a78-4f9b-a186-b3428cd14cd3.jpg)
