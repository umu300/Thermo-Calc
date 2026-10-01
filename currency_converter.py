print("====================================")
print(" 💵 極簡多國貨幣換算機 (離線版) ")
print("====================================")

# 設定基本基準匯率 (以 1 台幣 TWD 為基準的概略匯率)
# 註：此為範例固定匯率，使用者可自行在程式碼內修改
TWD_TO_USD = 0.031   # 美金
TWD_TO_JPY = 4.65    # 日幣
TWD_TO_EUR = 0.029   # 歐元
TWD_TO_KRW = 41.5    # 韓元

try:
    twd_amount = float(input("請輸入台幣金額 (TWD): ") or 0)
    
    if twd_amount <= 0:
        print("❌ 請輸入大於 0 的金額！")
    else:
        print(f"\n💰 【新台幣 {twd_amount:,.0f} 元】 可兌換：")
        print(f"  🇺🇸 美金 (USD) : ${twd_amount * TWD_TO_USD:,.2f}")
        print(f"  🇯🇵 日幣 (JPY) : ¥{twd_amount * TWD_TO_JPY:,.0f}")
        print(f"  🇪🇺 歐元 (EUR) : €{twd_amount * TWD_TO_EUR:,.2f}")
        print(f"  🇰🇷 韓元 (KRW) : ₩{twd_amount * TWD_TO_KRW:,.0f}")

except ValueError:
    print("❌ 錯誤：請輸入正確的數字金額！")

print("====================================")
input("\n按下 Enter 鍵結束程式...")
