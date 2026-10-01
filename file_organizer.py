import os
import shutil

print("====================================")
print(" 🧹 自動檔案分類整理小助手 ")
print("====================================")

target_dir = input("請貼上要整理的資料夾路徑 (例如 C:\\Users\\Name\\Downloads): ").strip()

# 定義副檔名對應的資料夾名稱
EXTENSION_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.txt', '.md'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Audio_Video': ['.mp3', '.wav', '.mp4', '.mkv', '.avi', '.mov'],
    'Installers': ['.exe', '.msi', '.dmg', '.pkg']
}

if not os.path.exists(target_dir):
    print("❌ 錯誤：找不到該資料夾路徑！")
else:
    print("\n🚀 開始分類檔案...")
    moved_count = 0
    
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        
        # 跳過資料夾
        if os.path.isdir(file_path):
            continue
            
        # 取得副檔名並轉小寫
        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        
        # 尋找對應的資料夾
        moved = False
        for folder_name, extensions in EXTENSION_MAP.items():
            if ext in extensions:
                # 建立分類資料夾
                dest_folder = os.path.join(target_dir, folder_name)
                os.makedirs(dest_folder, exist_ok=True)
                
                # 移動檔案
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"  [歸類] {filename} ➡️ {folder_name}/")
                moved_count += 1
                moved = True
                break
                
        # 如果是不認識的副檔名，丟到 Other
        if not moved and ext != '':
            dest_folder = os.path.join(target_dir, 'Others')
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_folder, filename))
            print(f"  [歸類] {filename} ➡️ Others/")
            moved_count += 1

    print(f"\n🎉 整理完畢！共自動分類了 {moved_count} 個檔案。")

print("====================================")
input("\n按下 Enter 鍵結束程式...")
