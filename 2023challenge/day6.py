numbers = [1, "💖", 2, "🔥", 3, "⭐️", 4, "💖", 5, "🔥", 6, "⭐️", 7, "💖", 8,
           "🔥", 9, "⭐️", 10, "💖", 11, "🔥", 12, "⭐️", 13, "💖", 14, "🔥", 15, "⭐️", 16]

numnbers_filter = []
emoticon_filter = []

for character in numbers:
    if type(character) == int:
        numnbers_filter.append(character)
    else:
        emoticon_filter.append(character)

print(sum(numnbers_filter))
