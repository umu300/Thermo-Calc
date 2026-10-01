import random
import time

print("====================================")
print(" 🃏 極簡撲克牌：單人抽鬼牌大賽 ")
print("====================================")

# 1. 初始化撲克牌（數字 1-13 各四張，外加一張鬼牌 'Joker'）
suits = ['♠', '♥', '♦', '♣']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [f"{s}{r}" for s in suits for r in ranks]
deck.append("🃏Joker")  # 加入鬼牌

random.shuffle(deck)

# 2. 發牌（玩家與電腦）
player_hand = []
computer_hand = []

for i, card in enumerate(deck):
    if i % 2 == 0:
        player_hand.append(card)
    else:
        computer_hand.append(card)

# 定義自動丟棄成對手牌的函數
def discard_pairs(hand):
    # 找出純數字/字母部分，例如 '♠A' -> 'A'
    def get_rank(c):
        return c[1:] if c != "🃏Joker" else "Joker"
        
    unique_hand = []
    # 依數字分類
    rank_groups = {}
    for card in hand:
        r = get_rank(card)
        if r not in rank_groups:
            rank_groups[r] = []
        rank_groups[r].append(card)
    
    # 如果同數字有奇數張留一張，偶數張全丟
    for r, cards in rank_groups.items():
        if r == "Joker":
            unique_hand.extend(cards)
        else:
            if len(cards) % 2 != 0:
                unique_hand.append(cards[0])
    return unique_hand

print("\n🔀 正在發牌並自動丟棄花色不同的對子...")
time.sleep(1)
player_hand = discard_pairs(player_hand)
computer_hand = discard_pairs(computer_hand)

# 3. 遊戲主循環
turn = 1  # 1 代表玩家抽電腦，2 代表電腦抽玩家
while len(player_hand) > 0 and len(computer_hand) > 0:
    print("\n" + "-"*40)
    print(f"你的手牌 ({len(player_hand)} 張):", ", ".join(player_hand))
    print(f"電腦手牌剩餘: {len(computer_hand)} 張")
    
    if turn == 1:
        print("\n👉 現在輪到你抽電腦的牌！")
        # 顯示密牌編號給玩家選
        print("電腦的手牌背面：", " ".join([f"[{i+1}]" for i in range(len(computer_hand))]))
        
        try:
            choice = input(f"請選擇要抽哪一張牌 (1-{len(computer_hand)}): ")
            idx = int(choice) - 1
            if idx < 0 or idx >= len(computer_hand):
                print("❌ 超出範圍，系統隨便幫你抽一張！")
                idx = random.randint(0, len(computer_hand)-1)
        except ValueError:
            print("❌ 輸入錯誤，系統隨便幫你抽一張！")
            idx = random.randint(0, len(computer_hand)-1)
            
        # 抽牌邏輯
        chosen_card = computer_hand.pop(idx)
        print(f"🔍 你抽到了：{chosen_card}")
        
        # 加入手牌並檢查是否有對子
        if chosen_card in player_hand: # 理論上花色不同，所以檢查同數字
            player_hand.append(chosen_card)
        else:
            player_hand.append(chosen_card)
            
        player_hand = discard_pairs(player_hand)
        turn = 2
        
    else:
        print("\n🤖 電腦正在思考要抽你的哪一張牌...")
        time.sleep(1.5)
        idx = random.randint(0, len(player_hand)-1)
        chosen_card = player_hand.pop(idx)
        print(f"💥 電腦抽走了你的某一間牌！")
        
        computer_hand.append(chosen_card)
        computer_hand = discard_pairs(computer_hand)
        turn = 1

# 4. 判定輸贏
print("\n====================================")
print(" 🏁 遊戲結束！ ")
print("====================================")
if len(player_hand) == 0 and len(computer_hand) == 0:
    print("🤝 奇蹟發生的平手！兩人都同時把牌出光了！")
elif len(player_hand) == 0:
    print("🎉 恭喜你！手牌先脫手成功，你贏了！")
else:
    print("💀 慘了！鬼牌 🃏Joker 留到最後，你輸了！")
print("====================================")

input("\n按下 Enter 鍵結束遊戲...")
