
'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  - /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           佛祖保佑     永不宕机     永无BUG

       佛曰:  
               写字楼里写字间，写字间里程序员；  
               程序人员写程序，又拿程序换酒钱。  
               酒醒只在网上坐，酒醉还来网下眠；  
               酒醉酒醒日复日，网上网下年复年。  
               但愿老死电脑间，不愿鞠躬老板前；  
               奔驰宝马贵者趣，公交自行程序员。  
               别人笑我忒疯癫，我笑自己命太贱；  
               不见满街漂亮妹，哪个归得程序员？
'''
#输出歌词
from time import sleep


sleep(0.2)
print('歌词准备打印')


l1 = "Soldier keep on marchin' on\nHead down 'til the work is done\nWaiting on that morning sun\nSoldier keep on marchin' on\n"
l2 = "Head in the dust, feet in the fire\nLabour on that midnight wire\nListening for that angel choir\nYou got nowhere to run\nYou wanna take a drink of that\npromise land\n"
l3 = "You gotta wipe the dirt off of\nyour hands\nCareful son, you got dreamer'splans\nBut it gets hard to stand\n"
l4 = "Soldier keep on marchin' on\nHead down 'til the work is done\nWaiting on that morning sun"

    #调用VIP进度条


from tqdm import tqdm

for i in tqdm(range(1, 100)):


    sleep(0.1)

sleep(0.9)

    #打印
with open('FuckLyrics.txt', 'a') as file:
   
    file.writelines([l1, l2, l3, l4])
    file.flush()
    #end
sleep(0.2)
print('歌词已经打印到"FuckLyrics.txt"中')
sleep(1)


 
