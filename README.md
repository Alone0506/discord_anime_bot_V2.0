# discord_anime_bot_V2.0

<p align="center">

<img src="https://img.shields.io/badge/made%20by-Alone-blue.svg" >

<img src="https://img.shields.io/badge/python-3.10.2-green.svg">
  
<img src="https://img.shields.io/badge/discord.py-1.7.3-green.svg">
 
<img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" >

</p>
### 2.0版本支持多伺服器同時使用
因為discord官方規定, 所以此bot目前暫停運作

### 功能介紹
主要功能為到巴哈姆特動畫瘋抓取網頁中的本季新番與週期表的動畫資訊並透過對discord bot 輸入指令的方式獲得動畫資訊, 用戶如果對該動畫有興趣, 也有提供連結可以直接前往觀看.

除此之外, 提供"訂閱"的功能, 每8到12分鐘會根據用戶的訂閱名單上網比對資料, 如果動畫有更新, 便會發出discord 的私人訊息告知用戶動畫已更新.
如果訂閱名單上的新番沒有出現在動畫瘋的新番列表內，也會自動將該動畫移出用戶的訂閱名單.

### 2.0版本支持多伺服器同時使用
在1.0中, 只要用戶輸入指令便會上網抓取檔案, 在單一或少量伺服器的情況下或許可行, 但如果同時有多個伺服器輸入指令, 會導致巴哈認為我的機器人在攻擊伺服器而鎖住機器人的ip.
所以在2.0中因為要避免被鎖iP而採取的作法為每8到12分鐘上網抓取檔案後儲存在伺服器內, 以這種做法來保護機器人.
~(其實可以用proxy, 但實測連到某些server的時候延遲會過高導致訂閱按鈕失效所以作罷 :) )~

### 如何讓這個機器人加到自己的伺服器
只要你有管理員的權限, 按下 : https://discord.com/api/oauth2/authorize?client_id=965889341991825409&permissions=2147502160&scope=bot 就可以讓機器人加入你的discord 群組!!
如果機器人要求的權限你都有給, 那麼在一開始加入的時候機器人會自動添加一個anime-channel的文字頻道到你的伺服器, 可以將此文字頻道設為無通知來避免別人輸入指令後產生的大量的通知.
![螢幕擷取畫面 2022-05-05 151753](https://user-images.githubusercontent.com/90964498/166877800-56491f9f-0eb6-4a19-b0cf-9a62eb60414f.jpg)

### 是否後續更新 ~(應該沒人關心)~
因為這是上禮拜主管在家隔離一個禮拜, 為了避免在公司的時候過於無聊, 為了充(上)實(班)自(裝)我(忙)所以寫了這個side project, 原本預計只花一個禮拜的, 結果為了升級成2.0的版本, 這個東西總共寫了兩個禮拜 :(, 所以後續除非有重大BUG, 不然應該不會再更新了.

### 使用$help的範例
![help](https://user-images.githubusercontent.com/90964498/166421108-dcec8838-60a1-40e0-a832-0a10d9d54e9d.gif)

### 訂閱與取消訂閱某動漫的範例
![sub](https://user-images.githubusercontent.com/90964498/166874343-0a1af364-e6be-4565-9267-168b1d9ef8a8.gif)

### 機器人會自動通知你
![alarm](https://user-images.githubusercontent.com/90964498/166874204-902ceadc-7a78-4f9b-a186-b3428cd14cd3.jpg)

### 心得
#### 其實在1.0寫出來的時候還是很有成就感的, 但因為是第一次碰request, beautifulsoup這些爬蟲工具和第一次碰discord的api 在前期找資料的時候真的花了不少時間, 1.0大概花了1個禮拜左右的時間完成, 但查資料就大概花了3到4天左右吧, 包括CSS Selector和discord components都找了不少資料, 有些是js的不能用, 有些因為是舊的語法所以也不能用, 到頭來只能去找官方的api文檔, 但有些細節官方文檔也沒講, 要配合著Stack Overflow找才有答案. 寫完後因為要讓bot持續上線, 又花了快兩天摸索上線的方式, 最後用repl.it 配合 UptimeRobot 才總算達成了目標. 所以真的在coding的時間大概只有1到2天左右吧. 有些地方也沒有寫的很漂亮, 如果有一天真的要寫3.0了再把語法弄漂亮些.

#### 2.0比起1.0新增的部分大都是python讀寫檔案和處理資料的基本語法而已, 基本上只要大學有修過python, 應該都寫得出來, 唯一不同的地方大概就只有用了defaultdict和with這些東西而已, 大學的課程應該不會教, 但這東西很好用, 學了不會後悔的(大推).除此之外, 花了一點時間嘗試讓bot自動抓網路上提供的免費proxy來連動畫瘋, 但是某些server的延遲太高, 導致discord的按鈕會失效, 原本應該可以用另一個網站檢測延遲的, 不過用越多網站就越容易出錯, 所以就放棄proxy改用8到12分鐘抓一次資料的方式來運作, 以一點延遲換來比較高的穩定性.

#### 最後, 希望我寫的bot能在日常生活幫你節省一點時間, 這是我做這個小小的side project最主要的目標, 下一個side project應該會做google套件後上架, 希望開發過程不會太難 :) .

![nanashi-mumei-mumei](https://user-images.githubusercontent.com/90964498/166890826-c5763d34-179d-4eda-95d5-533aadbeae08.gif)
