# get_dialogue
取得したスクレイピングデータから対話データに変換する
## スクリプトの説明
### shapingArticle.py
[https://github.com/hyoiutu/scrapingSS](https://github.com/hyoiutu/scrapingSS)で
収集したデータをinput_style_hoge.txt, otput_style_hoge.txtという番号で対応付けられた対話データに変換する
### dialogue_integration.sh
input_style_hoge.txt, otput_style_hoge.txtというデータは対話の数だけファイル数が増えるので
これをinput.txtとoutput.txtに統合する
### process_unique.py
input.txt,output.txtに含まれる重複のある対話を取り除き，unique_input.txt, unique_output.txtに保存する

