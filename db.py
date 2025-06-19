
#カラム名の変更
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

#idがnobunagaのtext1カラムにxxx,text2カラムにyyyを設定
# c.execute("UPDATE result SET text2 = '常識にとらわれず突き進むところが魅力です。出世欲が強く努力を惜しまないタイプ。成功を手にすると遊びほうけて身を滅ぼすことがあります。' WHERE id = 'hideyoshi'")



# idがnobunagaのimageカラムにnobunaga.jpgを設定
# c.execute("UPDATE result SET image = 'ieyasu.jpg' WHERE id = 'ieyasu'")
# c.execute("UPDATE result SET image = 'tadakatu.jpg' WHERE id = 'tadakatu'")
# c.execute("UPDATE result SET image = 'mitsunari.jpg' WHERE id = 'mitsunari'")
# c.execute("UPDATE result SET image = 'hideyoshi.jpg' WHERE id = 'hideyoshi'")
# c.execute("UPDATE result SET image = 'kanetsugu.jpg' WHERE id = 'kanetsugu'")
# c.execute("UPDATE result SET image = 'katsuyori.jpg' WHERE id = 'katsuyori'")
# c.execute("UPDATE result SET image = 'mitsuhide.jpg' WHERE id = 'mitsuhide'")
# c.execute("UPDATE result SET image = 'yoshimoto.jpg' WHERE id = 'yoshimoto'")


# カラムの追加
# c.execute("ALTER TABLE result ADD COLUMN image TEXT")
# c.execute("ALTER TABLE result ADD COLUMN text2 TEXT")
# print("カラム が追加されました。")

# try:
#     c.execute("INSERT INTO result (id, name) VALUES ('yoshimoto', '今川義元')")
#     c.execute("INSERT INTO result (id, name) VALUES ('katsuyori', '武田勝頼')")
#     c.execute("INSERT INTO result (id, name) VALUES ('kanetsugu', '直江兼続')")
#     c.execute("INSERT INTO result (id, name) VALUES ('mitsunari', '石田三成')")
#     c.execute("INSERT INTO result (id, name) VALUES ('mitsuhide', '明智光秀')")
#     print("テーブル でーた が追加されました。")
# except sqlite3.OperationalError as e:
#     print("エラー:", e)


# try:
#     c.execute("CREATE TABLE result (id TEXT PRIMARY KEY, name TEXT, text1 TEXT, text2 TEXT)")
#     print("テーブル 'result' が作成されました。")
# except sqlite3.OperationalError as e:
#     print("エラー:", e)

conn.commit()
conn.close()
