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
    "６", "７", "８", "９", "？", "！","ぁ", "ぃ", "ぅ", "ぇ", "ぉ",
    "ゃ", "ゅ", "ょ", "ゎ", "っ"
]

# Corrected list of complex Kanji, old-style Kanji, and ghost characters for replacement
corrected_replacement_kanji = [
    "龍", "驫", "龗", "纛", "灘", "嚢", "麤", "龜", "鑑", "驪",
    "顛", "纏", "龤", "覇", "鷹", "饕", "蠢", "籠", "𠜎", "龥",
    "鼇", "鑾", "麓", "霜", "壹", "瀧", "馨", "螺", "蟬", "覯",
    "顥", "颶", "驃", "驛", "驥", "麝", "𡚴", "鸚", "𪚥", "龕",
    "龦", "齡", "𡈽", "齋", "𠮟", "驎", "驤", "靂", "鷇", "𥝱",
    "龢", "爨", "𤭯", "麵", "鬮", "鬲", "齷", "齪", "齠", "攀",
    "贔", "靉", "鑠", "鐵", "霽", "蠱", "纂", "饗", "躔", "黯",
    "鼈", "龏", "龖", "𨋢", "龘", "鱗", "鱣", "黌", "黶", "黷",
    "災", "驊", "鹹", "𦧟", "龠", "𧈢", "驍", "𨰾", "龞", "蝣",
    "鴦", "薔", "辶", "蠶", "剩", "餅", "様", "號", "欠"
]

# Create dictionaries for mapping
hiragana_to_kanji = {original_chars[i]: corrected_replacement_kanji[i] for i in range(len(original_chars))}
kanji_to_hiragana = {corrected_replacement_kanji[i]: original_chars[i] for i in range(len(original_chars))}

def hiragana_to_replacement(text):
    # Convert Hiragana to corresponding complex Kanji
    return "".join([hiragana_to_kanji.get(char, char) for char in text])

def replacement_to_hiragana(text):
    # Convert complex Kanji back to corresponding Hiragana
    return "".join([kanji_to_hiragana.get(char, char) for char in text])

# Infinite loop for continuous input and conversion
while True:
    # Input text from user
    user_input = input("Enter text: ")

    # Convert Hiragana to complex Kanji
    converted_text = hiragana_to_replacement(user_input)
    print("Converted text:", converted_text)

    # Convert complex Kanji back to Hiragana
    restored_text = replacement_to_hiragana(converted_text)
    print("Restored text:", restored_text)
