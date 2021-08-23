src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


more_then = [val for idx, val in enumerate(src) if src[idx - 1] < src[idx] and idx > 0]
print([a for a in src if src.count(a) == 1])
