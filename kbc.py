gk_questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B. New Delhi"
    },
    {
        "question": "2. Who is known as the Father of the Nation in India?",
        "options": ["A. Jawaharlal Nehru", "B. Subhas Chandra Bose",
                    "C. Mahatma Gandhi", "D. Sardar Patel"],
        "answer": "C. Mahatma Gandhi"
    },
    {
        "question": "3. What is the national animal of India?",
        "options": ["A. Lion", "B. Elephant", "C. Bengal Tiger", "D. Leopard"],
        "answer": "C. Bengal Tiger"
    },
    {
        "question": "4. When did India gain independence?",
        "options": ["A. 26 January 1950", "B. 15 August 1947",
                    "C. 2 October 1947", "D. 15 August 1950"],
        "answer": "B. 15 August 1947"
    },
    {
        "question": "5. Who was the first Prime Minister of India?",
        "options": ["A. Sardar Patel", "B. Rajendra Prasad",
                    "C. Jawaharlal Nehru", "D. Lal Bahadur Shastri"],
        "answer": "C. Jawaharlal Nehru"
    },
    {
        "question": "6. What is the national flower of India?",
        "options": ["A. Rose", "B. Sunflower", "C. Jasmine", "D. Lotus"],
        "answer": "D. Lotus"
    },
    {
        "question": "7. Which is the longest river flowing entirely within India?",
        "options": ["A. Yamuna", "B. Godavari", "C. Ganga", "D. Narmada"],
        "answer": "B. Godavari"
    },
    {
        "question": "8. Who wrote India's national anthem, Jana Gana Mana?",
        "options": ["A. Bankim Chandra Chattopadhyay",
                    "B. Rabindranath Tagore",
                    "C. Sarojini Naidu",
                    "D. Muhammad Iqbal"],
        "answer": "B. Rabindranath Tagore"
    },
    {
        "question": "9. Which is the largest Indian state by area?",
        "options": ["A. Madhya Pradesh", "B. Maharashtra",
                    "C. Rajasthan", "D. Uttar Pradesh"],
        "answer": "C. Rajasthan"
    },
    {
        "question": "10. Where is the headquarters of the Reserve Bank of India?",
        "options": ["A. New Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
        "answer": "B. Mumbai"
    }
]

score = 0
for question in gk_questions:
    print(question["question"])
    for option in question["options"]:
        print(option)
    user_answer = input("Enter your answer (A/B/C/D): ")
    if user_answer.upper() == question["answer"][0]:
        print("Correct!\n")
        score += 10
    else:
        print(f"Wrong! The correct answer is: {question['answer']}\n")
        score -= 5

print(f"Your final score is: {score}/100")