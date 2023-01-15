import sqlite3

emo_list = ['喜び', '信頼', '恐れ', '驚き', '悲しみ', '嫌悪', '怒り', '期待']

connection = sqlite3.connect('flower.db')

def get_print():
    print("以下の感情の数字を入力してください")
    print("0を入力するまで続きます")
    for ind, emo in enumerate(emo_list):
        print(f"{ind+1}:{emo}", end=" ")
    print("")

def searchEmotion(emo):
    result = connection.execute(f'select * from mean where lab_id = {emo};')
    return result

def get_data(num):
    if (num-1 >= 0) and (num-1 < len(emo_list)):
        result = searchEmotion(num-1)
        for row in result:
            print(f'花の名前:{row[3]}, 花の種類：{row[0]}, 花の意味：{row[2]}')
    elif num==0:
        print("システムを終了します")
    else:
        print("入力が範囲外です")

a = None
while(a!=0):
    get_print()
    a = int(input())
    get_data(a)

connection.close()
