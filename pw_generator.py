import random
import string

print("====================================")
print(" 🔐 高強度隨機密碼生成器 ")
print("====================================")

try:
    length = int(input("請輸入想要的密碼長度 [預設 12 位數]: ") or 12)
    
    if length < 4:
        print("❌ 為了安全起見，密碼長度至少需要 4 位數！")
    else:
        # 定義密碼字元池
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = "!@#$%^&*"
        
        all_chars = lower + upper + digits + symbols
        
        # 確保密碼裡至少包含「各一個」大小寫、數字和符號，避免完全隨機漏掉
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(symbols)
        ]
        
        # 剩下的長度隨機補滿
        password += random.choices(all_chars, k=length - 4)
        
        # 把順序打亂，避免前四碼固定是特定類型
        random.shuffle(password)
        final_password = "".join(password)
        
        print("\n🎉 【生成成功】")
        print(f" 🔑 您的安全密碼為： {final_password}")
        print("\n提示：請妥善複製儲存，視窗關閉後將不留紀錄。")

except ValueError:
    print("❌ 錯誤：長度請輸入整數數字！")

print("====================================")
input("\n按下 Enter 鍵結束程式...")
