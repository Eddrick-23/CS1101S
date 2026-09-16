def count_matches(char, pos):
    # your solution goes here
    # pa_words is predeclared for us
    
    matching_words = filter(lambda s: char_at(s, pos) == char, pa_words)
    return length(matching_words)
