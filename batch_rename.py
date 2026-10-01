import os

print("====================================")
print(" 📁 資料夾檔案批次改名工具 ")
print("====================================")

# 讓使用者輸入路徑
folder_path = input("1. 請貼上資料夾路徑 (例如 C:\\Users\\Name\\Pictures): ").strip()
prefix = input("2. 請輸入新的檔案開頭名稱 (例如 Trip_2026): ").strip()

if not os.path.exists(folder_path):
    print("❌ 錯誤：找不到該資料夾路徑！")
else:
    # 取得資料夾內所有檔案
    files = os.listdir(folder_path)
    count = 1
    
    print("\n🚀 開始改名...")
    for filename in files:
        old_file = os.path.join(folder_path, filename)
        
        # 跳過資料夾，只處理檔案
        if os.path.isfile(old_file):
            # 取得原本的副檔名 (例如 .jpg, .txt)
            file_extension = os.path.splitext(filename)[1]
            
            # 組合新名稱：例如 Trip_2026_1.jpg
            new_filename = f"{prefix}_{count}{file_extension}"
            new_file = os.path.join(folder_path, new_filename)
            
            os.rename(old_file, new_file)
            print(f"  [成功] {filename} ➡️ {new_filename}")
            count += 1
            
    print(f"\n🎉 大功告成！總共處理了 {count-1} 個檔案。")

print("====================================")
input("\n按下 Enter 鍵結束程式...")
