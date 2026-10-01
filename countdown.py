import time
import sys

print("====================================")
print(" ⏱️ 終端機極簡倒數計時器 (番茄鐘) ")
print("====================================")

try:
    minutes = int(input("請問要倒數幾分鐘？[預設 25 分鐘]: ") or 25)
    seconds = minutes * 60

    print(f"\n⏳ 倒數 {minutes} 分鐘開始，專心時間！")
    print("------------------------------------")
    
    while seconds > 0:
        # 計算剩餘的分與秒
        mins, secs = divmod(seconds, 60)
        # timer 格式化為 00:00
        timer = f"剩餘時間: {mins:02d}:{secs:02d}"
        
        # \r 可以讓文字在同一行刷新，不會一直往下洗板
        sys.stdout.write(f"\r{timer}")
        sys.stdout.flush()
        
        time.sleep(1)
        seconds -= 1

    # 時間到，印出提示音（\a 在部分系統會觸發嗶聲）
    print("\n\n🎉 時間到！太棒了，休息一下吧！\a")

except ValueError:
    print("\n❌ 錯誤：請輸入整數數字！")

print("====================================")
input("\n按下 Enter 鍵結束程式...")
