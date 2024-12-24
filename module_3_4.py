def single_root_words(root_word, *other_words):
    same_words = []
    words = []
    word = root_word.lower()
    for w in other_words:
        w_lower = w.lower()
        if w_lower.count(word):
            same_words.append(w)
        else:
            words.append(w)
    return same_words, words


same_words, words = single_root_words("тр", "Трактор", "трамВай","треска", "трава", "друг", "ТРЕК")
print("Однокоренные:", same_words)
print("Не однокоренные:", words)

