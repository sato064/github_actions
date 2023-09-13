import re
from spellchecker import SpellChecker
spell = SpellChecker()
#キャメルケースになっているかチェックする場合
def is_cammelcase(target_string):
    #まずスネークケースになっていないかチェック
    if "_" in target_string:
        print(target_string + " ← アンダーバーが含まれています，スネークケースになっていませんか？")
        return False
    #次に最初の文字が大文字になっていないかチェック
    elif target_string[0].isupper():
        print(target_string + " ← 先頭の文字が大文字になっています")
        return False
    #最後に，大文字で正しく単語が区切られているかチェック

    else:
        splited_list = re.split('(?=[A-Z])', target_string)
        misspelled = spell.unknown(splited_list)
        if len(misspelled) > 0:
            print(target_string + " ← キャメルケースになっていますが，単語が正しく区切られていないか，スペルミスがあります")
            return False
        else:
            print("正常なキャメルケースになっています")
            return True


is_cammelcase("snake_case")
is_cammelcase("UpperCamelCase")
is_cammelcase("lowerCamelCasse")
is_cammelcase("lowerCamelId")