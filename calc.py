import math

print("====================================")
print(" 🌌 理想氣體熱力學膨脹做功計算機 ")
print("====================================")

try:
    n = float(input("請輸入氣體莫耳數 n (mol) [預設 1.0]: ") or 1.0)
    T = float(input("請輸入絕對溫度 T (K) [預設 300]: ") or 300)
    V1 = float(input("請輸入初始體積 V1 (m³) [預設 1.0]: ") or 1.0)
    V2 = float(input("請輸入膨脹後體積 V2 (m³) [預設 2.0]: ") or 2.0)

    R = 8.314

    if V2 <= V1:
        print("\n❌ 錯誤：終點體積必須大於初始體積！")
    else:
        W_iso = n * R * T * math.log(V2 / V1)
        gamma = 1.4
        P1 = (n * R * T) / V1
        P2 = P1 * (V1 / V2) ** gamma
        W_adi = (P1 * V1 - P2 * V2) / (gamma - 1)

        print("\n🎉 【計算結果】")
        print(f" 🔹 初始壓力 P1       : {P1:.2f} Pa")
        print(f" 🔹 膨脹後壓力 P2 (絕熱): {P2:.2f} Pa")
        print(f" 🔴 等溫膨脹做功 (Isothermal Work) : {W_iso:.2f} 焦耳 (J)")
        print(f" 🔵 絕熱膨脹做功 (Adiabatic Work)  : {W_adi:.2f} 焦耳 (J)")

except ValueError:
    print("\n❌ 錯誤：請輸入正確的數字！")

print("====================================")
input("\n按下 Enter 鍵結束程式...")
