# List of Hiragana, punctuation, and numbers
original_chars = [
    "あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ",
    "さ", "し", "す", "せ", "そ", "た", "ち", "つ", "て", "と",
    "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ",
    "ま", "み", "む", "め", "も", "や", "ゆ", "よ", "ら", "り",
    "る", "れ", "ろ", "わ", "を", "ん", "が", "ぎ", "ぐ", "げ", "ご",
    "ざ", "じ", "ず", "ぜ", "ぞ", "だ", "ぢ", "づ", "で", "ど",
    "ば", "び", "ぶ", "べ", "ぼ", "ぱ", "ぴ", "ぷ", "ぺ", "ぽ",
    "、", "。", "「", "」", "０", "１", "２", "３", "４", "５",
    "６", "７", "８", "９", "？", "！"
]

# List of complex Kanji and old-style Kanji for replacement
replacement_kanji = [
    "龍", "驫", "龗", "纛", "灘", "嚢", "麤", "龜", "鑑", "驪", 
    "顛", "纏", "驚", "覇", "鷹", "饕", "蠢", "籠", "龝", "龠", 
    "鼇", "鑾", "麓", "霜", "壹", "瀧", "馨", "螺", "蟬", "覯", 
    "顥", "颶", "驃", "驛", "驥", "麝", "鸞", "鸚", "鸛", "龕", 
    "龔", "齡", "龠", "齋", "龝", "驎", "驤", "靂", "鷇", "齲", 
    "龢", "齶", "鸛", "鬱", "鬮", "鬲", "齷", "齪", "齠", "麤", 
    "龝", "龠", "驄", "龡", "鑪", "龑", "龥", "齶", "齧", "龎", 
    "龏", "龖", "龜", "龘", "龔", "鱗", "鱣", "黌", "黶", "黷", 
    "災", "鸛", "驊", "鹹", "鸞", "龐", "齶", "鬱", "驫", "龗",
    "龜", "驚"
]

# Create dictionaries for mapping
hiragana_to_kanji = {original_chars[i]: replacement_kanji[i] for i in range(len(original_chars))}
kanji_to_hiragana = {replacement_kanji[i]: original_chars[i] for i in range(len(original_chars))}

def hiragana_to_replacement(text):
    # Convert Hiragana to corresponding complex Kanji
    return "".join([hiragana_to_kanji.get(char, char) for char in text])

def replacement_to_hiragana(text):
    # Convert complex Kanji back to corresponding Hiragana
    return "".join([kanji_to_hiragana.get(char, char) for char in text])

# Input text from user
user_input = input("Enter text: ")

# Convert Hiragana to complex Kanji
converted_text = hiragana_to_replacement(user_input)
print("Converted text:", converted_text)

# Convert complex Kanji back to Hiragana
restored_text = replacement_to_hiragana(converted_text)
print("Restored text:", restored_text)

# Wait for user input before ending
input("any sent me to finish: ")
print("End")
