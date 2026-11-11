import sys


def make_analysis() -> None:
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return 
        
    valid_scores: list[int] = []

    for arg in sys.argv[1:]:
        try:    
            score: int = int(arg)
            if score < 0:
                raise ValueError()
            else:
                valid_scores.append(score)
        except Exception as e:
            print(f"Invalid parameter: '{arg}'")

    len_of_scores: int = len(valid_scores)
    if len_of_scores == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    total_score: int = sum(valid_scores)

    print(f"Scores processed: {valid_scores}")
    print(f"Total players: {len_of_scores}")
    print(f"Total score: {total_score}")
    print(f"Average score: {total_score / len_of_scores}")
    print(f"High score: {max(valid_scores)}")
    print(f"Low score: {min(valid_scores)}")
    print(f"Score range: {max(valid_scores) - min(valid_scores)}")


if __name__ == "__main__":
    make_analysis()