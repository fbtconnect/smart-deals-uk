def score_deal(current_price, past_price, urgency_text=""):
    score = 0
    if current_price < past_price * 0.75:
        score += 4
    if "only" in urgency_text.lower():
        score += 2
    return score
