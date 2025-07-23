def timeInWords(h, m):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
             "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four",
             "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]

    if m == 0:
        return f"{words[h]} o' clock"
    elif m == 15:
        return f"quarter past {words[h]}"
    elif m == 30:
        return f"half past {words[h]}"
    elif m == 45:
        return f"quarter to {words[h+1]}"
    elif m < 30:
        return f"{words[m]} minute{'s' if m != 1 else ''} past {words[h]}"
    else:
        return f"{words[60 - m]} minute{'s' if 60 - m != 1 else ''} to {words[h + 1]}"
