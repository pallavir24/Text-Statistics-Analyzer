import os

def analyzing_text(text):
    if not text or not text.strip():
        raise ValueError("Input text cannot be empty.")
    
    words = text.split()
    characters = len(text)
    sentences = text.count('.') + text.count('!') + text.count('?')
    unique_words = set(w.lower() for w in words)
    
    # Word frequency dictionary
    freq = {}
    for word in words:
        w_clean = word.lower().strip('.,!?()[]{}"\'')
        if w_clean:
            freq[w_clean] = freq.get(w_clean, 0) + 1
            
    return {
        "characters": characters,
        "words": len(words),
        "sentences": max(1, sentences),
        "unique_terms": len(unique_words),
        "frequencies": freq
    }

def main():
    print("--- Text Statistics Analyzer ---")
    choice = input("1. Enter text manually\n2. Read from file\nChoice: ").strip()
    
    try:
        if choice == '1':
            text = input("Enter your text: ")
            stats = analyzing_text(text)
        elif choice == '2':
            filepath = input("Enter file path: ").strip()
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"The file '{filepath}' does not exist.")
            with open(filepath, 'r', encoding='utf-8') as f:
                stats = analyzing_text(f.read())
        else:
            print("Invalid choice.")
            return
            
        print("\n--- Results ---")
        for k, v in stats.items():
            if k != "frequencies":
                print(f"{k.capitalize()}: {v}")
        print("Top Frequencies:", sorted(stats["frequencies"].items(), key=lambda x: x[1], reverse=True)[:5])
        
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()