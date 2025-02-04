def reading_time(text):
    word_list = text.split()
    seconds = len(word_list) * 3.33
    minutes = seconds / 60
    return f"It would take approximately {seconds} seconds or {minutes:.2f} minutes to read this piece of text."
